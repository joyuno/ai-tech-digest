---
layout: post
title: "self-evolving multi-agent에서 사라지는 안전성 실증"
date: 2026-02-15
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies"
daily_url: "https://arxiv.org/abs/2602.09877"
daily_keywords: ["LLM", "Alignment", "Agent", "Prompt", "Multimodal", "Distillation", "Audio", "Claude", "Eval", "Transformer"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2602.09877.png"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.09877" target="_blank">The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


이 논문은 LLM 기반의 멀티 에이전트 시스템이 스스로 진화할 때 발생하는 '자기 진화 트릴레마'를 다룹니다. 에이전트 사회가 외부 개입 없이 자율적으로 발전하려 할 때, 안전성(Safety)이 필연적으로 약화된다는 점을 이론적 및 실증적으로 증명했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12036" target="_blank">Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


RLVR(검증 가능한 보상을 통한 강화학습)의 데이터 효율성을 높이기 위해 'Composition-RL'이라는 새로운 방법을 제안합니다. 성공하기 쉬운 프롬프트들을 결합하고 재구성하여 학습 데이터의 낭비를 줄이고, 모델의 성능을 더 효과적으로 향상시키는 데 초점을 맞췄습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12205" target="_blank">DeepGen 1.0: A Lightweight Unified Multimodal Model for Advancing Image Generation and Editing</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


거대 모델에 버금가는 성능을 가진 5B 파라미터 크기의 경량화 멀티모달 모델, 'DeepGen 1.0'을 소개합니다. 'SCB'라는 기술을 도입해 적은 리소스로도 이미지 생성 및 편집 작업에서 정밀한 의미 이해와 제어 능력을 보여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12125" target="_blank">Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>


학생 모델이 교사 모델을 모방하는 On-policy distillation(OPD)이 강화학습(RL)의 특수한 형태임을 이론적으로 규명했습니다. 이를 바탕으로 보상 외삽(Reward Extrapolation)을 활용해, 학생 모델이 교사 모델을 뛰어넘는 성능을 낼 수 있는 일반화된 학습법을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.10934" target="_blank">MOSS-Audio-Tokenizer: Scaling Audio Tokenizers for Future Audio Foundation Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>


LLM이 오디오를 더 잘 이해하고 생성할 수 있도록 돕는 새로운 오디오 토크나이저 아키텍처를 제안합니다. 기존의 복잡한 CNN 기반 방식 대신, 완전히 엔드투엔드로 학습되는 구조를 통해 오디오 복원 품질을 높이고 모델 확장이 용이하도록 설계되었습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/custom-cuda-kernels-agent-skills" target="_blank">Custom Kernels for All from Codex and Claude</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Codex나 Claude 같은 코딩 LLM을 활용해 누구나 쉽게 맞춤형 GPU 커널을 작성하는 방법을 다룹니다. 복잡한 CUDA 프로그래밍 지식 없이도 모델의 추론 속도를 최적화할 수 있는 실용적인 접근법을 제시합니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/openenv-turing" target="_blank">OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


도구를 사용하는 AI 에이전트를 실제 환경에서 평가하는 'OpenEnv' 프레임워크의 활용 사례를 소개합니다. 단순한 벤치마크를 넘어, 현실 세계의 복잡한 시나리오에서 에이전트가 얼마나 효과적으로 도구를 활용하는지 검증합니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/transformersjs-v4" target="_blank">Transformers.js v4 Preview: Now Available on NPM!</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


웹 브라우저에서 직접 Transformer 모델을 실행할 수 있는 'Transformers.js'의 v4 프리뷰 버전이 NPM에 공개되었습니다. 최신 모델 지원과 웹 환경에서의 성능 최적화가 포함되어, 서버 없이도 강력한 AI 기능을 웹앱에 구현할 수 있습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/tambo-ai/tambo" target="_blank">tambo-ai/tambo</a></h3>



React 환경에서 AI가 실시간으로 생성하는 'Generative UI'를 쉽게 구현할 수 있도록 돕는 SDK입니다. 개발자가 미리 모든 화면을 코딩하지 않아도, 상황에 맞춰 유동적으로 변하는 인터페이스를 구축할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/SynkraAI/aios-core" target="_blank">SynkraAI/aios-core</a></h3>



풀스택 개발 과정을 AI가 주도적으로 조율하는 'Synkra AIOS'의 핵심 프레임워크입니다. AI 오케스트레이션을 통해 복잡한 시스템 개발 및 관리를 자동화하여 개발 생산성을 극대화하는 것을 목표로 합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/rowboatlabs/rowboat" target="_blank">rowboatlabs/rowboat</a></h3>



사용자와의 대화나 작업 맥락을 기억하는(Memory) 기능을 갖춘 오픈소스 AI 동료 프로젝트입니다. 단순한 챗봇을 넘어, 과거의 상호작용을 바탕으로 지속적으로 업무를 보조하는 AI 에이전트를 만들 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/alibaba/zvec" target="_blank">alibaba/zvec</a></h3>



알리바바에서 공개한 초경량, 초고속 인프로세스(In-process) Vector Database입니다. 별도의 무거운 서버 구축 없이 애플리케이션 내부에서 가볍게 실행되며, 빠른 벡터 검색 속도를 제공하여 RAG 구축 등에 유용합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Zipstack/unstract" target="_blank">Zipstack/unstract</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


복잡한 코딩 없이 비정형 문서를 구조화된 데이터로 변환해 주는 노코드 LLM 플랫폼입니다. ETL 파이프라인을 손쉽게 구축하고 이를 API로 배포할 수 있어, 문서 처리 자동화 업무를 획기적으로 간소화해 줍니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Alignment</code> <code>Agent</code> <code>Prompt</code> <code>Multimodal</code> <code>Distillation</code> <code>Audio</code> <code>Claude</code> <code>Eval</code> <code>Transformer</code> 
</div>

---

