---
layout: post
title: "AI 기술 다이제스트 - 2026-03-15"
date: 2026-03-15
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12255" target="_blank">Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training</a></h3>



이 논문은 비디오 스트림에서 공간 정보를 효과적으로 처리하는 Spatial-TTT 모델을 제안합니다. Test-Time Training (TTT)을 활용해 끊임없이 들어오는 시각 데이터 속에서 중요한 공간 지식을 실시간으로 선택하고 유지할 수 있어요. AI의 공간 인지 능력을 한 단계 높여주는 유용한 기술입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12180" target="_blank">Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


멀티모달 에이전트가 복잡한 문서에서 단순히 찍기식 검색을 하는지, 아니면 진짜 전략적인 추론을 하는지 평가하는 MADQA 벤치마크를 소개합니다. 800개의 다양한 PDF 문서와 2,250개의 질문을 바탕으로 AI의 실제 문서 분석 능력을 꼼꼼하게 측정할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12201" target="_blank">IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


긴 문맥을 처리할 때 Sparse Attention의 계산 효율성을 극대화하는 IndexCache 기술을 제안합니다. 레이어 간 인덱스 재사용을 통해 기존 모델들의 인덱서 병목 현상을 해결하여, AI 모델의 추론 속도를 높이고 서빙 비용을 크게 줄일 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.10178" target="_blank">Video-Based Reward Modeling for Computer-Use Agents</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


컴퓨터 사용 에이전트(CUA)가 사용자 명령을 제대로 수행했는지 평가하기 위해 비디오 기반의 보상 모델링을 연구한 논문입니다. 에이전트의 내부 로직이 아닌 실제 실행 화면의 Keyframe들을 분석하여, 복잡한 화면 속에서도 AI의 행동을 정확히 채점할 수 있는 방법을 제시해요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.11421" target="_blank">ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


텍스트를 기반으로 영화 같은 다중 샷 비디오를 만들 때, 카메라 움직임을 정밀하게 제어할 수 있는 ShotVerse 기술을 소개합니다. 텍스트와 카메라 궤적, 비디오 데이터를 함께 묶어서 학습하는 새로운 패러다임으로 기존 생성 모델들의 제어 한계를 극복했어요.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12257" target="_blank">DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning</a></h3>



동영상 생성 과정에서 여러 등장인물의 특징을 유지하면서 움직임을 정교하게 제어하는 DreamVideo-Omni 프레임워크입니다. Latent Identity 강화 학습을 도입해 캐릭터 붕괴 문제를 해결하며, 더욱 자연스럽고 완성도 높은 맞춤형 비디오를 만들 수 있게 해줘요.

<small>👤 Yujie Wei, Xinyu Liu, Shiwei Zhang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12264" target="_blank">GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


단순한 일상 이미지를 넘어, 학문적이고 전문적인 지식이 필요한 이미지 편집 능력을 평가하는 GRADE 벤치마크를 공개했습니다. 10개의 다양한 학문 분야에 걸쳐 까다롭게 선별된 데이터를 통해 AI 모델의 깊이 있는 지식 추론 능력을 테스트할 수 있어요.

<small>👤 Mingxin Liu, Ziqian Fan, Zhaokai Wang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12267" target="_blank">EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation</a></h3>



비디오 생성 모델의 효율성을 높이기 위해 영상의 복잡도에 따라 토큰 길이를 조절하는 EVATok 기술을 제안합니다. 움직임이 없는 단순한 구간에서는 토큰을 아끼고 복잡한 구간에 집중하여, 화질은 유지하면서도 연산 비용을 획기적으로 줄여줍니다.

<small>👤 Tianwei Xiong, Jun Hao Liew, Zilong Huang</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/volcengine/OpenViking" target="_blank">volcengine/OpenViking</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


AI 에이전트를 위해 특별히 설계된 오픈소스 컨텍스트 데이터베이스인 OpenViking입니다. 친숙한 파일 시스템 방식을 사용해 에이전트의 메모리, 리소스, 스킬 등을 효율적으로 계층화하여 관리하고 스스로 진화할 수 있는 환경을 제공해요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/anthropics/claude-plugins-official" target="_blank">anthropics/claude-plugins-official</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Anthropic이 직접 관리하고 제공하는 Claude Code Plugin들의 공식 디렉토리입니다. 검증된 고품질 플러그인들을 모아두어, 개발자들이 Claude를 더욱 강력하고 확장성 있게 활용할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/p-e-w/heretic" target="_blank">p-e-w/heretic</a></h3>



언어 모델(LLM)에 적용된 자체 검열 기능을 완전히 자동으로 제거해 주는 강력한 오픈소스 도구입니다. 모델의 안전 필터를 우회하여 제약 없이 더욱 자유로운 답변을 생성할 수 있도록 지원해요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langflow-ai/openrag" target="_blank">langflow-ai/openrag</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Langflow, Docling, Opensearch를 하나로 결합하여 만든 종합 RAG 플랫폼입니다. 단일 패키지 형태로 제공되어 복잡한 설정 없이도 강력한 Retrieval-Augmented Generation 시스템을 쉽게 구축할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/lightpanda-io/browser" target="_blank">lightpanda-io/browser</a></h3>



AI와 자동화 시스템이 웹과 매끄럽게 상호작용할 수 있도록 설계된 Headless 브라우저입니다. 가볍고 빠른 성능을 자랑하며, AI 에이전트가 웹 문서를 수집하거나 자동화 작업을 수행하는 데 최적화되어 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>Agent</code> <code>Eval</code> <code>DeepSeek</code> <code>Inference</code> <code>Reasoning</code> <code>Prompt</code> <code>Benchmark</code> <code>AI Agent</code> <code>Claude</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>