"""X (Twitter) 수집기 - Nitter/XCancel RSS 사용

Twitter API 무료 티어 제한으로 인해 대안 RSS 서비스 사용:
- Nitter: Twitter 프론트엔드 (대부분 불안정)
- XCancel: Twitter 뷰어
- Twstalker: Twitter RSS 서비스

주의사항:
1. 대부분의 Nitter 인스턴스는 2024년 이후 불안정
2. RSS 서비스가 모두 실패할 경우 빈 리스트 반환
3. use_mock_data=True 옵션으로 테스트용 모의 데이터 사용 가능

사용 예시:
    config = {
        "accounts": ["_akhaliq", "bindureddy"],
        "max_tweets_per_account": 5,
        "use_mock_data": False,  # True로 설정하면 모의 데이터 사용
    }
    collector = TwitterCollector(config)
    tweets = collector.collect()
"""

import feedparser
import time
import urllib.request
import ssl
from typing import List, Dict, Optional
from datetime import datetime


class TwitterCollector:
    """X (Twitter)에서 AI 관련 트윗 수집 (Nitter/XCancel RSS 사용)

    Twitter API 무료 티어 제한을 우회하기 위해 Nitter RSS를 사용합니다.
    대상 계정: @_akhaliq, @bindureddy (기본값)
    """

    # Twitter RSS 서비스 목록 (폴백 지원)
    # 순서대로 시도하며, 첫 번째 성공한 서비스 사용
    RSS_SERVICES = [
        # Twstalker (비교적 안정적)
        ("https://twstalker.com", "/rss"),

        # XCancel (Twitter 뷰어)
        ("https://xcancel.com", "/rss"),

        # Nitter 인스턴스들 (2024년 이후 불안정)
        # Twitter의 API 정책 변경으로 많은 인스턴스가 작동 중단
        ("https://nitter.poast.org", "/rss"),
        ("https://nitter.net", "/rss"),
        ("https://nitter.privacydev.net", "/rss"),
        ("https://nitter.cz", "/rss"),
        ("https://nitter.lucabased.xyz", "/rss"),
        ("https://nitter.moomoo.me", "/rss"),
        ("https://bird.habedieeh.re", "/rss"),
    ]

    def __init__(self, config: dict):
        """
        Args:
            config (dict): 설정 딕셔너리
                - accounts (list): Twitter 계정 목록 (문자열 또는 딕셔너리)
                - max_tweets_per_account (int): 계정당 최대 트윗 수 (기본값: 5)
                - timeout (int): HTTP 요청 타임아웃 초 (기본값: 15)
                - use_mock_data (bool): 테스트용 모의 데이터 사용 여부 (기본값: False)
        """
        raw_accounts = config.get("accounts", ["_akhaliq", "bindureddy"])
        # 딕셔너리 형태도 지원 ({"username": "xxx"} 또는 문자열)
        self.accounts = []
        for acc in raw_accounts:
            if isinstance(acc, dict):
                self.accounts.append(acc.get("username", ""))
            else:
                self.accounts.append(str(acc))
        self.max_tweets = config.get("max_tweets_per_account", 5)
        self.timeout = config.get("timeout", 15)
        self.use_mock_data = config.get("use_mock_data", False)

    def _fetch_rss(self, username: str, service: tuple) -> Optional[feedparser.FeedParserDict]:
        """특정 RSS 서비스에서 피드 가져오기"""
        try:
            base_url, path_suffix = service
            rss_url = f"{base_url}/{username}{path_suffix}"
            print(f"  시도: {rss_url}")

            # SSL 컨텍스트 생성 (인증서 검증 비활성화)
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            # User-Agent 헤더 추가
            req = urllib.request.Request(
                rss_url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'application/rss+xml, application/xml, text/xml, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                }
            )

            with urllib.request.urlopen(req, timeout=self.timeout, context=ssl_context) as response:
                content = response.read()

            feed = feedparser.parse(content)

            # 피드가 유효한지 확인
            if hasattr(feed, 'entries') and len(feed.entries) > 0:
                print(f"  ✓ 성공: {len(feed.entries)}개 트윗 발견")
                return feed
            else:
                print(f"  ✗ 빈 피드")
                return None

        except urllib.error.HTTPError as e:
            print(f"  ✗ HTTP {e.code}: {e.reason}")
            return None
        except urllib.error.URLError as e:
            print(f"  ✗ 연결 실패: {str(e.reason)}")
            return None
        except Exception as e:
            print(f"  ✗ 에러: {type(e).__name__}")
            return None

    def _fetch_user_tweets(self, username: str) -> List[Dict]:
        """사용자의 트윗을 여러 RSS 서비스에서 시도하여 가져오기"""
        username = username.lstrip("@")  # @ 제거

        for service in self.RSS_SERVICES:
            feed = self._fetch_rss(username, service)

            if feed and hasattr(feed, 'entries') and len(feed.entries) > 0:
                return self._parse_feed(feed, username)

            time.sleep(0.5)  # 서비스 간 대기

        print(f"⚠️ @{username}: 모든 RSS 서비스 실패")
        return []

    def _parse_feed(self, feed: feedparser.FeedParserDict, username: str) -> List[Dict]:
        """RSS 피드를 파싱하여 트윗 데이터 추출"""
        results = []

        for entry in feed.entries[:self.max_tweets]:
            try:
                # 트윗 내용
                content = entry.get("description", "") or entry.get("summary", "")

                # HTML 태그 제거 (간단한 방법)
                import re
                content_text = re.sub(r'<[^>]+>', '', content)
                content_text = content_text.strip()

                # 제목: 트윗 내용 앞 100자
                title = content_text[:100]
                if len(content_text) > 100:
                    title += "..."

                # URL
                url = entry.get("link", "")

                # 발행일
                published = entry.get("published", "")
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    try:
                        dt = datetime(*entry.published_parsed[:6])
                        published = dt.isoformat()
                    except:
                        pass

                results.append({
                    "title": title,
                    "url": url,
                    "content": content_text,
                    "published": published,
                    "author": f"@{username}",
                    "source": "twitter",
                })

            except Exception as e:
                print(f"  트윗 파싱 에러: {str(e)}")
                continue

        return results

    def _get_mock_data(self, username: str) -> List[Dict]:
        """테스트용 모의 데이터 반환"""
        from datetime import datetime, timedelta

        mock_tweets = []
        base_time = datetime.now()

        for i in range(min(self.max_tweets, 3)):
            tweet_time = base_time - timedelta(hours=i * 2)
            mock_tweets.append({
                "title": f"[MOCK] Latest AI research on diffusion models and transformers (tweet {i+1})...",
                "url": f"https://twitter.com/{username}/status/mock{i+1}",
                "content": f"[MOCK DATA] This is a mock tweet from @{username}. Latest AI research on diffusion models and transformers shows significant improvements in image generation quality. Paper: arxiv.org/abs/2401.xxxxx #AI #MachineLearning",
                "published": tweet_time.isoformat(),
                "author": f"@{username}",
                "source": "twitter_mock",
            })

        return mock_tweets

    def collect(self) -> List[Dict]:
        """지정된 계정들의 최신 트윗 수집"""
        all_results = []

        mode = "모의 데이터" if self.use_mock_data else "Nitter/XCancel RSS"
        print(f"\n🐦 Twitter 수집 시작 ({mode} 사용)")
        print(f"   대상 계정: {', '.join(['@' + a.lstrip('@') for a in self.accounts])}")
        print(f"   계정당 최대: {self.max_tweets}개 트윗\n")

        for username in self.accounts:
            if not username:
                continue

            username = str(username).lstrip('@')
            print(f"📥 @{username} 수집 중...")

            if self.use_mock_data:
                tweets = self._get_mock_data(username)
                print(f"   ✓ 모의 데이터 생성: {len(tweets)}개")
            else:
                tweets = self._fetch_user_tweets(username)

            all_results.extend(tweets)
            print(f"   수집 완료: {len(tweets)}개\n")

            if not self.use_mock_data:
                time.sleep(2)  # 계정 간 대기

        print(f"✅ Twitter 수집 완료: 총 {len(all_results)}개 트윗\n")
        return all_results


if __name__ == "__main__":
    """테스트 실행"""
    import sys

    print("=" * 60)
    print("Twitter Collector 테스트")
    print("=" * 60)

    # 모드 선택
    use_mock = len(sys.argv) > 1 and sys.argv[1] == "--mock"

    if use_mock:
        print("\n⚠️  모의 데이터 모드 (실제 RSS 수집 없음)")
    else:
        print("\n🔍 실제 RSS 수집 모드")
        print("    (실패 시 --mock 옵션으로 모의 데이터 테스트 가능)")

    # 설정
    config = {
        "accounts": ["_akhaliq", "bindureddy"],
        "max_tweets_per_account": 3,
        "use_mock_data": use_mock,
    }

    # 수집기 생성 및 실행
    collector = TwitterCollector(config)
    results = collector.collect()

    # 결과 출력
    print("\n" + "=" * 60)
    print(f"수집 결과: {len(results)}개 트윗")
    print("=" * 60)

    if len(results) == 0:
        print("\n⚠️  수집된 트윗이 없습니다.")
        if not use_mock:
            print("    모의 데이터로 테스트하려면: python3 twitter_collector.py --mock")
    else:
        for i, tweet in enumerate(results, 1):
            print(f"\n[{i}] {tweet.get('author', 'Unknown')}")
            print(f"제목: {tweet.get('title', 'N/A')}")
            print(f"URL: {tweet.get('url', 'N/A')}")
            print(f"발행: {tweet.get('published', 'N/A')}")
            print(f"내용 (앞 200자): {tweet.get('content', '')[:200]}...")

    print("\n" + "=" * 60)
    print("테스트 완료")
    print("=" * 60)
