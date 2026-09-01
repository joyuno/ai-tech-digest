---
layout: post
title: "minimind — 2시간 만에 64M LLM을 처음부터 학습"
date: 2026-09-01
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "jingyaogong/minimind"
daily_url: "https://github.com/jingyaogong/minimind"
daily_image: "https://raw.githubusercontent.com/jingyaogong/minimind/master/images/logo.png"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.25518v1/fig_verification_loop.png" alt="Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.25518" target="_blank">Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#World Model</span> 
</div>


월드 모델을 확장하기 위해 단순히 더 많은 비디오 데이터를 사용하는 것은 비효율적이며, 명확한 보상 신호를 제공하는 재귀적인 데이터 엔진이 필요합니다. 이 논문은 에이전트를 활용한 게임 개발이 실행 가능한 환경을 통해 검증 가능한 궤적 데이터를 생성하므로, 월드 모델 확장을 위한 효과적인 데이터 엔진이 될 수 있다고 주장합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 185</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.27345v2/one_plausible_future.png" alt="PAWBench: How Far Are We from Probabilistically Aligned World Modeling?" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.27345" target="_blank">PAWBench: How Far Are We from Probabilistically Aligned World Modeling?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Alignment</span> <span class="sub-tag">#Eval</span> 
</div>


최신 월드 모델은 단일한 결과가 아닌, 발생 가능한 모든 결과의 분포를 재현해야 하며, 이를 '확률적 정렬(probabilistic alignment)'이라 합니다. 이 논문은 기존 평가 방식의 한계를 지적하며, 모델이 결과의 분포를 제대로 예측하는지 측정하는 새로운 벤치마크 PAWBench를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 138</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.27456v1/HKCase.png" alt="UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.27456" target="_blank">UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



멀티모달 대규모 언어 모델(MLLM)이 정적인 거리 풍경을 이해하는 것을 넘어, 실제 도시 환경에서 연속적인 행동을 수행할 수 있는지에 대한 연구입니다. 이를 위해 홍콩의 3D 지리공간 데이터로 구축된 실제 규모의 샌드박스 'UrbanGround'를 제안하여, MLLM 에이전트가 지역적 인식을 신뢰할 수 있는 행동으로 전환하는 능력을 시험합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 106</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.28281v1/looparena_harness.png" alt="LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.28281" target="_blank">LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#Eval</span> 
</div>


코딩 에이전트를 관리하기 위해 자동화된 루프를 설계하는 '루프 엔지니어링'에서 루프를 운영하는 컨트롤러 모델의 성능은 매우 중요합니다. 이 논문은 최종 결과만으로는 컨트롤러의 의사결정 과정을 평가하기 어렵다는 점을 지적하며, 다양한 모델이 루프 컨트롤러로서 얼마나 효과적인지 벤치마킹하는 'LoopArena'를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 89</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.27448v1/intro.png" alt="TTPO: Test-Time Policy Optimization" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.27448" target="_blank">TTPO: Test-Time Policy Optimization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> <span class="sub-tag">#RAG</span> 
</div>


기존의 강화학습 기반 후속 학습 방법은 정답 레이블이 필요하여 테스트 시점에는 적용하기 어렵다는 한계가 있습니다. 이 논문은 다수결 투표의 비대칭적 실패 모드에 착안하여, 정답 레이블 없이도 테스트 시점에 안전하게 모델 정책을 최적화하는 새로운 기법 TTPO(Test-Time Policy Optimization)를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 72</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.28460" target="_blank">LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in Video Generation</a></h3>







LayerRecall은 긴 비디오를 생성할 때 시간이 지나도 일관성을 유지하는 새로운 메모리 라우팅 기술입니다. 이 기술은 비디오 모델의 각 레이어가 현재, 최근, 과거 등 각기 다른 시간대의 정보를 선호한다는 점에 착안하여, 필요한 맥락 정보를 선별적으로 전달함으로써 장기적인 일관성 문제를 해결합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yixuan Ding, Jiahao Kong, Wei Huang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.28476" target="_blank">ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



ContextPilot은 LLM 에이전트가 장기적인 작업을 수행할 때 필요한 정보를 효율적으로 관리하도록 훈련시키는 기술입니다. 기존 방식은 정보를 검색, 삭제, 요약하는 제한된 도구만 사용했지만, ContextPilot은 세분화된 강화학습(RL)을 통해 에이전트가 스스로 작업 맥락을 주도적으로 편집하고 관리하는 능력을 향상시킵니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zhuoshi Pan, Qizhi Pei, Junru Lu</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.28478" target="_blank">Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



이 연구는 LLM이 잘 알려지지 않은 사실에 대해 여러 상충하는 정보가 존재할 때 이를 어떻게 처리하는지 탐구하며, '코끼리와 맹인' 우화처럼 편협한 시각을 갖는지 분석합니다. 이를 평가하기 위해 웹상의 다양한 의견 불일치를 바탕으로 구축한 'ElephantBench'라는 새로운 벤치마크를 도입하여, LLM이 단일 정답을 넘어 여러 관점을 얼마나 잘 이해하는지 측정합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zhuoshi Pan, Junru Lu, Yan Qian</span>
</div>

</div>



---


## <i data-lucide="shirt"></i> 무신사 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://techblog.musinsa.com/%ED%86%B5%ED%95%A9%EC%9E%84%EB%B2%A0%EB%94%A9%EC%9C%BC%EB%A1%9C-%EA%B0%9C%EC%9D%B8%ED%99%94-%ED%91%B8%EC%8B%9C-ctr-21-3-%EB%A5%BC-%EB%A7%8C%EB%93%A0-%EA%B3%BC%EC%A0%95-08bd63623aff?source=rss----f107b03c406e---4" target="_blank">통합임베딩으로 개인화 푸시 CTR +21.3%를 만든 과정</a></h3>







무신사의 개인화 시스템은 여러 모델이 사용자를 일관되게 이해해야 효과적인 의사결정을 내릴 수 있습니다. 이를 위해 사용자의 취향과 관심사를 공통으로 표현하는 '통합 임베딩'을 구축했으며, 그 결과 개인화 푸시 메시지의 클릭률(CTR)을 21.3% 향상시키는 성과를 거두었습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Seungmo Oh</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/THU-MAIC/OpenMAIC/main/assets/logo-horizontal.png" alt="THU-MAIC/OpenMAIC" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/THU-MAIC/OpenMAIC" target="_blank">THU-MAIC/OpenMAIC</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> 
</div>


OpenMAIC는 단 한 번의 클릭으로 몰입감 있는 다중 에이전트 학습 경험을 제공하는 오픈소스 프로젝트입니다. 사용자는 이 대화형 교실 환경에서 여러 AI 에이전트와 상호작용하며 효과적으로 학습할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2824 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/tt-a1i/archify/main/docs/assets/archify-readme-hero.png" alt="tt-a1i/archify" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/tt-a1i/archify" target="_blank">tt-a1i/archify</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



Archify는 AI 에이전트가 아름답고 검증 가능한 아키텍처, 워크플로우, 시퀀스 다이어그램 등을 생성하도록 돕는 기술입니다. 이 도구를 사용하면 애니메이션 효과가 포함된 단일 HTML 파일로 다이어그램을 만들고 선명한 이미지로 내보낼 수 있어 문서화 작업이 매우 편리해집니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 3991 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/K-Dense-AI/scientific-agent-skills" alt="K-Dense-AI/scientific-agent-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/K-Dense-AI/scientific-agent-skills" target="_blank">K-Dense-AI/scientific-agent-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


이 프로젝트는 모든 AI 에이전트를 'AI 과학자'로 변신시켜주는 과학 분야 최고의 에이전트 스킬 라이브러리입니다. 생물학, 화학, 의학 등 다양한 분야를 아우르는 165개 이상의 검증된 기술과 100개 이상의 과학 데이터베이스를 즉시 활용하여 복잡한 과학 연구를 자동화하고 가속화합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1980 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/jingyaogong/minimind/master/images/logo.png" alt="jingyaogong/minimind" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/jingyaogong/minimind" target="_blank">jingyaogong/minimind</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



Minimind는 단 2시간 만에 6,400만 개 파라미터 규모의 LLM을 처음부터 학습시킬 수 있는 획기적인 프로젝트입니다. 이를 통해 개발자들은 비교적 적은 자원으로도 자신만의 소형 언어 모델을 빠르고 효율적으로 구축하는 경험을 할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 495 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Osmantic/ODS/main/ods/docs/images/osmantic-lockup.png" alt="Osmantic/ODS" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Osmantic/ODS" target="_blank">Osmantic/ODS</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


ODS는 개인용 PC, Mac, 또는 리눅스 컴퓨터를 강력한 AI 서버로 변환해주는 오픈소스 프로젝트입니다. 이 도구를 설치하면 LLM 추론, 챗봇 UI, 음성 인식, RAG, 이미지 생성 등 다양한 최신 AI 기능을 자신의 컴퓨터에서 직접 구동할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 77 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Alignment</code> <code>Eval</code> <code>Prompt</code> <code>Reasoning</code> <code>Distillation</code> <code>RAG</code> <code>Claude</code> <code>AI Agent</code> 
</div>