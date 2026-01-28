"""Hugging Face 수집기 - Daily Papers (인기도 기반)"""

import requests
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class HuggingFaceCollector:
    """Hugging Face Daily Papers에서 인기 논문 수집 (upvotes 기반)

    arXiv collector와 다른 날짜 범위의 논문을 가져오거나,
    다른 카테고리의 인기 논문을 수집합니다.
    """

    # Hugging Face Papers API (최근 인기 논문)
    PAPERS_API = "https://huggingface.co/api/papers"

    def __init__(self, config: dict):
        self.max_results = config.get("max_results", 3)
        self.timeout = config.get("timeout", 15)

    def collect(self) -> List[Dict]:
        """인기도 순으로 논문 수집 (upvotes 기반)"""
        results = []

        try:
            print("  📊 Hugging Face Papers에서 인기 논문 수집 중...")

            # Papers API에서 최근 인기 논문 조회
            response = requests.get(
                self.PAPERS_API,
                params={"limit": self.max_results * 2},  # 여유분
                timeout=self.timeout,
                headers={"Accept": "application/json"}
            )
            response.raise_for_status()
            papers = response.json()

            if not papers:
                print("  ⚠️ Papers에서 논문을 찾을 수 없습니다")
                return self._fallback_rss()

            # upvotes 기준으로 정렬
            papers_sorted = sorted(
                papers,
                key=lambda x: x.get("upvotes", 0),
                reverse=True
            )

            for paper in papers_sorted[:self.max_results]:
                # arXiv ID에서 URL 생성
                paper_id = paper.get("id", "")
                arxiv_url = f"https://arxiv.org/abs/{paper_id}" if paper_id else ""
                hf_url = f"https://huggingface.co/papers/{paper_id}" if paper_id else ""

                # 요약 정리
                summary = paper.get("summary", "")
                if summary:
                    summary = summary.replace('\n', ' ').strip()[:500]

                # upvotes 수
                upvotes = paper.get("upvotes", 0)

                # 저자 정보
                authors = paper.get("authors", [])
                if isinstance(authors, list) and authors:
                    if isinstance(authors[0], dict):
                        author_names = [a.get("name", "") for a in authors[:3]]
                    else:
                        author_names = authors[:3]
                else:
                    author_names = []

                results.append({
                    "title": paper.get("title", "").strip(),
                    "url": hf_url or arxiv_url,
                    "summary": summary,
                    "author": ", ".join(author_names) if author_names else "Hugging Face",
                    "published": paper.get("publishedAt", ""),
                    "upvotes": upvotes,
                    "source": "huggingface",
                })

            print(f"  ✓ {len(results)}개 인기 논문 수집 (upvotes 기준)")

        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ API 요청 실패: {e}")
            return self._fallback_rss()
        except Exception as e:
            print(f"  ⚠️ HuggingFace 수집 실패: {e}")
            logger.error(f"Error: {e}")
            return []

        return results

    def _fallback_rss(self) -> List[Dict]:
        """API 실패 시 블로그 RSS로 폴백"""
        import feedparser

        print("  🔄 블로그 RSS로 폴백...")

        try:
            feed = feedparser.parse("https://huggingface.co/blog/feed.xml")

            if not feed.entries:
                return []

            results = []
            for entry in feed.entries[:self.max_results]:
                summary = entry.get("summary", "").strip()[:500]
                results.append({
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("link", ""),
                    "summary": summary,
                    "author": entry.get("author", "Hugging Face"),
                    "published": entry.get("published", ""),
                    "upvotes": 0,
                    "source": "huggingface",
                })

            return results
        except Exception as e:
            print(f"  ⚠️ RSS 폴백도 실패: {e}")
            return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print("=" * 80)
    print("Hugging Face Collector 테스트 (인기도 기반)")
    print("=" * 80)

    config = {"max_results": 5}
    collector = HuggingFaceCollector(config)

    try:
        articles = collector.collect()
        print(f"\n수집된 논문: {len(articles)}개\n")

        for i, article in enumerate(articles, 1):
            upvotes = article.get('upvotes', 0)
            print(f"{i}. 🔥 {upvotes} upvotes")
            print(f"   제목: {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   저자: {article['author']}")
            print(f"   요약: {article['summary'][:80]}...")
            print()

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
