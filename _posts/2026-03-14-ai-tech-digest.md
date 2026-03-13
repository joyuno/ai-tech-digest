---
layout: post
title: "AI 기술 다이제스트 - 2026-03-14"
date: 2026-03-14
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---

> 🤖 AI 기술 트렌드를 자동으로 수집하고 요약한 다이제스트입니다.

---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12255" target="_blank">Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training</a></h3>



끊임없이 들어오는 비디오 스트림에서 공간 정보를 효과적으로 유지하고 업데이트하는 새로운 AI 모델을 제안합니다. 단순히 문맥 길이를 늘리는 대신 Test-Time Training (TTT) 기법을 활용하여 시각적 기반의 스트리밍 공간 지능을 크게 향상시켰습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12180" target="_blank">Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


멀티모달 에이전트가 복잡한 문서 작업에서 진짜 전략적으로 정보를 찾는지, 아니면 단순한 찍기로 찾는지 평가하는 MADQA 벤치마크를 소개합니다. 800개의 다양한 PDF 문서와 2,250개의 질문을 통해 에이전트의 실제 추론 능력을 정밀하게 측정할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12201" target="_blank">IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


긴 문맥을 다루는 LLM의 처리 속도를 높이고 비용을 줄이기 위해 Sparse Attention 과정을 가속화하는 IndexCache 기술을 제안합니다. 레이어 간의 인덱스를 재사용하는 방식을 통해 기존 인덱서가 가지고 있던 높은 연산 복잡도 문제를 효과적으로 해결했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.10178" target="_blank">Video-Based Reward Modeling for Computer-Use Agents</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


컴퓨터를 조작하는 AI 에이전트가 사용자의 명령을 제대로 수행했는지 화면 녹화 비디오를 통해 평가하는 보상 모델링을 연구했습니다. 에이전트의 내부 로직 대신 화면의 핵심 프레임 변화만으로 작업 성공 여부를 판단하여 복잡한 환경에서도 정확한 평가가 가능합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12257" target="_blank">DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning</a></h3>



여러 등장인물의 특징을 유지하면서 동시에 세밀한 움직임까지 제어할 수 있는 맞춤형 비디오 생성 프레임워크인 DreamVideo-Omni를 제안합니다. 기존 모델들이 겪던 모션 제어의 한계와 캐릭터 정체성 훼손 문제를 극복하여 훨씬 자연스러운 영상을 만들어냅니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12257" target="_blank">DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning</a></h3>



다양한 피사체의 정체성과 세밀한 움직임을 동시에 정밀하게 제어할 수 있는 DreamVideo-Omni 비디오 생성 프레임워크입니다. 기존 Diffusion 모델의 한계였던 피사체 변형 문제와 모션 제어의 모호성을 해결하여 고품질의 맞춤형 영상을 제작할 수 있게 해줍니다.

<small>👤 Yujie Wei, Xinyu Liu, Shiwei Zhang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12264" target="_blank">GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI의 이미지 편집 능력을 평가할 때 단순한 상식을 넘어 전문적인 학문 지식까지 반영할 수 있는 최초의 벤치마크 GRADE를 소개합니다. 10가지 학문 분야에 걸친 520개의 정교한 샘플을 통해 멀티모달 모델의 도메인 특화 추론 능력을 정확하게 측정해 줍니다.

<small>👤 Mingxin Liu, Ziqian Fan, Zhaokai Wang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12267" target="_blank">EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation</a></h3>



비디오를 토큰으로 변환할 때 영상의 복잡도에 따라 길이를 유연하게 조절하는 EVATok 기술입니다. 정적이거나 단순한 장면에서는 토큰을 아끼고 복잡한 장면에서는 더 할당하여 Autoregressive 비디오 생성 모델의 효율성과 품질을 모두 잡았습니다.

<small>👤 Tianwei Xiong, Jun Hao Liew, Zilong Huang</small>

</div>



---


## 👕 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/the-philosophy-ai-native-hiring-c002c2775b3a?source=rss----f107b03c406e---4" target="_blank">The Philosophy: AI Native Hiring</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


무신사에서 진행한 'AI 네이티브 엔지니어' 채용 과정과 그 이면에 담긴 철학을 소개하는 기술 블로그 글입니다. 수백 명의 지원자를 처음부터 끝까지 평가하는 자동화된 AI 파이프라인 구축기를 통해 새로운 세대의 개발자 채용 방식을 엿볼 수 있습니다.

<small>👤 Tao Kim</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/microsoft/BitNet" target="_blank">microsoft/BitNet</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> 
</div>


마이크로소프트에서 공식 제공하는 1-bit LLM 전용 추론 프레임워크입니다. 모델의 가중치를 극단적으로 압축하여 메모리 사용량을 크게 줄이면서도 빠른 처리 속도를 제공하도록 설계되었습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langflow-ai/openrag" target="_blank">langflow-ai/openrag</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> <span class="category-tag">💻 개발 도구</span> 
</div>


복잡한 설정 없이 하나의 패키지로 완성되는 포괄적인 RAG 플랫폼입니다. Langflow, Docling, Opensearch를 기반으로 구축되어 누구나 쉽게 강력한 AI 검색 및 문서 생성 시스템을 만들 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/lightpanda-io/browser" target="_blank">lightpanda-io/browser</a></h3>



AI 에이전트와 자동화 작업을 위해 특별히 설계된 초경량 헤드리스 브라우저입니다. 불필요한 리소스 낭비 없이 빠르고 효율적으로 웹 페이지를 탐색하고 데이터를 수집할 수 있도록 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/promptfoo/promptfoo" target="_blank">promptfoo/promptfoo</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🎯 신뢰성/안전</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


다양한 프롬프트와 AI 에이전트, RAG 시스템의 성능을 테스트하고 취약점을 찾아내는 평가 도구입니다. 간단한 설정만으로 여러 LLM의 성능을 한눈에 비교할 수 있으며 CI/CD 파이프라인과도 쉽게 연동됩니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/msitarzewski/agency-agents" target="_blank">msitarzewski/agency-agents</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


프론트엔드 개발부터 커뮤니티 관리까지 각기 다른 전문성을 가진 AI 에이전트들을 모아둔 종합 패키지입니다. 고유한 성격과 검증된 업무 프로세스를 갖춘 에이전트들을 활용해 나만의 가상 에이전시를 손쉽게 운영해 볼 수 있습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>Agent</code> <code>Eval</code> <code>DeepSeek</code> <code>Inference</code> <code>Reasoning</code> <code>Benchmark</code> <code>GPT</code> <code>Copilot</code> <code>LLM</code> 
</div>

---

<small>🤖 이 포스트는 <a href="https://github.com/joyuno/ai-tech-digest">AI Tech Digest</a>에 의해 자동 생성되었습니다.</small>