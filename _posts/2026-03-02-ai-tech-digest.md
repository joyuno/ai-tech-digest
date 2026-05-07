---
layout: post
title: "airi 트렌드 지속 — Waifu AI를 내 OS에서 굴리는 흐름"
date: 2026-03-02
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "The Trinity of Consistency as a Defining Principle for General World Models"
daily_url: "https://arxiv.org/abs/2602.23152"
daily_keywords: ["Multimodal", "LLM", "Agent", "Eval", "Retrieval", "MoE", "Vision", "Llama", "Claude", "RAG"]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.23152" target="_blank">The Trinity of Consistency as a Defining Principle for General World Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


물리 법칙을 이해하는 'World Model' 구축은 AGI를 향한 중요한 과제입니다. 이 논문은 Sora와 같은 비디오 생성 모델과 UMM 아키텍처를 분석하며, 일관성(Consistency)을 핵심 원칙으로 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.22859" target="_blank">From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


기존 LMM 훈련 방식은 정적 데이터에 의존해 모델의 약점을 파악하기 어려웠습니다. 이를 해결하기 위해 오류를 진단하고 피드백을 통해 점진적으로 학습하는 DPE(Diagnostic-driven Progressive Evolution) 방법을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.22638" target="_blank">MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


LLM 기반의 경로 계획 에이전트를 실제 환경에서 평가하는 것은 매우 복잡한 문제입니다. 이를 위해 다양한 이동 시나리오와 지도 서비스를 반영하여 에이전트 성능을 체계적으로 측정할 수 있는 MobilityBench를 소개합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.17602" target="_blank">MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models</a></h3>



신약 개발을 위한 분자 생성 분야에서 기존 그래프 확산 모델의 낮은 화학적 유효성 문제를 지적합니다. 이를 극복하기 위해 계층적 이산 확산 모델인 MolHIT 프레임워크를 제안하여 분자 구조 생성 성능을 크게 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.18283" target="_blank">HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


사용자의 긴 행동 패턴을 분석해 추천하는 과정에서 효율성과 정확도 사이의 딜레마를 해결하고자 합니다. HyTRec 모델은 하이브리드 어텐션 구조를 통해 장기적인 선호도와 단기적인 관심을 분리하여 효율적으로 처리합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/moe-transformers" target="_blank">Mixture of Experts (MoEs) in Transformers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Transformer 모델의 효율성을 높이는 Mixture of Experts (MoE) 아키텍처에 대해 다룹니다. 입력 데이터에 따라 필요한 전문가(Expert) 네트워크만 활성화하여, 모델 크기는 키우면서도 연산 비용은 절감하는 원리를 설명합니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-on-jetson" target="_blank">Deploying Open Source Vision Language Models (VLM) on Jetson</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


NVIDIA Jetson과 같은 엣지 디바이스에서 오픈소스 VLM을 구동하는 방법을 안내합니다. 무거운 모델을 경량화하고 최적화하여 로컬 환경에서도 시각 및 언어 지능을 활용할 수 있도록 돕습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ggml-joins-hf" target="_blank">GGML and llama.cpp join HF to ensure the long-term progress of Local AI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로컬 환경에서 LLM을 효율적으로 실행하게 해주는 GGML과 llama.cpp 프로젝트가 Hugging Face와 협력하게 되었습니다. 이는 개인용 하드웨어에서도 고성능 AI 모델을 쉽게 구동할 수 있도록 오픈소스 생태계를 강화한다는 소식입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/moeru-ai/airi" target="_blank">moeru-ai/airi</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


나만의 AI 동반자를 만들 수 있는 셀프 호스팅 프로젝트로, 실시간 음성 채팅과 게임 플레이(Minecraft 등)가 가능합니다. 사용자가 직접 소유하고 관리하는 'Waifu' 스타일의 AI 에이전트를 다양한 OS에서 실행할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruflo" target="_blank">ruvnet/ruflo</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Anthropic의 Claude를 위한 에이전트 오케스트레이션 플랫폼입니다. 다중 에이전트 협업, RAG 통합, 자율 워크플로우 구축을 지원하며 기업 수준의 아키텍처를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/deer-flow" target="_blank">bytedance/deer-flow</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


조사부터 코딩, 창작까지 수행하는 오픈소스 SuperAgent 프레임워크입니다. 샌드박스와 메모리, 도구 활용 능력을 갖추어 몇 분에서 몇 시간이 걸리는 복잡한 작업을 자율적으로 처리할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/alibaba/OpenSandbox" target="_blank">alibaba/OpenSandbox</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 애플리케이션을 위한 범용 샌드박스 플랫폼으로, 코딩 에이전트나 GUI 에이전트가 안전하게 실행될 수 있는 환경을 제공합니다. 다양한 언어의 SDK와 Docker/Kubernetes 런타임을 지원하여 AI 코드 실행 및 평가에 최적화되어 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Shubhamsaboo/awesome-llm-apps" target="_blank">Shubhamsaboo/awesome-llm-apps</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


OpenAI, Anthropic, Gemini 및 오픈소스 모델을 활용한 다양한 LLM 앱과 AI 에이전트 모음집입니다. RAG 기술이 적용된 실전 예제들을 통해 최신 AI 애플리케이션 구축 아이디어를 얻을 수 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>LLM</code> <code>Agent</code> <code>Eval</code> <code>Retrieval</code> <code>MoE</code> <code>Vision</code> <code>Llama</code> <code>Claude</code> <code>RAG</code> 
</div>

---

