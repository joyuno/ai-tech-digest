"""AI Weekly 뉴스레터 수집기"""

import feedparser
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import re
from datetime import datetime


class AIWeeklyCollector:
    """AI Weekly RSS 수집 (RSS 실패시 웹 스크래핑 폴백)"""

    def __init__(self, config: dict):
        self.rss_url = config.get("rss_url", "https://aiweekly.co/issues.rss")
        self.alternative_urls = [
            "https://aiweekly.co/issues.rss",
            "https://aiweekly.co/feed.xml",
            "https://aiweekly.co/rss",
        ]
        self.web_url = "https://aiweekly.co/issues"
        self.max_results = config.get("max_results", 1)
        self.timeout = config.get("timeout", 10)

    def collect(self) -> List[Dict]:
        """RSS 피드에서 최신 뉴스레터 수집 (실패시 웹 스크래핑)"""
        # 1. RSS 피드 시도
        results = self._try_rss_feeds()

        # 2. RSS 실패시 웹 스크래핑 폴백
        if not results:
            print("RSS 피드 접근 실패, 웹 스크래핑 시도 중...")
            results = self._scrape_website()

        return results

    def _try_rss_feeds(self) -> List[Dict]:
        """여러 RSS URL 시도"""
        for rss_url in self.alternative_urls:
            try:
                print(f"RSS 피드 시도: {rss_url}")
                feed = feedparser.parse(rss_url)

                # 피드 파싱 성공 여부 확인
                if feed.bozo == 0 and feed.entries:
                    print(f"RSS 피드 성공: {len(feed.entries)}개 엔트리 발견")
                    return self._parse_rss_entries(feed.entries)
                elif feed.entries:
                    # bozo이지만 엔트리가 있으면 사용
                    print(f"RSS 피드 부분 성공 (bozo): {len(feed.entries)}개 엔트리 발견")
                    return self._parse_rss_entries(feed.entries)

            except Exception as e:
                print(f"RSS 피드 실패 ({rss_url}): {e}")
                continue

        return []

    def _parse_rss_entries(self, entries: list) -> List[Dict]:
        """RSS 엔트리 파싱"""
        results = []

        for entry in entries[: self.max_results]:
            try:
                # 요약 추출 (여러 필드 시도)
                summary = ""
                if hasattr(entry, "summary"):
                    summary = entry.summary
                elif hasattr(entry, "description"):
                    summary = entry.description
                elif hasattr(entry, "content"):
                    if isinstance(entry.content, list) and len(entry.content) > 0:
                        summary = entry.content[0].get("value", "")
                    else:
                        summary = str(entry.content)

                # HTML 태그 제거
                summary = self._clean_html(summary)

                # 발행일 파싱
                published = ""
                if hasattr(entry, "published"):
                    published = entry.published
                elif hasattr(entry, "updated"):
                    published = entry.updated
                elif hasattr(entry, "pubDate"):
                    published = entry.pubDate

                results.append({
                    "title": entry.get("title", "").strip(),
                    "url": entry.get("link", "").strip(),
                    "summary": summary[:500].strip(),
                    "published": published,
                })

            except Exception as e:
                print(f"RSS 엔트리 파싱 실패: {e}")
                continue

        return results

    def _scrape_website(self) -> List[Dict]:
        """웹사이트 직접 스크래핑"""
        results = []

        try:
            print(f"웹 스크래핑 시도: {self.web_url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(self.web_url, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            # AI Weekly 아카이브 페이지 구조에서 최신 이슈 추출
            issues = soup.find_all("div", class_="issue-item", limit=self.max_results)

            # 다양한 패턴 시도
            if not issues:
                issues = soup.find_all("article", limit=self.max_results)
            if not issues:
                issues = soup.find_all("div", class_="post", limit=self.max_results)

            for issue in issues[: self.max_results]:
                try:
                    # 제목 추출
                    title_elem = issue.find(["h1", "h2", "h3", "a"])
                    title = title_elem.get_text().strip() if title_elem else "No Title"

                    # URL 추출
                    link_elem = issue.find("a", href=True)
                    url = link_elem["href"] if link_elem else ""
                    if url and not url.startswith("http"):
                        url = f"https://aiweekly.co{url}"

                    # 요약 추출
                    summary_elem = issue.find(["p", "div", "span"])
                    summary = summary_elem.get_text().strip() if summary_elem else ""
                    summary = self._clean_text(summary)

                    # 날짜 추출
                    date_elem = issue.find("time")
                    if not date_elem:
                        date_elem = issue.find(class_=re.compile(r"date|time"))
                    published = date_elem.get_text().strip() if date_elem else ""

                    results.append({
                        "title": title,
                        "url": url,
                        "summary": summary[:500],
                        "published": published,
                    })

                except Exception as e:
                    print(f"이슈 파싱 실패: {e}")
                    continue

            if results:
                print(f"웹 스크래핑 성공: {len(results)}개 수집")
            else:
                print("웹 스크래핑: 이슈를 찾지 못했습니다")

        except requests.exceptions.RequestException as e:
            print(f"웹 스크래핑 HTTP 오류: {e}")
        except Exception as e:
            print(f"웹 스크래핑 실패: {e}")

        return results

    def _clean_html(self, text: str) -> str:
        """HTML 태그 제거 및 텍스트 정리"""
        if not text:
            return ""

        # BeautifulSoup으로 HTML 태그 제거
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text(separator=" ")

        # 공백 정리
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _clean_text(self, text: str) -> str:
        """텍스트 정리"""
        if not text:
            return ""

        # 연속된 공백 제거
        text = re.sub(r"\s+", " ", text)
        # 특수문자 정리
        text = text.replace("\n", " ").replace("\r", "")
        return text.strip()


if __name__ == "__main__":
    """테스트 코드"""
    print("=" * 60)
    print("AI Weekly 수집기 테스트")
    print("=" * 60)

    # 설정
    config = {
        "rss_url": "https://aiweekly.co/issues.rss",
        "max_results": 3,
        "timeout": 10,
    }

    # 수집기 초기화
    collector = AIWeeklyCollector(config)

    # 수집 실행
    print("\n[수집 시작]")
    results = collector.collect()

    # 결과 출력
    print(f"\n[수집 완료] 총 {len(results)}개 수집\n")

    if results:
        for idx, item in enumerate(results, 1):
            print(f"\n--- Issue #{idx} ---")
            print(f"제목: {item['title']}")
            print(f"URL: {item['url']}")
            print(f"발행일: {item['published']}")
            print(f"요약: {item['summary'][:200]}...")
            print()
    else:
        print("\n[경고] 수집된 데이터가 없습니다.")
        print("가능한 원인:")
        print("1. RSS 피드가 존재하지 않거나 형식이 변경됨")
        print("2. 웹사이트 구조가 변경됨")
        print("3. 네트워크 연결 문제")

    print("=" * 60)
    print("테스트 완료")
    print("=" * 60)
