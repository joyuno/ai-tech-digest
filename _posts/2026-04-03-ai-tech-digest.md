---
layout: post
title: "무신사 Self-POS Zero-to-One — 직원 없는 계산대 경험 설계"
date: 2026-04-03
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "musinsa"
daily_title: "무신사 Self-POS — Zero to One 구축기: 직원이 사라진 계산대, 그 자리를 채운 경험 설계"
daily_url: "https://techblog.musinsa.com/%EB%AC%B4%EC%8B%A0%EC%82%AC-self-pos-zero-to-one-%EA%B5%AC%EC%B6%95%EA%B8%B0-%EC%A7%81%EC%9B%90%EC%9D%B4-%EC%82%AC%EB%9D%BC%EC%A7%84-%EA%B3%84%EC%82%B0%EB%8C%80-%EA%B7%B8-%EC%9E%90%EB%A6%AC%EB%A5%BC-%EC%B1%84%EC%9A%B4-%EA%B2%BD%ED%97%98-%EC%84%A4%EA%B3%84-f5030d7d2292?source=rss----f107b03c406e---4"
daily_keywords: ["Safety", "Agent", "Multimodal", "RAG", "Eval", "Vision", "LLM", "Tool Use", "Inference", "GPT"]
daily_image: ""
daily_image_kind: "none"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.24414" target="_blank">ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


이 논문은 오픈소스 에이전트인 OpenClaw의 보안 취약점을 해결하는 안전 시스템인 ClawKeeper를 제안합니다. 도구 통합이나 로컬 파일 접근과 같은 강력한 기능이 가져올 수 있는 데이터 유출 및 악성 코드 실행 등의 위협을 효과적으로 방어해 줘요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.00073" target="_blank">Terminal Agents Suffice for Enterprise Automation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


기업 업무 자동화에 복잡한 GUI 에이전트나 API 도구가 과연 필수적인지 의문을 제기하는 논문입니다. 단순히 터미널 접근 권한만 갖춘 코딩 에이전트로도 충분히 효율적이고 의미 있는 기업 작업을 자동화할 수 있다고 주장해요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.27460" target="_blank">Project Imaging-X: A Survey of 1000+ Open-Access Medical Imaging Datasets for Foundation Model Development</a></h3>



의료 영상 분야의 Foundation Model 발전을 돕기 위해 1,000개 이상의 오픈 액세스 의료 데이터셋을 조사한 리뷰 논문입니다. 엄격한 개인정보 문제로 데이터를 구하기 어려운 의료 인공지능 연구자들에게 아주 유용한 길잡이가 될 것입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.28407" target="_blank">MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


멀티모달 심층 연구 에이전트를 과정과 결과 양면에서 평가하는 새로운 벤치마크인 MiroEval을 소개합니다. 최종 결과물만 보거나 현실성이 떨어지던 기존 평가의 한계를 극복하여, 에이전트가 실제 연구를 얼마나 잘 수행하는지 꼼꼼하게 테스트할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25823" target="_blank">ViGoR-Bench: How Far Are Visual Generative Models From Zero-Shot Visual Reasoners?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


최신 시각 생성 모델들이 겉보기엔 화려하지만 실제 물리적, 공간적 추론에는 약하다는 점을 짚어내는 연구입니다. 이를 제대로 평가하기 위해 ViGoR라는 새로운 벤치마크를 도입하여 모델의 숨겨진 '논리적 사막' 현상을 정확하게 측정하려고 합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.01161" target="_blank">Reasoning Shift: How Context Silently Shortens LLM Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


불필요하게 긴 문맥이나 여러 번 이어지는 대화 속에서 LLM의 추론 능력이 어떻게 조용히 짧아지고 약해지는지 분석한 연구입니다. 다양한 시나리오를 통해 최신 추론 모델들이 가진 성능의 한계와 견고성을 체계적으로 평가했어요.

<small><i data-lucide="user"></i> Gleb Rodionov</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.01221" target="_blank">HippoCamp: Benchmarking Contextual Agents on Personal Computers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


개인용 컴퓨터 환경에서 에이전트가 얼마나 똑똑하게 파일을 관리하는지 평가하는 HippoCamp 벤치마크를 제안합니다. 일반적인 웹 작업이 아닌, 실제 사용자의 다양한 파일 속에서 맥락을 파악하고 추론하는 능력을 효과적으로 테스트할 수 있습니다.

<small><i data-lucide="user"></i> Zhe Yang, Shulin Tian, Kairui Hu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.01220" target="_blank">Universal YOCO for Efficient Depth Scaling</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LLM의 추론 효율을 높이기 위해 기존 Transformer의 계산 부담과 KV 캐시 문제를 해결한 Universal YOCO 구조를 제안합니다. 디코더 구조에 재귀 연산을 결합하여, 모델의 깊이를 늘려도 가볍고 빠르게 작동할 수 있도록 만들었어요.

<small><i data-lucide="user"></i> Yutao Sun, Li Dong, Tianzhu Ye</small>

</div>



---


## <i data-lucide="shirt"></i> 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%EB%AC%B4%EC%8B%A0%EC%82%AC-self-pos-zero-to-one-%EA%B5%AC%EC%B6%95%EA%B8%B0-%EC%A7%81%EC%9B%90%EC%9D%B4-%EC%82%AC%EB%9D%BC%EC%A7%84-%EA%B3%84%EC%82%B0%EB%8C%80-%EA%B7%B8-%EC%9E%90%EB%A6%AC%EB%A5%BC-%EC%B1%84%EC%9A%B4-%EA%B2%BD%ED%97%98-%EC%84%A4%EA%B3%84-f5030d7d2292?source=rss----f107b03c406e---4" target="_blank">무신사 Self-POS — Zero to One 구축기: 직원이 사라진 계산대, 그 자리를 채운 경험 설계</a></h3>



무신사 오프라인 매장의 긴 결제 대기 줄과 인건비 문제를 해결하기 위해 도입한 Self-POS 구축 경험을 공유한 글입니다. 현장 리서치부터 AI를 활용한 UX 설계, UI 컨셉까지 무에서 유를 만들어낸 실무자의 생생한 고민을 엿볼 수 있어요.

<small><i data-lucide="user"></i> Minsun</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/asgeirtj/system_prompts_leaks" target="_blank">asgeirtj/system_prompts_leaks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


ChatGPT, Claude, Gemini 등 유명 LLM들의 유출된 시스템 프롬프트를 모아둔 흥미로운 저장소입니다. 각 AI 모델이 내부적으로 어떤 규칙과 지침을 가지고 작동하는지 확인할 수 있으며 꾸준히 업데이트되고 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/sherlock-project/sherlock" target="_blank">sherlock-project/sherlock</a></h3>



사용자 이름(username) 하나만 입력하면 수많은 소셜 네트워크 플랫폼을 뒤져 동일한 계정을 찾아내 줍니다. 온라인상에서 특정 아이디의 활동 내역을 추적할 때 아주 유용하게 쓸 수 있는 오픈소스 도구예요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/sherlock-project/sherlock" target="_blank">sherlock-project/sherlock</a></h3>



사용자 이름 하나로 전 세계 다양한 소셜 미디어 플랫폼에서 동일 계정을 추적할 수 있는 강력한 오픈소스 도구입니다. 복잡한 설정 없이도 특정 사용자의 온라인 발자취를 쉽게 찾아낼 수 있도록 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/MervinPraison/PraisonAI" target="_blank">MervinPraison/PraisonAI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


24시간 쉬지 않고 일하는 나만의 AI 직원 팀을 만들 수 있는 로우코드 멀티 에이전트 프레임워크입니다. 100개 이상의 LLM을 지원하며, 복잡한 업무를 자동화해 텔레그램이나 디스코드 같은 메신저로 결과를 바로 받아볼 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/yusufkaraaslan/Skill_Seekers" target="_blank">yusufkaraaslan/Skill_Seekers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


공식 문서나 GitHub 저장소, PDF 파일 등을 Claude AI가 바로 사용할 수 있는 스킬로 쉽게 변환해 주는 도구입니다. 문서 내용 간의 자동 충돌 감지 기능까지 포함되어 있어 AI를 더욱 똑똑하게 활용할 수 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Safety</code> <code>Agent</code> <code>Multimodal</code> <code>RAG</code> <code>Eval</code> <code>Vision</code> <code>LLM</code> <code>Tool Use</code> <code>Inference</code> <code>GPT</code> 
</div>

---

