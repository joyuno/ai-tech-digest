"""주간 AI/ML 논문 모음 수집기 — PyTorchKR(discuss.pytorch.kr) 소스.

이 시리즈(9bow/박정환)는 2026-06 중순 이후 GeekNews 크로스포스팅을 멈추고
PyTorchKR 포럼에서 매주 이어지고 있다. GeekNews만 보던 기존 로직이 "7·8월 글 없음"으로
오판하던 문제를 해결하기 위한 1차(primary) 소스.

흐름:
  1. Discourse search.json 으로 최신 '논문 모음' 토픽 자동 탐지 (또는 PYTORCHKR_TOPIC_ID 수동)
  2. /t/{id}.json 의 cooked 본문에서 arXiv ID 추출
  3. (topic_id, topic_url, topic_title, arxiv_ids[]) 반환 — GeekNews 수집기와 동일 shape
"""
import os
import re
from typing import Any, Dict, List, Optional

import requests

BASE = "https://discuss.pytorch.kr"
UA = "Mozilla/5.0 (compatible; ai-tech-digest/1.0)"
SERIES_QUERY = "이번 주에 살펴볼 만한 AI/ML 논문 모음"
TITLE_RE = re.compile(r"이번 주에 살펴볼 만한 AI/?ML 논문 모음")
ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")


class PyTorchKRPapersCollector:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout
        self.manual_topic_id = os.environ.get("PYTORCHKR_TOPIC_ID", "").strip()

    def _get_json(self, url: str, params: dict | None = None) -> dict:
        r = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=self.timeout)
        r.raise_for_status()
        # Content-Type charset 누락 시 requests 가 Latin-1 로 오탐지 → 한글 깨짐. UTF-8 강제.
        import json as _json
        return _json.loads(r.content.decode("utf-8", errors="replace"))

    def _discover_topic_id(self) -> Optional[str]:
        """Discourse 검색에서 제목이 시리즈 패턴인 최신 토픽 id."""
        try:
            d = self._get_json(f"{BASE}/search.json", {"q": f"{SERIES_QUERY} order:latest"})
        except Exception as e:
            print(f"  ❌ PyTorchKR 검색 실패: {e}")
            return None
        for t in d.get("topics", []):
            if TITLE_RE.search(t.get("title", "")):
                print(f"  🔎 PyTorchKR 최신 매칭: {t['title']!r} → topic id {t['id']}")
                return str(t["id"])
        return None

    def _extract(self, topic_id: str) -> tuple[str, List[str]]:
        """/t/{id}.json 의 첫 포스트 cooked 에서 제목·arXiv ID 추출."""
        d = self._get_json(f"{BASE}/t/{topic_id}.json")
        title = d.get("title", "")
        posts = d.get("post_stream", {}).get("posts", [])
        cooked = posts[0].get("cooked", "") if posts else ""
        arxiv_ids = list(dict.fromkeys(ARXIV_RE.findall(cooked)))  # 순서보존 dedup
        return title, arxiv_ids

    def collect(self) -> Dict[str, Any]:
        topic_id = self.manual_topic_id or self._discover_topic_id()
        if not topic_id:
            print("  ℹ️ PyTorchKR 주간 논문 글을 찾지 못함 — GeekNews fallback 시도")
            return {"topic_id": None, "topic_url": "", "topic_title": "", "arxiv_ids": [], "source": "pytorchkr"}
        topic_url = f"{BASE}/t/{topic_id}"
        try:
            title, arxiv_ids = self._extract(topic_id)
        except Exception as e:
            print(f"  ❌ PyTorchKR topic fetch 실패: {e}")
            return {"topic_id": topic_id, "topic_url": topic_url, "topic_title": "", "arxiv_ids": [], "source": "pytorchkr"}
        print(f"  ✅ 제목: {title!r}, arXiv 링크 {len(arxiv_ids)}개 추출")
        return {"topic_id": topic_id, "topic_url": topic_url, "topic_title": title,
                "arxiv_ids": arxiv_ids, "source": "pytorchkr"}
