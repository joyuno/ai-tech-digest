---
layout: post
title: "NVIDIA, AI 에이전트 스킬·플러그인 다계층 평가 프레임워크 공개"
date: 2026-11-19
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "NVIDIA/SkillEvaluator"
daily_url: "https://github.com/NVIDIA/SkillEvaluator"
daily_image: "https://opengraph.githubassets.com/auto/NVIDIA/SkillEvaluator"
daily_keywords: ["Eval"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.22115v1/xing4-285b-architecture.png" alt="TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.22115" target="_blank">TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


Xing 4는 중국산 Ascend NPU와 자체 프레임워크 환경에 맞춰 개발된 대규모 언어 모델 시리즈로, 기존 TeleChat 계열을 크게 확장했습니다. 모델 아키텍처 최적화와 대규모 사전 학습은 물론, 복잡한 추론과 에이전트 역량을 강화하기 위한 사후 학습 엔지니어링 설계를 집대성했습니다. 이를 통해 희소 활성화와 추측 디코딩 등을 적용하여 제한된 연산 자원 내에서 모델 성능을 극대화하는 방안을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 151</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.17621v1/figures/ascendforge-architecture.png" alt="AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.17621" target="_blank">AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


AscendGYM은 Ascend NPU 환경에서 대규모 언어 모델의 학습과 추론을 돕는 비용 인식 기반 커널 최적화 벤치마크입니다. 기존 벤치마크와 달리 AI 에이전트가 실제 워크로드 환경을 반영한 입력 조건에서 기존 커널을 얼마나 효과적으로 튜닝하는지 평가하는 데 초점을 맞춥니다. 총 3단계 난이도로 구성된 48개의 커널을 제공하여 현실적인 최적화 성능을 정밀하게 측정할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 91</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.22055" target="_blank">Weight-Space Programming Doesn't Need Transformers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


이 논문은 LLM이 경사 하강법 없이 직접 대상 신경망의 가중치를 작성하는 가중치 공간 프로그래밍에서 트랜스포머 아키텍처의 필요성을 재검토합니다. 트랜스포머는 기존 하드웨어와 역전파 학습에 최적화된 구조이므로, 가중치를 직접 생성하는 새로운 패러다임에서는 다른 구조가 더 적합할 수 있음을 실험적으로 증명합니다. 연구진은 최소한의 예시만으로 LLM이 비트랜스포머 구조의 가중치를 효과적으로 생성할 수 있음을 보여줍니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 51</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.19800" target="_blank">Multi-Branch Transformer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


Multi-Branch Transformer(MBT)는 트랜스포머 모델을 깊거나 넓게 쌓는 기존 확장 방식 대신 블록을 병렬로 분기하여 구성하는 새로운 아키텍처입니다. 입력 데이터를 공유 레이어를 거쳐 독립적인 병렬 블록에서 동시에 처리한 뒤 다시 융합하는 구조를 채택하여 계산 효율을 높였습니다. 동일한 학습 연산량 조건에서 기존 단일 경로 모델보다 뛰어난 확장성과 성능을 보여주며 새로운 모델 설계 가능성을 열었습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 45</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.17048v2/aura-v2-overall.png" alt="Beyond Answering: Learning to Speak First and Act in Streaming Video" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.17048" target="_blank">Beyond Answering: Learning to Speak First and Act in Streaming Video</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  



AURA 2.0은 사용자의 질문을 기다리기만 하던 기존 방식에서 벗어나 실시간 영상 스트림을 이해하고 먼저 대화를 시작할 수 있는 비디오 LLM입니다. 영상의 시각적 변화 속에서 의미 있는 대화 주제를 스스로 식별하고 적절한 타이밍에 개입하는 모델 주도 대화 기능을 핵심 기술로 도입했습니다. 이를 통해 상황을 선제적으로 파악하고 먼저 반응하며 행동할 수 있는 진정한 능동형 AI 어시스턴트를 구현했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 35</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.24102" target="_blank">IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#GUI Agent</span> 
</div>


오픈 가중치 GUI 에이전트는 특정 시각적 트리거가 나타날 때만 오작동하는 백도어 공격에 취약하여 보안상 큰 위험을 초래합니다. 본 연구는 지시어 대신 비정상적인 화면 영역이 동작을 가로채는지 분석하여 추론 시점에 백도어를 감지하는 IDEA 기법을 제안합니다. 이를 통해 기존 탐지 기법의 한계를 극복하고 에이전트의 단계별 안전성을 효과적으로 검증할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zhizhuo Kou, Sizai Hou, Jian Yang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.24075" target="_blank">Recurrent Domain Incremental Adaptation of Time-Series Foundation Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  



시계열 파운데이션 모델은 변화하는 운영 조건에 적응하면서도 이전에 학습한 지식을 유지해야 하는 도메인 증분 적응의 어려움을 겪고 있습니다. 특히 추론 시점에 환경 조건을 알 수 없거나 소량의 레이블 데이터만 주어지는 상황에서도 기존 성능의 저하를 막아야 합니다. 연구진은 이러한 적응 난제의 기하학적 구조를 파악하여 시계열 모델의 효과적인 환경 적응 방안을 제시합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Sachith Abeywickrama, Peiliang Gong, Emadeldeen Eldele</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.24654" target="_blank">CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



대규모 언어 모델을 특정 목표에 맞춰 미세 조정할 때 기존의 범용 역량이 손상되지 않도록 보존하는 일은 핵심적인 과제입니다. 본 연구는 매개변수 업데이트 과정에 역량 보존 제약을 직접 반영하는 확장형 프레임워크인 CurvDelta를 제안합니다. 모델 주변의 국소적 기하학 구조를 분석해 저곡률 공간을 구축함으로써, 일반 성능 저하 없이 정밀한 학습과 언러닝을 안정적으로 구현합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zeguan Xiao, Zhuocheng Liang, Yun Chen</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/mvanhorn/last30days-skill/main/media/pr-assets/last30days-ad.gif" alt="mvanhorn/last30days-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



레딧, 엑스, 유튜브, 해커뉴스 등 다양한 웹 플랫폼에서 특정 주제를 자동으로 심층 조사하는 AI 에이전트 스킬입니다. 흩어져 있는 최신 데이터를 수집하고 교차 검증하여 신뢰할 수 있는 핵심 요약본을 도출합니다. 사용자는 여러 커뮤니티를 일일이 탐색하지 않고도 최신 트렌드와 여론을 빠르게 파악할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1059 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/NVIDIA/SkillEvaluator" alt="NVIDIA/SkillEvaluator" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/NVIDIA/SkillEvaluator" target="_blank">NVIDIA/SkillEvaluator</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


AI 에이전트 스킬과 플러그인의 품질 및 동작 영향을 다각도로 검증하는 엔비디아의 다계층 평가 프레임워크입니다. 기능 간 의미적 중복 탐지, 합성 평가 데이터셋 생성, 품질 검증 관문 등의 체계적인 기능을 제공합니다. 이를 통해 새로운 스킬이 에이전트의 실제 행동에 미치는 영향을 정밀하게 분석하고 최적화할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 312 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/google-research/paper-orchestra/main/assets/overview.png" alt="google-research/paper-orchestra" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/google-research/paper-orchestra" target="_blank">google-research/paper-orchestra</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> 
</div>


구글 리서치에서 공개한 AI 연구 논문 자동 작성을 위한 멀티 에이전트 프레임워크입니다. 여러 특화 에이전트가 긴밀하게 협업하여 아이디어 구체화부터 문헌 정리, 초안 작성까지 복잡한 논문 집필 과정을 조율합니다. 연구자가 학술 연구 결과를 체계적으로 문서화하는 데 드는 시간과 비용을 획기적으로 줄여줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1524 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/google-labs-code/stitch-skills" alt="google-labs-code/stitch-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/google-labs-code/stitch-skills" target="_blank">google-labs-code/stitch-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#MCP</span> <span class="sub-tag">#AI Coding</span> 
</div>


Stitch MCP 서버와 유기적으로 연동되도록 설계된 공식 에이전트 스킬 라이브러리입니다. 에이전트 스킬 표준 규격을 준수하여 Cursor, Claude Code, Gemini CLI 등 다양한 AI 코딩 도구와 뛰어난 호환성을 제공합니다. 개발자는 이를 통해 여러 개발 환경에 일관된 워크플로와 맞춤형 기능을 간편하게 확장할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 365 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/appwrite/appwrite" alt="appwrite/appwrite" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/appwrite/appwrite" target="_blank">appwrite/appwrite</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


AI 에이전트와 소프트웨어 개발자를 위해 광범위한 기능을 제공하는 오픈소스 백엔드 클라우드 플랫폼입니다. 인증, 데이터베이스, 스토리지, 서버리스 함수 및 WAF 등 서비스 운영에 필수적인 핵심 인프라를 완벽히 지원합니다. 복잡한 서버 인프라 구축 부담을 덜어주어 고성능 애플리케이션 개발에만 온전히 집중할 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 232 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Agent</code> <code>LLM</code> <code>Inference</code> <code>Benchmark</code> <code>Transformer</code> <code>Prompt</code> <code>AI Agent</code> <code>Eval</code> <code>Claude</code> 
</div>