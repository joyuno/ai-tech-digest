---
layout: post
title: "thunderbolt 트렌드 지속 — bring-your-own AI 흐름"
date: 2026-04-20
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.11626" target="_blank">RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


시각적 생성 보상 모델이 단순한 점수 대신 다차원적인 평가와 그 이유를 명시적으로 생성하도록 학습시키는 방법을 제안합니다. 이를 통해 강화학습 훈련 과정과 테스트 환경 모두에서 생성기의 성능을 개선하고 평가 과정을 더 투명하게 만듭니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14268" target="_blank">HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


텍스트, 이미지, 비디오 등 다양한 입력을 받아 고품질 3D 환경을 생성하고 시뮬레이션할 수 있는 멀티모달 World Model인 HY-World 2.0을 소개합니다. 특히 텍스트나 단일 이미지만으로도 자유롭게 탐색 가능한 3D Gaussian Splatting 기반의 입체적인 세계를 만들어낼 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14683" target="_blank">DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


복잡하고 긴 호흡이 필요한 연구용 AI 에이전트를 평가하기 위해 현실적이고 재현 가능한 DR^{3}-Eval 벤치마크를 제안합니다. 실제 사용자가 제공한 자료를 바탕으로 구성되어, 멀티모달 이해력과 다중 파일 기반의 보고서 생성 능력을 정확하게 측정할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14004" target="_blank">Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


코딩 에이전트가 단일 도메인을 넘어 다양한 작업 환경에서도 축적된 기억(Memory)을 활용할 수 있도록 돕는 Memory Transfer Learning (MTL) 방법을 연구했습니다. 통합된 메모리 풀을 활용하여 서로 다른 프로그래밍 환경이나 언어 사이에서도 지식을 효과적으로 전달하고 코딩 문제 해결 능력을 향상시킵니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.15308" target="_blank">RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


자율주행의 모션 플래닝을 개선하기 위해 Generator와 Discriminator 구조를 활용한 RAD-2 프레임워크를 제안합니다. 기존 모방 학습의 한계를 극복하고 강화학습을 적용하여, 복잡한 주행 상황에서도 안정적이고 피드백 수용이 가능한 폐루프(closed-loop) 제어를 실현합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15308" target="_blank">RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


자율주행의 모션 플래닝을 개선하기 위해 Generator와 Discriminator 구조를 활용한 RAD-2 프레임워크를 제안합니다. 기존 모방 학습의 한계를 극복하고 강화학습을 적용하여, 복잡한 주행 상황에서도 안정적이고 피드백 수용이 가능한 폐루프(closed-loop) 제어를 실현합니다.

<small><i data-lucide="user"></i> Hao Gao, Shaoyu Chen, Yifan Zhu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15284" target="_blank">GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


3D Gaussian Splatting의 효율성을 높이기 위해 Global Scene Tokens를 활용하는 GlobalSplat 모델을 소개합니다. 기존의 지역적인 할당 방식의 한계를 벗어나 전체 장면의 맥락을 이해함으로써, 렌더링 품질과 3D 재구성 속도를 모두 크게 개선했습니다.

<small><i data-lucide="user"></i> Roni Itkin, Noam Issachar, Yehonatan Keypur</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15311" target="_blank">LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> 
</div>


Flow Matching 모델을 인간의 선호도에 맞게 미세조정할 때 발생하는 메모리 및 그래디언트 폭발 문제를 해결하는 LeapAlign 방법을 제안합니다. 전체 생성 과정을 짧은 두 단계 궤적으로 나누어 학습함으로써, 최종 이미지 품질에 중요한 초기 생성 단계까지 효과적으로 최적화할 수 있습니다.

<small><i data-lucide="user"></i> Zhanhao Liang, Tao Yang, Jie Wu</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thunderbird/thunderbolt" target="_blank">thunderbird/thunderbolt</a></h3>



사용자가 AI 모델을 직접 선택하고 데이터 소유권을 유지할 수 있도록 돕는 오픈소스 도구입니다. 특정 기업에 종속되는 Vendor lock-in을 방지하며, 나만의 맞춤형 AI 환경을 완벽하게 통제할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/tractorjuice/arc-kit" target="_blank">tractorjuice/arc-kit</a></h3>



기업의 엔터프라이즈 아키텍처(EA) 관리와 벤더 조달 과정을 돕는 실용적인 툴킷입니다. 체계적인 거버넌스 구축을 위한 다양한 템플릿과 가이드를 제공하여 효율적인 IT 인프라 기획을 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/openai/openai-agents-python" target="_blank">openai/openai-agents-python</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


OpenAI에서 공식적으로 제공하는 Python 기반의 경량화된 Multi-agent 워크플로우 프레임워크입니다. 여러 AI 에이전트들이 서로 협력하여 복잡한 작업을 수행할 수 있도록 쉽고 강력한 개발 환경을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/paperless-ngx/paperless-ngx" target="_blank">paperless-ngx/paperless-ngx</a></h3>



커뮤니티 주도로 개발되는 강력한 오픈소스 문서 관리 시스템입니다. 종이 문서나 디지털 파일을 스캔, 색인화, 보관하는 모든 과정을 자동화하여 체계적이고 깔끔한 문서 보관 환경을 만들어줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/EvoMap/evolver" target="_blank">EvoMap/evolver</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


유전자 진화 프로토콜(GEP)을 기반으로 작동하는 AI 에이전트용 자가 진화 엔진입니다. 에이전트 스스로 능력을 개선하고 진화할 수 있는 독특한 환경을 제공하여 더욱 고도화된 AI 시스템 구축을 돕습니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/485" target="_blank">AI Weekly Issue #485: When AI teaches AI, it teaches in secret</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Nvidia의 젠슨 황과 Anthropic에 얽힌 최신 AI 업계의 흥미로운 소식을 다루는 뉴스레터입니다. AI 에이전트 엔지니어링의 발전 현황과 다가오는 기술적 변곡점에 대한 심도 있는 팟캐스트 요약도 함께 만나볼 수 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Eval</code> <code>Prompt</code> <code>Multimodal</code> <code>Retrieval</code> <code>Agent</code> <code>RAG</code> <code>Inference</code> <code>Fine-tuning</code> <code>Alignment</code> 
</div>

---

