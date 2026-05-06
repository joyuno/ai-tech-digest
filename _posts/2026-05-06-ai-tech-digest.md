---
layout: post
title: "MolmoAct2 실세계 행동추론 모델"
date: 2026-05-06
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
---


---


## 📚 arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2605.02881" target="_blank">MolmoAct2: Action Reasoning Models for Real-world Deployment</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🎯 신뢰성/안전</span> 
</div>


현재 비전-언어-행동(VLA) 모델은 실제 로봇 환경에 적용하기에는 폐쇄적인 구조, 비싼 하드웨어, 높은 지연 시간 등 여러 한계가 있습니다. 이를 해결하기 위해 MolmoAct2는 실용적인 배포를 목표로 개발된 완전한 오픈소스 행동 추론 모델로, 기존 시스템의 단점을 극복하고자 합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.27660" target="_blank">From Context to Skills: Can Language Models Learn from Context Skillfully?</a></h3>


<div class="categories">
<span class="category-tag">🔍 추론/검색</span> 
</div>


언어 모델이 복잡한 맥락 속에서 필요한 지식을 학습하는 '컨텍스트 학습'은 많은 실제 과제 해결에 필수적입니다. 이 논문은 컨텍스트에서 규칙과 절차를 '스킬' 형태로 추출하여 활용하는 방식의 어려움을 지적하며, 수동적인 스킬 생성의 높은 비용 문제를 해결하기 위한 방안을 탐구합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.27221" target="_blank">Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> 
</div>


현재의 에이전트 기반 웹 검색 시스템은 단일 주제에 대한 깊이 있는 추론과 여러 소스에 걸친 구조화된 정보 수집이라는 두 가지 요구를 동시에 충족시키기 어렵습니다. Web2BigTable은 이러한 문제를 해결하기 위해 제안된 멀티 에이전트 프레임워크로, 웹에서 정보를 검색하고 이를 테이블 형태로 구조화하여 깊이와 넓이를 모두 아우르는 검색을 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.28123" target="_blank">Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🎯 신뢰성/안전</span> 
</div>


대규모 멀티모달 모델(LMM)의 표준 학습 방식인 지도 미세조정(SFT) 후 강화학습(RL)을 적용하는 과정은 모델의 원래 성능을 저해하는 분포 변화 문제를 야기합니다. 이 논문은 SFT와 RL 사이에 '사전 정렬' 단계를 도입하여 이러한 문제를 완화하는 새로운 접근법을 제시하며, 특히 멀티모달 추론에서 발생하는 오류를 줄이는 것을 목표로 합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.28075" target="_blank">Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling</a></h3>



독일어와 같은 비영어권 언어 모델을 학습시킬 때, 방대한 웹 데이터를 필터링하는 과정에서 데이터의 다양성을 우선할지, 아니면 고품질 데이터를 반복 학습하여 품질을 우선할지에 대한 딜레마가 존재합니다. 이 연구는 독일어 데이터를 대상으로 실험한 결과, 엄격한 필터링을 통해 고품질 핵심 데이터를 추출하고 이를 여러 에포크에 걸쳐 반복 학습하는 것이 더 효율적이라는 결론을 내렸습니다.



</div>



---


## 🤗 Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2605.04012" target="_blank">SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


기존 언어 모델은 풍부한 정보가 주어진 복잡한 의료 사례 진단에 뛰어난 성능을 보였지만, 이는 환자가 직접 증상을 설명하는 현실과는 거리가 있습니다. SymptomAI는 이러한 한계를 극복하고자 개발된 대화형 AI 에이전트로, Fitbit 앱을 통해 사용자의 증상을 직접 듣고 감별 진단을 수행하는 것을 목표로 합니다.

<small>👤 Joseph Breda, Fadi Yousif, Beszel Hawkins</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2605.04036" target="_blank">OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> <span class="category-tag">🤖 에이전트</span> 
</div>


첨단 LLM 에이전트의 핵심 역량인 딥서치 기능 개발은 막대한 자원이 필요한 복잡한 파이프라인 때문에 주로 거대 기업들이 주도해왔습니다. 하지만 이 연구는 정보 가치가 높고 난이도 있는 데이터를 활용하면, 단순한 지도 미세조정(SFT) 방식만으로도 놀라울 만큼 뛰어난 검색 에이전트를 만들 수 있음을 보여줍니다.

<small>👤 Yuwen Du, Rui Ye, Shuo Tang</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2605.03849" target="_blank">Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔧 학습/최적화</span> 
</div>


스트리밍 비디오 생성 모델의 속도를 높이는 증류 기법은 모든 학습 데이터를 동일하게 신뢰하는 기존 방식 때문에 성능 향상에 한계가 있었습니다. Stream-R1은 데이터의 신뢰도와 복잡도를 함께 고려하는 새로운 보상 증류 방식을 제안하여, 더 효율적이고 높은 품질의 비디오 생성 모델을 구현합니다.

<small>👤 Bin Wu, Mengqi Huang, Shaojin Wu</small>

</div>



---


## ⭐ GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/Hmbown/DeepSeek-TUI" target="_blank">Hmbown/DeepSeek-TUI</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🤖 에이전트</span> 
</div>


DeepSeek 모델을 위한 코딩 에이전트를 터미널 환경에서 실행할 수 있는 도구입니다. 이 프로젝트를 통해 개발자는 익숙한 터미널에서 바로 AI의 코딩 지원을 받을 수 있어 작업 효율을 높일 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/ruvnet/ruflo" target="_blank">ruvnet/ruflo</a></h3>


<div class="categories">
<span class="category-tag">🧠 모델/아키텍처</span> <span class="category-tag">🔍 추론/검색</span> <span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


Claude 모델을 위한 선도적인 에이전트 오케스트레이션 플랫폼입니다. 지능형 다중 에이전트 시스템을 배포하고 자율적인 워크플로우를 조정하여 정교한 대화형 AI 시스템을 구축할 수 있으며, RAG 통합과 같은 엔터프라이즈급 기능을 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bwya77/vscode-dark-islands" target="_blank">bwya77/vscode-dark-islands</a></h3>



easemate IDE와 Jetbrains의 islands 테마에서 영감을 받아 제작된 VSCode용 다크 테마입니다. 사용자에게 익숙하면서도 세련된 코드 편집기 환경을 제공하여 가독성과 개발 집중도를 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/mksglu/context-mode" target="_blank">mksglu/context-mode</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> <span class="category-tag">💻 개발 도구</span> 
</div>


AI 코딩 에이전트의 컨텍스트 창을 최적화하는 기술입니다. 도구의 출력 결과를 샌드박스 환경에서 처리하여 컨텍스트 크기를 98%까지 줄여주며, 이를 통해 LLM의 토큰 사용량을 절감하고 응답 속도를 개선합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/msitarzewski/agency-agents" target="_blank">msitarzewski/agency-agents</a></h3>


<div class="categories">
<span class="category-tag">🤖 에이전트</span> 
</div>


마치 하나의 완전한 AI 에이전시처럼 작동하는 에이전트 모음입니다. 프론트엔드 전문가부터 커뮤니티 관리자까지, 각 에이전트는 고유한 개성과 전문성을 가지고 특정 역할을 수행하도록 설계되었습니다.



</div>



---



## 📊 오늘의 키워드

<div class="keywords">
<code>Vision</code> <code>Grounding</code> <code>Inference</code> <code>LLM</code> <code>RAG</code> <code>Agent</code> <code>Multimodal</code> <code>Fine-tuning</code> <code>Alignment</code> <code>AI Agent</code> 
</div>

---

