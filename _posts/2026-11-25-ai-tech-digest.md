---
layout: post
title: "Claude-BugHunter — 레드팀과 취약점 분석을 위한 Claude Code 스킬 번들"
date: 2026-11-25
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "elementalsouls/Claude-BugHunter"
daily_url: "https://github.com/elementalsouls/Claude-BugHunter"
daily_image: "https://raw.githubusercontent.com/elementalsouls/Claude-BugHunter/main/assets/sponsors/apismart-light.png"
daily_keywords: ["Jailbreak", "AI Coding"]

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2611.12164" target="_blank">Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#SFT</span> 
</div>


기존의 코드 위치 탐색기는 수정 패치가 적용될 파일만 예측하도록 학습되어, 실제 코드 수정기가 참조해야 하는 맥락 정보를 충분히 반영하지 못하는 한계가 있었습니다. 이를 해결하기 위해 수정기가 올바른 패치를 생성할 가능성을 점수화하여 위치 탐색기를 학습시키는 FGL 기법이 제안되었습니다. 이 방식은 별도의 테스트 실행이나 강화학습 없이도 가중 지도 미세조정만을 활용해 수정 모델에 최적화된 위치 탐색 파이프라인을 효율적으로 구축합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 52</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.31358v1/figures/teaser/raster_appearance.jpg" alt="Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.31358" target="_blank">Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



시각적 콘텐츠 제작은 풍부한 이미지 표현력뿐만 아니라 텍스트와 레이아웃에 대한 정밀한 제어를 동시에 요구합니다. 본 연구에서 제안하는 프레임워크는 래스터 이미지를 이산 시각 토큰으로, 정형화된 구조물을 명시적 프로그램 코드로 연결하여 정밀 제어를 실현합니다. 이를 통해 이미지와 벡터 그래픽, 웹페이지 등 다양한 시각 매체 전반에서 실시간 시각적 피드백을 반영하며 완성도 높은 창작을 지원합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 37</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.25848v1/weather_forecast_comparison.png" alt="Interpretable Prototype-Conditioned Adaptation for Weather Forecasting" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.25848" target="_blank">Interpretable Prototype-Conditioned Adaptation for Weather Forecasting</a></h3>







데이터 기반 기상 예측 모델은 지역별 상태와 시간적 변화 패턴을 명확히 구분해야 하지만, 기존 신경망 모델은 패턴을 암묵적으로만 학습하여 해석이 어렵고 오차가 발생하기 쉬웠습니다. 이러한 문제를 해결하고자 국소 기상 패턴을 명시적으로 식별하고 해석할 수 있는 프로토타입 기반 적응형 예측 기법이 제안되었습니다. 이 접근법은 명시적인 패턴 참조 기준을 제공함으로써 예측 정확도를 향상시키고 모델의 설명 가능성을 크게 높입니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 21</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.28649v1/method.png" alt="S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.28649" target="_blank">S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  



멀티모달 LLM이 물리 세계를 이해하려면 여러 시점의 시각 정보를 하나의 일관된 3D 공간으로 통합하고 시점을 자유롭게 전환하는 공간 지능이 필수적입니다. 그러나 기존 모델들은 공간 미세조정을 거친 후에도 다중 뷰 기하학을 인지하고 추론하는 능력이 여전히 부족한 것으로 나타났습니다. 연구진은 이러한 한계를 극복하고 모델 내부에 다중 뷰 기하학적 인지 능력을 내재화하여 고차원적 공간 추론을 가능하게 하는 S-Mind 프레임워크를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 21</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.25403v1/figs/fig2_1_overview.png" alt="Antom 3-in-1 Transformer: A Payment Foundation Model" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.25403" target="_blank">Antom 3-in-1 Transformer: A Payment Foundation Model</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


결제 위험 감지를 위해 시퀀스, 테이블, 그래프 형태의 복합 데이터를 통합 처리하는 약 7B 파라미터 규모의 파운데이션 모델인 Antom 3-in-1 Transformer가 개발되었습니다. 이 모델은 작업 경로마다 약 1.7B 파라미터만 선별적으로 활성화하여 효율성을 높였으며, 결제 데이터 전반의 행동 및 관계 표현을 사전에 폭넓게 학습합니다. 그 결과 다양한 금융 및 결제 업무 영역으로의 전이 학습에서도 뛰어난 위험 탐지 성능 개선 효과를 입증했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 20</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.32554" target="_blank">PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



3D 객체를 의미론적으로 유의미한 부품으로 분할하기 위해 2D와 3D 전문 모델을 결합한 에이전트 기반 프레임워크 PartAgent를 제안합니다. 기하학적 구조 정보와 2D 기반 의미 정보를 상호보완적으로 통합하여 별도의 추가 학습 없이도 정교한 파트 분할을 수행합니다. 폐루프 정제 과정을 통해 분할 결과를 점진적으로 개선하며 정확도 높은 3D 파트 인식을 달성했습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yang Cao, Zhe Zhu, Yiheng Zhang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.32100" target="_blank">EEGJev: A System One Decision Model and Benchmark for Multi-Task EEG Question Answering</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


단일 뇌파(EEG) 데이터 기반의 다양한 분석 작업을 지원하는 고속 의사결정 모델 EEGJev와 다중 작업 벤치마크를 제시합니다. 고정 레이블 방식의 한계를 넘어 19개 공개 데이터셋과 6가지 질문 유형을 바탕으로 질문과 선택지가 동적으로 변하는 환경을 평가합니다. 단 한 번의 추론으로 후보 답변을 신속하게 채점하여 뇌파 기반 질의응답 시스템의 유연성을 크게 높였습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Dengzhe Hou, Kazunori D. Yamada</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.32491" target="_blank">X-3DComposer: Feed-Forward 3D Scene Composition with Any Assets from Any Views</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


이미지로부터 편집 가능한 3D 장면을 구축하기 위해 에셋 생성과 레이아웃 배치를 분리한 피드포워드 모델 X-3DComposer를 소개합니다. 기존 기법과 달리 반복적인 최적화나 복잡한 입력 조건 없이 다양한 시점의 이미지를 활용해 다중 객체의 배치를 한 번에 예측합니다. 임의의 3D 에셋을 자유롭게 장면에 합성할 수 있어 확장성 높은 3D 장면 생성을 실현했습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Zidian Qiu, Ancong Wu</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/elementalsouls/Claude-BugHunter/main/assets/sponsors/apismart-light.png" alt="elementalsouls/Claude-BugHunter" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/elementalsouls/Claude-BugHunter" target="_blank">elementalsouls/Claude-BugHunter</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Jailbreak</span> <span class="sub-tag">#AI Coding</span> 
</div>


Claude-BugHunter는 버그 바운티와 외부 레드팀 모의해킹 작업을 지원하는 Claude Code 전용 스킬 번들입니다. 84개의 스킬과 15개의 슬래시 명령어, 24개 주요 취약점 클래스에 걸친 681개의 공개 보고서 패턴을 제공합니다. 또한 기업용 계정 식별 및 인프라 공격 매트릭스까지 폭넓게 포함하고 있어 체계적인 보안 점검을 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1826 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/jingyaogong/minimind/master/images/logo.png" alt="jingyaogong/minimind" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/jingyaogong/minimind" target="_blank">jingyaogong/minimind</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



minimind는 단 2시간 만에 바닥부터 64M 파라미터 크기의 LLM을 직접 학습시킬 수 있는 오픈소스 프로젝트입니다. 대규모 컴퓨팅 자원 없이도 개인용 환경에서 언어 모델의 사전 학습부터 미세 조정까지의 전 과정을 실습해볼 수 있습니다. 경량 모델 구현 원리를 깊이 있게 이해하고 싶은 개발자들에게 훌륭한 입문 자료를 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 727 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/openvinotoolkit/openvino" alt="openvinotoolkit/openvino" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/openvinotoolkit/openvino" target="_blank">openvinotoolkit/openvino</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  



OpenVINO는 딥러닝 모델의 추론 성능을 최적화하고 다양한 하드웨어 환경에 손쉽게 배포할 수 있도록 돕는 오픈소스 툴킷입니다. 인텔의 CPU, GPU 등 여러 디바이스에서 AI 추론 속도를 극대화할 수 있도록 지원합니다. 다양한 딥러닝 프레임워크와 호환되어 엣지 디바이스부터 클라우드까지 폭넓게 활용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 185 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/screenshots/thumbs/import-drawio.webp" alt="cathrynlavery/diagram-design" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/cathrynlavery/diagram-design" target="_blank">cathrynlavery/diagram-design</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


diagram-design은 Claude Code, Cursor, Copilot 등 다양한 코딩 AI 도구에서 활용할 수 있는 다이어그램 디자인 리소스입니다. 불필요한 효과나 복잡한 의존성 없이 단독 실행 가능한 HTML과 SVG 기반으로 총 52가지 유형의 깔끔한 다이어그램을 제공합니다. 개발자가 복잡한 아키텍처나 개념을 가독성 높은 시각 자료로 신속하게 표현할 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 802 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/mvanhorn/last30days-skill/main/media/pr-assets/last30days-ad.gif" alt="mvanhorn/last30days-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



last30days-skill은 레딧, X, 유튜브, 해커뉴스 등 다양한 웹 플랫폼에서 특정 주제의 최신 30일간 데이터를 조사하는 AI 에이전트 스킬입니다. 여러 채널에서 수집된 방대한 정보를 종합 분석하여 신뢰성 높은 요약 보고서를 자동으로 생성합니다. 빠르게 변화하는 최신 트렌드나 특정 이슈의 여론을 한눈에 파악하기에 매우 유용합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 703 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Fine-tuning</code> <code>Agent</code> <code>LLM</code> <code>Transformer</code> <code>Reasoning</code> <code>Benchmark</code> <code>Retrieval</code> <code>Eval</code> <code>Claude</code> <code>Red-team</code> 
</div>