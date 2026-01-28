"""Gemini 기반 요약기"""

import google.generativeai as genai
import json
import re
from typing import Dict, List, Any
from datetime import datetime


class GeminiSummarizer:
    """Gemini 3 Pro를 사용한 AI 요약 생성"""

    def __init__(self, api_key: str, model: str = "gemini-3-pro-preview"):
        self.api_key = api_key
        self.model_name = model
        self._setup_client()

    def _setup_client(self):
        """Gemini 클라이언트 설정"""
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None
            print("⚠️ Gemini API 키 없음")

    def summarize(self, classified_data: Dict[str, List[Dict]]) -> Dict[str, Any]:
        """분류된 데이터를 요약"""
        if not self.model:
            return self._fallback_summary(classified_data)

        # 각 아이템을 한국어로 요약
        summarized_data = self._summarize_items(classified_data)

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "sources": self._format_sources(summarized_data),
            "raw_data": classified_data,
        }

    def _summarize_items(self, data: Dict) -> Dict:
        """각 아이템을 한국어로 요약"""
        # 요약할 아이템 수집
        items_to_summarize = []
        for source_name, items in data.items():
            for idx, item in enumerate(items[:5]):  # 소스당 최대 5개
                items_to_summarize.append({
                    "source": source_name,
                    "index": idx,
                    "title": item.get("title", ""),
                    "content": item.get("summary", "")[:500] or item.get("content", "")[:500],
                })

        if not items_to_summarize:
            return data

        # Gemini로 한국어 요약 생성
        prompt = self._build_batch_prompt(items_to_summarize)

        try:
            response = self.model.generate_content(prompt)
            summaries = self._parse_summaries(response.text, len(items_to_summarize))
        except Exception as e:
            print(f"⚠️ Gemini 요약 실패: {e}")
            summaries = {}

        # 요약 결과를 데이터에 적용
        result = {}
        for source_name, items in data.items():
            result[source_name] = []
            for idx, item in enumerate(items[:5]):
                new_item = item.copy()
                key = f"{source_name}_{idx}"
                if key in summaries:
                    new_item["summary"] = summaries[key]
                else:
                    # 기본 요약이 없으면 제목 사용
                    new_item["summary"] = new_item.get("summary", new_item.get("title", ""))[:200]
                result[source_name].append(new_item)

        return result

    def _build_batch_prompt(self, items: List[Dict]) -> str:
        """배치 요약 프롬프트 생성"""
        items_text = []
        for i, item in enumerate(items):
            items_text.append(f"""
[{item['source']}_{item['index']}]
제목: {item['title']}
내용: {item['content']}
""")

        return f"""당신은 AI 기술 전문 한국어 블로그 작가입니다.

아래 기술 콘텐츠들을 각각 **한국어로 2-3문장**으로 요약해주세요.

규칙:
- 반드시 한국어로 작성 (영어 금지)
- 기술 용어(LLM, API, Transformer 등)만 영어 유지
- 핵심 내용과 의미를 간결하게 설명
- 친근하고 이해하기 쉬운 문체

출력 형식 (JSON):
{{
  "source_index": "한국어 요약 내용",
  ...
}}

예시:
{{
  "arxiv_0": "이 논문은 대규모 언어 모델의 추론 능력을 향상시키는 새로운 방법을 제안합니다. Chain-of-Thought 프롬프팅을 개선하여 복잡한 수학 문제 해결 성능을 크게 높였습니다.",
  "github_trending_0": "AI 기반 코드 생성 도구로, 자연어 설명만으로 복잡한 함수를 자동 생성합니다. Python과 JavaScript를 지원하며 VS Code 확장으로 사용 가능합니다."
}}

콘텐츠:
{"".join(items_text)}

JSON만 출력하세요:"""

    def _parse_summaries(self, response_text: str, expected_count: int) -> Dict[str, str]:
        """Gemini 응답에서 요약 추출"""
        try:
            # ```json 블록 제거
            cleaned = re.sub(r'```json\s*', '', response_text)
            cleaned = re.sub(r'```\s*', '', cleaned)
            cleaned = cleaned.strip()

            # JSON 파싱 시도
            if cleaned.startswith('{'):
                return json.loads(cleaned)

            # JSON 블록 찾기
            json_match = re.search(r'\{[\s\S]*\}', cleaned)
            if json_match:
                return json.loads(json_match.group())
        except json.JSONDecodeError as e:
            print(f"⚠️ JSON 파싱 실패: {e}")

        # JSON 파싱 실패시 빈 딕셔너리 반환
        print("⚠️ 요약 파싱 실패, 기본값 사용")
        return {}

    def _format_sources(self, data: Dict) -> List[Dict]:
        """소스별 포맷팅"""
        source_emoji = {
            "arxiv": "📚",
            "huggingface": "🤗",
            "twitter": "🐦",
            "toss": "💳",
            "musinsa": "👕",
            "github_trending": "⭐",
            "aiweekly": "📰",
        }

        source_names = {
            "arxiv": "arXiv 논문",
            "huggingface": "Hugging Face Blog",
            "twitter": "X (Twitter)",
            "toss": "토스 기술블로그",
            "musinsa": "무신사 기술블로그",
            "github_trending": "GitHub Trending",
            "aiweekly": "AI Weekly",
        }

        sources = []
        for source_id, items in data.items():
            if items:
                sources.append({
                    "id": source_id,
                    "name": source_names.get(source_id, source_id),
                    "emoji": source_emoji.get(source_id, "📌"),
                    "items": items,
                })

        return sources

    def _fallback_summary(self, data: Dict) -> Dict[str, Any]:
        """API 실패시 기본 요약"""
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "sources": self._format_sources(data),
            "raw_data": data,
        }
