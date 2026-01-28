#!/usr/bin/env python3
"""
AI Tech Digest - Main Entry Point

매일 AI 기술 트렌드를 수집, 요약하여 카카오톡 알림 및 Jekyll 블로그 포스팅
"""

import os
import yaml
from datetime import datetime
from pathlib import Path

# Collectors
from collectors.arxiv_collector import ArxivCollector
from collectors.huggingface_collector import HuggingFaceCollector
from collectors.twitter_collector import TwitterCollector
from collectors.toss_collector import TossCollector
from collectors.github_trending_collector import GitHubTrendingCollector
from collectors.aiweekly_collector import AIWeeklyCollector

# Processors
from processors.ontology_classifier import OntologyClassifier
from processors.gemini_summarizer import GeminiSummarizer

# Publishers
from publishers.kakao_notifier import KakaoNotifier
from publishers.jekyll_publisher import JekyllPublisher


def load_config():
    """설정 파일 로드"""
    config_dir = Path(__file__).parent.parent / "config"

    with open(config_dir / "sources.yaml", "r", encoding="utf-8") as f:
        sources_config = yaml.safe_load(f)

    with open(config_dir / "ontology.yaml", "r", encoding="utf-8") as f:
        ontology_config = yaml.safe_load(f)

    return sources_config, ontology_config


def collect_all_sources(sources_config: dict) -> dict:
    """모든 소스에서 데이터 수집"""
    collectors = {
        "arxiv": ArxivCollector,
        "huggingface": HuggingFaceCollector,
        "twitter": TwitterCollector,
        "toss": TossCollector,
        "github_trending": GitHubTrendingCollector,
        "aiweekly": AIWeeklyCollector,
    }

    collected_data = {}

    for source_name, collector_class in collectors.items():
        source_cfg = sources_config["sources"].get(source_name, {})
        if source_cfg.get("enabled", False):
            print(f"📥 수집 중: {source_name}")
            try:
                collector = collector_class(source_cfg)
                collected_data[source_name] = collector.collect()
            except Exception as e:
                print(f"⚠️ {source_name} 수집 실패: {e}")
                collected_data[source_name] = []

    return collected_data


def main():
    """메인 실행 함수"""
    print("🚀 AI Tech Digest 시작")
    print(f"📅 날짜: {datetime.now().strftime('%Y-%m-%d')}")
    print("-" * 50)

    # 1. 설정 로드
    sources_config, ontology_config = load_config()

    # 2. 데이터 수집
    print("\n📥 데이터 수집 시작...")
    collected_data = collect_all_sources(sources_config)

    # 3. 온톨로지 분류
    print("\n🏷️ 온톨로지 분류...")
    classifier = OntologyClassifier(ontology_config)
    classified_data = classifier.classify_all(collected_data)

    # 4. Gemini 요약
    print("\n✨ AI 요약 생성...")
    summarizer = GeminiSummarizer(
        api_key=os.environ.get("GEMINI_API_KEY"),
        model=sources_config["gemini"]["model"]
    )
    summary = summarizer.summarize(classified_data)

    # 5. 카카오톡 알림
    print("\n📱 카카오톡 알림 발송...")
    kakao = KakaoNotifier(
        rest_api_key=os.environ.get("KAKAO_REST_API_KEY"),
        refresh_token=os.environ.get("KAKAO_REFRESH_TOKEN"),
        client_secret=os.environ.get("KAKAO_CLIENT_SECRET")
    )
    kakao.send(summary)

    # 6. Jekyll 블로그 포스팅
    print("\n📝 Jekyll 블로그 포스팅...")
    jekyll = JekyllPublisher(
        gh_token=os.environ.get("GH_PAT"),
        repo=sources_config["output"]["jekyll"]["repo"]
    )
    jekyll.publish(summary)

    print("\n✅ AI Tech Digest 완료!")


if __name__ == "__main__":
    main()
