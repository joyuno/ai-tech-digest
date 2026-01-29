"""중복 방지를 위한 수집 이력 추적기"""

import json
import requests
import base64
from typing import Set, Dict, List
from datetime import datetime


class DedupTracker:
    """GitHub에 수집 이력을 저장하여 중복 방지"""

    def __init__(self, gh_token: str, repo: str, branch: str = "gh-pages"):
        self.gh_token = gh_token
        self.repo = repo
        self.branch = branch
        self.tracker_file = "collected_urls.json"
        self.api_base = f"https://api.github.com/repos/{repo}/contents"
        self._collected_urls: Dict[str, Set[str]] = {}
        self._loaded = False

    def _load(self):
        """GitHub에서 수집 이력 로드"""
        if self._loaded:
            return

        try:
            url = f"{self.api_base}/{self.tracker_file}"
            headers = {
                "Authorization": f"token {self.gh_token}",
                "Accept": "application/vnd.github.v3+json",
            }

            response = requests.get(url, headers=headers, params={"ref": self.branch})

            if response.status_code == 200:
                content = response.json().get("content", "")
                decoded = base64.b64decode(content).decode("utf-8")
                data = json.loads(decoded)
                # Set으로 변환
                for source, urls in data.items():
                    self._collected_urls[source] = set(urls)
                print(f"  📂 수집 이력 로드 완료")
            else:
                print(f"  📂 수집 이력 없음 (새로 시작)")
                self._collected_urls = {}

        except Exception as e:
            print(f"  ⚠️ 수집 이력 로드 실패: {e}")
            self._collected_urls = {}

        self._loaded = True

    def is_duplicate(self, source: str, url: str) -> bool:
        """URL이 이미 수집된 것인지 확인"""
        self._load()
        return url in self._collected_urls.get(source, set())

    def filter_new_items(self, source: str, items: List[Dict]) -> List[Dict]:
        """새로운 항목만 필터링"""
        self._load()

        collected = self._collected_urls.get(source, set())
        new_items = []

        for item in items:
            url = item.get("url", "")
            if url and url not in collected:
                new_items.append(item)

        if len(new_items) < len(items):
            print(f"    중복 제거: {len(items) - len(new_items)}개 스킵")

        return new_items

    def mark_collected(self, source: str, urls: List[str]):
        """수집된 URL 기록"""
        self._load()

        if source not in self._collected_urls:
            self._collected_urls[source] = set()

        self._collected_urls[source].update(urls)

    def save(self):
        """수집 이력 저장"""
        if not self.gh_token:
            return

        try:
            # Set을 List로 변환 (JSON 직렬화)
            data = {}
            for source, urls in self._collected_urls.items():
                # 최근 100개만 유지 (메모리 관리)
                data[source] = list(urls)[-100:]

            content = json.dumps(data, ensure_ascii=False, indent=2)
            encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

            url = f"{self.api_base}/{self.tracker_file}"
            headers = {
                "Authorization": f"token {self.gh_token}",
                "Accept": "application/vnd.github.v3+json",
            }

            # 기존 파일 SHA 확인
            sha = None
            response = requests.get(url, headers=headers, params={"ref": self.branch})
            if response.status_code == 200:
                sha = response.json().get("sha")

            # 파일 업데이트
            payload = {
                "message": f"📝 수집 이력 업데이트 - {datetime.now().strftime('%Y-%m-%d')}",
                "content": encoded,
                "branch": self.branch,
            }
            if sha:
                payload["sha"] = sha

            response = requests.put(url, headers=headers, json=payload)
            if response.status_code in [200, 201]:
                print(f"  💾 수집 이력 저장 완료")
            else:
                print(f"  ⚠️ 수집 이력 저장 실패: {response.status_code}")

        except Exception as e:
            print(f"  ⚠️ 수집 이력 저장 실패: {e}")
