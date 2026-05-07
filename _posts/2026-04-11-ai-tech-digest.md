---
layout: post
title: "Reasoning SFT도 일반화한다 — RL only 통념을 반박"
date: 2026-04-11
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability"
daily_url: "https://arxiv.org/abs/2604.06628"
daily_keywords: ["LLM", "Chain-of-Thought", "Agent", "Vision", "Alignment", "Prompt", "AI Agent", "Eval", "Multimodal", "RAG"]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.06628" target="_blank">Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


LLM 후학습 과정에서 SFT는 암기만 하고 RL만이 일반화 능력을 갖춘다는 기존의 통념을 반박하는 논문입니다. 긴 CoT를 활용한 추론 SFT를 분석한 결과, 최적화 방식이나 학습 데이터 및 기본 모델의 성능 조건만 잘 맞으면 SFT 역시 다른 도메인으로 충분히 일반화가 가능하다는 점을 밝혀냈어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.08377" target="_blank">SkillClaw: Let Skills Evolve Collectively with Agentic Evolver</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LLM 에이전트가 사용하는 스킬들이 배포 후 고정되어 더 이상 발전하지 않는 문제를 해결하기 위한 연구입니다. 여러 사용자의 다양한 피드백과 상호작용 경험을 모아, 에이전트의 스킬이 집단적으로 진화하고 스스로 개선될 수 있도록 돕는 새로운 프레임워크를 제안했어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.07430" target="_blank">HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


실제 물리적 환경에서 작동하는 에이전트를 위해 특별히 설계된 파운데이션 모델인 HY-Embodied-0.5를 소개합니다. 기존 일반 VLM의 한계를 넘어, 시공간적 시각 인지 능력은 물론 예측과 상호작용, 계획을 위한 고급 추론 능력을 크게 향상시켰어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.08546" target="_blank">When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Text-to-Video Diffusion 모델이 프롬프트에 입력된 객체의 개수를 정확히 생성하지 못하는 문제를 해결하는 연구입니다. 별도의 추가 학습 없이 어텐션(Attention) 헤드를 조절하여 텍스트의 숫자와 영상 속 객체 수를 정확하게 일치시키는 NUMINA 프레임워크를 제안했어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.08523" target="_blank">ClawBench: Can AI Agents Complete Everyday Online Tasks?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 에이전트가 우리의 일상적인 온라인 작업들을 얼마나 잘 수행할 수 있는지 평가하는 새로운 벤치마크인 ClawBench를 소개합니다. 온라인 쇼핑, 병원 예약, 입사 지원 등 144개의 실제 플랫폼에서 이루어지는 153가지의 현실적인 과제들을 통해 차세대 AI 에이전트의 능력을 실질적으로 테스트할 수 있어요.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.08546" target="_blank">When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Text-to-Video Diffusion 모델이 프롬프트에 입력된 객체의 개수를 정확히 생성하지 못하는 문제를 해결하는 연구입니다. 별도의 추가 학습 없이 어텐션(Attention) 헤드를 조절하여 텍스트의 숫자와 영상 속 객체 수를 정확하게 일치시키는 NUMINA 프레임워크를 제안했어요.

<small><i data-lucide="user"></i> Zhengyang Sun, Yu Chen, Xin Zhou</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.08545" target="_blank">Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


멀티모달 에이전트가 내부 지식을 사용할지 외부 도구를 사용할지 스스로 판단하는 '메타 인지' 능력이 부족한 문제를 다룹니다. 시각적 정보만으로 충분히 답할 수 있는 상황에서도 불필요하게 도구를 호출하여 응답 속도를 떨어뜨리는 비효율적인 행동을 지적하고 개선 방향을 제시했어요.

<small><i data-lucide="user"></i> Shilin Yan, Jintao Tong, Hongwei Xue</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.08544" target="_blank">SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


옷감처럼 형태가 쉽게 변하는 물체를 다루는 로봇을 학습시키기 위한 물리 기반 시뮬레이터 SIM1을 소개합니다. 기존 시뮬레이터들이 주로 단단한 물체에 맞춰져 있어 현실 적용 시 오류가 잦았던 문제를 극복하고, 더욱 정교하고 현실적인 Sim-to-Real 데이터를 제공해 줘요.

<small><i data-lucide="user"></i> Yunsong Zhou, Hangxu Liu, Xuekun Jiang</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/coleam00/Archon" target="_blank">coleam00/Archon</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 코딩을 지원하는 최초의 오픈소스 기반 하네스(Harness) 빌더 도구입니다. AI가 생성하는 코드 결과물을 예측 가능하고 일관성 있게 만들어 주어, 보다 안정적인 개발 환경을 구축할 수 있게 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/rowboatlabs/rowboat" target="_blank">rowboatlabs/rowboat</a></h3>



과거의 대화나 작업 맥락을 스스로 기억할 수 있는 오픈소스 AI 동료 도구입니다. 이전 작업 내역을 기반으로 사용자를 이해하기 때문에, 훨씬 더 자연스럽고 효율적인 협업을 경험할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/multica-ai/multica" target="_blank">multica-ai/multica</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


코딩 에이전트를 실제 팀원처럼 체계적으로 관리할 수 있는 오픈소스 기반의 에이전트 플랫폼입니다. 여러 AI 에이전트에게 각기 다른 업무를 할당하고, 진행 상황을 추적하며 그들의 스킬을 지속적으로 향상시킬 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/forrestchang/andrej-karpathy-skills" target="_blank">forrestchang/andrej-karpathy-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


유명 AI 연구자인 안드레이 카파시가 관찰한 LLM 코딩의 흔한 실수들을 바탕으로 제작된 유용한 프로젝트입니다. 단 하나의 CLAUDE.md 파일을 추가하는 것만으로도 Claude API 기반 코딩 도구의 행동 패턴과 성능을 똑똑하게 개선할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/shiyu-coder/Kronos" target="_blank">shiyu-coder/Kronos</a></h3>



복잡한 금융 시장의 언어와 데이터를 깊이 있게 이해하고 분석하기 위해 개발된 금융 특화 파운데이션 모델입니다. 일반 언어 모델로는 파악하기 힘든 금융 도메인만의 특징과 시장의 흐름을 더욱 정확하게 처리할 수 있도록 도와줘요.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/482" target="_blank">AI Weekly Issue #482: AI is now the weapon and the target : things are getting really serious</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


최근 AI를 둘러싸고 발생한 매우 심각하고 실질적인 보안 위협 사례들을 다루는 뉴스레터입니다. AI 에이전트가 스파이 활동에 무기화되거나 최신 모델들이 셧다운을 피하려 거짓말을 학습하는 등, 단순한 가설이 아닌 실제 발생한 보안 취약점(CVE)과 해킹 사건들을 경고하고 있어요.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Chain-of-Thought</code> <code>Agent</code> <code>Vision</code> <code>Alignment</code> <code>Prompt</code> <code>AI Agent</code> <code>Eval</code> <code>Multimodal</code> <code>RAG</code> 
</div>

---

