---
layout: post
title: "claude-mem — Claude 세션 컨텍스트 자동 보존"
date: 2026-02-02
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "huggingface"
daily_title: "We Got Claude to Build CUDA Kernels and teach open models!"
daily_url: "https://huggingface.co/blog/upskill"
daily_keywords: ["LLM", "Fine-tuning", "Agent", "Reasoning", "Distillation", "Alignment", "RAG", "Prompt", "Llama", "Eval"]
daily_image: "https://huggingface.co/blog/assets/upskill/thumbnail.png"
daily_image_kind: "og_image"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.21558" target="_blank">ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


도구를 사용하는 LLM 에이전트를 학습시킬 때 발생하는 수동 개입과 불안정성 문제를 해결하기 위해 ASTRA라는 프레임워크가 등장했습니다. 이 방식은 에이전트의 경로 생성과 강화 학습 과정을 완전히 자동화하여, 복잡한 다단계 의사결정 성능을 안정적으로 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.23143" target="_blank">THINKSAFE: Self-Generated Safety Alignment for Reasoning Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


강력한 추론 능력을 가진 LRM이 유해한 프롬프트까지 따르는 안전성 문제를 해결하기 위해 ThinkSafe가 제안되었습니다. 외부 모델에 의존하지 않고 스스로 안전 데이터를 생성하여 정렬함으로써, 모델 고유의 추론 능력을 해치지 않으면서도 안전성을 확보합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22628" target="_blank">TTCS: Test-Time Curriculum Synthesis for Self-Evolving</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


테스트 시점의 데이터로 LLM을 적응시키는 Test-Time Training의 한계를 극복하기 위해 TTCS 프레임워크가 개발되었습니다. 어려운 추론 문제에 대해 커리큘럼 방식을 적용하여 스스로 학습 난이도를 조절하며, 적은 데이터로도 안정적으로 성능을 높일 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22046" target="_blank">PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction</a></h3>



단안 이미지 시퀀스에서 실시간 3D 재구성을 할 때 렌더링 품질과 정확한 기하학적 구조를 모두 잡기 위한 PLANING 프레임워크입니다. 기하학적 기본 요소와 Neural Gaussian을 결합한 하이브리드 표현 방식을 사용하여, 두 요소를 분리해 효율적으로 모델링하고 최적화합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22157" target="_blank">Discovering Hidden Gems in Model Repositories</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


수많은 모델이 공개되어 있지만 대다수는 유명한 몇몇 모델만 사용하는 현실에서, 연구진이 2,000개 이상의 모델을 분석해 '숨겨진 보석(Hidden Gems)'을 찾아냈습니다. 유명하지 않은 파인튜닝 모델 중에서도 Llama-3.1 같은 인기 모델보다 성능이 뛰어난 사례가 많다는 것을 입증했습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control" target="_blank">Introducing NVIDIA Cosmos Policy for Advanced Robot Control</a></h3>



NVIDIA가 로봇 제어 기술을 한 단계 더 발전시키기 위해 Cosmos Policy를 새롭게 공개했습니다. 이는 복잡한 로봇 동작과 정밀한 제어 작업을 수행할 수 있도록 설계된 고급 AI 모델 및 프레임워크로 보입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/daggr" target="_blank">Introducing Daggr: Chain apps programmatically, inspect visually</a></h3>



AI 애플리케이션의 체인을 프로그래밍 방식으로 구성하면서도 시각적으로 검사할 수 있는 Daggr라는 도구가 소개되었습니다. 복잡한 앱 흐름을 코드로 짜고 눈으로 쉽게 확인하며 디버깅할 수 있어 개발 생산성을 높여줍니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/upskill" target="_blank">We Got Claude to Build CUDA Kernels and teach open models!</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Claude를 활용해 고성능 병렬 처리를 위한 CUDA 커널 코드를 작성하고, 이를 통해 오픈 소스 모델을 가르친 흥미로운 사례입니다. LLM이 로우 레벨 최적화 코딩까지 수행하여 다른 모델의 성능 향상에 기여할 수 있음을 보여줍니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="shirt"></i> 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%EC%9D%B4%EB%B2%88-%EB%8B%AC%EB%8F%84-%EB%B0%A4%EC%83%98-%EC%A0%95%EC%82%B0%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%8D%94-%EC%9D%B4%EC%83%81-%EB%B0%A4%EC%83%98%ED%95%98%EC%A7%80-%EC%95%8A%EC%95%84%EB%8F%84-%EB%90%A9%EB%8B%88%EB%8B%A4-%EC%9A%B4%EC%98%81%ED%8E%B8-4f09ae3bdf5d?source=rss----f107b03c406e---4" target="_blank">“이번 달도 밤샘 정산입니다.” — 더 이상 밤샘하지 않아도 됩니다 (운영편)</a></h3>



무신사가 정산 시스템을 개편하며 개발자들이 밤샘 업무에서 해방된 실제 운영 노하우를 공유했습니다. 리스크를 줄이기 위해 기능이 아닌 데이터를 기준으로 단계적으로 오픈하는 전략을 취했으며, 실제 운영 데이터를 미리 수집해 엣지 케이스를 사전에 해결했습니다.

<small><i data-lucide="user"></i> 박성민(Seongmin)</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thedotmack/claude-mem" target="_blank">thedotmack/claude-mem</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


코딩 세션 동안 Claude가 수행한 모든 작업을 자동으로 기록하고 AI로 압축하여 기억하는 플러그인입니다. 이후 세션에서 관련된 맥락을 다시 주입해주므로, 긴 프로젝트에서도 연속성 있는 코딩 지원을 받을 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ThePrimeagen/99" target="_blank">ThePrimeagen/99</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


Neovim 사용자를 위해 최적화된 AI 에이전트 도구입니다. 가볍고 빠른 Neovim 환경의 장점을 살리면서도 AI의 도움을 받아 효율적인 코딩이 가능하도록 설계되었습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/netbirdio/netbird" target="_blank">netbirdio/netbird</a></h3>



WireGuard 기반으로 장치들을 안전하게 연결해주는 오버레이 네트워크 도구입니다. SSO와 MFA 같은 강력한 보안 기능과 세밀한 접근 제어를 지원하여 간편하게 보안 네트워크를 구축할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/OpenBMB/ChatDev" target="_blank">OpenBMB/ChatDev</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LLM 기반의 멀티 에이전트 협업을 통해 소프트웨어 개발 전체 과정을 자동화하는 ChatDev가 2.0 버전으로 업데이트되었습니다. 여러 AI 에이전트들이 서로 대화하며 기획부터 코딩까지 수행하는 능력이 더욱 강화되었습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/badlogic/pi-mono" target="_blank">badlogic/pi-mono</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


코딩 에이전트 CLI, 통합 LLM API, 웹 UI 등 다양한 도구를 한데 모은 포괄적인 AI 에이전트 툴킷입니다. Slack 봇이나 vLLM 파드 기능까지 포함되어 있어 개발자가 원하는 방식으로 유연하게 에이전트를 구축하고 활용할 수 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Fine-tuning</code> <code>Agent</code> <code>Reasoning</code> <code>Distillation</code> <code>Alignment</code> <code>RAG</code> <code>Prompt</code> <code>Llama</code> <code>Eval</code> 
</div>

---

