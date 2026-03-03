---
layout: post
title: "AI 기술 다이제스트 - 2026-03-04"
date: 2026-03-04
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.00141" target="_blank">From Scale to Speed: Adaptive Test-Time Scaling for Image Editing</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> 
</div>


이미지 편집 시 추론 시간을 조절하여 결과물의 품질을 높이는 적응형 Test-Time Scaling 기법을 소개합니다. 기존 생성 모델과 달리 원본 이미지의 제약을 고려하여 자원을 효율적으로 할당하는 Image-CoT 방식을 제안했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.02138" target="_blank">OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens</a></h3>



멀티모달 명령어로 고품질 벡터 애니메이션을 생성하는 OmniLottie 프레임워크를 제안합니다. 복잡한 Lottie 파일 구조를 학습하기 쉽도록 토큰화하여, 애니메이션 동작과 시각적 요소를 유연하게 제어할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.23866" target="_blank">SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


소프트웨어 엔지니어링 에이전트(SWE) 학습을 위한 대규모 언어 불문(Language-Agnostic) 벤치마크인 SWE-rebench V2를 공개했습니다. 기존 데이터셋의 한계를 넘어 다양한 프로그래밍 환경에서 에이전트의 성능을 강화 학습으로 향상시킬 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.01562" target="_blank">RubricBench: Aligning Model-Generated Rubrics with Human Standards</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🎯 신뢰성/안전</span> <span class="category-tag">💻 개발 도구</span> 
</div>


LLM 평가를 위한 보상 모델(Reward Model)이 편향을 줄이고 인간 기준에 부합하도록 돕는 벤치마크인 RubricBench를 소개합니다. 모델이 생성한 평가 기준(루브릭)을 정교하게 분석하여 더 정확하고 공정한 AI 평가 시스템을 구축하는 데 초점을 맞췄습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.01824" target="_blank">OpenAutoNLU: Open Source AutoML Library for NLU</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


텍스트 분류와 NER 같은 NLU 작업을 자동화해 주는 오픈소스 AutoML 라이브러리입니다. 별도의 설정 없이 데이터 특성에 맞는 학습 방식을 자동으로 선택해주며, 데이터 품질 진단과 LLM 기능까지 간편한 API로 지원합니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/Photoroom/prx-part3" target="_blank">PRX Part 3 — Training a Text-to-Image Model in 24h!</a></h3>



단 24시간 만에 Text-to-Image 모델을 처음부터 학습시키는 구체적인 과정을 다룹니다. 한정된 시간 내에 효율적으로 모델을 훈련하기 위한 최적화 전략과 실용적인 팁을 배울 수 있습니다.

<small>👤 Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/moe-transformers" target="_blank">Mixture of Experts (MoEs) in Transformers</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


Transformer 모델의 성능과 효율성을 극대화하는 Mixture of Experts (MoE) 아키텍처에 대해 깊이 있게 설명합니다. 모든 파라미터를 쓰지 않고 상황에 맞는 전문가 네트워크만 활성화하여 계산 비용을 줄이는 원리를 다룹니다.

<small>👤 Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-on-jetson" target="_blank">Deploying Open Source Vision Language Models (VLM) on Jetson</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


NVIDIA Jetson 같은 엣지 디바이스에서 오픈소스 Vision Language Model (VLM)을 구동하는 방법을 안내합니다. 하드웨어 자원이 제한된 환경에서도 시각-언어 모델을 최적화하여 배포하는 실전 가이드를 제공합니다.

<small>👤 Hugging Face</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/K-Dense-AI/claude-scientific-skills" target="_blank">K-Dense-AI/claude-scientific-skills</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


연구, 과학, 공학, 금융 등 전문 분야에서 AI 에이전트가 바로 활용할 수 있는 스킬 셋을 모아놓은 저장소입니다. Claude와 같은 모델이 복잡한 분석이나 전문적인 글쓰기 작업을 더 똑똑하게 수행하도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/moeru-ai/airi" target="_blank">moeru-ai/airi</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


직접 호스팅하여 나만의 AI 캐릭터와 소통할 수 있는 컴패니언 도구입니다. 실시간 음성 대화는 물론 마인크래프트 같은 게임도 함께 즐길 수 있으며, 웹과 데스크탑 환경에서 'Waifu' 스타일의 AI를 구동할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/CodebuffAI/codebuff" target="_blank">CodebuffAI/codebuff</a></h3>



터미널 환경에서 벗어나지 않고 명령줄에서 바로 AI를 이용해 코드를 생성할 수 있는 도구입니다. 개발 흐름을 끊지 않고 자연어 명령만으로 필요한 코드 스니펫이나 함수를 즉시 작성해 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/agentscope-ai/agentscope" target="_blank">agentscope-ai/agentscope</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


개발자가 내부 동작을 명확히 이해하고 신뢰할 수 있는 AI 에이전트를 구축하도록 돕는 프레임워크입니다. 에이전트의 실행 과정과 상호작용을 투명하게 관리하여 복잡한 애플리케이션을 쉽게 개발할 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/agentscope-ai/ReMe" target="_blank">agentscope-ai/ReMe</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


AI 에이전트의 기억 능력을 강화하기 위한 메모리 관리 키트입니다. 에이전트가 과거의 정보를 효율적으로 저장하고 정제(Refine)하여 더 똑똑하게 대화 맥락을 유지하도록 돕는 도구입니다.



</div>



---


## 📰 AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/468" target="_blank">AI News Weekly - Issue #468: AI would nuke us 95% of the time - Mar 3rd 2026</a></h3>



AI에게 핵무기 발사 권한을 주었을 때의 위험성을 경고하는 시뮬레이션 연구 등 충격적인 내용을 담은 뉴스레터입니다. 2026년이라는 미래 시점을 가정하여, 통제되지 않은 AI가 가져올 수 있는 심각한 안보 위기와 사회적 혼란을 시사하고 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Chain-of-Thought</code> <code>Agent</code> <code>Benchmark</code> <code>LLM</code> <code>Alignment</code> <code>Eval</code> <code>MoE</code> <code>Vision</code> <code>Claude</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>