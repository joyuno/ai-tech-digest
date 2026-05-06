#!/usr/bin/env python3
"""
AI Tech Digest - Main Entry Point

매일 AI 기술 트렌드를 수집, 요약하여 카카오톡 알림 및 Jekyll 블로그 포스팅
"""

import os
import sys
import json
import yaml
from datetime import datetime
from pathlib import Path

# 모듈 경로 추가
sys.path.insert(0, str(Path(__file__).parent))

# Collectors
from collectors.arxiv_collector import ArxivCollector
from collectors.huggingface_collector import HuggingFaceCollector
from collectors.twitter_collector import TwitterCollector
from collectors.toss_collector import TossCollector
from collectors.musinsa_collector import MusinsaCollector
from collectors.github_trending_collector import GitHubTrendingCollector
from collectors.aiweekly_collector import AIWeeklyCollector

# Processors
from processors.ontology_classifier import OntologyClassifier
from processors.openrouter_summarizer import OpenRouterSummarizer

# Publishers
from publishers.kakao_notifier import KakaoNotifier
from publishers.jekyll_publisher import JekyllPublisher

# Utils
from utils.dedup_tracker import DedupTracker

# 중복 방지 대상 소스 (최신순 정렬 소스들)
DEDUP_SOURCES = ["toss", "musinsa", "aiweekly"]


def load_config():
    """설정 파일 로드"""
    config_dir = Path(__file__).parent.parent / "config"

    with open(config_dir / "sources.yaml", "r", encoding="utf-8") as f:
        sources_config = yaml.safe_load(f)

    with open(config_dir / "ontology.yaml", "r", encoding="utf-8") as f:
        ontology_config = yaml.safe_load(f)

    return sources_config, ontology_config


def collect_all_sources(sources_config: dict, dedup_tracker: DedupTracker = None) -> dict:
    """모든 소스에서 데이터 수집"""
    collectors = {
        "arxiv": ArxivCollector,
        "huggingface": HuggingFaceCollector,
        "twitter": TwitterCollector,
        "toss": TossCollector,
        "musinsa": MusinsaCollector,
        "github_trending": GitHubTrendingCollector,
        "aiweekly": AIWeeklyCollector,
    }

    collected_data = {}
    total_items = 0

    for source_name, collector_class in collectors.items():
        source_cfg = sources_config["sources"].get(source_name, {})
        if source_cfg.get("enabled", False):
            print(f"📥 수집 중: {source_name}")
            try:
                collector = collector_class(source_cfg)
                items = collector.collect()

                # 중복 방지 대상 소스는 필터링
                if dedup_tracker and source_name in DEDUP_SOURCES:
                    original_count = len(items)
                    items = dedup_tracker.filter_new_items(source_name, items)
                    if original_count > len(items):
                        print(f"   🔄 중복 제거: {original_count - len(items)}개 스킵")

                    # 새 항목 기록
                    if items:
                        urls = [item.get("url", "") for item in items if item.get("url")]
                        dedup_tracker.mark_collected(source_name, urls)

                collected_data[source_name] = items
                total_items += len(items)
                print(f"   ✓ {len(items)}개 수집 완료")
            except Exception as e:
                print(f"   ⚠️ 수집 실패: {e}")
                collected_data[source_name] = []
        else:
            print(f"⏭️ 스킵: {source_name} (비활성화)")

    print(f"\n📊 총 {total_items}개 항목 수집")
    return collected_data


def save_output(data: dict, output_dir: Path, filename: str):
    """결과를 파일로 저장"""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    print(f"💾 저장됨: {output_path}")


def main():
    """메인 실행 함수"""
    start_time = datetime.now()
    today = start_time.strftime('%Y-%m-%d')

    print("=" * 60)
    print("🚀 AI Tech Digest 시작")
    print(f"📅 날짜: {today}")
    print(f"⏰ 시작 시간: {start_time.strftime('%H:%M:%S')}")
    print("=" * 60)

    # 출력 디렉토리 설정
    output_dir = Path(__file__).parent.parent / "output" / today

    try:
        # 1. 설정 로드
        print("\n📂 설정 로드...")
        sources_config, ontology_config = load_config()
        print("   ✓ 설정 로드 완료")

        # 2. 데이터 수집
        print("\n" + "=" * 60)
        print("📥 데이터 수집")
        print("=" * 60)

        # 중복 방지 트래커 초기화
        gh_token = os.environ.get("GH_PAT")
        dedup_tracker = None
        if gh_token:
            jekyll_config = sources_config.get("output", {}).get("jekyll", {})
            dedup_tracker = DedupTracker(
                gh_token=gh_token,
                repo=jekyll_config.get("repo", "joyuno/ai-tech-digest"),
                branch=jekyll_config.get("branch", "gh-pages")
            )
            print("  🔄 중복 방지 트래커 활성화")

        collected_data = collect_all_sources(sources_config, dedup_tracker)

        # 중복 방지 이력 저장
        if dedup_tracker:
            dedup_tracker.save()

        # 수집 결과 저장
        save_output(collected_data, output_dir, "collected_data.json")

        # 수집된 데이터가 없으면 종료
        total_items = sum(len(items) for items in collected_data.values())
        if total_items == 0:
            print("\n⚠️ 수집된 데이터가 없습니다. 종료합니다.")
            return

        # 3. 온톨로지 분류
        print("\n" + "=" * 60)
        print("🏷️ 온톨로지 분류")
        print("=" * 60)
        classifier = OntologyClassifier(ontology_config)
        classified_data = classifier.classify_all(collected_data)

        # 분류 통계
        for source, items in classified_data.items():
            categorized = sum(1 for item in items if item.get("categories"))
            print(f"   {source}: {len(items)}개 중 {categorized}개 분류됨")

        # 상위 키워드 추출
        top_keywords = classifier.get_top_keywords(classified_data, top_n=10)
        print(f"\n   🔑 상위 키워드: {', '.join(top_keywords[:5])}")

        # 4. AI 요약 (OpenRouter + grok-4.1-fast)
        print("\n" + "=" * 60)
        print("✨ AI 요약 생성 (OpenRouter)")
        print("=" * 60)

        summary_model = (
            sources_config.get("openrouter", {}).get("model")
            or sources_config.get("gemini", {}).get("model")  # 구설정 호환
            or "x-ai/grok-4.1-fast"
        )
        print(f"   모델: {summary_model}")

        summarizer = OpenRouterSummarizer(
            api_key=os.environ.get("OPENROUTER_API_KEY"),
            model=summary_model,
        )
        summary = summarizer.summarize(classified_data)
        summary["top_keywords"] = top_keywords

        # 요약 결과 저장
        save_output(summary, output_dir, "summary.json")

        # 5. 카카오톡 알림
        print("\n" + "=" * 60)
        print("📱 카카오톡 알림")
        print("=" * 60)

        kakao_enabled = bool(os.environ.get("KAKAO_REST_API_KEY"))
        if kakao_enabled:
            kakao = KakaoNotifier(
                rest_api_key=os.environ.get("KAKAO_REST_API_KEY"),
                refresh_token=os.environ.get("KAKAO_REFRESH_TOKEN"),
                client_secret=os.environ.get("KAKAO_CLIENT_SECRET")
            )
            if kakao.send(summary):
                print("   ✓ 카카오톡 발송 성공")
            else:
                print("   ⚠️ 카카오톡 발송 실패")
        else:
            print("   ⏭️ 스킵 (API 키 없음)")

        # 6. Jekyll 블로그 포스팅
        print("\n" + "=" * 60)
        print("📝 Jekyll 블로그 포스팅")
        print("=" * 60)

        gh_token = os.environ.get("GH_PAT")
        if gh_token:
            jekyll_config = sources_config.get("output", {}).get("jekyll", {})
            jekyll = JekyllPublisher(
                gh_token=gh_token,
                repo=jekyll_config.get("repo", "joyuno/ai-tech-digest"),
                branch=jekyll_config.get("branch", "gh-pages")
            )
            if jekyll.publish(summary):
                print("   ✓ Jekyll 포스팅 성공")
            else:
                print("   ⚠️ Jekyll 포스팅 실패")
        else:
            print("   ⏭️ 스킵 (GitHub 토큰 없음)")

        # 완료
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        print("\n" + "=" * 60)
        print("✅ AI Tech Digest 완료!")
        print(f"⏱️ 소요 시간: {duration:.1f}초")
        print(f"📊 처리 항목: {total_items}개")
        print(f"📁 출력 디렉토리: {output_dir}")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
