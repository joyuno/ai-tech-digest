---
layout: post
title: "AI 기술 다이제스트 - 2026-03-26"
date: 2026-03-26
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.22458" target="_blank">MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


문서 OCR 처리 시 발생하는 지연 시간과 오류 문제를 해결하기 위해 Diffusion 모델을 적용한 새로운 접근법을 제안합니다. 문서를 왼쪽에서 오른쪽으로 순차적으로 읽는 대신 역렌더링 관점에서 구조를 파악해 복잡한 문서도 빠르고 정확하게 분석합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.16932" target="_blank">Look Where It Matters: High-Resolution Crops Retrieval for Efficient VLMs</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">💻 개발 도구</span> 
</div>


VLM이 이미지를 처리할 때 정확도와 연산 효율성 사이의 균형을 찾아주는 AwaRes 프레임워크를 소개합니다. 저해상도로 전체 이미지를 먼저 파악한 후 중요한 부분만 고해상도로 잘라내어 분석하므로, 적은 연산 비용으로도 세부 정보를 놓치지 않습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.20278" target="_blank">OpenResearcher: A Fully Open Pipeline for Long-Horizon Deep Research Trajectory Synthesis</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


AI 연구 에이전트를 훈련시키기 위한 완전 개방형 데이터 생성 파이프라인인 OpenResearcher를 제안합니다. 기존의 유료 웹 API 대신 오프라인 환경에서 검색과 추론 과정을 수행하여, 복잡한 연구 궤적 데이터를 안정적이고 저렴하게 생성할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.23497" target="_blank">WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG</a></h3>



AI가 다양한 액션에 따른 환경 변화를 학습할 수 있도록 돕는 대규모 동적 세계 모델링 데이터셋입니다. 기존 데이터의 한계를 넘어 다양하고 의미 있는 액션과 명시적인 상태 정보를 제공하여, 생성형 ARPG와 같은 복잡한 환경을 더 잘 이해하게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.23483" target="_blank">SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


에이전트형 Multimodal LLM의 작업 처리 속도를 크게 높여주는 SpecEyes 프레임워크를 제안합니다. 시각적 인지와 도구 사용 등 단계별로 발생하는 지연 시간을 추측적 계획 방식을 통해 줄여주어, AI의 반응 속도와 동시 처리 능력을 대폭 향상시킵니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.23497" target="_blank">WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG</a></h3>



AI가 액션과 상태 변화의 관계를 깊이 있게 학습하도록 설계된 대규모 데이터셋입니다. 시각적 정보에만 의존하지 않고 명시적인 상태와 의미 있는 액션 데이터를 함께 제공하여, 향후 더 정교한 가상 세계 모델링에 폭넓게 활용될 수 있습니다.

<small>👤 Zhen Li, Zian Meng, Shuwei Shi</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.23499" target="_blank">DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models</a></h3>



노이즈나 화질 저하가 있는 실제 영상에서도 정확하게 움직임을 추적할 수 있는 DA-Flow 모델을 소개합니다. Diffusion 모델의 이미지 복원 능력을 활용해 영상의 손상 상태를 파악하고, 이를 바탕으로 한층 안정적인 광학 흐름 추정이 가능합니다.

<small>👤 Jaewon Min, Jaeeun Lee, Yeji Choi</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.23500" target="_blank">UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


추론과 이미지 생성을 결합한 통합 강화학습 프레임워크인 UniGRPO를 제안하는 연구입니다. AI가 이미지를 생성하기 전에 스스로 프롬프트를 분석하고 논리적으로 추론하는 과정을 거치게 하여, 사용자의 의도를 훨씬 더 정확하게 반영한 결과물을 만들어냅니다.

<small>👤 Jie Liu, Zilyu Ye, Linxiao Yuan</small>

</div>



---


## 💳 토스 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/place-metric-review" target="_blank">Metric Review, 실행을 이끌다</a></h3>



토스플레이스의 데이터 조직이 분석을 통해 얻은 인사이트를 실제 서비스 개선으로 연결하는 과정을 담은 글입니다. 단순하게 지표를 확인하는 것을 넘어, 구체적인 실행 계획을 이끌어내는 유용한 노하우를 친근하게 소개합니다.

<small>👤 토스</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


소셜 미디어나 웹에서 특정 주제에 대한 최근 30일간의 정보를 수집하고 분석해주는 AI 에이전트 스킬입니다. Reddit, YouTube, X 등 다양한 플랫폼을 한 번에 조사하여 신뢰할 수 있고 깔끔한 요약본을 만들어 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/deer-flow" target="_blank">bytedance/deer-flow</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


복잡한 리서치나 코딩 작업을 스스로 수행하는 오픈소스 에이전트 플랫폼입니다. 샌드박스와 메모리 기능, 하위 에이전트들을 유기적으로 결합하여 몇 시간이 걸리는 어려운 작업들도 알아서 척척 해결해 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/BerriAI/litellm" target="_blank">BerriAI/litellm</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🎯 신뢰성/안전</span> 
</div>


100개가 넘는 다양한 LLM API들을 마치 하나의 플랫폼처럼 쉽게 호출하고 관리할 수 있게 해주는 도구입니다. 비용 추적은 물론 트래픽 분산과 안전 장치까지 제공하여 여러 AI 모델을 효율적이고 안정적으로 다룰 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/letta-ai/claude-subconscious" target="_blank">letta-ai/claude-subconscious</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI 코딩 어시스턴트인 Claude에 마치 잠재의식이 있는 것처럼 지속적인 사고 능력을 부여하는 흥미로운 프로젝트입니다. 이를 통해 AI가 백그라운드에서 더 깊이 고민하고 최적의 코딩 해결책을 제시할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruflo" target="_blank">ruvnet/ruflo</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude 모델을 기반으로 여러 AI 에이전트를 하나로 묶어 지휘할 수 있는 강력한 오케스트레이션 플랫폼입니다. RAG 통합과 자율 워크플로우 기능을 통해 복잡한 기업용 다중 에이전트 시스템을 쉽고 효율적으로 구축하게 해줍니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Vision</code> <code>Retrieval</code> <code>Eval</code> <code>Reasoning</code> <code>Agent</code> <code>LLM</code> <code>Prompt</code> <code>AI Agent</code> <code>RAG</code> <code>Guardrails</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>