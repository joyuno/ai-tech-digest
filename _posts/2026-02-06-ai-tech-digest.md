---
layout: post
title: "무신사 풀필먼트, Jenkins에서 Temporal로 갈아탄 이유"
date: 2026-02-06
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "ERNIE 5.0 Technical Report"
daily_url: "https://arxiv.org/abs/2602.04705"
daily_keywords: ["Multimodal", "LLM", "RAG", "Tool Use", "Agent", "Retrieval", "Eval", "AI Agent", "Claude", "Claude Code"]
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.04705" target="_blank">ERNIE 5.0 Technical Report</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


ERNIE 5.0은 텍스트, 이미지, 비디오, 오디오를 아우르는 통합 멀티모달 이해 및 생성을 위해 설계된 모델입니다. 초희소(ultra-sparse) Mixture-of-Experts(MoE) 아키텍처를 기반으로 모든 모달리티를 처음부터 통합 학습하여 효율성을 극대화했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.03152" target="_blank">FASA: Frequency-aware Sparse Attention</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


긴 입력을 처리할 때 발생하는 LLM의 메모리 병목 현상을 해결하기 위해 KV 캐시를 효율적으로 관리하는 FASA를 제안합니다. 토큰의 빈도(Frequency)를 고려한 희소 어텐션 기법을 사용하여 중요 정보를 유지하면서도 메모리 사용량을 획기적으로 줄였습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.04634" target="_blank">WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


기존의 단일 에이전트 심층 추론(Depth Scaling)을 넘어, 다중 에이전트 시스템을 활용한 '너비 확장(Width Scaling)'을 탐구합니다. 이를 통해 광범위한 정보 탐색 작업에서 에이전트 간의 협업과 조직 능력을 강화하는 새로운 방향을 제시합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.04145" target="_blank">Training Data Efficiency in Multimodal Process Reward Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


MLLM의 시각적 추론 능력을 높이는 데 필요한 다중 모달 프로세스 보상 모델(MPRM)의 훈련 데이터 효율성을 분석한 논문입니다. 기존 데이터셋에 중복이 많다는 점을 발견하고, 적은 데이터로도 효율적으로 학습할 수 있는 가능성을 입증했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2602.04804" target="_blank">OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


오디오와 비디오를 이해하는 Omni-LLM의 긴 토큰 시퀀스로 인한 연산 부하 문제를 해결하기 위해 OmniSIFT 압축 프레임워크를 제안합니다. 모달리티별 비대칭 토큰 압축 방식을 적용하여 성능 저하 없이 모델의 효율성을 크게 개선했습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/ServiceNow-AI/sygra-studio" target="_blank">Introducing SyGra Studio</a></h3>



Hugging Face에 새롭게 소개된 SyGra Studio에 대한 내용을 다룹니다. 구체적인 내용은 본문을 통해 확인해야 하지만, 이름에서 유추할 수 있듯이 그래프 데이터나 합성 데이터(Synthetic Data) 관련 도구로 보입니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/nvidia/nemotron-colembed-v2" target="_blank">Nemotron ColEmbed V2: Raising the Bar for Multimodal Retrieval with ViDoRe V3’s Top Model</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


NVIDIA의 Nemotron 모델을 기반으로 멀티모달 검색 성능을 한층 높인 ColEmbed V2를 소개합니다. ViDoRe V3 벤치마크에서 최고 수준의 성능을 기록하며, 검색 시스템의 기준을 새롭게 정립했습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/blog/community-evals" target="_blank">Community Evals: Because we're done trusting black-box leaderboards over the community</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


불투명한 '블랙박스' 형태의 리더보드 대신 커뮤니티 주도의 투명한 평가 방식을 제안하는 글입니다. 사용자들이 직접 참여하여 모델을 검증하고, 더욱 신뢰할 수 있는 AI 평가 생태계를 구축하자는 메시지를 담고 있습니다.

<small><i data-lucide="user"></i> Hugging Face</small>

</div>



---


## <i data-lucide="shirt"></i> 무신사 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://techblog.musinsa.com/%EC%8A%A4%EC%BC%80%EC%A4%84%EC%9D%B4-%EB%98%90-%EC%95%88-%EB%8F%8C%EC%95%98%EC%96%B4%EC%9A%94-%EC%9A%B0%EB%A6%AC%EA%B0%80-temporal%EC%9D%84-%EC%84%A0%ED%83%9D%ED%95%9C-%EC%9D%B4%EC%9C%A0-f491e79a0f8f?source=rss----f107b03c406e---4" target="_blank">“스케줄이 또 안 돌았어요” — 우리가 Temporal을 선택한 이유</a></h3>



무신사 풀필먼트 시스템에서 Jenkins 기반의 스케줄링 불안정성을 해결하기 위해 Temporal을 도입한 기술 경험기입니다. 출고 지시 누락과 같은 운영 이슈를 해결하고, 워크플로우의 신뢰성을 높인 과정을 상세히 공유합니다.

<small><i data-lucide="user"></i> jaemin shim</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/bytedance/UI-TARS-desktop" target="_blank">bytedance/UI-TARS-desktop</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


최신 AI 모델과 에이전트 인프라를 연결하는 오픈소스 멀티모달 AI Agent 스택입니다. 데스크톱 환경을 제어하는 UI 자동화 기능을 포함하여, 다양한 멀티모달 작업을 수행할 수 있는 강력한 도구입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/openai/skills" target="_blank">openai/skills</a></h3>



OpenAI Codex가 코드를 생성하고 작업을 수행할 때 활용할 수 있는 기술(Skills) 목록을 모아둔 카탈로그입니다. Codex의 활용 범위를 넓히고 특정 프로그래밍 작업에 대한 적응력을 높이는 데 유용한 리소스입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/thedotmack/claude-mem" target="_blank">thedotmack/claude-mem</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude를 사용한 코딩 세션의 모든 내용을 자동으로 캡처하고 AI로 압축하여 기억하는 플러그인입니다. 향후 작업 시 이전 맥락을 자동으로 주입해주어, 개발자가 연속성 있게 코딩할 수 있도록 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/topoteretes/cognee" target="_blank">topoteretes/cognee</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


단 6줄의 코드로 AI 에이전트에게 장기 기억(Memory) 능력을 부여할 수 있는 라이브러리입니다. 에이전트가 과거의 상호작용과 데이터를 효율적으로 저장하고 불러올 수 있게 하여 더욱 똑똑한 대화를 가능하게 합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/aquasecurity/trivy" target="_blank">aquasecurity/trivy</a></h3>



컨테이너, Kubernetes, 코드 저장소, 클라우드 환경 등 다양한 인프라의 보안 취약점을 찾아주는 올인원 스캐너입니다. 잘못된 설정이나 노출된 비밀(Secret) 정보, SBOM 등을 탐지하여 보안 위협을 사전에 예방합니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/464" target="_blank">AI News Weekly - Issue #464: 5 reasons will will not get AGI soon - Feb 5th 2026</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


현재의 LLM 기반 모델이 AGI(일반 인공지능)에 도달하기 어려운 5가지 이유와 'Scaling Law'의 한계를 분석한 뉴스레터입니다. 단순히 모델 크기를 키우는 것만으로는 해결되지 않는 기술적 장벽과 최근 시장의 흐름을 다룹니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>LLM</code> <code>RAG</code> <code>Tool Use</code> <code>Agent</code> <code>Retrieval</code> <code>Eval</code> <code>AI Agent</code> <code>Claude</code> <code>Claude Code</code> 
</div>

---

