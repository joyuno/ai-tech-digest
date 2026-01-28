"""Hugging Face Blog 수집기"""

import feedparser
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class HuggingFaceCollector:
    """Hugging Face 공식 블로그 RSS 수집"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://huggingface.co/blog/feed.xml")
        self.max_results = config.get("max_results", 3)

    def collect(self) -> List[Dict]:
        """RSS 피드에서 최신 글 수집

        Returns:
            List[Dict]: 수집된 블로그 글 목록
            - title: 글 제목
            - url: 글 URL
            - summary: 요약 (최대 500자)
            - published: 발행일
            - author: 저자

        Raises:
            Exception: RSS 피드 파싱 실패 시
        """
        results = []

        try:
            logger.info(f"Fetching RSS feed from {self.rss_url}")
            feed = feedparser.parse(self.rss_url)

            # RSS 파싱 실패 확인
            if feed.bozo and not feed.entries:
                error_msg = f"RSS 피드 파싱 실패: {feed.bozo_exception if hasattr(feed, 'bozo_exception') else 'Unknown error'}"
                logger.error(error_msg)
                raise Exception(error_msg)

            if not feed.entries:
                logger.warning("RSS 피드에 항목이 없습니다")
                return []

            logger.info(f"Found {len(feed.entries)} entries, collecting up to {self.max_results}")

            for entry in feed.entries[: self.max_results]:
                # 요약 텍스트 정리
                summary = entry.get("summary", "")
                if summary:
                    # HTML 태그 제거 (feedparser가 자동으로 처리하지만 추가 정리)
                    summary = summary.strip()
                    # 500자 제한
                    summary = summary[:500]

                # 저자 정보 추출
                author = entry.get("author", "")
                if not author:
                    author = "Hugging Face"

                article = {
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("link", ""),
                    "summary": summary,
                    "published": entry.get("published", ""),
                    "author": author,
                }

                results.append(article)
                logger.debug(f"Collected: {article['title']}")

            logger.info(f"Successfully collected {len(results)} articles")
            return results

        except Exception as e:
            logger.error(f"Error collecting Hugging Face blog posts: {e}")
            raise


if __name__ == "__main__":
    # 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 테스트 실행
    print("=" * 80)
    print("Hugging Face Blog Collector Test")
    print("=" * 80)

    config = {
        "rss_url": "https://huggingface.co/blog/feed.xml",
        "max_results": 5
    }

    collector = HuggingFaceCollector(config)

    try:
        articles = collector.collect()

        print(f"\nCollected {len(articles)} articles:\n")

        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   Author: {article['author']}")
            print(f"   Published: {article['published']}")
            print(f"   Summary: {article['summary'][:100]}...")
            print()

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
