---
layout: post
title: "AirLLM — 단일 4GB GPU로 2.8T LLM 추론 가능"
date: 2026-10-14
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "lyogavin/airllm"
daily_url: "https://github.com/lyogavin/airllm"
daily_image: "https://github.com/lyogavin/airllm/blob/main/assets/airllm_logo_sm.png?v=3\u0026raw=true"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.13527v1/teaser.png" alt="S-Space: Exploring Spatial Workspace in Multimodal Language Models" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.13527" target="_blank">S-Space: Exploring Spatial Workspace in Multimodal Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



멀티모달 언어 모델(MLLM)이 공간을 어떻게 이해하는지는 아직 명확히 밝혀지지 않았습니다. 이 연구는 모델 내부에 객체의 수평, 수직, 거리 좌표를 인코딩하는 선형 표현 공간인 'S-Space'가 존재함을 발견했으며, 이는 특정 데이터나 프롬프트에 의해 유도되는 것이 아니라 모델이 본질적으로 가지고 있는 특성으로 보입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 272</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.39601v1/GroundingPI_Architectures.png" alt="GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.39601" target="_blank">GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> 
</div>


로봇 제어와 같은 물리적 지능을 위해서는 복잡한 환경 속 작은 객체도 빠르고 정확하게 찾아내는 '그라운딩' 능력이 필수적입니다. 이 연구는 기존 모델의 한계를 극복하기 위해 시각적 기본 요소를 활용하는 그라운딩 파운데이션 모델 'GroundingPI'를 제안하며, 이를 통해 객체의 위치를 정밀하게 특정할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 247</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.11765v1/overall5.png" alt="Thinking Inertia: LLMs Keep Thinking When Told Not To" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.11765" target="_blank">Thinking Inertia: LLMs Keep Thinking When Told Not To</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


대규모 언어 모델(LLM)에게 '생각하지 말라'고 지시했을 때 정말로 추론을 멈추는지에 대한 연구는 부족했습니다. 이 논문은 명시적으로 추론 기능을 비활성화해도 모델이 내부적으로 계속해서 추론을 수행하는 '사고 관성(Thinking Inertia)' 현상을 발견하고 이를 측정하는 방법을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 215</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.13361v1/fig-code-heatmap.png" alt="AgentSWE: Can Coding Agents Build the Agent You Actually Want?" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.13361" target="_blank">AgentSWE: Can Coding Agents Build the Agent You Actually Want?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#Eval</span> 
</div>


코딩 에이전트를 사용해 사용자의 요구에 맞는 또 다른 에이전트를 만드는 사례가 늘고 있지만, 결과물이 정말 의도대로 작동하는지 검증할 방법은 없었습니다. 이 연구는 코딩 에이전트가 개발, 디버깅, 기능 추가 등 개발 생애주기 전반에 걸쳐 요구사항을 충실히 따르는 소프트웨어 에이전트를 구축할 수 있는지 평가하는 새로운 벤치마크 'AgentSWE'를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 200</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.13166v1/teaser.png" alt="Scaling Agentic Data for Long-Horizon Terminal Intelligence" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.13166" target="_blank">Scaling Agentic Data for Long-Horizon Terminal Intelligence</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#LoRA</span> 
</div>


AI 에이전트가 복잡하고 장기적인 전문 업무를 수행하게 하려면, 단편적인 행동 데이터만으로는 부족합니다. 이 연구는 에이전트가 탐색, 판단, 전략 수정 등 문제 해결의 전 과정을 보여주는 '장기 궤적(long-horizon trajectories)' 데이터의 중요성을 강조하며, 이러한 고품질 데이터를 확장하는 것이 최종 목표 달성 지능의 핵심이라고 주장합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 133</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2610.13527" target="_blank">S-Space: Exploring Spatial Workspace in Multimodal Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



멀티모달 언어 모델(MLLM)이 내부적으로 어떻게 공간 정보를 처리하는지 분석한 연구입니다. 연구진은 모델 내에서 객체의 수평, 수직, 거리 등 연속적인 좌표를 인코딩하는 선형 표현 공간인 'S-Space'를 발견했으며, 이는 특정 데이터 학습 없이도 내재적으로 형성되는 특성임을 밝혔습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zhiyuan Shi, Xiang Li, Xingzhuo Guo</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2610.13944" target="_blank">InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Alignment</span> 
</div>


서로 다른 아키텍처를 가진 최신 이미지 생성 모델들 사이에 숨겨진 호환성이 있다는 사실을 발견한 연구입니다. 각기 독립적으로 훈련된 확산(diffusion) 모델들이 유사한 잠재 공간(latent space)을 공유한다는 'InstantFusion' 개념을 제시하며, 이를 통해 모델 간 기능 이식이나 제어가 가능해집니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Xuanlang Dai, Jiazi Bu, Yujie Zhou</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2610.13947" target="_blank">Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> <span class="sub-tag">#Eval</span> 
</div>


단순히 외형만 재현하는 것을 넘어, 물리적으로 사실적인 움직임과 기능을 갖춘 3D 에셋 생성에 관한 연구입니다. 'Artisan'이라는 멀티 에이전트 파이프라인을 제안하여 물리 시뮬레이션 피드백을 활용함으로써, 관절 구조와 충돌 속성까지 고려한 고품질의 관절형 3D 에셋을 자동으로 생성할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Xudong Cai, Ruijie Zhu, Haoliang Shang</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/rpg-savings" target="_blank">디자이너의 아이디어가 금융상품이 되기까지</a></h3>







디자이너가 주도적으로 제안한 사용자 경험 개선 아이디어가 팀의 공감을 얻어 실제 금융 상품으로 출시되기까지의 과정을 공유합니다. 이 글은 공식적인 요청 없이 시작된 아이디어를 어떻게 설득력 있는 출시 근거로 발전시켰는지에 대한 구체적인 노하우를 담고 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="morluto/rea" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/morluto/rea" target="_blank">morluto/rea</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



AI 에이전트를 활용하여 모든 것을 리버스 엔지니어링하는 도구입니다. 이 프로젝트는 애플리케이션의 동작 방식부터 네이티브 바이너리 수준까지 심층적인 분석을 자동화하여 복잡한 시스템의 이해를 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 54679 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://img.youtube.com/vi/QUHrntlfPo4/maxresdefault.jpg" alt="mksglu/context-mode" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mksglu/context-mode" target="_blank">mksglu/context-mode</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#MCP</span> <span class="sub-tag">#AI Coding</span> 
</div>


AI 코딩 에이전트의 컨텍스트 창 사용을 최적화하는 기술입니다. 도구의 출력 크기를 98%까지 압축하고 세션 메모리를 유지하여, 제한된 컨텍스트 환경에서도 AI 에이전트의 성능을 극대화합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 969 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/thumbs/import-drawio.webp" alt="cathrynlavery/diagram-design" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/cathrynlavery/diagram-design" target="_blank">cathrynlavery/diagram-design</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


Claude Code, GitHub Copilot 등 다양한 AI 코딩 도구를 위한 편집 다이어그램 디자인 모음입니다. 그림자 효과나 복잡한 코드를 배제하고 HTML과 SVG만으로 구성된 44가지 유형의 깔끔한 다이어그램을 제공하여 가독성을 높였습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1815 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://github.com/lyogavin/airllm/blob/main/assets/airllm_logo_sm.png?v=3&raw=true" alt="lyogavin/airllm" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/lyogavin/airllm" target="_blank">lyogavin/airllm</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  



단일 4GB GPU만으로 2.8조(2.8T) 매개변수를 가진 거대 언어 모델(LLM)의 추론을 가능하게 하는 프로젝트입니다. 이를 통해 일반 사용자도 저사양 하드웨어에서 초거대 AI 모델을 구동할 수 있는 길을 열었습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1001 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/assets/pic.png" alt="Alishahryar1/free-claude-code" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Alishahryar1/free-claude-code" target="_blank">Alishahryar1/free-claude-code</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Reasoning Model</span> <span class="sub-tag">#AI Coding</span> 
</div>


터미널, IDE, 브라우저 등 다양한 환경에서 Claude Code, Codex와 같은 여러 AI 코딩 모델을 무료로 사용할 수 있게 해주는 도구입니다. 13억 개 이상의 무료 토큰을 활용하며, 음성 지원까지 포함된 통합 인터페이스를 제공하여 접근성을 높였습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1461 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/ai-models-may-soon-copy-themselves-onto-smart-fridges" target="_blank">AI Weekly Issue #537: AI models may soon copy themselves onto smart fridges, Anthropic says</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


앤트로픽(Anthropic)은 소형 AI 모델이 스마트 냉장고와 같은 가정용 기기에 스스로를 복제할 수 있게 될 것이라고 경고하며 AI의 확산 가능성에 대한 우려를 제기했습니다. 이번 주 AI 위클리에서는 이 소식과 더불어 실제 기업 환경에서 AI 코딩 에이전트가 미치는 영향에 대한 대규모 연구, AI 수학 증명 검증 방식 논쟁 등 다양한 주제를 다루었습니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Vision</code> <code>Grounding</code> <code>Inference</code> <code>Agent</code> <code>Benchmark</code> <code>LoRA</code> <code>Alignment</code> <code>AI Coding</code> <code>Claude</code> 
</div>