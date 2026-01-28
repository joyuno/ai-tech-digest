# Twitter Collector 사용 가이드

## 개요

Twitter API 무료 티어의 제한으로 인해 Nitter RSS 대안을 사용하여 트윗을 수집합니다.

## 현재 상황 (2024-2026)

- **Twitter API**: 무료 티어는 매우 제한적 (월 1,500 트윗)
- **Nitter**: 대부분의 인스턴스가 불안정하거나 작동 중단
- **대안**: XCancel, Twstalker 같은 서비스 사용 시도

## 기능

- 다중 RSS 서비스 폴백 지원
- 계정당 최대 트윗 수 제한
- HTML 태그 제거 및 텍스트 추출
- 제목(100자 요약), URL, 전체 내용, 발행일 반환
- 에러 처리 및 재시도
- 테스트용 모의 데이터 모드

## 사용 예시

### 기본 사용

```python
from collectors.twitter_collector import TwitterCollector

config = {
    "accounts": ["_akhaliq", "bindureddy"],
    "max_tweets_per_account": 5,
}

collector = TwitterCollector(config)
tweets = collector.collect()

for tweet in tweets:
    print(f"{tweet['author']}: {tweet['title']}")
    print(f"URL: {tweet['url']}")
```

### 모의 데이터 모드 (테스트용)

```python
config = {
    "accounts": ["_akhaliq", "bindureddy"],
    "max_tweets_per_account": 3,
    "use_mock_data": True,  # 모의 데이터 사용
}

collector = TwitterCollector(config)
tweets = collector.collect()
```

### 명령줄 테스트

```bash
# 실제 RSS 수집 시도
python3 src/collectors/twitter_collector.py

# 모의 데이터로 테스트
python3 src/collectors/twitter_collector.py --mock
```

## 반환 데이터 형식

```python
{
    "title": "트윗 내용 앞 100자...",
    "url": "https://twitter.com/username/status/...",
    "content": "전체 트윗 내용",
    "published": "2026-01-28T12:00:00",
    "author": "@username",
    "source": "twitter"  # 또는 "twitter_mock"
}
```

## 문제 해결

### RSS 서비스가 모두 실패하는 경우

1. **Nitter 인스턴스 확인**
   - https://github.com/zedeus/nitter/wiki/Instances 에서 작동하는 인스턴스 확인
   - `RSS_SERVICES` 리스트 업데이트

2. **모의 데이터 사용**
   - 테스트나 개발 중에는 `use_mock_data=True` 사용

3. **Twitter API 사용 고려**
   - 유료 플랜 사용 또는
   - Tweepy 라이브러리로 직접 구현

### 타임아웃 증가

```python
config = {
    "accounts": ["_akhaliq"],
    "timeout": 30,  # 기본값 15초에서 증가
}
```

## 주의사항

- RSS 서비스의 가용성은 보장되지 않음
- 너무 많은 요청 시 차단될 수 있음
- 계정 간 2초 대기 시간 설정됨
- SSL 인증서 검증 비활성화 (프록시 서비스 특성상)

## 대상 계정

기본 설정된 AI/ML 관련 영향력 있는 계정:

- **@_akhaliq** (AK): Papers with Code 큐레이터
- **@bindureddy** (Bindu Reddy): Abacus.AI CEO

다른 계정을 추가하려면 config의 `accounts` 리스트에 추가하세요.
