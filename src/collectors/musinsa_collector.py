"""무신사 기술블로그 수집기"""

import feedparser
import re
from typing import List, Dict


class MusinsaCollector:
    """무신사 기술블로그 RSS 수집 (Medium)"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://medium.com/feed/musinsa-tech")
        self.max_results = config.get("max_results", 2)

    def _clean_html(self, html: str) -> str:
        """HTML 태그 제거"""
        clean = re.sub(r'<[^>]+>', '', html)
        clean = re.sub(r'\s+', ' ', clean)
        return clean.strip()

    def collect(self) -> List[Dict]:
        """RSS 피드에서 최신 글 수집"""
        results = []

        try:
            feed = feedparser.parse(self.rss_url)

            if not feed.entries:
                print(f"무신사 블로그에서 수집한 항목이 없습니다: {self.rss_url}")
                return results

            for entry in feed.entries[: self.max_results]:
                # Medium RSS는 content에 전체 내용이 들어있음
                content = entry.get("content", [{}])[0].get("value", "") if entry.get("content") else ""
                summary = entry.get("summary", "")

                # HTML 태그 제거
                clean_summary = self._clean_html(summary or content)[:500]

                results.append({
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": clean_summary,
                    "published": entry.get("published", ""),
                    "author": entry.get("author", "무신사"),
                })

        except Exception as e:
            print(f"무신사 블로그 수집 실패: {e}")

        return results


if __name__ == "__main__":
    print("=== 무신사 기술블로그 수집기 테스트 ===\n")

    collector = MusinsaCollector({"max_results": 3})
    articles = collector.collect()

    print(f"수집된 글 개수: {len(articles)}\n")

    for i, article in enumerate(articles, 1):
        print(f"[{i}] {article['title']}")
        print(f"    URL: {article['url']}")
        print(f"    저자: {article['author']}")
        print(f"    발행일: {article['published']}")
        print(f"    요약: {article['summary'][:100]}...")
        print()
