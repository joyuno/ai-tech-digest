---
layout: post
title: "무신사가 다시 정의한 사용자 경험 기준 비즈니스 심각도"
date: 2026-02-25
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "A Very Big Video Reasoning Suite"
daily_url: "https://arxiv.org/abs/2602.20159"
daily_keywords: ["Reasoning", "CoT", "LLM", "Inference", "Vision", "LoRA", "RAG", "Eval", "Agent", "Llama"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2602.20159.png"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.20159" target="_blank">A Very Big Video Reasoning Suite</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


비디오 모델들이 시각적 품질은 뛰어나지만 추론 능력은 아직 부족하다는 점을 지적하는 논문입니다. 텍스트로는 표현하기 힘든 시공간적 연속성과 인과관계를 이해하기 위해, 대규모 데이터 부족 문제를 해결하고 비디오 추론 능력을 체계적으로 연구하는 방법을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.08354" target="_blank">Does Your Reasoning Model Implicitly Know When to Stop Thinking?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


거대 추론 모델(LRM)이 복잡한 문제를 풀기 위해 Long Chain of Thought(CoT)를 사용할 때 발생하는 비효율성을 분석했습니다. 단순히 생각하는 과정이 길다고 정답률이 높아지는 것은 아니며, 모델이 불필요한 연산을 줄이고 언제 멈춰야 할지 아는 것이 중요하다는 점을 강조합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.10693" target="_blank">VESPO: Variational Sequence-Level Soft Policy Optimization for Stable Off-Policy LLM Training</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


LLM을 위한 강화학습(RL) 과정에서 발생하는 학습 불안정성과 정책 붕괴 문제를 해결하기 위한 연구입니다. 기존 Importance Sampling의 높은 분산 문제를 개선한 VESPO라는 기법을 통해, 더 안정적이고 효율적인 오프폴리시(Off-policy) 학습을 가능하게 합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.18532" target="_blank">VLANeXt: Recipes for Building Strong VLA Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


시각-언어-행동(VLA) 모델 분야가 파편화되어 있어 어떤 설계가 효과적인지 파악하기 어려웠던 점을 개선하고자 합니다. 다양한 VLA 모델의 학습 프로토콜을 재검토하여, 강력한 모델을 구축하기 위해 실제로 중요한 설계 요소가 무엇인지 정리한 '레시피'를 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.19672" target="_blank">SkillOrchestra: Learning to Route Agents via Skill Transfer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


복합 AI 시스템에서 여러 에이전트를 효율적으로 조율(Orchestration)하는 것은 매우 중요한 과제인데요. 기존 라우팅 방식의 한계를 극복하기 위해, SkillOrchestra라는 프레임워크를 제안하여 변화하는 작업 요구사항에 맞춰 에이전트들에게 작업을 똑똑하게 배분합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/cosmos-on-jetson" target="_blank">Deploying Open Source Vision Language Models (VLM) on Jetson</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


NVIDIA Jetson 같은 엣지 디바이스 환경에서 오픈소스 Vision Language Model(VLM)을 배포하고 실행하는 가이드를 제공합니다. 무거운 모델을 작은 장치에서도 효율적으로 최적화하여 구동하는 구체적인 방법을 확인할 수 있습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ggml-joins-hf" target="_blank">GGML and llama.cpp join HF to ensure the long-term progress of Local AI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로컬 AI 구동의 핵심 프로젝트인 GGML과 llama.cpp가 Hugging Face와 공식적으로 협력하게 되었다는 소식입니다. 이를 통해 개인 컴퓨터나 로컬 환경에서 AI 모델을 실행하는 기술이 앞으로 더욱 안정적이고 빠르게 발전할 것으로 기대됩니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/unsloth-jobs" target="_blank">Train AI models with Unsloth and Hugging Face Jobs for FREE</a></h3>



Unsloth 라이브러리를 활용해 학습 속도를 비약적으로 높이고, Hugging Face Jobs를 통해 무료로 모델을 학습시키는 방법을 소개합니다. 고성능 GPU 장비 없이도 효율적으로 나만의 AI 모델을 파인튜닝해볼 수 있는 유용한 팁입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="shirt"></i> 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%EC%9D%B4-%EC%9E%A5%EC%95%A0-%EC%96%BC%EB%A7%88%EB%82%98-%EC%8B%AC%EA%B0%81%ED%95%9C%EA%B0%80%EC%9A%94-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B2%BD%ED%97%98%EC%9D%84-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4-%EC%8B%AC%EA%B0%81%EB%8F%84%EB%A5%BC-%EC%A0%95%EC%9D%98%ED%95%98%EB%8B%A4-b13bf1d52b19?source=rss----f107b03c406e---4" target="_blank">“이 장애, 얼마나 심각한가요?” 사용자 경험을 기준으로 비즈니스 심각도를 정의하다</a></h3>



무신사 큐레이터 서비스팀이 장애 발생 시 대응 우선순위를 정하기 위해 '비즈니스 심각도'를 새롭게 정의한 경험기입니다. 핵심 사용자 여정(Critical User Journey)과 SLI를 기준으로, 단순한 기술적 오류를 넘어 실제 비즈니스와 사용자 경험에 미치는 영향을 중심으로 장애 대응 체계를 마련했습니다.

<small><i data-lucide="user"></i> Hyewon Choi</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/OpenBB-finance/OpenBB" target="_blank">OpenBB-finance/OpenBB</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


애널리스트, 퀀트, 그리고 AI 에이전트를 위해 설계된 오픈소스 금융 데이터 플랫폼입니다. 주식, 코인 등 다양한 금융 데이터를 통합적으로 제공하여, AI 기반의 투자 분석 도구나 자동화 시스템을 개발할 때 매우 유용합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools" target="_blank">x1xhlol/system-prompts-and-models-of-ai-tools</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude Code, Cursor, Devin 등 최근 화제가 된 AI 도구들의 시스템 프롬프트(System Prompts)와 모델 정보를 모아둔 저장소입니다. 상용 AI 서비스들이 내부적으로 어떻게 동작하도록 지시받았는지 엿볼 수 있어 프롬프트 엔지니어링에 참고하기 좋습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruvector" target="_blank">ruvnet/ruvector</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Rust로 개발된 고성능 벡터 및 그래프 데이터베이스로, AI 에이전트와 실시간 분석 시스템에 최적화되어 있습니다. HNSW 검색 알고리즘과 그래프 지능을 하나의 엔진으로 통합하여, 빠르고 확장성 있는 데이터 추론을 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/GVCLab/PersonaLive" target="_blank">GVCLab/PersonaLive</a></h3>



정지된 인물 사진을 라이브 스트리밍 환경에 맞춰 생동감 있게 애니메이션화하는 기술입니다. 단순한 입 모양을 넘어 풍부한 표정 연기가 가능하여, 버추얼 유튜버나 화상 회의 등 다양한 분야에서 활용될 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/VectifyAI/PageIndex" target="_blank">VectifyAI/PageIndex</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


벡터 임베딩(Vector Embedding) 없이 추론(Reasoning) 능력을 기반으로 문서를 색인하고 검색하는 새로운 RAG 접근 방식입니다. 기존 벡터 DB가 놓칠 수 있는 문서의 맥락과 구조를 더 깊이 있게 이해하여 정확한 정보를 찾아내는 것을 목표로 합니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>CoT</code> <code>LLM</code> <code>Inference</code> <code>Vision</code> <code>LoRA</code> <code>RAG</code> <code>Eval</code> <code>Agent</code> <code>Llama</code> 
</div>

---

