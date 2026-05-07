---
layout: post
title: "하마터면 못생겨질 뻔했다 — 토스 프론트 2 폰트 제작기"
date: 2026-04-10
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]
daily_source: "arxiv"
daily_title: "Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning"
daily_url: "https://arxiv.org/abs/2604.04746"
daily_keywords: ["Multimodal", "LLM", "RAG", "Agent", "Eval", "Vision", "Inference", "Claude Code", "Claude", "AI Coding"]
daily_image: "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2604.04746.png"
---


---


## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.04746" target="_blank">Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


인간이 스케치부터 디테일까지 단계별로 그림을 그리는 방식에서 착안한 프로세스 기반 이미지 생성 방법을 제안합니다. 단순한 픽셀 생성을 넘어, 생각과 행동이 교차하는 추론 과정을 통해 다중 모달 모델이 단계적으로 이미지를 완성하게 해주는 흥미로운 연구입니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.06268" target="_blank">RAGEN-2: Reasoning Collapse in Agentic RL</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>


멀티턴 LLM 에이전트의 강화학습 과정에서 발생하는 '템플릿 붕괴' 현상을 새롭게 조명한 논문입니다. 모델의 지표가 안정적으로 보이더라도 실제로는 다양한 입력에 대해 고정된 답변 템플릿만 반복하는 문제를 발견하고 그 원인을 심도 있게 분석했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.02648" target="_blank">GBQA: A Game Benchmark for Evaluating LLMs as Quality Assurance Engineers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


LLM이 자율적으로 소프트웨어 버그를 찾아내는 능력을 평가하기 위해 개발된 게임 QA 벤치마크(GBQA)를 소개합니다. 동적인 런타임 환경을 가진 30개의 게임과 124개의 검증된 버그 데이터를 통해 LLM의 QA 엔지니어로서의 가능성을 재미있게 실험해 보았습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.05091" target="_blank">MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU</a></h3>



단일 GPU만으로 100B 이상의 파라미터를 가진 거대 LLM을 온전한 정밀도로 학습시킬 수 있는 MegaTrain 시스템을 제안합니다. 파라미터와 최적화 상태를 CPU 메모리에 저장하고 GPU는 연산용으로만 활용하여 기존의 하드웨어 한계를 영리하게 극복했습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://arxiv.org/abs/2604.04934" target="_blank">Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


인물 사진과 옷 이미지, 포즈 비디오를 결합해 자연스럽게 옷을 입고 움직이는 영상을 만들어내는 Vanast 프레임워크를 소개합니다. 가상 피팅과 애니메이션 생성을 하나의 단계로 통합하여, 기존 방식에서 발생하던 신원 왜곡이나 옷의 부자연스러움을 말끔히 해결했습니다.



</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.07340" target="_blank">TC-AE: Unlocking Token Capacity for Deep Compression Autoencoders</a></h3>



이미지 압축 복원 품질을 높이기 위해 설계된 ViT 기반의 새로운 오토인코더 구조인 TC-AE를 제안합니다. 복잡한 구조를 추가하는 대신 토큰 공간 자체의 용량을 활용하여, 높은 압축률에서도 잠재 표현이 무너지는 현상을 효과적으로 방지해 줍니다.

<small><i data-lucide="user"></i> Teng Li, Ziyuan Huang, Cong Chen</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.07350" target="_blank">Fast Spatial Memory with Elastic Test-Time Training</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>


긴 문맥을 처리하는 3D 재구성 과정에서 발생하는 모델의 과적합과 치명적 망각 문제를 해결하기 위한 기술입니다. 기존의 Test-Time Training 방식에 탄력적인 가중치 조절 기법을 도입하여, 아무리 긴 시퀀스라도 한 번에 안정적으로 처리할 수 있게 해줍니다.

<small><i data-lucide="user"></i> Ziqiao Ma, Xueyang Yu, Haoyu Zhen</small>

</div>


<div class="digest-item" markdown="1">

<h3><a href="https://huggingface.co/papers/2604.07348" target="_blank">MoRight: Motion Control Done Right</a></h3>



사용자가 원하는 대로 객체의 움직임과 카메라 시점을 완벽하게 분리해서 제어할 수 있는 AI 영상 생성 기술입니다. 단순한 픽셀 이동을 넘어 물리적인 인과관계까지 고려하므로, 한층 더 자연스럽고 정교한 모션 컨트롤이 가능해집니다.

<small><i data-lucide="user"></i> Shaowei Liu, Xuanchi Ren, Tianchang Shen</small>

</div>



---


## <i data-lucide="credit-card"></i> 토스 기술블로그


<div class="digest-item" markdown="1">

<h3><a href="https://toss.tech/article/toss_front" target="_blank">하마터면 못생겨질 뻔했다 - 토스 프론트 2 제작기</a></h3>



디자인과 사용성을 모두 잡아낸 토스 프론트 2 폰트의 치열한 제작 과정을 담은 글입니다. '이게 정말 최선일까?'라는 끊임없는 고민을 통해 사용자에게 더 나은 경험을 제공하려 했던 토스 개발팀의 집요한 노력을 엿볼 수 있습니다.

<small><i data-lucide="user"></i> 토스</small>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/forrestchang/andrej-karpathy-skills" target="_blank">forrestchang/andrej-karpathy-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 전문가 Andrej Karpathy의 통찰을 바탕으로 Claude Code의 동작을 최적화하는 설정 파일입니다. 단일 CLAUDE.md 파일을 통해 LLM이 코딩 중 흔히 겪는 함정을 피하고 더 훌륭한 결과물을 내도록 도와줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/opendataloader-project/opendataloader-pdf" target="_blank">opendataloader-project/opendataloader-pdf</a></h3>



AI가 쉽게 데이터를 학습할 수 있도록 문서를 변환해 주는 오픈소스 PDF 파싱 도구입니다. 복잡한 PDF 문서의 접근성 처리를 자동화하여 데이터 전처리 시간을 크게 단축시켜 줍니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/TheCraigHewitt/seomachine" target="_blank">TheCraigHewitt/seomachine</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


검색 엔진 최적화(SEO)에 강력한 장문의 블로그 콘텐츠를 작성할 수 있게 해주는 특화된 Claude Code 워크스페이스입니다. 자료 조사부터 작성, 분석까지 한 번에 처리하여 타겟 고객에게 잘 노출되는 글을 쉽게 완성할 수 있습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/coleam00/Archon" target="_blank">coleam00/Archon</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>


AI 코딩 작업의 결과물을 예측 가능하고 일관성 있게 만들어주는 최초의 오픈소스 하네스 빌더 도구입니다. 복잡한 AI 코딩 과정을 체계적으로 관리하여 언제든 동일한 품질의 코드를 반복 생성할 수 있게 돕습니다.



</div>


<div class="digest-item" markdown="1">

<h3><a href="https://github.com/shiyu-coder/Kronos" target="_blank">shiyu-coder/Kronos</a></h3>



금융 시장의 복잡한 언어와 데이터를 이해하고 분석하기 위해 특별히 설계된 파운데이션 모델입니다. 금융 도메인에 특화된 지식을 바탕으로 AI가 투자와 시장 분석을 더 깊이 있게 수행할 수 있도록 든든하게 지원합니다.



</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">

<h3><a href="https://aiweekly.co/issues/481" target="_blank">AI Weekly Issue #481: Musk wants Altman fired, Anthropic passes OpenAI, Meta goes closed</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>


Anthropic이 기업용 수요를 바탕으로 OpenAI의 매출을 추월했다는 소식과 함께, 오픈소스를 지향하던 Meta가 폐쇄형 모델을 출시한 소식을 전합니다. 또한 일론 머스크와 샘 알트만 사이의 소송전 등 한 주간 AI 업계를 뒤흔든 굵직한 이슈들을 생생하게 다루고 있습니다.



</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Multimodal</code> <code>LLM</code> <code>RAG</code> <code>Agent</code> <code>Eval</code> <code>Vision</code> <code>Inference</code> <code>Claude Code</code> <code>Claude</code> <code>AI Coding</code> 
</div>

---

