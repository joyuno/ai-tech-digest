---
layout: post
title: "gstack — CEO부터 QA까지 구현한 Claude Code 도구 모음"
date: 2026-11-06
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "garrytan/gstack"
daily_url: "https://github.com/garrytan/gstack"
daily_image: "https://opengraph.githubassets.com/auto/garrytan/gstack"
daily_keywords: ["AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.06728v1/teaser_1024.png" alt="Turns Matter: Advancing Streaming Video RL via Turn-Level Credit" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.06728" target="_blank">Turns Matter: Advancing Streaming Video RL via Turn-Level Credit</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


스트리밍 비디오 이해 모델은 계속 관찰할지 응답할지를 매 턴마다 판단해야 하지만, 기존 강화학습은 전체 궤적 단위로만 보상을 부여해 불필요한 반복 응답이나 후속 행동 억제를 유발했습니다. 본 연구에서는 각 턴의 기여도를 정밀하게 분별하여 보상하는 TurnWise 프레임워크를 제안했습니다. 이를 통해 모델은 실시간 영상 흐름 속에서 적절한 타이밍에 알맞은 반응을 수행하는 능력을 크게 향상시켰습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 124</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.06918v1/NEO-VLA_Model_Overview.png" alt="From Pixels to Actions - Towards Native Vision-Language-Action Policies" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.06918" target="_blank">From Pixels to Actions - Towards Native Vision-Language-Action Policies</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> <span class="sub-tag">#DPO</span> 
</div>


기존 시각-언어-행동 모델은 시각 정보를 인코더로 미리 압축한 뒤 행동을 추론하므로, 정밀 조작에 필수적인 미세 형태나 깊이 정보가 쉽게 손실되는 한계가 있었습니다. 연구진은 고정된 시각 특징 대신 동적으로 변화하는 시각 연산 과정에 직접 접근하는 NEO-VLA 정책을 제안했습니다. 이로써 픽셀 수준의 시각 단서를 정교한 로봇 조작 제어로 직결시키는 네이티브 정책을 성공적으로 구현했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 56</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.06910v1/task_proposal.png" alt="FrontierPhysics: Evaluating Agents for End-to-End Physics Research" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.06910" target="_blank">FrontierPhysics: Evaluating Agents for End-to-End Physics Research</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 물리학 벤치마크는 단편적인 문제 풀이나 정답이 주어진 재현 작업에 치중되어 실제 연구의 질적 수준을 평가하기 어려웠습니다. 연구진은 42명의 물리학자가 실제 연구를 기반으로 제작한 이론, 계산, 실험 물리 분야의 56개 과제로 구성된 FrontierPhysics 벤치마크를 구축했습니다. AI 에이전트는 이를 통해 문헌 조사부터 최종 결론 도출까지 실제 물리 연구 전 과정을 종단간으로 평가받게 됩니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 47</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.06483v1/agent-rl-intro-figure_v6.png" alt="What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.06483" target="_blank">What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


멀티턴 에이전트 강화학습은 복잡한 장기 과제 해결에 유리하지만 상호작용 횟수 예산이 줄어들면 성능 향상 폭이 급격히 축소됩니다. 또한 이 방식은 모든 단일 단계의 의사결정 능력을 높이기보다 실패 후 오류 복구와 장기적 계획 유지에 집중적으로 기여하는 것으로 나타났습니다. 연구진은 포괄적인 평가 지표를 도입하여 강화학습이 LLM 에이전트의 어떤 역량을 실질적으로 개선하는지 명확히 규명했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 34</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.37257v3/GameVerse_v1.png" alt="GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.37257" target="_blank">GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling</a></h3>







상호작용형 월드 모델은 행동 입력을 받아 동적 환경을 생성할 수 있지만, 1분 이상의 장기 일관성을 유지하는 데는 데이터 부족으로 인한 어려움을 겪어왔습니다. 기존 게임 영상 데이터셋은 10초 미만의 짧은 클립과 거친 설명에 머물러 장기적인 제어 학습에 턱없이 부족했습니다. 이에 연구진은 분 단위의 연속 플레이 영상과 정밀한 설명을 포함한 GameVerse 데이터셋을 공개하여 장기 월드 모델링의 한계를 돌파했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 34</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.06918" target="_blank">From Pixels to Actions - Towards Native Vision-Language-Action Policies</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> <span class="sub-tag">#DPO</span> 
</div>


기존 비전-언어-행동 모델은 시각 정보를 사전에 압축하기 때문에 정밀한 로봇 조작에 필수적인 미세한 기하학적 정보나 상태 변화를 놓치는 한계가 있습니다. 연구진은 고정된 시각 정보를 단순히 전달받는 대신 동적인 시각 연산에 직접 접근하는 네이티브 정책인 NEO-VLA를 제안합니다. 이를 통해 시각적 세부 정보를 보존하며 더욱 정교하고 안정적인 물리적 조작을 구현할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Weichen Fan, Haiwen Diao, Penghao Wu</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.07461" target="_blank">The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> <span class="sub-tag">#Eval</span> 
</div>


최신 AI 모델들도 현실 환경의 복잡한 작업을 끝까지 완수하는 데 어려움을 겪고 있으며, 자원을 확보한 뒤 실제 작업에 적용하는 마지막 단계에서 주로 실패합니다. 이 연구는 매번 도구를 새로 구축하는 대신 재사용 가능한 빌딩 블록 형태로 설계된 에이전트 네이티브 프리미티브를 해결책으로 제시합니다. 이를 활용하면 에이전트의 실행 역량을 표준화하여 현실 문제 해결 능력을 대폭 끌어올릴 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Haibo Jin, Peng Kuang, Xiaopeng Yuan</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.06911" target="_blank">BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


자율 화학 실험실은 AI가 실험 환경을 인식하고 안전 및 절차적 제약 속에서 직접 행동하는 체화된 자동화를 목표로 발전하고 있습니다. 하지만 기존 벤치마크는 단순한 안전 감지나 일반 과학 지식 평가에 치우쳐 있어 MLLM의 실제 실험 실행 역량을 검증하기 어려웠습니다. 이에 연구진은 화학 실험실의 두뇌 역할을 정밀하게 측정할 수 있는 전문가 큐레이션 실행 중심 벤치마크 BEAKER를 새롭게 선보였습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Fei Lin, Tengchao Zhang, Ziyang Gong</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/NVIDIA/auto-ontology/main/docs/assets/arch.png" alt="NVIDIA/auto-ontology" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/NVIDIA/auto-ontology" target="_blank">NVIDIA/auto-ontology</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


엔비디아의 Auto Ontology는 데이터 위에 시맨틱 그래프 기반의 추론 계층을 구축하는 파이썬 프레임워크입니다. 이 기술은 결정론적인 쿼리 생성과 향상된 컨텍스트 검색을 지원합니다. 이를 통해 LLM과 AI 에이전트 워크플로 전반에서 설명 가능한 인공지능을 구현할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2679 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" alt="mattpocock/skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mattpocock/skills" target="_blank">mattpocock/skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



현업 엔지니어를 위해 실제 개발 환경의 에이전트 디렉터리에서 엄선한 실전 스킬 모음집입니다. 일상적인 개발 작업의 효율을 높일 수 있는 구체적이고 실용적인 에이전트 도구들을 제공합니다. AI 기반 개발 자동화에 관심 있는 엔지니어에게 유용한 참고 자료가 됩니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2071 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/garrytan/gstack" alt="garrytan/gstack" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/garrytan/gstack" target="_blank">garrytan/gstack</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


유명 투자자 개리 탄이 실제로 사용하는 Claude Code 개발 환경 설정을 그대로 공개한 프로젝트입니다. CEO, 디자이너, 엔지니어링 매니저, QA 등 23가지 역할을 수행하는 맞춤형 도구 모음으로 구성되어 있습니다. 복잡한 소프트웨어 개발 생명주기 전체를 AI로 보조받을 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 612 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Usagi-org/ai-goofish-monitor/master/static/img.png" alt="Usagi-org/ai-goofish-monitor" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Usagi-org/ai-goofish-monitor" target="_blank">Usagi-org/ai-goofish-monitor</a></h3>







Playwright와 AI 기술을 결합하여 중국 중고거래 플랫폼 셴위(Idle Fish)의 상품을 실시간 또는 주기적으로 모니터링하는 분석 시스템입니다. 직관적인 백엔드 관리 UI를 갖추고 있어 다중 모니터링 작업을 손쉽게 관리할 수 있습니다. 방대한 중고 매물 속에서 사용자가 원하는 최적의 상품을 스마트하게 선별해 줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 240 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/DataImpulse.png" alt="D4Vinci/Scrapling" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/D4Vinci/Scrapling" target="_blank">D4Vinci/Scrapling</a></h3>







단일 HTTP 요청부터 대규모 웹 크롤링까지 유연하게 처리할 수 있는 강력한 파이썬 기반 웹 스크래핑 프레임워크입니다. 데이터 수집 과정에서 마주하는 다양한 기술적 문제를 안정적으로 해결하도록 설계되었습니다. 활발한 커뮤니티와 팁 공유를 바탕으로 최신 스크래핑 기법을 손쉽게 적용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1655 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>RAG</code> <code>Vision</code> <code>DPO</code> <code>AI Agent</code> <code>Eval</code> <code>LLM</code> <code>Agent</code> <code>GPT</code> <code>Claude Code</code> <code>Safety</code> 
</div>