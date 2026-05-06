---
layout: post
title: "Toss Front SDK 퍼사드 패턴 설계"
date: 2026-02-27
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.18283" target="_blank">HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


추천 시스템에서 긴 사용자 행동 패턴을 효율적으로 분석하는 HyTRec 모델을 제안합니다. Hybrid Attention 구조를 통해 장기적인 선호도와 단기적인 행동 변화를 분리하여 학습함으로써, 계산 비용은 줄이면서도 추천의 정확도는 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12192" target="_blank">Query-focused and Memory-aware Reranker for Long Context Processing</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


LLM의 Retrieval Head를 활용해 검색 결과의 순위를 재조정(Reranking)하는 새로운 프레임워크입니다. 후보 목록 전체를 고려하는 Listwise 방식을 적용하여 연속적인 연관성 점수를 산출하며, 별도의 레이블 없이도 다양한 데이터셋에서 학습이 가능합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.17602" target="_blank">MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models</a></h3>



신약 개발 등에 활용되는 분자 그래프 생성의 품질을 높이기 위해 계층적 이산 Diffusion 모델인 MolHIT를 소개합니다. 기존 2D 그래프 모델들이 겪던 낮은 화학적 유효성 문제를 해결하고, 원하는 물성을 가진 분자를 더 정교하게 생성할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12160" target="_blank">DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


오디오와 비디오 생성, 편집, 애니메이션을 하나의 프레임워크로 통합한 인간 중심의 생성 모델입니다. 여러 캐릭터의 신원(Identity)과 목소리를 동시에 정밀하게 제어할 수 있어 콘텐츠 제작의 효율성을 크게 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.21204" target="_blank">Test-Time Training with KV Binding Is Secretly Linear Attention</a></h3>



시퀀스 모델링에서 사용되는 KV 바인딩 기반의 Test-Time Training(TTT)이 실제로는 Linear Attention의 한 형태임을 밝혀낸 연구입니다. TTT가 단순히 데이터를 암기하는 것이 아니라 학습된 연산자처럼 동작한다는 새로운 해석을 제시합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/moe-transformers" target="_blank">Mixture of Experts (MoEs) in Transformers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Transformer 모델의 크기를 키우면서도 연산 효율성을 유지하는 핵심 기술인 Mixture of Experts (MoE)를 설명합니다. 모든 파라미터를 사용하지 않고 상황에 맞는 전문가(Expert) 네트워크만 활성화하여 거대 모델을 효율적으로 구동하는 원리를 다룹니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-on-jetson" target="_blank">Deploying Open Source Vision Language Models (VLM) on Jetson</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


오픈소스 Vision Language Model (VLM)을 NVIDIA Jetson과 같은 엣지 디바이스에 배포하는 방법을 안내합니다. 클라우드 없이 로컬 환경에서도 시각 정보를 이해하고 처리하는 AI 애플리케이션을 구축하는 데 유용합니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ggml-joins-hf" target="_blank">GGML and llama.cpp join HF to ensure the long-term progress of Local AI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로컬 AI 구동의 핵심인 GGML 라이브러리와 llama.cpp 프로젝트가 Hugging Face와 협력한다는 소식입니다. 개인용 하드웨어에서도 최신 LLM을 빠르고 쉽게 실행할 수 있도록 오픈소스 AI 생태계를 더욱 강화할 예정입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/toss-front-sdk" target="_blank">쓰기 쉬운 Toss Front SDK</a></h3>



개발자가 사용하기 편한 프론트엔드 SDK를 설계하기 위해 퍼사드(Facade) 패턴을 적용한 노하우를 공유합니다. 단순히 기능을 나열하는 것이 아니라, 사용자가 직관적으로 코드를 작성할 수 있도록 인터페이스를 개선하는 방법을 다룹니다.

<small><i data-lucide="user"></i> 토스</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/harness-for-team-productivity" target="_blank">Software 3.0 시대, Harness를 통한 조직 생산성 저점 높이기</a></h3>



Software 3.0 시대를 맞아 개발 플랫폼 Harness를 도입하여 조직 전체의 생산성을 높이는 전략을 소개합니다. 개인의 역량에 의존하던 방식을 넘어, 팀 전체가 표준화된 프로세스로 효율적으로 개발하는 문화를 만드는 과정입니다.

<small><i data-lucide="user"></i> 토스</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/deer-flow" target="_blank">bytedance/deer-flow</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


연구부터 코딩, 창작까지 수행하는 오픈소스 SuperAgent 프레임워크입니다. 샌드박스 환경과 메모리 기능을 갖추고 있어, 복잡한 작업을 하위 에이전트들과 협력해 몇 분에서 몇 시간 걸리는 작업도 자율적으로 처리합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/farion1231/cc-switch" target="_blank">farion1231/cc-switch</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude Code, Codex, Gemini CLI 등 다양한 AI 코딩 어시스턴트를 한곳에서 관리하는 데스크톱 도구입니다. 크로스 플랫폼을 지원하며, 개발자가 여러 AI 도구를 손쉽게 전환하며 사용할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/claude-flow" target="_blank">ruvnet/claude-flow</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude 모델에 특화된 에이전트 오케스트레이션 플랫폼으로, 지능형 멀티 에이전트 시스템을 구축할 수 있습니다. RAG 통합 및 엔터프라이즈급 아키텍처를 제공하여 복잡한 업무 자동화 워크플로우를 효율적으로 관리합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruvector" target="_blank">ruvnet/ruvector</a></h3>



Rust 언어로 개발된 고성능 리얼타임 벡터 그래프 신경망(GNN)이자 데이터베이스입니다. 스스로 학습하는(Self-Learning) 기능을 탑재하여 실시간 데이터 처리와 복잡한 관계 분석에 강력한 성능을 발휘합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/moonshine-ai/moonshine" target="_blank">moonshine-ai/moonshine</a></h3>



엣지 디바이스 환경에 최적화된 빠르고 정확한 자동 음성 인식(ASR) 모델입니다. 리소스가 제한된 기기에서도 음성 데이터를 효율적으로 텍스트로 변환할 수 있어 온디바이스 AI 구현에 적합합니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/467" target="_blank">AI News Weekly - Issue #467: Anthropic has receipts. And nobody wants to pay for AI. - Feb 26th 2026</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


중국 연구소의 모델 유출 논란과 DeepSeek의 제재 우회 등 한 주간의 굵직한 AI 이슈를 정리했습니다. AI 분야에 천문학적인 자금이 쏟아지고 있지만, 정작 사용자와 기업들은 비용 지불에 인색한 수익화 딜레마를 함께 짚어봅니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Retrieval</code> <code>Eval</code> <code>RAG</code> <code>Audio</code> <code>MoE</code> <code>Vision</code> <code>Llama</code> <code>Agent</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

