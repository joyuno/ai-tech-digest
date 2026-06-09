#!/usr/bin/env python3
"""주간 AI/ML 논문 다이제스트 진입점.

흐름:
  1. GeekNews 에서 이번 주 글 자동 탐지 (또는 GEEKNEWS_TOPIC_ID 수동)
  2. 추출된 arXiv ID 로 정식 메타 fetch
  3. deepseek/deepseek-v4-flash 단일 모델로 본문급 한국어 해설 생성
  4. gh-pages 브랜치 _posts/ 에 발행

cron: 일요일 23:00 KST = 일요일 14:00 UTC (.github/workflows/weekly-papers.yml)

dry-run: --dry-run 옵션으로 발행 없이 마크다운만 stdout 출력.
"""
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# collectors/__init__.py 의 무거운 의존성(feedparser 등) 우회 — 모듈 직접 import
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util


def _load(name: str, rel_path: str):
    spec = importlib.util.spec_from_file_location(
        name, str(Path(__file__).parent / rel_path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="발행 없이 마크다운만 stdout 출력")
    parser.add_argument("--topic-id", type=str, default="",
                        help="GeekNews topic id 수동 지정 (자동 탐지 우회)")
    parser.add_argument("--output-json", type=str, default="output/weekly_papers.json",
                        help="중간 결과 JSON 저장 경로 (Actions artifact 용)")
    args = parser.parse_args(argv)

    if args.topic_id:
        os.environ["GEEKNEWS_TOPIC_ID"] = args.topic_id

    # 1) 모듈 로드
    gnc_mod = _load("gnc", "collectors/geeknews_papers_collector.py")
    am_mod = _load("am", "collectors/arxiv_metadata.py")
    smr_mod = _load("smr", "processors/paper_digest_summarizer.py")

    # 2) GeekNews 탐지 + arXiv ID 추출
    print("=" * 60)
    print("📡 [1/4] GeekNews 주간 글 탐지")
    geek = gnc_mod.GeekNewsPapersCollector().collect()
    if not geek["arxiv_ids"]:
        print("❌ 이번 주 글 또는 arXiv ID 0건 — 종료")
        return 1

    # 3) arXiv 메타 fetch
    print(f"\n📚 [2/4] arXiv 메타 fetch ({len(geek['arxiv_ids'])}건)")
    papers = am_mod.fetch_papers_by_ids(geek["arxiv_ids"])
    if not papers:
        print("❌ arXiv 메타 0건 — 종료")
        return 1
    success_ratio = len(papers) / len(geek["arxiv_ids"])
    if success_ratio < 0.7:
        print(f"⚠️ arXiv 성공률 {success_ratio:.0%} — 30% 이상 실패, 진행은 하되 카카오 알림 권장")

    # 4) 본문급 한국어 해설 생성
    print(f"\n✍️ [3/4] 본문급 해설 생성 (deepseek/deepseek-v4-flash)")
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("❌ OPENROUTER_API_KEY 환경변수 없음 — 종료")
        return 1
    summarizer = smr_mod.PaperDigestSummarizer(api_key)
    digest = summarizer.summarize(papers)

    # 데이터 통합
    data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "geeknews_topic_id": geek["topic_id"],
        "geeknews_url": geek["topic_url"],
        "geeknews_title": geek["topic_title"],
        "intro": digest.get("intro", ""),
        "papers": digest.get("papers", []),
    }

    # 중간 결과 JSON 저장 (Actions artifact)
    out_path = Path(args.output_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  💾 중간 결과 저장: {out_path}")

    # 5) 발행 또는 dry-run
    print(f"\n📤 [4/4] {'dry-run 마크다운 출력' if args.dry_run else '발행'}")
    from publishers.weekly_papers_publisher import WeeklyPapersPublisher

    gh_token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("BLOG_REPO", "joyuno/joyuno.github.io")
    branch = os.environ.get("BLOG_BRANCH", "gh-pages")
    publisher = WeeklyPapersPublisher(gh_token=gh_token, repo=repo, branch=branch)

    if args.dry_run:
        md = publisher.render_only(data, date=data["date"])
        print("\n" + "=" * 60 + "\n  RENDERED MARKDOWN  \n" + "=" * 60)
        print(md)
        print("=" * 60)
        return 0

    ok = publisher.publish_weekly(data)
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
