---
layout: post
title: "claude-mem 트렌드 지속 + 코딩 메모리 압축 흐름"
date: 2026-02-03
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas"
daily_url: "https://arxiv.org/abs/2601.21558"
daily_keywords: ["LLM", "Fine-tuning", "Agent", "Reasoning", "Distillation", "Alignment", "RAG", "Prompt", "Claude", "Claude Code"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2601.21558.png"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.21558" target="_blank">ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LLM 기반 에이전트가 도구를 더 잘 쓰도록 돕는 완전 자동화 프레임워크인 ASTRA를 소개합니다. 기존의 수작업이나 시뮬레이션 의존 없이도 안정적인 학습이 가능해 강력한 도구 활용 에이전트를 만들 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22813" target="_blank">Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


NVIDIA Blackwell GPU의 NVFP4 형식을 활용해 거대 모델을 효율적으로 학습하는 Quartet II 기법입니다. 기존 양자화 학습에서 발생하는 정확도 손실을 줄여 FP16 수준의 성능을 유지하면서도 속도는 높였답니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22975" target="_blank">Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


인터넷상의 일반 텍스트를 활용해 무제한으로 RLVR(검증 가능한 보상 기반 강화 학습) 데이터를 생성하는 'Golden Goose' 기법입니다. 빈칸 채우기를 객관식 문제로 변환하여 데이터 부족 문제를 해결하고 LLM의 추론 능력을 끌어올립니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.23143" target="_blank">THINKSAFE: Self-Generated Safety Alignment for Reasoning Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


추론 모델이 과도한 최적화로 인해 안전성을 잃는 문제를 해결하는 THINKSAFE 방법론입니다. 외부 모델에 의존하지 않고 스스로 안전 가이드라인을 학습하여, 원래의 뛰어난 추론 능력을 해치지 않고도 안전하게 모델을 조정합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2601.22628" target="_blank">TTCS: Test-Time Curriculum Synthesis for Self-Evolving</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


테스트 시점에 입력된 질문만으로 모델을 실시간 학습시켜 추론 능력을 높이는 TTCS 프레임워크입니다. 난이도가 높은 문제도 단계별 학습 과정을 스스로 생성(Self-Evolving)하여 해결하도록 돕는 똑똑한 방식이죠.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control" target="_blank">Introducing NVIDIA Cosmos Policy for Advanced Robot Control</a></h3>



NVIDIA가 고급 로봇 제어를 위해 새롭게 공개한 Cosmos Policy를 소개합니다. 물리 세계를 이해하고 복잡한 작업을 수행하는 로봇 AI 모델의 성능을 한 단계 높여줄 기술이에요.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/daggr" target="_blank">Introducing Daggr: Chain apps programmatically, inspect visually</a></h3>



복잡한 AI 애플리케이션 워크플로우를 코드로 연결하고 시각적으로 바로 확인할 수 있는 Daggr 도구입니다. 여러 기능을 체인처럼 엮어 효율적으로 관리하고 디버깅할 때 유용하겠네요.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/upskill" target="_blank">We Got Claude to Build CUDA Kernels and teach open models!</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


고성능 GPU 프로그래밍인 CUDA 커널을 Claude가 직접 작성하고, 이를 바탕으로 오픈 소스 모델을 교육시킨 흥미로운 사례입니다. LLM이 복잡한 하드웨어 최적화 코드까지 다룰 수 있음을 보여주네요.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thedotmack/claude-mem" target="_blank">thedotmack/claude-mem</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude를 사용한 코딩 내역을 자동으로 저장하고 압축하여 다음 작업에서도 문맥을 기억하게 해주는 플러그인입니다. 긴 코딩 세션에서도 중요한 정보를 잃지 않고 효율적으로 개발을 이어갈 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ThePrimeagen/99" target="_blank">ThePrimeagen/99</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


유명 개발 유튜버 ThePrimeagen이 만든, Neovim 사용자를 위한 '제대로 된' AI 에이전트 플러그인입니다. 터미널 환경에서 코딩할 때 AI의 도움을 매끄럽게 받을 수 있도록 설계되었습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/netbirdio/netbird" target="_blank">netbirdio/netbird</a></h3>



WireGuard 기반으로 여러 장치를 안전하게 연결해주는 가상 네트워크 구축 도구입니다. SSO나 MFA 같은 강력한 인증 기능을 지원해서, 복잡한 설정 없이도 기업 수준의 보안 네트워크를 만들 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/OpenBMB/ChatDev" target="_blank">OpenBMB/ChatDev</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LLM 기반의 여러 AI 에이전트들이 협업하여 소프트웨어를 개발하는 ChatDev가 2.0 버전으로 업데이트되었습니다. 기획부터 코딩까지, 가상의 AI 직원들이 회사를 운영하듯 프로젝트를 완성해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/badlogic/pi-mono" target="_blank">badlogic/pi-mono</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


코딩 에이전트 CLI부터 통합 LLM API, 웹 UI 라이브러리까지 포함된 종합 AI 에이전트 툴킷입니다. 나만의 AI 서비스를 개발할 때 필요한 다양한 도구들을 한곳에 모아두었네요.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/463" target="_blank">AI News Weekly - Issue #463: All about The "Moltbook" Phenomenon  - Feb 2nd 2026</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


인간은 가입할 수 없는 AI 에이전트 전용 커뮤니티 'Moltbook'이 등장해 화제와 논란을 동시에 낳고 있습니다. 에이전트끼리 가상 화폐 붐을 일으키기도 했지만, API 키 유출 등 보안 악몽이 우려된다는 소식입니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Fine-tuning</code> <code>Agent</code> <code>Reasoning</code> <code>Distillation</code> <code>Alignment</code> <code>RAG</code> <code>Prompt</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

