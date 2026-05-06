---
layout: post
title: "RationalRewards 추론 보상 시각 생성 스케일링"
date: 2026-04-19
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.11626" target="_blank">RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


이 논문은 시각 생성 모델을 평가할 때 단순한 점수 대신 다차원적인 피드백을 먼저 생성하도록 Reward Model을 학습시키는 방법을 제안합니다. 이를 통해 보상 모델이 수동적인 평가자를 넘어 능동적인 최적화 도구로 변신하며, 훈련과 테스트 단계 모두에서 생성 품질을 크게 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14268" target="_blank">HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


텍스트, 이미지, 비디오 등 다양한 입력을 처리해 탐색 가능한 3D 세계를 생성하고 시뮬레이션할 수 있는 멀티모달 World Model인 HY-World 2.0을 소개합니다. 4단계의 체계적인 생성 과정을 거쳐 고품질의 3D Gaussian Splatting(3DGS) 씬을 완벽하게 구현해내는 것이 특징입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14004" target="_blank">Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


코딩 에이전트들이 단일 작업 환경에서만 메모리를 활용하던 기존의 한계를 극복하기 위해 메모리 전이 학습(MTL)을 제안한 연구입니다. 다양한 도메인에서 수집된 통합 메모리 풀을 활용하여 프로그래밍 언어나 런타임 등 공통적인 기반 지식을 새로운 문제 해결에 효과적으로 적용할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14683" target="_blank">DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


복잡하고 장기적인 연구 작업을 수행하는 Deep Research Agent를 효과적으로 평가하기 위한 현실적인 벤치마크 도구입니다. 동적인 웹 환경과 모호한 작업 기준의 한계를 극복하기 위해, 실제 사용자가 제공한 자료를 바탕으로 재현 가능하면서도 정확한 평가 환경을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14142" target="_blank">From P(y|x) to P(y): Investigating Reinforcement Learning in Pre-train Space</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> 
</div>


LLM의 추론 능력을 강화할 때 기존 베이스 모델의 한계에 부딪히는 문제를 해결하기 위해, 사전학습 단계의 데이터 분포 자체를 최적화하는 연구입니다. 단순한 수동적 학습을 넘어, 모델 자체에 넓은 탐색 능력과 논리적 추론 능력을 깊숙이 내재화하는 새로운 강화학습 방향을 제시합니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15308" target="_blank">RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


고도화된 자율주행 모션 플래닝에서 발생하는 불안정성과 피드백 부족 문제를 해결하기 위해 고안된 Generator-Discriminator 기반 프레임워크입니다. 강화학습을 결합하여 복잡하고 불확실한 주행 상황에서도 더욱 안정적이고 정확한 이동 궤적을 계획할 수 있게 도와줍니다.

<small>👤 Hao Gao, Shaoyu Chen, Yifan Zhu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15284" target="_blank">GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> 
</div>


3D Gaussian Splatting 기술의 렌더링 속도와 품질 사이의 딜레마를 해결하기 위해 전역 씬 토큰(Global Scene Tokens)을 새롭게 도입했습니다. 기존의 부분적인 최적화 방식에서 벗어나 씬 전체의 맥락을 파악함으로써 더욱 효율적이고 정밀한 3D 공간 재구성이 가능해집니다.

<small>👤 Roni Itkin, Noam Issachar, Yehonatan Keypur</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15311" target="_blank">LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories</a></h3>


<div class="categories">
<span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🎯 신뢰성/안전</span> 
</div>


생성형 AI의 Flow Matching 모델을 인간의 선호도에 맞게 미세조정할 때 발생하는 엄청난 메모리 소모와 기울기 폭발 문제를 해결하는 기술입니다. 효율적인 2단계 궤적 학습법을 도입하여, 이미지의 전반적인 구조를 결정하는 초기 생성 단계부터 모델을 안정적으로 제어하고 최적화할 수 있습니다.

<small>👤 Zhanhao Liang, Tao Yang, Jie Wu</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thunderbird/thunderbolt" target="_blank">thunderbird/thunderbolt</a></h3>



사용자가 AI 모델을 직접 선택하고 데이터 소유권을 완벽하게 유지할 수 있게 해주는 오픈소스 AI 프레임워크 프로젝트입니다. 특정 기업 플랫폼에 종속되는 현상을 방지하고, 내 입맛에 맞는 자유로운 AI 통제 환경을 구축할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/BasedHardware/omi" target="_blank">BasedHardware/omi</a></h3>



사용자의 컴퓨터 화면을 실시간으로 분석하고 오디오 대화를 청취하여 지금 필요한 행동을 먼저 제안해 주는 스마트한 AI 어시스턴트입니다. 복잡한 명령 없이도 현재 상황을 AI가 스스로 인지하여 작업 효율을 크게 높여줄 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/openai/openai-agents-python" target="_blank">openai/openai-agents-python</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


복잡한 Multi-agent 워크플로우를 쉽게 구축하고 관리할 수 있도록 돕는 Python 기반의 공식 프레임워크입니다. 가벼우면서도 강력한 기능을 제공하여 여러 AI 에이전트가 협업하는 환경을 아주 손쉽게 구성할 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/EvoMap/evolver" target="_blank">EvoMap/evolver</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


AI 에이전트가 스스로 발전하고 구조를 개선할 수 있도록 돕는 GEP(Genome Evolution Protocol) 기반의 자가 진화 엔진입니다. 에이전트의 한계를 넘어 지속적으로 성능을 최적화하고 진화시키는 혁신적인 방법을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/deepseek-ai/DeepGEMM" target="_blank">deepseek-ai/DeepGEMM</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


정밀한 스케일링 기법을 적용하여 매우 깔끔하고 효율적으로 설계된 FP8 연산 처리용 GEMM 커널 라이브러리입니다. 최신 LLM이나 딥러닝 모델을 구동할 때 연산 속도를 끌어올리고 메모리 효율성을 극대화하는 데 유용하게 활용할 수 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Eval</code> <code>Prompt</code> <code>RAG</code> <code>Agent</code> <code>Multimodal</code> <code>Retrieval</code> <code>LLM</code> <code>LoRA</code> <code>Inference</code> 
</div>

---

