---
layout: post
title: "앤스로픽, 금융"
date: 2026-05-08
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "anthropics/financial-services"
daily_url: "https://github.com/anthropics/financial-services"
daily_image: "https://opengraph.githubassets.com/auto/anthropics/financial-services"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2605.03849.png" alt="Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.03849" target="_blank">Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Diffusion</span> <span class="sub-tag">#Reasoning Model</span> <span class="sub-tag">#Distillation</span> 
</div>


기존 스트리밍 비디오 생성 모델의 가속화 방식은 모든 학습 데이터를 동일하게 취급하는 한계가 있었습니다. Stream-R1은 신뢰도와 복잡도를 함께 고려하는 새로운 보상 증류 기법을 제안하여, 교사 모델의 결과 중 더 신뢰할 수 있는 부분만 선별적으로 학습함으로써 생성되는 비디오의 품질을 향상시킵니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 108</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2605.04461.png" alt="Stream-T1: Test-Time Scaling for Streaming Video Generation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.04461" target="_blank">Stream-T1: Test-Time Scaling for Streaming Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#LoRA</span> 
</div>


기존 비디오 생성 모델은 테스트 시점에 성능을 향상시키는 TTS 기술을 적용하기에 비효율적인 문제가 있었습니다. Stream-T1은 스트리밍 비디오 생성 모델의 청크 단위 처리 방식과 적은 노이즈 제거 단계가 TTS에 본질적으로 적합하다는 점을 활용하여, 재학습 없이도 훨씬 적은 비용으로 비디오 품질을 높이는 새로운 방법을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 93</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2605.03042.png" alt="ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.03042" target="_blank">ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Multi-Agent</span> 
</div>


LLM 기반의 자율 연구 에이전트는 그럴듯하지만 근거 없는 결론을 내리는 문제가 발생하기 쉽습니다. 이를 해결하기 위해 제안된 ARIS는 여러 에이전트가 연구자와 검토자처럼 서로 대립하며 협력하는 구조를 통해, 연구 과정의 신뢰성을 높이고 견고한 결론을 도출하도록 설계된 오픈소스 프레임워크입니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> wanshuiyin/Auto-claude-code-research-in-sleep · ★ 8345</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 91</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2605.03269.png" alt="RLDX-1 Technical Report" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.03269" target="_blank">RLDX-1 Technical Report</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> 
</div>


기존 시각-언어-행동(VLA) 모델은 일반적인 작업은 잘하지만, 움직임 인식이나 기억 기반 의사결정 등이 필요한 복잡한 현실 세계의 로봇 작업에는 한계를 보입니다. RLDX-1은 이러한 한계를 극복하기 위해 움직임 인식, 기억 기반 의사결정, 물리적 감지 등 더 넓은 기능적 역량을 통합한 범용 로봇 모델로, 복잡한 실제 환경의 과제를 효과적으로 수행할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 85</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2605.05185.png" alt="OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.05185" target="_blank">OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최신 멀티모달 검색 에이전트는 복잡한 질문을 해결할 수 있지만, 학습 데이터나 개발 과정이 공개되지 않아 재현이 어려웠습니다. OpenSearch-VL은 고품질 학습 데이터, 투명한 개발 파이프라인, 상세한 학습 방법까지 모두 포함하는 완전한 오픈소스 레시피를 제공하여 누구나 강력한 멀티모달 검색 에이전트를 쉽게 구축하고 발전시킬 수 있도록 돕습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 80</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.05185" target="_blank">OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



최신 멀티모달 에이전트의 핵심 기능인 딥서치는 복잡한 질문을 해결하는 데 필수적이지만, 대부분의 고성능 에이전트는 재현이 어렵습니다. OpenSearch-VL은 이러한 문제를 해결하기 위해 고품질 학습 데이터와 투명한 학습 과정을 포함한 완전한 오픈소스 레시피를 제공하여 누구나 강력한 멀티모달 검색 에이전트를 개발할 수 있도록 지원합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Shuang Chen, Kaituo Feng, Hangting Chen</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.05163" target="_blank">PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World</a></h3>







가상 세계나 AI 시뮬레이션을 위한 3D 에셋 생성은 상호작용에 필수적인 물리적 속성을 간과하는 경우가 많아 한계가 있었습니다. PhysForge는 기능과 물리 법칙에 기반한 새로운 프레임워크와 대규모 데이터셋 PhysDB를 통해, 정적인 형태를 넘어 실제처럼 상호작용할 수 있는 3D 에셋을 생성하는 방법을 제시합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yunhan Yang, Chunshi Wang, Junliang Ye</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.05204" target="_blank">D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#SFT</span> <span class="sub-tag">#Distillation</span> 
</div>


적은 스텝으로도 고품질 이미지를 생성하는 최신 확산 모델들은 효율적이지만, 기존 방식으로 미세조정(fine-tuning)하면 고유의 빠른 추론 성능이 저하되는 문제가 있습니다. D-OPSD는 이러한 스텝 증류(step-distilled) 모델을 지속적으로 튜닝하면서도 빠른 추론 능력을 유지할 수 있도록 하는 새로운 학습 패러다임을 제안합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Dengyang Jiang, Xin Jin, Dongyang Liu</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/anthropics/financial-services" alt="anthropics/financial-services" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/anthropics/financial-services" target="_blank">anthropics/financial-services</a></h3>







앤스로픽(Anthropic)이 금융 서비스 분야에서 자사의 AI 모델을 활용하는 방법을 보여주는 예제 모음입니다. 금융 관련 프롬프트 엔지니어링 예시나 도구를 제공하여, 금융 전문가들이 AI를 더 효과적으로 사용할 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1367 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Hmbown/DeepSeek-TUI/main/assets/screenshot.png" alt="Hmbown/DeepSeek-TUI" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Hmbown/DeepSeek-TUI" target="_blank">Hmbown/DeepSeek-TUI</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Coding Agent</span> 
</div>


DeepSeek 코딩 모델을 터미널 환경에서 직접 실행할 수 있는 코딩 에이전트입니다. 사용자는 별도의 그래픽 인터페이스 없이 터미널에서 텍스트 기반으로 AI와 상호작용하며 코딩 작업을 수행할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 5787 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/jianc99/jianc99.github.io/master/images/dflash_system.png" alt="z-lab/dflash" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/z-lab/dflash" target="_blank">z-lab/dflash</a></h3>







DFlash는 대규모 언어 모델(LLM)의 추론 속도를 높이기 위한 새로운 기술입니다. 플래시 추측 디코딩(Flash Speculative Decoding)에 블록 디퓨전(Block Diffusion) 기법을 적용하여 더 빠르고 효율적인 텍스트 생성을 목표로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 654 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/InsForge/InsForge/main/assets/insforge-star.gif" alt="InsForge/InsForge" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/InsForge/InsForge" target="_blank">InsForge/InsForge</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#RAG</span> <span class="sub-tag">#Coding Agent</span> 
</div>


InsForge는 코딩 에이전트 개발을 위해 설계된 올인원 백엔드 프레임워크입니다. Postgres 데이터베이스를 기반으로 인증, 저장소, 컴퓨팅, 호스팅 및 AI 게이트웨이 기능까지 제공하여 AI 에이전트 구축을 간소화합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 459 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/LearningCircuit/local-deep-research" alt="LearningCircuit/local-deep-research" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/LearningCircuit/local-deep-research" target="_blank">LearningCircuit/local-deep-research</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



로컬 환경에서 심층적인 리서치를 수행할 수 있도록 돕는 RAG(검색 증강 생성) 시스템입니다. 다양한 로컬 및 클라우드 LLM을 지원하며, 개인 문서나 arXiv 같은 외부 정보 소스를 활용하여 암호화된 상태로 안전하게 질문에 답변합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 564 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/anthropic-just-had-ais-biggest-week-of-2026" target="_blank">AI Weekly Issue #490: Anthropic just had AI's biggest week of 2026</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


앤스로픽(Anthropic)은 단 5일 만에 연간 매출 추정치를 80배 성장시키고 구글 및 스페이스X와 대규모 계약을 체결하는 등 AI 업계에서 기념비적인 한 주를 보냈습니다. 이들은 새로운 코딩 자동화 모드와 금융 서비스 에이전트를 출시했으며, 같은 기간 EU의 AI 법안 최종 합의와 같은 중요한 산업 소식도 있었습니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Vision</code> <code>Distillation</code> <code>LoRA</code> <code>LLM</code> <code>Agent</code> <code>Multimodal</code> <code>Fine-tuning</code> <code>Inference</code> <code>DeepSeek</code> <code>RAG</code> 
</div>