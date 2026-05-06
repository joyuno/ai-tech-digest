---
layout: post
title: "주니어 디자이너 비회원 퍼널 실험 설계"
date: 2026-02-28
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.23152" target="_blank">The Trinity of Consistency as a Defining Principle for General World Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


범용 인공지능(AGI)의 핵심인 물리 법칙을 이해하는 'World Model' 구축에 대해 다루는 논문입니다. Sora와 같은 비디오 모델의 발전을 언급하며, 인식과 언어, 추론을 통합하는 새로운 아키텍처인 Unified Multimodal Model (UMM)을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.22859" target="_blank">From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


기존의 정적인 데이터 학습 방식에서 벗어나, Large Multimodal Model (LMM)의 취약점을 진단하고 개선하는 DPE 학습법을 제안합니다. 모델이 실수하는 부분을 찾아내고 이에 맞춘 피드백을 제공하여, 복잡한 추론 능력을 더 효과적으로 향상시킬 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.22638" target="_blank">MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


LLM 기반의 경로 계획 에이전트가 실제 환경에서 얼마나 잘 작동하는지 평가하기 위한 벤치마크인 'MobilityBench'를 소개합니다. 다양한 경로 요구 사항과 지도 서비스의 변수들을 고려하여, 현실적인 모빌리티 시나리오에서 에이전트의 성능을 체계적으로 검증할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.17602" target="_blank">MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models</a></h3>



신약 개발 등을 위해 분자 구조를 생성하는 AI 모델의 성능을 높인 MolHIT 프레임워크를 소개합니다. 기존 그래프 기반 Diffusion 모델들이 겪던 화학적 타당성 문제를 해결하기 위해, 계층적 이산 확산 방식을 적용하여 더 정확한 분자 구조를 생성합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.18283" target="_blank">HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


사용자의 긴 행동 패턴을 분석해 추천 정확도를 높이는 HyTRec 모델을 제안합니다. 기존 Attention 메커니즘의 계산 비용과 정확도 사이의 딜레마를 해결하기 위해, 장기적인 선호도와 단기적인 관심을 분리하여 효율적으로 처리하는 하이브리드 구조를 사용했습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/moe-transformers" target="_blank">Mixture of Experts (MoEs) in Transformers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Transformer 모델의 효율성을 극대화하는 Mixture of Experts (MoE) 아키텍처에 대해 설명하는 글입니다. 모든 파라미터를 사용하지 않고 상황에 맞는 '전문가' 네트워크만 활성화하여, 모델의 크기는 키우면서도 연산 비용은 절감하는 원리를 다룹니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-on-jetson" target="_blank">Deploying Open Source Vision Language Models (VLM) on Jetson</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


강력한 Vision Language Model (VLM)을 클라우드가 아닌 NVIDIA Jetson과 같은 엣지 디바이스에서 구동하는 방법을 안내합니다. 오픈소스 모델을 활용해 로컬 환경에서도 시각 정보를 이해하고 처리하는 AI 애플리케이션을 구축할 수 있습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ggml-joins-hf" target="_blank">GGML and llama.cpp join HF to ensure the long-term progress of Local AI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로컬 AI 생태계의 핵심인 GGML과 llama.cpp가 Hugging Face와 협력한다는 중요한 소식입니다. 개인 컴퓨터에서도 거대 언어 모델(LLM)을 효율적으로 실행할 수 있도록 오픈소스 기술의 장기적인 발전과 표준화를 도모하려는 움직임입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/45391" target="_blank">신입 디자이너가 꼭 알아야 할 실험 설계 팁</a></h3>



실험 경험이 부족한 주니어 디자이너들을 위해, 비회원 퍼널 실험 사례를 통해 제품 실험 설계 노하우를 공유합니다. 데이터 기반으로 가설을 세우고 검증하는 과정을 통해 어떻게 제품 성장에 기여할 수 있는지 실질적인 팁을 얻을 수 있습니다.

<small><i data-lucide="user"></i> 토스</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/deer-flow" target="_blank">bytedance/deer-flow</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


연구부터 코딩까지 스스로 수행하는 강력한 오픈소스 SuperAgent 프레임워크입니다. 샌드박스, 메모리, 도구 활용 기능을 갖추고 있어 몇 분에서 몇 시간이 걸리는 복잡한 작업도 자율적으로 처리할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/moonshine-ai/moonshine" target="_blank">moonshine-ai/moonshine</a></h3>



엣지 디바이스에서도 빠르고 정확하게 작동하도록 최적화된 자동 음성 인식(ASR) 모델입니다. 무거운 서버 없이도 음성을 텍스트로 변환하는 기능을 효율적으로 구현할 수 있어 온디바이스 AI 개발에 유용합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruflo" target="_blank">ruvnet/ruflo</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude를 위한 전문 에이전트 오케스트레이션 플랫폼으로, 지능형 멀티 에이전트 시스템을 쉽게 구축할 수 있습니다. 기업급 아키텍처를 기반으로 자율 작업 흐름을 조정하고 RAG 기능까지 통합하여 고도화된 대화형 AI 시스템을 만듭니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/abhigyanpatwari/GitNexus" target="_blank">abhigyanpatwari/GitNexus</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


서버 없이 브라우저에서 바로 실행되는 코드 분석 엔진으로, GitHub 저장소를 지식 그래프(Knowledge Graph)로 시각화해 줍니다. 내장된 Graph RAG 에이전트를 통해 복잡한 코드를 쉽고 직관적으로 탐색하고 질문할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/moeru-ai/airi" target="_blank">moeru-ai/airi</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


나만의 AI 동반자를 직접 호스팅하여 만들 수 있는 프로젝트로, 실시간 음성 대화는 물론 마인크래프트 같은 게임도 함께 즐길 수 있습니다. 윈도우와 맥, 웹을 모두 지원하며 'Neuro-sama'처럼 개성 있는 가상 존재를 구현하고 싶은 분들에게 적합합니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>LLM</code> <code>Agent</code> <code>Eval</code> <code>Retrieval</code> <code>MoE</code> <code>Vision</code> <code>Llama</code> <code>RAG</code> <code>Claude</code> 
</div>

---

