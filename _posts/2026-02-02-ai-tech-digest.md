---
layout: post
title: "AI 기술 다이제스트 - 2026-02-02"
date: 2026-02-02
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.20833" target="_blank">Idea2Story: An Automated Pipeline for Transforming Research Concepts into Complete Scientific Narratives</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


연구 아이디어를 완전한 과학적 이야기로 변환해주는 자동화 파이프라인을 제안하는 논문입니다. 기존 LLM 에이전트들이 겪던 높은 계산 비용과 문맥 제한 문제를 해결하여, 보다 효율적으로 과학적 발견 과정을 자동화할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.20354" target="_blank">Everything in Its Place: Benchmarking Spatial Intelligence of Text-to-Image Models</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Text-to-Image 모델이 복잡한 공간 관계를 얼마나 잘 이해하고 표현하는지 평가하는 새로운 벤치마크 'SpatialGenEval'을 소개합니다. 기존 모델들이 화질은 좋지만 공간적 추론이나 사물 배치에 약하다는 점을 지적하며, 이를 체계적으로 측정할 수 있게 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.21204" target="_blank">Scaling Embeddings Outperforms Scaling Experts in Language Models</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


거대 언어 모델(LLM) 확장에 흔히 쓰이던 MoE(Mixture-of-Experts) 방식의 한계를 넘어, 임베딩 확장이 더 효율적일 수 있음을 밝혀낸 연구입니다. 실험을 통해 특정 조건에서는 임베딩을 키우는 것이 전문가(Expert) 수를 늘리는 것보다 더 나은 성능을 보인다는 점을 입증했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22153" target="_blank">DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


움직이는 물체를 조작하는 데 어려움을 겪는 기존 모델을 개선하기 위해, 시간적 추론과 지속적인 제어 기능을 갖춘 DynamicVLA를 제안합니다. 시각-언어-행동(VLA) 모델이 동적인 상황에서도 빠르게 인식하고 적응할 수 있도록 설계되었습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.21821" target="_blank">MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> 
</div>


오픈소스 시각 언어 모델(VLM)의 추론 능력을 상용 모델 수준으로 끌어올리기 위해 고품질 데이터셋인 MMFineReason을 공개했습니다. 과학 도표나 퍼즐 같은 복잡한 이미지를 Chain-of-Thought(CoT) 방식으로 학습시켜 모델의 시각적 추론 능력을 강화합니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control" target="_blank">Introducing NVIDIA Cosmos Policy for Advanced Robot Control</a></h3>



NVIDIA가 로봇 제어를 위해 새롭게 개발한 시스템인 Cosmos Policy를 소개합니다. 물리적인 환경에서 로봇이 더 정교하고 진보된 동작을 수행할 수 있도록 돕는 핵심 기반 기술입니다.

<small>👤 Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/daggr" target="_blank">Introducing Daggr: Chain apps programmatically, inspect visually</a></h3>



다양한 앱이나 기능을 프로그래밍 방식으로 연결하고, 그 흐름을 시각적으로 쉽게 확인할 수 있는 도구인 Daggr를 소개합니다. 복잡한 AI 워크플로우를 구성하고 디버깅하는 과정을 훨씬 직관적으로 만들어줍니다.

<small>👤 Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/upskill" target="_blank">We Got Claude to Build CUDA Kernels and teach open models!</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


고성능 LLM인 Claude를 활용해 복잡한 CUDA 커널 코드를 작성하게 하고, 이를 바탕으로 오픈소스 모델을 가르친 흥미로운 사례입니다. 상용 모델의 코딩 능력을 활용해 오픈 모델의 성능을 효율적으로 향상시키는 방법을 다룹니다.

<small>👤 Hugging Face</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/openclaw/openclaw" target="_blank">openclaw/openclaw</a></h3>



어떤 운영체제나 플랫폼에서도 사용할 수 있는 나만의 개인 AI 비서를 구축하는 프로젝트입니다. 사용자의 환경에 구애받지 않고 자유롭게 커스터마이징 가능한 AI 에이전트를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ThePrimeagen/99" target="_blank">ThePrimeagen/99</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


개발자들에게 인기 있는 에디터인 Neovim을 위해 최적화된 AI 에이전트 플러그인입니다. Neovim의 가볍고 빠른 환경에 맞춰 AI 기능을 통합하여 코딩 생산성을 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/badlogic/pi-mono" target="_blank">badlogic/pi-mono</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


코딩 에이전트 CLI, 통합 LLM API, 웹 UI, 슬랙 봇 등 AI 에이전트 개발에 필요한 모든 도구를 모아놓은 툴킷입니다. 다양한 인터페이스와 기능을 한 번에 제공하여 나만의 에이전트를 쉽게 만들 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thedotmack/claude-mem" target="_blank">thedotmack/claude-mem</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude Code 사용 중 발생하는 모든 작업 내용을 자동으로 기록하고 압축하여 기억하는 플러그인입니다. 과거의 코딩 세션 정보를 다음 작업에 자동으로 반영해주어, 연속성 있는 AI 코딩 경험을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/microsoft/agent-lightning" target="_blank">microsoft/agent-lightning</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


Microsoft에서 개발한 AI 에이전트 학습용 프레임워크로 보입니다. 에이전트 모델을 더 빠르고 효율적으로 트레이닝할 수 있도록 돕는 강력한 도구를 목표로 하고 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Reasoning</code> <code>Prompt</code> <code>MoE</code> <code>Vision</code> <code>Multimodal</code> <code>RAG</code> <code>Claude</code> <code>AI Agent</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>