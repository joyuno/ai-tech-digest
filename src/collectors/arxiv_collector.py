"""arXiv 논문 수집기 - Hugging Face Daily Papers (인기도 기반) + enrichment."""

import os
import re
import time
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# venue tier 매핑 — abstract / paper meta 의 venue 키워드
TIER1_VENUES = (
    "NeurIPS", "NIPS", "ICML", "ICLR", "CVPR", "ICCV", "ECCV",
    "ACL", "EMNLP", "NAACL", "SIGGRAPH", "Nature", "Science",
)
TIER2_VENUES = (
    "AAAI", "IJCAI", "EACL", "COLING", "INTERSPEECH",
    "WACV", "BMVC", "UAI", "KDD", "WWW",
)


def _classify_venue(text: str) -> str:
    if not text:
        return ""
    t = " " + text.lower() + " "
    # submitted/under-review 가 먼저 — "Submitted to ICLR" 가 tier1 으로 잘못 분류되는 거 회피
    if "submitted to" in t or "under review" in t:
        return "submitted"
    for v in TIER1_VENUES:
        if re.search(rf"(?<![a-z]){re.escape(v.lower())}(?![a-z])", t):
            return "tier1"
    for v in TIER2_VENUES:
        if re.search(rf"(?<![a-z]){re.escape(v.lower())}(?![a-z])", t):
            return "tier2"
    return ""


GH_REPO_RE = re.compile(r"github\.com/([\w.-]+/[\w.-]+?)(?=[\s)\],.;]|$)", re.IGNORECASE)


def _extract_github_repo(*texts: str) -> str:
    """여러 string 후보에서 처음 발견되는 github.com/owner/repo 추출."""
    for text in texts:
        if not text:
            continue
        m = GH_REPO_RE.search(text)
        if m:
            repo = m.group(1).rstrip(".").rstrip("/")
            # 흔한 false-positive 거르기
            if repo.lower().endswith((".git", ".pdf", ".html")):
                repo = repo.rsplit(".", 1)[0]
            if "/" in repo and len(repo) <= 80:
                return repo
    return ""


def _fetch_github_stars(repo: str, token: Optional[str] = None, timeout: int = 8) -> Optional[int]:
    if not repo:
        return None
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    try:
        r = requests.get(f"https://api.github.com/repos/{repo}", headers=headers, timeout=timeout)
        if r.status_code == 200:
            return r.json().get("stargazers_count")
    except requests.RequestException:
        pass
    return None


class ArxivCollector:
    """Hugging Face Daily Papers + enrichment (venue tier, linked GitHub repo + stars)."""

    DAILY_PAPERS_API = "https://huggingface.co/api/daily_papers"

    def __init__(self, config: dict):
        self.max_results = config.get("max_results", 5)
        self.timeout = config.get("timeout", 15)
        self.gh_token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN")
        self.enable_enrichment = config.get("enable_enrichment", True)

    def collect(self) -> List[Dict]:
        results = []
        try:
            print("  📊 Hugging Face Daily Papers에서 인기 논문 수집 중...")
            response = requests.get(
                self.DAILY_PAPERS_API,
                timeout=self.timeout,
                headers={"Accept": "application/json"},
            )
            response.raise_for_status()
            papers = response.json()

            if not papers:
                print("  ⚠️ Daily Papers에서 논문을 찾을 수 없습니다")
                return []

            papers_sorted = sorted(
                papers,
                key=lambda x: x.get("paper", {}).get("upvotes", 0),
                reverse=True,
            )

            for paper_data in papers_sorted[:self.max_results]:
                paper = paper_data.get("paper", {})
                arxiv_id = paper.get("id", "")
                arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""
                summary = (paper.get("summary") or "").replace("\n", " ").strip()[:500]
                title = (paper.get("title") or "").strip()
                upvotes = int(paper.get("upvotes") or 0)

                item = {
                    "title": title,
                    "url": arxiv_url,
                    "summary": summary,
                    "authors": paper.get("authors", [])[:3],
                    "published": paper.get("publishedAt", ""),
                    "upvotes": upvotes,
                    "hf_upvotes": upvotes,           # scoring.py 호환
                    "source": "arxiv",
                }

                if self.enable_enrichment:
                    self._enrich(item, paper)

                results.append(item)

            print(f"  ✓ {len(results)}개 인기 논문 수집 (upvotes 기준)")

        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ API 요청 실패: {e}")
            return self._fallback_collect()
        except Exception as e:
            print(f"  ⚠️ arXiv 수집 실패: {e}")
            return []

        return results

    def _enrich(self, item: Dict, paper: Dict) -> None:
        """venue tier + linked GitHub repo + stars 채움. 어떤 신호도 못 찾으면 묵묵히 skip."""
        # venue tier — paper 메타 + abstract 합쳐서 검사
        meta_text = " ".join([
            str(paper.get("conference") or ""),
            str(paper.get("venue") or ""),
            str(paper.get("comment") or ""),
            item["summary"],
        ])
        tier = _classify_venue(meta_text)
        if tier:
            item["venue_tier"] = tier

        # linked GitHub repo — paper meta + summary
        repo_candidates = [
            str(paper.get("github") or ""),
            str(paper.get("projectPage") or paper.get("project_page") or ""),
            item["summary"],
            item["title"],
        ]
        repo = _extract_github_repo(*repo_candidates)
        if repo:
            item["github_repo"] = repo
            stars = _fetch_github_stars(repo, token=self.gh_token)
            if stars is not None:
                item["github_stars"] = stars

    def _fallback_collect(self) -> List[Dict]:
        try:
            import arxiv

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
                summary = paper.summary.replace("\n", " ").strip()[:500]
                comment = paper.comment or ""
                item = {
                    "title": paper.title.strip(),
                    "url": paper.entry_id,
                    "summary": summary,
                    "authors": [a.name for a in paper.authors[:3]],
                    "published": paper.published.isoformat(),
                    "upvotes": 0,
                    "hf_upvotes": 0,
                    "source": "arxiv",
                }
                if self.enable_enrichment:
                    tier = _classify_venue(comment + " " + summary)
                    if tier:
                        item["venue_tier"] = tier
                    repo = _extract_github_repo(comment, summary, paper.title)
                    if repo:
                        item["github_repo"] = repo
                        stars = _fetch_github_stars(repo, token=self.gh_token)
                        if stars is not None:
                            item["github_stars"] = stars
                results.append(item)
            return results
        except Exception as e:
            print(f"  ⚠️ 폴백도 실패: {e}")
            return []


if __name__ == "__main__":
    print("=== arXiv Collector + enrichment 테스트 ===\n")
    collector = ArxivCollector({"max_results": 3})
    papers = collector.collect()
    for i, p in enumerate(papers, 1):
        print(f"\n[{i}] 🔥 {p.get('hf_upvotes', 0)} upvotes")
        print(f"    제목: {p['title']}")
        print(f"    URL: {p['url']}")
        if p.get("venue_tier"):
            print(f"    venue: {p['venue_tier']}")
        if p.get("github_repo"):
            print(f"    repo: {p['github_repo']} (★{p.get('github_stars', '?')})")
