"""Hugging Face Blog 수집기"""

import feedparser
from typing import List, Dict


class HuggingFaceCollector:
    """Hugging Face 공식 블로그 RSS 수집"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://huggingface.co/blog/feed.xml")
        self.max_results = config.get("max_results", 3)

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
                "author": entry.get("author", "Hugging Face"),
            })

        return results
