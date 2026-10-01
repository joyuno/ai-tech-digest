---
layout: post
title: "context-mode — AI 코딩 에이전트의 context window 최적화"
date: 2026-10-01
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "mksglu/context-mode"
daily_url: "https://github.com/mksglu/context-mode"
daily_image: "https://img.youtube.com/vi/QUHrntlfPo4/maxresdefault.jpg"
daily_keywords: ["Coding Agent", "MCP", "AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.32722v1/banner.png" alt="Scaling Properties of Same-Family On-Policy Distillation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.32722" target="_blank">Scaling Properties of Same-Family On-Policy Distillation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


강화학습으로 LLM의 추론 능력을 향상시킬 때, 모델 크기에 따라 성능이 어떻게 전이되는지 연구했습니다. 온폴리시 증류(OPD) 기법을 사용한 결과, 학습 초기에는 학생 모델의 성능이 교사 모델의 성능과 학습 데이터 양에 비례하여 예측 가능하게 향상되는 '유용 전이' 구간이 일관되게 나타났습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 213</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.31847v1/figures/omni-io-teaser.png" alt="Omni-IO Skills: Harnessing Your Agent Omni-Native" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.31847" target="_blank">Omni-IO Skills: Harnessing Your Agent Omni-Native</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


범용 에이전트가 텍스트, 이미지, 오디오 등 다양한 데이터를 통합적으로 처리하기 어려운 문제를 해결하기 위해 'Omni-IO Skills'라는 플러그인 방식의 프레임워크를 제안합니다. 이 프레임워크는 통합된 입출력 형식과 스킬 레지스트리를 통해 여러 전문 도구와 모델을 조율하여, 에이전트가 재학습 없이도 다양한 데이터 형식을 원활하게 다룰 수 있도록 지원합니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> any2any-mllm/Omni-IO-Skill · ★ 20</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 159</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.32607v1/fig5_opxev_compact.png" alt="VoxMem: Benchmarking Multimodal Memory in Large Audio Language Models" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.32607" target="_blank">VoxMem: Benchmarking Multimodal Memory in Large Audio Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


음성 대화 시스템은 대화 내용뿐만 아니라 화자, 억양 등 오디오에만 존재하는 정보까지 기억해야 하지만, 이를 평가할 방법이 부족했습니다. 이 문제를 해결하기 위해 텍스트만으로는 알 수 없는 음성 고유의 정보를 활용하여 오디오 언어 모델의 멀티모달 기억 능력을 종합적으로 평가하는 새로운 벤치마크 'VoxMem'을 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 125</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.36322" target="_blank">Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  



긴 컨텍스트를 처리하는 LLM의 메모리 사용량을 줄이는 '청크 KV-캐시 압축' 기술에서 주기적인 취약점이 발견되었습니다. 이 기술을 사용하면 토큰이 압축 윈도우 내 어느 위치에 있느냐에 따라 정보 검색 능력이 달라져, 동일한 정보라도 특정 위치에서는 접근이 어려워지는 문제가 발생합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 97</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.37226" target="_blank">Follow the Entities: A Corpus Map for Agentic Search</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



LLM 에이전트가 여러 문서에 흩어져 있는 정보를 연결하여 답을 찾는 것은 어려운 과제입니다. 이 연구는 검색 전에 문서들 속 개체(인물, 장소, 프로젝트 등)를 식별하고 연결하여 '코퍼스 맵'을 구축하는 방법을 제안하며, 이를 통해 에이전트가 전체 문서를 반복적으로 검색하는 대신 개체 간의 연결을 따라 효율적으로 정보를 탐색할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 73</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.38155" target="_blank">Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies</a></h3>







긴 비디오 속 특정 객체에 대한 질문에 답하기 위해, 여러 장면에 흩어진 동일 객체의 정보를 연결하는 것은 매우 중요합니다. 이 연구는 단순히 시간 순서로 사건을 나열하는 것을 넘어, 특정 객체의 전체 활동 기록인 '실체 기반 전기(Grounded Entity Biographies)'를 구축하여 비디오 내용 이해도를 높이는 새로운 접근법을 제안합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Hui Ren, Lei Fan, Henry Pao</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.38157" target="_blank">EmoRES-TTS: Residual-Enhanced Vector Steering for Emotional Speech Generation</a></h3>







감정 표현 TTS 모델이 원하는 감정을 정확히 생성하지 못하는 문제를 해결하기 위해, 추가 학습 없이 기존 모델의 내부 표현을 수정하는 '벡터 스티어링' 기법을 연구합니다. 이 논문은 기존 방식보다 더 정교하게 감정을 제어하는 '잔차 강화 벡터 스티어링(EmoRES-TTS)' 기술을 제안하여, 별도의 학습 비용 없이 감정 표현의 신뢰도를 향상시킵니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Kuan-Po Huang, Haohe Liu, Puyuan Peng</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.38170" target="_blank">Adversarial Training for Pixel Diffusion</a></h3>







픽셀 확산 모델은 이미지를 직접 생성하지만, 자연스러운 이미지의 미세한 질감을 제대로 표현하지 못하는 한계가 있습니다. 이 연구는 사전 학습된 모델에 적대적 학습(adversarial learning)을 후처리 방식으로 적용하여, 모델 구조 변경 없이도 더 현실적이고 세밀한 통계적 특성을 가진 이미지를 생성하도록 개선하는 방법을 제시합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Xin Lin, Zhifei Zhang, Yuqian Zhou</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/53545" target="_blank">추천 후보는 많을수록 좋을까? TopK를 최적화해 전환율을 높인 방법</a></h3>







추천 시스템에서 사용자에게 보여줄 후보군의 수(TopK)가 많을수록 좋다는 통념과 달리, 서비스의 목표에 맞는 최적의 개수가 존재합니다. 토스는 직관이 아닌 데이터 기반의 최적화 실험을 통해 최적의 TopK 값을 찾아냈으며, 이를 통해 실제 서비스의 전환율을 성공적으로 높인 과정을 공유합니다.

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




  



OpenShell은 NVIDIA가 공개한 자율 AI 에이전트를 위한 런타임 환경입니다. 이 프로젝트는 AI 에이전트가 안전하고 독립적으로 작동할 수 있도록 프라이버시를 보장하는 실행 환경을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1281 today</span> 

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


openrig는 여러 AI 모델을 하나의 시스템처럼 통합하여 구동하는 멀티 에이전트 프레임워크입니다. 이 프로젝트는 Claude Code와 Codex 같은 서로 다른 코딩 AI를 함께 활용하여 더욱 강력한 개발 환경을 구축할 수 있게 해줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 624 today</span> 

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


context-mode는 AI 코딩 에이전트의 컨텍스트 창 사용을 최적화하는 도구입니다. 도구 출력 결과를 샌드박스 환경에서 처리하여 컨텍스트를 98%까지 절감하고, 세션 메모리를 유지하며 17개 플랫폼 간의 라우팅을 관리합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 90 today</span> 

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




  



ponytail은 AI 에이전트가 마치 '게으른 시니어 개발자'처럼 효율적으로 사고하도록 돕는 프로젝트입니다. 불필요한 코드를 작성하기보다 가장 간단하고 효과적인 해결책을 찾도록 유도하여, '작성하지 않은 코드가 최고의 코드'라는 개발 철학을 AI에 적용합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 743 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/harry0703/MoneyPrinterTurbo/main/docs/webui.jpg" alt="harry0703/MoneyPrinterTurbo" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/harry0703/MoneyPrinterTurbo" target="_blank">harry0703/MoneyPrinterTurbo</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



MoneyPrinterTurbo는 AI와 자동화된 워크플로우를 이용해 고화질 단편 영상을 제작하는 도구입니다. 사용자가 원하는 주제나 키워드를 입력하기만 하면, AI가 영상 생성 과정을 자동으로 처리하여 손쉽게 콘텐츠를 만들 수 있도록 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 431 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Distillation</code> <code>Vision</code> <code>RAG</code> <code>Agent</code> <code>Multimodal</code> <code>Benchmark</code> <code>Inference</code> <code>AI Agent</code> <code>Claude</code> 
</div>