"""주간 AI/ML 논문 모음 요약기 (deepseek/deepseek-v4-flash 단일).

ninebow 의 GeekNews 주간 글 본문 구조를 모방한 한국어 해설을 생성한다.

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

INTRO_PROMPT = """당신은 AI/ML 분야 주간 논문 큐레이션 글을 작성하는 한국어 기술 라이터입니다.

아래 10편 논문의 영문 abstract 를 종합해 **이번 주 트렌드 3가지 핵심 축** 을 추출하세요.

규칙:
- 각 축마다 **굵은 라벨** + 1~2문장 한국어 설명 (총 80~140자/축).
- 라벨은 명사구 (예: "에이전트 메모리 외재화", "어텐션 효율화").
- 어떤 논문이 어느 축에 해당하는지 본문 흐름 안에 자연스럽게 녹일 것 (별도 리스트 X).
- 평어체 ("~다", "~한다"). 마크다운 본문만 출력 (헤더 없이 단락만).
- 영어 단어 최소화, 핵심 용어는 한·영 병기 가능 (예: 어텐션(attention)).

## 논문 목록 (이번 주 큐레이션)

{papers_block}

위 10편을 종합한 트렌드 3가지를 작성하세요. 도입 문장 1개 + 3축 + 마무리 문장 1개. 전체 400~600자."""


PAPER_PROMPT = """당신은 AI/ML 논문을 한국어로 해설하는 기술 라이터입니다.

아래 영문 abstract 를 바탕으로 **본문급 한국어 해설** 을 작성하세요.

## 글 구조 (반드시 따를 것 — 단일 문단으로 자연스럽게 연결)
1. **배경/문제 정의** (전체의 20~30%, ~2문장): 어떤 문제를 다루는지, 왜 중요한지.
2. **제안 방법론** (40~50%, ~3~4문장): 저자가 제안한 접근의 핵심 아이디어와 동작 방식.
3. **기술적 핵심** (20~30%, ~2문장): 가장 두드러진 기술적 결정·아키텍처·트릭.
4. **실험 결과·함의** (10~20%, ~1~2문장): 정량적 결과 또는 의의.

## 규칙
- **600~800자 단일 한국어 문단** (줄바꿈 없음, 리스트/헤더 없음).
- 평어체 ("~다", "~한다").
- 영어 abstract 를 그대로 옮기지 말 것. 직접 다시 정리.
- 핵심 용어는 한·영 병기 가능 (예: 어텐션(attention), 검색 에이전트(search agent)).
- 영문 그대로 인용 금지. 숫자·약어는 보존.
- abstract 에 없는 사실 날조 금지 — 모르면 "본 논문은 ~에 초점을 맞추고 있다" 식으로 안전하게.

## 논문 정보

제목: {title}
주분야: {primary_category}
저자: {authors}

abstract (영문):
{abstract}

위 abstract 만 근거로 한국어 해설을 작성하세요. 단일 문단, 600~800자."""


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
