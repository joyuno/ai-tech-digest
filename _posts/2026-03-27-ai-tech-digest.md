---
layout: post
title: "AI 기술 다이제스트 - 2026-03-27"
date: 2026-03-27
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.22458" target="_blank">MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


이 논문은 기존의 순차적 방식이 가진 지연 시간과 오류 전파 문제를 해결하기 위해 문서 OCR을 새로운 관점으로 접근합니다. Diffusion 디코딩을 활용한 역 렌더링 방식을 통해 길고 복잡한 문서 구조를 더욱 빠르고 정확하게 파악할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.23497" target="_blank">WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG</a></h3>



기존 비디오 기반 세계 모델이 가진 단순한 행동 패턴의 한계를 극복하기 위해 만들어진 대규모 데이터셋입니다. 시각적 정보에만 의존하지 않고 명시적인 상태와 다양한 행동 데이터를 제공하여, 앞으로 생성형 액션 RPG 게임 개발에 큰 도움을 줄 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.24440" target="_blank">CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


사람처럼 컴퓨터를 조작하는 에이전트의 성능을 높이기 위해 구축된 대규모 비디오 데이터셋입니다. 기존의 단편적인 스크린샷 데이터가 가진 한계를 극복하고, 연속적인 고품질 시연 영상을 제공하여 에이전트의 복잡한 업무 자동화 능력을 크게 향상시킵니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.23483" target="_blank">SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


멀티모달 LLM 에이전트가 시각적 도구를 사용할 때 발생하는 심각한 속도 지연 문제를 해결하기 위한 논문입니다. 'SpecEyes'라는 새로운 가설 기반 인식 및 계획 프레임워크를 도입하여, 에이전트의 추론 속도와 시스템 동시성을 획기적으로 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.23499" target="_blank">DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models</a></h3>



노이즈나 화질 저하가 심한 실제 비디오 환경에서도 객체의 움직임을 정확하게 추적할 수 있는 새로운 광학 흐름 추정 모델입니다. 이미지 복원용 Diffusion 모델이 가진 특징을 활용해 손상된 영상에서도 시간적 변화를 잘 인식하도록 똑똑하게 설계되었습니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.24533" target="_blank">UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🤖 에이전트</span> 
</div>


화면을 스스로 조작하는 모바일 GUI 에이전트가 실패 경험으로부터 더 똑똑하게 학습하는 방법을 제안합니다. 복잡한 화면 조작 과정에서 보상이 적어 학습하기 어려웠던 문제를 두 단계의 자가 진화 시스템을 통해 효과적으로 해결했습니다.

<small>👤 Zichuan Lin, Feiyu Liu, Yijun Yang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.24472" target="_blank">Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🔍 추론/검색</span> 
</div>


LLM을 최적화하는 기법인 Self-distillation이 수학 문제 같은 복잡한 추론 과정에서 오히려 성능을 떨어뜨리는 이유를 분석했습니다. 모델이 학습 과정에서 스스로의 불확실성을 표현하는 과정을 생략하게 되면서 추론 능력이 저하된다는 흥미로운 결과를 보여줍니다.

<small>👤 Jeonghye Kim, Xufang Luo, Minbeom Kim</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.24458" target="_blank">OmniWeaving: Towards Unified Video Generation with Free-form Composition and Reasoning</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> 
</div>


다양한 작업을 하나의 시스템으로 매끄럽게 처리할 수 있는 오픈소스 기반의 통합형 비디오 생성 모델을 소개합니다. 강력한 멀티모달 구성 능력과 추론 기능을 결합하여, 기존 상용 모델에 뒤지지 않는 자유롭고 일관된 영상 생성을 가능하게 합니다.

<small>👤 Kaihang Pan, Qi Tian, Jianwei Zhang</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


Reddit, X, YouTube 등 다양한 플랫폼의 최신 정보를 한 번에 수집해주는 AI 에이전트 도구입니다. 원하는 주제만 입력하면 웹 전체를 꼼꼼하게 조사하여 근거가 확실한 깔끔한 요약본을 만들어줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Yeachan-Heo/oh-my-claudecode" target="_blank">Yeachan-Heo/oh-my-claudecode</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude Code를 활용해 팀 단위의 협업을 돕는 멀티 에이전트 관리 도구입니다. 여러 AI 에이전트들이 유기적으로 소통하고 협력할 수 있는 환경을 만들어 개발 생산성을 한층 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/deer-flow" target="_blank">bytedance/deer-flow</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


복잡한 자료 조사부터 코딩, 창작까지 스스로 수행하는 만능 AI 에이전트 시스템입니다. 샌드박스와 메모리, 다양한 도구를 적절히 활용해 몇 분에서 길게는 몇 시간이 걸리는 어려운 작업도 척척 해냅니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Vaibhavs10/insanely-fast-whisper" target="_blank">Vaibhavs10/insanely-fast-whisper</a></h3>



음성 인식 모델인 Whisper를 놀라운 속도로 실행할 수 있게 해주는 훌륭한 오픈소스 도구입니다. 아주 긴 오디오 파일도 빠르고 정확하게 텍스트로 변환할 수 있어 실무에서 유용하게 활용할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/agentscope-ai/agentscope" target="_blank">agentscope-ai/agentscope</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


개발자가 직접 내부 동작을 확인하고 쉽게 이해할 수 있는 투명한 AI 에이전트 구축 프레임워크입니다. 에이전트가 어떻게 판단하고 작동하는지 명확하게 파악할 수 있어 더욱 신뢰할 수 있는 시스템을 만들 수 있습니다.



</div>



---


## 📰 AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/476" target="_blank">AI News Weekly - Can you guess how much cash Open AI was losing with Sora? - Mar 26th 2026</a></h3>



AI의 윤리와 책임 소재를 다룬 주간 뉴스레터로, 최근 법적 공방과 빅테크 기업들의 흥미로운 동향을 조명합니다. 특히 OpenAI가 영상 생성 모델인 Sora를 유지하는 데 막대한 비용을 쓰다가 결국 조용히 서비스를 종료했다는 충격적인 소식을 전해줍니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Vision</code> <code>Agent</code> <code>LLM</code> <code>Fine-tuning</code> <code>Distillation</code> <code>RAG</code> <code>Multimodal</code> <code>AI Agent</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>