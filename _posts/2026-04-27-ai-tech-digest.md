---
layout: post
title: "mattpocock/skills 실무 Claude 에이전트 모음"
date: 2026-04-27
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.20796" target="_blank">LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


LLaDA2.0-Uni는 텍스트와 이미지를 동시에 이해하고 생성할 수 있는 새로운 통합 멀티모달 모델입니다. 시각 정보를 텍스트처럼 잘게 쪼개어 처리하는 독특한 확산(diffusion) LLM 아키텍처를 사용하여, 다양한 종류의 데이터를 하나의 모델에서 효율적으로 다룰 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.17295" target="_blank">LLaTiSA: Towards Difficulty-Stratified Time Series Reasoning from Visual Perception to Semantics</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


이 논문은 LLM이 시계열 데이터를 이해하는 데 어려움을 겪는 문제를 해결하고자 합니다. 이를 위해 시계열 추론(TSR)의 난이도를 4단계로 체계화하고, 모델 성능을 제대로 평가할 수 있는 새로운 데이터셋 HiTSR을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.20733" target="_blank">Near-Future Policy Optimization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>


강화학습 모델의 훈련 후 성능을 높이는 RLVR(verifiable rewards) 기법을 개선하는 새로운 방법을 제안합니다. 기존 방식들이 외부 데이터를 쓰거나 과거 데이터에 의존하는 한계를 넘어, 더 빠르고 효과적으로 모델을 최적화할 수 있는 전략을 제시합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.19859" target="_blank">DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


엣지 디바이스에서도 강력한 성능을 내는 소형 리서치 에이전트 DR-Venus를 소개합니다. 1만 개의 공개 데이터만을 활용하여 데이터 품질과 활용도를 높이는 훈련 기법으로, 작지만 뛰어난 4B 규모의 모델을 만드는 방법을 제시합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.21686" target="_blank">WorldMark: A Unified Benchmark Suite for Interactive Video World Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


최근 빠르게 발전하는 인터랙티브 비디오 생성 모델들을 공정하게 비교할 수 있는 통합 벤치마크 WorldMark를 제안합니다. 각기 다른 환경에서 평가되던 기존 모델들과 달리, 동일한 조건에서 성능을 측정하여 객관적인 비교를 가능하게 합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.21931" target="_blank">Seeing Fast and Slow: Learning the Flow of Time in Videos</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


이 연구는 AI 모델이 비디오 속 시간의 흐름을 이해하고 조작하는 방법을 학습하도록 합니다. 비디오가 빨리 감기 되었는지, 아니면 느리게 재생되는지를 파악하고, 원하는 속도로 비디오를 생성하는 능력을 키우는 것을 목표로 합니다.

<small><i data-lucide="user"></i> Yen-Siang Wu, Rundong Luo, Jingsen Zhu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.21889" target="_blank">TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale</a></h3>



대규모 클라우드 서비스에서 발생하는 수많은 고객 문의 데이터 속에서 실시간으로 위험 이벤트를 탐지하는 시스템 TingIS를 소개합니다. 노이즈가 많고 복잡한 고객 데이터를 분석하여, 서비스 장애를 빠르게 발견하고 대응할 수 있도록 돕습니다.

<small><i data-lucide="user"></i> Jun Wang, Ziyin Zhang, Rui Wang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.21921" target="_blank">Context Unrolling in Omni Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


텍스트, 이미지, 비디오, 3D 등 다양한 종류의 데이터를 함께 학습한 통합 멀티모달 모델 Omni를 소개합니다. Omni는 여러 형식의 정보를 종합적으로 추론한 뒤 예측을 내놓는 '컨텍스트 언롤링(Context Unrolling)' 능력을 보여주며, 이를 통해 더 깊이 있는 이해가 가능합니다.

<small><i data-lucide="user"></i> Ceyuan Yang, Zhijie Lin, Yang Zhao</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/mattpocock/skills" target="_blank">mattpocock/skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


실제 엔지니어들이 유용하게 사용할 수 있는 AI 에이전트 스킬 모음입니다. 개발자가 직접 자신의 Claude 사용 경험을 바탕으로 만든 프롬프트와 기법들을 공유합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Alishahryar1/free-claude-code" target="_blank">Alishahryar1/free-claude-code</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


강력한 코딩 성능을 자랑하는 Claude AI 모델을 터미널이나 VS Code 확장 기능 등을 통해 무료로 사용할 수 있게 해주는 도구입니다. 복잡한 설정 없이 간편하게 코드 생성 및 분석 기능을 활용할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/abhigyanpatwari/GitNexus" target="_blank">abhigyanpatwari/GitNexus</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


서버 없이 브라우저에서 바로 동작하는 코드 인텔리전스 엔진입니다. GitHub 저장소나 ZIP 파일을 입력하면 코드의 구조를 시각적인 지식 그래프로 만들어주고, 내장된 RAG 에이전트를 통해 코드에 대해 질문하며 탐색할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/PostHog/posthog" target="_blank">PostHog/posthog</a></h3>



성공적인 제품 개발을 위한 올인원 개발자 플랫폼입니다. 제품 분석, 세션 리플레이, 기능 플래그, A/B 테스트 등 제품 개발과 운영에 필요한 거의 모든 기능을 한곳에서 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/trycua/cua" target="_blank">trycua/cua</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


컴퓨터 데스크톱 환경을 직접 제어하는 AI 에이전트를 훈련하고 평가하기 위한 오픈소스 인프라입니다. macOS, Linux, Windows 등 다양한 운영체제에서 AI가 사람처럼 컴퓨터를 사용할 수 있도록 돕는 샌드박스, SDK, 벤치마크를 제공합니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/100-years-from-now-the-allowance" target="_blank">AI Weekly Issue #487: 100 years from now : The Allowance</a></h3>



AI 기술이 완전히 자리 잡은 100년 후의 미래를 상상하는 주간 시리즈의 한 편입니다. 이번 주제는 경제를 장악한 억만장자들이 사람들에게 '용돈'을 지급하며 사회적 불만을 잠재우려는 미래 사회의 모습을 그립니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>RAG</code> <code>Eval</code> <code>LoRA</code> <code>Small Language Model</code> <code>Agent</code> <code>Multimodal</code> <code>Claude</code> <code>AI Agent</code> 
</div>

---

