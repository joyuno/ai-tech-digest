---
layout: post
title: "daily_stock_analysis — LLM 기반 멀티마켓 주식 분석 자동화 도구"
date: 2026-11-12
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "ZhuLinsen/daily_stock_analysis"
daily_url: "https://github.com/ZhuLinsen/daily_stock_analysis"
daily_image: "https://raw.githubusercontent.com/ZhuLinsen/daily_stock_analysis/main/docs/assets/modelflare_banner_zh.png"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.14210" target="_blank">Tree-Ising: Repairing Language Models with Bit-Level Ising Edits</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최근 LLM 에이전트가 모델의 가중치를 직접 수정해 오류를 바로잡는 가중치 공간 프로그래밍 연구가 주목받고 있습니다. 본 논문에서는 언어 모델의 반복 추론 루프 결함을 BF16 가중치 기반의 희소 이산 최적화 문제로 재구성하는 Tree-Ising 방식을 제안합니다. 이를 통해 대규모 연산이나 반복적인 에이전트 상호작용 없이도 비트 수준에서 모델의 결함을 정밀하게 복구할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 77</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.14033v1/3_case_gallery.png" alt="Few-Step Streaming Video Generation via Condition Shifting" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.14033" target="_blank">Few-Step Streaming Video Generation via Condition Shifting</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


스트리밍 비디오 생성의 비용을 줄이기 위해 적은 단계로 영상을 생성하는 효율적인 프레임워크를 제안합니다. 기존 증류 기법은 별도의 네트워크가 필요해 메모리와 연산 부담이 컸지만, 본 방식은 생성기 내부에서 조건 이동을 활용해 분포의 속도장을 직접 추정합니다. 그 결과 추가 네트워크 없이도 효율적인 연산으로 고품질의 실시간 비디오 생성이 가능해집니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 67</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.12885" target="_blank">World In-Context Learning for Agentic Robot Manipulation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



기존의 로봇 조작 정책은 학습된 환경에 과도하게 결속되어 새로운 환경에 적응하기 어렵다는 한계가 있었습니다. 연구진은 로봇 에이전트가 문맥 속에서 학습하는 본질이 시각적 형태가 아닌 작업 순서와 객체의 역할 등 의미 정보라는 점에 주목했습니다. 이를 바탕으로 서로 다른 환경에서 축적된 경험을 새로운 조작 작업으로 유연하게 전이하는 월드 인컨텍스트 학습을 구현했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 65</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.14320v1/fig01-teaser.png" alt="Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.14320" target="_blank">Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



외부 메모리는 LLM 에이전트가 과거의 경험에서 교훈을 얻도록 돕지만, 잘못된 교훈을 맹신하거나 오적용하여 오히려 성능이 떨어지는 문제를 유발하기도 합니다. 이는 과거 작업의 구체적인 맥락과 근거 없이 단순한 성공 및 실패 결과만을 바탕으로 교훈을 도출하기 때문입니다. 본 연구는 메모리에 명확한 증거를 연계하는 방식을 도입하여 메모리로 인한 성능 저하를 방지하고 의사결정의 신뢰도를 높였습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 57</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.11995v1/qvg_intro.png" alt="Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.11995" target="_blank">Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


최신 LLM 에이전트가 실제 AI 인프라를 장기적인 관점에서 자율적으로 최적화할 수 있는지 검증하는 벤치마크인 Infrathon을 구축했습니다. 6개 모델을 대상으로 1만 시간 이상의 GPU 연산을 투입해 장시간 평가를 진행한 결과, 최적화 진행 시간에 따라 모델 간의 성능 순위가 크게 변화함을 발견했습니다. 특히 대다수 실험에서 후반부 탐색을 통해 추가적인 성능 향상을 달성하여 장기적인 인프라 최적화 평가의 필요성을 확인했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 35</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.14488" target="_blank">Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> 
</div>


기억 증강 비전-언어-행동(VLA) 정책 모델들은 종종 사건 중심이 아닌 일정 시간 간격으로 프레임을 수집하여 기억을 채우는 한계가 있습니다. 이로 인해 로봇이 작업을 멈추거나 의미 없는 동작을 할 때도 단순 시간 경과에 의존하여 대기와 실제 작업을 제대로 구분하지 못합니다. 본 연구는 이러한 시간적 지름길 현상을 지적하며 기존 로봇 정책의 기억 메커니즘이 가진 취약점을 규명합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Chubin Zhang, Bo An</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.14516" target="_blank">TorchCurves: Differentiable Parametric Curves</a></h3>







TorchCurves는 벡터 매개변수 곡선을 학습 가능한 요소로 다루는 파이토치 기반 라이브러리입니다. B-스플라인과 르장드르 다항식 기저를 활용해 곡선의 입력값과 계수 모두에 대한 미분 연산을 지원합니다. 이를 통해 곡선 파라미터를 딥러닝 모델과 함께 직접 최적화하거나 다른 신경망을 통해 유연하게 생성할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Alex Shtoff</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.14496" target="_blank">RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Embedding</span> <span class="sub-tag">#Eval</span> 
</div>


RS-JEPA는 레이더(SAR)와 광학 등 서로 다른 센서로 촬영된 원격 탐사 영상 간의 이미지 검색을 지원하는 경량화된 공동 임베딩 예측 프레임워크입니다. 기존 방식들이 픽셀 세부 사항 재구성에 집착하거나 지나치게 거대한 트랜스포머 모델에 의존하던 문제를 해결했습니다. 라벨이 없는 환경에서도 이종 센서 간의 공통 의미 공간을 효율적으로 학습하여 검색 정확도를 높입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/ZhuLinsen/daily_stock_analysis/main/docs/assets/modelflare_banner_zh.png" alt="ZhuLinsen/daily_stock_analysis" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/ZhuLinsen/daily_stock_analysis" target="_blank">ZhuLinsen/daily_stock_analysis</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



LLM을 활용해 다중 시장의 주식 데이터를 종합적으로 분석하는 지능형 시스템입니다. 실시간 뉴스와 다양한 시세 정보를 바탕으로 의사결정 대시보드와 자동 알림을 제공하며, 추가 비용 없이 정기 실행이 가능합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 278 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/shadcn/improve" alt="shadcn/improve" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/shadcn/improve" target="_blank">shadcn/improve</a></h3>







고성능 모델을 사용해 코드베이스를 감사하고 실행 계획을 세운 뒤, 이를 저렴한 모델이 수행하도록 유도하는 도구입니다. 모델별 역량과 비용을 최적화하여 경제적이면서도 효과적인 코드 개선 워크플로를 구축할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 361 today</span> 

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


AI 코딩 에이전트가 프로덕션 수준의 작업을 수행할 수 있도록 돕는 엔지니어링 기술 모음집입니다. 실제 개발 환경에서 신뢰도 높은 코드를 작성하고 복잡한 문제를 해결할 수 있는 실용적인 방법론을 제시합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 787 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/vercel-labs/agent-browser" alt="vercel-labs/agent-browser" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/vercel-labs/agent-browser" target="_blank">vercel-labs/agent-browser</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



AI 에이전트를 위해 개발된 브라우저 자동화 CLI 도구입니다. 에이전트가 웹 브라우저와 원활하게 상호작용하며 복잡한 웹 기반 작업을 스스로 탐색하고 실행할 수 있도록 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 708 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/homeassistant-ai/ha-mcp/master/docs/img/demo.webp" alt="homeassistant-ai/ha-mcp" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/homeassistant-ai/ha-mcp" target="_blank">homeassistant-ai/ha-mcp</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#MCP</span> 
</div>


Claude나 ChatGPT 같은 AI 어시스턴트를 Home Assistant와 연결해 주는 프로젝트입니다. 자연어 대화를 통해 스마트홈 기기를 손쉽게 제어하고 맞춤형 자동화 환경을 편리하게 설정할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 645 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Distillation</code> <code>Eval</code> <code>Vision</code> <code>Transformer</code> <code>Retrieval</code> <code>AI Coding</code> <code>AI Agent</code> <code>GPT</code> 
</div>