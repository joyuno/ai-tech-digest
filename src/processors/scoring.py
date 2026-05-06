"""
하루의 항목 점수화 + 대표 항목 선정.

소스별 점수 cap (사용자 정책):
  GitHub Trending / arXiv 논문   cap 100  (정량 신호 풍부 — stars, HF upvotes,
                                          venue, citations 등이 들어오면 그대로 합산)
  토스 / 무신사 기술블로그          cap 90   (정량 신호 적음, 새 글 발행 자체가 신호)
  Hugging Face / AI Weekly /
  X (Twitter)                    cap 0    (대표 후보에서 제외 — 본문엔 그대로 노출)

가산 산식:
  GitHub Trending  base 60 + stars_today 보너스 (≥1000 +20, ≥500 +15, ≥200 +10, ≥50 +5)
                            + rank 0 +10
  arXiv 논문       base 50 + rank 0 +10
                            + (옵션) HF Daily Papers upvotes / venue tier / linked
                              repo stars / citations — collector enrichment 후 활성
  토스/무신사       base 60
  공통             + 카테고리 ≥ 3 매칭   +10
                  + 신규 항목 (seen_titles 에 없음)  +20

마지막에 source 별 cap 적용. cap 0 인 source 는 select_representative 후보에서 제외.
"""

from typing import Any, Dict, List, Optional

SOURCE_BASE = {
    "toss": 60,
    "musinsa": 60,
    "github_trending": 60,
    "arxiv": 50,
    "huggingface": 45,
    "twitter": 40,
    "aiweekly": 35,
}

SOURCE_CAP = {
    "github_trending": 100,
    "arxiv": 100,
    "toss": 90,
    "musinsa": 90,
    "huggingface": 0,   # 대표 후보 제외 (본문 노출은 유지)
    "aiweekly": 0,
    "twitter": 0,
}


def _stars_bonus(item: Dict[str, Any]) -> int:
    raw = item.get("stars_today")
    if raw is None:
        return 0
    try:
        s = int(str(raw).replace(",", ""))
    except (TypeError, ValueError):
        return 0
    if s >= 1000:
        return 20
    if s >= 500:
        return 15
    if s >= 200:
        return 10
    if s >= 50:
        return 5
    return 0


def _hf_upvote_bonus(item: Dict[str, Any]) -> int:
    """arXiv 항목에 HF Daily Papers upvotes 가 enrichment 됐을 때 가산.

    item['hf_upvotes'] 필드가 있을 때만 동작. collector enrichment 후 작동.
    """
    raw = item.get("hf_upvotes")
    if raw is None:
        return 0
    try:
        u = int(raw)
    except (TypeError, ValueError):
        return 0
    if u >= 100:
        return 25
    if u >= 50:
        return 20
    if u >= 20:
        return 15
    if u >= 5:
        return 10
    return 5  # daily list 에 등재된 것 자체로 +5


def _venue_bonus(item: Dict[str, Any]) -> int:
    """arxiv comment 의 venue 태그 (collector enrichment).

    item['venue_tier']: 'tier1' / 'tier2' / 'submitted'
    """
    tier = (item.get("venue_tier") or "").lower()
    if tier == "tier1":
        return 15
    if tier == "tier2":
        return 10
    if tier == "submitted":
        return 5
    return 0


def _repo_bonus(item: Dict[str, Any]) -> int:
    """linked GitHub repo stars (collector enrichment)."""
    stars = item.get("github_stars")
    if stars is None:
        return 0
    try:
        s = int(stars)
    except (TypeError, ValueError):
        return 0
    if s >= 1000:
        return 15
    if s >= 100:
        return 10
    if s >= 10:
        return 5
    return 3  # repo 자체 존재만으로


def _citation_bonus(item: Dict[str, Any]) -> int:
    """Semantic Scholar citations (collector enrichment, >1주 된 논문에서만 유의미)."""
    cits = item.get("citation_count")
    if cits is None:
        return 0
    try:
        c = int(cits)
    except (TypeError, ValueError):
        return 0
    if c >= 50:
        return 15
    if c >= 10:
        return 10
    if c >= 3:
        return 5
    return 0


def _category_count(item: Dict[str, Any]) -> int:
    cats = item.get("categories") or []
    return len(cats)


def score_item(source_id: str, item: Dict[str, Any], rank: int, seen_titles: set) -> int:
    """단일 항목의 점수. 소스별 cap 적용 후 반환."""
    score = SOURCE_BASE.get(source_id, 30)

    if source_id == "github_trending":
        score += _stars_bonus(item)
        if rank == 0:
            score += 10
    elif source_id == "arxiv":
        score += _hf_upvote_bonus(item)   # collector enrichment 후 작동
        score += _venue_bonus(item)
        score += _repo_bonus(item)
        score += _citation_bonus(item)
        if rank == 0:
            score += 10
    elif source_id == "huggingface":
        # cap 0 (제외) 이지만 산식은 유지 — 추후 정책 변경 시 즉시 활성
        raw = item.get("upvotes") or 0
        try:
            score += min(int(raw) // 5, 20)
        except (TypeError, ValueError):
            pass

    if _category_count(item) >= 3:
        score += 10

    title = (item.get("title") or "").strip()
    if title and title not in seen_titles:
        score += 20

    cap = SOURCE_CAP.get(source_id, 100)
    return min(score, cap)


def select_representative(
    classified_data: Dict[str, List[Dict[str, Any]]],
    seen_titles: Optional[set] = None,
) -> Optional[Dict[str, Any]]:
    """그날의 대표 항목 + 모든 소스 점수 반환. cap 0 인 source 는 후보에서 제외.

    Returns:
        {
          "source_id": str,
          "score": int,
          "item": {...},
          "all_scores": [{"source_id":..., "top_score":..., "top_title":...}, ...]
        }
        혹은 None (수집된 항목이 0개일 때).
    """
    seen_titles = seen_titles or set()
    by_source = []
    for source_id, items in classified_data.items():
        if not items:
            continue
        if SOURCE_CAP.get(source_id, 100) <= 0:
            continue  # 대표 후보에서 제외
        # 소스 안에서 첫 신규 항목을 그 소스 대표로 (없으면 첫 항목)
        rep = next((it for it in items if (it.get("title") or "").strip() not in seen_titles), items[0])
        s = score_item(source_id, rep, rank=0, seen_titles=seen_titles)
        by_source.append({
            "source_id": source_id,
            "score": s,
            "item": rep,
        })

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
