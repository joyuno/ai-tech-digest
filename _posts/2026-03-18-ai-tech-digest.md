---
layout: post
title: "Embracing the Software 3.0 Era (English edition)"
date: 2026-03-18
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "AI Can Learn Scientific Taste"
daily_url: "https://arxiv.org/abs/2603.14473"
daily_keywords: ["LLM", "Agent", "Tool Use", "Eval", "Grounding", "Retrieval", "RAG", "Claude", "Claude Code", "LoRA"]
daily_image: "https://ar5iv.labs.arxiv.org/html/2603.14473/assets/x1.png"
daily_image_kind: "ar5iv_fig"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.14473" target="_blank">AI Can Learn Scientific Taste</a></h3>



AI가 과학적 잠재력이 높은 연구 아이디어를 평가하고 제안하는 '과학적 안목'을 기를 수 있도록 돕는 연구입니다. 기존의 단순한 실행 능력 향상에 그치지 않고, 대규모 커뮤니티 피드백을 활용한 RLCF라는 새로운 훈련 방식을 제안합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.15594" target="_blank">OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


고성능 검색 에이전트 개발을 위해 필요한 고품질 훈련 데이터를 완전히 오픈소스로 공개한 OpenSeeker를 소개합니다. 이를 통해 일부 대기업에 집중되어 있던 기술 장벽을 낮추고, 누구나 강력한 LLM 기반 검색 에이전트를 연구할 수 있도록 지원합니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.13594" target="_blank">EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


기업의 실제 업무 환경에서 LLM 에이전트의 계획 수립 및 도구 사용 능력을 평가하기 위한 EnterpriseOps-Gym 벤치마크를 제안합니다. 상태 변화나 엄격한 접근 권한 등 전문적인 비즈니스 환경의 복잡한 특징들을 잘 반영하여 에이전트의 실질적인 업무 능력을 측정할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.15612" target="_blank">HSImul3R: Physics-in-the-Loop Reconstruction of Simulation-Ready Human-Scene Interactions</a></h3>



일반적인 영상이나 비디오에서 인간과 환경의 상호작용을 3D로 재구성해 시뮬레이션에 바로 적용할 수 있게 해주는 HSImul3R 프레임워크입니다. 물리 법칙을 위반하는 기존 시각화 방식의 한계를 극복하기 위해 물리 기반 최적화 파이프라인을 도입하여, 체화된 AI 적용에 필요한 안정성을 확보했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2603.15583" target="_blank">Grounding World Simulation Models in a Real-World Metropolis</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


가상의 공간이 아닌 실제 서울시를 배경으로 한 도시 규모의 세계 모델인 Seoul World Model(SWM)을 선보입니다. 주변 거리뷰 이미지 기반의 검색 증강 방식을 활용하여 실제 환경과 시각적으로 일치하는 사실적인 비디오 생성이 가능합니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.15619" target="_blank">Mixture-of-Depths Attention</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


LLM이 깊어질수록 얕은 층의 정보가 희석되는 신호 저하 문제를 해결하기 위해 MoDA(Mixture-of-Depths Attention) 메커니즘을 제안합니다. 각 어텐션 헤드가 현재 층뿐만 아니라 이전 층의 데이터에도 접근할 수 있게 하여, 모델의 깊이 확장 시 발생하는 성능 저하를 방지합니다.

<small><i data-lucide="user"></i> Lianghui Zhu, Yuxin Fang, Bencheng Liao</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.15618" target="_blank">Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


로봇 제어를 위한 VLA(Vision-Language-Action) 모델에서 시각적 정보가 행동 생성에 어떻게 반영되는지 심층적으로 분석한 연구입니다. LLM을 단순한 블랙박스로 취급하던 기존 방식에서 벗어나, 시각적 이해력을 높여 더욱 정교하고 신뢰할 수 있는 로봇의 행동 예측을 돕습니다.

<small><i data-lucide="user"></i> Yulin Luo, Hao Chen, Zhuangzhe Wu</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2603.15616" target="_blank">GlyphPrinter: Region-Grouped Direct Preference Optimization for Glyph-Accurate Visual Text Rendering</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


시각적 텍스트 렌더링 시 복잡한 글꼴이나 형태를 더 정확하게 생성하도록 돕는 GlyphPrinter 모델입니다. 기존 방식에서 발생하는 글자 형태의 왜곡과 부정확성을 개선하기 위해, 영역별로 그룹화된 직접 선호도 최적화 기법을 도입하여 높은 품질의 텍스트 이미지를 만들어냅니다.

<small><i data-lucide="user"></i> Xincheng Shuai, Ziye Li, Henghui Ding</small>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/harness-for-team-productivity-eng" target="_blank">Embracing the Software 3.0 Era</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


계층형 아키텍처에 익숙한 개발자의 시각에서 Claude Code를 어떻게 이해하고 활용할 수 있는지 다룬 글입니다. AI가 코드를 작성하는 Software 3.0 시대를 맞이하여, 개발 방식의 변화와 새로운 패러다임을 친숙하게 설명해 줍니다.

<small><i data-lucide="user"></i> 토스</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/abhigyanpatwari/GitNexus" target="_blank">abhigyanpatwari/GitNexus</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


서버 없이 웹 브라우저에서 바로 작동하는 코드 분석 도구인 GitNexus입니다. GitHub 저장소나 ZIP 파일을 넣기만 하면 대화형 지식 그래프와 내장된 Graph RAG 에이전트를 통해 코드를 쉽게 탐색하고 이해할 수 있어요.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langchain-ai/deepagents" target="_blank">langchain-ai/deepagents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LangChain과 LangGraph를 기반으로 구축된 강력한 에이전트 프레임워크입니다. 계획 수립 도구, 파일 시스템 연동, 하위 에이전트 생성 기능 등을 갖추고 있어 복잡한 자율 에이전트 작업을 효과적으로 처리할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/jarrodwatts/claude-hud" target="_blank">jarrodwatts/claude-hud</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


Claude Code의 작업 상태를 한눈에 파악할 수 있도록 돕는 시각화 플러그인입니다. 현재 컨텍스트 사용량, 활성화된 도구, 실행 중인 에이전트 상태 및 할 일 진행도를 실시간으로 보여주어 개발 작업 효율을 크게 높여줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/langchain-ai/deepagents" target="_blank">langchain-ai/deepagents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


LangChain과 LangGraph로 만들어진 고급 에이전트 프레임워크 저장소입니다. 파일 시스템 관리부터 계획 수립, 서브 에이전트 생성까지 지원하여 복잡한 에이전트 기반 시스템을 쉽게 구축할 수 있도록 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/resemble-ai/chatterbox" target="_blank">resemble-ai/chatterbox</a></h3>



최고 수준의 성능(SoTA)을 자랑하는 오픈소스 TTS(Text-to-Speech) 모델입니다. 최신 음성 합성 기술을 바탕으로 자연스럽고 고품질의 사람 음성을 생성할 수 있어 다양한 AI 서비스에 활용하기 좋습니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/473" target="_blank">AI News Weekly - The godfather of AI bets against LLM's - Mar 17th 2026</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


AI의 선구자 얀 르쿤이 메타를 떠나 10억 달러 규모의 투자를 유치하며 새로운 AI 기업 'AMI Labs'를 설립했다는 놀라운 뉴스입니다. 유럽 최대 규모의 시드 투자를 받으며 기존 LLM 방식과는 다른 새로운 AI 비전을 제시해 업계의 큰 주목을 받고 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Tool Use</code> <code>Eval</code> <code>Grounding</code> <code>Retrieval</code> <code>RAG</code> <code>Claude</code> <code>Claude Code</code> <code>LoRA</code> 
</div>

---

