---
layout: post
title: "AI Tech - 2026-06-14"
date: 2026-06-14
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "chatwoot/chatwoot"
daily_url: "https://github.com/chatwoot/chatwoot"
daily_image: "https://opengraph.githubassets.com/auto/chatwoot/chatwoot"
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


현재 LLM 에이전트 평가는 대부분 정적인 환경에서 이루어지지만, 실제 환경은 계속 변화하여 에이전트의 지속적인 적응이 필요합니다. 이 문제를 해결하기 위해 'EvoArena'라는 새로운 벤치마크를 제안하며, 이는 소프트웨어 업데이트와 같은 환경 변화에 LLM 에이전트가 얼마나 잘 적응하고 기억을 발전시키는지 평가합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 118</span> 


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


수백만 토큰에 달하는 초장문 컨텍스트를 처리하기에는 기존 어텐션 메커니즘의 연산 비용이 너무 높다는 문제가 있습니다. 'MiniMax Sparse Attention(MSA)'은 Grouped Query Attention(GQA)을 기반으로 중요한 키-값 블록만 선택적으로 계산하는 새로운 블록 단위 희소 어텐션 방식으로, 이러한 문제를 해결하여 대규모 배포를 가능하게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 102</span> 


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


기존 컴퓨터 사용 에이전트(CUA) 벤치마크는 시각적 제어, 커맨드 라인 등 개별 인터페이스의 성능만 평가하여 여러 인터페이스를 오가는 복잡한 장기 작업을 측정하기 어려웠습니다. 'WeaveBench'는 실제 사용자 요청에 기반한 114개의 장기 과제를 포함하는 새로운 벤치마크로, 여러 인터페이스를 복합적으로 사용해야 하는 에이전트의 능력을 종합적으로 평가합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 94</span> 


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


시각언어모델(VLM)은 3D 공간에서 객체의 위치나 관계를 파악하는 공간 추론 능력에 어려움을 겪습니다. 이 연구는 VLM에 특화된 인식 모듈을 도구처럼 결합할 때, 그 도구를 호출하는 '액션 인터페이스'의 설계 방식이 에이전트의 공간 추론 능력에 어떤 영향을 미치는지 탐구합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 80</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.08063v1/x1.png" alt="Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.08063" target="_blank">Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Alignment</span> 
</div>


멀티모달 대형 언어 모델(MLLM)은 시각적 입력이 손상되면 성능이 크게 저하되며, 기존의 강건성 향상 방법들은 한계가 명확했습니다. 이 연구는 'MLLM이 손상된 시각적 콘텐츠를 스스로 복구하여 강건한 이해 능력을 확보할 수 있는가?'라는 근본적인 질문을 던지고 그 가능성을 탐구합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 74</span> 


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


기존 LLM 에이전트 평가는 대부분 정적인 환경에서 이루어져 현실 세계의 역동성을 반영하지 못하는 한계가 있었습니다. 이를 해결하고자 'EvoArena'는 소프트웨어 업데이트처럼 지속적으로 변화하는 환경에 에이전트가 얼마나 잘 적응하고 지식과 기술을 발전시키는지 평가하는 새로운 벤치마크를 제안합니다.

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


시각-언어 모델(VLM)은 3D 공간에서 객체의 위치나 관계를 파악하는 공간 추론 능력에 어려움을 겪습니다. 'SpatialClaw'는 도구를 활용하는 에이전트의 성능이 도구를 호출하는 '액션 인터페이스' 설계에 크게 좌우된다는 점에 주목하여, 개방형 공간 추론 능력을 향상시키기 위한 새로운 인터페이스 설계 방식을 연구합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Seokju Cho, Ryo Hachiuma, Abhishek Badki</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.13679" target="_blank">InterleaveThinker: Reinforcing Agentic Interleaved Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최신 이미지 생성 모델은 단일 이미지 생성에는 뛰어나지만, 텍스트와 이미지가 번갈아 나타나는 '인터리브 생성(interleaved generation)' 작업에는 한계를 보입니다. 'InterleaveThinker'는 시각적 서사나 가이드라인처럼 여러 단계에 걸쳐 텍스트와 이미지를 함께 생성해야 하는 복합적인 작업에서 통합 멀티모달 모델(UMM)의 성능을 강화하는 새로운 방법을 제시합니다.

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







전 세계에서 공개적으로 이용 가능한 IPTV 채널들을 모아놓은 컬렉션입니다. 이 프로젝트를 통해 다양한 국가의 TV 방송을 인터넷으로 시청할 수 있는 링크를 얻을 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 650 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://addyosmani.com/assets/images/addys-agent-skills.jpg" alt="addyosmani/agent-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/addyosmani/agent-skills" target="_blank">addyosmani/agent-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


AI 코딩 에이전트가 실제 상용 수준의 엔지니어링 작업을 수행하기 위해 갖춰야 할 기술들을 정리한 자료입니다. 이 가이드는 AI 에이전트의 개발 및 평가에 필요한 실질적인 역량과 기준을 제시합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1507 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/chatwoot/chatwoot" alt="chatwoot/chatwoot" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/chatwoot/chatwoot" target="_blank">chatwoot/chatwoot</a></h3>







라이브 채팅, 이메일 지원 등을 통합한 오픈소스 옴니채널 고객 지원 플랫폼입니다. 인터콤(Intercom)이나 젠데스크(Zendesk) 같은 상용 솔루션을 대체하여 고객과의 소통을 효율적으로 관리할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 86 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/apple/container/main/docs/assets/landing-movie.gif" alt="apple/container" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/apple/container" target="_blank">apple/container</a></h3>







Mac 환경에서 경량 가상 머신을 사용해 리눅스 컨테이너를 생성하고 실행할 수 있도록 Apple이 개발한 도구입니다. Swift로 작성되었으며 Apple Silicon에 최적화되어 효율적인 컨테이너 활용을 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1471 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://agentsview.io/screenshots/dashboard.png" alt="kenn-io/agentsview" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/kenn-io/agentsview" target="_blank">kenn-io/agentsview</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


코딩 AI 에이전트의 세션 활동을 분석하고 인사이트를 제공하는 로컬 우선(local-first) 분석 도구입니다. Claude Code, Codex 등 20개 이상의 에이전트를 지원하며, 기존 도구보다 월등히 빠른 성능을 자랑합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 187 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Eval</code> <code>Vision</code> <code>Alignment</code> <code>Multimodal</code> <code>AI Coding</code> <code>Claude</code> <code>Claude Code</code> 
</div>