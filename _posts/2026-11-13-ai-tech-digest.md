---
layout: post
title: "OpenAI codex-security — 코드 취약점 탐지 및 자동 수정 CLI"
date: 2026-11-13
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "openai/codex-security"
daily_url: "https://github.com/openai/codex-security"
daily_image: "https://opengraph.githubassets.com/auto/openai/codex-security"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.14320v1/fig01-teaser.png" alt="Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.14320" target="_blank">Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



LLM 에이전트의 외부 메모리는 이전 경험을 활용해 성능을 높이지만, 잘못되거나 오적용된 교훈으로 인해 오히려 문제를 틀리는 메모리 유발 성능 저하를 일으키기도 합니다. 본 연구에서는 교훈의 근거가 되는 과거 수행 궤적을 메모리에 직접 연결하여 이러한 성능 저하를 방지하는 접근법을 제안합니다. 이를 통해 에이전트는 무분별한 기억 의존을 줄이고 더 신뢰도 높은 판단을 내릴 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 66</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.14210" target="_blank">Tree-Ising: Repairing Language Models with Bit-Level Ising Edits</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최근 대형 언어 모델의 가중치를 직접 수정해 비정상적인 추론 루프를 교정하는 기법이 등장했으나, 막대한 연산량과 토큰이 소모되는 한계가 있었습니다. 본 연구진이 제안한 Tree-Ising은 가중치 수정 과정을 이산 최적화 문제로 전환하여 모델의 비트 수준에서 효율적으로 루프 패턴을 약화시킵니다. 이를 통해 과도한 자원 소모 없이도 언어 모델 내부의 추론 오류를 정밀하게 수리할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 62</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2610.40394v1/head1_1014_split_rc6.png" alt="Scaling Mathematical Proof Supervision from Structured Textbooks" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2610.40394" target="_blank">Scaling Mathematical Proof Supervision from Structured Textbooks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



기존 언어 모델을 위한 수학 학습 데이터는 개별 문제와 정답 쌍으로 단순화되어 교재가 지닌 체계적인 교육 과정과 증명 연결 구조를 잃어버리는 문제가 있었습니다. 본 논문은 대학 수준 수학 교재 2,118권을 기반으로 목차 순서와 명제 간 의존 관계를 보존한 대규모 데이터셋 TOME-Math를 구축했습니다. 약 38만 건의 구조화된 증명 기록을 제공함으로써 언어 모델이 깊이 있는 수학적 논리를 학습할 수 있도록 지원합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 40</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.13001v1/04_task_rank_analysis_pooled_spearman_member_complete.png" alt="One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.13001" target="_blank">One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


표 데이터에 대한 데이터 생성, 결측치 대체, 타깃 예측은 동일한 분포를 공유하지만 그동안 독립적으로만 평가되어 단일 모델의 범용 역량을 파악하기 어려웠습니다. 이에 연구진은 56개 데이터셋과 46개 모델을 포괄하여 세 작업을 통합 평가하는 One Table 벤치마크를 새롭게 제안했습니다. 이를 통해 동일한 조건에서 모델들을 다각도로 비교하며 표 데이터를 다루는 범용 파운데이션 모델의 가능성을 체계적으로 검증합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 40</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.13410v1/method.png" alt="SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.13410" target="_blank">SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Quantization</span> 
</div>


저비트 양자화는 LLM 에이전트의 추론 비용을 절감하지만 작업 환경 조건을 간과하게 만들어 성공 경로에서 이탈하는 문제를 일으킵니다. 학생 모델의 실패 상황을 사후 데이터만으로 바로잡기 어렵다는 점에 착안하여, 교사 모델이 실시간으로 주행 경로를 유도하는 SteerDistill 기법을 제안했습니다. 폐루프 방식의 조향을 통해 양자화된 에이전트의 행동 편차를 신속히 교정하고 전반적인 작업 성공률을 효과적으로 보존합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 32</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.14953" target="_blank">RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#Eval</span> 
</div>


RSLiveBench-UAV는 드론 기반 항공 공간 지능을 평가하기 위해 지속적으로 진화하는 비전-언어 벤치마크입니다. 시점과 축척 변화에 따른 객체 및 공간 관계 이해도를 정밀하게 측정하고자 실제 UAV 촬영 데이터를 주기적으로 수집하여 새로운 평가 문제를 생성합니다. 이를 통해 최신 모델의 다각도 공간 추론 능력을 현실감 있는 환경에서 지속해서 검증할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yue Zhou, Jiawei Liu, Jue Chen</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.14516" target="_blank">TorchCurves: Differentiable Parametric Curves</a></h3>







TorchCurves는 벡터 값 매개변수 곡선을 학습 가능한 요소로 다루는 파이토치 기반 라이브러리입니다. B-스플라인이나 르장드르 다항식을 활용해 곡선 상의 좌표를 매핑하며, 입력값과 계수 모두에 대해 미분 연산을 지원합니다. 따라서 곡선 매개변수를 딥러닝 모델과 함께 직접 최적화하거나 다른 신경망의 출력값으로 유연하게 활용할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Alex Shtoff</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.15049" target="_blank">Science Prediction Universe</a></h3>







Science Prediction Universe는 차세대 AGI의 핵심 역량인 과학 실험 결과 예측 능력을 탐구하는 프로젝트입니다. 자연 현상에 대한 깊은 이해를 바탕으로 인간 연구자보다 정확하게 실험 결과를 예측함으로써 과학적 발견의 속도를 획기적으로 높이고자 합니다. 이러한 신뢰도 높은 예측 능력은 인류가 직면한 다양한 난제를 해결하고 전반적인 복지를 증진하는 데 크게 기여할 것입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zengji Tu, Xiang Liu, Jiarui Sun</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/openai/codex-security" alt="openai/codex-security" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/openai/codex-security" target="_blank">openai/codex-security</a></h3>







OpenAI의 Codex Security는 코드 내 보안 취약점을 탐지하고 검증하며 수정까지 돕는 개발 도구입니다. CLI와 TypeScript SDK 형태로 제공되어 기존 워크플로우나 프로젝트에 손쉽게 통합할 수 있습니다. 이를 통해 소프트웨어 개발 주기 전반에서 보안 결함을 사전에 예방하고 신속하게 조치할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 643 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://img.alicdn.com/imgextra/i1/O1CN01DXWdF8BDUdD3XPhl_!!6000000001721-2-tps-1743-902.png" alt="QwenLM/qwen-code" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/QwenLM/qwen-code" target="_blank">QwenLM/qwen-code</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> <span class="sub-tag">#AI Coding</span> 
</div>


터미널 환경에서 직접 실행되는 오픈소스 AI 코딩 어시스턴트 프로젝트입니다. 개발자는 터미널 창을 벗어나지 않고도 코드 생성, 리팩터링, 디버깅 등 다양한 작업을 AI와 대화하며 처리할 수 있습니다. 콘솔 기반 워크플로우를 선호하는 개발자에게 높은 작업 효율성을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 151 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/ashhart/TensorFold" alt="ashhart/TensorFold" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/ashhart/TensorFold" target="_blank">ashhart/TensorFold</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  



Metal, CUDA, Vulkan 등 다양한 그래픽 백엔드를 포괄적으로 지원하는 LLM 추론 엔진입니다. 애플 실리콘과 엔비디아 GPU를 비롯한 여러 하드웨어 환경에서 최적화된 모델 실행 성능을 발휘하도록 돕습니다. 하드웨어 종속성을 줄이면서 대규모 언어 모델을 유연하게 서빙하고자 할 때 유용합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 54 today</span> 

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


AI 코딩 에이전트가 실제 상용 서비스 개발에 투입될 수 있도록 돕는 실무 수준의 엔지니어링 역량 모음집입니다. 고품질 코드 작성, 아키텍처 설계, 유지보수 등 현업의 엄격한 기준을 충족하는 체계적인 가이드를 제공합니다. 단순 코드 완성을 넘어 자율적인 AI 소프트웨어 엔지니어를 구축하는 데 핵심적인 지침이 됩니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 816 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/CopilotKit/OpenBot/main/app/src/assets/openbot-logo.png" alt="CopilotKit/OpenBot" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/CopilotKit/OpenBot" target="_blank">CopilotKit/OpenBot</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


브라우저, 파일 시스템, 작업 툴이 갖춰진 독립된 가상 컴퓨터 환경에서 활동하는 오픈소스 AI 가상 동료 프로젝트입니다. 수행할 작업을 사전에 계획하고 실행 후 모든 내역을 투명하게 기록하여 안전한 자동화를 실현합니다. 다양한 에이전트와 연동할 수 있어 복잡한 디지털 업무를 사람처럼 자율적으로 처리할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 298 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>LLM</code> <code>Agent</code> <code>Vision</code> <code>Eval</code> <code>Quantization</code> <code>Inference</code> <code>AI Coding</code> <code>Copilot</code> 
</div>