---
layout: post
title: "VESPO — Off-Policy LLM RL 안정화하는 variational soft PO"
date: 2026-02-24
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "VESPO: Variational Sequence-Level Soft Policy Optimization for Stable Off-Policy LLM Training"
daily_url: "https://arxiv.org/abs/2602.10693"
daily_keywords: ["LLM", "Inference", "Reasoning", "CoT", "Agent", "Eval", "Fine-tuning", "Llama", "Claude", "Cursor"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2602.10693.png"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.10693" target="_blank">VESPO: Variational Sequence-Level Soft Policy Optimization for Stable Off-Policy LLM Training</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


LLM의 강화학습(RL) 과정에서 발생하는 학습 불안정성을 해결하기 위한 VESPO라는 새로운 기법을 제안합니다. 기존 중요도 샘플링(Importance Sampling)의 높은 분산 문제를 개선하여, 정책이 최신 상태와 달라져도 안정적으로 학습할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.08354" target="_blank">Does Your Reasoning Model Implicitly Know When to Stop Thinking?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


복잡한 추론 모델이 긴 Chain of Thought(CoT)를 사용할 때 발생하는 비효율성과 중복성 문제를 심도 있게 분석했습니다. 무작정 추론 과정이 길다고 정답률이 높은 것은 아니며, 모델이 언제 '생각'을 멈춰야 할지에 대한 중요한 통찰을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.17270" target="_blank">Unified Latents (UL): How to train your latents</a></h3>



Diffusion 모델을 활용해 잠재 표현(Latent Representation)을 효과적으로 학습하는 Unified Latents(UL) 프레임워크를 소개합니다. 기존 방식보다 적은 연산량으로도 ImageNet-512에서 뛰어난 이미지 품질과 재구성 성능을 달성했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.14296" target="_blank">AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


웹 GUI 에이전트 학습을 위해 검증 가능한 웹 환경을 자동으로 생성해주는 AutoWebWorld 프레임워크입니다. 실제 웹 데이터 수집의 비용과 검증 한계를 극복하기 위해 유한 상태 기계(Finite State Machines)를 기반으로 신뢰할 수 있는 합성 데이터를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.13515" target="_blank">SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>


Diffusion 모델의 추론 속도를 높이기 위해 Top-k와 Top-p 마스킹을 결합한 훈련 가능한 Sparse Attention 기법을 연구했습니다. 이를 통해 이미지 생성 품질을 유지하면서도 기존 방식보다 더 높은 희소성(Sparsity)을 달성하여 효율성을 극대화했습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ggml-joins-hf" target="_blank">GGML and llama.cpp join HF to ensure the long-term progress of Local AI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로컬 AI 구동의 핵심 기술인 GGML과 llama.cpp 팀이 Hugging Face에 공식적으로 합류했다는 소식입니다. 이는 온디바이스(On-device) 및 오픈소스 AI 생태계의 장기적인 발전을 가속화할 중요한 협력으로 기대됩니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/unsloth-jobs" target="_blank">Train AI models with Unsloth and Hugging Face Jobs for FREE</a></h3>



학습 속도를 획기적으로 높여주는 Unsloth 라이브러리와 Hugging Face Jobs를 활용해 AI 모델을 무료로 학습하는 방법을 소개합니다. 비용 효율적으로 고성능 모델을 파인튜닝하고 싶은 개발자들에게 매우 유용한 가이드입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/nemotron-personas-japan-nttdata-ja" target="_blank">「データ不足」の壁を越える：合成ペルソナが日本のAI開発を加速</a></h3>



일본 AI 개발 현장의 데이터 부족 문제를 해결하기 위해 '합성 페르소나' 데이터를 활용하는 전략을 다룹니다. 양질의 일본어 데이터를 확보하여 AI 모델의 성능을 높이는 구체적인 사례와 방법론을 설명합니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools" target="_blank">x1xhlol/system-prompts-and-models-of-ai-tools</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude Code, Cursor, Devin 등 최신 AI 코딩 도구와 에이전트들의 시스템 프롬프트(System Prompts)를 모아놓은 저장소입니다. 상용 AI 서비스들이 내부적으로 어떤 지시를 받아 동작하는지 파악할 수 있는 흥미로운 분석 자료입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/OpenBB-finance/OpenBB" target="_blank">OpenBB-finance/OpenBB</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


애널리스트와 퀀트, 그리고 AI 에이전트를 위한 강력한 오픈소스 금융 데이터 플랫폼입니다. 다양한 시장 데이터를 통합하여 분석하거나, 금융 분야에 특화된 AI 애플리케이션을 개발할 때 필수적인 인프라를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/f/prompts.chat" target="_blank">f/prompts.chat</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


일명 'Awesome ChatGPT Prompts'로 불리는 프로젝트로, 커뮤니티에서 검증된 유용한 프롬프트 컬렉션입니다. 오픈소스로 제공되어, 조직 내부에서 자체적으로 호스팅하며 안전하게 프롬프트를 공유하고 관리할 수도 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/CompVis/stable-diffusion" target="_blank">CompVis/stable-diffusion</a></h3>



텍스트를 입력하면 고품질 이미지를 생성해주는 그 유명한 Stable Diffusion의 공식 저장소입니다. Latent Diffusion 모델의 구조와 핵심 코드를 직접 확인하고 연구나 프로젝트에 활용할 수 있는 이미지 생성 AI의 바이블과 같은 자료입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/abhigyanpatwari/GitNexus" target="_blank">abhigyanpatwari/GitNexus</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


서버 없이 브라우저에서 바로 GitHub 저장소나 코드를 분석해 지식 그래프(Knowledge Graph)를 생성해주는 도구입니다. 내장된 Graph RAG 에이전트를 통해 복잡한 코드 구조를 시각적으로 탐색하고 이해하는 데 큰 도움을 줍니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Inference</code> <code>Reasoning</code> <code>CoT</code> <code>Agent</code> <code>Eval</code> <code>Fine-tuning</code> <code>Llama</code> <code>Claude</code> <code>Cursor</code> 
</div>

---

