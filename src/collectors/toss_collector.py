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
        # TODO: 구현 필요
        results = []

        feed = feedparser.parse(self.rss_url)

        for entry in feed.entries[: self.max_results]:
            results.append({
                "title": entry.get("title", ""),
                "url": entry.get("link", ""),
                "summary": entry.get("summary", "")[:500],
                "published": entry.get("published", ""),
                "author": entry.get("author", "토스"),
            })

        return results
