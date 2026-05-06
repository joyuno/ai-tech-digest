"""
하루의 항목 점수화 + 대표 항목 선정.

점수 모델 (100점 만점 정규화):

  토스 기술블로그          base 80   (새 게시글 자체가 high signal)
  무신사 기술블로그         base 80
  GitHub Trending         base 60
                          + stars_today 가산
                              >= 1000   +20
                              >=  500   +15
                              >=  200   +10
                              >=   50   +5
                          + 1등 (첫 항목) +10
  arXiv 논문              base 50
                          + 1등 (첫 항목) +10
  Hugging Face Blog       base 45
                          + min(upvotes // 5, 20)
  X (Twitter)             base 40
  AI Weekly               base 35

공통 가산:
  + 카테고리 ≥ 3 매칭                 +10
  + 이전 글들에서 안 다룬 신규 항목      +20  (history 인자)

대표 항목 = 점수 1위 source 의 첫 항목.
같은 항목이 여러 날 1위가 되더라도 신규 보너스를 못 받아 자연 회전한다.
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
    raw = item.get("upvotes") or 0
    try:
        u = int(raw)
    except (TypeError, ValueError):
        return 0
    return min(u // 5, 20)


def _category_count(item: Dict[str, Any]) -> int:
    cats = item.get("categories") or []
    return len(cats)


def score_item(source_id: str, item: Dict[str, Any], rank: int, seen_titles: set) -> int:
    """단일 항목의 점수."""
    score = SOURCE_BASE.get(source_id, 30)

    if source_id == "github_trending":
        score += _stars_bonus(item)
        if rank == 0:
            score += 10
    elif source_id == "huggingface":
        score += _hf_upvote_bonus(item)
    elif source_id in ("arxiv",):
        if rank == 0:
            score += 10

    if _category_count(item) >= 3:
        score += 10

    title = item.get("title", "").strip()
    if title and title not in seen_titles:
        score += 20

    return score


def select_representative(
    classified_data: Dict[str, List[Dict[str, Any]]],
    seen_titles: Optional[set] = None,
) -> Optional[Dict[str, Any]]:
    """그날의 대표 항목 + 모든 소스 점수 반환.

    Returns:
        {
          "source_id": str,
          "score": int,
          "item": {...},
          "all_scores": [{"source_id":..., "top_score":..., "top_title":...}, ...]
        }
        혹은 None (수집된 항목이 0개일 때)
    """
    seen_titles = seen_titles or set()
    by_source = []
    for source_id, items in classified_data.items():
        if not items:
            continue
        # 소스 안에서 1등 (첫 항목)이 그 소스 대표
        first = items[0]
        s = score_item(source_id, first, rank=0, seen_titles=seen_titles)
        by_source.append({
            "source_id": source_id,
            "score": s,
            "item": first,
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
