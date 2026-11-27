---
layout: post
title: "Claude-BugHunter — 버그 바운티와 레드팀을 위한 스킬 번들"
date: 2026-11-27
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



<h3><a href="https://arxiv.org/abs/2611.34923" target="_blank">Mixture-of-Loops Transformer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


루프 트랜스포머는 공유 레이어를 재사용해 모델의 표현력을 높이지만 연산 효율성이 저하되는 한계가 있었습니다. 이를 해결하기 위해 제안된 MoLT는 키-값(KV)을 메모리로 활용하여 여러 루프와 레이어 전반에서 정보를 선택적으로 재사용합니다. 이를 통해 인접 루프 간의 효율적인 정보 전달을 실현하고 표현력과 연산 효율성의 균형을 효과적으로 개선했습니다.

<div class="item-meta">

<span class="meta-pill meta-repo"><i data-lucide="github"></i> hustvl/MoLT · ★ 77</span> 
<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 66</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.34051v1/illustration.png" alt="Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.34051" target="_blank">Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="search"></i> 추론/검색</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


선형 어텐션 기반의 Gated DeltaNet-2는 삭제와 쓰기 연산을 독립 제어하여 긴 문맥 처리 능력을 높였으나, 학습 도중 상태가 불안정해지는 문제가 있었습니다. 연구진은 이러한 학습 실패 원인이 삭제 과정에서 읽기와 수정 방향의 비대칭성으로 인해 비정규 연산자가 발생하기 때문임을 규명했습니다. 이 분석을 토대로 불안정성을 완화하여 긴 문맥에서도 안정적으로 학습할 수 있는 개선 방안을 제시했습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 50</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.34232v1/Figure_2.png" alt="OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.34232" target="_blank">OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="bot"></i> 에이전트</span> <span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  

  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


컴퓨터 조작 에이전트는 단순한 화면 클릭을 넘어 여러 운영체제를 넘나드는 복합 작업을 수행할 수 있어야 하지만, 기존 벤치마크는 단일 환경 평가에 치중되어 있었습니다. OS-Omni는 윈도우와 우분투 등 다양한 환경에서 긴 호흡의 워크플로를 직접 실행하고 검증할 수 있는 통합 벤치마크 환경을 제공합니다. 이를 통해 범용 에이전트가 멀티 플랫폼 환경에서 지속적인 애플리케이션 상태를 관리하며 현실적인 작업을 완수할 수 있는지 측정합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 38</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.34457v1/fig2.png" alt="ProxyGenBench: Benchmarking Proxy-Guided Video Generation" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.34457" target="_blank">ProxyGenBench: Benchmarking Proxy-Guided Video Generation</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="code-2"></i> 개발 도구</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Eval</span> 
</div>


최근 비디오 생성 모델의 제어력을 높이기 위해 3D 블록아웃과 같은 구조적 프록시를 가이드로 활용하는 방식이 주목받고 있습니다. 그러나 이러한 입력은 세부 정보가 생략되어 있어 구조를 유지하면서도 결측된 내용을 자연스럽게 채우고 텍스트 지시와 결합하는 능력을 정밀하게 평가해야 합니다. 이에 본 연구는 프록시 기반 비디오 생성의 구조 보존과 세부 묘사 완성도를 종합적으로 검증하는 ProxyGenBench를 제안합니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 32</span> 


</div>

</div>


<div class="digest-item has-thumb" markdown="1">


<div class="digest-thumb">
  <img src="https://arxiv.org/html/2611.34420v1/finding.png" alt="DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding" loading="lazy" referrerpolicy="no-referrer">
</div>


<h3><a href="https://arxiv.org/abs/2611.34420" target="_blank">DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#VLM</span> 
</div>


기존 다중 페이지 문서 비전-언어 모델은 각 페이지를 독립적으로 인코딩하여 페이지 경계에서 시각적 정보의 단절이 발생하는 문제를 안고 있었습니다. 연구진이 제안한 DocSEAM은 비전 인코더와 언어 모델 사이에 추가되는 경량 모듈로, 인접 페이지 간의 국소적 상호작용 정보를 효과적으로 주입합니다. 그 결과 언어 모델이 페이지 간 단절 없이 연속적인 문맥을 파악하게 되어 복잡한 다중 페이지 문서 이해 성능이 크게 향상되었습니다.

<div class="item-meta">


<span class="meta-pill meta-hf"><i data-lucide="thumbs-up"></i> 27</span> 


</div>

</div>



---


## <i data-lucide="cpu"></i> Hugging Face Blog


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.34923" target="_blank">Mixture-of-Loops Transformer</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> 
</div>


루프형 트랜스포머는 레이어를 재사용해 표현력을 높이지만 연산 효율성이 저하되는 한계가 있었습니다. 이를 해결하기 위해 루프 간 키-값 메모리를 선택적으로 재사용하는 MoLT(Mixture-of-Loops Transformer) 모델이 제안되었습니다. 이 방식은 루프 간 연결 구조를 개선하여 모델의 표현력과 연산 효율성을 동시에 극복합니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Lianghui Zhu, Shijie Wang, Xinggang Wang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.34941" target="_blank">Improving and Expanding Video Editing Capabilities Without Videos</a></h3>







비디오 편집 모델은 쌍을 이루는 학습 데이터의 부족으로 인해 이미지 편집 기술에 비해 발전이 더뎠습니다. 연구진은 새로운 비디오 데이터셋 없이도 이미지 편집기의 성능을 비디오 편집기로 전이하는 I2VT 기법을 제시했습니다. 이를 통해 모델 구조 변경 없이 효율적인 사후 학습만으로 비디오 편집 역량을 크게 확장할 수 있습니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Ji Xie, Yanhao Jia, Xiangpeng Yang</span>
</div>

</div>


<div class="digest-item" markdown="1">



<h3><a href="https://huggingface.co/papers/2611.34929" target="_blank">High-Fidelity Image Matting with Pixel-Space Diffusion Transformers</a></h3>


<div class="categories">
<span class="category-tag"><i data-lucide="brain"></i> 모델/아키텍처</span> 
</div>




  


<div class="sub-tags">
<span class="sub-tag">#Transformer</span> <span class="sub-tag">#Diffusion</span> 
</div>


기존의 잠재 확산 모델 기반 이미지 매팅은 이미지 압축 과정에서 정밀한 고주파 정보가 손실되는 문제가 있었습니다. 본 연구에서는 픽셀 공간 확산 트랜스포머를 매팅 작업에 적용한 고화질 프레임워크인 PixelMatte를 제안합니다. 이 모델은 대규모 사전 학습에서 얻은 생성 능력을 활용하여 미세한 디테일까지 정교하게 분리해 냅니다.

<div class="item-meta">




<span class="meta-pill meta-author"><i data-lucide="user"></i> Baihan Yang, Xin Lin, Yufan Wei</span>
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


버그 바운티와 외부 레드팀 모의해킹 작업을 위해 개발된 Claude Code 전용 스킬 번들입니다. 24개 핵심 취약점 분류와 681개의 실제 공개 보고서 패턴을 기반으로 한 85개의 스킬 및 16개의 슬래시 명령어를 제공합니다. 또한 엔터프라이즈 신원 및 인프라 공격 매트릭스까지 포함하여 체계적인 보안 점검을 돕습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 1597 today</span> 

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




  



단 2시간 만에 바닥부터 자신만의 64M 규모 경량 LLM을 직접 학습시킬 수 있는 오픈소스 프로젝트입니다. 거대 언어 모델의 전체 학습 파이프라인을 빠르고 직관적으로 경험할 수 있도록 구성되어 있습니다. 초보자나 연구자가 언어 모델의 사전 학습 및 미세조정 원리를 비용 부담 없이 실습하기에 매우 적합합니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 702 today</span> 

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




  



인텔이 개발한 오픈소스 툴킷으로, 딥러닝 인공지능 모델의 추론 성능을 최적화하고 다양한 하드웨어에 배포할 수 있도록 돕습니다. 단 한 번의 최적화로 CPU, GPU, VPU 등 다양한 엣지 및 클라우드 장비에서 효율적으로 모델을 실행할 수 있습니다. 컴퓨터 비전과 음성, 대규모 언어 모델까지 폭넓은 AI 워크로드의 처리 속도를 크게 향상시킵니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 176 today</span> 

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


Claude Code, GitHub Copilot, Cursor 등 다양한 AI 코딩 어시스턴트에서 깔끔하고 정돈된 다이어그램을 생성할 수 있도록 지원하는 디자인 도구입니다. 복잡한 외부 라이브러리 없이 독립적인 HTML과 SVG 형태로 52가지 유형의 고품질 에디토리얼 다이어그램을 구현합니다. 불필요한 시각적 효과를 배제하고 직관적인 정보 전달에 집중하여 가독성이 뛰어납니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 955 today</span> 

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




  



레딧, X, 유튜브, 해커뉴스, 폴리마켓 등 다양한 플랫폼과 웹 전반을 실시간으로 탐색하는 AI 에이전트용 리서치 스킬입니다. 사용자가 지정한 주제에 대해 최근 30일간의 데이터를 빠르게 수집하고 신뢰도 높은 요약 보고서를 합성해 냅니다. 최신 트렌드와 여론, 시장 동향을 하나의 워크플로우에서 포괄적으로 파악할 때 유용하게 활용할 수 있습니다.

<div class="item-meta">



<span class="meta-pill meta-stars"><i data-lucide="star"></i> 759 today</span> 

</div>

</div>



---



## <i data-lucide="bar-chart-3"></i> 오늘의 키워드

<div class="keywords">
<code>Transformer</code> <code>Retrieval</code> <code>Eval</code> <code>Agent</code> <code>Benchmark</code> <code>Vision</code> <code>Claude</code> <code>Red-team</code> <code>Claude Code</code> <code>LLM</code> 
</div>