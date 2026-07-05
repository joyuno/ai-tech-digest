---
layout: post
title: "Anthropic·OpenAI·Google, 주요 모델 시스템 프롬프트 유출"
date: 2026-07-06
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "asgeirtj/system_prompts_leaks"
daily_url: "https://github.com/asgeirtj/system_prompts_leaks"
daily_image: "https://opengraph.githubassets.com/auto/asgeirtj/system_prompts_leaks"
daily_keywords: ["AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.02512v1/x1.png" alt="Program-as-Weights: A Programming Paradigm for Fuzzy Functions" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.02512" target="_blank">Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></h3>







기존의 규칙 기반 프로그래밍으로 구현하기 어려운 모호한 작업들을 LLM API에 의존하는 대신, 자연어 명세를 소형 신경망으로 컴파일하는 새로운 패러다임을 제안합니다. 'Program-as-Weights(PaW)'라고 불리는 이 접근법은 외부 API 호출 없이도 로컬 환경에서 빠르고 효율적으로 애매한 함수를 실행할 수 있게 해줍니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 83</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2607.02255" target="_blank">AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


장기적인 작업을 수행하는 LLM 에이전트의 메모리 관리 문제를 해결하기 위해, 과거의 모든 정보를 무작정 쌓는 대신 제한된 메모리 계약을 제안합니다. 'AgenticSTS'라는 새로운 테스트베드는 매번 의사결정을 할 때마다 원시적인 대화 기록이 아닌, 유형별로 검색된 정보로 구성된 새로운 메시지를 사용함으로써 에이전트의 성능을 정밀하게 평가합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 47</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.02440v1/x1.png" alt="EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.02440" target="_blank">EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


자율 에이전트가 피드백을 통해 실행 가능한 정책을 개선하는 능력을 정밀하게 평가하기 위한 새로운 프레임워크 'Autonomous Policy Evolution'을 소개합니다. 이를 구현한 'EvoPolicyGym' 벤치마크는 제한된 상호작용 예산 내에서 에이전트가 정책 코드를 반복적으로 수정하는 과정을 관찰함으로써, 최종 점수만이 아닌 정책의 진화 과정을 체계적으로 측정합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 43</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.30562v1/figs/flashmorph.png" alt="Morphing into Hybrid Attention Models" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.30562" target="_blank">Morphing into Hybrid Attention Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


긴 컨텍스트 처리 효율을 높이는 하이브리드 어텐션 모델의 성능은 어떤 레이어에 풀 어텐션을 유지하느냐에 따라 크게 좌우됩니다. 기존의 휴리스틱 방식과 달리, 이 연구는 레이어 간의 상호의존성을 고려하여 최적의 레이어 조합을 찾아내는 새로운 변환 방법을 제안함으로써 모델의 성능 저하를 최소화합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 39</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.28322v2/x1.png" alt="PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.28322" target="_blank">PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 멀티모달 벤치마크 점수가 실제 성능을 제대로 반영하지 못하는 문제를 해결하기 위해, 인간의 인식과 유사한 평가 프레임워크 'PerceptionRubrics'를 제안합니다. 이 프레임워크는 전체적인 의미 일치 여부만 보는 대신, 1,000개 이상의 이미지에 대해 12,000개가 넘는 세분화된 평가 기준(루브릭)을 적용하여 모델의 능력을 원자 단위로 정밀하게 감사합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 38</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.02512" target="_blank">Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></h3>







LLM API에 의존하던 로그 분석이나 검색 결과 순위 지정과 같은 모호한 프로그래밍 작업을 해결하기 위한 새로운 패러다임을 제안합니다. 이 'Program-as-Weights' (PaW) 방식은 자연어 명세를 작고 로컬에서 실행 가능한 신경망으로 컴파일하여, 비용과 재현성 문제를 개선합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Wentao Zhang, Liliana Hotsko, Woojeong Kim</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.02517" target="_blank">WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#World Model</span> <span class="sub-tag">#LoRA</span> <span class="sub-tag">#RAG</span> <span class="sub-tag">#Orchestration</span> 
</div>


'WorldDirector'는 객체의 움직임을 지속적으로 기억하고 자유로운 시점 탐색이 가능한 고도로 제어 가능한 비디오 월드 모델 프레임워크입니다. 기존 모델과 달리 물리적 역학과 시각적 렌더링을 명확히 분리하고, LLM을 활용하여 3D 궤적과 카메라 움직임을 조율함으로써 더욱 정교한 시뮬레이션 환경을 구축합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Hanlin Wang, Hao Ouyang, Qiuyu Wang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.02508" target="_blank">From SRA to Self-Flow: Data Augmentation or Self-Supervision?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Diffusion</span> <span class="sub-tag">#Alignment</span> 
</div>


확산 트랜스포머(diffusion transformer) 학습을 가속하는 자기 정렬(self-alignment) 기법인 SRA와 Self-Flow의 성능 향상 원인을 분석합니다. 특히 Self-Flow가 도입한 '이중 시간 스케줄링'이 서로 다른 시간대의 토큰 상호작용 때문인지, 아니면 데이터 증강이나 자기 지도 학습(self-supervision)의 효과인지 그 근본적인 메커니즘을 탐구합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Dengyang Jiang, Mengmeng Wang, Harry Yang</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Zackriya-Solutions/meetily/main/docs/Meetily-6.png" alt="Zackriya-Solutions/meetily" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Zackriya-Solutions/meetily" target="_blank">Zackriya-Solutions/meetily</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



Meetily는 개인정보 보호를 최우선으로 하는 AI 회의 비서 애플리케이션입니다. Rust로 개발되어 클라우드 없이 100% 로컬 환경에서 작동하며, 빠른 실시간 음성 인식과 화자 분리, 요약 기능을 제공하는 오픈소스 프로젝트입니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1409 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/openai/codex-plugin-cc" alt="openai/codex-plugin-cc" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/openai/codex-plugin-cc" target="_blank">openai/codex-plugin-cc</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


이 프로젝트는 Claude Code 환경 내에서 OpenAI의 Codex를 활용할 수 있게 해주는 플러그인입니다. 사용자는 이를 통해 코드 리뷰를 수행하거나 특정 개발 작업을 위임하는 등 생산성을 높일 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1519 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/asgeirtj/system_prompts_leaks" alt="asgeirtj/system_prompts_leaks" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/asgeirtj/system_prompts_leaks" target="_blank">asgeirtj/system_prompts_leaks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


다양한 AI 모델의 시스템 프롬프트를 추출하여 모아놓은 저장소입니다. Anthropic의 Claude, OpenAI의 GPT, Google의 Gemini 등 주요 LLM이 어떤 내부 명령어로 작동하는지 엿볼 수 있으며, 지속적으로 업데이트됩니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 981 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/assets/readme-banner.webp" alt="Leonxlnx/taste-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Leonxlnx/taste-skill" target="_blank">Leonxlnx/taste-skill</a></h3>







Taste-Skill은 AI가 단조롭고 일반적인 결과물을 생성하는 것을 방지해 주는 프로젝트입니다. AI에게 '좋은 취향'을 부여하여 더 흥미롭고 독창적인 결과물을 만들도록 유도하는 것을 목표로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 850 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/alirezarezvani/claude-skills" alt="alirezarezvani/claude-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/alirezarezvani/claude-skills" target="_blank">alirezarezvani/claude-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


Claude Code, Codex, Gemini CLI 등 다양한 코딩 에이전트를 위한 330개 이상의 스킬과 플러그인을 모아놓은 종합 패키지입니다. 엔지니어링, 마케팅, 재무 등 여러 전문 분야와 일상적인 생산성 향상에 필요한 기능들을 포함하고 있어 AI 에이전트의 활용도를 크게 높여줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 394 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Retrieval</code> <code>Agent</code> <code>Prompt</code> <code>Eval</code> <code>Transformer</code> <code>Multimodal</code> <code>LoRA</code> <code>RAG</code> <code>Orchestration</code> 
</div>