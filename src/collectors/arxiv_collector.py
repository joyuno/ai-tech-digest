"""arXiv 논문 수집기"""

import arxiv
from datetime import datetime, timedelta, timezone
from typing import List, Dict


class ArxivCollector:
    """arXiv에서 최신 AI/ML 논문 수집"""

    def __init__(self, config: dict):
        self.categories = config.get("categories", ["cs.AI", "cs.LG", "cs.CL"])
        self.max_results = config.get("max_results", 5)
        self.hours_ago = config.get("hours_ago", 24)

    def collect(self) -> List[Dict]:
        """최근 24시간 논문 수집"""
        results = []
        cutoff_time = datetime.now(timezone.utc) - timedelta(hours=self.hours_ago)

        try:
            # 카테고리별 쿼리 구성 (cs.AI OR cs.LG OR cs.CL)
            query = " OR ".join([f"cat:{cat}" for cat in self.categories])

            # arxiv.Search로 검색
            search = arxiv.Search(
                query=query,
                max_results=self.max_results * 2,  # 필터링 고려해서 여유있게
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )

            # 결과 수집 및 필터링
            for paper in search.results():
                # timezone-aware 비교를 위해 published도 UTC로 변환
                published_time = paper.published
                if published_time.tzinfo is None:
                    published_time = published_time.replace(tzinfo=timezone.utc)

                # 최근 24시간 이내 논문만 필터링
                if published_time >= cutoff_time:
                    # 요약 정리 (500자 제한, 줄바꿈 제거)
                    summary = paper.summary.replace('\n', ' ').strip()
                    if len(summary) > 500:
                        summary = summary[:497] + "..."

                    results.append({
                        "title": paper.title.strip(),
                        "url": paper.entry_id,
                        "summary": summary,
                        "authors": [a.name for a in paper.authors[:3]],
                        "categories": paper.categories,
                        "published": paper.published.isoformat(),
                    })

                # max_results 도달 시 중단
                if len(results) >= self.max_results:
                    break

        except Exception as e:
            print(f"arXiv 수집 실패: {e}")
            return []

        return results


if __name__ == "__main__":
    """테스트 코드"""
    print("=== arXiv Collector 테스트 ===\n")

    # 설정
    config = {
        "categories": ["cs.AI", "cs.LG", "cs.CL"],
        "max_results": 5,
        "hours_ago": 24,
    }

    # 수집기 생성 및 실행
    collector = ArxivCollector(config)
    papers = collector.collect()

    # 결과 출력
    print(f"총 {len(papers)}개 논문 수집\n")
    print("-" * 80)

    for i, paper in enumerate(papers, 1):
        print(f"\n[{i}] {paper['title']}")
        print(f"URL: {paper['url']}")
        print(f"저자: {', '.join(paper['authors'])}")
        print(f"카테고리: {', '.join(paper['categories'])}")
        print(f"발행일: {paper['published']}")
        print(f"요약: {paper['summary'][:100]}...")
        print("-" * 80)
