"""
하루의 항목 점수화 + 대표 항목 선정.

각 가산 변수의 max 합 = source 의 자연 만점.
인위적 cap 없음. raw 만점:
  GitHub Trending  100  (모든 신호 만점일 때 자연스럽게 100)
  arXiv 논문        100
  토스/무신사 기술블로그 90
  HF / AI Weekly / X(Twitter)  → 대표 후보 제외 (EXCLUDED set)

GitHub Trending 100 분배:
  base                                 50
  stars_today  ≥1000 +25 / ≥500 +18 / ≥200 +12 / ≥50 +6     max +25
  카테고리 ≥ 3                              +10
  rank 0 (첫 항목)                         +5
  신규 항목                              +10
                                       ─────
                                          100

arXiv 논문 100 분배:
  base                                 30
  HF Daily Papers upvotes
       ≥100 +20 / ≥50 +15 / ≥20 +10 / ≥5 +5 / on list +2  max +20
  venue tier   tier1 +12 / tier2 +8 / submitted +3        max +12
  linked GitHub repo  ≥1000★ +10 / ≥100★ +7 / ≥10★ +4 /
                       repo 존재만 +2                       max +10
  citations    ≥50 +8 / ≥10 +5 / ≥3 +3                     max +8
  카테고리 ≥ 3                              +5
  rank 0                                   +5
  신규                                    +10
                                       ─────
                                          100

토스 / 무신사 기술블로그 90 분배:
  base                                 55
  카테고리 ≥ 3                              +15
  신규                                    +20
                                       ─────
                                           90

(arXiv enrichment 보너스들은 collector enrichment 후 활성. 지금은 raw 데이터에
필드 없으면 zero-effect. 코드 경로는 미리 깔아둠.)
"""

from typing import Any, Dict, List, Optional

EXCLUDED_FROM_REPRESENTATIVE = {"huggingface", "aiweekly", "twitter"}


# ---------- GitHub Trending ----------

def _stars_bonus(item: Dict[str, Any]) -> int:
    raw = item.get("stars_today")
    if raw is None:
        return 0
    try:
        s = int(str(raw).replace(",", ""))
    except (TypeError, ValueError):
        return 0
    if s >= 1000:
        return 25
    if s >= 500:
        return 18
    if s >= 200:
        return 12
    if s >= 50:
        return 6
    return 0


# ---------- arXiv ----------

def _hf_upvote_bonus(item: Dict[str, Any]) -> int:
    """HF Daily Papers upvotes (collector enrichment 후 활성, max +20)."""
    raw = item.get("hf_upvotes")
    if raw is None:
        return 0
    try:
        u = int(raw)
    except (TypeError, ValueError):
        return 0
    if u >= 100:
        return 20
    if u >= 50:
        return 15
    if u >= 20:
        return 10
    if u >= 5:
        return 5
    return 2  # daily list 등재만으로


def _venue_bonus(item: Dict[str, Any]) -> int:
    """arxiv comment 의 venue 태그 (max +12)."""
    tier = (item.get("venue_tier") or "").lower()
    if tier == "tier1":
        return 12
    if tier == "tier2":
        return 8
    if tier == "submitted":
        return 3
    return 0


def _repo_bonus(item: Dict[str, Any]) -> int:
    """linked GitHub repo stars (max +10)."""
    stars = item.get("github_stars")
    if stars is None:
        return 0
    try:
        s = int(stars)
    except (TypeError, ValueError):
        return 0
    if s >= 1000:
        return 10
    if s >= 100:
        return 7
    if s >= 10:
        return 4
    return 2


def _citation_bonus(item: Dict[str, Any]) -> int:
    """Semantic Scholar citations (max +8, >1주 된 논문에서만 유의미)."""
    cits = item.get("citation_count")
    if cits is None:
        return 0
    try:
        c = int(cits)
    except (TypeError, ValueError):
        return 0
    if c >= 50:
        return 8
    if c >= 10:
        return 5
    if c >= 3:
        return 3
    return 0


# ---------- 공통 ----------

def _category_bonus(item: Dict[str, Any], source_id: str) -> int:
    """카테고리 ≥ 3 매칭."""
    cats = item.get("categories") or []
    if len(cats) < 3:
        return 0
    if source_id == "arxiv":
        return 5
    if source_id == "github_trending":
        return 10
    if source_id in ("toss", "musinsa"):
        return 15
    return 0


def _rank_bonus(source_id: str, rank: int) -> int:
    """rank 0 (첫 항목)."""
    if rank != 0:
        return 0
    if source_id == "arxiv":
        return 5
    if source_id == "github_trending":
        return 5
    return 0


def _new_bonus(item: Dict[str, Any], seen_titles: set, source_id: str) -> int:
    """신규 항목 (seen_titles 에 없음)."""
    title = (item.get("title") or "").strip()
    if not title or title in seen_titles:
        return 0
    if source_id == "arxiv":
        return 10
    if source_id == "github_trending":
        return 10
    if source_id in ("toss", "musinsa"):
        return 20
    return 0


def _base(source_id: str) -> int:
    if source_id == "arxiv":
        return 30
    if source_id == "github_trending":
        return 50
    if source_id in ("toss", "musinsa"):
        return 55
    return 0


def score_item(source_id: str, item: Dict[str, Any], rank: int, seen_titles: set) -> int:
    """단일 항목 점수. raw max = source 의 자연 만점 (arXiv·GitHub 100, 토스·무신사 90)."""
    score = _base(source_id)

    if source_id == "github_trending":
        score += _stars_bonus(item)
    elif source_id == "arxiv":
        score += _hf_upvote_bonus(item)
        score += _venue_bonus(item)
        score += _repo_bonus(item)
        score += _citation_bonus(item)

    score += _category_bonus(item, source_id)
    score += _rank_bonus(source_id, rank)
    score += _new_bonus(item, seen_titles, source_id)
    return score


def select_representative(
    classified_data: Dict[str, List[Dict[str, Any]]],
    seen_titles: Optional[set] = None,
) -> Optional[Dict[str, Any]]:
    """그날의 대표 항목 + 모든 소스 점수.

    각 소스 안에서 첫 신규 항목(없으면 첫 항목)을 그 소스의 대표로 잡고 점수 매김.
    EXCLUDED_FROM_REPRESENTATIVE 의 source 는 후보에서 빠지지만 본문 노출은 유지.
    """
    seen_titles = seen_titles or set()
    by_source = []
    for source_id, items in classified_data.items():
        if not items:
            continue
        if source_id in EXCLUDED_FROM_REPRESENTATIVE:
            continue
        rep = next(
            (it for it in items if (it.get("title") or "").strip() not in seen_titles),
            items[0],
        )
        s = score_item(source_id, rep, rank=0, seen_titles=seen_titles)
        by_source.append({"source_id": source_id, "score": s, "item": rep})

    if not by_source:
        return None

    by_source.sort(key=lambda b: b["score"], reverse=True)
    top = by_source[0]
    return {
        "source_id": top["source_id"],
        "score": top["score"],
        "item": top["item"],
        "all_scores": [
            {
                "source_id": b["source_id"],
                "top_score": b["score"],
                "top_title": b["item"].get("title", ""),
            }
            for b in by_source
        ],
    }
