"""arXiv 논문 수집기 - Hugging Face Daily Papers (인기도 기반)"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict


class ArxivCollector:
    """Hugging Face Daily Papers에서 인기 AI/ML 논문 수집 (upvotes 기반)

    Hugging Face Daily Papers는 arXiv 논문 중 커뮤니티에서 인기 있는 논문을
    upvotes 기준으로 정렬하여 제공합니다.
    """

    DAILY_PAPERS_API = "https://huggingface.co/api/daily_papers"

    def __init__(self, config: dict):
        self.max_results = config.get("max_results", 5)
        self.timeout = config.get("timeout", 15)

    def collect(self) -> List[Dict]:
        """인기도 순으로 논문 수집 (upvotes 기반)"""
        results = []

        try:
            print("  📊 Hugging Face Daily Papers에서 인기 논문 수집 중...")

            response = requests.get(
                self.DAILY_PAPERS_API,
                timeout=self.timeout,
                headers={"Accept": "application/json"}
            )
            response.raise_for_status()
            papers = response.json()

            if not papers:
                print("  ⚠️ Daily Papers에서 논문을 찾을 수 없습니다")
                return []

            # upvotes 기준으로 정렬 (이미 정렬되어 있지만 확실하게)
            papers_sorted = sorted(
                papers,
                key=lambda x: x.get("paper", {}).get("upvotes", 0),
                reverse=True
            )

            for paper_data in papers_sorted[:self.max_results]:
                paper = paper_data.get("paper", {})

                # arXiv ID에서 URL 생성
                arxiv_id = paper.get("id", "")
                arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""

                # 요약 정리
                summary = paper.get("summary", "")
                if summary:
                    summary = summary.replace('\n', ' ').strip()[:500]

                # upvotes 수
                upvotes = paper.get("upvotes", 0)

                results.append({
                    "title": paper.get("title", "").strip(),
                    "url": arxiv_url,
                    "summary": summary,
                    "authors": paper.get("authors", [])[:3],
                    "published": paper.get("publishedAt", ""),
                    "upvotes": upvotes,
                    "source": "arxiv",
                })

            print(f"  ✓ {len(results)}개 인기 논문 수집 (upvotes 기준)")

        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ API 요청 실패: {e}")
            return self._fallback_collect()
        except Exception as e:
            print(f"  ⚠️ arXiv 수집 실패: {e}")
            return []

        return results

    def _fallback_collect(self) -> List[Dict]:
        """API 실패 시 기본 arXiv 검색으로 폴백"""
        try:
            import arxiv
            from datetime import timezone

            print("  🔄 기본 arXiv 검색으로 폴백...")

            query = "cat:cs.AI OR cat:cs.LG OR cat:cs.CL"
            search = arxiv.Search(
                query=query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )

            results = []
            for paper in search.results():
                summary = paper.summary.replace('\n', ' ').strip()[:500]
                results.append({
                    "title": paper.title.strip(),
                    "url": paper.entry_id,
                    "summary": summary,
                    "authors": [a.name for a in paper.authors[:3]],
                    "published": paper.published.isoformat(),
                    "upvotes": 0,
                    "source": "arxiv",
                })

            return results
        except Exception as e:
            print(f"  ⚠️ 폴백도 실패: {e}")
            return []


if __name__ == "__main__":
    """테스트 코드"""
    print("=== arXiv Collector 테스트 (인기도 기반) ===\n")

    config = {"max_results": 5}
    collector = ArxivCollector(config)
    papers = collector.collect()

    print(f"\n총 {len(papers)}개 논문 수집\n")
    print("-" * 80)

    for i, paper in enumerate(papers, 1):
        upvotes = paper.get('upvotes', 0)
        print(f"\n[{i}] 🔥 {upvotes} upvotes")
        print(f"제목: {paper['title']}")
        print(f"URL: {paper['url']}")
        print(f"저자: {paper.get('authors', [])}")
        print(f"요약: {paper['summary'][:100]}...")
        print("-" * 80)
