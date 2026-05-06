---
layout: post
title: "Sparse Autoencoder, 정말 random baseline을 이기는가"
date: 2026-02-19
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.14111" target="_blank">Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


신경망 해석을 위해 사용되는 Sparse Autoencoders (SAE)가 실제로 무작위 베이스라인보다 더 의미 있는 특징을 찾아내는지 검증한 연구입니다. 최근 SAE의 효과에 대한 의문이 제기됨에 따라, 체계적인 평가를 통해 이 기술이 정말로 유효한지 꼼꼼하게 따져보았습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.13949" target="_blank">Experiential Reinforcement Learning</a></h3>



언어 모델이 지연되고 희소한 피드백 환경에서도 잘 학습할 수 있도록 돕는 Experiential Reinforcement Learning (ERL)을 제안합니다. 경험, 성찰, 통합의 과정을 거치는 루프를 통해 모델이 과거의 실패로부터 더 나은 행동을 스스로 학습하도록 설계했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.10809" target="_blank">DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


단순한 이미지 매칭을 넘어, 시각적 히스토리 내의 맥락까지 고려하는 DeepImageSearch라는 새로운 검색 패러다임을 소개합니다. 에이전트가 시간적 흐름과 의존성을 파악하여 자율적으로 필요한 정보를 탐색하고 찾아내는 능력을 갖추게 됩니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.12670" target="_blank">SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


LLM 에이전트의 성능을 높여주는 'Agent Skills'가 실제로 얼마나 효과적인지 측정하는 SkillsBench 벤치마크를 공개했습니다. 11개 도메인의 다양한 작업에서 큐레이팅된 스킬과 자체 생성 스킬을 비교 평가하여 에이전트의 능력 향상 여부를 검증합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.15763" target="_blank">GLM-5: from Vibe Coding to Agentic Engineering</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


Vibe Coding에서 Agentic Engineering으로의 전환을 이끄는 차세대 파운데이션 모델 GLM-5를 발표했습니다. 추론과 코딩 능력을 대폭 강화하고 새로운 비동기 RL 인프라를 적용하여, 비용 효율성과 모델의 자율성을 동시에 잡았습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ibm-research/itbenchandmast" target="_blank">IBM and UC Berkeley Diagnose Why Enterprise Agents Fail Using IT-Bench and MAST</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


IBM과 UC Berkeley가 협력하여 기업용 에이전트가 실패하는 주된 원인을 심층 분석한 리포트입니다. IT-Bench와 MAST라는 평가 도구를 활용해 엔터프라이즈 환경에서 AI 에이전트가 겪는 실질적인 문제점과 해결책을 진단했습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/gradio-html-one-shot-apps" target="_blank">One-Shot Any Web App with Gradio's gr.HTML</a></h3>



Gradio의 `gr.HTML` 컴포넌트를 활용해 복잡한 과정 없이 단번에 웹 애플리케이션을 구현하는 방법을 소개합니다. Python 코드만으로도 유연하고 강력한 웹 인터페이스를 손쉽게 만들 수 있는 유용한 팁을 담고 있습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/nemotron-nano-9b-v2-japanese-ja" target="_blank">NVIDIA Nemotron 2 Nano 9B Japanese: 日本のソブリンAIを支える最先端小規模言語モデル</a></h3>



NVIDIA가 일본의 Sovereign AI 전략을 지원하기 위해 공개한 일본어 특화 소형 언어 모델입니다. 9B 파라미터 사이즈로 가볍지만 강력한 성능을 제공하여, 일본어 관련 다양한 로컬 AI 서비스에 활용하기 좋습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/alibaba/zvec" target="_blank">alibaba/zvec</a></h3>



알리바바에서 공개한 초경량, 초고속 인프로세스(In-process) 벡터 데이터베이스입니다. 별도의 무거운 서버 구축 없이 애플리케이션 내부에서 바로 빠르고 간편하게 벡터 검색 기능을 구현할 수 있어 효율적입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/p-e-w/heretic" target="_blank">p-e-w/heretic</a></h3>



언어 모델에 적용된 검열을 자동으로 제거하여 모델이 답변을 거부하지 않도록 조정하는 도구입니다. 사용자가 원하는 답변을 자유롭게 얻을 수 있게 해주지만, 윤리적인 사용에 대해서는 주의가 필요한 프로젝트입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/QwenLM/qwen-code" target="_blank">QwenLM/qwen-code</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


개발자의 터미널 환경에 상주하며 코딩 작업을 돕는 오픈소스 AI 에이전트입니다. 자연어 명령만으로 복잡한 작업을 수행하거나 코드를 작성해 주어, 터미널을 떠나지 않고도 생산성을 크게 높일 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/NirDiamant/RAG_Techniques" target="_blank">NirDiamant/RAG_Techniques</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Retrieval-Augmented Generation (RAG) 시스템을 구축할 때 필요한 다양한 고급 기술들을 한곳에 모은 저장소입니다. 검색의 정확도를 높이고 생성 모델의 답변 품질을 향상시키는 실전 기법과 예제 코드를 학습하기 좋습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/HailToDodongo/pyrite64" target="_blank">HailToDodongo/pyrite64</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


libdragon과 tiny3d 라이브러리를 기반으로 한 닌텐도 64(N64)용 게임 엔진 및 에디터입니다. 레트로 게임 개발에 관심 있는 분들이 실제 N64 하드웨어에서 구동되는 게임을 쉽게 제작할 수 있도록 돕습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Eval</code> <code>Multimodal</code> <code>LoRA</code> <code>Retrieval</code> <code>Agent</code> <code>LLM</code> <code>Inference</code> <code>Reasoning</code> <code>Alignment</code> <code>AI Agent</code> 
</div>

---

