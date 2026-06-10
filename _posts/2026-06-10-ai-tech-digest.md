---
layout: post
title: "AI Tech - 2026-06-10"
date: 2026-06-10
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "aaif-goose/goose"
daily_url: "https://github.com/aaif-goose/goose"
daily_image: "https://opengraph.githubassets.com/auto/aaif-goose/goose"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.05405v1/x1.png" alt="Agents' Last Exam" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.05405" target="_blank">Agents' Last Exam</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


현재 AI 시스템의 벤치마크는 실제 경제적 가치를 지닌 업무 수행 능력을 제대로 평가하지 못하는 한계가 있습니다. 이 논문은 이러한 격차를 해소하기 위해, 길고 복잡하며 경제적으로 의미 있는 실제 업무를 기반으로 AI 에이전트를 평가하는 새로운 벤치마크 'ALE(Agents' Last Exam)'를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 65</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.06087v1/figures/motivation_1.png" alt="LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.06087" target="_blank">LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#LoRA</span> 
</div>


LLM 에이전트가 매번 프롬프트에 텍스트 스킬을 주입하는 방식은 컨텍스트 용량을 많이 차지하고 비효율적입니다. 'LatentSkill'은 이러한 텍스트 스킬을 모델의 가중치 공간에 저장하는 LoRA 어댑터로 변환하여, 프롬프트 오버헤드 없이 모듈식으로 스킬을 활용할 수 있게 하는 새로운 프레임워크입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 50</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.09079v1/x1.png" alt="FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.09079" target="_blank">FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Long Context</span> 
</div>


긴 컨텍스트를 처리하는 LLM은 전체 KV 캐시를 GPU 메모리에 유지해야 하므로 심각한 메모리 병목 현상이 발생합니다. 이 문제를 해결하기 위해 'Lookahead Sparse Attention(LSA)' 기술은 미래에 필요한 컨텍스트를 예측하여 쿼리에 핵심적인 KV 청크만 GPU 메모리에 보존하는 새로운 추론 방식을 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 42</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.09659v1/x1.png" alt="End-to-End Context Compression at Scale" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.09659" target="_blank">End-to-End Context Compression at Scale</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Inference Engine</span> 
</div>


긴 컨텍스트를 사용하는 언어 모델 추론은 컨텍스트 길이에 따라 KV 캐시가 증가하여 메모리 병목 현상을 겪습니다. 이 논문은 기존 압축 기술의 단점을 보완하여, 긴 컨텍스트를 효율적으로 압축하면서도 모델 품질 저하가 적고 실제 서비스 환경과 호환되는 새로운 엔드투엔드 압축 방식을 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 17</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.09826v1/x1.png" alt="OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.09826" target="_blank">OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#Eval</span> 
</div>


기존의 VLM(Vision-Language Model) 게임 에이전트 벤치마크는 단일 시도 점수만 제공하거나 다양한 종류의 에이전트를 동일한 기준으로 평가하기 어려웠습니다. 'OmniGameArena'는 언리얼 엔진 5 기반의 새로운 통합 벤치마크로, 여러 에이전트를 동일한 환경에서 테스트하고 시간에 따른 성능 향상까지 측정할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 16</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.09380" target="_blank">Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  



대규모 언어 모델(LLM)의 추론 능력을 향상시키는 강화학습(RLVR)은 여러 결과물이 동일한 보상을 받을 경우 학습 신호를 제공하지 못하는 한계가 있습니다. 'Reasoning Arena'는 이러한 상황에서 토너먼트 방식으로 결과물들을 직접 비교하여, 검증 가능한 보상만으로는 부족했던 추론 품질의 미세한 차이를 포착하고 더 정교한 학습 신호를 생성하는 새로운 기법입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Han Zhou, Adam X. Yang, Laurence Aitchison</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.09570" target="_blank">UXBench: Benchmarking User Experience in AI Assistants</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Alignment</span> <span class="sub-tag">#Eval</span> 
</div>


AI 어시스턴트의 성능 평가는 일반적인 모델 역량을 넘어 실제 사용자 경험(UX)을 측정하는 것이 중요해지고 있습니다. 'UXBench'는 실제 사용자 피드백 데이터를 기반으로 구축된 최초의 사용자 중심 벤치마크로, AI 어시스턴트의 선호도 정렬 및 대화 생성 능력을 보다 현실적으로 평가하는 기준을 제시합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Mengze Hong, Xia Zeng, Zeyang Lei</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.09585" target="_blank">Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#CoT</span> 
</div>


기존 멀티모달 모델이 텍스트나 텍스트와 이미지를 혼합하여 추론하는 것과 달리, 이 연구는 이미지만을 추론의 매개체로 사용하는 '광학적 추론(Optical Reasoning)'이라는 새로운 개념을 제안합니다. 이는 텍스트 설명 없이 오직 연속된 이미지 자체로 사고의 과정을 표현하고 언어 및 멀티모달 과제를 해결하는 혁신적인 방식을 모색합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yutong Bian, Dongjie Cheng, Heming Xia</span>
</div>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/tam-connect-2025" target="_blank">빠르게 움직이는 조직에서, TAM은 어떻게 문제를 해결할까?</a></h3>







토스와 카카오페이의 Technical Account Manager(TAM)들이 만나 빠르게 변화하는 조직에서 겪는 어려움과 해결책을 논의했습니다. 이 글은 고객과 개발팀 사이의 가교 역할을 하는 TAM의 중요성을 강조하며, 이들의 생생한 경험과 문제 해결 노하우를 공유합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://toss.tech/article/history-of-face-recognition-facepay" target="_blank">얼굴 인식의 역사와 페이스페이의 미래</a></h3>







이 글은 기계가 사람의 얼굴을 인식하기까지 지난 60년간의 얼굴 인식 기술 발전 과정을 되짚어 봅니다. 초기 연구 단계부터 현재의 페이스페이와 같은 상용 서비스에 이르기까지, 기술의 역사적 흐름과 미래 전망을 함께 조명합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> 토스</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/mvanhorn/last30days-skill" alt="mvanhorn/last30days-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



레딧, X, 유튜브 등 다양한 웹 소스에서 특정 주제에 대한 정보를 리서치하는 AI 에이전트 스킬입니다. 수집한 정보를 종합하여 근거에 기반한 요약문을 생성해 줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 3191 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/header.png" alt="RyanCodrai/turbovec" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/RyanCodrai/turbovec" target="_blank">RyanCodrai/turbovec</a></h3>







TurboQuant 기술을 기반으로 구축된 새로운 벡터 인덱스 라이브러리입니다. Rust로 작성되었으며 파이썬 바인딩을 제공하여 파이썬 환경에서도 쉽게 사용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1801 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/opencv/opencv" alt="opencv/opencv" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/opencv/opencv" target="_blank">opencv/opencv</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



실시간 이미지 처리 등 다양한 기능을 제공하는 대표적인 오픈소스 컴퓨터 비전 라이브러리입니다. 오랜 역사와 방대한 커뮤니티를 바탕으로 학계와 산업계 전반에서 폭넓게 활용되고 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 102 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/aaif-goose/goose" alt="aaif-goose/goose" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/aaif-goose/goose" target="_blank">aaif-goose/goose</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



단순한 코드 제안을 넘어, 코드의 설치, 실행, 수정, 테스트까지 수행하는 오픈소스 AI 에이전트입니다. 확장 가능한 구조로 설계되었으며, 사용자가 원하는 어떤 LLM과도 연동하여 활용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 489 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Andyyyy64/whichllm/main/assets/demo.gif" alt="Andyyyy64/whichllm" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Andyyyy64/whichllm" target="_blank">Andyyyy64/whichllm</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


사용자의 하드웨어에서 실제로 가장 잘 실행되고 최고의 성능을 내는 로컬 LLM을 찾아주는 도구입니다. 단순한 파라미터 수가 아닌, 최신 실제 벤치마크 결과를 기반으로 순위를 매겨주며 단일 명령어로 즉시 실행할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 633 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/musks-175-trillion-bet-isnt-a-rocket-company" target="_blank">AI Weekly Issue #501: Musk's $1.75 Trillion Bet Isn't a Rocket Company</a></h3>







일론 머스크의 스페이스X가 역대 최대 규모인 1.75조 달러로 상장하지만, 이 거대한 가치의 핵심은 로켓이 아닌 AI 사업에 있습니다. 작년에 64억 달러의 손실을 기록했음에도, 100만 개의 데이터센터 위성을 쏘아 올리려는 AI 계획이 바로 머스크의 진짜 승부수인 셈입니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>AI Agent</code> <code>Eval</code> <code>LLM</code> <code>LoRA</code> <code>Agent</code> <code>Prompt</code> <code>Long Context</code> <code>Inference</code> <code>Vision</code> <code>Alignment</code> 
</div>