"""주간 기술뉴스 다이제스트 발행기 — JekyllPublisher 의 _create_or_update_file 재활용."""
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from jinja2 import Template

from .jekyll_publisher import JekyllPublisher


class WeeklyNewsPublisher(JekyllPublisher):
    TEMPLATE_NAME = "weekly_news_post.j2"
    FILENAME_SUFFIX = "tech-weekly"  # URL slug에 매체명(geeknews) 미노출

    def post_path(self, date: str) -> str:
        return f"_posts/{date}-{self.FILENAME_SUFFIX}.md"

    def publish_weekly(self, data: Dict[str, Any], date: str) -> bool:
        if not self.gh_token:
            print("⚠️ GitHub 토큰 없음 — 발행 스킵")
            return False
        if not data.get("items"):
            print("⚠️ 발행 대상 뉴스 0건 — 스킵")
            return False
        content = self.render(data, date)
        path = self.post_path(date)
        print(f"  📝 발행 대상 파일: {path}")
        return self._create_or_update_file(path, content)

    def render(self, data: Dict[str, Any], date: str) -> str:
        template_path = Path(__file__).parent.parent.parent / "templates" / self.TEMPLATE_NAME
        if not template_path.exists():
            raise FileNotFoundError(f"템플릿 없음: {template_path}")
        template = Template(template_path.read_text(encoding="utf-8"))
        post_title = f"이번 주 개발·기술 소식 핵심 요약 ({date})"
        return template.render(
            date=date,
            post_title=post_title,
            weekly_id=data.get("weekly_id", ""),
            intro=(data.get("intro") or "").strip(),
            items=data.get("items", []),
        )
