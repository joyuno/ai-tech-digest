---
layout: post
title: "AI Tech - 2026-06-03"
date: 2026-06-03
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "chopratejas/headroom"
daily_url: "https://github.com/chopratejas/headroom"
daily_image: "https://raw.githubusercontent.com/chopratejas/headroom/main/HeadroomDemo-Fast.gif"
daily_keywords: ["RAG", "MCP"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2605.28556" target="_blank">A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> <span class="sub-tag">#Eval</span> 
</div>


기존 AI 에이전트 벤치마크는 성능 포화 상태에 이르렀지만 새로운 벤치마크 제작은 어렵습니다. 이 논문은 작업 생성 과정을 역으로 진행하는 TASTE 방법론을 제안하여, 더 넓은 범위와 높은 난이도를 가진 벤치마크를 자동으로 생성함으로써 이러한 문제를 해결합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 54</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2606.02373" target="_blank">Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



기존 검색 에이전트는 검색 결정과 상태 관리를 동시에 수행해야 하는 비효율적인 부담이 있었습니다. Harness-1은 상태 관리를 에이전트 외부 환경으로 분리하는 '하네스' 개념을 도입하여, 강화학습이 의미론적 검색 작업에만 집중하도록 만들어 학습 효율과 신뢰성을 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 31</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.29707v1/x1.png" alt="Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.29707" target="_blank">Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  



LLM 추론 속도를 높이는 추측적 디코딩(Speculative Decoding)은 초안 생성의 품질과 비용 사이의 상충 관계라는 한계가 있었습니다. Domino는 인과 모델링과 초안 생성을 분리하는 새로운 프레임워크로, 순차적 오버헤드를 줄이면서도 높은 품질의 초안을 생성하여 LLM 추론 속도를 효과적으로 개선합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 26</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.30501v1/figures/visual_token_ensemble.png" alt="Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.30501" target="_blank">Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


AI 생성 텍스트를 식별하기 위한 워터마킹 기술에 치명적인 취약점이 발견되었습니다. 여러 모델의 출력 확률 분포를 평균 내는 간단한 '선형 앙상블' 기법만으로도 워터마크가 쉽게 제거될 수 있어, 여러 AI 서비스를 사용하는 현실에서 워터마킹이 쉽게 무력화될 수 있음을 시사합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 25</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.24202v2/x1.png" alt="When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.24202" target="_blank">When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> <span class="sub-tag">#Eval</span> 
</div>


여러 LLM 에이전트가 협업하는 워크플로우는 정확도를 높일 수 있지만, 강화학습(RL)을 이용한 공동 훈련은 불안정합니다. 이 연구는 다중 에이전트 워크플로우에 강화학습을 적용하는 것이 언제 효과적인지 탐구하며, 정책 공유 방식과 규모에 따른 성능 변화를 분석하여 안정적인 훈련 조건에 대한 이해를 돕습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 13</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.02564" target="_blank">VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


최신 비디오 생성 모델(VGM)은 시각적 품질은 뛰어나지만 복잡한 규칙을 따르지 못해 비디오 추론 과제에서 논리적 오류를 일으키는 한계가 있습니다. 이 연구는 비전-언어 모델(VLM)을 '교사'로 삼아 생성 과정에서 실시간으로 VGM을 최적화함으로써, 모델이 주어진 규칙을 더 정확하게 따르고 추론 성능을 높이도록 유도합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Junhao Cheng, Liang Hou, Tianxiong Zhong</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.02553" target="_blank">LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> <span class="sub-tag">#Eval</span> 
</div>


기존의 장편 비디오 생성 모델은 시간이 지남에 따라 오류가 누적되고 객체의 일관성이 저하되는 문제를 겪습니다. 이 문제를 해결하기 위해 본 연구는 검색 증강 생성(RAG) 기술을 활용한 'LongLive-RAG' 프레임워크를 제안하며, 과거의 주요 프레임을 참조하여 누적 오류를 수정하고 긴 비디오에서도 인물이나 배경의 일관성을 성공적으로 유지합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Qixin Hu, Shuai Yang, Wei Huang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.02580" target="_blank">Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


'역 그래픽스(Inverse graphics)'는 단일 이미지로부터 편집 가능한 3D 씬을 재구성하는 매우 어려운 문제입니다. 본 연구는 사전 훈련된 비전-언어 모델(VLM)이 이미지를 분석하여 직접 블렌더(Blender) 프로그램을 생성하는 새로운 방식을 제안하며, 이를 통해 별도의 3D 데이터 없이도 2D 이미지를 3D 씬으로 변환할 수 있음을 보여줍니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Guangzhao He, Rundong Luo, Wei-Chiu Ma</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/chopratejas/headroom/main/HeadroomDemo-Fast.gif" alt="chopratejas/headroom" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/chopratejas/headroom" target="_blank">chopratejas/headroom</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> <span class="sub-tag">#MCP</span> 
</div>


이 프로젝트는 LLM에 데이터를 보내기 전에 도구 출력, 로그, 파일 등을 압축하여 토큰 사용량을 획기적으로 줄여주는 도구입니다. 이를 통해 최대 95%의 토큰을 절약하면서도 LLM의 답변 품질은 동일하게 유지할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1265 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/affaan-m/ECC/main/assets/hero.png" alt="affaan-m/ECC" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/affaan-m/ECC" target="_blank">affaan-m/ECC</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


AI 에이전트의 성능 최적화를 위한 시스템으로, 에이전트 하네스(agent harness)라고 불립니다. 이 시스템은 Claude Code, Codex와 같은 코드 생성 AI에 기술, 본능, 메모리, 보안 등의 고도화된 기능을 부여하여 성능을 향상시킵니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1533 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://ml4t.s3.amazonaws.com/assets/cover_toc_gh.png" alt="stefan-jansen/machine-learning-for-trading" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/stefan-jansen/machine-learning-for-trading" target="_blank">stefan-jansen/machine-learning-for-trading</a></h3>







'알고리즘 트레이딩을 위한 머신러닝(Machine Learning for Algorithmic Trading)' 2판 서적에 수록된 공식 코드 저장소입니다. 책에서 다루는 다양한 머신러닝 기반 트레이딩 전략을 독자들이 직접 실습하고 구현해볼 수 있도록 모든 예제 코드를 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 574 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/jamwithai/production-agentic-rag-course/main/static/mother_of_ai_project_rag_architecture.gif" alt="jamwithai/production-agentic-rag-course" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/jamwithai/production-agentic-rag-course" target="_blank">jamwithai/production-agentic-rag-course</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


실제 서비스 환경에 적용 가능한 '에이전틱 RAG(Agentic RAG)' 시스템 구축 방법을 다루는 강의 자료입니다. 이 강의는 검색 증강 생성(RAG) 기술에 AI 에이전트 개념을 결합하여, 복잡한 태스크를 자율적으로 수행하는 프로덕션 수준의 시스템을 개발하는 노하우를 공유합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 30 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/supermemoryai/supermemory" alt="supermemoryai/supermemory" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/supermemoryai/supermemory" target="_blank">supermemoryai/supermemory</a></h3>







AI 시대를 위해 설계된 초고속의 확장 가능한 메모리 엔진 및 애플리케이션입니다. 이 프로젝트는 AI 애플리케이션이 정보를 빠르고 효율적으로 저장하고 검색할 수 있도록 지원하는 '메모리 API'를 제공하는 것을 목표로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 680 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>RAG</code> <code>Agent</code> <code>Benchmark</code> <code>LLM</code> <code>Inference</code> <code>Eval</code> <code>Vision</code> <code>MCP</code> <code>Claude</code> <code>Cursor</code> 
</div>