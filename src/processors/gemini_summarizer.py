"""Gemini 기반 요약기"""

import google.generativeai as genai
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

        # 프롬프트 생성
        prompt = self._build_prompt(classified_data)

        try:
            response = self.model.generate_content(prompt)
            summary_text = response.text
        except Exception as e:
            print(f"⚠️ Gemini 요약 실패: {e}")
            return self._fallback_summary(classified_data)

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "summary_text": summary_text,
            "sources": self._format_sources(classified_data),
            "raw_data": classified_data,
        }

    def _build_prompt(self, data: Dict) -> str:
        """요약 프롬프트 생성"""
        content_parts = []

        for source_name, items in data.items():
            if items:
                content_parts.append(f"\n## {source_name}")
                for item in items[:3]:  # 소스당 최대 3개
                    content_parts.append(f"- 제목: {item.get('title', '')}")
                    content_parts.append(f"  링크: {item.get('url', '')}")
                    content_parts.append(f"  내용: {item.get('summary', '')[:300]}")

        content = "\n".join(content_parts)

        prompt = f"""
당신은 AI 기술 전문 한국어 블로그 작가입니다.
다음 AI 기술 관련 콘텐츠들을 **반드시 한국어로** 요약해주세요.

중요 규칙:
- 모든 설명과 요약은 한국어로 작성
- 기술 용어(LLM, Transformer, API 등)만 영어 유지
- 논문 제목이나 프로젝트명은 원어 유지하되, 설명은 한국어로

각 항목별로:
1. 핵심 내용을 2-3문장의 한국어로 요약
2. 왜 중요한지 한국어로 간단히 설명

스타일:
- 친근하고 이해하기 쉬운 한국어 사용
- 전문가가 아니어도 이해할 수 있게 설명

콘텐츠:
{content}
"""
        return prompt

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
            "summary_text": "AI 요약을 생성할 수 없습니다.",
            "sources": self._format_sources(data),
            "raw_data": data,
        }
