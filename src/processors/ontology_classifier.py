"""온톨로지 기반 분류기"""

from typing import List, Dict, Any


class OntologyClassifier:
    """AI 기술 온톨로지 기반 콘텐츠 분류"""

    def __init__(self, ontology_config: dict):
        self.ontology = ontology_config.get("ontology", {})

    def classify(self, content: str) -> List[str]:
        """콘텐츠를 온톨로지 카테고리로 분류"""
        matched = []
        content_lower = content.lower()

        for category_id, category_data in self.ontology.items():
            keywords = category_data.get("keywords", [])
            for keyword in keywords:
                if keyword.lower() in content_lower:
                    matched.append({
                        "id": category_id,
                        "name": category_data.get("name", category_id),
                        "emoji": category_data.get("emoji", "📌"),
                        "matched_keyword": keyword,
                    })
                    break  # 카테고리당 하나만 매칭

        return matched

    def classify_all(self, collected_data: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
        """수집된 모든 데이터를 분류"""
        classified = {}

        for source_name, items in collected_data.items():
            classified_items = []
            for item in items:
                # 제목과 요약을 합쳐서 분류
                text = f"{item.get('title', '')} {item.get('summary', '')}"
                categories = self.classify(text)
                item["categories"] = categories
                classified_items.append(item)
            classified[source_name] = classified_items

        return classified

    def get_top_keywords(self, classified_data: Dict, top_n: int = 10) -> List[str]:
        """가장 많이 매칭된 키워드 추출"""
        keyword_count = {}

        for items in classified_data.values():
            for item in items:
                for cat in item.get("categories", []):
                    kw = cat.get("matched_keyword", "")
                    if kw:
                        keyword_count[kw] = keyword_count.get(kw, 0) + 1

        sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
        return [kw for kw, _ in sorted_keywords[:top_n]]
