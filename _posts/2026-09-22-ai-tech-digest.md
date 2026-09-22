---
layout: post
title: "OpenStock — 비싼 주식 시장 플랫폼의 오픈소스 대안"
date: 2026-09-22
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "Open-Dev-Society/OpenStock"
daily_url: "https://github.com/Open-Dev-Society/OpenStock"
daily_image: "https://raw.githubusercontent.com/Open-Dev-Society/OpenStock/main/public/assets/images/dashboard.png"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.19969v1/figures/teaser_a.png" alt="DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.19969" target="_blank">DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


긴 컨텍스트를 처리하는 모델은 연산량이 많고 KV 캐시가 커서 배포 비용이 높다는 문제가 있습니다. 이 연구는 KV 캐시 압축 기술의 한계를 뛰어넘는 DeepSeek-V4.1-Flash를 제안하여, 연산, 저장, 대역폭 비용을 크게 절감하는 새로운 해결책을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 146</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.18323v1/fig1.png" alt="Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.18323" target="_blank">Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Alignment</span> <span class="sub-tag">#Eval</span> 
</div>


텍스트, 이미지, 영상, 오디오를 통합적으로 처리하는 최신 옴니모달 모델(Omni-Modal Model)은 물리 세계에 대한 추론 능력을 향상시킬 수 있을까요? 이 연구는 MiniMax-H3 모델을 중심으로, 다중 모드 입력이 모델의 세계 이해도에 미치는 영향을 분석하고 새로운 평가 패러다임을 탐구합니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> gulucaptain/MiniMax-H3-Reason · ★ 24</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 116</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2609.20511v1/fig/baseline_opd.png" alt="When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2609.20511" target="_blank">When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


온폴리시 증류(on-policy distillation) 과정에서 학생 모델이 지나치게 긴 답변을 생성하는 '길이 팽창' 현상이 발생합니다. 이 연구는 학생 모델과 교사 모델이 서로 다른 종료 토큰(EOS token)에 정지 확률을 부여하는 불일치가 이 문제의 주요 원인임을 밝혀냈습니다. 이러한 불일치는 학생 모델이 문장 생성을 적절히 멈추지 못하게 만듭니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 96</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.21346" target="_blank">IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#MoE</span> 
</div>


기존 MoE(Mixture-of-Experts) 모델은 전문가 참여도, 연산량, 메모리 비용을 독립적으로 제어하기 어려웠습니다. IntBMoE는 블록 레벨 조건부 통합을 통해 모든 전문가가 추론에 참여하면서도 연산 및 메모리 비용은 낮게 유지하는 새로운 아키텍처를 제안하여 모델의 용량과 효율성을 동시에 극대화합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 90</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2609.22068" target="_blank">CodeMidas: Scaling Agentic Coding RL Environments from Code Itself</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> 
</div>


강화학습(RL) 기반 코딩 에이전트를 훈련시키려면 다양하고 신뢰할 수 있는 과제가 필요하지만, 기존 방식은 과제 생성에 한계가 있었습니다. CodeMidas는 기존 소스 코드 자체를 활용하여 실행 가능한 RL 환경을 자동으로 생성하는 에이전틱 파이프라인을 제시하여, 훨씬 더 방대하고 다양한 훈련 환경을 구축할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 88</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.22068" target="_blank">CodeMidas: Scaling Agentic Coding RL Environments from Code Itself</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> 
</div>


CodeMidas는 기존 코드베이스의 소스 코드를 직접 활용하여 실행 가능한 강화학습(RL) 환경을 자동으로 생성하는 에이전틱 파이프라인입니다. 이를 통해 기존에 이슈나 커밋에 의존하던 방식의 한계를 넘어, 훨씬 더 방대하고 다양한 코딩 훈련 환경을 구축할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Bowen Ye, Lei Li, Shicheng Li</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.22086" target="_blank">Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



Designer-RSI는 정답이 정해져 있지 않은 전문 그래픽 디자인 작업을 위한 에이전트 프레임워크로, 수많은 도구를 사용하는 모델과 사용자 경험으로부터 디자인 절차를 학습하는 외부 메모리를 결합합니다. 이 시스템은 실제 사용자 트래픽을 통해 재사용 가능한 디자인 기술을 자연어 형태로 축적하고 개선하며 지속적으로 발전합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Hongyang Du, Lan Yan, Christian Flores</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2609.22069" target="_blank">OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


OmniVBench는 다양한 종류의 레퍼런스를 복합적으로 활용해 비디오를 생성하는 '옴니 R2V(omni Reference-to-Video)' 기술을 위한 새로운 벤치마크 및 대규모 데이터셋입니다. 기존 벤치마크의 한계를 넘어, 여러 레퍼런스 요소가 생성된 비디오에 올바르게 반영되고 분리되었는지 종합적으로 평가할 수 있는 새로운 기준을 제시합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Wenxue Li, Peiyan Guan, Haoyang Jiang</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/remittance_transfer" target="_blank">도메인 지식 없는 디자이너가 팀의 기준을 바꾼 방법</a></h3>







전문 분야인 은행 지식이 없던 디자이너가 규제가 많은 금융 도메인에서 팀의 기준을 높인 경험을 공유합니다. 외부인의 신선한 관점이 오히려 기존의 틀을 깨고 문제 해결에 기여하며 팀 전체에 긍정적인 변화를 가져온 과정을 이야기합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/trycua/cua/main/img/card-cua-fleets-wide.gif" alt="trycua/cua" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/trycua/cua" target="_blank">trycua/cua</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


오픈소스 드라이버를 통해 다양한 운영체제에서 컴퓨터 사용을 자동화하고 확장하는 프로젝트입니다. 이 프로젝트는 AI 모델의 훈련, 평가, 데이터 생성을 위한 벤치마크를 제공하여 컴퓨터 제어 기술 발전에 기여합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 609 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Open-Dev-Society/OpenStock/main/public/assets/images/dashboard.png" alt="Open-Dev-Society/OpenStock" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Open-Dev-Society/OpenStock" target="_blank">Open-Dev-Society/OpenStock</a></h3>







고가의 상용 주식 시장 플랫폼을 대체할 수 있는 오픈소스 대안입니다. 실시간 시세 추적, 개인 맞춤형 알림 설정, 상세한 기업 정보 조회 기능을 누구나 영구적으로 무료 사용할 수 있도록 개발되었습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 844 today</span> 

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




  



코딩 작업을 수행하는 AI 에이전트를 위한 장기 기억 솔루션입니다. CLI 환경에서 작동하며, 서로 다른 개발사의 AI 에이전트 간에 작업 내용을 원활하게 인계할 수 있도록 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 167 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/anthropics/financial-services" alt="anthropics/financial-services" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/anthropics/financial-services" target="_blank">anthropics/financial-services</a></h3>







AI 기업 앤트로픽(Anthropic)이 공개한 금융 서비스 관련 프로젝트입니다. 자사의 AI 모델을 활용하여 금융 분야의 특정 문제들을 해결하는 방법을 보여주는 예제나 도구를 포함하고 있을 것으로 예상됩니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 424 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/zhouxiaoka/autoclip/main/docs/images/import-local.jpg" alt="zhouxiaoka/autoclip" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/zhouxiaoka/autoclip" target="_blank">zhouxiaoka/autoclip</a></h3>







AI 기술을 이용해 긴 영상에서 하이라이트 구간을 자동으로 추출하고 편집해주는 도구입니다. 원본 영상을 바탕으로 짧은 클립을 만드는 2차 창작 활동을 더 쉽고 편리하게 만들어 줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 250 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>DeepSeek</code> <code>RAG</code> <code>Agent</code> <code>Multimodal</code> <code>Alignment</code> <code>Eval</code> <code>Llama</code> <code>Distillation</code> <code>MoE</code> 
</div>