---
layout: post
title: "Spatial-TTT 스트리밍 시각 공간 지능"
date: 2026-03-16
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12255" target="_blank">Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training</a></h3>



끊임없이 이어지는 비디오 스트림에서 공간 정보를 효과적으로 선택하고 기억하는 방법을 제안하는 논문입니다. Test-Time Training(TTT)을 활용하여 AI가 실시간으로 시각적 공간 지능을 유지하고 업데이트할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12180" target="_blank">Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Multimodal Agent가 방대한 문서 속에서 진짜 전략적 추론을 하는지, 아니면 단순한 찍기(Stochastic Search)를 하는지 평가하는 논문입니다. 이를 위해 800개의 다양한 문서 기반으로 작성된 MADQA라는 새로운 벤치마크를 도입하여 Agent의 실제 문제 해결 능력을 측정합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.12201" target="_blank">IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


Long-context LLM의 추론 속도와 비용 문제를 해결하기 위해 Sparse Attention을 가속화하는 IndexCache 기술을 소개합니다. 레이어 간 인덱스를 재사용하는 방식으로 기존 인덱서의 높은 연산 복잡도를 줄여 모델의 효율성을 크게 높였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.10178" target="_blank">Video-Based Reward Modeling for Computer-Use Agents</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


컴퓨터 제어 Agent가 사용자의 지시를 제대로 수행했는지 평가하기 위해 실행 비디오 기반의 Reward Modeling을 연구한 논문입니다. 복잡한 화면 레이아웃과 미세한 시각적 단서들을 분석하여 Agent의 내부 추론 과정 없이도 작업 성공 여부를 판단할 수 있게 해줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.11421" target="_blank">ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation</a></h3>


<div class="categories">
<span class="category-tag">💻 개발 도구</span> 
</div>


텍스트 기반 비디오 생성 모델에서 영화처럼 자연스러운 다중 샷 카메라 제어를 가능하게 하는 새로운 패러다임을 제안합니다. 캡션, 카메라 궤적, 비디오 데이터를 유기적으로 연결하여 기존 프롬프트의 한계를 극복하고 정밀한 연출을 지원합니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12257" target="_blank">DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning</a></h3>



여러 피사체가 등장하는 비디오 생성 시 각 캐릭터의 정체성을 유지하면서도 세밀한 움직임을 제어할 수 있는 DreamVideo-Omni 프레임워크입니다. 잠재 정체성 강화 학습(Latent Identity Reinforcement Learning)을 통해 기존 모델들의 제어 모호성과 화질 저하 문제를 효과적으로 해결했습니다.

<small>👤 Yujie Wei, Xinyu Liu, Shiwei Zhang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12264" target="_blank">GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI 모델이 단순한 상식을 넘어 전문적인 학문 지식을 바탕으로 이미지를 편집할 수 있는지 평가하는 GRADE 벤치마크를 소개합니다. 10개의 다양한 학문 분야에 걸쳐 세심하게 구성된 520개의 샘플을 통해 Multimodal 모델의 고도화된 추론 능력을 측정합니다.

<small>👤 Mingxin Liu, Ziqian Fan, Zhaokai Wang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.12267" target="_blank">EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation</a></h3>



비디오의 복잡도에 따라 토큰 길이를 유연하게 조절하여 Autoregressive(AR) 비디오 생성의 효율성을 극대화하는 EVATok 기술입니다. 정적이거나 단순한 장면에서는 토큰 낭비를 줄이고, 역동적인 장면에는 더 많은 토큰을 할당하여 연산 비용과 생성 품질의 균형을 맞췄습니다.

<small>👤 Tianwei Xiong, Jun Hao Liew, Zilong Huang</small>

</div>



---


## 👕 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%ED%9E%98%EC%84%B8%EA%B3%A0-%EA%B0%95%ED%95%9C-%EC%95%84%EC%B9%A8-%EC%9D%84-%EB%84%98%EC%96%B4-gpt-4o-mini%EB%A5%BC-%EB%8C%80%EC%B2%B4%ED%95%A0-translategemma-%EC%8B%A4%ED%97%98%EA%B8%B0-a670cc318cb7?source=rss----f107b03c406e---4" target="_blank">“힘세고 강한 아침”을 넘어: GPT-4o-mini를 대체할 TranslateGemma 실험기</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


무신사 백엔드 개발자가 상용 LLM의 어색한 직역 문제를 해결하기 위해 On-Premise 번역 모델인 TranslateGemma를 도입한 생생한 실험기입니다. 단순한 번역 품질 개선을 넘어, 실제 서비스 운영 환경에서 발생할 수 있는 리스크를 줄이고 안정적인 시스템을 구축하는 과정이 담겨 있습니다.

<small>👤 Yang Chisoo</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/lightpanda-io/browser" target="_blank">lightpanda-io/browser</a></h3>



AI Agent와 자동화 작업을 위해 특별히 설계된 빠르고 가벼운 Headless 브라우저입니다. 복잡한 웹 스크래핑이나 AI의 웹 탐색 능력을 향상시키는 데 유용하게 활용될 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Crosstalk-Solutions/project-nomad" target="_blank">Crosstalk-Solutions/project-nomad</a></h3>



언제 어디서나 사용할 수 있는 오프라인 기반의 자급자족형 생존 컴퓨터 프로젝트입니다. 인터넷 연결 없이도 필수 도구와 지식, 그리고 AI 기능을 제공하여 위기 상황에서도 사용자를 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/volcengine/OpenViking" target="_blank">volcengine/OpenViking</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


AI Agent가 필요로 하는 메모리와 리소스를 파일 시스템 방식으로 통합 관리해 주는 오픈소스 컨텍스트 데이터베이스입니다. 이를 통해 Agent는 계층적으로 컨텍스트를 전달받으며 스스로 진화할 수 있는 환경을 갖추게 됩니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/shareAI-lab/learn-claude-code" target="_blank">shareAI-lab/learn-claude-code</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


기초부터 직접 구축해 볼 수 있는 초소형 Claude Code 스타일의 AI Agent 오픈소스입니다. Bash 환경만으로도 강력한 코딩 보조 Agent를 구현하는 방법을 배울 수 있어 교육용으로 아주 훌륭합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/shanraisshan/claude-code-best-practice" target="_blank">shanraisshan/claude-code-best-practice</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> 
</div>


Claude Code를 더욱 완벽하고 효율적으로 사용하기 위한 다양한 모범 사례와 팁들을 모아둔 레포지토리입니다. AI 기반 코딩 도구를 실무에 바로 적용하고 싶은 개발자들에게 유용한 가이드가 됩니다.



</div>



---


## 📰 AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/472" target="_blank">AI News Weekly - 100 years from now : Future lost in transation - Mar 15th 2026</a></h3>



지금 우리가 만드는 AI 기술들이 100년 후 일상에 어떤 영향을 미칠지 상상해 보는 흥미로운 주간 뉴스레터입니다. 기계의 언어를 더 이상 인간이 온전히 이해하지 못하게 되었을 때 발생할 수 있는 사회적 변화와 철학적 고민을 다룹니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>Agent</code> <code>Eval</code> <code>DeepSeek</code> <code>Inference</code> <code>Reasoning</code> <code>Prompt</code> <code>Benchmark</code> <code>GPT</code> <code>AI Agent</code> 
</div>

---

