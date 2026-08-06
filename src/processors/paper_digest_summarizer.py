"""주간 AI/ML 논문 모음 요약기 (deepseek/deepseek-v4-flash 단일).

arXiv abstract 만 근거로, 블로그 저자 1인칭 감상(느낀점) 톤의 한국어 해설을 생성한다.

호출 횟수:
  - 도입 트렌드: 1 (10편 abstract 종합 → 트렌드 3가지 축)
  - 논문 해설: 10 (논문당 abstract → 600~800자 단일 문단)

품질 가드:
  - 한국어 비율 ≥ 0.3 (영어 fallback 방지)
  - 본문 길이 ≥ 400자 (너무 짧으면 한 번 재시도)
  - 모델 fallback 없음 (사용자 정책 — 예외 없이 deepseek 만)
"""
import json
import os
import re
import time
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional


MODEL = "deepseek/deepseek-v4-flash"
PROVIDER = {"order": ["deepseek"], "allow_fallbacks": True}
RETRY_BACKOFF = [10, 25, 60]
HTTP_TIMEOUT = 180
MAX_OUTPUT_TOKENS = 2200

KOREAN_RATIO_MIN = 0.3
PER_PAPER_MIN_CHARS = 400
HANGUL_RE = re.compile(r"[가-힣]")


def korean_ratio(text: str) -> float:
    if not text:
        return 0.0
    text = text.strip()
    if not text:
        return 0.0
    return len(HANGUL_RE.findall(text)) / len(text)


# ---------------------------------------------------------------------------
# 프롬프트
# ---------------------------------------------------------------------------

INTRO_PROMPT = """당신은 매주 AI/ML 논문을 직접 챙겨 읽고, 블로그에 개인적인 감상과 해석을 남기는 개발자입니다.

아래 10편 논문의 영문 abstract 를 종합해, **이번 주 읽으며 내가 느낀 흐름 3가지** 를 1인칭 감상으로 정리하세요.

규칙:
- 각 축마다 **굵은 라벨**(명사구) + 그 흐름을 보며 든 생각을 1~2문장으로 (총 100~160자/축).
- 중립 요약이 아니라 **내 시선**: "~점이 인상적이었다", "~눈길이 갔다", "~고민하게 된다", "~실무에선 ~일 듯하다" 같은 톤.
- 어떤 논문이 어느 흐름인지 본문 안에 자연스럽게 녹일 것 (별도 리스트 X).
- 평어체·1인칭. 마크다운 단락만 출력 (헤더 없이).
- 핵심 용어는 한·영 병기 가능. abstract 에 없는 사실은 지어내지 말 것.

## 이번 주 읽은 논문

{papers_block}

도입 한 문장(이번 주 인상) + 흐름 3축 + 마무리 한 문장(개인적 결론). 전체 450~650자."""


PAPER_PROMPT = """당신은 이 논문을 방금 읽고 블로그에 감상을 남기는 개발자입니다.

아래 영문 abstract 를 근거로, **무엇을 다루는지 + 내가 왜 흥미로웠고 어떤 함의를 느꼈는지** 를 1인칭 감상으로 녹여 쓰세요.

## 글 흐름 (단일 문단으로 자연스럽게 연결)
1. **무슨 문제인가** (~2문장): 어떤 문제를 왜 다루는지.
2. **어떻게 풀었나** (~2~3문장): 저자 접근의 핵심 아이디어와 동작 방식.
3. **내가 주목한 점 / 느낀점** (~2문장): 가장 인상적이었던 기술적 선택, 또는 실무·미래에 대해 든 생각. ("~점이 흥미로웠다", "~에 쓸 수 있을 듯하다", "~는 여전히 의문이다" 같은 개인 시선)
4. **그래서 의미는** (~1문장): 정량 결과 또는 내가 보는 의의.

## 규칙
- **450~700자 단일 한국어 문단** (줄바꿈 없음, 리스트/헤더 없음).
- 평어체·1인칭 감상 톤. 중립 요약체 지양.
- 영어 abstract 를 그대로 옮기지 말고 직접 다시 정리. 숫자·약어는 보존.
- abstract 에 없는 사실 날조 금지 — 근거 없는 성능 수치·비교 지어내지 말 것.

## 논문 정보

제목: {title}
주분야: {primary_category}
저자: {authors}

abstract (영문):
{abstract}

위 abstract 만 근거로, 1인칭 감상이 담긴 단일 문단(450~700자)을 작성하세요."""


class PaperDigestSummarizer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    # ---------------- public ----------------

    def summarize(self, papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """papers: arxiv_metadata.fetch_papers_by_ids() 결과.

        반환:
          - intro: 트렌드 도입 (str)
          - papers: 입력 순서대로 한국어 해설 추가됨 ('explanation_ko')
        """
        if not papers:
            return {"intro": "", "papers": []}
        if not self.api_key:
            print("  ⚠️ OPENROUTER_API_KEY 미설정 — summarize 스킵")
            return {"intro": "", "papers": papers}

        intro = self._generate_intro(papers)
        enriched = []
        for idx, paper in enumerate(papers, start=1):
            print(f"  ✍️ [{idx}/{len(papers)}] {paper['arxiv_id']} 해설 생성 중...")
            explanation = self._generate_paper_explanation(paper)
            paper["explanation_ko"] = explanation
            enriched.append(paper)
        return {"intro": intro, "papers": enriched}

    # ---------------- prompt builders ----------------

    def _generate_intro(self, papers: List[Dict[str, Any]]) -> str:
        block_lines = []
        for i, p in enumerate(papers, 1):
            abst = (p.get("abstract") or "").replace("\n", " ")[:600]
            block_lines.append(f"### 논문 {i}: {p.get('title', '')}\n{abst}")
        prompt = INTRO_PROMPT.format(papers_block="\n\n".join(block_lines))
        result = self._call_with_retry(prompt, min_chars=300, label="intro")
        return result or ""

    def _generate_paper_explanation(self, paper: Dict[str, Any]) -> str:
        authors = ", ".join(paper.get("authors", [])[:3])
        if len(paper.get("authors", [])) > 3:
            authors += " 외"
        prompt = PAPER_PROMPT.format(
            title=paper.get("title", ""),
            primary_category=paper.get("primary_category", ""),
            authors=authors or "(저자 정보 누락)",
            abstract=(paper.get("abstract") or "")[:3500],
        )
        result = self._call_with_retry(
            prompt, min_chars=PER_PAPER_MIN_CHARS, label=paper.get("arxiv_id", "?")
        )
        # 본문 미달 시 abstract 영문 그대로 마지막 fallback (날조 방지)
        if not result:
            print(f"     ⚠️ {paper.get('arxiv_id')} 본문 생성 실패 — abstract 영문 그대로 사용")
            return f"_(한국어 해설 생성 실패. 원문 abstract:)_\n\n{paper.get('abstract', '')[:1200]}"
        return result

    # ---------------- LLM 호출 ----------------

    def _call_with_retry(self, prompt: str, min_chars: int, label: str) -> Optional[str]:
        max_attempts = len(RETRY_BACKOFF) + 1
        for attempt in range(1, max_attempts + 1):
            text = self._call_openrouter(prompt, label=label, attempt=attempt)
            if not text:
                if attempt <= len(RETRY_BACKOFF):
                    wait = RETRY_BACKOFF[attempt - 1]
                    print(f"     ⏳ {wait}s 대기 후 재시도 ({attempt}/{max_attempts})")
                    time.sleep(wait)
                continue
            # 품질 검증
            ratio = korean_ratio(text)
            if ratio < KOREAN_RATIO_MIN:
                print(f"     ⚠️ 한국어 비율 미달 ({ratio:.2f}) — 재시도")
                continue
            if len(text) < min_chars:
                print(f"     ⚠️ 본문 길이 미달 ({len(text)} < {min_chars}자) — 재시도")
                continue
            return text
        return None

    def _call_openrouter(self, prompt: str, label: str, attempt: int) -> str:
        body = {
            "model": MODEL,
            "provider": PROVIDER,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": MAX_OUTPUT_TOKENS,
            "temperature": 0.6,
        }
        payload = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            text = (data["choices"][0]["message"]["content"] or "").strip()
            # 코드펜스 제거 (LLM 이 가끔 ```markdown 으로 감쌈)
            text = re.sub(r"^```(?:markdown)?\s*\n?", "", text)
            text = re.sub(r"\n?```\s*$", "", text)
            return text
        except urllib.error.HTTPError as e:
            body_preview = e.read()[:200] if hasattr(e, "read") else b""
            print(f"     ⚠️ HTTP {e.code} ({label}, 시도 {attempt}): {body_preview!r}")
        except Exception as e:
            print(f"     ⚠️ 호출 실패 ({label}, 시도 {attempt}): {e}")
        return ""


if __name__ == "__main__":
    import sys
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("OPENROUTER_API_KEY 환경변수 필요")
        sys.exit(1)
    test_paper = {
        "arxiv_id": "2606.02373",
        "title": "Harness-1: Reinforcement Learning for Search Agents",
        "authors": ["Test"],
        "primary_category": "cs.AI",
        "abstract": "Search agents are often trained as policies over growing transcripts...",
    }
    s = PaperDigestSummarizer(api_key)
    out = s.summarize([test_paper])
    print(json.dumps(out, ensure_ascii=False, indent=2)[:2000])
