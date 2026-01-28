"""GitHub Trending 수집기"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict


class GitHubTrendingCollector:
    """GitHub Trending 페이지에서 인기 AI 레포 수집"""

    def __init__(self, config: dict):
        self.base_url = "https://github.com/trending"
        self.languages = config.get("languages", ["", "python"])
        self.max_results = config.get("max_results", 5)

    def collect(self) -> List[Dict]:
        """Trending 페이지 스크래핑"""
        # TODO: 구현 필요
        results = []

        for lang in self.languages[:1]:  # 첫 번째 언어만
            url = f"{self.base_url}/{lang}" if lang else self.base_url

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "lxml")

                repos = soup.select("article.Box-row")

                for repo in repos[: self.max_results]:
                    # 레포 정보 파싱
                    name_elem = repo.select_one("h2 a")
                    desc_elem = repo.select_one("p")
                    stars_elem = repo.select_one("span.d-inline-block.float-sm-right")

                    if name_elem:
                        repo_name = name_elem.get_text(strip=True).replace("\n", "").replace(" ", "")
                        results.append({
                            "title": repo_name,
                            "url": f"https://github.com{name_elem.get('href', '')}",
                            "summary": desc_elem.get_text(strip=True) if desc_elem else "",
                            "stars": stars_elem.get_text(strip=True) if stars_elem else "",
                        })

            except Exception as e:
                print(f"GitHub Trending 스크래핑 실패: {e}")

        return results
