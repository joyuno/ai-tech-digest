"""카카오톡 알림 발송기"""

import json
import requests
from typing import Dict, Any
from pathlib import Path
from jinja2 import Template


class KakaoNotifier:
    """카카오톡 나에게 보내기 API"""

    TOKEN_URL = "https://kauth.kakao.com/oauth/token"
    SEND_URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    def __init__(self, rest_api_key: str, refresh_token: str):
        self.rest_api_key = rest_api_key
        self.refresh_token = refresh_token
        self.access_token = None

    def _refresh_access_token(self) -> bool:
        """액세스 토큰 갱신"""
        if not self.rest_api_key or not self.refresh_token:
            print("⚠️ 카카오 API 키 또는 리프레시 토큰 없음")
            return False

        data = {
            "grant_type": "refresh_token",
            "client_id": self.rest_api_key,
            "refresh_token": self.refresh_token,
        }

        try:
            response = requests.post(self.TOKEN_URL, data=data)
            response.raise_for_status()
            tokens = response.json()
            self.access_token = tokens.get("access_token")
            return True
        except Exception as e:
            print(f"⚠️ 토큰 갱신 실패: {e}")
            return False

    def send(self, summary: Dict[str, Any]) -> bool:
        """카카오톡 메시지 발송"""
        if not self._refresh_access_token():
            return False

        # 메시지 생성
        message = self._build_message(summary)

        # 템플릿 객체 생성
        template_object = {
            "object_type": "text",
            "text": message[:1000],  # 최대 1000자
            "link": {
                "web_url": f"https://joyuno.github.io/ai/tech/{summary['date']}-ai-tech-digest",
                "mobile_web_url": f"https://joyuno.github.io/ai/tech/{summary['date']}-ai-tech-digest",
            },
        }

        headers = {"Authorization": f"Bearer {self.access_token}"}
        data = {"template_object": json.dumps(template_object)}

        try:
            response = requests.post(self.SEND_URL, headers=headers, data=data)
            response.raise_for_status()
            print("✅ 카카오톡 발송 성공")
            return True
        except Exception as e:
            print(f"⚠️ 카카오톡 발송 실패: {e}")
            return False

    def _build_message(self, summary: Dict[str, Any]) -> str:
        """카카오톡 메시지 생성"""
        template_path = Path(__file__).parent.parent.parent / "templates" / "kakao_message.j2"

        if template_path.exists():
            with open(template_path, "r", encoding="utf-8") as f:
                template = Template(f.read())
            return template.render(
                date=summary["date"],
                sources=summary.get("sources", []),
                blog_url=f"https://joyuno.github.io/{summary['date']}-ai-tech-digest",
            )

        # 기본 메시지
        lines = [f"🤖 AI 기술 다이제스트 ({summary['date']})"]

        for source in summary.get("sources", [])[:4]:
            lines.append(f"\n{source['emoji']} {source['name']}")
            for item in source.get("items", [])[:1]:
                title = item.get("title", "")[:40]
                lines.append(f"• {title}...")

        lines.append(f"\n👉 https://joyuno.github.io")

        return "\n".join(lines)
