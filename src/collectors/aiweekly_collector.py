"""AI Weekly 뉴스레터 수집기"""

import feedparser
from typing import List, Dict


class AIWeeklyCollector:
    """AI Weekly RSS 수집"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://aiweekly.co/issues.rss")
        self.max_results = config.get("max_results", 1)

    def collect(self) -> List[Dict]:
        """RSS 피드에서 최신 뉴스레터 수집"""
        # TODO: 구현 필요
        results = []

        try:
            feed = feedparser.parse(self.rss_url)

            for entry in feed.entries[: self.max_results]:
                results.append({
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:500],
                    "published": entry.get("published", ""),
                })
        except Exception as e:
            print(f"AI Weekly 수집 실패: {e}")

        return results
