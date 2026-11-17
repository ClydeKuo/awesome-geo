# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | **한국어** | [Español](README.es.md) | [Deutsch](README.de.md)

> 생성형 엔진 최적화(GEO) 관련 자료를 엄선한 목록으로, 연구 논문, 가이드, 기술 표준, 도구, 세계 각지의 AI 검색 엔진을 정리했습니다.

## 목차

- [GEO 소개](#geo-소개)
- [입문](#입문)
- [연구 논문](#연구-논문)
  - [기초 논문](#기초-논문)
  - [벤치마크와 데이터셋](#벤치마크와-데이터셋)
  - [공격과 조작](#공격과-조작)
  - [인용 및 가시성 분석](#인용-및-가시성-분석)
  - [서베이 논문](#서베이-논문)
- [가이드와 아티클](#가이드와-아티클)
  - [전략](#전략)
  - [콘텐츠 작성](#콘텐츠-작성)
  - [기술 구현](#기술-구현)
  - [업계 보고서와 데이터](#업계-보고서와-데이터)
- [표준과 기술 사양](#표준과-기술-사양)
  - [llms.txt](#llmstxt)
  - [AI 크롤러와 robots.txt](#ai-크롤러와-robotstxt)
  - [구조화된 데이터](#구조화된-데이터)
  - [엔진별 공식 문서](#엔진별-공식-문서)
- [도구](#도구)
  - [AI 가시성 모니터링](#ai-가시성-모니터링)
  - [콘텐츠 진단과 최적화](#콘텐츠-진단과-최적화)
  - [오픈 소스 도구와 라이브러리](#오픈-소스-도구와-라이브러리)
  - [llms.txt 생성기](#llmstxt-생성기)
  - [크롤러 로그 분석](#크롤러-로그-분석)
- [AI 검색 엔진과 어시스턴트](#ai-검색-엔진과-어시스턴트)
  - [글로벌](#글로벌)
  - [중국](#중국)
  - [일본](#일본)
  - [한국](#한국)
  - [유럽](#유럽)
  - [기타 지역](#기타-지역)
- [언어별 GEO 자료](#언어별-geo-자료)
  - [중국어](#중국어)
  - [일본어](#일본어)
  - [한국어](#한국어)
  - [스페인어](#스페인어)
  - [독일어](#독일어)
- [사례 연구](#사례-연구)
- [강의, 영상, 팟캐스트](#강의-영상-팟캐스트)
- [뉴스레터와 커뮤니티](#뉴스레터와-커뮤니티)
- [다른 큐레이션 목록](#다른-큐레이션-목록)
- [라이선스](#라이선스)

**범례:** 🆓 무료, 🪙 부분 유료, 💲 유료, 🔓 오픈 소스

## GEO 소개

생성형 엔진 최적화(GEO)는 ChatGPT, Perplexity, Google AI Overviews 같은 AI 답변 엔진이 콘텐츠를 쉽게 찾고 이해하며 인용할 수 있도록 만드는 작업입니다. SEO가 검색 결과 목록에서 순위를 다툰다면 GEO는 AI가 생성한 답변 안에서 콘텐츠가 직접 인용되거나 언급되는 것을 목표로 하며, 따라서 성과도 클릭 수보다 인용과 가시성으로 측정합니다. 이 개념은 프린스턴 대학교 등의 Aggarwal 외 연구진이 KDD 2024에서 발표한 논문 “GEO: Generative Engine Optimization”에서 처음 제시되었습니다.

## 입문

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - 생성형 엔진 최적화(GEO)를 AI 답변에서 인용과 언급을 얻는 일로 정의하고 SEO 기본기 위에 어떻게 쌓이는지 설명하는 Search Engine Land 해설 기사입니다.
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - 생성형 엔진 최적화(GEO)를 정의하고 용어의 기원을 2023년 논문에서 찾으며, AEO, LLMO 등 관련 명칭과 비판을 정리한 백과사전 항목입니다.
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - AEO와 GEO를 일반 SEO의 일부로 보고 llms.txt와 청킹의 효과를 부정한 2026년 5월 Google 가이드를 다룬 Search Engine Journal 기사입니다.
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - AI 기능을 위한 최적화도 결국 SEO라고 밝히고 llms.txt나 청킹 같은 전술은 필요하지 않다고 정리한 Google의 공식 가이드입니다.
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - SEO와 GEO의 목표, 측정 방식, 공통 관행을 비교한 Search Engine Land 기사입니다.
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - 생성형 엔진 최적화(GEO)라는 용어의 기원을 Aggarwal 등의 KDD 2024 논문에서 찾고, 업계 정의를 비교하며 AI 가시성에 관해 알려진 내용을 요약한 해설 글입니다.

## 연구 논문

### 기초 논문

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - 콘텐츠마다 9가지 GEO 전략을 평가하고 밴딧 기법으로 최적 전략 선택 속도를 높이는 에이전트 시스템을 시연한 논문입니다. (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - 정적 휴리스틱과 단일 프롬프트 재작성을 넘어 요약형 답변에서 가시성을 높이는 자기 진화형 GEO 에이전트 시스템을 제안한 논문입니다. (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - GEO를 경쟁자를 고려한 전략 선택 문제로 정식화하고, 조합 구조 위의 베이지안 최적화로 재작성 전략을 고르는 논문입니다. (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - 개별 문서가 생성형 엔진에 인용되지 않는 원인을 진단하고, 일괄적인 재작성 규칙 대신 맞춤형 수정을 적용하는 논문입니다. (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - GEO를 전략 학습으로 보고, 계획·편집·평가 에이전트로 여러 작업과 엔진에서 재사용 가능한 편집 전략을 추출하는 논문입니다. (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - 여러 쿼리에서 충돌하는 수정 요구를 발산 후 수렴 프레임워크로 해결해 최적화 선호를 찾아내고 하나의 수정안으로 통합하는 논문입니다. (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - 생성형 엔진이 인용하는 페이지에 영향을 주도록 여러 계층 수준에서 콘텐츠 구조를 설계하는 프레임워크 GEO-SFE를 제안한 논문입니다. (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - 해석 가능한 페이지의 구조, 콘텐츠, 언어 특징을 최적화해 인용 가시성과 콘텐츠 품질의 균형을 맞추는 FeatGEO를 제안한 논문입니다. (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - 여행 웹사이트 텍스트로 만든 합성 쌍으로 BART-base 모델을 미세 조정해 LLM 출력에서 더 잘 발견되도록 콘텐츠를 재작성한 논문입니다. (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - 사용자 의도와 역할을 미리 추론해 대상 쿼리나 엔진 피드백 없이 생성형 검색 엔진에 맞게 콘텐츠를 최적화하는 논문입니다. (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - 생성형 엔진이 검색된 콘텐츠에서 선호하는 특성을 학습하고 그에 맞춰 웹 페이지를 재작성해 가시성을 높이는 AutoGEO를 제시한 논문입니다. (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - 생성형 AI 기반의 화이트햇 검색 엔진 최적화 기법을 제시하고 실증적 개선 효과를 보고한 논문입니다. (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - 생성형 엔진 최적화(GEO) 개념과 생성형 엔진 답변 속 콘텐츠 가시성을 측정하는 벤치마크를 제안한 논문입니다. (2023)

### 벤치마크와 데이터셋

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - 작업, 도메인, 도입자 수에 따라 대화형 SEO 기법을 벤치마크해 대부분 효과가 없고 기존 SEO가 더 나은 경우가 많음을 보인 논문입니다. (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - 사람이 검증한 쿼리와 통제된 조건에서, 표적 허위 정보를 담은 GEO 최적화 문서에 대한 방어 기법을 벤치마크합니다. (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - 실제 생성형 엔진이 페이지를 가져와 순위를 매기는 라이브 웹에서도 GEO 가시성 향상이 유지되는지 검증하는 LIVE-GEO를 제안한 논문입니다. (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - 이커머스에서 여러 생성형 엔진의 GEO 재작성 휴리스틱을 시험하도록 소비자 상품 쿼리 1만 3,746개와 검색된 상품 목록을 제공합니다. (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - 검색된 근거를 인용하는 LLM 답변의 유창성, 정확성, 인용 품질을 자동 지표로 평가하는 벤치마크 ALCE를 제안한 논문입니다. (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - 통일된 데이터셋과 지표를 갖춘 단일 프로토콜로 GEO 순위 조작 공격을 평가하고 공격 강도와 탐지 가능성을 비교한 논문입니다. (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - 사용자 쿼리 1만 1,500개의 데이터셋을 공개하고 Google 검색, AI Overviews, Gemini가 제공하는 출처와 정보를 비교한 논문입니다. (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - 생성뿐 아니라 검색과 순위까지 포함해 검색 증강 GEO 전략을 엔드투엔드로 평가하는 환경을 제공합니다. (2026)

### 공격과 조작

프롬프트 인젝션이나 순위 조작 공격 등으로 AI 답변 엔진이 조작되는 방식과 그 방어 방법을 다루는 적대적 GEO 연구입니다.

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - LLM이 생성하는 상품 추천에서 항목이 나타나는 위치를 제어하는 최적화 기법 CORE를 제안한 논문입니다. (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - AI 검색용 llms.txt 방식 매니페스트에 관한 근거를 검토해 자동 수집이 거의 없음을 밝히고 보안상의 영향을 평가한 논문입니다. (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - GEO 공격이 콘텐츠 품질을 떨어뜨리는 인용 전쟁으로 번질 수 있음을 보이고, 상생 결과를 위한 메커니즘 설계를 연구한 논문입니다. (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - 이미지 교란과 텍스트를 함께 설계하면 시각 언어 모델의 상품 순위를 조작할 수 있음을 보인 논문입니다. (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - GEO가 영향력 집중, 공개되지 않은 상업적 영향, 학계와 업계의 사각지대라는 위험을 낳는다고 주장하고, 공개·감사 등 답변 단위 거버넌스를 요구하는 논문입니다. (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - 판매자가 자기 상품을 상위에 올리려고 콘텐츠에 심는 설득 구조를 탐지해 LLM 기반 순위를 방어하는 논문입니다. (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - 사실 관계는 유지해 팩트 체크와 퍼플렉서티 필터를 피하는 악의적 GEO 재작성으로부터 생성형 검색을 방어하는 논문입니다. (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - LLM 검색의 순위 조작 공격을 무한 반복 죄수의 딜레마로 모델링하고 협력이 유지되는 조건을 분석한 논문입니다. (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - 생성형 엔진이 어떤 퍼블리셔를 인용하는지, 공격자가 답변의 출처에 악성 콘텐츠를 주입하기가 얼마나 어려운지 분석한 논문입니다. (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - 에너지 기반 최적화로 자연스럽고 탐지하기 어려운 프롬프트를 만들어 LLM 기반 순위를 조작하는 공격을 제시한 논문입니다. (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - 여러 공격자가 같은 쿼리를 서로 다른 목표로 유도하는 RAG 시스템의 경쟁적 포이즈닝 공격을 연구하고 PoisonArena 벤치마크를 제안하는 논문입니다. (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - LLM의 선택을 공격자 콘텐츠 쪽으로 유도하는 선호 조작 공격을 제시하고, 이 공격이 판매자 사이에 죄수의 딜레마를 만든다는 점을 보인 논문입니다. (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - 많은 RAG 시스템의 검색 계층인 밀집 임베딩 검색에 걸리도록 적대적 문단을 만드는 SEO형 공격을 연구한 논문입니다. (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - 상품 페이지에 전략적으로 설계한 텍스트 시퀀스를 넣으면 LLM 기반 검색 엔진이 그 상품을 가장 먼저 추천하게 만들 수 있음을 보인 논문입니다. (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - 실제 소비자 상품 페이지를 이용해 웹 페이지 텍스트 속 프롬프트 인젝션이 대화형 검색 결과에서 출처의 순위를 끌어올릴 수 있음을 보인 논문입니다. (2024)

### 인용 및 가시성 분석

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - AI Overviews와 AI Mode를 없애면 퍼블리셔로 가는 클릭이 늘어난다는 사전 등록 현장 실험(N=1,100) 결과를 보고한 논문입니다. (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - 똑같이 근거가 되는 두 출처 중 에이전트 검색 엔진이 무엇을 인용하는지가 문서 제시 방식에 따라 어떻게 바뀌는지 인과적으로 진단한 논문입니다. (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - AI 검색 답변이 실행, 프롬프트, 시점에 따라 달라지므로 가시성을 한 번이 아니라 반복해 측정해야 함을 보인 논문입니다. (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - 인용 선택과 인용 흡수를 구분하고 ChatGPT, Google AI, Perplexity에서 프롬프트 602개를 분석한 논문입니다. (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - 프롬프트 관측치 약 3만 5,000건을 분석해 브랜드 자체 도메인이 실시간 검색에 나타나면 브랜드 언급률이 급격히 오른다는 결과를 보인 논문입니다. (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - ChatGPT, Claude, Perplexity, Gemini 전반의 브랜드 가시성 측정 방법을 연구하고, 엔진이 브랜드를 인용할 때 의존하는 출처도 분석한 논문입니다. (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - GEO 가시성 점수가 프롬프트 코퍼스와 가중치에 좌우되며, 이 둘이 실제 수요와 다를 수 있는 답변 시장을 규정한다고 주장하는 논문입니다. (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - 쿼리 5만 5,393개를 40일간 추적해 AI Overviews의 노출 조건, 출처 품질, 주장의 충실도, 퍼블리셔에 미치는 영향을 측정한 논문입니다. (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - Google 검색 결과와 생성형 AI 답변이 인용 도메인, 도메인 유형, 쿼리 의도, 최신성에서 어떻게 다른지 정량화한 논문입니다. (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - ChatGPT, Copilot, Google, Perplexity를 진단해 엔진 간 겹치는 URL이 매우 적어 엔진 무관 GEO 점수에 한계가 있음을 밝힌 논문입니다. (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - 쿼리 712개로 생성형 검색 엔진 4곳을 진단해 인용 출처의 약 16%가 AI 생성 콘텐츠로 보인다는 결과를 제시한 논문입니다. (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - Google AI Overviews와 Reddit 데이터로 AI 검색이 인용된 커뮤니티의 참여를 높였고 그 효과가 AI Mode 출시 후 줄었음을 보인 논문입니다. (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - ChatGPT Web 설정 4가지의 쿼리 재작성, 페이지 검색, 인용 선택을 관찰해 검색 빈도가 인용을 예측한다는 결과를 보인 논문입니다. (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - 쿼리 614개로 중국어 생성형 검색 플랫폼 4곳의 인용 행태, 출처 표기, 엔티티 노출을 분석한 논문입니다. (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - 답변 15만 8,099건을 분석해 ChatGPT가 재작성한 하위 쿼리로 검색하는 페이지가 페이지 속성보다 인용을 훨씬 잘 설명함을 보인 논문입니다. (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - 16개 항목의 페이지 진단을 제시하고, 세 엔진에서 메타데이터, 시맨틱 HTML, 구조화된 데이터가 인용과 가장 관련이 깊다는 결과를 보인 논문입니다. (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - 여러 업종과 언어에 걸친 통제 실험으로 AI 검색 엔진과 Google을 비교해 브랜드 자체 콘텐츠보다 언드 미디어를 크게 선호한다는 결과를 보인 논문입니다. (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - ConflictingQA를 구축해 LLM이 페이지와 쿼리의 관련성에 크게 의존하고 과학적 참고 문헌 같은 문체 단서는 대체로 무시함을 보인 논문입니다. (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - Bing Chat, NeevaAI, Perplexity, YouChat의 인용 재현율과 정밀도를 진단해 많은 문장이 인용으로 충분히 뒷받침되지 않음을 밝힌 논문입니다. (2023)

### 서베이 논문

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - 2023~2026년 연구 45편을 검토해 GEO를 다단계 확률적 파이프라인으로 보고, GEO 관련 주장을 평가하는 체크리스트를 제시한 서베이 논문입니다. (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - LLM 기반 검색 에이전트를 아키텍처, 최적화, 응용, 평가 기준으로 체계적으로 분류하고 남은 과제를 정리한 서베이 논문입니다. (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - 대규모 언어 모델 기반의 생성형 검색과 추천을 기술적 관점에서 정리한 서베이 논문입니다. (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - LLM 개선을 위한 검색과 검색 개선을 위한 LLM을 아울러 검색 엔진과 LLM이 서로 도울 수 있는 방식을 살펴본 논문입니다. (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - 쿼리 재작성, 검색, 재순위화, 읽기 등 정보 검색 시스템 전반에서 대규모 언어 모델이 활용되는 방식을 정리한 서베이 논문입니다. (2023)

## 가이드와 아티클

### 전략

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - 생성형 엔진 최적화(GEO)가 AI 기반 검색 결과에 콘텐츠가 노출되도록 돕는 방식을 실무 관점에서 소개합니다. (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - 생성형 엔진 최적화(GEO)의 개념과 SEO와의 차이, AI 답변에 인용되는 데 도움이 되는 기법을 설명하며 내려받을 수 있는 진단 체크리스트를 제공합니다. (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - AI 검색과 기존 검색의 차이, 5가지 GEO 전술, GEO 성과 측정법을 설명하며 AI 검색도 여전히 기존 검색에 의존한다고 짚습니다. (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - 검색이 링크 기반 순위에서 언어 모델 답변으로 옮겨 가고 있다고 주장하며, GEO를 약 800억 달러 규모 SEO 시장의 다음 단계로 규정합니다. (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - Structure, Evidence, Entity, Notability의 4계층 GEO 프레임워크 SEEN과 0·1점으로 가장 약한 계층을 찾는 41개 항목 체크리스트를 다룹니다. (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - 우선순위 주제와 기준선 설정부터 인용 출처 분석, 콘텐츠 개선, 성과 보고까지 10단계 생성형 엔진 최적화(GEO) 프로세스를 안내합니다. (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - AEO와 SEO의 차이, 답변 엔진의 작동 방식, AI 가시성 추적, 프롬프트 선정, AI 답변 속 오류 수정을 다루는 8부작 AEO 가이드의 첫 글입니다. (2025)

### 콘텐츠 작성

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - Google AI Overviews의 개념과 웹 출처에서 생성되는 방식, 사이트 소유자가 이에 맞춰 최적화하고 가시성을 추적하는 방법을 설명합니다. (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - ChatGPT 인용을 검색되는 단계와 인용할 만한 내용이 되는 단계로 나눠 설명하고, 인용 도메인의 AI 크롤러 허용 여부 등 자체 측정으로 각 단계를 뒷받침합니다. (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - ChatGPT에서 진행한 구매자 질문 테스트 13건과 자사 서버 로그가 보여 준 결과를 부정적 결과까지 포함해 전하고, 허용할 AI 크롤러를 정리합니다. (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - 키워드 리서치부터 서식까지, ChatGPT와 Google 같은 AI 검색 엔진에 콘텐츠가 인용되도록 하는 7단계를 안내합니다. (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - AI 시스템이 추출하기 쉬운 콘텐츠를 만들고 사이트 밖에서 합의를 쌓아 ChatGPT 검색에서 순위를 높이는 8단계를 제시합니다. (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - LLM 최적화(LLMO) 관점에서 LLM이 생성한 답변 속 브랜드 가시성을 높이는 10가지 방법을 소개합니다. (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - 스키마, 명확한 제목, 독립형 Q&A 블록 등 AI 검색 답변용 콘텐츠 요건과 탭·PDF에 답변을 숨기는 실수를 다룬 Microsoft Advertising 가이드입니다. (2025)

### 기술 구현

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - Google Tag Manager 등으로 클라이언트 측에서 삽입한 JSON-LD는 JavaScript를 실행하지 못하는 AI 크롤러가 놓친다는 조사 결과를 전합니다. (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - ChatGPT, Gemini 등에서 유입되는 AI 추천 트래픽을 Google Analytics 4에서 추적하는 방법을 설명합니다. (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - AI 에이전트에 페이지를 Markdown으로 제공하는 기능을 소개하며, 한 게시물이 HTML 1만 6,180토큰에서 Markdown 3,150토큰으로 줄어든 예를 보여 줍니다. (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - ChatGPT, Claude 등 AI 크롤러의 JavaScript와 콘텐츠 유형 처리 방식을 MERJ와 Vercel 데이터로 보여 주고 사이트 소유자를 위한 권고를 제시합니다. (2024)

### 업계 보고서와 데이터

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - 웹사이트 3,000곳을 조사해 AI 챗봇 유입 트래픽을 추정한 연구로, 63%가 AI 트래픽을 받고 그중 98%가 챗봇 3개에서 온다는 결과입니다. (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - 업종 중심 데이터와 크롤링 목적별 AI 크롤러 트래픽 분석을 Cloudflare Radar에 추가한 내용을 소개합니다. (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - AI 인용 3,100만 건과 퍼블리셔 105곳의 robots.txt를 분석해 AI 크롤러 차단이 일부 모델에는 효과가 있지만 다른 모델에는 효과가 없음을 밝힙니다. (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - 16개월간의 데이터로 AI Overviews 인용과 자연 검색 순위의 겹침이 32%에서 54%로 늘었음을 보여 주며 업종별 분석도 제공합니다. (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - AI Overviews가 클릭 수를 34.5% 줄인다는 Ahrefs 연구 결과로, 클릭이 늘어난다는 Google의 주장을 반박합니다. (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - AI 검색 도구 8개를 뉴스 발췌문으로 시험해 쿼리의 60% 이상에서 출처를 잘못 인용한다는 결과를 제시합니다. (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - ChatGPT, Gemini, Claude의 시장 점유율, 유입 트래픽, 인용, AI 답변 속 광고에 관한 2026년 Similarweb 데이터를 모았습니다. (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - 브랜드 7만 5,000개를 분석해 AI Overviews의 브랜드 언급에 가장 큰 영향을 줄 가능성이 높은 검색 요인을 찾습니다. (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - 2025년 3월 Google 사용자의 행동을 비교해 AI 요약을 본 사용자가 다른 웹사이트 링크를 클릭할 가능성이 더 낮다는 결과를 제시합니다. (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - ChatGPT, Gemini, Copilot, Google에서 인용 3만 7,500건을 추적해 절반이 다음 날 사라지고 대부분 다시 나타난다는 결과를 제시합니다. (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - 도메인 30만 개를 조사해 llms.txt의 사용 범위와 이 파일이 LLM의 도메인 인용 빈도에 영향을 주는지 살펴봅니다. (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - 2024년 11월부터 2026년 3월까지의 로그 파일 약 70억 개를 분석해 OpenAI 크롤러 3종이 웹을 어떻게 크롤링하는지 보여 줍니다. (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - 생성형 AI가 뉴스 업계를 재편하면서 ChatGPT 뉴스 쿼리가 212% 급증하고 퍼블리셔 트래픽이 26% 감소했다고 보고합니다. (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - 키워드 1,000만 개 이상을 분석해 Google AI Overviews가 검색을 어떻게 바꾸고 있으며 SEO에 어떤 의미가 있는지 보여 줍니다. (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - SERP 86만 3,000개를 분석해 AI Overviews 인용의 38%가 상위 10위 페이지에서 나오며, 1년 전 76%보다 줄었다는 결과를 제시합니다. (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - JSON-LD를 추가한 페이지 1,885개를 추적해 Google AI Overviews, AI Mode, ChatGPT 인용에 미친 영향을 측정합니다. (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - 프롬프트 140만 개를 분석해 페이지 제목, URL, 스니펫이 ChatGPT가 검색한 페이지 중 어느 것을 인용하는지에 미치는 영향을 보여 줍니다. (2026)

## 표준과 기술 사양

AI 크롤러가 사이트에 접근하는 방식과 AI 답변 엔진이 콘텐츠를 읽는 방식을 규정하는 사양과 공식 문서입니다.

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - llms.txt 제안의 원본 소스 코드와 참조 도구, 관련 논의를 담은 저장소입니다.
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - John Mueller가 llms.txt를 현재로서는 추측에 가깝다고 평가하고 Google이 지원하는 대안 WebMCP를 선호한다고 밝힌 내용을 전합니다.
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - 서버 로그상 현재 llms.txt를 사용하는 AI 시스템이 없다는 John Mueller의 발언을 전합니다. (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - llms.txt를 도입한 웹사이트 디렉터리로, API, 플랫폼, 개발자 도구의 예시 파일을 제공합니다.
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - 2026년 9월 조사에서 상위 1,000개와 상위 1만 개 도메인의 llms.txt 도입률을 측정하고 방법론과 내려받을 수 있는 데이터를 제공합니다. (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - 개발자가 실제 사례를 살펴볼 수 있도록 llms.txt 파일을 게시한 웹사이트를 모은 목록입니다.
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - llms.txt를 게시한 사이트를 나열하고, 각 사이트가 선언한 학습, 검색, 요약에 대한 AI 허용 범위를 보여 줍니다.
- [The /llms.txt file](https://llmstxt.org) 🆓 - 사이트 루트에 두는 Markdown 파일 /llms.txt로 언어 모델에 사이트 개요와 가장 유용한 콘텐츠 링크를 제공하자는 제안입니다. (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - Vercel, Google, Anthropic 사례로 llms.txt의 가치를 주장하고, 일반적인 SEO 관행으로 충분하다는 비판에 반론을 제시합니다. (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - llms.txt 파일이 무엇인지 설명하고, 이 파일을 추가하는 것이 개발자와 마케터에게 실제로 효과가 있는지 검토합니다.

### AI 크롤러와 robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - 운영사 12곳의 AI 크롤러 사용자 에이전트 25개를 4개 그룹으로 나누고, 플랫폼 157곳 중 각각을 robots.txt로 차단하는 곳의 수를 정리합니다. (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - 사이트 소유자가 AI 학습을 거부할 때 쓸 수 있는 robots.txt 항목, 메타 태그 등 알려진 설정을 모았습니다.
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - 차단할 AI 에이전트와 크롤러를 커뮤니티가 함께 관리하는 목록으로, 자동 생성된 robots.txt와 서버 설정 파일을 제공합니다.
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - Amazonbot, Amzn-SearchBot, Amzn-User와 각 크롤러를 개별적으로 제어하는 robots.txt 설정을 설명합니다.
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - 사이트 소유자가 AI 크롤러에 접근 비용을 청구하고 미결제 요청에는 HTTP 402로 답하는 Pay Per Crawl을 설명하며, 현재 비공개 베타입니다.
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - Google 소리 내어 읽기처럼 사용자 요청에 따라 작동하는 Google 페처를 나열하고, 이들이 대체로 robots.txt 규칙을 따르지 않는다고 설명합니다.
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - Googlebot을 포함한 Google의 일반 크롤러를 사용자 에이전트 문자열, robots.txt 토큰과 함께 설명하는 문서입니다.
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - Yandex 로봇 사용자 에이전트 약 40개의 용도와 robots.txt 처리 방식을 정리하고, 역방향 DNS로 확인하는 방법을 설명합니다.
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - AI의 콘텐츠 수집·이용에 관한 선호를 표현하는 공통 어휘와, robots.txt나 HTTP 헤더 같은 부착 방식을 표준화합니다.
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - IP 허용 목록과 사용자 에이전트 문자열을 대신해 AI 크롤러, 에이전트 등 자동화 클라이언트를 암호학적으로 인증하는 방법을 표준화합니다.
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - DuckAssistBot이 DuckDuckGo의 AI 보조 답변에 쓸 출처를 수집하며, AI 학습에는 쓰이지 않고 robots.txt로 차단할 수 있다고 설명합니다.
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - Meta AI 검색용 Meta-WebIndexer, AI 모델 학습용 Meta-ExternalAgent 등 Meta 크롤러와 각각의 용도를 정리합니다.
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - MistralAI-User, MistralAI-Index, MistralAI-Training 사용자 에이전트와 각각의 용도를 설명합니다.
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - AI 크롤러가 준수해야 할 로봇 배제 프로토콜인 robots.txt의 문법과 의미를 규정한 사양입니다. (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - IETF AIPREF 초안을 바탕으로 robots.txt의 공통 AI 학습 거부 설정을 따를 계획이며 2027년 지원을 목표로 한다는 Google의 발표입니다. (2026)

### 구조화된 데이터

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - Google이 구조화된 데이터 마크업으로 콘텐츠를 이해하는 방식과 지원 형식, 마크업 위치를 설명합니다.
- [JSON-LD](https://json-ld.org) 🆓 - Schema.org 마크업 작성에 흔히 쓰이는 JSON 기반 링크드 데이터 형식인 JSON-LD의 사양을 게시합니다.
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - URL이나 코드 스니펫을 테스트해 구조화된 데이터로 생성될 수 있는 Google 리치 결과를 알려 주는 도구입니다.
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - 이미 AI에 인용된 페이지에 스키마 마크업을 추가하면 인용률이 오르는지 시험한 Ahrefs 보고서를 요약합니다. (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - JSON-LD, Microdata, RDFa로 작성된 모든 Schema.org 유형의 구조화된 데이터를 검증합니다.
- [Schema.org](https://schema.org) 🆓 - 검색 엔진 등이 웹 페이지를 해석할 수 있도록 마크업하는 데 쓰는 공통 유형·속성 어휘를 게시합니다.
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - Schema.org 어휘의 소스 코드와 이를 지원하는 소프트웨어를 담은 저장소입니다.
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - Google 검색 기능을 구동하는 구조화된 데이터 유형을 예시, 구현 가이드와 함께 정리한 목록입니다.

### 엔진별 공식 문서

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - Spotlight, Siri, Safari 검색에 쓰이는 Applebot과, 차단하면 생성형 AI 학습을 거부할 수 있는 Applebot-Extended를 설명합니다.
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - Google 검색의 AI Overviews와 AI Mode가 작동하는 방식과 사이트 소유자가 콘텐츠 포함 여부에 대응하는 방법을 설명합니다.
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - 사이트 리소스 제출, 크롤링 및 robots 데이터, 검색 위젯, AI 트래픽 분석 기능을 갖춘 Baidu의 웹마스터 플랫폼입니다.
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - Common Crawl 공개 웹 아카이브를 수집하는 크롤러 CCBot의 사용자 에이전트와 검증·차단 방법을 설명합니다.
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - ClaudeBot, Claude-User, Claude-SearchBot 크롤러와 사이트 소유자가 robots.txt로 각각을 차단하는 방법을 설명합니다.
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - 참여 검색 엔진에 새로 추가, 수정, 삭제된 URL을 알리는 IndexNow 프로토콜 문서입니다.
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - Microsoft Copilot과 Bing의 AI 생성 요약에서 사이트가 답변에 인용되는 시점을 보여 주는 Bing Webmaster Tools 보고서를 발표한 글입니다. (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - AI Overviews, AI Mode 등 생성형 AI 기능에 페이지가 노출되는 빈도를 페이지, 국가, 기기, 날짜별로 보여 주는 Search Console 보고서를 발표합니다. (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - Perplexity가 참여 퍼블리셔와 수익을 나누고 API 이용과 개발 지원을 제공하는 프로그램을 발표합니다. (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - 네이버 검색이 사이트를 발견하고 색인하는 데 필요한 사항을 다루는 네이버의 웹마스터 가이드와 도구로, AI 브리핑도 같은 색인의 웹 문서를 활용합니다.
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - OAI-SearchBot, GPTBot, ChatGPT-User, OAI-AdsBot 사용자 에이전트와 각각의 용도를 설명합니다.
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - 검색 결과 노출용 PerplexityBot과, 사용자 요청 시 페이지를 가져오고 대개 robots.txt를 무시하는 Perplexity-User를 설명합니다.
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - ChatGPT 검색 노출, OAI-SearchBot 크롤러, ChatGPT 유입 트래픽에 관한 퍼블리셔와 개발자의 질문에 답합니다.
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - AI Overviews, AI Mode, Discover 생성형 AI에 콘텐츠를 포함·제외하는 Search Console 설정을 설명하며 AI 학습과는 무관하다고 밝힙니다.
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Yandex AI 답변이 질문을 여러 부분으로 나누고 출처를 골라 분석한 뒤 답변에 링크하는 방식을 설명하는 도움말입니다.
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Google 검색의 AI 기능에서 콘텐츠가 좋은 성과를 내도록 Google이 권장하는 방법을 소개합니다. (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Yandex 검색에서 사이트 소유권 확인, 색인 현황 모니터링, 크롤링 문제 진단을 할 수 있는 Yandex의 웹마스터 서비스입니다.
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - AI 학습과 그라운딩 설정을 분리해 robots.txt, 메타 태그, X-Robots-Tag로 지정하고 Microsoft가 2027년 2월부터 읽는다고 발표합니다. (2026)

## 도구

### AI 가시성 모니터링

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - 가입 없이 ChatGPT, Gemini, Perplexity, Copilot, AI Overviews가 브랜드를 어떻게 언급·인용하는지 확인하는 도구입니다.
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - 프롬프트 DB나 자체 프롬프트로 AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini, Copilot 답변의 브랜드 노출 빈도를 보고합니다.
- [AthenaHQ](https://athenahq.ai) 🪙 - ChatGPT, Perplexity, Gemini, AI Overviews, Copilot 등의 브랜드 가시성 추적, 콘텐츠 수정안, 시작 크레딧이 든 무료 요금제를 제공합니다.
- [Geoptie](https://geoptie.com) 💲 - ChatGPT, Gemini, Claude, Perplexity, Google AI가 구매자 프롬프트에 어떻게 답하고 어떤 출처를 인용하는지 보여 줍니다.
- [Goodie](https://higoodie.com) 💲 - ChatGPT, AI Overviews, Perplexity, Copilot 등의 브랜드 가시성을 추적해 최적화 방안을 제안하며, 상위 요금제는 더 많은 엔진을 지원합니다.
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - ChatGPT, Perplexity, Gemini가 브랜드를 어떻게 설명하는지 1회 무료로 평가하며, 유료 주간 모니터링은 HubSpot AEO로 제공됩니다.
- [Knowatoa](https://www.knowatoa.com) 💲 - ChatGPT, Google AI Overviews, AI Mode 등 AI 검색 서비스의 브랜드 가시성을 추적하며 프롬프트 추적과 보고서 연동 기능을 제공합니다.
- [Otterly.AI](https://otterly.ai) 💲 - ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot의 브랜드 언급·인용 추적, 경쟁사 비교, 프롬프트 리서치를 제공합니다.
- [Peec AI](https://peec.ai) 💲 - ChatGPT, Perplexity, AI Overviews, AI Mode, Gemini 등에서 브랜드 가시성, 위치, 감성을 추적하고 프롬프트별 보고서를 제공합니다.
- [Profound](https://www.tryprofound.com) 💲 - 매일 실행하는 프롬프트와 인용 분석으로 ChatGPT, Perplexity, Google AI Mode, Gemini, Claude 등 답변 엔진의 브랜드 가시성을 추적합니다.
- [Promptwatch](https://promptwatch.com) 💲 - ChatGPT, AI Overviews, Perplexity, Claude, Gemini 등에서 프롬프트로 브랜드 가시성을 추적하며 상위 요금제는 AI 크롤러 분석을 제공합니다.
- [Rankscale](https://rankscale.ai) 💲 - 크레딧 기반 요금제로 17개 이상의 AI 검색 엔진에서 브랜드 언급과 인용을 추적하며, 상위 요금제에서 브랜드 대시보드와 API를 제공합니다.
- [Scrunch](https://scrunch.com) 💲 - 주요 AI 플랫폼에서 프롬프트, 인용, 경쟁사 순위, AI 크롤러 활동을 모니터링하며, 사이트의 AI 최적화 버전을 제공할 수도 있습니다.
- [Searchable](https://www.searchable.com) 💲 - ChatGPT, Google AI Overviews, Perplexity의 브랜드 언급, 경쟁사 비교, 인용 출처를 추적하며 Claude, Gemini 등은 유료 추가 기능입니다.
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - 프롬프트 추적과 경쟁사 모니터링으로 ChatGPT, Google AI Mode 등의 브랜드 언급과 가시성을 추적하며, Semrush SEO+AI Search 요금제에 포함됩니다.
- [Trakkr](https://trakkr.ai) 💲 - 프롬프트 추적으로 AI 모델 8개에서 브랜드가 어떻게 노출되는지 추적하며, 상위 요금제에서 다중 브랜드와 고객 포털을 제공합니다.
- [Waikay](https://waikay.io) 🪙 - ChatGPT, Google, Claude, Perplexity가 브랜드를 어떻게 설명하는지 분석해 환각과 지식 공백을 짚고 실행 계획을 제안합니다.
- [Writesonic](https://writesonic.com) 💲 - AI 답변 속 브랜드 가시성을 추적하고 하위 요금제는 ChatGPT, Gemini, Google AI Overviews를 지원하며 아티클 작성과 사이트 진단·수정도 제공합니다.
- [ZipTie](https://ziptie.ai) 💲 - ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot 등 7개 엔진에서 선택한 프롬프트를 추적하며 확인 건당 과금합니다.

### 콘텐츠 진단과 최적화

- [Clearscope](https://www.clearscope.io) 💲 - Google과 AI 답변에 맞춘 콘텐츠 개선안을 제시하고 ChatGPT와 Gemini의 쿼리를 추적해 브랜드가 언급되는 시점을 보여 줍니다.
- [Frase](https://www.frase.io) 💲 - SEO와 GEO 관점에서 콘텐츠를 평가하고 ChatGPT, Google AI 등 AI 엔진의 브랜드 가시성을 모니터링하며, 상위 요금제에서 더 많은 엔진을 지원합니다.
- [GeoReady](https://geoready.dev) 🪙 - ChatGPT, Perplexity, Claude, Gemini가 사이트에 접근해 읽고 인용할 수 있는지 9개 범주, 100점 만점으로 진단하고 수정 우선순위를 제시합니다.
- [NEURONwriter](https://neuronwriter.com) 💲 - 상위 페이지를 바탕으로 용어와 구조를 제안해 Google과 AI 답변에 맞게 콘텐츠를 최적화하고, AI 모델 전반의 브랜드 보이스 점유율(SOV)을 모니터링합니다.
- [Surfer](https://surfer.ai) 💲 - 경쟁사 대비 초안 채점 에디터와 ChatGPT, Perplexity, Gemini, AI Overviews, AI Mode 브랜드 언급 추적용 AI Tracker를 갖췄습니다.

### 오픈 소스 도구와 라이브러리

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - AEO와 GEO 업무를 위한 에이전트 우선 운영 플랫폼으로, npm 패키지로 배포됩니다.
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok, AI Overviews의 브랜드 언급·인용을 추적하는 셀프 호스팅 플랫폼입니다.
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - 여러 LLM 제공업체에 프롬프트를 예약 실행해 웹 검색 인용을 수집하고, 대시보드와 CLI로 브랜드 언급을 추적합니다.
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - AI 엔진이 사이트를 크롤링하고 이해하고 인용할 수 있는지를 0~100점으로 평가하며, CLI, Python 라이브러리, MCP 서버로 제공됩니다.
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - ChatGPT, Perplexity, Gemini, Google AI Mode가 브랜드를 언급·인용하는 방식을 추적하는 셀프 호스팅 대시보드로, MCP 서버와 CLI를 제공합니다.
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - 웹사이트에 AI 크롤러가 접근해 읽을 수 있는지 확인하고 점수를 매기는 도구로, PyPI 패키지와 GitHub Action으로 제공됩니다.
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - 전략이 내장되어 있고 사용자 정의 전략도 등록할 수 있는 플러그인 방식의 Go용 GEO 프레임워크입니다.
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - CI나 pre-commit에서 실행해 문서와 정적 사이트의 구조 및 출처 표기 문제를 찾아내는 결정론적 콘텐츠 린터로, npm 패키지로 배포됩니다.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - AI 답변 속 브랜드 노출을 추적하고 개선하는 오픈 소스 플랫폼입니다.
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - SQLite와 MCP 서버를 갖춘 단일 Go 바이너리 형태의 셀프 호스팅 가시성 추적 도구로, 주요 AI 엔진의 브랜드 언급·인용을 기록합니다.
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - HTTP 콘텐츠 협상으로 AI 에이전트에 페이지의 Markdown 버전을 제공하는 NGINX 모듈입니다.
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews의 제품 화면에서 브랜드 언급·인용을 모니터링하는 셀프 호스팅 도구입니다.
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - 에이전트가 읽기 쉬운 정도로 사이트를 0~100점으로 평가하고, 페이지의 Markdown 사본과 robots.txt, llms.txt, sitemap.xml을 생성합니다.
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - React에서 타입 검사가 되는 Schema.org JSON-LD를 작성할 수 있게 합니다.
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - Schema.org JSON-LD 작성을 위한 TypeScript 타입입니다.
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - JavaScript 사이트용 Schema.org JSON-LD 그래프를 만드는 라이브러리로, Astro 통합을 제공합니다.
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - Schema.org 유형을 플루언트 방식으로 만들어 JSON-LD로 출력하는 PHP 빌더입니다.

### llms.txt 생성기

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - Vite, Astro, Next.js, Nuxt 사이트의 빌드 시점에 llms.txt, JSON-LD, Markdown 미러, AI 크롤러 제어 설정을 생성하고 검증합니다.
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - 웹사이트를 크롤링하고 콘텐츠를 추출해 llms.txt 파일을 만드는 Apify Actor입니다.
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - 사이트를 크롤링해 llms.txt 초안을 만드는 도구로, 페이지 탐색, 비즈니스 맥락 추가, 공개 파일의 일일 업데이트 기능을 제공합니다.
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - sitemap.xml을 llms.txt 파일로 변환하는 명령줄 도구입니다.
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - 문서 사이트용 /llms.txt 파일을 생성하는 MkDocs 플러그인입니다.
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - 애플리케이션의 /llms.txt Markdown 문서를 자동 생성하는 Nuxt 모듈입니다.
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - llms.txt 파일을 생성하는 Sphinx 확장입니다.
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - LLM이 읽기 좋은 문서 파일을 생성하는 VitePress 플러그인입니다.
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - 가입 없이 공개 홈페이지에서 사이트맵과 내부 링크로 찾은 최대 30개 페이지를 확인해 llms.txt 초안을 만듭니다.
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - 무료 Yoast SEO 플러그인에서 llms.txt 파일을 자동으로 생성·갱신하며, 핵심 콘텐츠를 자동 또는 수동으로 고를 수 있습니다.

### 크롤러 로그 분석

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - AI 크롤러 사용자 에이전트 목록으로, robots.txt 진단, 접근 가능 여부 테스트, 액세스 로그 분석을 하는 Node CLI와 GitHub Action을 함께 제공합니다.
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - 사이트를 크롤링하는 AI 서비스를 보여 주고 크롤러별 허용·차단과 robots.txt 준수 여부 보고를 제공하며, 모든 Cloudflare 요금제에서 쓸 수 있습니다.
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - AI 크롤러와 LLM 크롤러 트래픽을 엣지에서 감지하고 추적하는 Cloudflare Worker입니다.
- [Known Agents](https://knownagents.com) 🪙 - AI 에이전트·봇 디렉터리, robots.txt 검사기, 에이전트 분석을 제공하며, 무료 요금제는 월 10만 이벤트로 제한됩니다.

## AI 검색 엔진과 어시스턴트

지역별로 정리한 AI 답변 엔진으로, 가능한 경우 공식 사이트와 웹마스터 문서, 알려진 크롤러 사용자 에이전트를 함께 소개합니다.

### 글로벌

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Microsoft Bing의 대화형 검색 모드로, 옛 Copilot Search가 2026년에 AI Mode와 일반 검색 결과의 AI Overview 요약으로 나뉘었습니다.
- [Brave Search](https://brave.com/search/) 🪙 - 자체 독립 인덱스를 기반으로 한 Brave의 검색 엔진으로, 출처를 인용하는 Answer with AI 요약과 후속 질문용 Ask Brave 채팅 모드를 제공합니다.
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - 웹 검색이 내장된 OpenAI의 ChatGPT로, 대화 속에서 질문에 답하고 참고한 페이지 링크를 제공합니다.
- [Claude](https://claude.ai) 🪙 - 대화 중 웹을 검색하고 답변의 근거가 된 페이지를 인용할 수 있는 Anthropic의 Claude 어시스턴트입니다.
- [Duck.ai](https://duck.ai) 🪙 - 서드파티 AI 모델과 익명으로 대화하는 DuckDuckGo의 채팅으로 검색 결과에서 바로 열 수 있으며, DuckDuckGo 검색도 선택형 AI 보조 답변을 제공합니다.
- [Gemini](https://gemini.google.com) 🪙 - Google 검색을 활용해 답변에 최신 정보를 반영하는 Google의 Gemini AI 어시스턴트입니다.
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Gemini 기반의 Google 검색 대화형 모드로, 복잡한 질문에 답하고 후속 질문을 받으며 웹의 출처로 연결되는 링크를 제공합니다.
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Google 검색의 일반 결과 위에 표시되는 생성형 요약으로, 참고한 출처 링크를 함께 보여 주며 120개 이상의 국가와 지역에서 제공됩니다.
- [Grok](https://grok.com) 🪙 - 현재 SpaceX 산하인 xAI의 AI 어시스턴트로, 웹과 X 게시물을 검색해 시사 관련 질문에 답합니다.
- [Kagi Assistant](https://kagi.com/assistant) 💲 - 여러 제공업체의 모델에 Kagi의 광고 없는 검색 결과를 선택적으로 연결해 쓰는 유료 회원용 Kagi 채팅 어시스턴트입니다.
- [Meta AI](https://www.meta.ai) 🪙 - 웹과 WhatsApp, Instagram, Facebook에서 쓸 수 있는 Meta의 AI 어시스턴트로, 시의성 있는 질문에는 웹 검색 결과를 가져올 수 있습니다.
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Bing 웹 검색 결과로 질문에 답하고 참고한 페이지를 인용하는 Microsoft의 소비자용 Copilot 어시스턴트입니다.
- [Perplexity](https://www.perplexity.ai) 🪙 - 웹을 실시간으로 검색해 번호가 매겨진 출처 인용과 함께 대화형 답변을 제공하는 AI 답변 엔진입니다.

### 중국

- [ChatGLM](https://chatglm.cn) 🆓 - Zhipu AI의 중국어 어시스턴트(Zhipu Qingyan)로, 자사 GLM 모델을 기반으로 웹 검색과 에이전트 기능을 제공합니다.
- [DeepSeek](https://www.deepseek.com) 🆓 - 오픈 웨이트 모델을 기반으로 한 DeepSeek의 채팅 어시스턴트로, 최신 정보로 답하는 웹 검색 모드를 선택해 쓸 수 있습니다.
- [Doubao](https://www.doubao.com) 🆓 - ByteDance의 범용 AI 어시스턴트로, 채팅에서 웹을 검색해 질문에 답하고 참고한 출처를 보여 줍니다.
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - Baidu의 ERNIE Bot 어시스턴트(옛 Wenxin Yiyan)로, 현재 웹에서는 Baidu Wenxin Assistant로 제공되며 Baidu 검색과 연동됩니다.
- [Kimi](https://www.kimi.com) 🪙 - 긴 문맥 읽기로 알려진 Moonshot AI의 Kimi 어시스턴트로, 웹을 검색하고 읽은 페이지를 인용합니다.
- [Metaso](https://metaso.cn) 🪙 - MetaSOTA의 광고 없는 중국 AI 검색 엔진으로, 출처를 인용해 질문에 답하며 학술 문헌도 검색할 수 있습니다.
- [Quark](https://www.quark.cn) 🪙 - AI 어시스턴트 중심으로 재구성되어 쿼리에 생성형 결과로 답하는 Alibaba의 검색·브라우저 앱 Quark입니다.
- [Qwen](https://www.qianwen.com) 🆓 - Alibaba의 Qwen 앱(옛 Tongyi)으로, 자사 Qwen 모델 기반에 웹 검색을 갖춘 AI 어시스턴트이며 해외용 웹 버전은 Qwen Chat입니다.
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - WeChat 공식 계정 글을 포함한 웹 검색 결과로 답하는 Tencent의 AI 어시스턴트입니다.
- [Yuanbao Search](https://so.qq.com) 🆓 - Tencent의 AI 웹 검색 사이트로, 출처를 인용하고 WeChat 공식 계정과 Channels 콘텐츠도 검색하며 후속 질문용 AI 모드를 제공합니다.

### 일본

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - Yahoo! JAPAN 검색 AI Assistant와 LINE AI를 통합해 2026년 4월 출시한 LY Corporation의 AI 에이전트로, 검색창과 LINE에서 씁니다.
- [Felo](https://felo.ai) 🪙 - 도쿄 스타트업이 만든 다국어 AI 검색 엔진으로, 인용과 함께 답변하며 여러 언어의 출처를 검색할 수 있습니다.

### 한국

- [A. (A-dot)](https://adot.ai) 🆓 - SK텔레콤의 AI 개인 비서로, 여러 채팅 모델과 함께 Perplexity와 공동 개발한 AI 검색 기능을 제공합니다.
- [Kanana](https://kanana.ai) 🆓 - 카카오의 AI 브랜드로, 카카오톡 속 Kanana 어시스턴트와 오픈 소스 모델을 아우르며 2026년 10월 카카오톡 기반 에이전트 Kanana Space를 발표했습니다.
- [Liner](https://liner.com) 🪙 - 서울에 본사를 둔 기업의 AI 검색·리서치 어시스턴트로, 인용이 달린 답변과 학술 자료에 중점을 둡니다.
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - HyperCLOVA X 기반의 네이버 검색 생성형 답변으로, 페이지 상단에서 결과를 요약하고 참고한 출처 콘텐츠를 보여 줍니다.
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - 2026년 6월 전체 사용자에게 공개된 네이버의 대화형 AI 검색 탭으로, 상품, 장소, 예약 카드와 함께 대화로 답합니다.
- [Wrtn](https://wrtn.ai) 🆓 - 뤼튼테크놀로지스의 한국어 AI 어시스턴트로, 실시간 웹 결과로 답하고 출처를 보여 주는 무료 AI 검색 기능을 제공합니다.

### 유럽

- [Ecosia AI search](https://www.ecosia.org) 🆓 - 나무 심기를 후원하는 베를린 기반 검색 엔진 Ecosia의 AI 검색 기능으로, 사용자가 끄면 AI 없는 결과를 볼 수 있습니다.
- [Lumo](https://lumo.proton.me) 🪙 - 스위스에 기반을 둔 Proton의 개인정보 보호 중심 AI 어시스턴트로, 웹 검색이 내장되어 있으며 쿼리를 광고 타기팅에 쓰지 않습니다.
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - Le Chat에서 Vibe로 이름을 바꾼 Mistral AI의 어시스턴트로, 채팅 어시스턴트에 웹 검색과 코딩 에이전트를 결합했습니다.

### 기타 지역

- [Alice AI](https://alice.yandex.ru) 🆓 - Yandex의 Alice AI 어시스턴트로, 같은 모델이 Yandex 검색에서 출처 링크가 달린 AI 답변도 생성합니다.

## 언어별 GEO 자료

영어 이외의 언어로 발행된 아티클, 커뮤니티, 현지 도구를 모았으며, 대행사와 서비스 업체는 싣지 않습니다.

### 중국어

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - 지식재산권, 알고리즘 편향, 설명 가능성, 허위 정보 등 GEO의 윤리적 위험을 다루고 5가지 대응 방안을 제안한 중국어 프리프린트입니다. (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - 2026년 5월 열린 AIIA 신뢰 GEO 세미나를 다룬 신화통신 보도로, CAICT의 GEO 서비스 평가, GEO 위험 보고서, 업계 자율 규제를 소개합니다. (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - GEO 서비스 제공자, 신뢰할 수 있는 콘텐츠 출처, 금지 기법, 성과 보고에 관한 요건을 정한 중국광고협회의 단체 표준입니다. (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - 2026년 중국의 GEO 열풍을 다룬 기획 기사로, GEO가 AI 답변의 검색 단계를 겨냥하는 방식과 대량의 콘텐츠 시딩으로 가짜 제품이 AI 추천에 오른 사례를 설명합니다. (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - 블랙햇 GEO를 이용한 AI 데이터 포이즈닝을 규제와 플랫폼 대응까지 다룬 장문 분석으로, Hunan Daily 자체의 신뢰 GEO 서비스도 소개합니다. (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - AI 답변 조작을 겨냥한 Google의 2026년 스팸 정책 개정을 분석해 GEO와 유료 콘텐츠 시딩을 구분하고 그 사이의 회색 지대를 짚습니다. (2026)

### 일본어

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - 사이트를 AI Overviews와 AI Mode에서 28일간 제외한 실험을 정리한 글로, 두 기능의 클릭률이 사이트 평균의 2배 이상이라고 추정합니다. (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - 일본어 정보성 키워드를 대상으로 한 Ahrefs 연구로, AI Overviews 때문에 2026년 6월까지 1위 결과의 클릭률이 62.7% 줄었다고 추정합니다. (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - AI 검색 최적화를 다룬 Nikkei xTrend 연재의 첫 회로, AI Overviews가 일본에서 클릭을 줄인 Ahrefs 데이터를 인용하며 본문 대부분은 유료 회원용입니다. (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - 일본어 AI Mode 출시를 알리는 Google 재팬의 발표로, 질문을 하위 주제로 나눠 각각 검색하는 쿼리 팬아웃 기법을 설명합니다. (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - GEO와 LLMO가 전통적인 SEO에 기반한다고 주장한 Kenichi Suzuki의 강연 보고로, Google AI 검색이 답변을 만드는 과정의 개념 모델을 제시합니다. (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - 일본에서 GEO를 가리키는 말로 널리 쓰이는 LLMO와 SEO의 차이를 설명하는 Nikkei xTECH 해설 기사로, 전문을 읽으려면 무료 회원 가입이 필요합니다. (2026)

### 한국어

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - AI 브라우저와 제로 클릭 답변이 뉴스 유통 구조와 언론사 수익 모델을 어떻게 바꾸는지 분석한 한국언론진흥재단 보고서입니다. (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - AI 옵트아웃, AI 검색 데이터, 출처 표기 등 영국 CMA가 2026년 Google에 부과한 요구 사항과 한국에 주는 시사점을 다룬 한국언론진흥재단 보고서입니다. (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - 한국광고총연합회 학술지의 트렌드 리뷰로, GEO와 Perplexity, Gemini 등의 엔진이 검색 데이터를 활용하는 방식, E-E-A-T의 역할을 소개합니다. (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - 한국 결제 기업이 쓴 온라인 쇼핑몰용 GEO 가이드로, Q&A 콘텐츠, 사용 사례 중심 상품 설명, FAQ, 외부 언급 등 5가지 전술을 소개합니다. (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - AI 브리핑이 창작자 게시물을 출처로 보여 주는 방식과, AI 브리핑 인용을 기준으로 매달 창작자 약 3,000명에게 보상하는 네이버 메이트를 소개한 네이버 보도자료입니다. (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - a16z의 GEO 에세이를 한국어로 요약한 GeekNews 게시물로, GEO와 AEO 용어가 겹치는 지점에 관한 짧은 독자 토론이 달려 있습니다. (2025)

### 스페인어

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - 일반적인 여행 쿼리 하나를 여러 AI 시스템에 세 시점에 걸쳐 입력해 호텔 브랜드 가시성과 인용 출처의 변동이 매우 크다는 결과를 얻은 탐색적 연구입니다. (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - GEO 문헌을 검토해 가시성, 영향력, 검증 가능성 지표와 구조, 구조화된 데이터, 권위 같은 반복적인 전략으로 수렴하고 있음을 밝힙니다. (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - AI Overviews와 AI Mode가 스페인 뉴스 사이트의 트래픽을 크게 줄였으며 언론사가 GEO, 독자 충성도, 공동 라이선싱에 나서야 한다고 주장합니다. (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - 기관 리포지터리를 위한 최초의 GEO 지침을 제안하며 기술 설정, 의미 구조, 메타데이터, 다국어 콘텐츠, 새로운 지표를 다룹니다. (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - 스페인어 프롬프트 226만 개로 ChatGPT, Gemini, Perplexity, Copilot, Grok, Google AI 기능이 자주 인용하는 언론사 순위를 매깁니다. (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - 키워드 2,699개를 분석해 스페인 주요 언론사 관련 검색의 29.8%에 AI Overviews가 나오지만 속보에는 드물다는 바르셀로나 대학교 연구를 요약합니다. (2026)

### 독일어

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - 검색에서 AI 답변 시스템으로의 전환을 다룬 독일 디지털 산업 협회의 백서로, GEO의 표준 정의와 SEO와의 관계를 제안합니다. (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - 독일어 ChatGPT 답변 380만 건을 분석해 2026년 5월 모델 교체 후 이틀 만에 인용 도메인 구성이 47% 바뀌었음을 보여 줍니다. (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - AI 답변 25만 건 분석에서 ChatGPT, AI Overviews, Perplexity가 가장 많이 인용한 출처는 기업 사이트, YouTube, Reddit 순이라고 전합니다. (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - 쿼리 팬아웃, 검색 색인, 기술적 접근성 관점에서 ChatGPT, Gemini, Copilot, Perplexity의 페이지 탐색·인용 방식과 기업용 체크리스트를 제공합니다. (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - DACH 지역 AI 답변에서 같은 도메인의 인용·비인용 페이지를 비교해 구조와 스키마는 인용과 상관관계가 있지만 llms.txt는 효과가 없음을 밝힙니다. (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - 생성형 검색의 브랜드 가시성을 측정하는 9가지 KPI를 제안하고 프롬프트 세트 구성과 정기 점검에 관한 조언을 담은 BVDW의 짧은 백서입니다. (2026)

## 사례 연구

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - AI 검색 방문자가 Ahrefs 전체 트래픽의 0.5%에 불과했지만 가입자의 12.1%를 차지했다는 자사 분석 데이터를 공유합니다. (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - Profound가 측정한 Ramp 매입 채무 관리 제품의 AI 검색 가시성이 22.2%로 오른 과정과 Ramp가 공략한 페이지, 쿼리를 소개하는 업체 사례 연구입니다. (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - Vercel이 LLM에서 잘 발견되도록 SEO를 조정하는 방식을 소개하며, 신규 가입의 약 10%가 ChatGPT에서 유입되어 6개월 전 1%에서 늘었다고 밝힙니다. (2025)

## 강의, 영상, 팟캐스트

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Sam Oh의 무료 12강 영상 강의로, AI 검색 엔진의 인용 선택 방식, 프롬프트 리서치, AI 검색용 콘텐츠와 YouTube, 기술 설정, AI 트래픽 추적을 다룹니다.
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - SkillUp의 4시간 분량 Coursera 강의로, 2개 모듈에서 엔티티와 주제 권위, AI 친화적 콘텐츠 형식, GEO 지표, 실습을 다루며 수료증은 유료입니다.
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - 답변 엔진 인용, 질문 리서치, 온페이지 및 스키마 작업, AI 유입과 보이스 점유율(SOV) 측정을 다루는 7강짜리 무료 인증 과정입니다.
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Aleyda Solis가 엮은 무료 학습 로드맵으로, AI 검색 기초, 측정, 이커머스, 도구 가이드를 순서대로 정리하고 콘텐츠 최적화 체크리스트를 제공합니다.
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - PR·커뮤니케이션 팀을 위한 짧은 수료 과정으로, 언드 미디어가 AI 답변에 미치는 영향, 프롬프트 테스트, GEO 인사이트를 활용한 미디어 타기팅을 다룹니다.
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Google Search Relations 팀의 팟캐스트로, AI 기능을 포함한 Google 검색의 내부 작동 방식과 최근 SEO 커뮤니티 화제를 다룹니다.
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - 프롬프트 리서치, 보이스 점유율(SOV), 브랜드 언급, LLM용 콘텐츠 구성을 다루는 무료 20편 영상 강의로, 수료증이 있고 일부 강의는 Semrush 도구를 시연합니다.

## 뉴스레터와 커뮤니티

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Tom Critchlow의 Substack 뉴스레터(옛 The SEO MBA)로, AI 검색에 대응하는 검색 팀의 전략과 리더십을 다룹니다.
- [brightonSEO](https://brightonseo.com/) 💲 - 브라이턴과 샌디에이고에서 열리는 대규모 검색 마케팅 콘퍼런스 시리즈로, SEO, 콘텐츠, AI 검색 강연과 교육이 있으며 영국 행사는 무료 티켓 추첨도 합니다.
- [GEO Conference](https://geo-conference.com/) 💲 - 미국 여러 도시에서 열리는 생성형 엔진 최적화(GEO) 대면 1일 콘퍼런스 시리즈로, 행사마다 150석으로 제한하며 주로 GEO·SEO 도구 업체가 후원합니다.
- [Growth Memo](https://www.growth-memo.com/) 🪙 - 오가닉 성장에 관한 Kevin Indig의 뉴스레터로, AI 검색 행태, 인용, 트래픽에 관한 데이터 연구를 정기적으로 싣고 일부 호는 유료 구독자용입니다.
- [MozCon](https://moz.com/mozcon) 💲 - SEO, AI 검색, GEO를 다루는 Moz의 마케팅 콘퍼런스로, 2026년에는 런던과 뉴욕에서 오프라인 순회 행사로 열렸습니다.
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Barry Schwartz가 운영하는 일간 뉴스 사이트로, 검색 커뮤니티의 논의와 AI 검색 기능을 포함한 Google, Bing의 변화를 다룹니다.
- [SEOFOMO](https://seofomo.co/) 🆓 - SEO와 AI 검색 소식, 가이드, 도구, 행사, 채용 정보를 모은 Aleyda Solis의 주간 뉴스레터입니다.

## 다른 큐레이션 목록

이 목록과 주제가 겹치는 GEO 및 AI 검색 관련 목록을 감사의 뜻을 담아 소개합니다.

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - 플랫폼별 가이드, 에이전틱 커머스, 도구, 연구, 뉴스레터, 영상, 행사를 폭넓게 다루는 GEO 자료 목록입니다.
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - GEO 논문을 연도별로 정리한 연구 중심 목록입니다.
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - GEO용 무료 플랫폼과 오픈 소스 저장소 목록으로, 별도 웹사이트에서 점수, 검색, 무료 도구를 제공합니다.
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - GEO와 AI 가시성 추적 도구를 알파벳순으로 정리하고 기능과 가격을 짧게 설명한 디렉터리입니다.
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - 학습 자료, 도구, AI 검색 엔진, 전략, 모니터링, 사례 연구, 커뮤니티, 플랫폼 소식을 다루는 종합 GEO 목록입니다.
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - 연구, 플랫폼 공식 문서, 가이드, 도구, 강의, 뉴스레터, 커뮤니티를 정리한 GEO 목록으로, 옛 이름은 Tusko/awesome-geo입니다.
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - 지원 엔진, 갱신 주기, 가격, 데이터 내보내기 기준으로 GEO 도구를 비교한 표로, 자사 도구도 목록에 올린 GEO 도구 업체가 관리합니다.

## 기여하기

기여를 환영합니다. 풀 리퀘스트를 보내기 전에 [기여 가이드](CONTRIBUTING.md)를 읽어 주세요. 설명은 영어로만 작성하면 되며, 다른 언어는 메인테이너가 추가합니다.

## 라이선스

법이 허용하는 범위에서 기여자들은 [CC0 1.0 범용](LICENSE)에 따라 이 목록에 대한 모든 저작권 및 관련 권리를 포기합니다.
