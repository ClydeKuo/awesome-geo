# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Deutsch](README.de.md)

> A curated list of resources on Generative Engine Optimization (GEO): research, guides, standards, tools and AI search engines from around the world.

## Contents

- [What is GEO](#what-is-geo)
- [Introduction](#introduction)
- [Research Papers](#research-papers)
  - [Foundational Papers](#foundational-papers)
  - [Benchmarks and Datasets](#benchmarks-and-datasets)
  - [Attacks and Manipulation](#attacks-and-manipulation)
  - [Citation and Visibility Analysis](#citation-and-visibility-analysis)
  - [Surveys](#surveys)
- [Guides and Articles](#guides-and-articles)
  - [Strategy](#strategy)
  - [Content Writing](#content-writing)
  - [Technical Implementation](#technical-implementation)
  - [Industry Reports and Data](#industry-reports-and-data)
- [Standards and Specifications](#standards-and-specifications)
  - [llms.txt](#llmstxt)
  - [AI Crawlers and robots.txt](#ai-crawlers-and-robotstxt)
  - [Structured Data](#structured-data)
  - [Official Engine Documentation](#official-engine-documentation)
- [Tools](#tools)
  - [AI Visibility Monitoring](#ai-visibility-monitoring)
  - [Content Audit and Optimization](#content-audit-and-optimization)
  - [Open Source Tools and Libraries](#open-source-tools-and-libraries)
  - [llms.txt Generators](#llmstxt-generators)
  - [Crawler Log Analysis](#crawler-log-analysis)
- [AI Search Engines and Assistants](#ai-search-engines-and-assistants)
  - [Global](#global)
  - [China](#china)
  - [Japan](#japan)
  - [South Korea](#south-korea)
  - [Europe](#europe)
  - [Other Regions](#other-regions)
- [Regional GEO Resources](#regional-geo-resources)
  - [Chinese](#chinese)
  - [Japanese](#japanese)
  - [Korean](#korean)
  - [Spanish](#spanish)
  - [German](#german)
- [Case Studies](#case-studies)
- [Courses, Videos and Podcasts](#courses-videos-and-podcasts)
- [Newsletters and Communities](#newsletters-and-communities)
- [Other Curated Lists](#other-curated-lists)
- [Licensing](#licensing)

**Legend:** 🆓 free, 🪙 freemium, 💲 paid, 🔓 open source

## What is GEO

Generative Engine Optimization (GEO) is the practice of making content easy for AI answer engines such as ChatGPT, Perplexity and Google AI Overviews to find, understand and cite. Where SEO competes for rankings in a list of links, GEO aims to have content quoted or referenced inside the generated answer itself, so success is measured in citations and visibility rather than clicks. The term was coined in the paper “GEO: Generative Engine Optimization” by Aggarwal et al. (Princeton University and others, KDD 2024).

## Introduction

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - Search Engine Land explainer defining GEO as earning citations and mentions in AI answers and describing how it builds on SEO fundamentals.
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - Encyclopedia entry defining GEO, tracing the term to the 2023 research paper, listing related names such as AEO and LLMO, and noting criticism.
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - Search Engine Journal report on Google's May 2026 guidance treating AEO and GEO as part of ordinary SEO and debunking llms.txt and chunking.
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - Google's own guidance, stating that optimizing for AI features is still SEO and listing tactics such as llms.txt and chunking as unnecessary.
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - Search Engine Land comparison of SEO and GEO, covering goals, measurement and the practices the two share.
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - Explainer that traces the term GEO to the KDD 2024 paper by Aggarwal et al., compares industry definitions and summarizes what is known about AI visibility.

## Research Papers

### Foundational Papers

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - Demonstrates an agentic system that evaluates nine GEO strategies per content item and speeds up selecting the best one with a bandit approach. (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - Proposes a self-evolving agentic system for GEO that goes beyond static heuristics and single-prompt rewriting to raise visibility in summarized answers. (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - Formalizes GEO as competitor-aware strategy selection and uses Bayesian optimization over combinatorial structures to choose rewriting strategies. (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - Diagnoses why an individual document is not cited by a generative engine and applies targeted repairs instead of uniform rewriting rules. (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - Treats GEO as strategy learning, using planning, editing and evaluation agents to distill reusable editing strategies across tasks and engines. (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - Resolves conflicting revision demands across many queries with a diverge-then-converge framework that mines optimization preferences and fuses them into one revision. (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - Proposes GEO-SFE, a framework that engineers content structure at several hierarchical levels to influence which pages generative engines cite. (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - Proposes FeatGEO, which optimizes interpretable structural, content and linguistic page features to balance citation visibility against content quality. (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - Fine-tunes a BART-base model on synthetic pairs of travel-website text to rewrite content for better discoverability in LLM outputs. (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - Optimizes content for generative search engines without knowing target queries or engine feedback, by inferring user intents and roles in advance. (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - Presents AutoGEO, which learns what generative engines prefer in retrieved content and rewrites web pages accordingly to gain more visibility. (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - Presents white-hat search engine optimization techniques based on generative AI and reports their empirical gains. (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - Introduces GEO and a benchmark for measuring content visibility in generative engine responses. (2023)

### Benchmarks and Datasets

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - Benchmarks conversational SEO methods across tasks, domains and numbers of adopters, finding most are ineffective and classic SEO often works better. (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - Benchmarks defenses against GEO-optimized documents that carry targeted misinformation, using human-verified queries under controlled conditions. (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - Introduces LIVE-GEO to test whether GEO visibility gains hold on the live web, where pages are fetched and ranked by real generative engines. (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - Provides 13,746 consumer product queries with retrieved listings for testing GEO rewriting heuristics across several generative engines in e-commerce. (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - Introduces ALCE, a benchmark with automatic metrics for fluency, correctness and citation quality of LLM answers that cite retrieved evidence. (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - Evaluates GEO ranking-manipulation attacks under one protocol with unified datasets and metrics, comparing their strength and detectability. (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - Releases a dataset of 11,500 user queries and compares the sources and information returned by Google Search, AI Overviews and Gemini. (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - Offers an environment for end-to-end evaluation of search-augmented GEO strategies, covering retrieval and ranking as well as generation. (2026)

### Attacks and Manipulation

Adversarial GEO research on how answer engines can be manipulated, for example through prompt injection or ranking attacks, and how to defend against it.

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - Proposes CORE, an optimization method that controls where items appear in LLM-generated product recommendations. (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - Audits evidence on llms.txt-style manifests for AI search, finding little automatic fetching, and evaluates their security implications. (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - Shows GEO attacks can escalate into citation wars that degrade content quality, and studies mechanism design for win-win outcomes. (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - Shows that jointly crafted image perturbations and text can manipulate how vision-language models rank products. (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - Argues that GEO risks concentrated influence, undisclosed commercial influence and academic-industry blind spots, and calls for answer-level governance such as disclosure and auditing. (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - Defends LLM-based rankings by detecting the persuasive structure sellers embed in content to push their items to the top. (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - Defends generative search against malicious GEO rewrites that stay factually consistent and so evade fact checking and perplexity filters. (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - Models ranking-manipulation attacks on LLM search as an infinitely repeated prisoner's dilemma and analyzes when cooperation can be sustained. (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - Analyzes which publishers generative engines cite and how hard it is for attackers to inject malicious content into the sources behind answers. (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - Presents an attack that uses energy-based optimization to craft fluent, hard-to-detect prompts that manipulate LLM-driven rankings. (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - Studies competing poisoning attacks on RAG systems, where several adversaries steer the same query toward different targets, and introduces the PoisonArena benchmark. (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - Introduces preference manipulation attacks that steer LLM selections toward attacker content and shows they create a prisoner's dilemma among sellers. (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - Studies SEO-style attacks in which adversarial passages are crafted to be retrieved by dense embedding search, the retrieval layer behind many RAG systems. (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - Shows that adding a crafted strategic text sequence to a product page can make an LLM-based search engine recommend that product first. (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - Shows that prompt injections in web page text can raise a source's position in conversational search results, using real consumer product pages. (2024)

### Citation and Visibility Analysis

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - Reports a preregistered field experiment (N=1,100) finding that removing AI Overviews and AI Mode raises click-through to publishers. (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - Runs a causal audit of how document presentation changes which of two equally supporting sources an agentic search engine cites. (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - Shows that AI search answers vary across runs, prompts and time, so visibility must be measured repeatedly rather than once. (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - Separates citation selection from citation absorption and analyzes 602 prompts across ChatGPT, Google AI and Perplexity. (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - Analyzes nearly 35,000 prompt observations and finds brand mention rates rise sharply once a brand's own domain appears in live retrieval. (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - Studies how to measure brand visibility across ChatGPT, Claude, Perplexity and Gemini, including which sources the engines rely on when citing brands. (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - Argues that GEO visibility scores depend on the prompt corpus and weights, which define an answer market that may not match real demand. (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - Tracks 55,393 queries over 40 days to measure when AI Overviews appear, the quality of their sources, claim fidelity and publisher impact. (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - Quantifies how Google results and generative AI answers differ in cited domains, domain types, query intent and freshness. (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - Audits ChatGPT, Copilot, Google and Perplexity, finding very low cross-engine URL overlap that limits engine-agnostic GEO scores. (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - Audits four generative search engines on 712 queries and finds about 16 percent of cited sources appear to be AI-generated. (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - Uses Google AI Overviews and Reddit to show that AI search raised engagement in cited communities, with the gains fading after AI Mode launched. (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - Observes how four ChatGPT Web settings rewrite queries, retrieve pages and pick citations, with retrieval frequency predicting citation. (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - Analyzes citation behavior, source attribution and entity exposure across four Chinese-language generative search platforms using 614 queries. (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - Analyzes 158,099 answers and finds that the pages ChatGPT retrieves for its rewritten sub-queries explain citations far better than page properties do. (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - Introduces a 16-pillar page audit and finds that metadata, semantic HTML and structured data relate most to citations across three engines. (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - Compares AI search engines with Google in controlled experiments across verticals and languages, finding a strong bias toward earned media over brand-owned content. (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - Builds ConflictingQA to show that LLMs rely heavily on a page's relevance to the query while largely ignoring stylistic cues such as scientific references. (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - Audits Bing Chat, NeevaAI, Perplexity and YouChat for citation recall and precision, finding many statements lack full citation support. (2023)

### Surveys

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - Reviews 45 studies from 2023 to 2026, frames GEO as a multi-stage stochastic pipeline and offers a checklist for grading GEO claims. (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - Systematically categorizes LLM-based search agents by architecture, optimization, application and evaluation and lists open challenges. (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - Surveys generative search and recommendation with large language models from a technical perspective. (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - Examines how search engines and LLMs can benefit each other, covering search for improving LLMs and LLMs for improving search. (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - Surveys how large language models are used across information retrieval systems, including query rewriting, retrieval, reranking and reading. (2023)

## Guides and Articles

### Strategy

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - Gives a practical introduction to how generative engine optimization helps content appear in AI-powered search results. (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - Explains what GEO is, how it differs from SEO and which techniques help content get cited in AI answers, with a downloadable audit checklist. (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - Explains how AI search differs from traditional search, lays out five GEO tactics and covers how to measure GEO success, noting that AI search still relies on traditional search. (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - Argues that search is moving from link-based ranking to language-model answers and frames GEO as the next phase of the roughly $80 billion SEO market. (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - Presents SEEN, a four-layer GEO framework of Structure, Evidence, Entity and Notability, with a 41-item checklist scored 0 or 1 to reveal the weakest layer. (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - Walks through a ten-step GEO process, from choosing priority topics and a baseline to reading cited sources, improving content and reporting results. (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - Opens an eight-part AEO guide covering how AEO differs from SEO, how answer engines work, tracking AI visibility, choosing prompts and fixing mistakes in AI answers. (2025)

### Content Writing

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - Explains what Google's AI Overviews are, how they are generated from web sources and how site owners can optimize for and track their visibility. (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - Describes a two-stage method for ChatGPT citation, being retrieved then being quotable, with each step backed by the authors' own measurements such as which cited domains allow AI crawlers. (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - Reports what 13 buyer-question tests in ChatGPT and the site's server logs showed, including a negative result, and which AI bots to allow. (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - Walks through seven steps for getting content cited by AI search engines such as ChatGPT and Google, from keyword research to formatting. (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - Gives eight steps for ranking in ChatGPT search by making content easy for AI systems to extract and by building off-site consensus. (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - Lists ten ways to improve a brand's visibility in LLM-generated responses, framed as LLM optimization (LLMO). (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - Microsoft Advertising guidance on what makes content usable in AI search answers, including schema, clear headings, self-contained Q&A blocks and mistakes such as hiding answers in tabs or PDFs. (2025)

### Technical Implementation

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - Reports an investigation finding that JSON-LD injected client-side, for example through Google Tag Manager, is missed by AI crawlers that cannot execute JavaScript. (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - Shows how to track AI-driven referral traffic from tools such as ChatGPT and Gemini in Google Analytics 4. (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - Introduces serving pages as markdown to AI agents, showing how it cuts token use, with one post falling from 16,180 tokens in HTML to 3,150 in markdown. (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - Presents MERJ and Vercel data on how ChatGPT, Claude and other AI crawlers handle JavaScript and content types, with recommendations for site owners. (2024)

### Industry Reports and Data

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - Studies 3,000 websites to estimate how much traffic AI chatbots send, finding 63% of sites receive some and that three chatbots account for 98% of it. (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - Extends Cloudflare Radar with industry-focused data and a breakdown of AI bot traffic by crawl purpose. (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - Analyzes 31 million AI citations and 105 publishers' robots.txt files, finding that blocking AI crawlers works on some models and does nothing on others. (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - Tracks 16 months of data showing AI Overview citations overlapping with organic rankings growing from 32% to 54%, with industry breakdowns. (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - Presents Ahrefs research finding that AI Overviews reduce clicks by 34.5%, countering Google's claim that they increase clicks. (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - Tests eight AI search tools on news excerpts and finds they cite sources incorrectly in more than 60 percent of queries. (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - Collects 2026 Similarweb data on ChatGPT, Gemini and Claude market share, referral traffic, citations and ads inside AI answers. (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - Analyzes 75,000 brands to identify which search factors are most likely to influence brand mentions in AI Overviews. (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - Compares Google users' behavior in March 2025 and finds those who saw an AI summary were less likely to click links to other websites. (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - Tracks 37,500 citations across ChatGPT, Gemini, Copilot and Google, finding that half disappear the next day and most come back. (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - Examines 300,000 domains to see how widely llms.txt is used and whether it affects how often a domain is cited by LLMs. (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - Analyzes about 7 billion log files from November 2024 to March 2026 to show how OpenAI's three crawlers interact with the web. (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - Reports a 212% surge in ChatGPT news queries and a 26% drop in publisher traffic as generative AI reshapes the news sector. (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - Analyzes more than 10 million keywords to show how Google's AI Overviews are changing search and what that means for SEO. (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - Finds from 863K SERPs that 38% of AI Overview citations come from top-10 pages, down from 76% a year earlier. (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - Tracks 1,885 pages that added JSON-LD and measures the impact on citations in Google AI Overviews, AI Mode and ChatGPT. (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - Studies 1.4 million prompts to show how page titles, URLs and snippets influence which retrieved pages ChatGPT cites. (2026)

## Standards and Specifications

Specifications and official documentation that govern how AI crawlers access a site and how answer engines read its content.

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - Hosts the source of the llms.txt proposal together with its reference tooling and discussion.
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - Reports John Mueller calling llms.txt speculative for now and saying he prefers WebMCP, a Google-backed alternative.
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - Reports John Mueller's statement that no AI system currently uses llms.txt, based on what server logs show. (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - Directory of websites that implement llms.txt, with example files for APIs, platforms and developer tools.
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - Measures llms.txt adoption among the top 1,000 and top 10,000 domains in a September 2026 study, with methodology and downloadable data. (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - Lists websites that publish an llms.txt file so developers can browse real examples of the format.
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - Lists sites that publish llms.txt and shows the AI permissions they declare for training, retrieval and summarization.
- [The /llms.txt file](https://llmstxt.org) 🆓 - Proposes a /llms.txt markdown file at a site root that gives language models a curated overview of the site and links to its most useful content. (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - Makes the case for llms.txt with examples from Vercel, Google and Anthropic and answers critics who say general SEO practice is enough. (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - Explains what the llms.txt file is and examines whether adding it does anything for developers and marketers.

### AI Crawlers and robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - Lists 25 AI crawler user agents from 12 operators in four groups, with how many of 157 platforms block each in robots.txt. (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - Collects known robots.txt entries, meta tags and other settings that site owners can use to opt out of AI training.
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - Maintains a community list of AI agents and crawlers to block, with generated robots.txt and server configuration files.
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - Describes Amazonbot, Amzn-SearchBot and Amzn-User and the independent robots.txt settings that control each of them.
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - Explains how Pay Per Crawl lets site owners charge AI crawlers for access, answering unpaid requests with HTTP 402; the feature is in closed beta.
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - Lists the Google fetchers that act on a user request, such as Google Read Aloud, and notes that they generally ignore robots.txt rules.
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - Documents the common Google crawlers, including Googlebot, with their user agent strings and robots.txt tokens.
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - Lists about 40 Yandex robot user agents with their purpose and robots.txt behavior, and explains how to verify them with reverse DNS.
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - Standardizes a common vocabulary and attachment methods, such as robots.txt and HTTP headers, for expressing preferences on how content is collected and used by AI.
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - Standardizes methods for cryptographically authenticating automated clients such as AI crawlers and agents, replacing IP allowlists and user-agent strings.
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - Explains that DuckAssistBot gathers sources for DuckDuckGo's AI-assisted answers, is not used for AI training and can be blocked in robots.txt.
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - Lists the Meta crawlers, including Meta-WebIndexer for Meta AI search and Meta-ExternalAgent for AI model training, and what each is used for.
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - Describes the MistralAI-User, MistralAI-Index and MistralAI-Training user agents and what each is used for.
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - Specifies the syntax and semantics of robots.txt, the Robots Exclusion Protocol that AI crawlers are expected to honor. (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - Announces that Google plans to honor a shared AI training opt-out in robots.txt based on an IETF AIPREF draft, with support targeted for 2027. (2026)

### Structured Data

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - Explains how Google uses structured data markup to understand content, which formats it supports and where to place the markup.
- [JSON-LD](https://json-ld.org) 🆓 - Hosts the JSON-LD specifications, the JSON-based linked data format in which Schema.org markup is commonly written.
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - Tests a URL or code snippet and reports which Google rich results its structured data can generate.
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - Summarizes an Ahrefs report testing whether adding schema markup to pages already cited by AI improved their citation rates. (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - Validates structured data of any Schema.org type in JSON-LD, Microdata or RDFa.
- [Schema.org](https://schema.org) 🆓 - Hosts the shared vocabulary of types and properties used to mark up web pages for search engines and other consumers.
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - Hosts the source of the Schema.org vocabulary and its supporting software.
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - Catalogs the structured data types that power features in Google Search, with examples and implementation guidance.

### Official Engine Documentation

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - Describes Applebot, which feeds search features in Spotlight, Siri and Safari, and Applebot-Extended, which publishers can disallow to opt out of generative AI training.
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - Explains how AI Overviews and AI Mode work in Google Search and how site owners can approach inclusion of their content in them.
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - Baidu's webmaster platform with site resource submission, crawl and robots data, search widgets and AI traffic analysis.
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - Describes CCBot, the crawler behind the Common Crawl open web archive, with its user agent and ways to verify and block it.
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - Describes the ClaudeBot, Claude-User and Claude-SearchBot crawlers and how site owners can block each through robots.txt.
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - Documents the IndexNow protocol for notifying participating search engines of new, updated or deleted URLs.
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - Announces a Bing Webmaster Tools report showing when a site is cited in answers across Microsoft Copilot and Bing's AI-generated summaries. (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - Announces Search Console reports showing how often pages appear in generative AI features such as AI Overviews and AI Mode, by page, country, device and date. (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - Announces the program through which Perplexity shares revenue with participating publishers and supports them with API access and developer help. (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - Naver's webmaster guide and tools covering what a site needs for Naver Search to discover and index it; AI Briefing draws on web documents from the same index.
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - Describes the OAI-SearchBot, GPTBot, ChatGPT-User and OAI-AdsBot user agents and what each is used for.
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - Describes PerplexityBot, which surfaces sites in Perplexity search results, and Perplexity-User, which fetches pages on a user request and generally ignores robots.txt.
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - Answers publisher and developer questions about appearing in ChatGPT search, the OAI-SearchBot crawler and referral traffic from ChatGPT.
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - Explains the Search Console control for including or excluding content from AI Overviews, AI Mode and generative AI in Discover, and notes it does not affect AI training.
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Yandex help page explaining how its AI answers split a question into parts, pick and analyze sources, and link to them in the response.
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Offers Google's recommended practices for making content perform well in its AI experiences on Search. (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Yandex's webmaster service for verifying sites, monitoring indexing and diagnosing crawl problems in Yandex Search.
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - Announces separate publisher preferences for AI training and AI grounding, set through robots.txt, meta tags or X-Robots-Tag headers and read by Microsoft from February 2027. (2026)

## Tools

### AI Visibility Monitoring

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - Checks without signup how ChatGPT, Gemini, Perplexity, Copilot and AI Overviews mention and cite a brand.
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - Reports how often a brand appears in answers from Google AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini and Copilot, using a prompt database or custom prompts.
- [AthenaHQ](https://athenahq.ai) 🪙 - Tracks brand visibility across AI models such as ChatGPT, Perplexity, Gemini, AI Overviews and Copilot and suggests content changes, with a free plan that includes starter credit.
- [Geoptie](https://geoptie.com) 💲 - Shows how ChatGPT, Gemini, Claude, Perplexity and Google AI answer buyer prompts and which sources they cite.
- [Goodie](https://higoodie.com) 💲 - Tracks brand visibility across AI engines such as ChatGPT, AI Overviews, Perplexity and Copilot and recommends optimizations, with more engines on higher plans.
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - Scores how ChatGPT, Perplexity and Gemini describe a brand in a free one-time check, with paid weekly monitoring offered as HubSpot AEO.
- [Knowatoa](https://www.knowatoa.com) 💲 - Tracks brand visibility in ChatGPT, Google AI Overviews, AI Mode and other AI search services, with prompt tracking and reporting integrations.
- [Otterly.AI](https://otterly.ai) 💲 - Monitors brand mentions and website citations in ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity and Copilot, with competitor comparison and prompt research.
- [Peec AI](https://peec.ai) 💲 - Tracks brand visibility, position and sentiment in AI search platforms such as ChatGPT, Perplexity, AI Overviews, AI Mode and Gemini, with prompt-level reports.
- [Profound](https://www.tryprofound.com) 💲 - Tracks brand visibility in answer engines such as ChatGPT, Perplexity, Google AI Mode, Gemini and Claude through daily prompt runs and citation analysis.
- [Promptwatch](https://promptwatch.com) 💲 - Tracks brand visibility across AI models including ChatGPT, Google AI Overviews, Perplexity, Claude and Gemini by running prompts, with AI crawler analytics on higher plans.
- [Rankscale](https://rankscale.ai) 💲 - Tracks brand mentions and citations across more than 17 AI search engines on credit-based plans, with brand dashboards and an API on higher tiers.
- [Scrunch](https://scrunch.com) 💲 - Monitors prompts, citations, competitor rankings and AI bot crawl activity across major AI platforms, and can serve an AI-optimized version of a site.
- [Searchable](https://www.searchable.com) 💲 - Tracks brand mentions, competitor comparisons and cited sources in ChatGPT, Google AI Overviews and Perplexity, with Claude, Gemini and other AI engines as paid add-ons.
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - Tracks brand mentions and visibility in ChatGPT, Google AI Mode and other AI platforms through prompt tracking and competitor monitoring, included in Semrush's SEO plus AI Search plans.
- [Trakkr](https://trakkr.ai) 💲 - Tracks how a brand appears across eight AI models through prompt tracking, with multi-brand plans and client portals on the higher tier.
- [Waikay](https://waikay.io) 🪙 - Analyzes how ChatGPT, Google, Claude and Perplexity describe a brand, flagging hallucinations and knowledge gaps and suggesting action plans.
- [Writesonic](https://writesonic.com) 💲 - Monitors brand visibility in AI answers, covering ChatGPT, Gemini and Google AI Overviews on lower plans, alongside article writing and site-audit fixes.
- [ZipTie](https://ziptie.ai) 💲 - Tracks chosen prompts across seven engines, including ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity and Copilot, with usage-based pricing per check.

### Content Audit and Optimization

- [Clearscope](https://www.clearscope.io) 💲 - Recommends content improvements for Google and AI answers and tracks queries in ChatGPT and Gemini to show when a brand is mentioned.
- [Frase](https://www.frase.io) 💲 - Scores content for SEO and GEO and monitors brand visibility in AI engines such as ChatGPT and Google AI, with more engines on higher plans.
- [GeoReady](https://geoready.dev) 🪙 - Audits whether ChatGPT, Perplexity, Claude and Gemini can reach, read and cite a site, scoring it out of 100 across nine categories with ranked fixes.
- [NEURONwriter](https://neuronwriter.com) 💲 - Suggests terms and structure from top-ranking pages to optimize content for Google and AI answers, and monitors brand share of voice across AI models.
- [Surfer](https://surfer.ai) 💲 - Combines a content editor that scores drafts against competitors with an AI Tracker for brand mentions in ChatGPT, Perplexity, Gemini, AI Overviews and AI Mode.

### Open Source Tools and Libraries

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - Agent-first operating platform for AEO and GEO work, distributed as an npm package.
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - Self-hostable platform that tracks how ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok and Google AI Overviews mention and cite a brand.
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - Schedules prompts across several LLM providers, captures their web-search citations and tracks brand mentions through a dashboard and CLI.
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - Scores a site from 0 to 100 on whether AI engines can crawl, understand and cite it, through a CLI, Python library and MCP server.
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - Tracks how ChatGPT, Perplexity, Gemini and Google AI Mode mention and cite a brand, as a self-hosted dashboard with an MCP server and CLI.
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - Checks whether a website is reachable and readable by AI crawlers and scores it, as a PyPI package and GitHub Action.
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - Provides a pluggable Go framework for GEO with built-in strategies and support for registering custom ones.
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - Deterministic content linter that runs in CI or pre-commit to flag structure and sourcing issues in documentation and static sites, published as an npm package.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - Open-source platform for tracking and improving a brand's presence in AI answers.
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - Self-hosted visibility tracker, a single Go binary with SQLite and an MCP server, that records how major AI engines mention and cite a brand.
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - NGINX module that serves Markdown versions of pages to AI agents through HTTP content negotiation.
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - Self-hostable tracker that monitors how ChatGPT, Perplexity, Gemini, Claude and Google AI Overviews mention and cite a brand through their product interfaces.
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - Scores a site from 0 to 100 for agent readability and generates Markdown copies of pages plus robots.txt, llms.txt and sitemap.xml.
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - Type-checked Schema.org JSON-LD for React.
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - TypeScript types for writing Schema.org JSON-LD.
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - Builds a Schema.org JSON-LD graph for JavaScript sites, with an Astro integration.
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - PHP fluent builder for Schema.org types that outputs JSON-LD.

### llms.txt Generators

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - Generates llms.txt, JSON-LD, Markdown mirrors and AI crawler controls at build time for Vite, Astro, Next.js and Nuxt sites, and validates them.
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - Apify Actor that crawls a website and extracts its content to create an llms.txt file.
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - Crawls a site to draft an llms.txt file, with page discovery, added business context and daily updates of the public file.
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - Command-line tool that converts a sitemap.xml into an llms.txt file.
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - MkDocs plugin that generates an /llms.txt file for a documentation site.
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - Nuxt module that automatically generates /llms.txt markdown documentation for an application.
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - Sphinx extension that generates an llms.txt file.
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - VitePress plugin that generates LLM-friendly documentation files.
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - Builds an llms.txt draft from a public homepage by checking up to 30 pages found through the sitemap and internal links, without signup.
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - Generates and refreshes an llms.txt file automatically inside the free Yoast SEO plugin, with automatic or manual choice of key content.

### Crawler Log Analysis

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - Curated list of AI crawler user agents with a Node CLI and GitHub Action that audit robots.txt, test reachability and read access logs.
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - Shows which AI services crawl a site, lets owners allow or block each crawler and reports which ones obey robots.txt; available on all Cloudflare plans.
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - Cloudflare Worker that detects and tracks AI crawler and LLM bot traffic at the edge.
- [Known Agents](https://knownagents.com) 🪙 - Offers a directory of AI agents and bots, a robots.txt checker and agent analytics, with a free plan limited to 100,000 events per month.

## AI Search Engines and Assistants

AI answer engines grouped by region, with their official sites, webmaster documentation and known crawler user agents where available.

### Global

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Microsoft Bing's conversational search mode, formerly Copilot Search, which in 2026 was split into AI Mode and the AI Overview summaries shown in regular results.
- [Brave Search](https://brave.com/search/) 🪙 - Brave's search engine built on its own independent index, with Answer with AI summaries that cite their sources and an Ask Brave chat mode for follow-up questions.
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - OpenAI's ChatGPT with built-in web search, which answers questions in conversation and links to the pages it used.
- [Claude](https://claude.ai) 🪙 - Anthropic's Claude assistant, which can search the web during a conversation and cite the pages behind its answer.
- [Duck.ai](https://duck.ai) 🪙 - DuckDuckGo's anonymized chat with third-party AI models, reachable from search results; DuckDuckGo search also offers optional AI-assisted answers.
- [Gemini](https://gemini.google.com) 🪙 - Google's Gemini AI assistant, which draws on Google Search for current information in its answers.
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Google Search's conversational mode, built on Gemini, which answers complex questions, takes follow-ups and links to sources on the web.
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Google Search's generative summaries shown above regular results, with links to the sources they draw on, in more than 120 countries and territories.
- [Grok](https://grok.com) 🪙 - AI assistant from xAI, now part of SpaceX, which searches the web and posts on X to answer questions about current events.
- [Kagi Assistant](https://kagi.com/assistant) 💲 - Kagi's chat assistant for paying members, which pairs models from many providers with optional access to Kagi's ad-free search results.
- [Meta AI](https://www.meta.ai) 🪙 - Meta's AI assistant on the web and inside WhatsApp, Instagram and Facebook, which can pull in web search results for current questions.
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Microsoft's consumer Copilot assistant, which uses Bing web results to answer questions and cites the pages it draws on.
- [Perplexity](https://www.perplexity.ai) 🪙 - AI answer engine that searches the web in real time and returns conversational answers with numbered source citations.

### China

- [ChatGLM](https://chatglm.cn) 🆓 - Zhipu AI's Chinese assistant (Zhipu Qingyan), built on its GLM models, with web search and agent features.
- [DeepSeek](https://www.deepseek.com) 🆓 - DeepSeek's chat assistant built on its open-weight models, with an optional web search mode for up-to-date answers.
- [Doubao](https://www.doubao.com) 🆓 - ByteDance's general-purpose AI assistant, which searches the web to answer questions in chat and lists the sources it consulted.
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - Baidu's ERNIE Bot assistant (formerly Wenxin Yiyan), now served on the web as Baidu Wenxin Assistant and connected to Baidu Search.
- [Kimi](https://www.kimi.com) 🪙 - Moonshot AI's Kimi assistant, known for long-context reading, which searches the web and cites the pages it reads.
- [Metaso](https://metaso.cn) 🪙 - MetaSOTA's ad-free Chinese AI search engine, which answers questions with cited sources and can also search academic literature.
- [Quark](https://www.quark.cn) 🪙 - Alibaba's Quark, a search and browser app rebuilt around an AI assistant that answers queries with generated results.
- [Qwen](https://www.qianwen.com) 🆓 - Alibaba's Qwen app (formerly Tongyi), an AI assistant built on its Qwen models with web search; the international web version is Qwen Chat.
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - Tencent's AI assistant, which answers with web search results that include articles from WeChat Official Accounts.
- [Yuanbao Search](https://so.qq.com) 🆓 - Tencent's AI web search site, which cites its sources, can search WeChat Official Account and Channels content and offers an AI mode for follow-up questions.

### Japan

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - LY Corporation's AI agent, launched in April 2026 by merging Yahoo! JAPAN Search's AI Assistant and LINE AI, and opened from the Yahoo! JAPAN search box and LINE.
- [Felo](https://felo.ai) 🪙 - Multilingual AI search engine from a Tokyo startup that answers with citations and can search sources across languages.

### South Korea

- [A. (A-dot)](https://adot.ai) 🆓 - SK Telecom's AI personal assistant, which offers an AI search feature developed with Perplexity alongside several chat models.
- [Kanana](https://kanana.ai) 🆓 - Kakao's AI brand, covering the Kanana in KakaoTalk assistant and open-source Kanana models, with the KakaoTalk-based Kanana Space agent announced in October 2026.
- [Liner](https://liner.com) 🪙 - AI search and research assistant from a Seoul-based company, focused on cited answers and academic sources.
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - Naver Search's generative answers built on HyperCLOVA X, which summarize results at the top of the page and show the source content they used.
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - Naver's conversational AI search tab, opened to all users in June 2026, which answers in dialogue with product, place and booking cards.
- [Wrtn](https://wrtn.ai) 🆓 - Korean AI assistant from Wrtn Technologies, with a free AI search feature that answers from live web results and lists its sources.

### Europe

- [Ecosia AI search](https://www.ecosia.org) 🆓 - AI search features in Ecosia, the Berlin-based search engine that funds tree planting; users can switch them off for AI-free results.
- [Lumo](https://lumo.proton.me) 🪙 - Proton's privacy-focused AI assistant, based in Switzerland, with built-in web search and no use of queries for ad targeting.
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - Mistral AI's assistant, renamed from Le Chat to Vibe, which pairs a chat assistant with web search and a coding agent.

### Other Regions

- [Alice AI](https://alice.yandex.ru) 🆓 - Yandex's Alice AI assistant, whose models also generate the source-linked AI answers in Yandex Search.

## Regional GEO Resources

Articles, communities and local tools published in languages other than English; agencies and service providers are not listed.

### Chinese

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - Chinese-language preprint on the ethical risks of GEO, such as intellectual property, algorithmic bias, explainability and misinformation, with five proposed responses. (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - Xinhua report on the May 2026 AIIA seminar on trustworthy GEO, covering CAICT's GEO service evaluations, a report on GEO risks and industry self-regulation. (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - China Advertising Association group standard that sets requirements for GEO service providers, trusted content sources, prohibited techniques and results reporting. (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - Feature on the 2026 GEO boom in China, explaining how GEO targets the retrieval step of AI answers and how mass content seeding pushed a fake product into AI recommendations. (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - Long-form analysis of AI data poisoning through black-hat GEO, covering regulation and platform countermeasures and including the Hunan Daily's own trusted-GEO service. (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - Analysis of Google's 2026 spam policy update against manipulating AI answers, separating GEO from paid content seeding and discussing the grey areas between them. (2026)

### Japanese

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - Write-up of a 28-day test that opted a site out of AI Overviews and AI Mode, estimating their click-through rate at more than twice the site average. (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - Ahrefs study of Japanese informational keywords estimating that AI Overviews cut the first result's click-through rate by 62.7% by June 2026. (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - Opening part of a Nikkei xTrend series on AI search optimization, citing Ahrefs data on how AI Overviews cut clicks in Japan; most of the text is for paying members. (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - Google Japan announcement of AI Mode in Japanese, describing how its query fan-out technique splits a question into subtopics and runs a search for each. (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - Report of a talk by Kenichi Suzuki arguing that GEO and LLMO rest on conventional SEO, with a conceptual model of how Google's AI search builds its answers. (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - Nikkei xTECH explainer on LLMO, the term widely used in Japan for GEO, and how it differs from SEO; free registration is needed to read it in full. (2026)

### Korean

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - Korea Press Foundation report on how AI browsers and zero-click answers reshape news distribution and publishers' revenue models. (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - Korea Press Foundation report on the UK CMA's 2026 requirements for Google, such as AI opt-outs, AI search data and source attribution, and what they mean for Korea. (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - Trend review in the Korea Federation of Advertising Associations journal introducing GEO, how engines such as Perplexity and Gemini draw on search data, and the role of E-E-A-T. (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - Guide to GEO for online shops from a Korean payments company, with five tactics such as Q&A content, use-case product descriptions, FAQs and outside mentions. (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - Naver press release on how AI Briefing shows creators' posts as sources, and on Naver Mate, which pays about 3,000 creators a month based on AI Briefing citations. (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - GeekNews post summarizing a16z's essay on GEO in Korean, with a short reader discussion of how the terms GEO and AEO overlap. (2025)

### Spanish

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - Exploratory study that ran one generic travel query through several AI systems at three points in time and found hotel brand visibility and cited sources highly volatile. (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - Reviews GEO literature and finds it converging on visibility, influence and verifiability metrics and on recurring strategies such as structure, structured data and authority. (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - Argues that AI Overviews and AI Mode have sharply cut traffic to Spanish news sites and that publishers should add GEO, reader loyalty and collective licensing. (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - Proposes the first GEO guidelines for institutional repositories, covering technical setup, semantic structure, metadata, multilingual content and new metrics. (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - Analysis of 2.26 million Spanish prompts ranking which news outlets ChatGPT, Gemini, Perplexity, Copilot, Grok and Google's AI features cite most often. (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - Summary of a University of Barcelona study of 2,699 keywords that found AI Overviews on 29.8% of searches about major Spanish news outlets but rarely on breaking news. (2026)

### German

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - German digital industry association whitepaper on the shift from search to AI answer systems, with a proposed standard definition of GEO and how it relates to SEO. (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - Analysis of 3.8 million German-language ChatGPT answers showing that a May 2026 model switch shifted the mix of cited domains by 47% within two days. (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - Report on a study of 250,000 AI answers showing which sources ChatGPT, AI Overviews and Perplexity cite most, led by company websites, YouTube and Reddit. (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - Explains how ChatGPT, Gemini, Copilot and Perplexity find and cite pages, from query fan-out and search indexes to technical access, with a checklist for companies. (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - Compares cited and uncited pages of the same domains in DACH AI answers, finding that structure and schema correlate with citations while llms.txt shows no effect. (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - Short BVDW whitepaper proposing nine KPIs for measuring brand visibility in generative search, with advice on prompt sets and regular review. (2026)

## Case Studies

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - Shares Ahrefs' own analytics showing that AI search visitors were 0.5% of its traffic but 12.1% of signups. (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - Vendor case study reporting Profound-measured AI search visibility for Ramp's accounts payable product rising to 22.2%, with the pages and queries Ramp targeted. (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - Describes how Vercel adapts SEO for LLM discovery, reporting that ChatGPT referred around 10% of its new signups, up from 1% six months earlier. (2025)

## Courses, Videos and Podcasts

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Free 12-lesson video course by Sam Oh on how AI search engines choose citations, prompt research, content and YouTube for AI search, technical setup and tracking AI traffic.
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - Four-hour Coursera course by SkillUp in two modules, covering entities and topical authority, AI-friendly content formats, GEO metrics and hands-on labs; the certificate is paid.
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - Free certification course of seven lessons on being cited by answer engines, question research, on-page and schema work, and measuring AI referrals and share of voice.
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Free learning roadmap curated by Aleyda Solis that orders guides on AI search fundamentals, measurement, ecommerce and tools, with a content optimization checklist.
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - Short certificate course for PR and communications teams on how earned media shapes AI answers, prompt testing and using GEO insights in media targeting.
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Podcast from the Google Search Relations team about how Google Search works behind the scenes, including its AI features and current SEO community topics.
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - Free 20-video course with a certificate on prompt research, share of voice, brand mentions and formatting content for LLMs; several lessons demonstrate Semrush tools.

## Newsletters and Communities

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Substack newsletter by Tom Critchlow, formerly The SEO MBA, on strategy and leadership for search teams adapting to AI search.
- [brightonSEO](https://brightonseo.com/) 💲 - Large search marketing conference series held in Brighton and San Diego, with talks and training on SEO, content and AI search, plus a free ticket ballot for the UK event.
- [GEO Conference](https://geo-conference.com/) 💲 - In-person, single-day conference series on generative engine optimization held in US cities, limited to 150 seats per event and sponsored mainly by GEO and SEO tool vendors.
- [Growth Memo](https://www.growth-memo.com/) 🪙 - Kevin Indig's newsletter on organic growth, with regular data studies on AI search behavior, citations and traffic; some issues are for paid subscribers.
- [MozCon](https://moz.com/mozcon) 💲 - Moz's marketing conference on SEO, AI search and GEO, run in 2026 as an in-person roadshow with events in London and New York.
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Daily news site by Barry Schwartz that tracks search community discussions and changes to Google and Bing, including their AI search features.
- [SEOFOMO](https://seofomo.co/) 🆓 - Weekly newsletter by Aleyda Solis collecting SEO and AI search news, guides, tools, events and jobs.

## Other Curated Lists

Lists covering GEO and AI search that overlap with this one, credited here with thanks.

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - Broad GEO resource list with platform-specific guides, agentic commerce, tools, research, newsletters, videos and events.
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - Research-focused list of GEO papers, arranged by year.
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - List of free platforms and open-source repositories for GEO, with scores, search and free tools on a companion website.
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - Alphabetical directory of GEO and AI visibility tracking tools with short notes on features and pricing.
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - General GEO list covering learning resources, tools, AI search engines, strategies, monitoring, case studies, communities and platform news.
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - GEO list (formerly Tusko/awesome-geo) of research, official platform documentation, guides, tools, courses, newsletters and communities.
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - Comparison table of GEO tools by engines covered, refresh rate, price and data export, maintained by a GEO tool vendor that lists itself too.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request; an English description is all you need, and maintainers add the other languages.

## Licensing

To the extent possible under law, the contributors have waived all copyright and related rights to this list under [CC0 1.0 Universal](LICENSE).
