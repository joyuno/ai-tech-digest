"""arXiv ID 리스트 → 정식 메타데이터 fetch.

arXiv export API (http://export.arxiv.org/api/query) 의 id_list 파라미터로
한 번에 여러 논문 메타를 받아온다. 응답은 Atom XML.

ArxivCollector 의 카테고리 기반 search 와 별개로, 이미 알고 있는 ID 집합만
정확히 조회할 때 쓴다 (weekly papers 용).
"""
import re
import time
from typing import Dict, List
from xml.etree import ElementTree as ET

import requests


ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
UA = "Mozilla/5.0 (compatible; ai-tech-digest-weekly/1.0)"

# 논문 본문에서 종종 발견되는 official code repo 추출 (best-effort)
GITHUB_REPO_RE = re.compile(
    r"https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.IGNORECASE
)


def fetch_papers_by_ids(arxiv_ids: List[str], timeout: int = 30) -> List[Dict]:
    """ID 리스트로 arXiv 메타 fetch.

    반환 항목 (논문당):
      - arxiv_id, title, authors, abstract, published, updated,
        primary_category, url (abs), pdf_url, code_url (있으면)

    실패한 ID 는 결과에서 빠진다 (조용히 skip — 부분 결과라도 반환).
    """
    if not arxiv_ids:
        return []

    # arXiv API 는 id_list 콤마 구분, 한 번에 100개까지 권장
    results: List[Dict] = []
    batch_size = 50
    for i in range(0, len(arxiv_ids), batch_size):
        batch = arxiv_ids[i: i + batch_size]
        params = {"id_list": ",".join(batch), "max_results": len(batch)}
        try:
            r = requests.get(
                ARXIV_API,
                params=params,
                headers={"User-Agent": UA},
                timeout=timeout,
            )
            r.raise_for_status()
        except Exception as e:
            print(f"  ⚠️ arXiv API fetch 실패 (batch {i // batch_size}): {e}")
            continue

        try:
            root = ET.fromstring(r.content)
        except ET.ParseError as e:
            print(f"  ⚠️ arXiv XML 파싱 실패: {e}")
            continue

        for entry in root.findall(f"{ATOM_NS}entry"):
            parsed = _parse_entry(entry)
            if parsed:
                results.append(parsed)

        # arXiv 권장 — 호출 간 3초 sleep (rate limit 보호)
        if i + batch_size < len(arxiv_ids):
            time.sleep(3)

    # 입력 순서 보존 (GeekNews 큐레이션 순서를 유지)
    order = {aid: idx for idx, aid in enumerate(arxiv_ids)}
    results.sort(key=lambda x: order.get(x["arxiv_id"], 999))
    print(f"  ✅ arXiv 메타 {len(results)}/{len(arxiv_ids)} 건 수집")
    return results


def _parse_entry(entry) -> Dict:
    """Atom entry → 메타 dict. 필수 필드 누락 시 빈 dict 반환."""
    def text(tag: str) -> str:
        el = entry.find(f"{ATOM_NS}{tag}")
        return (el.text or "").strip() if el is not None else ""

    raw_id = text("id")  # "http://arxiv.org/abs/2401.12345v2"
    m = re.search(r"abs/([\d.]+?)(?:v\d+)?$", raw_id)
    if not m:
        return {}
    arxiv_id = m.group(1)

    title = re.sub(r"\s+", " ", text("title")).strip()
    abstract = re.sub(r"\s+", " ", text("summary")).strip()
    if not title or not abstract:
        return {}

    authors = []
    for au in entry.findall(f"{ATOM_NS}author"):
        name = au.find(f"{ATOM_NS}name")
        if name is not None and name.text:
            authors.append(name.text.strip())

    primary_category = ""
    pc = entry.find("{http://arxiv.org/schemas/atom}primary_category")
    if pc is not None:
        primary_category = pc.attrib.get("term", "")

    pdf_url = ""
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    for link in entry.findall(f"{ATOM_NS}link"):
        if link.attrib.get("title") == "pdf":
            pdf_url = link.attrib.get("href", "")
        elif link.attrib.get("rel") == "alternate":
            abs_url = link.attrib.get("href", abs_url)

    # abstract 안에서 GitHub 코드 링크 best-effort 추출 (있을 수도, 없을 수도)
    code_url = ""
    code_match = GITHUB_REPO_RE.search(abstract)
    if code_match:
        code_url = f"https://github.com/{code_match.group(1).rstrip('.')}"

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "published": text("published"),
        "updated": text("updated"),
        "primary_category": primary_category,
        "url": abs_url,
        "pdf_url": pdf_url,
        "code_url": code_url,
    }


if __name__ == "__main__":
    import json as _json
    sample = fetch_papers_by_ids(["2401.04081", "2305.18290"])
    print(_json.dumps(sample, ensure_ascii=False, indent=2)[:2000])
