---
layout: post
title: "LLM2Vec-Gen — 잠재 응답으로 만드는 generative embedding"
date: 2026-03-13
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.03143" target="_blank">Geometry-Guided Reinforcement Learning for Multi-view Consistent 3D Scene Editing</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


2D Diffusion 모델을 활용한 3D 장면 편집에서 다중 시점의 일관성을 유지하기 위해 강화학습을 적용한 새로운 논문입니다. 일관된 3D 데이터를 직접 생성하는 것은 어렵지만 검증은 가능하다는 점에 착안하여 학습 데이터 부족 문제를 획기적으로 해결했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.10165" target="_blank">OpenClaw-RL: Train Any Agent Simply by Talking</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


사용자의 답변이나 터미널 결과 등 모든 상호작용 피드백을 실시간 온라인 학습 데이터로 활용하는 OpenClaw-RL 프레임워크를 제안합니다. 일상적인 대화나 GUI 조작 등 다양한 환경의 신호를 동시에 학습하여 Agent 성능을 자연스럽게 향상시킬 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.09906" target="_blank">Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


단순한 사실 확인 질문에 대해 LLM이 추론 과정을 거칠 때 어떤 효과가 있는지 분석한 흥미로운 연구입니다. 복잡한 논리가 필요 없는 질문이더라도, 스스로 생각하는 과정을 통해 모델 내부에 숨겨진 매개변수적 지식을 훨씬 더 효과적으로 꺼내어 정확한 답변을 도출합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.09229" target="_blank">Flash-KMeans: Fast and Memory-Efficient Exact K-Means</a></h3>



과거의 오프라인 처리 방식이었던 k-means 알고리즘을 최신 AI 시스템 설계에 맞게 완전히 최적화한 Flash-KMeans입니다. 기존 GPU 환경에서 발생하던 저수준의 메모리 병목 현상을 해결하여, 실시간 온라인 시스템에서도 극적으로 빠르고 효율적으로 사용할 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.09877" target="_blank">InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


이미지 이해, 추론, 생성, 그리고 편집 기능까지 하나의 프레임워크에 담아낸 4B 파라미터 크기의 경량화 다중 모달 모델 InternVL-U를 소개합니다. 시각적 표현을 분리하는 모듈식 설계를 적용하여, 모델의 언어 이해력을 단단하게 유지하면서도 뛰어난 생성 능력을 자랑합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.10913" target="_blank">LLM2Vec-Gen: Generative Embeddings from Large Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


LLM을 활용해 텍스트 임베딩을 만들 때, 입력값 자체가 아닌 모델이 내놓을 '잠재적 응답'을 표현하도록 학습시키는 새로운 자기 지도 학습 방식인 LLM2Vec-Gen입니다. 대조 학습 기반의 기존 방식에서 벗어나, 다양한 입력과 출력 사이의 의미적 연결성을 더욱 깊이 있게 포착하도록 도와줍니다.

<small><i data-lucide="user"></i> Parishad BehnamGhader, Vaibhav Adlakha, Fabian David Schmidt</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.11048" target="_blank">COMIC: Agentic Sketch Comedy Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


캐릭터 정보만 주어지면 유명 코미디 쇼처럼 재미있는 짧은 스케치 영상을 자동으로 만들어내는 훌륭한 AI 시스템입니다. 실제 방송 스튜디오의 역할들을 모방한 여러 Agent들이 서로 경쟁하고 평가하는 과정을 반복하며 대본과 영상의 퀄리티를 최적화합니다.

<small><i data-lucide="user"></i> Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.11042" target="_blank">V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation</a></h3>



영상 속 사건의 타이밍에 딱 맞춰서 배경 음악을 자동으로 생성해 주는 V2M-Zero 모델입니다. 영상과 음악 데이터가 짝지어져 있지 않아도, 시각적 변화와 청각적 변화가 공유하는 시간적 구조를 똑똑하게 분석하여 아주 자연스럽게 동기화된 음악을 만들어냅니다.

<small><i data-lucide="user"></i> Yan-Bo Lin, Jonah Casebeer, Long Mai</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/microsoft/BitNet" target="_blank">microsoft/BitNet</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


마이크로소프트에서 공식적으로 공개한 1-bit LLM 전용 추론 프레임워크입니다. 모델의 가중치를 극단적으로 압축하는 기술을 통해, 메모리 사용량을 대폭 줄이면서도 빠르고 효율적인 모델 실행을 가능하게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langflow-ai/openrag" target="_blank">langflow-ai/openrag</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Langflow와 Opensearch 등을 기반으로 구축된 포괄적인 RAG(검색 증강 생성) 오픈소스 플랫폼인 OpenRAG입니다. 단일 패키지 형태로 제공되어 복잡한 설정 없이도 누구나 쉽게 자체 데이터를 활용한 답변 생성 시스템을 구축할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/vectorize-io/hindsight" target="_blank">vectorize-io/hindsight</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


과거의 행동과 결과를 스스로 학습하여 갈수록 더 똑똑해지는 Agent 메모리 시스템인 Hindsight입니다. AI가 이전의 상호작용 경험을 기억하고 분석함으로써, 앞으로의 작업에서 발생할 수 있는 오류를 줄이고 작업 성능을 꾸준히 개선합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/google-ai-edge/LiteRT" target="_blank">google-ai-edge/LiteRT</a></h3>



TensorFlow Lite의 뒤를 잇는 구글의 새로운 온디바이스 AI 프레임워크인 LiteRT입니다. 모바일이나 엣지 기기 환경에서 고성능 머신러닝 모델과 생성형 AI를 매우 효율적으로 변환하고 최적화하여 실행할 수 있도록 강력하게 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/msitarzewski/agency-agents" target="_blank">msitarzewski/agency-agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


프론트엔드 개발자부터 커뮤니티 관리자까지 다양한 역할을 수행하는 전문화된 AI Agent들을 모아둔 재미있는 프로젝트입니다. 각 에이전트마다 고유한 성격과 작업 프로세스가 부여되어 있어, 마치 실제 전문가들로 구성된 멋진 에이전시를 운영하는 듯한 경험을 줍니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Fine-tuning</code> <code>RAG</code> <code>Agent</code> <code>LLM</code> <code>Multimodal</code> <code>Eval</code> <code>Inference</code> 
</div>

---

