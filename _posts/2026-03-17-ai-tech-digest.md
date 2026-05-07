---
layout: post
title: "LMEB — long-horizon memory를 평가하는 새 벤치마크"
date: 2026-03-17
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "LMEB: Long-horizon Memory Embedding Benchmark"
daily_url: "https://arxiv.org/abs/2603.12572"
daily_keywords: ["RAG", "Eval", "Vision", "Benchmark", "Multimodal", "Tool Use", "Agent", "Fine-tuning", "Claude", "Claude Code"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2603.12572.png"
daily_image_kind: "hf_first_page"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12572" target="_blank">LMEB: Long-horizon Memory Embedding Benchmark</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 에이전트의 장기 기억력을 제대로 평가하기 위해 설계된 새로운 벤치마크인 LMEB를 소개하는 논문입니다. 기존의 단순한 문서 검색을 넘어, 파편화되고 문맥에 의존하는 긴 시간의 메모리 정보를 얼마나 잘 검색하는지 정교하게 측정할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.08436" target="_blank">Can Vision-Language Models Solve the Shell Game?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


최신 VLM들이 시각적으로 똑같이 생긴 객체를 시공간의 흐름만으로 추론하고 추적할 수 있는지 테스트하는 VET-Bench를 제안합니다. 실험 결과, 놀랍게도 현재 SOTA 모델들조차 야바위 게임처럼 단순한 추적 문제를 거의 찍기 수준으로밖에 풀지 못한다는 점을 밝혀냈어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12793" target="_blank">Cheers: Decoupling Patch Details from Semantic Representations Enables Unified Multimodal Comprehension and Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


이미지 이해와 생성을 하나의 모델에서 완벽하게 처리할 수 있도록 돕는 통합 멀티모달 모델인 Cheers를 소개합니다. 이미지의 세부적인 패치 정보와 전반적인 의미 정보를 분리해 학습함으로써, 모델의 이해 능력과 이미지 생성 퀄리티를 동시에 크게 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12056" target="_blank">XSkill: Continual Learning from Experience and Skills in Multimodal Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


멀티모달 에이전트가 복잡한 파라미터 업데이트 없이도 스스로 성능을 개선할 수 있는 지속 학습 방법을 제안합니다. 과거의 성공적인 도구 사용 '경험'과 재사용 가능한 '스킬'을 분리해 저장하고 활용함으로써 에이전트의 문제 해결 능력을 한층 더 끌어올려 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.13023" target="_blank">daVinci-Env: Open SWE Environment Synthesis at Scale</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


소프트웨어 엔지니어링(SWE) 에이전트를 훈련시키기 위해 대규모로 구축된 오픈소스 가상 환경 프레임워크입니다. AI가 실제 코드를 수정하고 테스트하며 피드백을 받을 수 있는 투명한 환경을 제공하여, 학계의 연구 진입 장벽을 크게 낮춰줍니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.13224" target="_blank">Visual-ERM: Reward Modeling for Visual Equivalence</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>


차트나 표 같은 시각 데이터를 코드로 변환할 때, 모델이 시각적인 디테일을 더 정확하게 살리도록 돕는 새로운 보상 모델링 기법입니다. 기존 RL 방식들이 놓치기 쉬운 미세한 시각적 차이까지 정교하게 평가하여, 생성된 코드의 시각적 완성도를 한 단계 높일 수 있어요.

<small><i data-lucide="user"></i> Ziyu Liu, Shengyuan Ding, Xinyu Fang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.13089" target="_blank">V-Bridge: Bridging Video Generative Priors to Versatile Few-shot Image Restoration</a></h3>



대규모 비디오 생성 모델이 학습한 풍부한 시각적 사전 지식을 활용하여 손상된 이미지를 복원하는 V-Bridge 프레임워크를 소개합니다. 비디오 모델의 강력한 생성 능력을 소수의 데이터만으로도 다양한 퓨샷(Few-shot) 이미지 복원 작업에 유연하게 적용할 수 있는 점이 돋보입니다.

<small><i data-lucide="user"></i> Shenghe Zheng, Junpeng Jiang, Wenbo Li</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.13033" target="_blank">ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


VLM이 실제 물리적 환경에서 얼마나 정확하게 공간을 인지하고 추론하는지 평가하는 ESPIRE 벤치마크입니다. 로봇 공학에 필요한 시뮬레이션 기반의 공간 추론 테스트를 제공하여 체화된 AI 모델의 실질적인 개발 속도를 높여주는 유용한 도구입니다.

<small><i data-lucide="user"></i> Yanpeng Zhao, Wentao Ding, Hongtao Li</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thedotmack/claude-mem" target="_blank">thedotmack/claude-mem</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


코딩을 하는 동안 Claude AI의 모든 작업 내역을 자동으로 기록하고 요약해 주는 유용한 플러그인입니다. 이렇게 저장된 핵심 문맥을 다음 작업 때 다시 주입해 주어, AI가 이전 상황을 잊지 않고 매끄럽게 코딩을 이어가게 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Crosstalk-Solutions/project-nomad" target="_blank">Crosstalk-Solutions/project-nomad</a></h3>



인터넷이 끊긴 극한의 상황에서도 작동하도록 설계된 독립형 오프라인 생존 컴퓨터 프로젝트입니다. 필수적인 지식 데이터베이스와 유용한 도구, 그리고 AI를 내장하고 있어 언제 어디서든 강력한 오프라인 정보망을 활용할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/abhigyanpatwari/GitNexus" target="_blank">abhigyanpatwari/GitNexus</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


복잡한 서버 설정 없이 웹 브라우저 안에서 바로 작동하는 코드 분석 지식 그래프 도구입니다. GitHub 저장소나 압축 파일을 넣기만 하면 Graph RAG 기반의 AI 에이전트와 대화하며 코드 구조를 쉽고 직관적으로 탐색할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/lightpanda-io/browser" target="_blank">lightpanda-io/browser</a></h3>



AI 에이전트와 웹 자동화 작업을 위해 특별히 가볍고 빠르게 설계된 헤드리스 브라우저입니다. 불필요한 리소스 소모를 크게 줄여, 대규모 웹 스크래핑이나 AI 기반의 브라우저 제어 작업을 훨씬 더 효율적으로 처리할 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/volcengine/OpenViking" target="_blank">volcengine/OpenViking</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


AI 에이전트가 필요로 하는 다양한 기억과 자원, 스킬을 체계적으로 관리해 주는 오픈소스 컨텍스트 데이터베이스입니다. 파일 시스템 구조를 채택하여 에이전트가 필요한 정보를 쉽게 찾고 스스로 진화할 수 있는 강력한 메모리 기반을 제공합니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>RAG</code> <code>Eval</code> <code>Vision</code> <code>Benchmark</code> <code>Multimodal</code> <code>Tool Use</code> <code>Agent</code> <code>Fine-tuning</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

