"""GitHub Trending 수집기 + README 대표 이미지 추출."""

import os
import re
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup


# README 안의 첫 이미지 — markdown ![alt](url) / <img src="..."> 둘 다 매칭
_MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(\s*([^)\s]+)", re.MULTILINE)
_HTML_IMG_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

# badge / shield 이미지는 보통 대표 이미지가 아님 — 거름
_SKIP_HOSTS = (
    "shields.io", "img.shields.io", "badge.fury.io", "badgen.net",
    "travis-ci", "circleci.com", "codecov.io", "coveralls.io",
    "github.com/.+?/workflows", "github-readme-stats",
)


def _is_badge(url: str) -> bool:
    u = url.lower()
    return any(h in u for h in (
        "shields.io", "badge.fury.io", "badgen.net",
        "travis-ci", "circleci", "codecov", "coveralls",
        "github-readme-stats", "actions/workflows", "/badge.svg",
    ))


def _resolve_relative(url: str, owner: str, repo: str, branch: str) -> str:
    """상대 경로 README 이미지를 raw.githubusercontent.com 절대 URL 로 변환."""
    if url.startswith(("http://", "https://", "//")):
        return url if not url.startswith("//") else "https:" + url
    # ./foo.png, /foo.png, foo.png
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

    # 1) GitHub API 의 default branch README — 자동으로 main / master 처리
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    try:
        r = requests.get(api_url, headers=headers, timeout=timeout)
        if r.status_code != 200:
            return None
        text = r.text
    except requests.RequestException:
        return None

    # default branch 알아내기 (raw URL resolution 위해)
    branch = "main"
    try:
        meta = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
            headers={"Accept": "application/vnd.github.v3+json", **({"Authorization": f"token {token}"} if token else {})},
            timeout=timeout,
        )
        if meta.status_code == 200:
            branch = meta.json().get("default_branch", "main") or "main"
    except requests.RequestException:
        pass

    # markdown 먼저, 그다음 HTML
    candidates: List[str] = []
    candidates.extend(_MD_IMG_RE.findall(text))
    candidates.extend(_HTML_IMG_RE.findall(text))

    for url in candidates:
        url = url.strip().split(" ")[0]   # `(url "title")` 형식 분리
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


class GitHubTrendingCollector:
    """GitHub Trending 페이지에서 인기 AI/ML 레포 수집"""

    # AI/ML 관련 키워드 (레포 이름, 설명, 언어에서 매칭)
    AI_KEYWORDS = {
        "ai", "llm", "machine-learning", "deep-learning", "gpt", "transformer",
        "neural", "ml", "bert", "diffusion", "stable-diffusion", "chatgpt",
        "langchain", "pytorch", "tensorflow", "keras", "scikit-learn",
        "openai", "anthropic", "claude", "gemini", "mistral", "llama",
        "embedding", "vector", "rag", "fine-tuning", "training", "model",
        "nlp", "computer-vision", "cv", "reinforcement-learning", "rl"
    }

    def __init__(self, config: dict):
        self.base_url = "https://github.com/trending"
        self.languages = config.get("languages", ["", "python"])
        self.max_results = config.get("max_results", 5)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def collect(self) -> List[Dict]:
        """Trending 페이지 스크래핑 + AI/ML 필터링 + README 첫 이미지 enrichment."""
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
        """레포지토리 정보 파싱"""
        try:
            # 레포 이름 및 URL
            name_elem = repo_element.select_one("h2 a")
            if not name_elem:
                return None

            repo_name = name_elem.get_text(strip=True).replace("\n", "").replace(" ", "")
            repo_url = f"https://github.com{name_elem.get('href', '')}"

            # 설명
            desc_elem = repo_element.select_one("p.col-9")
            description = desc_elem.get_text(strip=True) if desc_elem else ""

            # 언어
            lang_elem = repo_element.select_one("span[itemprop='programmingLanguage']")
            language = lang_elem.get_text(strip=True) if lang_elem else ""

            # 오늘의 stars (예: "123 stars today")
            stars_today = ""
            stars_span = repo_element.select("span.d-inline-block.float-sm-right")
            for span in stars_span:
                text = span.get_text(strip=True)
                if "stars today" in text or "star today" in text:
                    stars_today = text
                    break

            # stars 숫자만 추출 (예: "123 stars today" -> "123")
            stars_count = self._extract_stars_count(stars_today)

            return {
                "title": repo_name,
                "url": repo_url,
                "summary": description,
                "language": language,
                "stars_today": stars_count,
                "stars_text": stars_today
            }

        except Exception as e:
            print(f"레포 파싱 실패: {e}")
            return None

    def _extract_stars_count(self, stars_text: str) -> str:
        """stars 텍스트에서 숫자 추출 (예: '123 stars today' -> '123')"""
        if not stars_text:
            return "0"

        match = re.search(r'([\d,]+)', stars_text)
        if match:
            return match.group(1).replace(",", "")
        return "0"

    def _is_ai_related(self, repo: Dict) -> bool:
        """AI/ML 관련 레포인지 키워드로 필터링"""
        # 검색 대상 텍스트: 레포 이름 + 설명 + 언어
        search_text = (
            repo.get("title", "") + " " +
            repo.get("summary", "") + " " +
            repo.get("language", "")
        ).lower()

        # 키워드 중 하나라도 매칭되면 AI 관련으로 판단
        return any(keyword in search_text for keyword in self.AI_KEYWORDS)


if __name__ == "__main__":
    """단독 실행 테스트"""
    print("GitHub Trending Collector 테스트 시작...\n")

    # 테스트 설정
    config = {
        "languages": ["", "python"],  # 전체 + Python
        "max_results": 5
    }

    collector = GitHubTrendingCollector(config)

    try:
        results = collector.collect()

        print(f"수집된 AI/ML 레포: {len(results)}개\n")
        print("=" * 80)

        for idx, repo in enumerate(results, 1):
            print(f"\n[{idx}] {repo['title']}")
            print(f"    URL: {repo['url']}")
            print(f"    언어: {repo['language']}")
            print(f"    오늘의 Stars: {repo['stars_today']} ({repo['stars_text']})")
            print(f"    설명: {repo['summary'][:100]}...")

        print("\n" + "=" * 80)
        print("테스트 완료")

    except Exception as e:
        print(f"테스트 실패: {e}")
        import traceback
        traceback.print_exc()
