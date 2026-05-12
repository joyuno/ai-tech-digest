"""Jekyll 블로그 발행기"""

import base64
import re
import requests
from typing import Dict, Any, Set
from pathlib import Path
from jinja2 import Template
from datetime import datetime, timedelta


class JekyllPublisher:
    """GitHub API를 통한 Jekyll 블로그 포스트 발행"""

    def __init__(self, gh_token: str, repo: str, branch: str = "gh-pages"):
        self.gh_token = gh_token
        self.repo = repo  # "owner/repo" 형식
        self.branch = branch
        self.api_base = f"https://api.github.com/repos/{repo}/contents"

    def fetch_recent_daily_titles(self, days: int = 14) -> Set[str]:
        """최근 N일치 게시된 representative title 모음 (오늘 제외).

        scoring.select_representative 의 seen_titles 인자로 그대로 넘기면
        과거 며칠 대표였던 항목이 또 1순위로 뽑히는 것을 방지한다.
        네트워크/파싱 실패는 무시하고 부분 결과라도 반환 — 페널티 일부 적용이
        '전혀 미적용' 보다 낫다. raw.githubusercontent.com 은 공개 repo 면 토큰 불필요.
        """
        seen: Set[str] = set()
        today = datetime.now().date()
        base = f"https://raw.githubusercontent.com/{self.repo}/{self.branch}/_posts"
        for i in range(1, max(1, days) + 1):
            d = today - timedelta(days=i)
            url = f"{base}/{d.isoformat()}-ai-tech-digest.md"
            try:
                r = requests.get(url, timeout=5)
                if r.status_code != 200:
                    continue
                title = self._extract_daily_title(r.text)
                if title:
                    seen.add(title)
            except Exception:
                continue
        return seen

    @staticmethod
    def _extract_daily_title(content: str) -> str:
        """Jekyll frontmatter 에서 daily_title 값만 뽑아낸다 (간단 파서)."""
        if not content.startswith("---"):
            return ""
        end = content.find("\n---", 3)
        if end == -1:
            return ""
        for line in content[3:end].split("\n"):
            m = re.match(r'\s*daily_title\s*:\s*(.+?)\s*$', line)
            if not m:
                continue
            value = m.group(1).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            return value
        return ""

    def publish(self, summary: Dict[str, Any]) -> bool:
        """Jekyll 포스트 발행"""
        if not self.gh_token:
            print("⚠️ GitHub 토큰 없음")
            return False

        # 포스트 내용 생성
        content = self._build_post(summary)
        date = summary.get("date", datetime.now().strftime("%Y-%m-%d"))
        filename = f"_posts/{date}-ai-tech-digest.md"

        # GitHub API로 파일 생성/업데이트
        return self._create_or_update_file(filename, content)

    def _build_post(self, summary: Dict[str, Any]) -> str:
        """Jekyll 포스트 생성"""
        template_path = Path(__file__).parent.parent.parent / "templates" / "jekyll_post.j2"

        if template_path.exists():
            with open(template_path, "r", encoding="utf-8") as f:
                template = Template(f.read())

            # 상위 키워드 추출
            top_keywords = []
            for source in summary.get("sources", []):
                for item in source.get("items", []):
                    for cat in item.get("categories", []):
                        kw = cat.get("matched_keyword", "")
                        if kw and kw not in top_keywords:
                            top_keywords.append(kw)

            return template.render(
                date=summary["date"],
                headline=summary.get("headline", "").strip(),
                sources=summary.get("sources", []),
                top_keywords=top_keywords[:10],
                representative=summary.get("representative") or {},
            )

        # 기본 포스트
        return self._default_post(summary)

    def _default_post(self, summary: Dict[str, Any]) -> str:
        """기본 포스트 포맷"""
        date = summary.get("date", datetime.now().strftime("%Y-%m-%d"))

        lines = [
            "---",
            "layout: post",
            f'title: "AI 기술 다이제스트 - {date}"',
            f"date: {date}",
            "categories: [AI, Tech]",
            "tags: [AI, LLM, 트렌드]",
            "---",
            "",
            "> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.",
            "",
        ]

        for source in summary.get("sources", []):
            lines.append(f"## {source['emoji']} {source['name']}")
            lines.append("")
            for item in source.get("items", []):
                lines.append(f"### [{item.get('title', '')}]({item.get('url', '')})")
                lines.append(f"- **요약**: {item.get('summary', '')[:200]}...")
                lines.append("")
            lines.append("---")
            lines.append("")

        return "\n".join(lines)

    def _create_or_update_file(self, path: str, content: str) -> bool:
        """GitHub API로 파일 생성/업데이트"""
        url = f"{self.api_base}/{path}"
        headers = {
            "Authorization": f"token {self.gh_token}",
            "Accept": "application/vnd.github.v3+json",
        }

        # 기존 파일 확인 (SHA 필요)
        sha = None
        try:
            response = requests.get(url, headers=headers, params={"ref": self.branch})
            if response.status_code == 200:
                sha = response.json().get("sha")
        except Exception:
            pass

        # 파일 생성/업데이트
        data = {
            "message": f"📝 AI Tech Digest - {datetime.now().strftime('%Y-%m-%d')}",
            "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
            "branch": self.branch,
        }
        if sha:
            data["sha"] = sha

        try:
            response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()
            print(f"✅ Jekyll 포스트 발행 성공: {path}")
            return True
        except Exception as e:
            print(f"⚠️ Jekyll 발행 실패: {e}")
            return False
