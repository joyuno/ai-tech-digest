---
layout: post
title: "diagram-design — Claude, Codex용 38종 다이어그램 타입 제공"
date: 2026-09-07
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "cathrynlavery/diagram-design"
daily_url: "https://github.com/cathrynlavery/diagram-design"
daily_image: "https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/thumbs/architecture.webp"
daily_keywords: ["AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.04199v1/paw_helper_case_study.png" alt="Compile by Training: Turning Natural-Language Specifications into Local Neural Functions" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.04199" target="_blank">Compile by Training: Turning Natural-Language Specifications into Local Neural Functions</a></h3>







자연어 명령을 로컬에서 실행 가능한 작은 신경망 함수로 변환하는 '학습을 통한 컴파일' 기법을 제안합니다. 이 방식은 컴파일 시점에 대규모 '교사' 모델이 생성한 데이터를 바탕으로 소형 '해석기' 모델을 학습시켜, 반복적인 비용과 지연 시간 없이 특정 텍스트 처리 기능을 재사용할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 317</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.04148v1/framework.png" alt="Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.04148" target="_blank">Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


터미널 기반 코드 에이전트의 학습 데이터는 많지만 실제 실행 가능한 환경은 부족하다는 문제에 주목합니다. '터미널-유니버스'는 기존 에이전트의 실행 기록을 재사용하여 상호작용이 가능한 확장형 터미널 환경으로 변환하는 기술로, 이를 통해 에이전트의 후속 학습 효율을 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 272</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.03796v1/qwen_image_bench_overall.png" alt="LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.03796" target="_blank">LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Diffusion</span> <span class="sub-tag">#VLM</span> 
</div>


완전한 오픈소스 학습 레시피를 기반으로 강력한 이미지 생성기를 구축하는 'LLaDA-Image' 프레임워크를 소개합니다. 이 프레임워크는 처음부터 학습시킨 DiT(Diffusion Transformer)와 LLaDA2.0-Mini 기반의 비전-언어 모듈을 결합하며, 특히 이미지 전용 사전 학습을 통해 강력한 시각적 생성 능력을 먼저 확보하는 전략을 사용합니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> inclusionAI/LLaDA-Image · ★ 147</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 227</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.03430" target="_blank">Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


LLM의 장문 추론 시 발생하는 KV 캐시 메모리 병목 현상을 해결하기 위해 '무작위 어텐션(Random Attention)'을 제안합니다. 기존 방식과 달리 캐시의 중요도를 계산하지 않고, 초기 프롬프트를 제외한 나머지를 무작위로 제거하여 복잡한 연산 없이도 추론 효율성을 크게 향상시킵니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 163</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2608.26730" target="_blank">Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


자율적으로 LLM을 후속 학습시킬 때, 모델이 변경됨에 따라 과거의 학습 경험 중 어떤 것을 재사용할지 결정하는 문제를 다룹니다. 이 연구는 특정 업데이트의 효과가 부모 모델에 따라 달라진다는 점에 착안하여, 모델 변화 후에도 과거의 어떤 업데이트 증거가 여전히 유효한지 판단하는 '조건부 경험 전이' 방법을 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 150</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04199" target="_blank">Compile by Training: Turning Natural-Language Specifications into Local Neural Functions</a></h3>







자연어 지시를 재사용 가능한 로컬 신경망 함수로 변환하는 'Compile by Training' 기법을 제안합니다. 이 방식은 컴파일 시점에 대형 교사 모델이 생성한 예시로 소형 어댑터를 학습시켜, 매번 원격 모델을 호출하는 비용과 지연 시간 없이 특정 작업을 위한 작고 효율적인 함수를 만들어냅니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yuntian Deng, Pengyu Nie, Stuart Shieber</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04196" target="_blank">Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



외부 모듈 없이 물리적 이해, 공간 시뮬레이션, 3D 월드 생성 및 재구성을 통합하는 단일 멀티모달 아키텍처 'Puffin-World'를 제안합니다. 이 프레임워크는 물리, 기하, 외형이라는 세 가지 세계 상태를 공동으로 모델링하여 3D 세계를 안정적으로 구축하고 상호작용합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Kang Liao, Yihang Luo, Xiao-Ming Wu</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04201" target="_blank">Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction</a></h3>







긴 비디오에서 온라인 3D 재구성 성능이 저하되는 문제를 해결하기 위한 'Scal3R' 기법을 소개합니다. 이 접근법은 전역 자세 추정과 지역 기하학 정보를 분리하고 효율적인 다중 상대 자세 쿼리를 학습하여, 긴 비디오에서도 오류 누적 없이 안정적인 3D 재구성을 가능하게 합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Chin-Yang Lin, Yang-Che Sun, Cheng Sun</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/affaan-m/ECC/main/docs/releases/2.1.0/assets/ecc-plan-canvas-demo.gif" alt="affaan-m/ECC" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/affaan-m/ECC" target="_blank">affaan-m/ECC</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


AI 에이전트의 성능 최적화를 위한 시스템으로, Claude Code, Codex 등 다양한 모델을 지원합니다. 기술, 메모리, 보안 등의 기능을 통합하여 연구 중심의 개발을 목표로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1485 today</span> 

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




  



실제 엔지니어가 사용하는 AI 에이전트용 기술(skill) 모음입니다. 개발자가 자신의 에이전트 디렉토리에서 직접 가져온 실용적인 예제들을 제공하여 현실적인 문제 해결에 도움을 줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2207 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/thumbs/architecture.webp" alt="cathrynlavery/diagram-design" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/cathrynlavery/diagram-design" target="_blank">cathrynlavery/diagram-design</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


Claude Code, Codex와 같은 AI 모델을 위해 디자인된 38가지 다이어그램 유형을 제공합니다. 외부 도구 없이 독립적인 HTML과 SVG 파일만으로 그림자 효과 없는 깔끔한 다이어그램을 만들 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 620 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/openai/skills" alt="openai/skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/openai/skills" target="_blank">openai/skills</a></h3>







OpenAI가 공식적으로 제공하는 Codex 모델을 위한 기술(skill) 카탈로그입니다. 이 저장소는 Codex가 다양한 작업을 더 효과적으로 수행할 수 있도록 돕는 기능들의 모음집 역할을 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 46 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/blader/humanizer" alt="blader/humanizer" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/blader/humanizer" target="_blank">blader/humanizer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



AI가 생성한 글에서 인공적인 느낌을 제거하여 사람이 쓴 것처럼 자연스럽게 만들어주는 에이전트 기술입니다. 이 도구를 사용하면 텍스트를 보다 인간적인 문체로 다듬을 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 748 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Agent</code> <code>Eval</code> <code>Vision</code> <code>Reasoning</code> <code>Prompt</code> <code>LLM</code> <code>Multimodal</code> <code>Claude</code> <code>Cursor</code> <code>Claude Code</code> 
</div>