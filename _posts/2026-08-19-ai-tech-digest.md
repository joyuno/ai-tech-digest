---
layout: post
title: "munder-difflin — 로컬에서 돌리는 멀티 에이전트 하네스"
date: 2026-08-19
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "chaitanyagiri/munder-difflin"
daily_url: "https://github.com/chaitanyagiri/munder-difflin"
daily_image: "https://raw.githubusercontent.com/chaitanyagiri/munder-difflin/main/docs/logo.png"
daily_keywords: ["Multi-Agent"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.16859v1/fig_teaser.png" alt="HarnessEval-W: Agentifying the Evaluation of Visual Worlds" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.16859" target="_blank">HarnessEval-W: Agentifying the Evaluation of Visual Worlds</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#World Model</span> <span class="sub-tag">#Eval</span> 
</div>


기존 월드 모델 벤치마크는 물리 법칙이나 인과 관계가 올바르게 작동하는지 판단하는 근거 없이 단순한 점수만 제공하는 한계가 있었습니다. HarnessEval-W는 이러한 평가 과정을 에이전트화하여, 점수에 대한 논리적 추론 과정을 자동으로 생성하고 검증함으로써 벤치마크의 신뢰도를 높이는 새로운 프레임워크입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 110</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2608.15089" target="_blank">StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



장기적인 작업을 수행하는 에이전트는 기반 모델의 성능이 충분하더라도 상태를 놓치거나 이전 경험을 활용하지 못하는 등 실행 시스템의 한계로 인해 실패하는 경우가 많습니다. StateM은 모델 가중치를 변경하지 않고 안정적인 상태 관리와 단계별 컨텍스트 활용으로 실행 시스템을 개선하는 '하네스 스케일링' 개념을 도입하여 에이전트의 작업 수행 능력을 크게 향상시킵니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 100</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.15265v1/Figure/fig_samples.png" alt="VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.15265" target="_blank">VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 3D 오픈 월드 구축 기술은 이상적인 환경에서만 평가되어, 멀티모달 에이전트의 사용자 의도 파악 및 3D 도구 활용 능력을 체계적으로 분석하기 어려웠습니다. VibeWorlding은 사용자 의도를 추론하고 3D 도구를 활용하여 자율적으로 3D 세계를 구축하는 에이전트를 벤치마킹하고 훈련시키기 위한 통합 프레임워크를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 51</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.15669v1/evolution.drawio.png" alt="Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.15669" target="_blank">Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#SSM</span> <span class="sub-tag">#Eval</span> 
</div>


분자나 단백질 서열 같은 방대한 가설 공간에서 최적의 해를 찾는 과학적 발견 과정에서 LLM은 유용하지만, 관찰되지 않은 새로운 후보에 대한 평가는 신뢰하기 어렵습니다. 이 논문은 생성 모델의 사전 지식과 경험적 모델 기반 탐색을 결합한 '대규모 발견 모델(Large Discovery Models)'을 통해, 광범위하고 구조화된 공간에서 보다 효율적으로 새로운 발견을 이끌어냅니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 49</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.16072v1/rollout.png" alt="Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.16072" target="_blank">Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization</a></h3>







여러 보상 목표를 동시에 최적화하는 기존 강화학습 방식은 고정된 가중치를 사용해, 이미 숙달된 목표에 불필요한 노력을 쏟는 비효율 문제가 있었습니다. 이 연구는 모델이 특정 목표를 얼마나 숙달했는지 인지하여 보상 가중치를 동적으로 조절하는 새로운 기법을 제안하며, 이를 통해 아직 숙달하지 못한 목표에 학습을 집중시켜 최적화 효율을 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 44</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.16859" target="_blank">HarnessEval-W: Agentifying the Evaluation of Visual Worlds</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#World Model</span> <span class="sub-tag">#Eval</span> 
</div>


기존 월드 모델 벤치마크는 단순 점수만 제공하여 평가의 신뢰성을 파악하기 어렵습니다. HarnessEval-W는 물리 법칙, 인과 관계 등의 위반 여부를 인간처럼 판단하고 그 근거를 함께 제시하여, 모델 평가에 대한 깊이 있는 이해와 신뢰를 제공하는 새로운 평가 프레임워크입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Weiliang Chen, Haowen Sun, Jun Gao</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.16798" target="_blank">ClawGym II: Exploring Black-Box RL on Agent Harness</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



에이전트 하네스(Agent harness)는 장기 과제(long-horizon task) 해결에 효과적이지만, 이를 활용한 강화학습(RL) 훈련은 확장성 문제로 인해 연구가 미진했습니다. 이에 ClawGym II는 샌드박스 기반 환경에서 복잡한 하네스를 통해 에이전트를 안정적으로 최적화하는 통합 블랙박스 RL 프레임워크를 제안하여 이 문제를 해결합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Huatong Song, Fei Bai, Ming Yang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.16887" target="_blank">An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models</a></h3>







이 논문은 텍스트-이미지 생성 분야에서 중요성이 커지고 있는 픽셀 공간(pixel-space) 확산 모델에 대한 실증적 연구를 다룹니다. 기존 연구와 달리 대규모 데이터셋을 직접 픽셀 공간에서 사전 훈련시킬 때 발생하는 수렴 속도 저하 문제를 발견했으며, 잠재 공간(latent-space) 모델에 필적하는 성능을 내기 위한 실용적인 훈련 방법을 탐구합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Dengyang Jiang, Ruoyi Du, Zhennan Chen</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/games-in-ads" target="_blank">토스는 어떻게 광고 속에 게임을 넣었을까</a></h3>







토스는 사용자가 광고를 직접 플레이하며 즐길 수 있는 '플레이어블 광고'를 도입하기 위해 자체 기술 개발을 선택했습니다. 외부 솔루션 대신 MRAID 표준에 기반한 광고 SDK를 직접 제작하여, 앱 환경에 최적화된 매끄러운 인터랙티브 광고 경험을 구현해냈습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/harry0703/MoneyPrinterTurbo/main/docs/webui.jpg" alt="harry0703/MoneyPrinterTurbo" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/harry0703/MoneyPrinterTurbo" target="_blank">harry0703/MoneyPrinterTurbo</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 프로젝트는 AI 대규모 모델과 자동화된 워크플로우를 활용하여, 주제나 키워드만으로 고화질의 짧은 동영상을 클릭 한 번에 생성해주는 도구입니다. 콘텐츠 제작 과정을 자동화하여 누구나 쉽게 영상을 만들 수 있도록 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2306 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/chaitanyagiri/munder-difflin/main/docs/logo.png" alt="chaitanyagiri/munder-difflin" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/chaitanyagiri/munder-difflin" target="_blank">chaitanyagiri/munder-difflin</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> 
</div>


이 프로젝트는 로컬 환경에서 여러 AI 에이전트를 동시에 실행하고 관리할 수 있도록 설계된 멀티 에이전트 개발 도구입니다. 개발자들은 자신의 컴퓨터에서 복잡한 에이전트 시스템을 손쉽게 구축하고 테스트할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 256 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/akitaonrails/ai-memory/main/docs/logo-light.png" alt="akitaonrails/ai-memory" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/akitaonrails/ai-memory" target="_blank">akitaonrails/ai-memory</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 프로젝트는 AI 코딩 에이전트를 위한 장기 기억 솔루션을 제공하여, 여러 다른 공급업체의 AI 에이전트 간에 작업 내용과 맥락을 원활하게 전달하고 공유할 수 있도록 돕습니다. 이를 통해 에이전트의 연속적인 작업 수행 능력을 향상시킵니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 730 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/volcengine/OpenViking/main/docs/images/studio-playground.png" alt="volcengine/OpenViking" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/volcengine/OpenViking" target="_blank">volcengine/OpenViking</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> <span class="sub-tag">#Self-Evolving</span> 
</div>


OpenViking은 AI 에이전트를 위한 자기 진화형 컨텍스트 데이터베이스입니다. 에이전트의 기억, RAG 기반 지식, 그리고 기술을 하나로 통합하여 관리함으로써 에이전트가 스스로 학습하고 발전할 수 있는 기반을 마련합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 298 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/mukul975/Anthropic-Cybersecurity-Skills/main/assets/banner.png" alt="mukul975/Anthropic-Cybersecurity-Skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills" target="_blank">mukul975/Anthropic-Cybersecurity-Skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


이 프로젝트는 AI 에이전트를 위해 817개의 구조화된 사이버 보안 기술 데이터셋을 제공합니다. 이 기술들은 MITRE ATT&CK, NIST 등 6개의 주요 보안 프레임워크와 연계되어 있으며, 20개 이상의 다양한 AI 플랫폼에서 활용될 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 726 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/ai-ethics-is-nobodys-job-now-the-labs-prefer-it-that-way" target="_blank">AI Weekly Issue #523: AI ethics is nobody's job now. The labs prefer it that way.</a></h3>







최첨단 AI 연구소들에서 AI 윤리를 책임지는 조직과 인력이 사라지면서 사실상 책임자가 부재한 상황이 되고 있습니다. 이는 기업들이 의도적으로 책임 구조를 해체하고 있음을 시사하며, 선한 의도만으로는 윤리적 AI 개발을 보장할 수 없다는 퇴사 연구원의 지적이 문제의 심각성을 보여줍니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Agent</code> <code>Eval</code> <code>Multimodal</code> <code>LLM</code> <code>Workflow</code> <code>RAG</code> <code>AI Agent</code> <code>Claude</code> <code>Cursor</code> 
</div>