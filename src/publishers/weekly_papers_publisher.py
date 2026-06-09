"""주간 논문 다이제스트 발행기 — JekyllPublisher 의 _create_or_update_file 만 재활용."""
import base64
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import requests
from jinja2 import Template

from .jekyll_publisher import JekyllPublisher


class WeeklyPapersPublisher(JekyllPublisher):
    """JekyllPublisher 상속 — gh-pages 브랜치 · /ai-tech-digest/_posts/ 에 발행.

    daily digest 의 self-host image 로직은 사용하지 않음 (논문 글에는 OG 이미지 없음).
    파일명 suffix: -weekly-papers.md
    """

    TEMPLATE_NAME = "weekly_papers_post.j2"
    FILENAME_SUFFIX = "weekly-papers"

    def publish_weekly(self, data: Dict[str, Any]) -> bool:
        """data 구조:
          - geeknews_topic_id, geeknews_url, geeknews_title
          - intro (str), papers (List[Dict])
          - date (선택, 'YYYY-MM-DD')
        """
        if not self.gh_token:
            print("⚠️ GitHub 토큰 없음 — 발행 스킵")
            return False
        if not data.get("papers"):
            print("⚠️ 발행 대상 논문 0건 — 스킵")
            return False

        date = data.get("date") or datetime.now().strftime("%Y-%m-%d")
        content = self._build_post(data, date)
        filename = f"_posts/{date}-{self.FILENAME_SUFFIX}.md"
        print(f"  📝 발행 대상 파일: {filename}")
        return self._create_or_update_file(filename, content)

    def _build_post(self, data: Dict[str, Any], date: str) -> str:  # noqa: D401
        template_path = (
            Path(__file__).parent.parent.parent / "templates" / self.TEMPLATE_NAME
        )
        if not template_path.exists():
            raise FileNotFoundError(f"템플릿 없음: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        post_title = self._derive_title(data, date)
        return template.render(
            date=date,
            post_title=post_title,
            intro=data.get("intro", "").strip() or "_(트렌드 도입 생성 실패)_",
            papers=data.get("papers", []),
            geeknews_url=data.get("geeknews_url", ""),
            geeknews_title=data.get("geeknews_title", ""),
            geeknews_topic_id=data.get("geeknews_topic_id", ""),
        )

    @staticmethod
    def _derive_title(data: Dict[str, Any], date: str) -> str:
        """발행 제목 — GeekNews 의 [날짜 범위] 부분 보존, 없으면 fallback."""
        gn_title = (data.get("geeknews_title") or "").strip()
        if "AI/ML 논문" in gn_title:
            return gn_title
        return f"이번 주에 살펴볼 만한 AI/ML 논문 모음 ({date})"

    # 발행 후 dry-run 검증/디버깅용
    def render_only(self, data: Dict[str, Any], date: str = "") -> str:
        date = date or datetime.now().strftime("%Y-%m-%d")
        return self._build_post(data, date)
