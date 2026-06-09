# Publishers Package
#
# kakao_notifier 는 jinja2 의존 — weekly 흐름엔 불필요하므로 lazy 처리.
# (weekly pipeline 이 publishers 패키지 import 만으로 KakaoNotifier 까지 끌고 와
#  실패하던 문제 방지)

try:
    from .kakao_notifier import KakaoNotifier
except ImportError:
    KakaoNotifier = None  # type: ignore

from .jekyll_publisher import JekyllPublisher
from .weekly_papers_publisher import WeeklyPapersPublisher

__all__ = [
    "KakaoNotifier",
    "JekyllPublisher",
    "WeeklyPapersPublisher",
]
