"""온톨로지 기반 분류기 — sub_tags 지원."""

from typing import List, Dict, Any


class OntologyClassifier:
    """AI 기술 온톨로지 기반 콘텐츠 분류 (메인 카테고리 + sub_tags)."""

    def __init__(self, ontology_config: dict):
        self.ontology = ontology_config.get("ontology", {})

    def classify(self, content: str) -> List[Dict[str, Any]]:
        """콘텐츠를 메인 카테고리 + 그 안의 sub_tags 로 분류."""
        matched = []
        content_lower = content.lower()

        for category_id, category_data in self.ontology.items():
            # 메인 카테고리 매칭
            keywords = category_data.get("keywords", [])
            main_hit = None
            for keyword in keywords:
                if keyword.lower() in content_lower:
                    main_hit = keyword
                    break

            if not main_hit:
                continue

            # sub_tags 매칭 (최대 3개)
            sub_matches = []
            for sub in category_data.get("sub_tags", []):
                sub_name = sub.get("name", "")
                for sub_kw in sub.get("keywords", []):
                    if sub_kw.lower() in content_lower:
                        if sub_name and sub_name not in sub_matches:
                            sub_matches.append(sub_name)
                        break
                if len(sub_matches) >= 3:
                    break

            matched.append({
                "id": category_id,
                "name": category_data.get("name", category_id),
                "emoji": category_data.get("emoji", "📌"),
                "matched_keyword": main_hit,
                "sub_tags": sub_matches,
            })

        return matched

    def classify_all(self, collected_data: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
        classified = {}
        for source_name, items in collected_data.items():
            classified_items = []
            for item in items:
                text = f"{item.get('title', '')} {item.get('summary', '')}"
                categories = self.classify(text)
                item["categories"] = categories
                # 모든 sub_tags 평탄화 — 카드/그래프에서 키워드로 사용
                related = []
                for c in categories:
                    related.extend(c.get("sub_tags", []))
                item["related_keywords"] = list(dict.fromkeys(related))
                classified_items.append(item)
            classified[source_name] = classified_items
        return classified

    def get_top_keywords(self, classified_data: Dict, top_n: int = 10) -> List[str]:
        """가장 많이 매칭된 sub_tag (없으면 keyword) 추출."""
        keyword_count = {}

        for items in classified_data.values():
            for item in items:
                # sub_tags 우선
                for cat in item.get("categories", []):
                    for sub in cat.get("sub_tags", []):
                        keyword_count[sub] = keyword_count.get(sub, 0) + 1
                # fallback: matched_keyword
                if not any(c.get("sub_tags") for c in item.get("categories", [])):
                    for cat in item.get("categories", []):
                        kw = cat.get("matched_keyword", "")
                        if kw:
                            keyword_count[kw] = keyword_count.get(kw, 0) + 1

        sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
        return [kw for kw, _ in sorted_keywords[:top_n]]
