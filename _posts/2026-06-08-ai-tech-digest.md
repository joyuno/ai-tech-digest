---
layout: post
title: "AI Tech - 2026-06-08"
date: 2026-06-08
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "opencv/opencv"
daily_url: "https://github.com/opencv/opencv"
daily_image: "https://opengraph.githubassets.com/auto/opencv/opencv"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.06492v1/x1.png" alt="Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.06492" target="_blank">Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#LoRA</span> <span class="sub-tag">#RAG</span> 
</div>


기존 코드 언어 모델은 RAG나 미세조정(fine-tuning)을 통해 저장소(repository)별 컨텍스트를 학습했지만, 비용이 많이 들고 코드 변경에 취약했습니다. Code2LoRA는 하이퍼네트워크를 이용해 각 저장소에 맞는 LoRA 어댑터를 동적으로 생성하여, 추론 시 추가적인 토큰 오버헤드 없이 저장소의 지식을 효율적으로 모델에 주입합니다. 이를 통해 끊임없이 변화하는 소프트웨어 환경에 효과적으로 대응할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 72</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2606.05553" target="_blank">ArcANE: Do Role-Playing Language Agents Stay in Character at the Right Time?</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


기존의 역할극 언어 에이전트(RPLA) 벤치마크는 이야기 속 캐릭터의 고정된 정보만을 평가할 뿐, 스토리 진행에 따른 인물의 심리적 변화나 성장을 제대로 측정하지 못했습니다. 이를 해결하기 위해 ArcANE이라는 새로운 벤치마크를 제안하며, 이는 소설 속 주요 인물들의 감정 및 가치관 변화 궤적을 자동으로 추적하고 평가합니다. ArcANE을 통해 에이전트가 원작에 나오지 않는 새로운 상황에서도 캐릭터의 변화된 성격에 맞춰 일관성 있게 반응하는지 심층적으로 검증할 수 있습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 45</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.04743v1/x1.png" alt="TIDE: Proactive Multi-Problem Discovery via Template-Guided Iteration" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.04743" target="_blank">TIDE: Proactive Multi-Problem Discovery via Template-Guided Iteration</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



기존 AI 에이전트는 사용자가 직접 요청한 문제만 해결하는 수동적 역할에 머물러, 사용자의 전체 컨텍스트 속에 숨겨진 여러 잠재적 문제를 놓치곤 했습니다. 이 논문은 컨텍스트 내에 숨겨진 여러 문제를 능동적으로 발견하는 새로운 과업을 제시하며, 이를 위한 TIDE라는 프레임워크를 제안합니다. TIDE는 템플릿 기반의 반복적 탐색을 통해 숨겨진 문제들을 근거와 함께 발견하고 알려줌으로써, 보다 선제적인 AI 비서의 역할을 수행할 수 있게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 38</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.05622v1/x1.png" alt="AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.05622" target="_blank">AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


현실 세계의 문제 해결을 위해 LLM 에이전트는 점진적으로 드러나는 외부 환경 및 사용자 제약 조건에 맞춰 계획을 수정해야 하지만, 기존 벤치마크는 이러한 적응적 계획 수립 능력을 제대로 평가하지 못했습니다. 이를 극복하기 위해, 상호작용을 통해 제약 조건이 순차적으로 공개되는 동적 환경에서 LLM 에이전트의 계획 및 재계획 능력을 평가하는 새로운 벤치마크 AdaPlanBench를 제안합니다. AdaPlanBench는 에이전트가 예측 불가능한 변화에 얼마나 유연하게 대처하는지 측정하여, 보다 현실적인 문제 해결 능력을 검증하는 기준을 제시합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 37</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2606.05259v1/x2.png" alt="VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2606.05259" target="_blank">VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#CoT</span> 
</div>


심층적인 지식과 추론 능력을 요구하는 비디오 이해 기술을 강화하기 위해, VideoKR이라는 새로운 대규모 학습 데이터셋을 공개합니다. VideoKR은 전문가 도메인의 비디오를 기반으로 생성된 31만 5천 개의 비디오 추론 예시를 포함하며, 인간 참여형 파이프라인을 통해 제작되어 예시의 난이도와 다양성을 확보했습니다. 이를 통해 모델이 단순한 인식을 넘어 복잡한 상황을 이해하고 추론하는 능력을 효과적으로 학습하도록 돕습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 34</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.06492" target="_blank">Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#LoRA</span> <span class="sub-tag">#RAG</span> 
</div>


코드 언어 모델이 전체 저장소의 맥락을 이해하기 위해 사용하는 기존 RAG나 미세조정 방식은 비용이 많이 들고 비효율적입니다. 이 논문은 하이퍼네트워크를 이용해 각 코드 저장소에 맞는 LoRA 어댑터를 동적으로 생성하는 Code2LoRA 프레임워크를 제안하며, 이를 통해 추론 시 추가적인 토큰 오버헤드 없이 저장소의 지식을 효율적으로 모델에 주입합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Liliana Hotsko, Yinxi Li, Yuntian Deng</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.06477" target="_blank">Complexity-Balanced Diffusion Splitting</a></h3>







기존 확산 모델은 생성 과정 전체에 단일 대규모 네트워크를 사용해 비효율적입니다. 이 논문은 생성 과정의 시간대별 복잡도에 맞춰 모델 용량을 다르게 할당하는 '복잡도 균형 분할(CBS)' 기법을 제안하며, 이를 통해 전체 작업을 여러 전문 네트워크에 분산시켜 효율을 높입니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Noam Issachar, Dani Lischinski, Raanan Fattal</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2606.06486" target="_blank">Regret Minimization with Adaptive Opponents in Repeated Games</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



반복 게임에서 상대방이 과거 기록에 따라 전략을 바꾸는 경우, 기존의 후회 최소화 지표는 이러한 적응성을 제대로 반영하지 못합니다. 이 논문은 모든 플레이어가 과거 기록에 대응할 수 있다는 반사실적 상황까지 고려하는 새로운 게임 이론 지표인 '반복 정책 후회(RP-Regret)'를 제안하여, 적응형 상대를 포함한 복잡한 게임 환경에서의 의사결정을 더 정확하게 평가합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/mvanhorn/last30days-skill" alt="mvanhorn/last30days-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/mvanhorn/last30days-skill" target="_blank">mvanhorn/last30days-skill</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 AI 에이전트 스킬은 특정 주제에 대해 레딧, X, 유튜브 등 다양한 온라인 소스를 리서치합니다. 수집된 정보를 바탕으로 근거에 기반한 종합적인 요약문을 생성하여 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1097 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/opencv/opencv" alt="opencv/opencv" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/opencv/opencv" target="_blank">opencv/opencv</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  



OpenCV는 오픈소스 컴퓨터 비전 라이브러리의 대표주자입니다. 이미지 처리, 객체 감지, 얼굴 인식 등 다양한 컴퓨터 비전 기능을 개발자들이 쉽게 구현할 수 있도록 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 89 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/assets/readme-banner.png" alt="Leonxlnx/taste-skill" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/Leonxlnx/taste-skill" target="_blank">Leonxlnx/taste-skill</a></h3>







Taste-Skill은 AI가 더 흥미롭고 독창적인 결과물을 생성하도록 돕는 기술입니다. AI가 지루하고 일반적인 내용을 반복적으로 만들어내는 것을 방지하여, 보다 수준 높은 '취향'을 갖게 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1104 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/yikart/AiToEarn/main/presentation/monetize-cn.png" alt="yikart/AiToEarn" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/yikart/AiToEarn" target="_blank">yikart/AiToEarn</a></h3>







AiToEarn은 AI 기술을 활용하여 수익을 창출하는 다양한 방법을 탐구하고 공유하는 프로젝트입니다. 자동화된 작업, 콘텐츠 생성, 데이터 분석 등 AI를 이용한 수익화 모델과 실제 사례들을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 180 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/aaif-goose/goose" alt="aaif-goose/goose" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/aaif-goose/goose" target="_blank">aaif-goose/goose</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



Goose는 단순한 코드 제안을 넘어선 오픈소스 AI 에이전트입니다. 이 에이전트는 어떤 LLM과도 연동하여 코드 설치, 실행, 수정, 테스트까지 자율적으로 수행할 수 있는 확장성을 갖추고 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 338 today</span> 

</div>

</div>



---


## <i data-lucide="newspaper"></i> AI Weekly


<div class="digest-item" markdown="1">



<h3><a href="https://aiweekly.co/issues/wall-street-cant-agree-if-the-ai-bubble-just-burst" target="_blank">AI Weekly Issue #500: $1.3 trillion vanished Friday. Bubble, or just profit-taking?</a></h3>







금요일 AI 및 반도체 주식이 1조 3천억 달러 규모의 폭락을 기록하며 2020년 이후 최악의 날을 맞았습니다. 이는 최근의 주가 급등에 따른 단순한 차익 실현인지, 아니면 AI 버블 붕괴의 시작인지에 대해 금융 전문가들의 의견이 첨예하게 엇갈리고 있습니다.

<div class="item-meta">





</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Fine-tuning</code> <code>RAG</code> <code>Agent</code> <code>Eval</code> <code>LLM</code> <code>Reasoning</code> <code>CoT</code> <code>AI Agent</code> <code>Vision</code> 
</div>