---
layout: post
title: "NVIDIA/OpenShell, 자율 AI 에이전트를 위한 안전한 private 런타임"
date: 2026-09-30
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "NVIDIA/OpenShell"
daily_url: "https://github.com/NVIDIA/OpenShell"
daily_image: "https://raw.githubusercontent.com/NVIDIA/OpenShell/main/docs/brand/assets/openshell-banner-light.png"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.32577" target="_blank">Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



코드 에이전트를 위한 강화학습은 주로 테스트 통과 여부로 보상을 제공하여 코드 품질 차이를 반영하지 못하는 한계가 있습니다. 이 논문은 GAG라는 새로운 기법을 제안하여, 불필요한 코드가 포함된 해법보다 깔끔하고 명확한 구현을 선호하도록 학습 신호를 개선합니다. 이를 통해 에이전트는 단순히 테스트를 통과하는 것을 넘어 더 우수한 품질의 코드를 생성하도록 유도됩니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 108</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.33325v1/main2.png" alt="VisionHOPE: Visual Backbones as Self-Modifying Learning Systems" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.33325" target="_blank">VisionHOPE: Visual Backbones as Self-Modifying Learning Systems</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#SSM</span> 
</div>


기존의 비전 백본 모델들은 입력 이미지에 따라 연산을 조절하지만, 그 적응 방식 자체는 훈련 중에 고정됩니다. 이 논문은 추론 과정에서 스스로의 처리 규칙을 수정하는 새로운 비전 백본 VisionHOPE를 제안하여, 각 이미지에 최적화된 방식으로 스스로를 개선하는 자기-수정 학습 시스템을 구현합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 107</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.35457v1/mm_transition.png" alt="How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.35457" target="_blank">How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



대부분의 멀티모달 LLM은 사전 훈련된 시각 인코더에 의존하지만, 인코더 없이 원본 픽셀로부터 직접 시각 정보를 학습하는 모델에 대한 연구가 진행되고 있습니다. 이 논문은 인코더-프리 모델의 스케일링 법칙을 분석하여, 구조는 단순하지만 기존 인코더 기반 모델과 동일한 성능을 달성하기 위해서는 훨씬 더 많은 컴퓨팅 자원과 데이터가 필요하다는 점을 밝혀냈습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 55</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.33378v1/figure1.png" alt="Recursive Harness Distillation across Agents for Robot Manipulation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.33378" target="_blank">Recursive Harness Distillation across Agents for Robot Manipulation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> <span class="sub-tag">#Distillation</span> 
</div>


로봇 조작을 위한 VLA 모델은 범용적이지만 실패 상황에 대처하고 행동을 수정하는 데 어려움을 겪습니다. 이 논문은 '재귀적 하네스 증류' 기법을 제안하여, 유능한 에이전트가 실패를 극복하며 얻은 경험을 다른 에이전트들이 재사용할 수 있는 가이드라인으로 축적합니다. 이를 통해 여러 에이전트에 걸쳐 문제 해결 경험이 공유되고 누적되어 전반적인 로봇 조작 능력이 향상됩니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 30</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.33848" target="_blank">QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Long Context</span> 
</div>


수 시간에 걸쳐 수백만 토큰을 처리하는 초장기 태스크에서 LLM 에이전트를 강화학습으로 훈련시키는 것은 GPU 유휴 시간과 데이터 비효율성 문제를 야기합니다. 이 논문은 이러한 문제를 해결하기 위해 데이터 수집과 훈련을 분리하고 방대한 궤적 데이터를 효율적으로 재사용 및 압축하는 탄력적인 강화학습 프레임워크 QwenGyre를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 27</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.36246" target="_blank">Learning from Teacher Continuations at Student States</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#SFT</span> <span class="sub-tag">#Distillation</span> <span class="sub-tag">#RAG</span> 
</div>


OLIVE는 학생 모델의 결과물을 교사 모델이 실시간으로 보완하고, 이를 학생이 다시 학습하는 온라인 증류 기법입니다. 이 방식은 학생 모델이 생성한 텍스트의 다음 내용을 교사 모델이 이어 작성해주면, 학생 모델이 그 결과를 바탕으로 업데이트되는 구조로 기존 오프라인 미세조정(SFT)의 한계를 극복합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Haojin Wang, Dylan Zhang, Huaibo Chen</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.36219" target="_blank">LeRF: Learning Reference Coordinate Frames for Perspective Taking Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


시각-언어 모델(VLM)은 특정 인물의 시점처럼 주어진 관점에서 공간을 추론하는 능력이 부족하여, 종종 카메라 시점으로만 상황을 판단합니다. LeRF는 이러한 한계를 극복하기 위해 '기준 좌표계'를 학습하는 새로운 프레임워크를 제안하며, 이를 통해 모델은 다양한 관점을 명확히 이해하고 지정된 시점에서 공간 관계를 정확하게 해석할 수 있게 됩니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Bang Xiao, Wenqi Jia, Ozgur Kara</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.36218" target="_blank">CineSubBench: Evaluating LLMs on Long-Form Narrative and Cultural Understanding from Multilingual Movie Subtitles</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


CineSubBench는 다국어 영화 자막을 이용해 LLM의 장편 서사 및 문화 이해도를 평가하는 새로운 벤치마크입니다. 영화는 긴 이야기 흐름과 문화적 맥락의 이해가 필수적임에도 기존 LLM 평가에서는 주목받지 못했으며, 이 벤치마크는 시간 순서로 구성된 자막 데이터를 통해 모델이 복잡한 내러티브를 얼마나 깊이 있게 파악하는지 측정합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Mir Tafseer Nayeem, Susmoy Chakraborty, Davood Rafiei</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/chipmunk" target="_blank">9인조 다람쥐 아이돌을 데뷔시켰습니다</a></h3>







토스는 사용자들이 개설 후 잘 확인하지 않는 적금 상품에 대한 관심을 높이고자 '다람쥐 아이돌 키우기'라는 게이미피케이션 요소를 도입했습니다. 이 기능은 자칫 지루할 수 있는 저축 과정에 재미를 더해, 사용자들이 매일 꾸준히 저축에 참여하도록 성공적으로 유도했습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/NVIDIA/OpenShell/main/docs/brand/assets/openshell-banner-light.png" alt="NVIDIA/OpenShell" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/NVIDIA/OpenShell" target="_blank">NVIDIA/OpenShell</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



OpenShell은 자율적으로 작동하는 AI 에이전트를 위한 안전하고 프라이버시를 보장하는 런타임 환경입니다. 이 프로젝트는 AI 에이전트가 독립적으로 작업을 수행할 수 있는 기반을 제공하여 보안과 신뢰성을 높입니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 990 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-github-banner.png" alt="vectorize-io/hindsight" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/vectorize-io/hindsight" target="_blank">vectorize-io/hindsight</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



Hindsight는 학습 능력을 갖춘 혁신적인 AI 에이전트 메모리 시스템입니다. 이를 통해 에이전트는 과거의 경험과 상호작용을 기억하고 학습하여 미래의 의사결정 능력을 향상시킬 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2575 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/paperclipai/paperclip/master/doc/assets/banner.jpg" alt="paperclipai/paperclip" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/paperclipai/paperclip" target="_blank">paperclipai/paperclip</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



Paperclip은 업무 환경에서 다양한 AI 에이전트를 관리하고 활용하기 위한 오픈소스 애플리케이션입니다. 사용자는 이 도구를 통해 여러 에이전트를 효율적으로 제어하고 작업을 자동화할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2458 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://dl.dbxio.com/assets/readme-hero-20260925.png" alt="t8y2/dbx" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/t8y2/dbx" target="_blank">t8y2/dbx</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#MCP</span> 
</div>


dbx는 25MB의 가벼운 용량을 자랑하는 크로스플랫폼 데이터베이스 클라이언트입니다. MySQL, PostgreSQL, MongoDB 등 100개 이상의 데이터베이스를 지원하며, 내장 AI 비서와 데스크톱, CLI, Docker 등 다양한 환경을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 232 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/mvschwarz/openrig/main/assets/readme/openrig-agents-working.gif" alt="mvschwarz/openrig" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mvschwarz/openrig" target="_blank">mvschwarz/openrig</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


openrig는 여러 AI 에이전트를 함께 구동하기 위한 멀티 에이전트 하네스(harness)입니다. 이 시스템은 Claude Code와 Codex 같은 서로 다른 모델을 하나의 통합된 시스템처럼 연동하여 복잡한 작업을 수행할 수 있게 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 737 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Agent</code> <code>Vision</code> <code>LLM</code> <code>Distillation</code> <code>1M tokens</code> <code>Fine-tuning</code> <code>RAG</code> <code>Eval</code> <code>AI Agent</code> <code>MCP</code> 
</div>