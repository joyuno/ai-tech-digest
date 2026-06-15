---
layout: post
title: "AI Tech - 2026-06-15"
date: 2026-06-15
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "NVIDIA/SkillSpector"
daily_url: "https://github.com/NVIDIA/SkillSpector"
daily_image: "https://opengraph.githubassets.com/auto/NVIDIA/SkillSpector"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.13681v1/x1.png" alt="EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.13681" target="_blank">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 LLM 에이전트 평가는 대부분 정적인 환경을 가정하지만, 실제 세계는 끊임없이 변화하여 에이전트의 지속적인 적응을 요구합니다. 이러한 한계를 극복하기 위해 'EvoArena'는 소프트웨어 업데이트나 작업 조건 변경 등 동적인 환경 변화를 모델링하여 에이전트의 적응 능력을 측정하는 새로운 벤치마크입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 127</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.13392v1/figures/msa_arch.png" alt="MiniMax Sparse Attention" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.13392" target="_blank">MiniMax Sparse Attention</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


LLM이 수백만 토큰에 달하는 초장문 컨텍스트를 처리하려면 기존 어텐션 방식의 높은 연산 비용이 큰 걸림돌이 됩니다. 이를 해결하기 위해 'MiniMax Sparse Attention'(MSA)은 중요한 데이터 블록만 선별적으로 계산하는 새로운 희소 어텐션 기법을 제안하여, 대규모 배포 환경에서도 초장문 컨텍스트 작업을 효율적으로 수행할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 118</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.09426v2/x2.png" alt="WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.09426" target="_blank">WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Orchestration</span> <span class="sub-tag">#Eval</span> 
</div>


기존 컴퓨터 사용 에이전트(CUA) 벤치마크는 시각적 제어, 커맨드 라인 등 여러 인터페이스를 개별적으로 평가하여 복합적인 장기 작업 능력을 측정하기 어려웠습니다. 'WeaveBench'는 실제 사용자 요청에 기반한 114개의 과제를 통해 여러 인터페이스를 복합적으로 사용해야 하는 에이전트의 능력을 평가하는 새로운 벤치마크입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 97</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.13673v1/x1.png" alt="SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.13673" target="_blank">SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


시각-언어 모델(VLM)은 3D 공간에서 객체의 위치나 관계를 파악하는 공간 추론 능력에 한계가 있으며, 외부 도구를 사용하는 에이전트 역시 도구 호출 인터페이스의 제약을 받습니다. 이 연구는 에이전트가 도구를 호출하는 '액션 인터페이스'의 설계가 공간 추론 능력에 미치는 영향을 분석하고, 이를 개선하기 위한 'SpatialClaw'를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 86</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.13679v1/x4.png" alt="InterleaveThinker: Reinforcing Agentic Interleaved Generation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.13679" target="_blank">InterleaveThinker: Reinforcing Agentic Interleaved Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최신 이미지 생성 모델은 단일 이미지 생성에는 뛰어나지만, 텍스트와 이미지가 순차적으로 결합된 콘텐츠 생성에는 한계를 보입니다. 'InterleaveThinker'는 에이전트가 텍스트 설명과 이미지를 번갈아 생성하는 '인터리브 생성' 능력을 강화하는 새로운 기법으로, 이를 통해 시각적 이야기나 단계별 안내 가이드 제작이 가능해집니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 77</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.13681" target="_blank">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 LLM 에이전트 평가는 대부분 정적인 환경을 가정하지만 실제 세계는 끊임없이 변화합니다. 'EvoArena'는 소프트웨어 업데이트와 같이 동적으로 변하는 환경 속에서 에이전트가 얼마나 효과적으로 지식과 기술을 업데이트하며 적응하는지 평가하는 새로운 벤치마크입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Jundong Xu, Qingchuan Li, Jiaying Wu</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.13673" target="_blank">SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


3D 공간 추론 능력은 시각-언어 모델(VLM)에게 여전히 어려운 과제이며, 도구를 사용하는 에이전트의 성능은 액션 인터페이스 설계에 의해 제한됩니다. 'SpatialClaw'는 에이전트가 공간 추론을 위해 도구를 호출하고 사용하는 방식, 즉 액션 인터페이스의 설계를 재고하여 개방형 공간 추론 능력을 향상시키는 방법을 연구합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Seokju Cho, Ryo Hachiuma, Abhishek Badki</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.13679" target="_blank">InterleaveThinker: Reinforcing Agentic Interleaved Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최신 이미지 생성 모델은 단일 이미지 생성에는 뛰어나지만, 텍스트와 이미지가 번갈아 나오는 '인터리브 생성'은 잘하지 못합니다. 'InterleaveThinker'는 시각적 스토리텔링이나 가이드에 필수적인 이 기능을 강화하기 위해, 통합 멀티모달 모델(UMM)의 인터리브 생성 능력을 향상시키는 새로운 방법을 제안합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Dian Zheng, Harry Lee, Manyuan Zhang</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://github.com/iptv-org/iptv/raw/master/.readme/preview.png" alt="iptv-org/iptv" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/iptv-org/iptv" target="_blank">iptv-org/iptv</a></h3>







전 세계에서 공개적으로 이용 가능한 IPTV 채널들을 모아놓은 컬렉션입니다. 이 프로젝트를 통해 다양한 국가의 TV 방송을 인터넷으로 시청할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1528 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/chatwoot/chatwoot" alt="chatwoot/chatwoot" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/chatwoot/chatwoot" target="_blank">chatwoot/chatwoot</a></h3>







Chatwoot은 라이브 채팅, 이메일 지원 등을 통합한 오픈소스 고객 지원 플랫폼입니다. Intercom이나 Zendesk와 같은 상용 서비스를 대체할 수 있는 강력한 옴니채널 기능을 제공하여 고객과의 소통을 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 400 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/NVIDIA/SkillSpector" alt="NVIDIA/SkillSpector" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/NVIDIA/SkillSpector" target="_blank">NVIDIA/SkillSpector</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



NVIDIA가 개발한 SkillSpector는 AI 에이전트의 '스킬'에 대한 보안 스캐너입니다. 이 도구는 AI 에이전트가 수행하는 작업 속의 취약점, 악성 패턴, 잠재적 보안 위험을 탐지하여 안전성을 강화합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 964 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/GorvGoyl/Clone-Wars/main/img/og.png" alt="GorvGoyl/Clone-Wars" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/GorvGoyl/Clone-Wars" target="_blank">GorvGoyl/Clone-Wars</a></h3>







유명 웹사이트 100개 이상을 복제한 오픈소스 클론 프로젝트들을 모아놓은 저장소입니다. 에어비앤비, 아마존, 넷플릭스 등 인기 서비스의 클론 코드와 데모, 사용된 기술 스택까지 확인할 수 있어 개발 학습에 유용합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 269 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/shiyu-coder/Kronos/master/figures/logo.png" alt="shiyu-coder/Kronos" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/shiyu-coder/Kronos" target="_blank">shiyu-coder/Kronos</a></h3>







Kronos는 금융 시장의 언어를 이해하기 위해 특별히 설계된 파운데이션 모델입니다. 이 모델은 복잡한 금융 데이터와 시장 동향을 언어적으로 분석하고 예측하는 데 사용될 수 있는 강력한 AI 기술입니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 244 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Eval</code> <code>Vision</code> <code>Multimodal</code> <code>AI Agent</code> 
</div>