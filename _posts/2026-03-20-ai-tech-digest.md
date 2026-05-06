---
layout: post
title: "AI Tech - 2026-03-20"
date: 2026-03-20
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.13398" target="_blank">Qianfan-OCR: A Unified End-to-End Model for Document Intelligence</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


문서 분석과 이해를 하나의 모델로 통합한 4B 파라미터 크기의 Vision-Language 모델입니다. 이미지를 바로 Markdown으로 변환할 수 있으며, 표 추출이나 문서 QA 같은 다양한 프롬프트 기반 작업도 거뜬히 수행해냅니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.17187" target="_blank">MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


사용자의 요구사항 변화에 맞춰 스스로 학습하고 진화하는 새로운 LLM Agent 프레임워크를 제안합니다. 기존의 정적인 Agent와 달리, 다양한 작업 환경에서 지속적으로 능력을 업데이트하며 더 나은 서비스를 제공할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.14935" target="_blank">Video-CoE: Reinforcing Video Event Prediction via Chain of Events</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


비디오 이벤트 예측 분야에서 최신 MLLM들이 겪고 있는 논리적 추론의 한계를 짚어낸 연구입니다. 이를 해결하기 위해 비디오 내 시간적 흐름과 미래 사건을 연결하는 'Chain of Events' 방식을 도입하여 예측 정확도를 크게 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.17117" target="_blank">MosaicMem: Hybrid Spatial Memory for Controllable Video World Models</a></h3>



비디오 생성 모델에서 카메라의 움직임이나 화면 전환 시에도 일관된 장면을 유지할 수 있도록 돕는 하이브리드 공간 메모리 시스템입니다. 이미지를 3D 패치 형태로 변환하여 기억함으로써, 움직이는 객체와 카메라 워킹을 훨씬 더 자연스럽게 표현합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.17218" target="_blank">Alignment Makes Language Models Normative, Not Descriptive</a></h3>


<div class="categories">
<span class="category-tag">🎯 신뢰성/안전</span> <span class="category-tag">💻 개발 도구</span> 
</div>


언어 모델의 정렬(Alignment) 과정이 모델을 인간의 이상적인 선호도에 맞추지만, 실제 사람의 행동을 예측하는 능력은 오히려 떨어뜨린다는 흥미로운 연구 결과입니다. 다양한 게임 이론 환경에서 테스트한 결과, 정렬되지 않은 베이스 모델이 사람의 선택을 훨씬 더 잘 예측했습니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.17995" target="_blank">LoST: Level of Semantics Tokenization for 3D Shapes</a></h3>



3D 모델 생성을 위한 AR(Autoregressive) 모델의 효율성을 극대화하기 위해 의미 기반의 새로운 Tokenization 기법을 제안합니다. 기존 기하학적 방식이 가진 비효율성을 개선하여, 3D 형태를 훨씬 더 똑똑하고 가볍게 학습할 수 있게 해줍니다.

<small>👤 Niladri Shekhar Dutt, Zifan Shi, Paul Guerrero</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.18004" target="_blank">Unified Spatio-Temporal Token Scoring for Efficient Video VLMs</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


비디오 기반 Vision-Language 모델의 계산 효율을 높이기 위해 불필요한 토큰을 똑똑하게 제거하는 기법입니다. 시공간의 중복된 정보를 효과적으로 줄여주어, 모델의 성능은 유지하면서도 연산량은 대폭 감소시킬 수 있습니다.

<small>👤 Jianrui Zhang, Yue Yang, Rohun Tripathi</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.17965" target="_blank">LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


자연어 프롬프트만으로 포스터나 로고 같은 디자인 작업물을 여러 개의 편집 가능한 레이어로 생성해 내는 모델입니다. 기존 방식과 달리 레이어 수에 제한이 없고 의미 단위로 요소를 분리해 주어, 생성 후 디자인 수정과 활용이 매우 편리해집니다.

<small>👤 Vlad-Constantin Lungu-Stan, Ionut Mironica, Mariana-Iuliana Georgescu</small>

</div>



---


## 👕 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/ai%EB%A5%BC-%EC%93%B0%EB%8A%94-%ED%9A%8C%EC%82%AC-vs-ai%EB%A5%BC-%EB%A7%8C%EB%93%9C%EB%8A%94-%ED%9A%8C%EC%82%AC-47932e6565d3?source=rss----f107b03c406e---4" target="_blank">AI를 쓰는 회사 vs AI를 만드는 회사</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


오프라인 매장에서 옷을 직접 입어보고 느끼는 '핏(Fit)' 경험을 온라인으로 구현하기 위한 무신사의 기술적 고민을 담은 글입니다. 단순한 LLM 도입을 넘어, 자체적인 데이터 자산을 구축하며 AI 전략을 만들어가는 생생한 과정을 엿볼 수 있습니다.

<small>👤 Daeyun Kim</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/opendataloader-project/opendataloader-pdf" target="_blank">opendataloader-project/opendataloader-pdf</a></h3>



복잡한 PDF 문서를 AI가 학습하기 좋은 데이터 형태로 자동 변환해 주는 오픈소스 파서 도구입니다. 접근성 높은 데이터를 쉽게 구축할 수 있어 LLM 학습이나 RAG 파이프라인 구성에 매우 유용하게 쓰일 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langchain-ai/open-swe" target="_blank">langchain-ai/open-swe</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


비동기 방식으로 동작하여 더욱 빠르고 효율적으로 코드를 작성해 주는 오픈소스 AI 코딩 Agent입니다. 복잡한 개발 작업도 스스로 계획하고 실행할 수 있어 개발자들의 든든한 조수 역할을 해냅니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/jarrodwatts/claude-hud" target="_blank">jarrodwatts/claude-hud</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude Code 사용 시 현재 실행 중인 도구나 Agent의 상태, Context 사용량 등을 시각적으로 한눈에 보여주는 유용한 플러그인입니다. 작업의 진행 상황을 투명하게 파악할 수 있어 개발 생산성을 크게 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/unslothai/unsloth" target="_blank">unslothai/unsloth</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


Qwen, DeepSeek, Gemma 등 다양한 오픈소스 모델을 로컬 환경에서 쉽게 훈련하고 실행할 수 있도록 돕는 통합 웹 UI 도구입니다. 복잡한 설정 없이도 누구나 편리하게 자신만의 모델을 튜닝해 볼 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/mobile-dev-inc/Maestro" target="_blank">mobile-dev-inc/Maestro</a></h3>



모바일 앱과 웹 서비스의 엔드투엔드(E2E) 테스트를 놀랍도록 쉽게 자동화해 주는 도구입니다. 직관적인 흐름으로 테스트 코드를 작성할 수 있어 개발과 QA 과정의 번거로움을 크게 덜어줍니다.



</div>



---


## 📰 AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/474" target="_blank">AI News Weekly - $27B for AI, 16K jobs gone, and the first real deepfake campaign ad - Mar 19th 2026</a></h3>



메타(Meta)가 AI 인프라에 270억 달러를 투자하는 동시에 대규모 구조조정을 진행했다는 소식을 다룹니다. 선거판에 등장한 사실적인 AI 딥페이크 광고 사례와 함께, AI 시대가 가져올 거대한 변화와 그림자를 현실적으로 조명합니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Vision</code> <code>Prompt</code> <code>LLM</code> <code>Agent</code> <code>Eval</code> <code>Alignment</code> <code>Claude</code> <code>Claude Code</code> <code>GPT</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>