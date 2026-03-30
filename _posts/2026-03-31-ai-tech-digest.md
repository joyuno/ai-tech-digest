---
layout: post
title: "AI 기술 다이제스트 - 2026-03-31"
date: 2026-03-31
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25716" target="_blank">Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models</a></h3>



이 논문은 비디오 World Model에서 동적 객체가 화면 밖으로 사라졌다가 다시 나타날 때 발생하는 왜곡 현상을 해결합니다. 정적인 배경을 기억하면서도 움직이는 객체를 지속적으로 추적하는 새로운 Hybrid Memory 방식을 제안하여 일관된 영상 생성 성능을 보여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25040" target="_blank">Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


1조 개의 파라미터를 갖춘 세계 최초의 과학 분야 멀티모달 Foundation Model인 Intern-S1-Pro를 소개합니다. 강력한 추론 및 이미지-텍스트 이해 능력을 바탕으로 100개 이상의 전문 과학 작업을 완벽하게 수행하며, 고급 Agent 기능까지 지원하여 과학 연구에 큰 도움을 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25728" target="_blank">PixelSmile: Toward Fine-Grained Facial Expression Editing</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


기존 얼굴 표정 편집 모델들의 한계를 극복하기 위해 세밀한 감정 표현이 가능한 새로운 데이터셋과 평가 지표를 구축했습니다. 이를 바탕으로 개인의 고유한 얼굴 특징을 유지하면서도 자연스럽고 정교하게 표정만 바꿔주는 새로운 Diffusion 프레임워크인 PixelSmile을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25746" target="_blank">ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


긴 서사의 스토리텔링 영상을 생성할 때 발생하는 지연 시간을 줄이고 사용자와의 상호작용을 높이는 새로운 비디오 생성 아키텍처입니다. 이전 영상의 맥락을 바탕으로 다음 장면을 실시간으로 생성해 내며, 사용자가 프롬프트를 통해 이야기 흐름을 즉각적으로 바꿀 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.24800" target="_blank">Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


Diffusion Transformer(DiT)의 생성 능력을 극대화하기 위해 적은 파라미터만으로 모델을 최적화하는 Calibri라는 새로운 기법을 소개합니다. 노이즈 제거 과정을 세밀하게 분석하여 단일 스케일링 파라미터를 추가하는 것만으로도 이미지 생성 품질을 크게 높일 수 있습니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.26664" target="_blank">Learning to Commit: Generating Organic Pull Requests via Online Repository Memory</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


LLM 기반 코딩 Agent가 기능적으로는 올바르지만 기존 프로젝트의 규칙이나 내부 API를 무시해서 PR이 거부되는 현상을 분석했습니다. 모델이 프로젝트 코드를 단순히 읽는 것을 넘어 실제 개발자처럼 유기적이고 자연스러운 코드를 작성할 수 있도록 돕는 온라인 저장소 메모리 방식을 제안합니다.

<small>👤 Mo Li, L. H. Xu, Qitai Tan</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.26658" target="_blank">Zero-Shot Depth from Defocus</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


초점이 다른 여러 장의 사진(포커스 스택)에서 깊이 정보를 추출할 때, 처음 보는 데이터에서도 잘 작동하도록 Zero-Shot 일반화에 집중한 연구입니다. 기존보다 훨씬 크고 정밀한 새로운 벤치마크 데이터셋을 구축하고, 이에 최적화된 Transformer 기반의 혁신적인 네트워크 구조를 선보입니다.

<small>👤 Yiming Zuo, Hongyu Wen, Venkat Subramanian</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.26362" target="_blank">HandVQA: Diagnosing and Improving Fine-Grained Spatial Reasoning about Hands in Vision-Language Models</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Vision-Language Model(VLM)이 복잡한 인간의 손동작과 미세한 공간 정보를 얼마나 잘 이해하는지 평가하는 대규모 벤치마크를 소개합니다. 로봇 수술이나 AR/VR처럼 정밀한 손동작 인식이 필수적인 분야에서 AI의 성능을 진단하고 개선하는 데 유용하게 활용될 수 있습니다.

<small>👤 MD Khalequzzaman Chowdhury Sayem, Mubarrat Tajoar Chowdhury, Yihalem Yimolal Tiruneh</small>

</div>



---


## 👕 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%ED%9B%84%EA%B8%B0-10%EB%A7%8C-%EA%B0%9C-%EB%8B%A4-%EC%9D%BD%EA%B3%A0-%EA%B3%84%EC%8B%A0%EA%B0%80%EC%9A%94-ai-%ED%9B%84%EA%B8%B0-%EC%9A%94%EC%95%BD-%EA%B8%B0%EB%8A%A5-%EB%8F%84%EC%9E%85%EA%B8%B0-9efff4b12783?source=rss----f107b03c406e---4" target="_blank">후기 10만 개, 다 읽고 계신가요? - AI 후기 요약 기능 도입기</a></h3>



수십만 개가 넘는 상품 후기 속에서 고객이 원하는 정보만 빠르게 찾을 수 있도록 무신사에 AI 후기 요약 기능을 도입한 과정을 담은 글입니다. 기획 단계에서의 문제 정의부터 엔지니어링 측면의 기술적 고민과 해결책까지 실무진들의 생생한 경험담을 읽어볼 수 있습니다.

<small>👤 박소정</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/microsoft/VibeVoice" target="_blank">microsoft/VibeVoice</a></h3>



마이크로소프트에서 공개한 최첨단 오픈소스 음성 AI 프로젝트입니다. 사람의 목소리와 감정을 섬세하게 표현하는 고품질 음성 인식 및 생성 기능을 제공하여 다양한 애플리케이션에 활용할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/luongnv89/claude-howto" target="_blank">luongnv89/claude-howto</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude Code의 기본 개념부터 고급 Agent 활용법까지 시각적인 예제와 함께 쉽게 설명해 주는 실전 가이드입니다. 실무에 바로 복사해서 쓸 수 있는 유용한 템플릿들이 가득해 코딩 생산성을 크게 높일 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/shanraisshan/claude-code-best-practice" target="_blank">shanraisshan/claude-code-best-practice</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


AI 코딩 어시스턴트인 Claude를 가장 효율적으로 활용하기 위한 모범 사례(Best Practice)들을 모아둔 저장소입니다. 다양한 실무 상황에서 프롬프트를 어떻게 작성해야 최적의 코드를 얻을 수 있는지에 대한 유용한 팁을 제공합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/OpenBB-finance/OpenBB" target="_blank">OpenBB-finance/OpenBB</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


금융 분석가와 퀀트 투자자, 그리고 AI Agent를 위해 설계된 강력한 오픈소스 금융 데이터 플랫폼입니다. 전 세계의 다양한 금융 API를 하나로 통합하여 복잡한 시장 데이터를 쉽고 빠르게 분석할 수 있도록 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/sherlock-project/sherlock" target="_blank">sherlock-project/sherlock</a></h3>



특정 사용자 이름(Username) 하나만으로 전 세계 수백 개의 소셜 미디어 플랫폼을 검색해 동일한 계정을 찾아내는 흥미로운 오픈소스 도구입니다. 복잡한 설정 없이 터미널에서 간단한 명령어만으로 강력한 정보 수집 기능을 사용할 수 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>Agent</code> <code>Eval</code> <code>Prompt</code> <code>Transformer</code> <code>LLM</code> <code>Benchmark</code> <code>Vision</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>