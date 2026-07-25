---
layout: post
title: "alibaba/open-code-review — Alibaba 규모의 하이브리드 코드 리뷰 LLM Agent"
date: 2026-07-26
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "alibaba/open-code-review"
daily_url: "https://github.com/alibaba/open-code-review"
daily_image: "https://raw.githubusercontent.com/alibaba/open-code-review/main/imgs/highlights-en.png"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.21461v1/x1.png" alt="AREX: Towards a Recursively Self-Improving Agent for Deep Research" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.21461" target="_blank">AREX: Towards a Recursively Self-Improving Agent for Deep Research</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



심층 연구는 여러 제약 조건을 동시에 만족시키는 답을 찾아야 하므로 매우 어렵지만, 후보 답변을 검증하는 것은 상대적으로 쉽습니다. 이 논문은 이러한 발견-검증의 비대칭성을 활용하여, 중간 결과를 검증하고 그 피드백을 통해 스스로 답을 개선해 나가는 재귀적 자기 개선 에이전트 AREX를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 127</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2607.20145" target="_blank">SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#MoE</span> 
</div>


조 단위 파라미터 규모의 MoE 모델을 전체 파라미터로 후속 학습시키는 것은 메모리, 통신 등 막대한 시스템 자원을 요구하는 어려운 과제입니다. 이 보고서는 대부분의 대규모 LLM 학습이 GPU 클러스터에서 이루어지는 것과 달리, 어센드(Ascend) NPU 슈퍼POD 환경에서 DeepSeek-V4 모델군을 성공적으로 학습시키기 위한 엔드투엔드 최적화 사례를 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 56</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.09635v3/x3.png" alt="K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.09635" target="_blank">K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존 교육용 LLM 벤치마크는 주로 시험 문제 풀이에 초점을 맞추고 있어, 교육과정 지식의 구조적 이해 능력을 평가하는 데 한계가 있었습니다. 이 연구는 선수과목 관계, 개념 체계 등 교육과정 인지 능력을 측정하고 훈련하기 위해, 실제 교과서 기반으로 구축된 지식 그래프 K12-KGraph를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 55</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.20061v1/x1.png" alt="ReferTrack: Referring Then Tracking for Embodied Visual Tracking" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.20061" target="_blank">ReferTrack: Referring Then Tracking for Embodied Visual Tracking</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#VLA</span> <span class="sub-tag">#CoT</span> 
</div>


체화된 시각적 추적(EVT)은 에이전트가 자연어 설명을 듣고 특정 대상을 계속 따라가는 기술이지만, 기존 방식은 추론 과정이 추상적이고 감독하기 어려운 단점이 있었습니다. 이 문제를 해결하기 위해, 먼저 이미지에서 대상을 명확히 식별하고(referring) 그 다음에 추적하는(tracking) 2단계 접근 방식인 ReferTrack을 제안하여 성능을 개선합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 49</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2607.21556v1/x1.png" alt="Visual Contrastive Self-Distillation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2607.21556" target="_blank">Visual Contrastive Self-Distillation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


온-폴리시 자기 증류(OPSD)는 외부 교사 모델 없이 스스로 학습하는 유망한 방법이지만, 학생보다 교사가 더 나은 정보를 갖도록 하는 정보 비대칭성이 필요합니다. 이 연구는 기존 방식과 달리 특별한 정답이나 시각적 단서 없이, 순수하게 입력 조건을 조절하는 것만으로 정보 비대칭성을 만들어내는 더 간단한 시각적 대조 자기 증류 기법을 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 41</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.21556" target="_blank">Visual Contrastive Self-Distillation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


기존의 자기 증류(self-distillation) 방식은 교사와 학생 모델 간의 정보 비대칭성을 필요로 했습니다. 이 연구는 이러한 비대칭성을 만들기 위해 사용되던 추가적인 정보를 제거하고, 오직 입력 데이터 조건만으로 학습하는 더 단순하고 효율적인 자기 증류 방법을 제안합니다. 이를 통해 모델 구조를 간소화하고 학습 과정을 개선할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yijun Liang, Yunjie Tian, Yijiang Li</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.21553" target="_blank">SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Diffusion</span> 
</div>


SANA-Video 2.0은 단일 GPU 환경에서도 최대 720p 고화질 영상을 생성할 수 있는 새로운 하이브리드 비디오 확산 트랜스포머 모델입니다. 이 모델은 선형 어텐션(linear attention)의 효율성과 소프트맥스 어텐션(softmax attention)의 품질을 결합한 독자적인 하이브리드 어텐션 구조를 사용하여, 긴 시퀀스에서도 뛰어난 성능과 효율성을 동시에 달성합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Junsong Chen, Jincheng Yu, Yitong Li</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2607.21576" target="_blank">Self-Supervised Learning of Structured Dynamics from Videos</a></h3>







영상 속 움직임을 이해하는 것은 카메라의 움직임과 객체의 실제 움직임이 뒤섞여 있어 어려운 과제입니다. 이 연구는 자기 지도 학습(self-supervised learning)을 통해 이 두 가지 동역학 요소를 분리하는 새로운 방법을 제안합니다. 이를 통해 카메라 움직임으로 인한 변화와 실제 객체의 의미 있는 움직임을 구분하여, 더 강건한 모션 표현을 학습할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Lukas Knobel, Andrew Zisserman, Yuki M. Asano</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/alibaba/open-code-review/main/imgs/highlights-en.png" alt="alibaba/open-code-review" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/alibaba/open-code-review" target="_blank">alibaba/open-code-review</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="target"></i> 신뢰성/안전</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  



알리바바가 대규모 서비스 환경에서 검증한 오픈소스 코드 리뷰 도구입니다. 결정론적 파이프라인과 LLM 에이전트를 결합한 하이브리드 아키텍처를 통해 NPE, 스레드 안전성, XSS 등 다양한 문제를 정확히 탐지하고 줄 단위의 정밀한 코멘트를 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 439 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/citrolabs/ego-lite/main/docs/assets/banner.png" alt="citrolabs/ego-lite" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/citrolabs/ego-lite" target="_blank">citrolabs/ego-lite</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#AI Coding</span> 
</div>


AI 에이전트의 웹 자동화를 위해 특별히 설계된 초고속 브라우저입니다. 사용자의 작업 흐름을 방해하지 않으면서 로그인된 브라우저 상태를 AI 에이전트와 공유하여 복잡한 작업을 자동화할 수 있으며, 별도의 설정이나 비용이 필요 없습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 986 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/ComposioHQ/awesome-claude-skills" alt="ComposioHQ/awesome-claude-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/ComposioHQ/awesome-claude-skills" target="_blank">ComposioHQ/awesome-claude-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



앤스로픽의 AI 모델 클로드(Claude)를 더욱 효과적으로 활용하기 위한 스킬, 리소스, 도구들을 엄선하여 모아놓은 목록입니다. 이 자료들을 통해 사용자는 자신만의 클로드 AI 워크플로우를 구축하고 생산성을 극대화할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 574 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/anthropics/claude-cookbooks" alt="anthropics/claude-cookbooks" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/anthropics/claude-cookbooks" target="_blank">anthropics/claude-cookbooks</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



클로드 개발사 앤스로픽이 직접 제공하는 공식 예제 코드 모음집입니다. 노트북 형태의 다양한 레시피를 통해 클로드를 재미있고 효과적으로 활용하는 구체적인 방법들을 익힐 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 144 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/shiyu-coder/Kronos/master/figures/logo.png" alt="shiyu-coder/Kronos" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/shiyu-coder/Kronos" target="_blank">shiyu-coder/Kronos</a></h3>







크로노스(Kronos)는 금융 시장의 언어를 이해하고 분석하기 위해 특별히 설계된 파운데이션 모델입니다. 이 모델은 복잡한 금융 데이터를 처리하여 시장 동향 예측 및 투자 전략 수립에 기여하는 것을 목표로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 319 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Agent</code> <code>LLM</code> <code>Grounding</code> <code>Knowledge Graph</code> <code>Benchmark</code> <code>Vision</code> <code>Chain-of-Thought</code> <code>Distillation</code> <code>Transformer</code> <code>Safety</code> 
</div>