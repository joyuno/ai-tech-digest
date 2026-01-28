"""토스 기술블로그 수집기"""

import feedparser
from typing import List, Dict


class TossCollector:
    """토스 기술블로그 RSS 수집"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://toss.tech/rss.xml")
        self.max_results = config.get("max_results", 2)

    def collect(self) -> List[Dict]:
        """RSS 피드에서 최신 글 수집"""
        results = []

        try:
            feed = feedparser.parse(self.rss_url)

            if not feed.entries:
                print(f"토스 블로그에서 수집한 항목이 없습니다: {self.rss_url}")
                return results

            for entry in feed.entries[: self.max_results]:
                results.append({
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:500],
                    "published": entry.get("published", ""),
                    "author": entry.get("author", "토스"),
                })

        except Exception as e:
            print(f"토스 블로그 수집 실패: {e}")

        return results


if __name__ == "__main__":
    print("=== 토스 기술블로그 수집기 테스트 ===\n")

    collector = TossCollector({"max_results": 3})
    articles = collector.collect()

    print(f"수집된 글 개수: {len(articles)}\n")

    for i, article in enumerate(articles, 1):
        print(f"[{i}] {article['title']}")
        print(f"    URL: {article['url']}")
        print(f"    저자: {article['author']}")
        print(f"    발행일: {article['published']}")
        print(f"    요약: {article['summary'][:100]}...")
        print()
