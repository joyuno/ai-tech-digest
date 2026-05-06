---
layout: post
title: "RationalRewards 추론 보상 시각 생성 스케일링"
date: 2026-04-18
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


이 논문은 시각적 이미지 생성 모델을 평가하는 새로운 보상 모델인 RationalRewards를 제안합니다. 단순한 점수 대신 세부적인 비평을 명시적으로 생성하게 하여 모델을 능동적인 최적화 도구로 활용할 수 있게 해줍니다. 이를 통해 훈련과 테스트 단계 모두에서 이미지 생성 품질을 크게 향상시킬 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14268" target="_blank">HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


텍스트, 이미지, 비디오 등 다양한 형태의 입력을 받아 3D 가상 세계를 만들어내는 다중 모달 월드 모델인 HY-World 2.0을 소개합니다. 특히 텍스트 프롬프트나 단일 이미지만으로도 자유롭게 탐색 가능한 고품질의 3D Gaussian Splatting 씬을 정교하게 생성해냅니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14004" target="_blank">Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI 코딩 에이전트가 과거의 경험을 기억하고 활용하는 Memory Transfer Learning(MTL) 방법을 연구한 논문입니다. 기존에는 비슷한 작업에서만 메모리를 활용했지만, 이 방법을 통해 전혀 다른 도메인의 문제들 사이에서도 프로그래밍 언어나 실행 환경에 대한 지식을 효과적으로 전이하고 공유할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.14142" target="_blank">From P(y|x) to P(y): Investigating Reinforcement Learning in Pre-train Space</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> 
</div>


LLM의 추론 능력을 높이기 위해 사전 학습(Pre-train) 공간에서 강화 학습을 적용하는 새로운 접근법을 탐구합니다. 기존처럼 특정 질문에 대한 답변 확률을 높이는 대신, 모델의 전반적인 출력 분포 자체를 최적화하여 근본적인 추론 한계를 극복하고 더 넓은 탐색 능력을 유지하도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.11045" target="_blank">Sema Code: Decoupling AI Coding Agents into Programmable, Embeddable Infrastructure</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI 코딩 에이전트를 특정 IDE나 웹 환경에 종속되지 않도록 분리한 오픈소스 프레임워크인 Sema Code를 소개합니다. 이를 통해 기업들은 다양하고 복잡한 엔지니어링 환경 어디에나 AI 코딩 기능을 레고 블록처럼 쉽게 내장하고 결합하여 사용할 수 있습니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15308" target="_blank">RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


고도화된 자율 주행을 위한 안전하고 정교한 모션 플래닝 프레임워크인 RAD-2를 제안합니다. 기존 Diffusion 모델이 가진 불안정성과 모방 학습의 한계를 해결하기 위해 Generator-Discriminator 구조를 결합하여 주행의 안정성을 크게 높였습니다.

<small>👤 Hao Gao, Shaoyu Chen, Yifan Zhu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15284" target="_blank">GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> 
</div>


3D Gaussian Splatting의 렌더링 속도와 품질을 동시에 높이기 위해 Global Scene Tokens를 활용하는 GlobalSplat 모델입니다. 기존의 지엽적인 처리 방식을 벗어나 전체 씬의 맥락을 파악함으로써 3D 요소를 효율적으로 배치하고 빠르고 정교하게 재구성할 수 있습니다.

<small>👤 Roni Itkin, Noam Issachar, Yehonatan Keypur</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.15311" target="_blank">LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories</a></h3>


<div class="categories">
<span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🎯 신뢰성/안전</span> 
</div>


이미지 생성에 쓰이는 Flow Matching 모델을 사람의 선호도에 맞게 미세 조정할 때 발생하는 메모리 부족 및 그래디언트 폭발 문제를 해결하는 기법입니다. 생성 과정을 두 단계의 짧은 궤적으로 단축하여 모델이 이미지를 그리는 어떤 단계에서든 효율적으로 학습을 진행할 수 있게 해줍니다.

<small>👤 Zhanhao Liang, Tao Yang, Jie Wu</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/EvoMap/evolver" target="_blank">EvoMap/evolver</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


AI 에이전트 스스로 발전하고 진화할 수 있도록 돕는 GEP(유전자 진화 프로토콜) 기반의 자가 진화 엔진입니다. 에이전트의 능력을 지속적으로 향상시키고 복잡한 문제를 해결할 수 있는 강력한 프레임워크를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/SimoneAvogadro/android-reverse-engineering-skill" target="_blank">SimoneAvogadro/android-reverse-engineering-skill</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


안드로이드 애플리케이션의 리버스 엔지니어링 작업을 전문적으로 도와주는 Claude Code 스킬입니다. 개발자나 보안 전문가가 앱의 내부 구조를 쉽게 분석하고 파악할 수 있도록 AI 기반의 스마트한 도구를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/BasedHardware/omi" target="_blank">BasedHardware/omi</a></h3>



사용자의 화면을 시각적으로 인식하고 주변의 대화 내용을 들으며 실시간으로 조언을 제공하는 AI 비서 프로젝트입니다. 일상생활이나 업무 중에 필요한 행동이나 답변을 맥락에 맞게 똑똑하게 제안해 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Lordog/dive-into-llms" target="_blank">Lordog/dive-into-llms</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


LLM의 핵심 원리와 작동 방식을 직접 코딩하며 배울 수 있는 실전 프로그래밍 튜토리얼입니다. 기초부터 심화 과정까지 단계별 실습을 통해 대규모 언어 모델 개발과 활용법을 쉽게 익힐 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Donchitos/Claude-Code-Game-Studios" target="_blank">Donchitos/Claude-Code-Game-Studios</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude Code를 실제 게임 개발 스튜디오처럼 완벽하게 탈바꿈시켜 주는 흥미로운 프로젝트입니다. 49개의 AI 에이전트와 72개의 워크플로우 기술이 현실의 개발팀 직급 체계에 맞춰 협업하며 게임을 자동으로 제작해 줍니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Eval</code> <code>Prompt</code> <code>RAG</code> <code>Agent</code> <code>LLM</code> <code>LoRA</code> <code>AI Coding</code> <code>Multimodal</code> <code>Inference</code> 
</div>

---

