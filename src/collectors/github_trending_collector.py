"""GitHub Trending 수집기 + README 대표 이미지 추출."""

import os
import re
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup


# README 안의 첫 이미지 — markdown ![alt](url) / <img src="..."> 둘 다 매칭
_MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(\s*([^)\s]+)", re.MULTILINE)
_HTML_IMG_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)


def _is_badge(url: str) -> bool:
    """badge / button / shield / status 이미지 거름. README hero 는 보통 png/jpg/gif/webp."""
    u = url.lower().strip()
    # SVG 는 거의 항상 badge/button — hero 이미지는 raster
    if u.split("?", 1)[0].endswith(".svg"):
        return True
    # 알려진 badge / 트래커 호스트
    bad_hosts = (
        "shields.io", "badge.fury.io", "badgen.net",
        "travis-ci", "circleci", "codecov", "coveralls",
        "github-readme-stats",
        "pepy.tech", "trendshift.io", "star-history.com",
        "img.shields.io", "vercel.com/button", "railway.com/button",
        "deploy.workers.dev", "deploy.cf",
        "securityscorecards.dev", "snyk.io/test", "deps.dev",
        "scorecard.dev", "sonarcloud.io",
    )
    if any(h in u for h in bad_hosts):
        return True
    # URL 패턴 — /badge.* /button.* /actions/workflows
    if "/badge." in u or "/button." in u or "actions/workflows" in u:
        return True
    return False


def _resolve_relative(url: str, owner: str, repo: str, branch: str) -> str:
    """상대 경로 README 이미지를 raw.githubusercontent.com 절대 URL 로 변환."""
    if url.startswith(("http://", "https://")):
        return url
    if url.startswith("//"):
        return "https:" + url
    rel = url.lstrip("./").lstrip("/")
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel}"


def _fetch_readme_image(repo_full_name: str, token: Optional[str], timeout: int = 8) -> Optional[str]:
    """repo 의 README 첫 의미있는 이미지 URL 반환. 없으면 None."""
    if not repo_full_name or "/" not in repo_full_name:
        return None
    owner, repo = repo_full_name.split("/", 1)
    headers = {"Accept": "application/vnd.github.v3.raw"}
    if token:
        headers["Authorization"] = f"token {token}"

    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    try:
        r = requests.get(api_url, headers=headers, timeout=timeout)
        if r.status_code != 200:
            return None
        text = r.text
    except requests.RequestException:
        return None

    # default branch (raw URL resolution 위해)
    branch = "main"
    try:
        meta_headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            meta_headers["Authorization"] = f"token {token}"
        meta = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
            headers=meta_headers,
            timeout=timeout,
        )
        if meta.status_code == 200:
            branch = meta.json().get("default_branch", "main") or "main"
    except requests.RequestException:
        pass

    candidates: List[str] = []
    candidates.extend(_MD_IMG_RE.findall(text))
    candidates.extend(_HTML_IMG_RE.findall(text))

    for url in candidates:
        url = url.strip().split(" ")[0]
        if not url or url.startswith("#"):
            continue
        if _is_badge(url):
            continue
        return _resolve_relative(url, owner, repo, branch)
    return None


def _extract_owner_repo(url: str) -> Optional[str]:
    m = re.search(r"github\.com/([\w.-]+/[\w.-]+)", url)
    if not m:
        return None
    return m.group(1).rstrip(".").rstrip("/")


class GitHubTrendingCollector:
    """GitHub Trending + README 첫 이미지 추출."""

    AI_KEYWORDS = {
        "ai", "llm", "machine-learning", "deep-learning", "gpt", "transformer",
        "neural", "ml", "bert", "diffusion", "stable-diffusion", "chatgpt",
        "langchain", "pytorch", "tensorflow", "keras", "scikit-learn",
        "openai", "anthropic", "claude", "gemini", "mistral", "llama",
        "embedding", "vector", "rag", "fine-tuning", "training", "model",
        "nlp", "computer-vision", "cv", "reinforcement-learning", "rl",
    }

    def __init__(self, config: dict):
        self.base_url = "https://github.com/trending"
        self.languages = config.get("languages", ["", "python"])
        self.max_results = config.get("max_results", 5)
        self.enable_image = config.get("enable_image", True)
        self.gh_token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN")
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def collect(self) -> List[Dict]:
        """Trending 페이지 + AI/ML 필터링 + README 첫 이미지 enrichment."""
        results = []
        for lang in self.languages:
            url = f"{self.base_url}/{lang}" if lang else self.base_url
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "lxml")
                repos = soup.select("article.Box-row")
                for repo in repos:
                    parsed = self._parse_repo(repo)
                    if parsed and self._is_ai_related(parsed):
                        if self.enable_image:
                            self._enrich_image(parsed)
                        results.append(parsed)
                        if len(results) >= self.max_results:
                            return results
            except requests.RequestException as e:
                print(f"GitHub Trending 스크래핑 실패 ({lang}): {e}")
            except Exception as e:
                print(f"예상치 못한 오류 ({lang}): {e}")
        return results[:self.max_results]

    def _enrich_image(self, item: Dict) -> None:
        repo_full = _extract_owner_repo(item.get("url", ""))
        if not repo_full:
            return
        img = _fetch_readme_image(repo_full, token=self.gh_token)
        if img:
            item["image_url"] = img
            item["image_source"] = "readme"

    def _parse_repo(self, repo_element):
        try:
            name_elem = repo_element.select_one("h2 a")
            if not name_elem:
                return None
            repo_name = name_elem.get_text(strip=True).replace("\n", "").replace(" ", "")
            repo_url = f"https://github.com{name_elem.get('href', '')}"
            desc_elem = repo_element.select_one("p.col-9")
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            lang_elem = repo_element.select_one("span[itemprop='programmingLanguage']")
            language = lang_elem.get_text(strip=True) if lang_elem else ""
            stars_today = ""
            for span in repo_element.select("span.d-inline-block.float-sm-right"):
                text = span.get_text(strip=True)
                if "stars today" in text or "star today" in text:
                    stars_today = text
                    break
            stars_count = self._extract_stars_count(stars_today)
            return {
                "title": repo_name,
                "url": repo_url,
                "summary": description,
                "language": language,
                "stars_today": stars_count,
                "stars_text": stars_today,
            }
        except Exception as e:
            print(f"레포 파싱 실패: {e}")
            return None

    def _extract_stars_count(self, stars_text: str) -> str:
        if not stars_text:
            return "0"
        m = re.search(r"([\d,]+)", stars_text)
        if m:
            return m.group(1).replace(",", "")
        return "0"

    def _is_ai_related(self, repo: Dict) -> bool:
        search_text = (
            (repo.get("title") or "") + " "
            + (repo.get("summary") or "") + " "
            + (repo.get("language") or "")
        ).lower()
        return any(keyword in search_text for keyword in self.AI_KEYWORDS)


if __name__ == "__main__":
    print("GitHub Trending Collector + README image 테스트\n")
    collector = GitHubTrendingCollector({"languages": ["", "python"], "max_results": 5})
    results = collector.collect()
    print(f"수집: {len(results)}개\n")
    for i, r in enumerate(results, 1):
        print(f"[{i}] {r['title']}")
        print(f"    URL: {r['url']}")
        print(f"    Stars today: {r['stars_today']} ({r.get('stars_text', '')})")
        if r.get("image_url"):
            print(f"    image: {r['image_url'][:80]}")
        print(f"    desc: {r['summary'][:80]}")
