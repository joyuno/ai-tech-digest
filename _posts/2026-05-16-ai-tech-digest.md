---
layout: post
title: "AI Tech - 2026-05-16"
date: 2026-05-16
categories: [AI, Tech]
tags: [AI, LLM, 트렌드, 기술블로그]


daily_source: "github_trending"
daily_title: "anthropics/skills"
daily_url: "https://github.com/anthropics/skills"
daily_image: "https://skills.sh/b/anthropics/skills"
daily_keywords: []

---






## <i data-lucide="book-open"></i> arXiv 논문


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.13301v1/x4.png" alt="Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.13301" target="_blank">Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Reasoning Model</span> 
</div>


최근 AI 모델들이 국제 수학/물리 올림피아드에서 금메달 수준의 성과를 내고 있는 가운데, 이 논문은 기존에 학습된 추론 모델을 간단하고 통일된 방법을 통해 최고 수준의 올림피아드 문제 해결사로 만드는 레시피를 제안합니다. 이 방법은 특수한 커리큘럼을 사용한 미세조정(SFT)을 통해 모델의 추론 능력을 극대화하여 올림피아드 수준의 문제 해결 능력을 갖추게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 126</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.15141v1/x1.png" alt="Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.15141" target="_blank">Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


실시간 양방향 비디오 생성을 위해서는 낮은 지연 시간과 스트리밍 제어가 필수적입니다. 이 논문은 'Causal Forcing++'라는 새로운 기술을 통해 기존 확산 모델 증류 방식의 한계를 극복하고, 단 1~2단계의 샘플링만으로 프레임 단위의 비디오를 빠르고 정교하게 생성하는 방법을 제시합니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> thu-ml/Causal-Forcing · ★ 652</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 74</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.15155v1/x1.png" alt="Self-Distilled Agentic Reinforcement Learning" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.15155" target="_blank">Self-Distilled Agentic Reinforcement Learning</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="wrench"></i> 학습/최적화</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#Distillation</span> 
</div>


LLM 에이전트를 학습시키는 강화학습(RL)은 장기적인 작업에서 보상 신호가 너무 부족하여 비효율적입니다. 이 논문은 '자기 증류 에이전트 강화학습'이라는 새로운 패러다임을 제안하여, 특권적인 정보를 가진 교사 모델이 학생 에이전트에게 토큰 수준의 촘촘한 가이드를 제공하게 함으로써 복잡한 상호작용에서도 안정적이고 효율적인 학습을 가능하게 합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 66</span> 


</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://arxiv.org/abs/2605.14906" target="_blank">MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> <span class="sub-tag">#Eval</span> 
</div>


대규모 비전-언어 모델(LVLM)이 긴 멀티모달 대화를 이해하려면 장기 기억 능력이 필수적이지만, 이를 체계적으로 평가할 벤치마크가 부족했습니다. 이 논문은 'MemLens'라는 새로운 벤치마크를 소개하여, 여러 세션에 걸친 대화에서 시각 및 텍스트 정보를 모두 기억해야만 답할 수 있는 질문들을 통해 모델의 장기 기억 성능을 종합적으로 측정하고 비교합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 61</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2605.15178v1/x1.png" alt="SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2605.15178" target="_blank">SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Diffusion</span> <span class="sub-tag">#World Model</span> 
</div>


이 논문은 분 단위의 고화질(720p) 영상을 정밀한 카메라 제어와 함께 생성할 수 있는 효율적인 오픈소스 월드 모델 'SANA-WM'을 소개합니다. SANA-WM은 하이브리드 선형 어텐션 등 네 가지 핵심 설계를 통해 대규모 산업용 모델에 필적하는 영상 품질을 달성하면서도 효율성은 크게 향상시켰습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 51</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.15198" target="_blank">ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



기존 시각적 추론 모델은 이미지를 직접 생성하거나 외부 도구를 사용하는 방식으로 인해 계산 비용이 높고 지연 시간이 발생하는 문제가 있었습니다. ATLAS는 에이전트 기반 추론과 잠재 공간 추론을 하나의 단어로 제어하는 통합적 접근 방식을 제안하여, 이러한 비효율성을 해결하고 더 빠르고 간결한 시각적 추론을 가능하게 합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Ziyu Guo, Rain Liu, Xinyan Chen</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.15186" target="_blank">VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction</a></h3>







기존 3D 장면 재구성 모델은 정적인 장면을 만드는 데는 뛰어나지만, 사용자의 지시에 따라 동적으로 편집하는 기능은 부족했습니다. VGGT-Edit는 2D 이미지를 거치지 않고 3D 공간에서 직접 장면을 편집하는 새로운 피드포워드 방식을 제안하여, 상호작용이 필요한 애플리케이션에서의 활용 가능성을 높였습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Kaixin Zhu, Yiwen Tang, Yifan Yang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2605.15190" target="_blank">RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> 
</div>




  



실시간 스트리밍 비디오 생성 모델은 이전 내용을 바탕으로 미래 영상을 예측하지만, 시간이 길어질수록 생성 품질이 저하되는 문제가 있었습니다. RAVEN은 훈련 시와 추론 시의 데이터 분포 차이를 줄이는 새로운 네트워크 구조를 도입하여, 장시간에 걸쳐 일관성 있고 높은 품질의 비디오를 실시간으로 생성하는 것을 목표로 합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Yanzuo Lu, Ronglai Zuo, Jiankang Deng</span>
</div>

</div>



---


## <i data-lucide="star"></i> GitHub Trending


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/tinyhumansai/openhuman/main/gitbooks/.gitbook/assets/demo.png" alt="tinyhumansai/openhuman" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/tinyhumansai/openhuman" target="_blank">tinyhumansai/openhuman</a></h3>







OpenHuman은 개인화된 AI 초지능을 목표로 하는 프로젝트입니다. 사용자의 개인정보를 보호하면서도 간단하고 강력한 AI 경험을 제공하는 것을 특징으로 합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1272 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://opengraph.githubassets.com/auto/K-Dense-AI/scientific-agent-skills" alt="K-Dense-AI/scientific-agent-skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/K-Dense-AI/scientific-agent-skills" target="_blank">K-Dense-AI/scientific-agent-skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 저장소는 연구, 과학, 공학, 분석 등 다양한 전문 분야에서 바로 사용할 수 있는 AI 에이전트 스킬 모음입니다. 개발자들은 이 스킬들을 활용하여 특정 작업에 특화된 고성능 AI 에이전트를 더 쉽게 구축할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 643 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://skills.sh/b/anthropics/skills" alt="anthropics/skills" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/anthropics/skills" target="_blank">anthropics/skills</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  



이 프로젝트는 AI 모델 '클로드(Claude)' 개발사 앤트로픽(Anthropic)이 공개한 공식 에이전트 스킬 저장소입니다. 다양한 도구 및 API와 상호작용할 수 있는 AI 에이전트의 능력을 확장하기 위한 스킬들을 제공합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 625 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://raw.githubusercontent.com/czlonkowski/n8n-mcp/main/docs/img/skills.png" alt="czlonkowski/n8n-mcp" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/czlonkowski/n8n-mcp" target="_blank">czlonkowski/n8n-mcp</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  

  


<div class="sub-tags">
<span class="sub-tag">#MCP</span> <span class="sub-tag">#AI Coding</span> 
</div>


n8n-mcp는 Claude Desktop, Claude Code 등 다양한 AI 도구를 활용하여 n8n 워크플로우를 자동으로 생성해주는 도구입니다. 사용자가 자연어로 원하는 작업을 설명하면, AI가 이를 분석하여 복잡한 자동화 워크플로우를 대신 구축해줍니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 68 today</span> 

</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/raw/main/assets/vss-architecture.png" alt="NVIDIA-AI-Blueprints/video-search-and-summarization" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization" target="_blank">NVIDIA-AI-Blueprints/video-search-and-summarization</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> <span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> 
</div>




  

  



NVIDIA에서 제공하는 GPU 가속 비전 에이전트 및 AI 기반 영상 분석 애플리케이션 구축을 위한 레퍼런스 아키텍처 모음입니다. 이 블루프린트를 활용하면 영상 검색, 요약 등 고성능 비전 AI 서비스를 효율적으로 개발하고 배포할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 305 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Reasoning</code> <code>Distillation</code> <code>LLM</code> <code>Agent</code> <code>Multimodal</code> <code>Benchmark</code> <code>Transformer</code> <code>Inference</code> <code>Claude</code> <code>Workflow</code> 
</div>