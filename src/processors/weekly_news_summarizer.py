"""주간 기술뉴스 핵심요약기 (deepseek/deepseek-v4-flash, OpenRouter).

각 뉴스의 제목+요약을 근거로 한국어 5줄 핵심 요약을 생성한다(핵심요약 기법: 요점 우선·중복 제거).
큐레이션 매체명(GeekNews 등)은 결과에 넣지 않는다 — 개인 다이제스트 톤.
"""
import json
import time
import urllib.request
from typing import Any, Dict, List, Optional

MODEL = "deepseek/deepseek-v4-flash"
PROVIDER = {"order": ["deepseek"], "allow_fallbacks": True}
HTTP_TIMEOUT = 90
RETRY_BACKOFF = [5, 12]
# deepseek-v4 는 reasoning 토큰이 max_tokens 를 함께 소모 → 700이면 5줄이 중간에 잘림.
# 2000도 원문 긴 항목 일부가 잘려 3500으로 여유. (출력 토큰 단가 저렴해 비용 영향 미미)
MAX_OUTPUT_TOKENS = 3500

ITEM_PROMPT = """당신은 지난 한 주 개발·기술 소식을 골라 블로그에 정리하는 개발자입니다.
아래 뉴스의 제목과 내용을 바탕으로, 핵심만 뽑아 한국어로 재정리하세요.

## 규칙 (핵심요약 기법)
- 정확히 **5줄**. 각 줄은 "- " 로 시작하는 간결한 한 문장.
- 가장 중요한 사실·수치·시사점을 앞줄에. 중복·군더더기 제거.
- 원문 표현을 그대로 복사하지 말고 직접 압축. 내용에 없는 사실 날조 금지.
- 담백한 평어체. **특정 큐레이션 매체명(예: GeekNews 등)은 언급하지 말 것.**

## 뉴스
제목: {title}
내용: {content}

5줄 핵심 요약(- 로 시작하는 5줄만 출력):"""

INTRO_PROMPT = """당신은 지난 한 주 개발·기술 소식을 정리하는 개발자입니다.
아래 이번 주 뉴스 제목들을 훑고, 이번 주 전체 흐름을 2~3문장으로 담백하게 요약하세요.
평어체, 한국어. 매체명 언급 금지. 마크다운 단락만 출력.

## 이번 주 제목들
{titles}

이번 주 흐름 2~3문장:"""


class WeeklyNewsSummarizer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def summarize(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        titles = "\n".join(f"- {it['title']}" for it in items)
        intro = self._call(INTRO_PROMPT.format(titles=titles[:4000]), label="intro") or ""
        enriched = []
        for idx, it in enumerate(items, 1):
            print(f"  ✍️ [{idx}/{len(items)}] {it['title'][:36]} …")
            summary = self._call(
                ITEM_PROMPT.format(title=it["title"], content=it["content"]),
                label=it["id"],
            )
            enriched.append({**it, "summary": summary or f"- {it['content'][:180]}"})
        return {"intro": intro.strip(), "items": enriched}

    # ---------------- LLM 호출 ----------------

    def _call(self, prompt: str, label: str) -> Optional[str]:
        for attempt in range(len(RETRY_BACKOFF) + 1):
            text = self._call_openrouter(prompt, label, attempt + 1)
            if text and len(text) > 10:
                return text
            if attempt < len(RETRY_BACKOFF):
                time.sleep(RETRY_BACKOFF[attempt])
        return None

    def _call_openrouter(self, prompt: str, label: str, attempt: int) -> str:
        body = {
            "model": MODEL,
            "provider": PROVIDER,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": MAX_OUTPUT_TOKENS,
            "temperature": 0.5,
        }
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return (data["choices"][0]["message"]["content"] or "").strip()
        except Exception as e:
            print(f"     ⚠️ LLM 호출 실패 ({label}, 시도 {attempt}): {e}")
            return ""
