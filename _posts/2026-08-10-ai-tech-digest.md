---
layout: post
title: "code-graph-rag, 지식 그래프로 monorepo를 이해하는 RAG"
date: 2026-08-10
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "vitali87/code-graph-rag"
daily_url: "https://github.com/vitali87/code-graph-rag"
daily_image: "https://raw.githubusercontent.com/vitali87/code-graph-rag/main/assets/logo-dark-any.png"
daily_keywords: ["RAG"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.05466v1/x3.png" alt="Recursive Synthesis for Long-Horizon Terminal Tasks" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.05466" target="_blank">Recursive Synthesis for Long-Horizon Terminal Tasks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



장기적인(long-horizon) 작업을 위한 고품질 학습 데이터 생성은 비용이 많이 들고 복잡합니다. 이 논문은 RST(Recursive Synthetic Terminal Tasks)라는 재귀적 검증 합성 프레임워크를 제안하여, 상호 의존성이 중요한 장기 과제 데이터를 효율적으로 구축하는 방법을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 223</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.05987v1/x1.png" alt="AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.05987" target="_blank">AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#RLVR</span> <span class="sub-tag">#Distillation</span> 
</div>


여러 단계로 이루어진 장기 에이전트 작업에서 어떤 결정이 성공에 기여했는지 파악하기는 어렵습니다. AgentOPSD는 비평가(critic-free) 방식의 재귀적 자기 증류(self-distillation) 기법으로, 각 차례(turn)별 행동의 중요도를 정밀하게 평가하여 에이전트의 학습 효율을 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 85</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.28609v2/x3.png" alt="OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.28609" target="_blank">OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#Eval</span> 
</div>


컴퓨터를 사용하는 에이전트(CUA)의 작업 성공 여부를 대규모로 검증하는 것은 매우 중요하지만, 인간의 직접적인 평가는 한계가 있습니다. 이러한 한계를 극복하기 위해 VLM(비전-언어 모델)을 평가자로 활용하는 추세에 맞춰, OSReward는 여러 플랫폼에 걸쳐 컴퓨터 사용 보상 모델의 성능을 표준화하여 평가하는 새로운 프레임워크를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 67</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.01481v1/figures/interpretable_frontend_pipeline.png" alt="Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.01481" target="_blank">Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Embedding</span> <span class="sub-tag">#Eval</span> 
</div>


뇌자도(MEG) 기록에서 인지된 음성을 디코딩하는 딥러닝 모델은 성능은 높지만, 그 작동 원리를 이해하기는 어려웠습니다. 이 연구는 모델의 구조를 재설계하여 해석 가능성을 높임으로써, 어떤 대뇌 피질 영역과 음성 특징이 음성 정보 검색에 결정적인 역할을 하는지 명확히 밝혀냈습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 65</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2608.05102v1/x1.png" alt="ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2608.05102" target="_blank">ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#SFT</span> 
</div>


장기적인 검색 에이전트는 최종 답변을 찾기 위해 여러 단계를 수행하지만, 기존 학습 방식은 모든 단계의 중요도를 동일하게 취급하는 문제가 있었습니다. 이 논문은 최종 답변에서부터 역추적하여 각 행동의 기여도를 정밀하게 평가하는 ABC(Answer-Backtracked Credit Assignment) 기법을 제안하여 에이전트가 핵심적인 행동에 집중하도록 학습시킵니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 63</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.06301" target="_blank">HarnessOpt-Bench: Evaluating LLMs at Harness Optimization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Orchestration</span> <span class="sub-tag">#Eval</span> 
</div>


에이전트 시스템에서 LLM의 성능은 모델 자체뿐만 아니라 프롬프트, 도구, 제어 흐름 등을 포함하는 '하네스'에 크게 의존합니다. 'HarnessOpt-Bench'는 AI 시스템이 스스로의 하네스를 반복적으로 개선하고 평가하는 '하네스 최적화' 능력을 측정하기 위해 제안된 새로운 벤치마크입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Varun Ursekar, Apaar Shanker, Yash Maurya</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.06374" target="_blank">DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> 
</div>


다양한 형태의 로봇을 단일 VLA(Vision-Language-Action) 모델로 제어하는 것은 기존 방법의 한계로 인해 어려운 문제였습니다. 'DyPES-VLA'는 여러 로봇에 공통으로 적용되는 동역학 원리를 학습하고 로봇별 제어 방식을 자동으로 익혀, 이종 로봇 간의 조작 능력을 효과적으로 이전하는 새로운 방법을 제안합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Junfeng Li, Junjie He, Zhide Zhong</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2608.06352" target="_blank">CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



AI 에이전트 훈련을 위해서는 단순히 해결 가능한 수준을 넘어, 학습에 적절한 난이도를 가진 '터미널 태스크'가 필수적입니다. 'CalibForge'는 여러 솔버의 성능을 비교 분석하는 '적대적 솔버 보정' 기법을 통해, 주어진 에이전트에 최적화된 난이도의 태스크를 자율적으로 생성하고 수정하는 시스템입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Fanzhe Meng, Guoxin Chen, Jiale Zhao</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/PrimeIntellect-ai/prime-agent" alt="PrimeIntellect-ai/prime-agent" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/PrimeIntellect-ai/prime-agent" target="_blank">PrimeIntellect-ai/prime-agent</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



prime-agent는 코딩 작업 흐름과 장시간 자율 작업을 위해 설계된 AI 에이전트입니다. 스스로 학습하고 개선하는 능력을 갖추고 있어, 복잡한 개발 업무를 효율적으로 자동화할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 2319 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/vitali87/code-graph-rag/main/assets/logo-dark-any.png" alt="vitali87/code-graph-rag" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/vitali87/code-graph-rag" target="_blank">vitali87/code-graph-rag</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> 
</div>


code-graph-rag는 모노레포(monorepo) 환경에 최적화된 RAG 기술입니다. AI와 지식 그래프(knowledge graph)를 활용해 여러 언어로 구성된 복잡한 코드 베이스를 조회하고 이해하며 수정까지 할 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 59 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/msitarzewski/agency-agents" alt="msitarzewski/agency-agents" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/msitarzewski/agency-agents" target="_blank">msitarzewski/agency-agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



agency-agents는 마치 하나의 완전한 AI 에이전시처럼 동작하는 에이전트 모음입니다. 프론트엔드 전문가부터 커뮤니티 담당자까지, 각기 다른 개성과 전문성을 가진 에이전트들이 팀을 이루어 구체적인 결과물을 만들어냅니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 932 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/pranshuparmar/witr" alt="pranshuparmar/witr" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/pranshuparmar/witr" target="_blank">pranshuparmar/witr</a></h3>







witr는 '이 프로세스는 왜 실행되고 있는가?'라는 질문에 답을 주는 추적 도구입니다. 특정 프로세스, 포트, 컨테이너 등이 어떤 원인으로 시작되었는지 그 근원을 역추적해주며, CLI와 TUI 인터페이스를 모두 지원합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 342 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://addyosmani.com/assets/images/addys-agent-skills.jpg" alt="addyosmani/agent-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/addyosmani/agent-skills" target="_blank">addyosmani/agent-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


agent-skills는 AI 코딩 에이전트에게 실제 현업 수준의 엔지니어링 기술을 부여하기 위한 프로젝트입니다. 이를 통해 AI 에이전트가 단순 코드 생성을 넘어, 실제 프로덕션 환경에서 안정적으로 기여할 수 있도록 돕는 다양한 기술과 방법을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 670 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/what-a-week-ai-became-everybodys-decision" target="_blank">AI Weekly Issue #520: What a week: AI became everybody's decision</a></h3>







과거 단일 산업으로 다뤄지던 인공지능은 이제 서로 다른 목표를 가진 여러 기관으로 논의의 주체가 분산되었습니다. 이에 따라 특정 기술이나 권위자가 중심이 되기보다, 기술이 사회에 어떤 조건으로 남을지를 협상하는 새로운 국면으로 접어들었습니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Vision</code> <code>Distillation</code> <code>Eval</code> <code>Audio</code> <code>Retrieval</code> <code>Fine-tuning</code> <code>Prompt</code> <code>RAG</code> 
</div>