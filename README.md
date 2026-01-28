# AI Tech Digest 🤖

AI 기술 온톨로지 기반 자동 트렌드 수집 & 요약 시스템

## 기능

- **자동 수집**: arXiv, Hugging Face, X(Twitter), 토스 기술블로그, GitHub Trending, AI Weekly
- **온톨로지 분류**: AI 기술 키워드 기반 자동 분류
- **AI 요약**: Gemini 3 Pro로 한국어 요약
- **자동 알림**: 매일 카카오톡으로 다이제스트 발송
- **블로그 포스팅**: Jekyll 기반 GitHub Pages 자동 업로드

## 설치

```bash
pip install -r requirements.txt
```

## 설정

### 환경 변수 (GitHub Secrets)

```
KAKAO_REST_API_KEY      # 카카오 REST API 키
KAKAO_REFRESH_TOKEN     # 카카오 리프레시 토큰
GEMINI_API_KEY          # Gemini API 키
GH_PAT                  # GitHub Personal Access Token
TWITTER_BEARER_TOKEN    # Twitter API Bearer Token (선택)
```

### 설정 파일

- `config/sources.yaml`: 데이터 소스 설정
- `config/ontology.yaml`: AI 기술 온톨로지 정의

## 실행

### 로컬 실행
```bash
python src/main.py
```

### GitHub Actions
매일 오전 9시(KST) 자동 실행

## 프로젝트 구조

```
ai-tech-digest/
├── .github/workflows/
│   └── daily-digest.yml
├── src/
│   ├── collectors/          # 데이터 수집기
│   ├── processors/          # 처리기 (분류, 요약)
│   ├── publishers/          # 발행기 (카카오, Jekyll)
│   └── main.py
├── config/
│   ├── ontology.yaml
│   └── sources.yaml
├── templates/
│   ├── jekyll_post.j2
│   └── kakao_message.j2
└── requirements.txt
```

## 온톨로지

```
🧠 모델/아키텍처  - LLM, Multimodal, SLM, MoE, Reasoning Models
🔧 학습/최적화    - Fine-tuning, RLHF, Quantization, Synthetic Data
🎯 신뢰성/안전    - Hallucination, Alignment, Jailbreak, Factuality
🔍 추론/검색      - RAG, CoT, Tool Use, Long Context
🤖 에이전트       - AI Agents, Multi-Agent, Computer Use
💻 개발 도구      - AI Coding, Prompt Engineering, Eval
```

## License

MIT
