"""arXiv 논문 수집기"""

import arxiv
from datetime import datetime, timedelta
from typing import List, Dict


class ArxivCollector:
    """arXiv에서 최신 AI/ML 논문 수집"""

    def __init__(self, config: dict):
        self.categories = config.get("categories", ["cs.AI", "cs.LG"])
        self.max_results = config.get("max_results", 5)

    def collect(self) -> List[Dict]:
        """최근 24시간 논문 수집"""
        # TODO: 구현 필요
        results = []

        query = " OR ".join([f"cat:{cat}" for cat in self.categories])

        search = arxiv.Search(
            query=query,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        for paper in search.results():
            results.append({
                "title": paper.title,
                "url": paper.entry_id,
                "summary": paper.summary[:500],
                "authors": [a.name for a in paper.authors[:3]],
                "categories": paper.categories,
                "published": paper.published.isoformat(),
            })

        return results
