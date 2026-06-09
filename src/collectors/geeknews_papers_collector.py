"""GeekNews 주간 AI/ML 논문 모음 collector.

흐름:
  1. RSS (https://news.hada.io/rss/news) 에서 "이번 주에 살펴볼 만한 AI/ML 논문" 패턴 매칭 → topic id 탐지
  2. topic 페이지 (https://news.hada.io/topic?id=N) HTML fetch
  3. arxiv.org/abs/XXXX.XXXXX 패턴으로 arXiv ID 추출 (중복 제거, 등장 순서 보존)
  4. (geeknews_url, geeknews_title, arxiv_ids[]) 반환

자동 탐지 실패 시 환경변수 GEEKNEWS_TOPIC_ID 로 수동 지정 가능.
"""
import os
import re
from typing import Dict, List, Optional
from xml.etree import ElementTree as ET

import requests


RSS_URL = "https://news.hada.io/rss/news"
TOPIC_URL_TEMPLATE = "https://news.hada.io/topic?id={topic_id}"
TITLE_PATTERNS = [
    re.compile(r"이번\s*주.*살펴볼.*AI/?ML.*논문"),
    re.compile(r"이번\s*주.*AI/?ML.*논문.*모음"),
]
ARXIV_ID_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", re.IGNORECASE)
TOPIC_ID_RE = re.compile(r"topic\?id=(\d+)")
PAGE_TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)
UA = "Mozilla/5.0 (compatible; ai-tech-digest-weekly/1.0)"


class GeekNewsPapersCollector:
    """GeekNews 주간 AI/ML 논문 글에서 arXiv ID 추출."""

    def __init__(self, config: Optional[dict] = None):
        config = config or {}
        self.timeout = config.get("timeout", 15)
        # 수동 지정 우선 — env var 또는 config 의 manual_topic_id
        self.manual_topic_id = (
            os.environ.get("GEEKNEWS_TOPIC_ID")
            or str(config.get("manual_topic_id") or "").strip() or None
        )

    def collect(self) -> Dict:
        """단일 dict 반환 — main_weekly 에서 그대로 소비.

        반환 키:
          - topic_id, topic_url, topic_title
          - arxiv_ids: List[str]
        실패 시 arxiv_ids=[] 로 반환 (main_weekly 가 skip 결정).
        """
        topic_id = self.manual_topic_id or self._discover_topic_id_via_rss()
        if not topic_id:
            print("  ❌ GeekNews 주간 논문 글을 RSS 에서 찾지 못함 (수동 GEEKNEWS_TOPIC_ID 지정 필요)")
            return {"topic_id": None, "topic_url": "", "topic_title": "", "arxiv_ids": []}

        topic_url = TOPIC_URL_TEMPLATE.format(topic_id=topic_id)
        print(f"  🔍 GeekNews topic 페이지 fetch: {topic_url}")
        try:
            r = requests.get(topic_url, headers={"User-Agent": UA}, timeout=self.timeout)
            r.raise_for_status()
        except Exception as e:
            print(f"  ❌ topic fetch 실패: {e}")
            return {"topic_id": topic_id, "topic_url": topic_url, "topic_title": "", "arxiv_ids": []}

        html = r.text
        title = self._extract_title(html)
        arxiv_ids = self._extract_arxiv_ids(html)
        print(f"  ✅ 제목: {title!r}, arXiv 링크 {len(arxiv_ids)}개 추출")
        return {
            "topic_id": topic_id,
            "topic_url": topic_url,
            "topic_title": title,
            "arxiv_ids": arxiv_ids,
        }

    def _discover_topic_id_via_rss(self) -> Optional[str]:
        """RSS atom 에서 제목이 weekly papers 패턴인 최신 entry 의 topic id 추출."""
        try:
            r = requests.get(RSS_URL, headers={"User-Agent": UA}, timeout=self.timeout)
            r.raise_for_status()
        except Exception as e:
            print(f"  ⚠️ RSS fetch 실패: {e}")
            return None

        try:
            root = ET.fromstring(r.content)
        except ET.ParseError as e:
            print(f"  ⚠️ RSS 파싱 실패: {e}")
            return None

        # atom 네임스페이스 대응 (요소 tag 가 '{...}entry' 형태)
        for entry in root.iter():
            if not entry.tag.endswith("}entry") and entry.tag != "entry":
                continue
            title_text = ""
            link_href = ""
            for child in entry:
                tag = child.tag.split("}", 1)[-1]
                if tag == "title":
                    title_text = (child.text or "").strip()
                elif tag == "link":
                    link_href = child.attrib.get("href", "") or link_href
            if not title_text:
                continue
            if any(p.search(title_text) for p in TITLE_PATTERNS):
                m = TOPIC_ID_RE.search(link_href)
                if m:
                    print(f"  🔎 RSS 매칭: {title_text!r} → topic id {m.group(1)}")
                    return m.group(1)

        print("  ⚠️ RSS 에서 weekly papers 패턴 매칭 0건")
        return None

    @staticmethod
    def _extract_arxiv_ids(html: str) -> List[str]:
        """HTML 본문에서 arXiv ID 추출, 중복 제거 + 등장 순서 보존."""
        seen = []
        seen_set = set()
        for m in ARXIV_ID_RE.finditer(html):
            aid = m.group(1)
            if aid not in seen_set:
                seen_set.add(aid)
                seen.append(aid)
        return seen

    @staticmethod
    def _extract_title(html: str) -> str:
        m = PAGE_TITLE_RE.search(html)
        if not m:
            return ""
        title = m.group(1).strip()
        # " | GeekNews" 같은 suffix 정리
        for sep in (" | GeekNews", " - GeekNews", " | news.hada.io"):
            if title.endswith(sep):
                title = title[: -len(sep)].strip()
                break
        return title


if __name__ == "__main__":
    import json as _json
    out = GeekNewsPapersCollector().collect()
    print(_json.dumps(out, ensure_ascii=False, indent=2))
