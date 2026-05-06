---
layout: post
title: "AI Tech - 2026-03-29"
date: 2026-03-29
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25728" target="_blank">PixelSmile: Toward Fine-Grained Facial Expression Editing</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


이 논문은 자연스럽고 세밀하게 얼굴 표정을 편집할 수 있는 PixelSmile이라는 Diffusion 프레임워크를 소개합니다. 표정 데이터의 한계를 극복하기 위해 새로운 전용 데이터셋을 구축하고, 모델 성능을 꼼꼼하게 평가할 수 있는 벤치마크도 함께 제공해요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25040" target="_blank">Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


1조 개의 파라미터를 자랑하는 세계 최초의 과학 분야 특화 멀티모달 Foundation Model인 Intern-S1-Pro를 소개합니다. 뛰어난 추론 능력과 강화된 Agent 기능을 바탕으로 100개가 넘는 전문적인 과학 작업들을 훌륭하게 수행할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.24440" target="_blank">CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


PC를 자동 제어하는 Computer-use agents(CUAs)의 원활한 학습을 위해 사람이 직접 주석을 단 대규모 비디오 데이터셋을 구축했습니다. 기존의 단순한 스크린샷이 가진 한계를 벗어나, 연속적이고 고품질인 비디오 데이터를 제공하여 Agent 성능을 크게 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.24800" target="_blank">Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


Diffusion Transformers(DiTs)의 이미지 생성 능력을 극대화하는 파라미터 효율적인 보정 방식인 Calibri를 제안합니다. 복잡한 수정 없이 학습 가능한 단 하나의 스케일링 파라미터만 추가해도 생성 품질이 눈에 띄게 향상되는 것을 확인할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.25502" target="_blank">RealRestorer: Towards Generalizable Real-World Image Restoration with Large-Scale Image Editing Models</a></h3>



다양한 현실 환경에서 훼손된 이미지를 실제처럼 복원해주는 범용적인 이미지 복원 모델인 RealRestorer를 소개합니다. 대규모 이미지 편집 모델이 가진 강력한 일반화 능력을 활용해, 기존 학습 데이터의 한계를 뛰어넘는 놀라운 복원 퀄리티를 보여줍니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.25746" target="_blank">ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


긴 스토리텔링에 필수적인 멀티 숏 비디오 생성을 위해 사용자와 상호작용이 가능한 ShotStream 아키텍처를 제안합니다. 사용자가 프롬프트를 통해 실시간으로 이야기를 지시하면, 이전 문맥에 맞춰 빠르고 자연스럽게 다음 비디오 장면을 만들어내요.

<small>👤 Yawen Luo, Xiaoyu Shi, Junhao Zhuang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.25745" target="_blank">Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting</a></h3>



기존 3D Gaussian Splatting의 해상도 한계를 극복하여 4K 고화질 생성을 가능하게 하는 프레임워크입니다. 가우시안 개수를 기하급수적으로 늘리는 대신 개별 텍스처를 결합하는 방식을 사용하여, 복잡한 연산 부담을 획기적으로 줄여줍니다.

<small>👤 Yixing Lao, Xuyang Bai, Xiaoyang Wu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.25744" target="_blank">MuRF: Unlocking the Multi-Scale Potential of Vision Foundation Models</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Vision Foundation Models(VFMs)이 추론 시 단일 해상도만 사용하는 한계를 극복하기 위해 새로운 멀티 스케일 접근법을 제안합니다. 저해상도의 전체적인 맥락과 고해상도의 섬세한 디테일을 동시에 활용하여 모델의 시각적 인지 능력을 대폭 끌어올렸어요.

<small>👤 Bocheng Zou, Mu Cai, Mark Stanley</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/SakanaAI/AI-Scientist-v2" target="_blank">SakanaAI/AI-Scientist-v2</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


트리 탐색 기반의 Agent 기능을 통해 워크샵 수준의 과학적 발견을 자동화해 주는 AI-Scientist-v2 프로젝트입니다. AI가 스스로 연구 아이디어를 찾고 발전시킬 수 있는 혁신적인 도구예요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/onyx-dot-app/onyx" target="_blank">onyx-dot-app/onyx</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


거의 모든 LLM과 연동하여 사용할 수 있는 강력한 기능의 오픈소스 AI 채팅 플랫폼입니다. 다양한 고급 기능을 지원하여 누구나 쉽게 맞춤형 AI 챗봇 환경을 구축하고 활용할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/datalab-to/chandra" target="_blank">datalab-to/chandra</a></h3>



복잡한 표나 양식, 심지어 손글씨까지 원래의 문서 레이아웃 그대로 완벽하게 인식하는 강력한 OCR 모델입니다. 문서의 구조를 훼손하지 않고 깔끔하게 텍스트 데이터를 추출할 때 매우 유용하게 쓰일 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/agentscope-ai/agentscope" target="_blank">agentscope-ai/agentscope</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


시각적으로 작동 과정을 확인하고 신뢰할 수 있는 투명한 AI Agent를 구축할 수 있는 오픈소스 프레임워크입니다. 개발자가 Agent의 내부 판단 과정을 쉽게 이해하고 안정적으로 제어할 수 있도록 도와줘요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/SakanaAI/AI-Scientist-v2" target="_blank">SakanaAI/AI-Scientist-v2</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


트리 탐색 기반의 Agent 기능을 통해 워크샵 수준의 과학적 발견을 자동화해 주는 AI-Scientist-v2 프로젝트입니다. AI가 스스로 연구 아이디어를 탐색하고 논문 작성까지 돕는 혁신적인 연구 워크플로우를 제공해요.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Eval</code> <code>Multimodal</code> <code>Agent</code> <code>Transformer</code> <code>Prompt</code> <code>Vision</code> <code>Inference</code> <code>LLM</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>