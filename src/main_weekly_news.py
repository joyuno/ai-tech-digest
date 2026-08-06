#!/usr/bin/env python3
"""주간 기술뉴스 다이제스트 진입점.

흐름:
  1. GeekNews Weekly 최신호 자동 탐지 (/weekly → /weekly/YYYYWW)
  2. '이번 주 주요 뉴스' 각 항목(제목+요약) 추출
  3. 이미 발행한 이슈면 skip (중복 방지) — 갱신 안 됐을 때 재작성 X
  4. deepseek-v4-flash 로 각 뉴스 5줄 핵심 요약 + 이번 주 흐름 intro
  5. 메인 블로그 _posts/ 에 발행

cron: 매주 월요일 오후 (GeekNews Weekly 는 월요일 아침 발행)

dry-run: --dry-run 으로 발행 없이 마크다운 stdout.
"""
import argparse
import importlib.util
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, str(Path(__file__).parent / rel))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _post_date(period_end: str) -> str:
    """이슈 발행일(월요일) = 기간 종료(일요일) + 1일. 없으면 오늘."""
    if period_end:
        try:
            return (datetime.strptime(period_end, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return datetime.now().strftime("%Y-%m-%d")


def _post_exists(repo: str, branch: str, path: str, token: str) -> bool:
    if not token:
        return False
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    try:
        r = requests.get(url, headers={"Authorization": f"token {token}"},
                         params={"ref": branch}, timeout=15)
        return r.status_code == 200
    except Exception:
        return False


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--weekly-id", type=str, default="", help="weekly 이슈 id 수동 지정")
    parser.add_argument("--max-items", type=int,
                        default=int(os.environ.get("MAX_ITEMS") or "35"))
    parser.add_argument("--force", action="store_true", help="이미 발행됐어도 재발행")
    args = parser.parse_args(argv)

    if args.weekly_id:
        os.environ["WEEKLY_ID"] = args.weekly_id

    col_mod = _load("gnw", "collectors/geeknews_weekly_collector.py")
    smr_mod = _load("wns", "processors/weekly_news_summarizer.py")

    print("=" * 60)
    print("📡 [1/3] GeekNews Weekly 최신호 탐지")
    data = col_mod.GeekNewsWeeklyCollector().collect()
    items = data.get("items", [])
    if not items:
        print("ℹ️ 주요 뉴스 0건 — 발행 skip. 정상 종료.")
        return 0

    date = _post_date(data.get("period_end", ""))
    repo = os.environ.get("BLOG_REPO", "joyuno/joyuno.github.io")
    branch = os.environ.get("BLOG_BRANCH", "main")

    # 3) 중복 방지 — 이 이슈 글이 이미 있으면 skip
    from publishers.weekly_news_publisher import WeeklyNewsPublisher
    gh_token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN", "")
    publisher = WeeklyNewsPublisher(gh_token=gh_token, repo=repo, branch=branch)
    path = publisher.post_path(date)
    if not args.dry_run and not args.force and _post_exists(repo, branch, path, gh_token):
        print(f"ℹ️ 이미 발행된 이슈({data['weekly_id']}, {path}) — 갱신 없음, skip. 정상 종료.")
        return 0

    items = items[: args.max_items]
    print(f"\n✍️ [2/3] 핵심 5줄 요약 생성 ({len(items)}건, deepseek-v4-flash)")
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("❌ OPENROUTER_API_KEY 없음 — 종료")
        return 1
    digest = smr_mod.WeeklyNewsSummarizer(api_key).summarize(items)
    out = {"weekly_id": data["weekly_id"], "intro": digest["intro"], "items": digest["items"]}

    print(f"\n📤 [3/3] {'dry-run' if args.dry_run else '발행'} (date={date})")
    if args.dry_run:
        print("\n" + "=" * 60 + "\n  RENDERED MARKDOWN\n" + "=" * 60)
        print(publisher.render(out, date))
        return 0
    return 0 if publisher.publish_weekly(out, date) else 2


if __name__ == "__main__":
    sys.exit(main())
