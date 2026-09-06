---
layout: post
title: "ECC — AI 에이전트 성능 최적화를 위한 하네스 시스템 (29자). This fits the length requirement (25-45)"
date: 2026-09-06
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "affaan-m/ECC"
daily_url: "https://github.com/affaan-m/ECC"
daily_image: "https://raw.githubusercontent.com/affaan-m/ECC/main/docs/releases/2.1.0/assets/ecc-plan-canvas-demo.gif"
daily_keywords: ["AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.04199v1/paw_helper_case_study.png" alt="Compile by Training: Turning Natural-Language Specifications into Local Neural Functions" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.04199" target="_blank">Compile by Training: Turning Natural-Language Specifications into Local Neural Functions</a></h3>







자연어 명령을 매번 거대 원격 모델로 처리하는 것은 비용과 지연 문제가 크므로, 이 연구는 자연어 명세를 재사용 가능한 소형 신경망 함수로 '컴파일'하는 방법을 제안합니다. 컴파일 시점에 대형 교사 모델이 생성한 예제로 소형 어댑터를 훈련시켜, 원격 서버 의존 없이 로컬에서 빠르고 효율적으로 실행되는 맞춤형 함수를 만듭니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 310</span> 


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


에이전트의 행동 기록 데이터는 많지만 실제 훈련에 필요한 실행 환경은 부족한 문제를 해결하기 위해, 이 연구는 기존 기록에 포함된 도구 실행 내역을 분석하여 확장 가능한 가상 터미널 환경으로 전환하는 'Terminal-Universe'를 제안합니다. 이 방법은 단일 시연 데이터로부터 검증 가능한 여러 작업과 실행 피드백을 제공하는 풍부한 훈련 환경을 자동으로 구축합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 265</span> 


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


이 논문은 완전한 오픈 소스 훈련법을 기반으로 강력한 이미지 생성기를 구축하는 'LLaDA-Image' 프레임워크를 소개합니다. 이미지-텍스트 쌍 데이터에 대한 의존도를 낮추고 이미지 전용 사전 훈련으로 강력한 시각적 생성 능력을 먼저 확보한 후, 이를 언어 이해 모듈과 결합하는 효율적인 방식을 사용합니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> inclusionAI/LLaDA-Image · ★ 106</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 222</span> 


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


LLM의 긴 추론 과정에서 발생하는 KV 캐시 메모리 병목 현상을 해결하기 위해 기존 방식들은 중요 토큰을 선별하여 저장했지만, 이 연구는 그러한 선별 과정이 큰 효과가 없음을 보입니다. 대신 초기 프롬프트를 제외한 캐시를 무작위로 제거하는 'Random Attention' 기법을 제안하며, 이 단순한 방식이 복잡한 기존 기법들과 비슷하거나 더 나은 성능을 효율적으로 달성합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 159</span> 


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


LLM을 지속적으로 후속 훈련시킬 때 과거의 어떤 훈련 경험을 재사용할지 결정하는 것은 매우 중요하며, 이 연구는 부모 모델의 변경 정도에 따라 과거 경험의 재사용 여부를 조건부로 결정하는 방법을 제안합니다. 이를 통해 시스템은 오래되어 유효하지 않은 정보로 인한 성능 저하를 피하고, 관련성 높은 과거 경험만을 선별적으로 활용하여 훈련 효율성을 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 149</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04199" target="_blank">Compile by Training: Turning Natural-Language Specifications into Local Neural Functions</a></h3>







‘Compile by training’은 자연어 지시를 재사용 가능한 소형 로컬 신경망 함수로 변환하는 기법입니다. 컴파일 시점에 대형 교사 모델이 생성한 데이터를 바탕으로 작은 어댑터를 학습시키므로, 이후에는 원격 모델 호출 없이도 빠르고 효율적으로 작업을 수행할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yuntian Deng, Pengyu Nie, Stuart Shieber</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04196" target="_blank">Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



Puffin-World는 물리적 이해, 공간 시뮬레이션, 3D 세계 생성을 외부 모듈 없이 통합한 새로운 멀티모달 아키텍처를 제안합니다. 이 모델은 물리, 기하, 외형이라는 세 가지 세계 상태를 함께 모델링하고 통합된 '옴니-카메라' 표현을 사용하여, 3D 세계를 안정적으로 구축하고 상호작용할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Kang Liao, Yihang Luo, Xiao-Ming Wu</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.04201" target="_blank">Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction</a></h3>







Scal3R은 긴 영상에서 발생하는 온라인 3D 재구성 실패 문제를 해결하는 새로운 접근법입니다. 기존 모델이 고정된 첫 프레임을 기준으로 자세를 추정하며 오류가 누적되는 것과 달리, Scal3R은 다중 상대 자세 쿼리를 도입하여 기하학적 붕괴 없이 안정적인 재구성을 수행합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Chin-Yang Lin, Yang-Che Sun, Cheng Sun</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" alt="mattpocock/skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mattpocock/skills" target="_blank">mattpocock/skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



실제 엔지니어가 사용하는 AI 에이전트용 스킬 모음입니다. 개발자의 개인 디렉토리에서 직접 가져온 실용적인 기술들을 담고 있어, 현실적인 문제 해결에 바로 적용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2692 today</span> 

</div>

</div>


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


ECC는 AI 에이전트의 성능을 최적화하기 위한 시스템입니다. Claude Code, Codex와 같은 코드 생성 AI를 위해 스킬, 메모리, 보안 등 다양한 요소를 통합하고 연구 중심의 개발을 지원하여 에이전트의 능력을 극대화합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1314 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/DietrichGebert/ponytail/main/assets/logo.png" alt="DietrichGebert/ponytail" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/DietrichGebert/ponytail" target="_blank">DietrichGebert/ponytail</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 프로젝트는 AI 에이전트가 마치 '게으른 시니어 개발자'처럼 생각하도록 만듭니다. '가장 좋은 코드는 작성하지 않은 코드'라는 철학을 바탕으로, 불필요한 작업을 피하고 가장 효율적인 해결책을 찾도록 유도합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2845 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/anthropics/skills" alt="anthropics/skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/anthropics/skills" target="_blank">anthropics/skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



AI 모델 클로드(Claude) 개발사 앤트로픽(Anthropic)이 공개한 공식 에이전트 스킬 저장소입니다. 이 프로젝트는 AI 에이전트가 다양한 작업을 수행할 수 있도록 돕는 표준화된 기술들을 제공하여 생태계 확장에 기여합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 475 today</span> 

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


Claude Code, Codex 등 AI를 위한 38가지 다이어그램 디자인 유형을 제공합니다. 그림자 효과나 Mermaid 같은 복잡한 도구 없이, 독립적인 HTML과 SVG 파일만으로 깔끔하고 전문적인 다이어그램을 생성할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 855 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/openai-faces-50-plus-lawsuits-over-alleged-chatgpt-harm" target="_blank">AI Weekly Issue #529: OpenAI faces 50-plus lawsuits over alleged ChatGPT harm</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



OpenAI가 ChatGPT로 인한 피해를 주장하는 50건 이상의 소송에 직면했습니다. 특히 캐나다 학교 총기 난사 사건의 생존자들은 OpenAI가 경찰에 사전 경고를 하지 않았다고 비난하며 새로운 소송을 제기했으며, 회사는 이에 대해 주요 혐의를 부인하고 있습니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Agent</code> <code>Eval</code> <code>Vision</code> <code>Reasoning</code> <code>Prompt</code> <code>LLM</code> <code>Multimodal</code> <code>Claude</code> <code>Cursor</code> <code>AI Agent</code> 
</div>