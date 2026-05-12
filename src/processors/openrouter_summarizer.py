"""OpenRouter (x-ai/grok-4.1-fast) 기반 요약기.

기존 GeminiSummarizer 의 한계 보완:
  - 35개 한 번에 batch → 부분 실패 시 전체 손실 → **소스별로 batch 분리**
  - max_output_tokens 미지정으로 잘림 → **8000으로 명시**
  - Gemini가 영어로 fallback → **한국어 비율 검증**으로 강제
  - 모델 deprecated 시 즉시 중단 → **fallback chain** (grok → claude-haiku → gemini)
"""

import json
import os
import re
import time
import urllib.request
import urllib.error
from typing import Dict, List, Any, Optional
from datetime import datetime

from .scoring import select_representative


FALLBACK_MODEL_CHAIN = [
    "x-ai/grok-4.1-fast",
    "anthropic/claude-haiku-4-5",
    "google/gemini-2.5-flash",
]
RETRY_BACKOFF = [10, 20, 40]
HTTP_TIMEOUT = 180
MAX_OUTPUT_TOKENS = 8000

# 한국어 비율 임계치 — 이보다 낮으면 영어 fallback 의심, 거부
KOREAN_RATIO_MIN = 0.3
HANGUL_RE = re.compile(r'[가-힣]')


def korean_ratio(text: str) -> float:
    if not text:
        return 0.0
    text = text.strip()
    if not text:
        return 0.0
    return len(HANGUL_RE.findall(text)) / len(text)


SOURCE_NAMES = {
    "arxiv": "arXiv 논문",
    "huggingface": "Hugging Face Blog",
    "twitter": "X (Twitter)",
    "toss": "토스 기술블로그",
    "musinsa": "무신사 기술블로그",
    "github_trending": "GitHub Trending",
    "aiweekly": "AI Weekly",
}
SOURCE_EMOJI = {
    "arxiv": "📚",
    "huggingface": "🤗",
    "twitter": "🐦",
    "toss": "💳",
    "musinsa": "👕",
    "github_trending": "⭐",
    "aiweekly": "📰",
}


class OpenRouterSummarizer:
    """OpenRouter API 기반 한국어 요약 생성. 외부 API는 GeminiSummarizer 와 호환."""

    def __init__(self, api_key: str, model: str = FALLBACK_MODEL_CHAIN[0]):
        self.api_key = api_key
        primary = model or FALLBACK_MODEL_CHAIN[0]
        self.model_chain = [primary] + [m for m in FALLBACK_MODEL_CHAIN if m != primary]

    # ---------- 외부 API ----------

    def summarize(
        self,
        classified_data: Dict[str, List[Dict]],
        seen_titles: Optional[set] = None,
    ) -> Dict[str, Any]:
        if not self.api_key:
            print("⚠️ OPENROUTER_API_KEY 미설정 — fallback (원문 유지)")
            return self._fallback(classified_data)

        summarized_data = self._summarize_per_source(classified_data)
        sources = self._format_sources(summarized_data)

        # 점수화 → 그날의 대표 항목 (헤드라인 angle).
        # seen_titles 가 있으면 최근 며칠 대표였던 항목은 1순위에서 밀려나고 +new_bonus 도 못 받는다.
        representative = select_representative(classified_data, seen_titles=seen_titles or set())
        if representative:
            print(
                f"  🏆 대표 소스={representative['source_id']} "
                f"점수={representative['score']} "
                f"항목={representative['item'].get('title', '')[:40]!r}"
            )

        headline = self._generate_headline(sources, representative)

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "headline": headline,
            "representative": representative,
            "sources": sources,
            "raw_data": classified_data,
        }

    # ---------- 큐레이션 헤드라인 ----------

    def _generate_headline(self, sources: List[Dict], representative: Dict[str, Any] = None) -> str:
        """그날의 항목 전체 + 점수화 결과를 보고 한국어 한 줄 헤드라인 생성.

        representative 가 주어지면 그 항목을 헤드라인 angle 로 강조. 실패 시
        빈 문자열 반환 → 템플릿이 기본 폴백(`AI Tech - YYYY-MM-DD`) 사용.
        """
        items = []
        cats = []
        first_snippet = ""
        for src in sources:
            for it in src.get("items", []):
                if it.get("title"):
                    items.append(it["title"])
                for c in (it.get("categories") or []):
                    name = c.get("name") if isinstance(c, dict) else str(c)
                    if name:
                        cats.append(name)
                if not first_snippet and it.get("summary"):
                    first_snippet = str(it["summary"])[:280]

        items = items[:7]
        cats = list(dict.fromkeys(cats))[:6]
        if not items:
            return ""

        # 대표 항목 라인 — 점수화 결과를 prompt 에 명시
        rep_line = ""
        if representative and representative.get("item"):
            rep_item = representative["item"]
            rep_line = (
                f"\n\n[그날의 대표 — 점수 {representative['score']}점, "
                f"소스 {representative['source_id']}]\n"
                f"제목: {rep_item.get('title', '')[:160]}\n"
                f"요약: {(rep_item.get('summary') or '')[:200]}"
            )

        prompt = (
            "당신은 매일의 AI 기술 트렌드를 한국어 헤드라인으로 정제하는 에디터입니다.\n\n"
            "오늘의 항목들과 점수화된 대표 항목을 보고 그날의 핵심 흐름을 "
            "**25~45자 한 줄 헤드라인**으로 작성해주세요. 너무 짧게 자르지 말 것.\n\n"
            "## 핵심 규칙\n"
            "1. **영어 고유명사·논문명·repo명·모델명·회사명은 영어 그대로**. 한국어 음역 절대 금지.\n"
            "   - X: 앤스로픽, 모로모액트, 클로드  →  O: Anthropic, MolmoAct2, Claude\n"
            "2. **권장 패턴 (다음 둘 중 하나)**:\n"
            "   - `영어명 — 한국어 보조 설명`  (예: `MolmoAct2 — 로봇의 real-world 행동추론 모델`)\n"
            "   - `영어명/회사, 한국어 동작·결과`  (예: `Anthropic, 금융서비스 가이드라인 제공`)\n"
            "3. 한국어 단어 + 영어 키워드 자연스럽게 섞기 (예: `로봇의 real-world 행동추론`).\n"
            "4. 따옴표·이모지·말꼬리 종결(`~다`, `~음`) 금지.\n"
            "5. 출력은 제목 한 줄만 (다른 설명 X).\n\n"
            "## 안 좋은 예 (절대 X)\n"
            "- `실세계 로` (너무 짧음, 어절 잘림)\n"
            "- `앤스로픽, 금융` (한국어 음역 + 짧음)\n"
            "- `로봇 행동 모델` (영어 고유명사 모두 한국어로 압축)\n"
            "- `MolmoAct2: Action Reasoning Models for Real-world Deployment` (논문 영어 제목 그대로 = 번역 안 한 것)\n\n"
            "## 좋은 예\n"
            "- `MolmoAct2 — 로봇의 real-world 행동추론 모델`\n"
            "- `Anthropic, 금융서비스 가이드라인 제공`\n"
            "- `DeepSeek-TUI, 터미널에서 굴리는 DeepSeek 코딩 에이전트`\n"
            "- `LLaDA2.0-Uni — 통합 멀티모달 diffusion LLM`\n\n"
            f"카테고리: {', '.join(cats) if cats else '—'}\n"
            "전체 항목:\n"
            + "\n".join(f"- {t}" for t in items)
            + (f"\n\n첫 항목 요약: {first_snippet}" if first_snippet else "")
            + rep_line
            + "\n\n한국어 헤드라인:"
        )

        for model in self.model_chain[:2]:  # primary + 첫 fallback 만 시도 (속도)
            try:
                payload = json.dumps({
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 120,
                    "temperature": 0.5,
                }).encode("utf-8")
                req = urllib.request.Request(
                    "https://openrouter.ai/api/v1/chat/completions",
                    data=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                    body = json.loads(resp.read().decode("utf-8"))
                text = (body["choices"][0]["message"]["content"] or "").strip()
                if not text:
                    continue
                line = text.splitlines()[0].strip().strip('"\'').rstrip(".· ")
                # 강화: 너무 짧은 제목 거부 (15자 미만 = 어절 잘림 위험)
                if 15 <= len(line) <= 80 and korean_ratio(line) >= 0.2:
                    print(f"  📰 헤드라인: {line}")
                    return line
                else:
                    print(f"  ⚠️ 헤드라인 부적절 ({len(line)}자, 한국어 {korean_ratio(line):.0%}) — 다음 모델: {line!r}")
            except Exception as e:
                print(f"  ⚠️ 헤드라인 생성 실패 ({model}): {e}")
        return ""

    # ---------- 내부 ----------

    def _summarize_per_source(self, data: Dict) -> Dict:
        """소스별로 분리 호출 — 한 소스가 실패해도 다른 소스는 살아남는다."""
        result = {}
        for source_name, items in data.items():
            if not items:
                result[source_name] = []
                continue

            head = items[:5]
            tail = items[5:]  # 보존 (요약 안 하지만 데이터는 유지)

            print(f"  📝 {source_name}: {len(head)}개 요약 시도")
            summaries = self._call_for_batch(source_name, head)

            new_items = []
            for idx, item in enumerate(head):
                summary = summaries.get(str(idx))
                if summary and korean_ratio(summary) >= KOREAN_RATIO_MIN:
                    new_item = item.copy()
                    new_item["summary"] = summary
                    new_items.append(new_item)
                else:
                    # 영어 fallback이거나 빈 요약 — 원문 보존하되 명시적 마커
                    new_item = item.copy()
                    new_item["summary"] = item.get("summary") or item.get("title", "")
                    new_item["_summary_failed"] = True
                    new_items.append(new_item)

            result[source_name] = new_items + tail
        return result

    def _call_for_batch(self, source_name: str, items: List[Dict]) -> Dict[str, str]:
        """한 소스의 항목들을 한 번에 요약. 모델 chain으로 retry."""
        prompt = self._build_prompt(source_name, items)

        for model_idx, model in enumerate(self.model_chain, start=1):
            text = self._call_openrouter(prompt, model, model_idx, len(self.model_chain))
            if not text:
                continue

            parsed = self._parse_json(text)
            if not parsed:
                print(f"     ⚠️ {model} JSON 파싱 실패 — 다음 모델")
                continue

            # 한국어 비율 검증
            valid = {
                k: v for k, v in parsed.items()
                if isinstance(v, str) and korean_ratio(v) >= KOREAN_RATIO_MIN
            }
            if len(valid) < len(parsed) * 0.5:
                print(f"     ⚠️ {model} 한국어 비율 부족 — 다음 모델")
                continue

            return valid

        print(f"     ❌ 모든 모델 실패 — {source_name} 원문 유지")
        return {}

    def _build_prompt(self, source_name: str, items: List[Dict]) -> str:
        items_text = []
        for idx, item in enumerate(items):
            title = item.get("title", "")[:300]
            content = (item.get("summary", "") or item.get("content", ""))[:600]
            items_text.append(f"[{idx}]\n제목: {title}\n내용: {content}")

        items_block = "\n\n".join(items_text)

        return f"""당신은 AI 기술 전문 한국어 블로그 작가입니다.

아래 {source_name} 출처 콘텐츠 {len(items)}개를 각각 **완전한 한국어 2~3문장**으로 요약해주세요.

엄격한 규칙:
1. **반드시 한국어로** 작성 — 영어 문장은 금지 (LLM, API, RAG 같은 고유 기술 용어만 영어 OK)
2. 영어 abstract를 그대로 옮기지 말고 의역 + 핵심 정리
3. 요약은 완결된 문장으로 끝내기 — 어절·문장 중간에 끊지 말 것
4. 출력은 **반드시 JSON 객체** — 다른 설명·markdown·코드펜스 없이 JSON만

출력 포맷:
{{
  "0": "첫 번째 항목의 한국어 요약 (2~3문장)",
  "1": "두 번째 항목의 한국어 요약 (2~3문장)"
}}

콘텐츠:
{items_block}

JSON 객체만 출력:"""

    def _call_openrouter(self, prompt: str, model: str, idx: int, total: int) -> str:
        max_retries = len(RETRY_BACKOFF) + 1

        for attempt in range(1, max_retries + 1):
            try:
                payload = json.dumps({
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": MAX_OUTPUT_TOKENS,
                    "temperature": 0.4,
                    "response_format": {"type": "json_object"},
                }).encode("utf-8")

                req = urllib.request.Request(
                    "https://openrouter.ai/api/v1/chat/completions",
                    data=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                    body = json.loads(resp.read().decode("utf-8"))

                text = (body["choices"][0]["message"]["content"] or "").strip()
                if text:
                    return text
                print(f"     ⚠️ {model} 빈 응답 (시도 {attempt}/{max_retries})")
            except urllib.error.HTTPError as e:
                # response_format을 모델이 거부하면 한 번만 안 붙이고 재시도
                err_body = e.read().decode("utf-8", errors="ignore")[:200]
                print(f"     ⚠️ {model} HTTP {e.code} (시도 {attempt}/{max_retries}): {err_body}")
            except Exception as e:
                print(f"     ⚠️ {model} 실패 (시도 {attempt}/{max_retries}): {e}")

            if attempt <= len(RETRY_BACKOFF):
                wait = RETRY_BACKOFF[attempt - 1]
                time.sleep(wait)

        return ""

    @staticmethod
    def _parse_json(text: str) -> Dict[str, str]:
        # 코드펜스 제거
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        text = text.strip()
        try:
            obj = json.loads(text)
            if isinstance(obj, dict):
                return {str(k): str(v) for k, v in obj.items()}
        except json.JSONDecodeError:
            pass

        # JSON 객체 부분만 추출 시도
        m = re.search(r'\{[\s\S]*\}', text)
        if m:
            try:
                obj = json.loads(m.group())
                if isinstance(obj, dict):
                    return {str(k): str(v) for k, v in obj.items()}
            except json.JSONDecodeError:
                pass
        return {}

    def _format_sources(self, data: Dict) -> List[Dict]:
        sources = []
        for source_id, items in data.items():
            if items:
                sources.append({
                    "id": source_id,
                    "name": SOURCE_NAMES.get(source_id, source_id),
                    "emoji": SOURCE_EMOJI.get(source_id, "📌"),
                    "items": items,
                })
        return sources

    def _fallback(self, data: Dict) -> Dict[str, Any]:
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "sources": self._format_sources(data),
            "raw_data": data,
        }


# 외부 호환: 기존 코드가 GeminiSummarizer를 import하고 있더라도 동작하도록 alias
GeminiSummarizer = OpenRouterSummarizer
