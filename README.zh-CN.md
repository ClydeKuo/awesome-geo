# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | **简体中文** | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Deutsch](README.de.md)

> 生成式引擎优化（GEO）精选资源清单，涵盖研究论文、指南、技术规范、工具以及全球各地的 AI 搜索引擎。

## 目录

- [什么是 GEO](#什么是-geo)
- [入门](#入门)
- [研究论文](#研究论文)
  - [奠基性论文](#奠基性论文)
  - [基准与数据集](#基准与数据集)
  - [攻击与操纵](#攻击与操纵)
  - [引用与可见度分析](#引用与可见度分析)
  - [综述](#综述)
- [指南与文章](#指南与文章)
  - [策略](#策略)
  - [内容创作](#内容创作)
  - [技术实现](#技术实现)
  - [行业报告与数据](#行业报告与数据)
- [标准与技术规范](#标准与技术规范)
  - [llms.txt](#llmstxt)
  - [AI 爬虫与 robots.txt](#ai-爬虫与-robotstxt)
  - [结构化数据](#结构化数据)
  - [引擎官方文档](#引擎官方文档)
- [工具](#工具)
  - [AI 可见度监测](#ai-可见度监测)
  - [内容审计与优化](#内容审计与优化)
  - [开源工具与库](#开源工具与库)
  - [llms.txt 生成器](#llmstxt-生成器)
  - [爬虫日志分析](#爬虫日志分析)
- [AI 搜索引擎与助手](#ai-搜索引擎与助手)
  - [全球](#全球)
  - [中国](#中国)
  - [日本](#日本)
  - [韩国](#韩国)
  - [欧洲](#欧洲)
  - [其他地区](#其他地区)
- [各语种 GEO 资源](#各语种-geo-资源)
  - [中文](#中文)
  - [日语](#日语)
  - [韩语](#韩语)
  - [西班牙语](#西班牙语)
  - [德语](#德语)
- [案例研究](#案例研究)
- [课程、视频与播客](#课程视频与播客)
- [通讯与社区](#通讯与社区)
- [其他精选清单](#其他精选清单)
- [许可证](#许可证)

**图例：** 🆓 免费、🪙 免费增值、💲 付费、🔓 开源

## 什么是 GEO

生成式引擎优化（GEO）是一套让内容更容易被 ChatGPT、Perplexity、Google AI Overviews 等 AI 回答引擎发现、理解和引用的方法。SEO 争夺的是搜索结果列表中的排名，而 GEO 追求的是内容直接出现在 AI 生成的答案中并被引用或提及，因此衡量效果看的是引用和可见度，而不是点击量。这一概念出自普林斯顿大学等机构的 Aggarwal 等人发表于 KDD 2024 的论文《GEO: Generative Engine Optimization》。

## 入门

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - Search Engine Land 的科普文章，将生成式引擎优化（GEO）定义为在 AI 回答中获得引用和提及，并说明它如何建立在 SEO 基础之上。
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - 定义生成式引擎优化（GEO）的百科条目，将该术语追溯至 2023 年的研究论文，列出 AEO、LLMO 等相关名称，并提及相关批评。
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - Search Engine Journal 报道 Google 2026 年 5 月的指南将答案引擎优化（AEO）和生成式引擎优化（GEO）归入常规 SEO，并否定 llms.txt 和内容分块。
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - Google 官方指南，指出针对 AI 功能的优化本质上仍是 SEO，并将 llms.txt 和内容分块等做法列为不必要。
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - Search Engine Land 对 SEO 与生成式引擎优化（GEO）的比较，涵盖目标、衡量方式以及二者共通的做法。
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - 科普文章，把生成式引擎优化（GEO）一词溯源至 Aggarwal 等人的 KDD 2024 论文，比较业界定义并总结 AI 可见度的已有认识。

## 研究论文

### 奠基性论文

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - 演示一套智能体系统，针对每条内容评估 9 种 GEO 策略，并用多臂老虎机方法更快选出最优策略。 (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - 提出面向 GEO 的自进化智能体系统，突破静态启发式规则和单一提示词改写的局限，提升内容在摘要式回答中的可见度。 (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - 将 GEO 形式化为考虑竞争对手的策略选择问题，并在组合结构上用贝叶斯优化选择改写策略。 (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - 诊断单篇文档未被生成式引擎引用的原因，并进行针对性修复，而非套用统一的改写规则。 (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - 将 GEO 视为策略学习，借助规划、编辑和评估智能体，提炼可跨任务和引擎复用的编辑策略。 (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - 采用先发散后收敛的框架，挖掘优化偏好并融合为一次修订，化解多条查询之间相互冲突的修改需求。 (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - 提出 GEO-SFE 框架，在多个层级上设计内容结构，以影响生成式引擎引用哪些页面。 (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - 提出 FeatGEO，通过优化可解释的页面结构、内容和语言特征，在引用可见度与内容质量之间取得平衡。 (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - 用旅游网站文本合成的文本对微调 BART-base 模型，改写内容以提升其在大语言模型输出中的可发现性。 (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - 预先推断用户意图和角色，在不知道目标查询、也没有引擎反馈的情况下为生成式搜索引擎优化内容。 (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - 介绍 AutoGEO，学习生成式引擎在检索内容中的偏好，并据此改写网页以提升可见度。 (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - 介绍基于生成式 AI 的白帽搜索引擎优化（SEO）技术，并报告其实证效果。 (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - 提出生成式引擎优化（GEO）及衡量内容在生成式引擎回答中可见度的基准。 (2023)

### 基准与数据集

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - 在不同任务、领域和采用者数量下对对话式 SEO 方法进行基准测试，发现多数无效，传统 SEO 往往效果更好。 (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - 在受控条件下，用经人工核验的查询评测防御方法，应对经 GEO 处理、携带定向虚假信息的文档。 (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - 提出 LIVE-GEO，在页面由真实生成式引擎抓取和排序的线上环境中，检验 GEO 的可见度提升是否依然成立。 (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - 提供 13746 条消费品查询及检索到的商品列表，用于在多个生成式引擎上测试电商场景的 GEO 改写启发式方法。 (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - 提出 ALCE 基准，以自动指标评估大语言模型引用检索证据作答时的流畅度、正确性和引用质量。 (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - 在统一协议、数据集和指标下评估 GEO 排名操纵攻击，比较其攻击强度和可检测性。 (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - 发布包含 1.15 万条用户查询的数据集，比较 Google 搜索、Google AI Overviews 和 Gemini 返回的来源与信息。 (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - 提供端到端评估搜索增强型 GEO 策略的环境，覆盖检索、排序和生成环节。 (2026)

### 攻击与操纵

对抗性 GEO 研究，关注 AI 回答引擎如何通过提示词注入、排名操纵等手段被操控，以及相应的防御方法。

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - 提出 CORE 优化方法，控制商品在大语言模型生成的产品推荐中的出现位置。 (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - 审查 AI 搜索中 llms.txt 类清单文件的相关证据，发现这类文件很少被自动抓取，并评估其安全影响。 (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - 表明 GEO 攻击可能升级为降低内容质量的引用战，并研究实现双赢的机制设计。 (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - 表明联合构造的图像扰动和文本可以操纵视觉语言模型对商品的排序。 (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - 认为 GEO 存在影响力集中、商业影响未披露及学界与业界盲区等风险，呼吁在回答层面实施信息披露和审计等治理。 (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - 检测商家在内容中嵌入、用于把商品推到前列的说服性结构，以保护基于大语言模型的排序。 (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - 防御针对生成式搜索的恶意 GEO 改写，这类改写保持事实一致，因而能绕过事实核查和困惑度过滤。 (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - 将针对大语言模型搜索的排名操纵攻击建模为无限重复囚徒困境，并分析何时能维持合作。 (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - 分析生成式引擎引用哪些发布商，以及攻击者向回答背后的来源注入恶意内容的难度。 (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - 提出一种攻击方法，利用基于能量的优化构造流畅且难以察觉的提示词，以操纵大语言模型驱动的排序。 (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - 研究检索增强生成（RAG）系统中的竞争性投毒攻击，即多个攻击者把同一查询引向不同目标，并提出 PoisonArena 基准。 (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - 提出偏好操纵攻击，诱导大语言模型选择攻击者的内容，并指出这类攻击会让商家陷入囚徒困境。 (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - 研究一类 SEO 式攻击，即构造对抗性段落使其被稠密嵌入检索命中，而这种检索正是许多检索增强生成（RAG）系统的检索层。 (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - 表明在商品页面中加入精心构造的策略性文本序列，可使基于大语言模型的搜索引擎优先推荐该商品。 (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - 以真实消费品页面为例，表明网页文本中的提示词注入可提升某个来源在对话式搜索结果中的位置。 (2024)

### 引用与可见度分析

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - 报告一项预注册的实地实验（N=1100），发现移除 Google AI Overviews 和 AI Mode 后，流向发布商的点击率上升。 (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - 通过因果审计，研究文档呈现方式如何影响智能体搜索引擎在两个证据支持程度相同的来源中选择引用。 (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - 指出 AI 搜索的回答会随运行次数、提示词和时间变化，因此可见度需要反复测量，而非只测一次。 (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - 区分引用选择与引用吸收，并分析 ChatGPT、Google AI 和 Perplexity 上的 602 条提示词。 (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - 分析近 3.5 万条提示词观测数据，发现品牌自有域名一旦出现在实时检索结果中，品牌被提及率便大幅上升。 (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - 研究如何衡量品牌在 ChatGPT、Claude、Perplexity 和 Gemini 中的可见度，包括这些引擎引用品牌时依赖哪些来源。 (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - 认为 GEO 可见度得分取决于提示词语料及其权重，二者界定的回答市场未必符合真实需求。 (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - 在 40 天内追踪 55393 条查询，衡量 Google AI Overviews 的出现时机、来源质量、陈述忠实度及对发布商的影响。 (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - 量化 Google 搜索结果与生成式 AI 回答在被引用域名、域名类型、查询意图和时效性上的差异。 (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - 审计 ChatGPT、Copilot、Google 和 Perplexity，发现不同引擎间 URL 重合度极低，限制了与引擎无关的 GEO 评分的作用。 (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - 以 712 条查询审计四个生成式搜索引擎，发现约 16% 的被引用来源疑似由 AI 生成。 (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - 以 Google AI Overviews 和 Reddit 为例，表明 AI 搜索提升了被引用社区的参与度，但这一增益在 AI Mode 推出后逐渐消退。 (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - 观察四种 ChatGPT 网页搜索配置如何改写查询、检索页面和选择引用，发现检索频率可以预测引用。 (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - 基于 614 条查询，分析四个中文生成式搜索平台的引用行为、来源归属和实体曝光。 (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - 分析 158099 条回答，发现 ChatGPT 为改写后的子查询检索到的页面，比页面自身属性更能解释引用情况。 (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - 提出包含 16 个维度的页面审计框架，发现在三个引擎中，元数据、语义化 HTML 和结构化数据与引用的关联最强。 (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - 通过跨行业、跨语言的对照实验比较 AI 搜索引擎与 Google，发现前者更偏向非付费的第三方内容，而非品牌自有内容。 (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - 构建 ConflictingQA 数据集，表明大语言模型高度依赖页面与查询的相关性，而基本忽略科学参考文献等风格线索。 (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - 审计 Bing Chat、NeevaAI、Perplexity 和 YouChat 的引用召回率与精确率，发现许多陈述缺乏完整的引用支撑。 (2023)

### 综述

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - 综述 2023 至 2026 年的 45 项研究，把 GEO 视为多阶段随机流程，并提供评估 GEO 主张的清单。 (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - 按架构、优化、应用和评估对基于大语言模型的搜索智能体进行系统分类，并列出待解决的挑战。 (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - 从技术视角综述大语言模型时代的生成式搜索与推荐。 (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - 探讨搜索引擎与大语言模型如何互相促进，涵盖用搜索改进大语言模型和用大语言模型改进搜索。 (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - 综述大语言模型在信息检索系统中的应用，包括查询改写、检索、重排序和阅读。 (2023)

## 指南与文章

### 策略

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - 实用入门指南，介绍 GEO 如何帮助内容出现在 AI 驱动的搜索结果中。 (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - 讲解 GEO 是什么、与 SEO 有何不同，以及哪些技巧有助于内容被 AI 回答引用，附可下载的审计清单。 (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - 解释 AI 搜索与传统搜索的区别，列出五种 GEO 策略并介绍如何衡量 GEO 成效，同时指出 AI 搜索仍依赖传统搜索。 (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - 认为搜索正从基于链接的排名转向大语言模型生成的回答，并将 GEO 视为规模约 800 亿美元的 SEO 市场的下一阶段。 (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - 提出 SEEN 四层 GEO 框架（结构、证据、实体、知名度），附 41 项按 0 或 1 计分的清单，用于找出最薄弱的一层。 (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - 逐步讲解十步 GEO 流程，从确定优先主题和基线，到解读引用来源、改进内容和汇报结果。 (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - 八篇系列答案引擎优化（AEO）指南的开篇，涵盖 AEO 与 SEO 的区别、回答引擎的工作原理、AI 可见度追踪、提示词选择及纠正 AI 回答中的错误。 (2025)

### 内容创作

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - 解释什么是 Google AI Overviews、它如何基于网络来源生成，以及网站所有者如何针对其优化并追踪可见度。 (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - 介绍获得 ChatGPT 引用的两步方法，即先被检索到、再值得引用，每一步都有作者自己的测量数据支撑，例如哪些被引用域名允许 AI 爬虫。 (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - 报告在 ChatGPT 中测试 13 个购物问题及分析网站服务器日志的结果（含一项负面结果），并说明应放行哪些 AI 爬虫。 (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - 讲解让内容被 ChatGPT、Google 等 AI 搜索引擎引用的七个步骤，从关键词研究到内容排版。 (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - 给出在 ChatGPT 搜索中获得排名的八个步骤，包括让内容便于 AI 系统提取，以及在站外建立共识。 (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - 列出提升品牌在大语言模型生成回答中可见度的 10 种方法，并将其归为大语言模型优化（LLMO）。 (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - Microsoft Advertising 的指南，说明怎样的内容可用于 AI 搜索回答，包括 Schema、清晰标题、独立问答块，以及把答案藏在标签页或 PDF 中等错误。 (2025)

### 技术实现

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - 报道一项调查发现，通过 Google Tag Manager 等方式在客户端注入的 JSON-LD 会被无法执行 JavaScript 的 AI 爬虫遗漏。 (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - 介绍如何在 Google Analytics 4 中追踪来自 ChatGPT、Gemini 等工具的 AI 引荐流量。 (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - 介绍以 Markdown 格式向 AI 智能体提供页面，展示其如何减少 token 用量，例如一篇文章从 HTML 的 16180 个 token 降至 Markdown 的 3150 个。 (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - 发布 MERJ 与 Vercel 的数据，揭示 ChatGPT、Claude 等 AI 爬虫如何处理 JavaScript 和不同内容类型，并为网站所有者提供建议。 (2024)

### 行业报告与数据

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - 研究 3000 个网站，估算 AI 聊天机器人带来的流量，发现 63% 的网站获得过此类流量，其中 98% 来自三款聊天机器人。 (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - 为 Cloudflare Radar 增加行业维度数据，并按抓取目的细分 AI 爬虫流量。 (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - 分析 3100 万条 AI 引用和 105 家发布商的 robots.txt 文件，发现屏蔽 AI 爬虫对部分模型有效，对另一些则毫无作用。 (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - 基于 16 个月的数据，显示 Google AI Overviews 引用与自然排名的重合率从 32% 升至 54%，并按行业细分。 (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - 介绍 Ahrefs 的研究发现，Google AI Overviews 让点击量下降 34.5%，与 Google 声称其能增加点击的说法相悖。 (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - 用新闻摘录测试八款 AI 搜索工具，发现它们在超过 60% 的查询中引用来源有误。 (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - 汇集 Similarweb 2026 年关于 ChatGPT、Gemini 和 Claude 的市场份额、引荐流量、引用以及 AI 回答内广告的数据。 (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - 分析 7.5 万个品牌，找出最可能影响 Google AI Overviews 中品牌提及的搜索因素。 (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - 对比 2025 年 3 月 Google 用户的行为，发现看到 AI 摘要的用户点击其他网站链接的可能性更低。 (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - 追踪 ChatGPT、Gemini、Copilot 和 Google 上的 3.75 万条引用，发现半数在次日消失，但大多会重新出现。 (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - 考察 30 万个域名，了解 llms.txt 的普及程度，以及它是否影响域名被大语言模型引用的频率。 (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - 分析 2024 年 11 月至 2026 年 3 月约 70 亿个日志文件，揭示 OpenAI 的三款爬虫如何访问网络。 (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - 报告指出，随着生成式 AI 重塑新闻行业，ChatGPT 新闻类查询激增 212%，发布商流量下降 26%。 (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - 分析超过 1000 万个关键词，展示 Google AI Overviews 如何改变搜索以及这对 SEO 意味着什么。 (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - 基于 86.3 万个搜索结果页发现，Google AI Overviews 中 38% 的引用来自排名前 10 的页面，低于一年前的 76%。 (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - 追踪 1885 个添加了 JSON-LD 的页面，衡量其对 Google AI Overviews、AI Mode 和 ChatGPT 中引用的影响。 (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - 研究 140 万条提示词，揭示页面标题、URL 和摘要如何影响 ChatGPT 引用检索结果中的哪些页面。 (2026)

## 标准与技术规范

规定 AI 爬虫如何访问网站、AI 回答引擎如何读取内容的技术规范与官方文档。

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - 托管 llms.txt 提案的源文件，以及配套的参考工具和讨论。
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - 报道 John Mueller 称 llms.txt 目前仍属推测性质，并表示他更青睐 Google 支持的替代方案 WebMCP。
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - 报道 John Mueller 根据服务器日志表示，目前没有任何 AI 系统使用 llms.txt。 (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - 实现了 llms.txt 的网站目录，附 API、平台和开发者工具的示例文件。
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - 2026 年 9 月的研究，测量排名前 1000 和前 1 万的域名中 llms.txt 的采用率，附研究方法和可下载数据。 (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - 收录发布 llms.txt 文件的网站，供开发者浏览该格式的真实示例。
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - 收录发布 llms.txt 的网站，并展示其声明的训练、检索和摘要等 AI 权限。
- [The /llms.txt file](https://llmstxt.org) 🆓 - 提议在网站根目录放置 Markdown 格式的 /llms.txt 文件，为语言模型提供精选的网站概览及最有用内容的链接。 (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - 以 Vercel、Google 和 Anthropic 为例论证 llms.txt 的价值，并回应认为常规 SEO 做法已足够的批评者。 (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - 解释 llms.txt 文件是什么，并探讨添加它对开发者和营销人员是否真有作用。

### AI 爬虫与 robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - 分四组列出 12 家运营方的 25 个 AI 爬虫 User-Agent，并统计 157 个平台中各有多少在 robots.txt 中屏蔽它们。 (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - 汇总网站所有者可用来退出 AI 训练的已知 robots.txt 条目、meta 标签及其他设置。
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - 维护社区整理的待屏蔽 AI 智能体与爬虫列表，并生成相应的 robots.txt 和服务器配置文件。
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - 介绍 Amazonbot、Amzn-SearchBot 和 Amzn-User 爬虫，以及分别控制它们的独立 robots.txt 设置。
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - 解释 Pay Per Crawl 如何让网站所有者向 AI 爬虫收取访问费用，并以 HTTP 402 响应未付费请求，该功能处于封闭测试阶段。
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - 列出响应用户请求执行抓取的 Google 抓取工具（如 Google Read Aloud），并说明它们通常忽略 robots.txt 规则。
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - 列出 Googlebot 等 Google 常用爬虫及其 User-Agent 字符串和 robots.txt 标识。
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - 列出约 40 个 Yandex 爬虫 User-Agent 及其用途和 robots.txt 行为，并说明如何通过反向 DNS 验证。
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - 制定通用词汇及附加方式（如 robots.txt 和 HTTP 头）的标准，用于表达内容被 AI 收集和使用的偏好。
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - 制定以加密方式认证 AI 爬虫、智能体等自动化客户端的标准方法，以取代 IP 白名单和 User-Agent 字符串。
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - 说明 DuckAssistBot 为 DuckDuckGo 的 AI 辅助回答收集来源，不用于 AI 训练，可在 robots.txt 中屏蔽。
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - 列出 Meta 的各类爬虫及其用途，包括用于 Meta AI 搜索的 Meta-WebIndexer 和用于 AI 模型训练的 Meta-ExternalAgent。
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - 介绍 MistralAI-User、MistralAI-Index 和 MistralAI-Training 三个 User-Agent 及其各自用途。
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - 规定 robots.txt 的语法和语义，即 AI 爬虫应当遵守的机器人排除协议。 (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - 宣布 Google 计划遵循基于 IETF AIPREF 草案、在 robots.txt 中声明的通用 AI 训练退出设置，目标是 2027 年提供支持。 (2026)

### 结构化数据

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - 介绍 Google 如何利用结构化数据标记理解内容、支持哪些格式以及标记应放在何处。
- [JSON-LD](https://json-ld.org) 🆓 - 托管 JSON-LD 规范，这是一种基于 JSON 的关联数据格式，Schema.org 标记通常以此编写。
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - 测试网址或代码片段，报告其结构化数据可生成哪些 Google 富媒体搜索结果。
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - 总结 Ahrefs 的一份报告，测试为已被 AI 引用的页面添加 Schema 标记能否提高其被引用率。 (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - 校验 JSON-LD、Microdata 或 RDFa 格式中任意 Schema.org 类型的结构化数据。
- [Schema.org](https://schema.org) 🆓 - 托管供搜索引擎等使用方标记网页的通用类型与属性词汇表。
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - 托管 Schema.org 词汇表及其配套软件的源代码。
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - 汇总支持 Google 搜索各项功能的结构化数据类型，附示例和实施指南。

### 引擎官方文档

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - 介绍为 Spotlight、Siri 和 Safari 搜索功能提供数据的 Applebot，以及发布商可通过禁止抓取来退出生成式 AI 训练的 Applebot-Extended。
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - 说明 AI Overviews 和 AI Mode 在 Google 搜索中如何运作，以及网站所有者可以如何争取内容被纳入其中。
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - 百度的站长平台，提供网站资源提交、抓取与 robots 数据、搜索组件及 AI 流量分析。
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - 介绍 Common Crawl 开放网络档案背后的爬虫 CCBot，包括其 User-Agent 以及验证和屏蔽方法。
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - 介绍 ClaudeBot、Claude-User 和 Claude-SearchBot 三个爬虫，以及网站所有者如何通过 robots.txt 分别屏蔽。
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - IndexNow 协议文档，该协议用于通知参与的搜索引擎有新增、更新或删除的网址。
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - 宣布 Bing Webmaster Tools 新增报告，显示网站何时在 Microsoft Copilot 回答和 Bing AI 生成摘要中被引用。 (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - 宣布 Search Console 推出新报告，按页面、国家、设备和日期显示页面在 AI Overviews、AI Mode 等生成式 AI 功能中的出现频率。 (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - 宣布 Perplexity 发布商计划，与参与的发布商分享收入，并提供 API 访问和开发支持。 (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - Naver 的站长指南与工具，说明网站被 Naver 搜索发现和收录所需的条件，AI Briefing 也取自同一索引中的网页文档。
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - 介绍 OAI-SearchBot、GPTBot、ChatGPT-User 和 OAI-AdsBot 四个 User-Agent 及其各自用途。
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - 介绍让网站出现在 Perplexity 搜索结果中的 PerplexityBot，以及应用户请求抓取页面、通常忽略 robots.txt 的 Perplexity-User。
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - 解答发布商和开发者关于在 ChatGPT 搜索中出现、OAI-SearchBot 爬虫以及来自 ChatGPT 的引荐流量等问题。
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - 介绍 Search Console 中的设置，用于控制内容是否出现在 AI Overviews、AI Mode 以及 Discover 的生成式 AI 功能中，并说明该设置不影响 AI 训练。
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Yandex 帮助页面，说明其 AI 回答如何拆分问题、挑选并分析来源，并在回答中附上链接。
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Google 推荐的做法，帮助内容在 Google 搜索的 AI 体验中取得良好表现。 (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Yandex 的站长服务，用于验证网站、监测收录情况并诊断 Yandex 搜索中的抓取问题。
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - 宣布发布商可用 robots.txt、meta 标签或 X-Robots-Tag 头分别设置 AI 训练和回答依据（grounding）偏好，Microsoft 自 2027 年 2 月起读取。 (2026)

## 工具

### AI 可见度监测

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - 免注册查看 ChatGPT、Gemini、Perplexity、Copilot 和 Google AI Overviews 如何提及和引用某个品牌。
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - 借助提示词数据库或自定义提示词，统计品牌在 Google AI Overviews、AI Mode、ChatGPT、Perplexity、Gemini 和 Copilot 回答中出现的频率。
- [AthenaHQ](https://athenahq.ai) 🪙 - 追踪品牌在 ChatGPT、Perplexity、Gemini、Google AI Overviews、Copilot 等 AI 模型中的可见度并给出内容修改建议，免费方案含初始额度。
- [Geoptie](https://geoptie.com) 💲 - 展示 ChatGPT、Gemini、Claude、Perplexity 和 Google AI 对购物咨询的回答及其引用来源。
- [Goodie](https://higoodie.com) 💲 - 追踪品牌在 ChatGPT、Google AI Overviews、Perplexity、Copilot 等 AI 引擎中的可见度并给出优化建议，高级套餐支持更多引擎。
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - 一次性免费检测 ChatGPT、Perplexity 和 Gemini 如何描述品牌并打分，付费的每周监测由 HubSpot AEO 提供。
- [Knowatoa](https://www.knowatoa.com) 💲 - 追踪品牌在 ChatGPT、Google AI Overviews、AI Mode 等 AI 搜索服务中的可见度，支持提示词追踪和报告集成。
- [Otterly.AI](https://otterly.ai) 💲 - 监测品牌在 ChatGPT、Google AI Overviews、AI Mode、Gemini、Perplexity 和 Copilot 中的提及及网站引用情况，支持竞品对比和提示词研究。
- [Peec AI](https://peec.ai) 💲 - 追踪品牌在 ChatGPT、Perplexity、Google AI Overviews、AI Mode、Gemini 等 AI 搜索平台中的可见度、排位和情感倾向，提供提示词级报告。
- [Profound](https://www.tryprofound.com) 💲 - 通过每日运行提示词和引用分析，追踪品牌在 ChatGPT、Perplexity、Google AI Mode、Gemini、Claude 等回答引擎中的可见度。
- [Promptwatch](https://promptwatch.com) 💲 - 通过运行提示词，追踪品牌在 ChatGPT、Google AI Overviews、Perplexity、Claude、Gemini 等 AI 模型中的可见度，高级套餐提供 AI 爬虫分析。
- [Rankscale](https://rankscale.ai) 💲 - 采用按点数计费的套餐，追踪品牌在 17 个以上 AI 搜索引擎中的提及和引用，高级套餐提供品牌仪表板和 API。
- [Scrunch](https://scrunch.com) 💲 - 在主流 AI 平台上监测提示词、引用、竞品排名和 AI 爬虫抓取活动，并可向 AI 提供经优化的网站版本。
- [Searchable](https://www.searchable.com) 💲 - 追踪品牌在 ChatGPT、Google AI Overviews 和 Perplexity 中的提及、竞品对比和引用来源，Claude、Gemini 等 AI 引擎为付费附加项。
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - 通过提示词追踪和竞品监测，衡量品牌在 ChatGPT、Google AI Mode 等 AI 平台中的提及和可见度，包含在 Semrush 的 SEO 与 AI 搜索套餐中。
- [Trakkr](https://trakkr.ai) 💲 - 通过提示词追踪品牌在八个 AI 模型中的呈现情况，高级套餐提供多品牌方案和客户门户。
- [Waikay](https://waikay.io) 🪙 - 分析 ChatGPT、Google、Claude 和 Perplexity 如何描述品牌，标记幻觉和知识空白并给出行动建议。
- [Writesonic](https://writesonic.com) 💲 - 监测品牌在 AI 回答中的可见度，基础套餐覆盖 ChatGPT、Gemini 和 Google AI Overviews，并提供文章写作和网站审计修复功能。
- [ZipTie](https://ziptie.ai) 💲 - 追踪选定提示词在 ChatGPT、Google AI Overviews、AI Mode、Gemini、Perplexity、Copilot 等七个引擎中的表现，按检查次数计费。

### 内容审计与优化

- [Clearscope](https://www.clearscope.io) 💲 - 提供适用于 Google 和 AI 回答的内容改进建议，并追踪 ChatGPT 和 Gemini 中的查询，显示品牌被提及的情况。
- [Frase](https://www.frase.io) 💲 - 从 SEO 和 GEO 角度为内容打分，并监测品牌在 ChatGPT、Google AI 等 AI 引擎中的可见度，高级套餐支持更多引擎。
- [GeoReady](https://geoready.dev) 🪙 - 审计 ChatGPT、Perplexity、Claude 和 Gemini 能否访问、读取并引用网站，按九个类别给出百分制评分，并按优先级列出修复项。
- [NEURONwriter](https://neuronwriter.com) 💲 - 根据排名靠前的页面建议用词和结构，针对 Google 和 AI 回答优化内容，并监测品牌在各 AI 模型中的声量占比。
- [Surfer](https://surfer.ai) 💲 - 集成内容编辑器与 AI Tracker，前者对照竞品为草稿打分，后者追踪 ChatGPT、Perplexity、Gemini、Google AI Overviews 和 AI Mode 中的品牌提及。

### 开源工具与库

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - 面向智能体的答案引擎优化（AEO）与 GEO 运营平台，以 npm 包形式发布。
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - 可自托管的平台，追踪 ChatGPT、Claude、Perplexity、Gemini、Copilot、Grok 和 Google AI Overviews 如何提及和引用品牌。
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - 在多个大语言模型服务商上定时运行提示词，抓取其联网搜索引用，并通过仪表板和命令行工具追踪品牌提及。
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - 以 0 到 100 分评估网站能否被 AI 引擎抓取、理解和引用，提供命令行工具、Python 库和 MCP 服务器。
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - 追踪 ChatGPT、Perplexity、Gemini 和 Google AI Mode 如何提及和引用品牌，形式为自托管仪表板，附 MCP 服务器和命令行工具。
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - 检查网站能否被 AI 爬虫访问和读取并给出评分，提供 PyPI 包和 GitHub Action。
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - 提供可插拔的 Go 语言 GEO 框架，内置多种策略并支持注册自定义策略。
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - 确定性的内容检查工具（linter），可在 CI 或 pre-commit 中运行，标记文档和静态网站中的结构与来源问题，以 npm 包发布。
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - 用于追踪并提升品牌在 AI 回答中出现情况的开源平台。
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - 可自托管的可见度追踪工具，以内含 SQLite 和 MCP 服务器的单个 Go 二进制文件形式提供，记录主流 AI 引擎如何提及和引用品牌。
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - 通过 HTTP 内容协商向 AI 智能体提供 Markdown 版页面的 NGINX 模块。
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - 可自托管的追踪工具，通过产品界面监测 ChatGPT、Perplexity、Gemini、Claude 和 Google AI Overviews 如何提及和引用品牌。
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - 按智能体可读性为网站打 0 至 100 分，并生成页面的 Markdown 副本以及 robots.txt、llms.txt 和 sitemap.xml。
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - 用于 React 的带类型检查的 Schema.org JSON-LD 库。
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - 用于编写 Schema.org JSON-LD 的 TypeScript 类型定义。
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - 为 JavaScript 网站构建 Schema.org JSON-LD 图谱，并提供 Astro 集成。
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - 以链式调用构建 Schema.org 类型并输出 JSON-LD 的 PHP 库。

### llms.txt 生成器

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - 在构建时为 Vite、Astro、Next.js 和 Nuxt 网站生成 llms.txt、JSON-LD、Markdown 镜像和 AI 爬虫控制规则，并进行校验。
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - 抓取网站并提取内容以生成 llms.txt 文件的 Apify Actor。
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - 抓取网站以起草 llms.txt 文件，支持页面发现、补充业务背景信息，并每日更新公开文件。
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - 将 sitemap.xml 转换为 llms.txt 文件的命令行工具。
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - 为文档网站生成 /llms.txt 文件的 MkDocs 插件。
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - 为应用自动生成 Markdown 格式 /llms.txt 文档的 Nuxt 模块。
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - 生成 llms.txt 文件的 Sphinx 扩展。
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - 生成适合大语言模型阅读的文档文件的 VitePress 插件。
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - 无需注册，从公开首页出发，检查通过网站地图（sitemap）和内部链接找到的最多 30 个页面，生成 llms.txt 草稿。
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - 在免费的 Yoast SEO 插件中自动生成并更新 llms.txt 文件，可自动或手动选择重点内容。

### 爬虫日志分析

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - AI 爬虫 User-Agent 精选列表，附带 Node 命令行工具和 GitHub Action，可审计 robots.txt、测试可访问性并读取访问日志。
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - 显示哪些 AI 服务在抓取网站，允许网站所有者逐个放行或屏蔽爬虫，并报告哪些爬虫遵守 robots.txt，所有 Cloudflare 套餐均可使用。
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - 在边缘检测并追踪 AI 爬虫与大语言模型爬虫流量的 Cloudflare Worker。
- [Known Agents](https://knownagents.com) 🪙 - 提供 AI 智能体与爬虫目录、robots.txt 检查工具和智能体分析，免费方案每月限 10 万个事件。

## AI 搜索引擎与助手

按地区整理的 AI 回答引擎，尽量附上官方网站、站长文档和已知的爬虫 User-Agent。

### 全球

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Microsoft Bing 的对话式搜索模式，前身为 Copilot Search，2026 年拆分为 AI Mode 和常规结果中的 AI Overview 摘要。
- [Brave Search](https://brave.com/search/) 🪙 - Brave 基于自有独立索引的搜索引擎，提供附带来源引用的 Answer with AI 摘要，以及可继续追问的 Ask Brave 聊天模式。
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - OpenAI 内置网页搜索的 ChatGPT，在对话中回答问题并附上所参考页面的链接。
- [Claude](https://claude.ai) 🪙 - Anthropic 的 Claude 助手，可在对话中搜索网页并引用回答所依据的页面。
- [Duck.ai](https://duck.ai) 🪙 - DuckDuckGo 提供的匿名化第三方 AI 模型聊天服务，可从搜索结果进入；DuckDuckGo 搜索也提供可选的 AI 辅助回答。
- [Gemini](https://gemini.google.com) 🪙 - Google 的 Gemini AI 助手，借助 Google 搜索在回答中提供最新信息。
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Google 搜索基于 Gemini 的对话模式，可回答复杂问题、支持追问，并链接到网络上的来源。
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Google 搜索在常规结果上方显示的生成式摘要，附有所引来源的链接，覆盖 120 多个国家和地区。
- [Grok](https://grok.com) 🪙 - xAI（现隶属 SpaceX）推出的 AI 助手，通过搜索网页和 X 上的帖子回答时事问题。
- [Kagi Assistant](https://kagi.com/assistant) 💲 - Kagi 面向付费会员的聊天助手，可搭配多家服务商的模型，并可选接入 Kagi 无广告的搜索结果。
- [Meta AI](https://www.meta.ai) 🪙 - Meta 的 AI 助手，覆盖网页端以及 WhatsApp、Instagram 和 Facebook，可调用网页搜索结果回答时效性问题。
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Microsoft 面向个人用户的 Copilot 助手，利用 Bing 网页结果回答问题并引用所依据的页面。
- [Perplexity](https://www.perplexity.ai) 🪙 - 实时搜索网页的 AI 回答引擎，以对话形式作答并附带编号的来源引用。

### 中国

- [ChatGLM](https://chatglm.cn) 🆓 - 智谱基于 GLM 模型打造的中文助手智谱清言，具备联网搜索和智能体功能。
- [DeepSeek](https://www.deepseek.com) 🆓 - DeepSeek 基于自家开放权重模型打造的聊天助手，可选联网搜索模式以获取最新回答。
- [Doubao](https://www.doubao.com) 🆓 - 字节跳动的通用 AI 助手，可在对话中联网搜索作答并列出参考来源。
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - 百度的 AI 助手文心（原文心一言），网页端现为百度文心助手，并接入百度搜索。
- [Kimi](https://www.kimi.com) 🪙 - 月之暗面的 Kimi 助手，以长上下文阅读见长，可联网搜索并引用所阅读的页面。
- [Metaso](https://metaso.cn) 🪙 - 秘塔推出的无广告中文 AI 搜索引擎，回答附带引用来源，也可检索学术文献。
- [Quark](https://www.quark.cn) 🪙 - 阿里巴巴的夸克，围绕 AI 助手重构的搜索与浏览器应用，以生成式结果回答查询。
- [Qwen](https://www.qianwen.com) 🆓 - 阿里巴巴的千问 App（原通义），基于 Qwen 系列模型、支持联网搜索的 AI 助手，国际网页版为 Qwen Chat。
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - 腾讯的 AI 助手，结合网页搜索结果作答，来源包括微信公众号文章。
- [Yuanbao Search](https://so.qq.com) 🆓 - 腾讯的 AI 网页搜索网站，回答附带引用来源，可搜索微信公众号和视频号内容，并提供可追问的 AI 模式。

### 日本

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - LY Corporation 于 2026 年 4 月整合 Yahoo! JAPAN 搜索的 AI 助手与 LINE AI 推出的 AI 智能体，入口为 Yahoo! JAPAN 搜索框和 LINE。
- [Felo](https://felo.ai) 🪙 - 东京初创公司推出的多语言 AI 搜索引擎，回答附带引用，并可跨语言检索来源。

### 韩国

- [A. (A-dot)](https://adot.ai) 🆓 - SK Telecom 的 AI 个人助手，除多款聊天模型外，还提供与 Perplexity 合作开发的 AI 搜索功能。
- [Kanana](https://kanana.ai) 🆓 - Kakao 的 AI 品牌，涵盖 Kanana in KakaoTalk 助手和开源 Kanana 模型，2026 年 10 月又公布基于 KakaoTalk 的 Kanana Space 智能体。
- [Liner](https://liner.com) 🪙 - 首尔公司推出的 AI 搜索与研究助手，侧重带引用的回答和学术来源。
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - Naver 搜索基于 HyperCLOVA X 的生成式回答，在页面顶部汇总结果并展示所用的来源内容。
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - Naver 的对话式 AI 搜索标签页，2026 年 6 月向全体用户开放，以对话形式作答并附商品、地点和预订卡片。
- [Wrtn](https://wrtn.ai) 🆓 - Wrtn Technologies 推出的韩国 AI 助手，提供免费的 AI 搜索功能，基于实时网页结果作答并列出来源。

### 欧洲

- [Ecosia AI search](https://www.ecosia.org) 🆓 - 总部位于柏林、以收益资助植树的搜索引擎 Ecosia 的 AI 搜索功能，用户可将其关闭以获得无 AI 的结果。
- [Lumo](https://lumo.proton.me) 🪙 - Proton 推出的注重隐私的 AI 助手，总部位于瑞士，内置网页搜索，不将查询用于广告定向。
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - Mistral AI 的助手，由 Le Chat 更名为 Vibe，集聊天助手、网页搜索和编程智能体于一体。

### 其他地区

- [Alice AI](https://alice.yandex.ru) 🆓 - Yandex 的 Alice AI 助手，其模型也用于生成 Yandex 搜索中附带来源链接的 AI 回答。

## 各语种 GEO 资源

以英语以外的语言发布的文章、社区和本地工具，不收录代理商和服务商。

### 中文

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - 中文预印本，探讨 GEO 的知识产权、算法偏见、可解释性和虚假信息等伦理风险，并提出五项应对措施。 (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - 新华网报道 2026 年 5 月 AIIA 可信 GEO 研讨会，涉及中国信通院的 GEO 服务评估、GEO 风险报告和行业自律。 (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - 中国广告协会团体标准，对 GEO 服务商、可信内容来源、禁用手段和效果报告提出要求。 (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - 报道 2026 年中国的 GEO 热潮，解释 GEO 如何瞄准 AI 回答的检索环节，以及批量投放内容如何把一款虚假产品推入 AI 推荐结果。 (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - 长文分析黑帽 GEO 造成的 AI 数据投毒，涵盖监管和平台应对措施，并介绍湖南日报自家的可信 GEO 服务。 (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - 分析 Google 2026 年针对操纵 AI 回答的垃圾内容政策更新，区分 GEO 与付费内容投放，并讨论二者之间的灰色地带。 (2026)

### 日语

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - 记录一项为期 28 天的实验，让网站退出 Google AI Overviews 和 AI Mode，估算二者的点击率是网站平均值的两倍以上。 (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - Ahrefs 针对日语信息类关键词的研究，估算到 2026 年 6 月 Google AI Overviews 使首位结果的点击率下降 62.7%。 (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - 日经 xTrend AI 搜索优化系列的首篇，引用 Ahrefs 数据说明 Google AI Overviews 如何减少日本的点击量，正文大部分仅限付费会员。 (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - Google 日本宣布推出日语版 AI Mode，介绍其查询扇出（query fan-out）技术如何把问题拆分为子主题并分别搜索。 (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - 铃木谦一的演讲报道，认为 GEO 和大语言模型优化（LLMO）都建立在传统 SEO 之上，并给出 Google AI 搜索生成回答的概念模型。 (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - 日经 xTECH 讲解大语言模型优化（LLMO）的文章，LLMO 是日本对 GEO 的常用叫法，文中说明其与 SEO 的区别，需免费注册阅读全文。 (2026)

### 韩语

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - 韩国言论振兴财团的报告，分析 AI 浏览器和零点击回答如何重塑新闻分发和媒体盈利模式。 (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - 韩国言论振兴财团的报告，介绍英国 CMA 于 2026 年对 Google 提出的 AI 退出选项、AI 搜索数据和来源标注等要求，及其对韩国的意义。 (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - 韩国广告团体联合会期刊中的趋势评论，介绍 GEO、Perplexity 和 Gemini 等引擎如何利用搜索数据，以及 E-E-A-T 的作用。 (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - 韩国一家支付公司面向网店的 GEO 指南，提出问答内容、按使用场景撰写商品描述、常见问题和外部提及等五项策略。 (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - Naver 新闻稿，介绍 AI Briefing 如何将创作者的帖子作为来源展示，以及按 AI Briefing 引用每月向约 3000 名创作者付费的 Naver Mate。 (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - GeekNews 上用韩语概述 a16z GEO 文章的帖子，附有读者关于 GEO 与答案引擎优化（AEO）概念重叠的简短讨论。 (2025)

### 西班牙语

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - 探索性研究，在三个时间点向多个 AI 系统提交同一条通用旅游查询，发现酒店品牌的可见度和引用来源波动很大。 (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - 综述 GEO 文献，发现研究逐渐采用可见度、影响力和可验证性指标，并围绕结构、结构化数据和权威性等常见策略展开。 (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - 认为 Google AI Overviews 和 AI Mode 大幅减少了西班牙新闻网站的流量，建议发布商引入 GEO、读者忠诚度建设和集体授权。 (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - 首次为机构知识库提出 GEO 指南，涵盖技术设置、语义结构、元数据、多语言内容和新指标。 (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - 分析 226 万条西班牙语提示词，统计 ChatGPT、Gemini、Perplexity、Copilot、Grok 及 Google AI 功能最常引用的新闻媒体排名。 (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - 概述巴塞罗那大学对 2699 个关键词的研究，发现在涉及西班牙主要新闻媒体的搜索中 29.8% 出现 Google AI Overviews，但突发新闻中很少出现。 (2026)

### 德语

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - 德国数字行业协会的白皮书，探讨从搜索到 AI 回答系统的转变，提出 GEO 的标准定义及其与 SEO 的关系。 (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - 分析 380 万条德语 ChatGPT 回答，显示 2026 年 5 月的模型切换在两天内使被引用域名的构成变化了 47%。 (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - 报道一项涉及 25 万条 AI 回答的研究，揭示 ChatGPT、Google AI Overviews 和 Perplexity 最常引用的来源，居首的是企业网站、YouTube 和 Reddit。 (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - 解释 ChatGPT、Gemini、Copilot 和 Perplexity 如何查找和引用页面，从查询扇出、搜索索引到技术访问，并附面向企业的检查清单。 (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - 比较德语区（DACH）AI 回答中同一域名下被引用与未被引用的页面，发现结构和 Schema 与引用相关，而 llms.txt 没有效果。 (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - BVDW 的简短白皮书，提出衡量品牌在生成式搜索中可见度的 9 项 KPI，并就提示词集和定期复盘给出建议。 (2026)

## 案例研究

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - 分享 Ahrefs 自身的分析数据，AI 搜索访客仅占其流量的 0.5%，却贡献了 12.1% 的注册。 (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - 厂商案例研究，称经 Profound 测量，Ramp 应付账款产品的 AI 搜索可见度升至 22.2%，并列出 Ramp 重点优化的页面和查询。 (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - 介绍 Vercel 如何调整 SEO，让大语言模型更容易发现其内容，称 ChatGPT 带来的新注册约占 10%，而六个月前仅为 1%。 (2025)

## 课程、视频与播客

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Sam Oh 主讲的 12 节免费视频课程，讲解 AI 搜索引擎如何选择引用、提示词研究、面向 AI 搜索的内容与 YouTube、技术设置及 AI 流量追踪。
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - SkillUp 在 Coursera 开设的 4 小时课程，分两个模块，涵盖实体与主题权威、适合 AI 的内容格式、GEO 指标和实操练习，证书需付费。
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - 含 7 节课的免费认证课程，讲解如何被回答引擎引用、问题研究、页面与 Schema 优化，以及衡量 AI 引荐流量和声量占比。
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Aleyda Solis 整理的免费学习路线图，按顺序编排 AI 搜索基础、效果衡量、电商和工具等指南，并附内容优化清单。
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - 面向公关与传播团队的短期证书课程，讲解非付费的第三方报道如何影响 AI 回答、如何测试提示词，以及如何用 GEO 分析结果选择目标媒体。
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Google 搜索关系团队的播客，讲述 Google 搜索幕后的工作原理，包括其 AI 功能和 SEO 社区的热门话题。
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - 含 20 个视频的免费证书课程，涵盖提示词研究、声量占比、品牌提及和面向大语言模型的内容格式，部分课程演示 Semrush 工具。

## 通讯与社区

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Tom Critchlow 在 Substack 上的通讯（原名 The SEO MBA），关注搜索团队适应 AI 搜索过程中的策略与领导力。
- [brightonSEO](https://brightonseo.com/) 💲 - 在布莱顿和圣迭戈举办的大型搜索营销系列会议，提供 SEO、内容和 AI 搜索方面的演讲与培训，英国场设有免费门票抽签。
- [GEO Conference](https://geo-conference.com/) 💲 - 在美国多个城市举办的 GEO 线下单日系列会议，每场限 150 个席位，主要由 GEO 和 SEO 工具厂商赞助。
- [Growth Memo](https://www.growth-memo.com/) 🪙 - Kevin Indig 关于自然增长的通讯，定期发布 AI 搜索行为、引用和流量的数据研究，部分内容仅限付费订阅者。
- [MozCon](https://moz.com/mozcon) 💲 - Moz 举办的营销大会，聚焦 SEO、AI 搜索和 GEO，2026 年以线下巡回形式在伦敦和纽约举行。
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Barry Schwartz 的每日新闻网站，追踪搜索社区讨论以及 Google 和 Bing 的变化，包括其 AI 搜索功能。
- [SEOFOMO](https://seofomo.co/) 🆓 - Aleyda Solis 的每周通讯，汇集 SEO 与 AI 搜索的新闻、指南、工具、活动和招聘信息。

## 其他精选清单

与本清单主题相近的 GEO 和 AI 搜索资源清单，在此一并致谢。

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - 覆盖面广的 GEO 资源清单，收录各平台专项指南、智能体电商、工具、研究、通讯、视频和活动。
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - 以研究为主的 GEO 论文清单，按年份整理。
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - 收录 GEO 免费平台和开源仓库的清单，配套网站提供评分、搜索和免费工具。
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - 按字母排序的 GEO 与 AI 可见度追踪工具目录，附功能与价格简介。
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - 综合性 GEO 清单，涵盖学习资源、工具、AI 搜索引擎、策略、监测、案例研究、社区和平台动态。
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - GEO 清单（原 Tusko/awesome-geo），收录研究、平台官方文档、指南、工具、课程、通讯和社区。
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - 按覆盖引擎、刷新频率、价格和数据导出对比 GEO 工具的表格，由一家 GEO 工具厂商维护，其自家产品也在其中。

## 参与贡献

欢迎参与贡献。提交 Pull Request 前请先阅读[贡献指南](CONTRIBUTING.md#贡献指南)；只需填写英文描述，其他语言由维护者补齐。

## 许可证

在法律允许的范围内，贡献者依据 [CC0 1.0 通用](LICENSE)协议放弃对本清单的全部著作权及相关权利。
