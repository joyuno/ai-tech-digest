"""GeekNews Weekly(news.hada.io/weekly) 최신호 수집기.

/weekly 에서 최신 이슈(/weekly/YYYYWW)를 찾아, '이번 주 주요 뉴스' 섹션의
각 항목을 추출한다. 요약 소스는 각 뉴스의 GeekNews topic 원문(clean markdown
엔드포인트 /topic/{id}.md) — 사용자 지시(‘topic 원문 타고 요약’). fetch 실패 시
weekly 페이지의 인라인 요약으로 fallback. 외부 원문 URL 은 있으면 링크용으로만 보관.
"""
import os
import re
from html import unescape
from typing import Any, Dict, Optional

import requests

BASE = "https://news.hada.io"
UA = "Mozilla/5.0 (compatible; ai-tech-digest/1.0)"
# <li id='topic-31899' class='weekly-topic-item'><a href='...'>제목</a><div class='content'><p>요약</p></div></li>
ITEM_RE = re.compile(
    r"<li id='topic-(\d+)' class='weekly-topic-item'>"
    r"<a href='([^']+)'[^>]*>(.*?)</a>\s*"
    r"<div class='content'>(.*?)</div></li>",
    re.S,
)
PERIOD_RE = re.compile(r"(\d{4}-\d{2}-\d{2})\s*[–\-]\s*(\d{4}-\d{2}-\d{2})")
EXT_SRC_RE = re.compile(r"Original source URL:\s*\[?(https?://[^\]\s)]+)", re.I)
CONTENT_CAP = 6000  # 요약 입력 상한(토큰/속도 절약; deepseek 1M 컨텍스트라 여유)


def _clean(html: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", html))).strip()


class GeekNewsWeeklyCollector:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout
        self.manual_id = os.environ.get("WEEKLY_ID", "").strip()

    def _get(self, url: str) -> str:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=self.timeout)
        r.raise_for_status()
        # Content-Type charset 누락 시 requests 가 Latin-1 오탐지 → 한글 깨짐. UTF-8 강제.
        return r.content.decode("utf-8", errors="replace")

    def _topic_md(self, tid: str) -> tuple[str, str]:
        """/topic/{id}.md 에서 (본문 텍스트, 외부원문 URL). 실패 시 ('','')."""
        try:
            md = self._get(f"{BASE}/topic/{tid}.md")
        except Exception:
            return "", ""
        ext_m = EXT_SRC_RE.search(md)
        ext = ext_m.group(1) if ext_m else ""
        body = md
        meta = re.search(r"##\s*Metadata.*?(?=\n#{1,3}\s|\Z)", body, re.S)  # 메타 블록 제거
        if meta:
            body = body[: meta.start()] + body[meta.end():]
        body = re.sub(r"^>.*$", "", body, flags=re.M)      # 안내 인용줄 제거
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        return body[:CONTENT_CAP], ext

    def _latest_id(self) -> Optional[str]:
        """/weekly 목록의 첫 번째(최신) 이슈 id (YYYYWW)."""
        try:
            h = self._get(f"{BASE}/weekly")
        except Exception as e:
            print(f"  ❌ /weekly 목록 fetch 실패: {e}")
            return None
        ids = re.findall(r"weekly/(\d+)", h)
        return ids[0] if ids else None

    def collect(self) -> Dict[str, Any]:
        weekly_id = self.manual_id or self._latest_id()
        if not weekly_id:
            print("  ℹ️ 최신 weekly 이슈를 찾지 못함")
            return {"weekly_id": None, "items": []}
        url = f"{BASE}/weekly/{weekly_id}"
        try:
            h = self._get(url)
        except Exception as e:
            print(f"  ❌ weekly/{weekly_id} fetch 실패: {e}")
            return {"weekly_id": weekly_id, "weekly_url": url, "items": []}
        title_m = re.search(r"<title>([^<]+)</title>", h)
        issue_title = _clean(title_m.group(1)) if title_m else ""
        period = PERIOD_RE.search(h)
        items = [
            {"id": tid, "url": turl, "title": _clean(title), "inline": _clean(content)}
            for tid, turl, title, content in ITEM_RE.findall(h)
        ]
        print(f"  ✅ Weekly {weekly_id}: {issue_title[:45]!r}, 주요 뉴스 {len(items)}개")
        # 각 항목: topic 원문(.md) 을 요약 소스로. 실패/짧으면 인라인 요약 fallback.
        for it in items:
            body, ext = self._topic_md(it["id"])
            it["content"] = body if len(body) > len(it["inline"]) else it["inline"]
            it["source_url"] = ext
        return {
            "weekly_id": weekly_id,
            "weekly_url": url,
            "issue_title": issue_title,
            "period_start": period.group(1) if period else "",
            "period_end": period.group(2) if period else "",
            "items": items,
        }
