# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md) | **日本語** | [한국어](README.ko.md) | [Español](README.es.md) | [Deutsch](README.de.md)

> 生成エンジン最適化（GEO）の厳選リソース集です。研究論文、ガイド、技術仕様、ツール、世界各地の AI 検索エンジンをまとめています。

## 目次

- [GEO とは](#geo-とは)
- [入門](#入門)
- [研究論文](#研究論文)
  - [基礎となる論文](#基礎となる論文)
  - [ベンチマークとデータセット](#ベンチマークとデータセット)
  - [攻撃と操作](#攻撃と操作)
  - [引用と可視性の分析](#引用と可視性の分析)
  - [サーベイ](#サーベイ)
- [ガイドと記事](#ガイドと記事)
  - [戦略](#戦略)
  - [コンテンツ制作](#コンテンツ制作)
  - [技術的な実装](#技術的な実装)
  - [業界レポートとデータ](#業界レポートとデータ)
- [標準と技術仕様](#標準と技術仕様)
  - [llms.txt](#llmstxt)
  - [AI クローラーと robots.txt](#ai-クローラーと-robotstxt)
  - [構造化データ](#構造化データ)
  - [各エンジンの公式ドキュメント](#各エンジンの公式ドキュメント)
- [ツール](#ツール)
  - [AI 可視性モニタリング](#ai-可視性モニタリング)
  - [コンテンツ監査と最適化](#コンテンツ監査と最適化)
  - [オープンソースのツールとライブラリ](#オープンソースのツールとライブラリ)
  - [llms.txt ジェネレーター](#llmstxt-ジェネレーター)
  - [クローラーのログ解析](#クローラーのログ解析)
- [AI 検索エンジンとアシスタント](#ai-検索エンジンとアシスタント)
  - [グローバル](#グローバル)
  - [中国](#中国)
  - [日本](#日本)
  - [韓国](#韓国)
  - [ヨーロッパ](#ヨーロッパ)
  - [その他の地域](#その他の地域)
- [言語別の GEO リソース](#言語別の-geo-リソース)
  - [中国語](#中国語)
  - [日本語](#日本語)
  - [韓国語](#韓国語)
  - [スペイン語](#スペイン語)
  - [ドイツ語](#ドイツ語)
- [事例](#事例)
- [講座・動画・ポッドキャスト](#講座動画ポッドキャスト)
- [ニュースレターとコミュニティ](#ニュースレターとコミュニティ)
- [ほかの厳選リスト](#ほかの厳選リスト)
- [ライセンス](#ライセンス)

**凡例：** 🆓 無料、🪙 フリーミアム、💲 有料、🔓 オープンソース

## GEO とは

生成エンジン最適化（GEO）とは、ChatGPT、Perplexity、Google の AI Overviews などの AI 回答エンジンがコンテンツを見つけ、理解し、引用しやすくするための取り組みです。SEO が検索結果のリンク一覧での順位を競うのに対し、GEO は AI が生成する回答そのものの中でコンテンツが引用・言及されることを目指すため、成果はクリック数ではなく引用や可視性で測ります。この概念は、プリンストン大学などの Aggarwal らが KDD 2024 で発表した論文「GEO: Generative Engine Optimization」で提唱されました。

## 入門

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - GEO を AI 回答で引用や言及を獲得する取り組みと定義し、それが SEO の基本の上に成り立つことを解説した Search Engine Land の記事です。
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - GEO を定義し、用語の起源を 2023年の研究論文にたどり、AEO や LLMO などの関連する呼び名と批判も紹介した百科事典の項目です。
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - AEO と GEO も SEO の一部とし、llms.txt やチャンク分割を否定した Google の 2026年5月のガイダンスを伝える Search Engine Journal の記事です。
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - AI 機能向けの最適化も SEO にほかならないとし、llms.txt やチャンク分割などの施策は不要だと明記した Google 自身のガイダンスです。
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - SEO と GEO の目標、測定方法、共通する実践を比較した Search Engine Land の記事です。
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - GEO という用語の起源を Aggarwal らの KDD 2024 論文にたどり、業界の定義を比較し、AI 可視性について分かっていることをまとめた解説記事です。

## 研究論文

### 基礎となる論文

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - コンテンツごとに 9種類の GEO 戦略を評価し、バンディット手法で最適な戦略の選択を高速化するエージェント型システムを示した論文です。 (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - 静的なヒューリスティクスや単一プロンプトによる書き換えを超えて、要約回答での可視性を高める自己進化型のエージェント型 GEO システムを提案した論文です。 (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - GEO を競合を考慮した戦略選択として定式化し、組合せ構造上のベイズ最適化で書き換え戦略を選ぶ手法を示した論文です。 (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - 個々の文書が生成エンジンに引用されない理由を診断し、一律の書き換えルールではなく対象を絞った修正を施す手法を示した論文です。 (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - GEO を戦略学習として扱い、計画・編集・評価のエージェントを使って、タスクやエンジンをまたいで再利用できる編集戦略を抽出する手法を示した論文です。 (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - 多数のクエリ間で対立する修正要求を、最適化の選好を抽出して 1つの修正に統合する発散・収束型のフレームワークで解決する手法を示した論文です。 (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - 生成エンジンがどのページを引用するかに影響を与えるため、コンテンツ構造を複数の階層で設計するフレームワーク GEO-SFE を提案した論文です。 (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - ページの構造・内容・言語に関する解釈可能な特徴を最適化し、引用での可視性とコンテンツの質のバランスを取る FeatGEO を提案した論文です。 (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - 旅行サイトのテキストから作った合成ペアで BART-base モデルをファインチューニングし、LLM の出力で見つかりやすくなるようコンテンツを書き換える手法を示した論文です。 (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - ユーザーの意図と役割を事前に推定することで、対象クエリやエンジンからのフィードバックなしに生成検索エンジン向けにコンテンツを最適化する手法を示した論文です。 (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - 生成エンジンが取得コンテンツのどんな特徴を好むかを学習し、それに合わせてウェブページを書き換えて可視性を高める AutoGEO を提案した論文です。 (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - 生成 AI に基づくホワイトハットの SEO 手法を示し、その実証的な効果を報告した論文です。 (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - 生成エンジン最適化（GEO）の概念と、生成エンジンの回答におけるコンテンツの可視性を測るベンチマークを提案した論文です。 (2023)

### ベンチマークとデータセット

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - 会話型 SEO の手法をタスク、ドメイン、採用者数の別に評価するベンチマークで、ほとんどの手法は効果がなく、従来の SEO のほうが有効な場合が多いことを示しています。 (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - 標的型の誤情報を含む GEO 最適化文書に対する防御策を、人手で検証したクエリと統制された条件で評価するベンチマークです。 (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - 実際の生成エンジンがページを取得・順位付けするライブのウェブ上でも、GEO による可視性向上が維持されるかを検証する LIVE-GEO を提案した論文です。 (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - EC 分野で GEO の書き換えヒューリスティクスを複数の生成エンジンで検証するための、取得済み商品リスト付きの消費者向け商品クエリ 1万3746件を提供するテストベッドです。 (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - 取得した根拠を引用する LLM の回答について、流暢さ、正確さ、引用の質を自動指標で評価するベンチマーク ALCE を提案した論文です。 (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - GEO の順位操作攻撃を、統一したデータセットと指標による単一のプロトコルで評価し、その強さと検出しやすさを比較したベンチマークです。 (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - 1万1500件のユーザークエリのデータセットを公開し、Google 検索、AI Overviews、Gemini が返す情報源と情報を比較した論文です。 (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - 生成だけでなく検索と順位付けも含めて、検索拡張型の GEO 戦略をエンドツーエンドで評価できる環境を提案した論文です。 (2026)

### 攻撃と操作

プロンプトインジェクションやランキング攻撃などによって AI 回答エンジンが操作される仕組みと、その防御策を扱う敵対的 GEO の研究です。

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - LLM が生成する商品推薦で、アイテムが表示される位置を制御する最適化手法 CORE を提案した論文です。 (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - AI 検索向けの llms.txt 型マニフェストに関する根拠を監査して自動取得がほとんど行われていないことを示し、そのセキュリティ上の影響も評価した論文です。 (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - GEO 攻撃がコンテンツの質を下げる引用合戦へとエスカレートしうることを示し、双方に利益のある結果に向けたメカニズムデザインを検討した論文です。 (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - 画像の摂動とテキストを組み合わせて作ることで、視覚言語モデルによる商品の順位付けを操作できることを示した論文です。 (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - GEO が影響力の集中、開示されない商業的影響、学術界と産業界の盲点というリスクを生むと論じ、開示や監査など回答レベルのガバナンスを求めるポジションペーパーです。 (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - 販売者が自社商品を上位に押し上げるためにコンテンツに埋め込む説得的な構造を検出し、LLM ベースのランキングを守る手法を示した論文です。 (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - 事実との整合性を保つことでファクトチェックやパープレキシティによるフィルターをすり抜ける悪意ある GEO の書き換えから、生成検索を守る手法を示した論文です。 (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - LLM 検索に対する順位操作攻撃を無限回繰り返しの囚人のジレンマとしてモデル化し、協調が維持される条件を分析した論文です。 (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - 生成エンジンがどのパブリッシャーを引用しているか、また攻撃者が回答の情報源に悪意あるコンテンツを注入するのがどれほど難しいかを分析した論文です。 (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - エネルギーベースの最適化で自然かつ検出されにくいプロンプトを作成し、LLM によるランキングを操作する攻撃を示した論文です。 (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - 複数の攻撃者が同じクエリを別々の標的へ誘導する RAG システムへの競合的なポイズニング攻撃を調べ、PoisonArena ベンチマークを提案した論文です。 (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - LLM の選択を攻撃者のコンテンツへ誘導する選好操作攻撃を提案し、それが販売者間に囚人のジレンマを生むことを示した論文です。 (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - 多くの RAG システムの検索層である密ベクトル埋め込み検索に取得されるよう敵対的な文章を作る、SEO 型の攻撃を調べた論文です。 (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - 細工した戦略的テキスト列を商品ページに加えると、LLM ベースの検索エンジンがその商品を最初に推薦するようになることを示した論文です。 (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - 実際の商品ページを用いて、ウェブページのテキストに仕込んだプロンプトインジェクションが会話型検索の結果で情報源の順位を押し上げることを示した論文です。 (2024)

### 引用と可視性の分析

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - 1100人を対象とした事前登録のフィールド実験で、AI Overviews と AI Mode を取り除くとパブリッシャーへのクリック率が上がることを示した論文です。 (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - 同程度に根拠となる 2つの情報源のうち、エージェント型検索エンジンがどちらを引用するかが文書の提示方法でどう変わるかを、因果的に監査した論文です。 (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - AI 検索の回答は実行ごと、プロンプトごと、時期ごとに変わるため、可視性は一度ではなく繰り返し測定する必要があることを示した論文です。 (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - 引用の選択と引用の吸収を区別し、ChatGPT、Google AI、Perplexity を対象に 602件のプロンプトを分析した論文です。 (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - 約 3万5000件のプロンプト観測を分析し、ブランド自身のドメインがライブ検索の結果に現れると、ブランドの言及率が急上昇することを示した論文です。 (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - ChatGPT、Claude、Perplexity、Gemini でブランドの可視性を測定する方法と、各エンジンがブランドを引用する際にどの情報源に頼っているかを調べた論文です。 (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - GEO の可視性スコアはプロンプトコーパスと重みづけに左右され、それらが定める「回答市場」は実際の需要と一致しない場合があると論じた論文です。 (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - 5万5393件のクエリを 40日間追跡し、AI Overviews の表示条件、情報源の質、主張の忠実性、パブリッシャーへの影響を測定した論文です。 (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - Google の検索結果と生成 AI の回答が、引用ドメイン、ドメインの種類、クエリの意図、情報の新しさの点でどう異なるかを定量化した論文です。 (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - ChatGPT、Copilot、Google、Perplexity を監査し、エンジン間の URL の重なりがごくわずかなため、エンジンに依存しない GEO スコアには限界があることを示した論文です。 (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - 4つの生成検索エンジンを 712件のクエリで監査し、引用元の約 16% が AI 生成とみられることを示した論文です。 (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - Google の AI Overviews と Reddit をもとに、AI 検索が引用されたコミュニティのエンゲージメントを高め、AI Mode の開始後にその効果が薄れたことを示した論文です。 (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - ChatGPT Web の 4つの設定がクエリをどう書き換え、ページを取得し、引用を選ぶかを観察し、取得頻度が引用を予測することを示した論文です。 (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - 614件のクエリを用いて、中国語の生成検索プラットフォーム 4つにおける引用の傾向、出典の示し方、エンティティの露出を分析した論文です。 (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - 15万8099件の回答を分析し、ChatGPT が書き換えたサブクエリで取得するページの方が、ページの特性よりもはるかによく引用を説明することを示した論文です。 (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - 16の柱からなるページ監査を提案し、3つのエンジンでメタデータ、セマンティック HTML、構造化データが引用と最も強く関係することを示した論文です。 (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - 業界や言語をまたぐ統制実験で AI 検索エンジンと Google を比較し、ブランド自身のコンテンツよりアーンドメディアを強く優先する傾向を示した論文です。 (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - ConflictingQA を構築し、LLM はクエリとページの関連性に大きく依存する一方、科学的な参考文献などの文体上の手がかりはほとんど無視することを示した論文です。 (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - Bing Chat、NeevaAI、Perplexity、YouChat の引用の再現率と適合率を監査し、多くの記述が引用で十分に裏付けられていないことを示した論文です。 (2023)

### サーベイ

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - 2023年から 2026年までの 45件の研究をレビューし、GEO を多段階の確率的パイプラインとして捉え、GEO に関する主張を評価するチェックリストを示したサーベイ論文です。 (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - LLM ベースの検索エージェントをアーキテクチャ、最適化、応用、評価の観点から体系的に分類し、未解決の課題を挙げたサーベイ論文です。 (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - 大規模言語モデルによる生成検索と生成推薦を、技術的な観点からまとめたサーベイ論文です。 (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - 検索エンジンと LLM が互いをどう高め合えるかを、LLM を改善する検索と検索を改善する LLM の両面から検討した論文です。 (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - クエリの書き換え、検索、リランキング、読解など、情報検索システム全体で大規模言語モデルがどう使われているかをまとめたサーベイ論文です。 (2023)

## ガイドと記事

### 戦略

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - 生成エンジン最適化（GEO）によってコンテンツを AI 検索の結果に表示させる方法を、実践的に紹介した入門ガイドです。 (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - GEO の概要、SEO との違い、AI 回答で引用されやすくする手法を解説したガイドで、ダウンロードできる監査チェックリストも付いています。 (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - AI 検索と従来の検索の違い、5つの GEO 施策、GEO の成果の測り方を解説し、AI 検索が今も従来の検索に依存している点にも触れたガイドです。 (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - 検索がリンクに基づく順位付けから言語モデルによる回答へ移りつつあると論じ、GEO を約 800億ドル規模の SEO 市場の次の段階と位置づけた記事です。 (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - Structure、Evidence、Entity、Notability の 4層の GEO フレームワーク SEEN と、0/1 で採点して最も弱い層を示す 41項目のチェックリストの紹介です。 (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - 優先トピックとベースラインの設定から、引用元の読み解き、コンテンツの改善、成果の報告まで、10ステップの GEO プロセスを解説したガイドです。 (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - 全 8回の AEO ガイドの初回で、SEO との違い、回答エンジンの仕組み、AI 可視性の追跡、プロンプトの選び方、AI 回答の誤りの修正を扱います。 (2025)

### コンテンツ制作

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - Google の AI Overviews とは何か、ウェブ上の情報源からどう生成されるか、サイト所有者が最適化し可視性を追跡する方法を解説したガイドです。 (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - ChatGPT に引用されるまでを「取得される」「引用に適する」の 2段階で説明し、引用ドメインの AI クローラー許可状況など、各段階を自社の計測で裏付けた記事です。 (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - ChatGPT で購買者の質問 13件を試した結果とサイトのサーバーログから分かったことを、否定的な結果も含めて報告し、許可すべき AI ボットを示した記事です。 (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - キーワード調査から書式設定まで、ChatGPT や Google などの AI 検索エンジンにコンテンツを引用されるための 7つのステップを解説したガイドです。 (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - AI システムがコンテンツを抽出しやすくし、サイト外でコンセンサスを築くことで、ChatGPT の検索で上位に表示されるための 8つのステップを示したガイドです。 (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - LLM が生成する回答でブランドの可視性を高める 10の方法を、LLMO（LLM 最適化）の観点から紹介した記事です。 (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - スキーマ、明確な見出し、完結した Q&A ブロックなど AI 検索の回答に使われやすい条件と、回答をタブや PDF に隠す誤りを解説した Microsoft Advertising のガイドです。 (2025)

### 技術的な実装

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - Google タグマネージャーなどでクライアントサイドに挿入した JSON-LD は、JavaScript を実行できない AI クローラーに読み取られないという調査結果を伝える記事です。 (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - ChatGPT や Gemini などからの AI 経由の参照トラフィックを Google Analytics 4 で追跡する方法を示したガイドです。 (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - AI エージェントにページを Markdown で配信する機能を紹介し、ある記事のトークン数が HTML の 1万6180 から Markdown では 3150 に減った例で削減効果を示しています。 (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - ChatGPT、Claude などの AI クローラーによる JavaScript やコンテンツ種別の扱いを MERJ と Vercel のデータで示し、サイト所有者への推奨をまとめた記事です。 (2024)

### 業界レポートとデータ

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - 3000サイトを調査して AI チャットボットが送るトラフィック量を推計し、63% のサイトが流入を受け、その 98% を 3つのチャットボットが占めることを示した調査です。 (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - Cloudflare Radar に業界別のデータと、クロール目的別の AI ボットトラフィックの内訳を追加したことを紹介する記事です。 (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - 3100万件の AI 引用と 105のパブリッシャーの robots.txt を分析し、AI クローラーのブロックが一部のモデルには効く一方、ほかのモデルには効果がないことを示した調査です。 (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - 16か月分のデータを追跡し、AI Overviews の引用とオーガニック順位の重なりが 32% から 54% に拡大したことを、業界別の内訳とあわせて示した調査です。 (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - AI Overviews によってクリック数が 34.5% 減ることを示した Ahrefs の調査で、クリックが増えるとする Google の主張に反する結果です。 (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - 8つの AI 検索ツールをニュース記事の抜粋で検証し、60% を超えるクエリで引用元を誤って示したことを報告した記事です。 (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - ChatGPT、Gemini、Claude の市場シェア、参照トラフィック、引用、AI 回答内の広告について、2026年の Similarweb のデータをまとめた記事です。 (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - 7万5000のブランドを分析し、AI Overviews でのブランド言及に影響しやすい検索要因を特定した調査です。 (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - 2025年3月の Google ユーザーの行動を比較し、AI の要約を見た人はほかのサイトへのリンクをクリックする割合が低いことを示した調査です。 (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - ChatGPT、Gemini、Copilot、Google での 3万7500件の引用を追跡し、半数が翌日に消え、その大半が再び現れることを示した調査です。 (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - 30万のドメインを調べ、llms.txt がどの程度使われているか、また LLM に引用される頻度に影響するかを検証した調査です。 (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - 2024年11月から 2026年3月までの約 70億件のログファイルを分析し、OpenAI の 3つのクローラーがウェブとどう関わっているかを示した調査です。 (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - 生成 AI がニュース業界を変えるなかで、ChatGPT のニュース関連クエリが 212% 急増し、パブリッシャーのトラフィックが 26% 減少したことを報告したレポートです。 (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - 1000万以上のキーワードを分析し、Google の AI Overviews が検索をどう変えつつあり、それが SEO にとって何を意味するかを示した調査です。 (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - 86万3000件の SERP から、AI Overviews の引用の 38% が上位 10件のページによるもので、1年前の 76% から低下したことを示した調査です。 (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - JSON-LD を追加した 1885ページを追跡し、Google の AI Overviews、AI Mode、ChatGPT での引用への影響を測定した調査です。 (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - 140万件のプロンプトを分析し、ページタイトル、URL、スニペットが、ChatGPT が取得したページのうちどれを引用するかに与える影響を示した調査です。 (2026)

## 標準と技術仕様

AI クローラーによるサイトへのアクセスや、AI 回答エンジンによるコンテンツの読み取りを左右する仕様と公式ドキュメントです。

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - llms.txt 提案のソースを、リファレンス実装のツールや議論とあわせて公開しているリポジトリです。
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - John Mueller が llms.txt を現時点では憶測の段階だとし、Google が支援する代替案 WebMCP のほうが好ましいと述べたことを伝える記事です。
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - サーバーログを見る限り、現在 llms.txt を使っている AI システムはないという John Mueller の発言を伝える記事です。 (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - llms.txt を導入しているウェブサイトのディレクトリで、API、プラットフォーム、開発者ツールのサンプルファイルを掲載しています。
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - 2026年9月の調査で、上位 1000ドメインと上位 1万ドメインにおける llms.txt の導入率を測定したレポートで、手法とダウンロード可能なデータも公開しています。 (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - llms.txt ファイルを公開しているウェブサイトの一覧で、開発者がこの形式の実例を閲覧できます。
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - llms.txt を公開しているサイトを一覧にし、学習、検索、要約について各サイトが宣言している AI への許可を示すディレクトリです。
- [The /llms.txt file](https://llmstxt.org) 🆓 - サイトのルートに Markdown 形式の /llms.txt ファイルを置き、言語モデルにサイトの厳選した概要と特に有用なコンテンツへのリンクを示すことを提案した仕様です。 (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - Vercel、Google、Anthropic の例を挙げて llms.txt の価値を主張し、一般的な SEO の実践で十分だとする批判に反論した記事です。 (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - llms.txt ファイルとは何かを説明し、導入が開発者やマーケターにとって効果があるのかを検証した記事です。

### AI クローラーと robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - 12の事業者の AI クローラー 25種のユーザーエージェントを 4グループに分けて紹介し、157のプラットフォームのうち robots.txt で各クローラーを拒否する数を示した記事です。 (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - サイト所有者が AI の学習をオプトアウトするために使える robots.txt のエントリ、meta タグなどの既知の設定を集めたリポジトリです。
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - ブロック対象とする AI エージェントとクローラーのコミュニティリストを管理し、そこから生成した robots.txt やサーバー設定ファイルを提供しています。
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - Amazonbot、Amzn-SearchBot、Amzn-User と、それぞれを個別に制御する robots.txt の設定を説明したドキュメントです。
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - サイト所有者が AI クローラーにアクセス料金を課し、未払いのリクエストには HTTP 402 を返せる Pay Per Crawl の仕組みを解説した記事で、機能はクローズドベータです。
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - Google Read Aloud など、ユーザーのリクエストに応じて動作する Google のフェッチャーを一覧にし、通常は robots.txt のルールを無視することを記載したドキュメントです。
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - Googlebot を含む Google の一般的なクローラーについて、ユーザーエージェント文字列と robots.txt のトークンを記載したドキュメントです。
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - Yandex のロボット約 40種類のユーザーエージェントを用途と robots.txt での扱いとともに一覧にし、逆引き DNS で確認する方法を説明したドキュメントです。
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - robots.txt や HTTP ヘッダーなど、AI によるコンテンツの収集・利用についての意向を表明するための共通語彙と付与方法を標準化する作業部会です。
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - IP アドレスの許可リストやユーザーエージェント文字列に代わり、AI クローラーやエージェントなどの自動クライアントを暗号技術で認証する方法を標準化する作業部会です。
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - DuckAssistBot が DuckDuckGo の AI 支援回答のための情報源を集めるクローラーで、AI の学習には使われず、robots.txt でブロックできることを説明したページです。
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - Meta AI の検索向けの Meta-WebIndexer や AI モデル学習向けの Meta-ExternalAgent など、Meta のクローラーと各用途を一覧にしたドキュメントです。
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - MistralAI-User、MistralAI-Index、MistralAI-Training の各ユーザーエージェントとそれぞれの用途を説明したドキュメントです。
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - AI クローラーも従うことが期待される Robots Exclusion Protocol、すなわち robots.txt の構文と意味を定めた仕様です。 (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - IETF の AIPREF ドラフトに基づく robots.txt の共通の AI 学習オプトアウトを Google が尊重する予定だと発表した記事で、2027年の対応を目指しています。 (2026)

### 構造化データ

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - Google が構造化データマークアップでコンテンツを理解する仕組み、対応する形式、マークアップの配置場所を説明したドキュメントです。
- [JSON-LD](https://json-ld.org) 🆓 - Schema.org のマークアップでよく使われる、JSON ベースのリンクトデータ形式 JSON-LD の仕様を公開しているサイトです。
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - URL やコードスニペットを検証し、その構造化データからどの Google リッチリザルトを生成できるかを報告するツールです。
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - AI にすでに引用されているページにスキーママークアップを追加すると引用率が上がるかを検証した、Ahrefs のレポートを要約した記事です。 (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - JSON-LD、Microdata、RDFa で書かれたあらゆる Schema.org タイプの構造化データを検証するツールです。
- [Schema.org](https://schema.org) 🆓 - 検索エンジンなどのサービスに向けてウェブページをマークアップするための、タイプとプロパティの共通語彙を公開しているサイトです。
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - Schema.org の語彙のソースと関連ソフトウェアを公開しているリポジトリです。
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - Google 検索の機能を支える構造化データの種類を、例と実装ガイダンスとともにまとめたドキュメントです。

### 各エンジンの公式ドキュメント

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - Spotlight、Siri、Safari の検索機能を支える Applebot と、拒否すると生成 AI の学習から除外される Applebot-Extended を説明したドキュメントです。
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - Google 検索の AI Overviews と AI Mode の仕組みと、サイト所有者が自分のコンテンツをそこに含めるための考え方を説明したドキュメントです。
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - Baidu のウェブマスター向けプラットフォームで、サイトリソースの送信、クロールと robots のデータ、検索ウィジェット、AI トラフィック分析を提供しています。
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - Common Crawl のオープンなウェブアーカイブを支えるクローラー CCBot について、ユーザーエージェントと検証・ブロックの方法を説明したドキュメントです。
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - ClaudeBot、Claude-User、Claude-SearchBot の各クローラーと、サイト所有者が robots.txt でそれぞれをブロックする方法を説明したドキュメントです。
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - 参加する検索エンジンに URL の追加・更新・削除を通知する IndexNow プロトコルのドキュメントです。
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - Microsoft Copilot や Bing の AI 生成の要約でサイトが引用されたタイミングを示す、Bing Webmaster Tools の新しいレポートを発表した記事です。 (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - AI Overviews や AI Mode などの生成 AI 機能にページが表示される頻度を、ページ・国・デバイス・日付別に示す Search Console のレポートを発表した記事です。 (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - Perplexity が参加パブリッシャーと収益を分配し、API アクセスや開発者支援も提供するプログラムを発表した記事です。 (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - Naver 検索にサイトを発見・インデックスしてもらうための要件を扱う Naver のウェブマスター向けガイドとツールで、AI Briefing も同じインデックスのウェブ文書を利用します。
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - OAI-SearchBot、GPTBot、ChatGPT-User、OAI-AdsBot の各ユーザーエージェントとそれぞれの用途を説明したドキュメントです。
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - Perplexity の検索結果にサイトを表示する PerplexityBot と、ユーザーの依頼でページを取得し通常は robots.txt を無視する Perplexity-User の説明です。
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - ChatGPT の検索での表示、OAI-SearchBot クローラー、ChatGPT からの参照トラフィックについて、パブリッシャーと開発者の質問に答える FAQ です。
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - AI Overviews、AI Mode、Discover の生成 AI への掲載可否を選べる Search Console の設定を説明し、AI の学習には影響しないことにも触れたドキュメントです。
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Yandex の AI 回答が質問を分割し、情報源を選んで分析し、回答内でリンクする仕組みを説明したヘルプページです。
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Google 検索の AI 機能でコンテンツが成果を上げるための、Google 推奨の方法を紹介した記事です。 (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Yandex 検索でのサイトの所有確認、インデックス状況のモニタリング、クロールの問題の診断ができる Yandex のウェブマスター向けサービスです。
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - AI 学習とグラウンディングへの利用可否を個別指定する仕組みの発表で、robots.txt、meta タグ、X-Robots-Tag で設定し、2027年2月から Microsoft が参照します。 (2026)

## ツール

### AI 可視性モニタリング

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - ChatGPT、Gemini、Perplexity、Copilot、AI Overviews がブランドをどう言及・引用しているかを、登録不要で確認できるツールです。
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - Google AI Overviews、AI Mode、ChatGPT、Perplexity、Gemini、Copilot でのブランド登場頻度を、プロンプトデータベースか独自プロンプトで計測します。
- [AthenaHQ](https://athenahq.ai) 🪙 - ChatGPT、Perplexity、Gemini、AI Overviews、Copilot などでブランドの可視性を追跡し、改善案を示すツールで、初期クレジット付きの無料プランがあります。
- [Geoptie](https://geoptie.com) 💲 - ChatGPT、Gemini、Claude、Perplexity、Google AI が購買者のプロンプトにどう答え、どの情報源を引用するかを確認できるツールです。
- [Goodie](https://higoodie.com) 💲 - ChatGPT、AI Overviews、Perplexity、Copilot などの AI エンジンでブランドの可視性を追跡し、最適化策を提案するツールで、上位プランでは対象エンジンが増えます。
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - ChatGPT、Perplexity、Gemini がブランドをどう説明しているかを 1回限りの無料チェックで採点するツールで、毎週のモニタリングは有料の HubSpot AEO で提供されています。
- [Knowatoa](https://www.knowatoa.com) 💲 - ChatGPT、Google AI Overviews、AI Mode などの AI 検索サービスでブランドの可視性を追跡するツールで、プロンプト追跡とレポート連携の機能を備えています。
- [Otterly.AI](https://otterly.ai) 💲 - ChatGPT、Google AI Overviews、AI Mode、Gemini、Perplexity、Copilot のブランド言及・引用をモニタリングし、競合比較やプロンプト調査も可能です。
- [Peec AI](https://peec.ai) 💲 - ChatGPT、Perplexity、AI Overviews、AI Mode、Gemini などでブランドの可視性、順位、センチメントを追跡し、プロンプト単位でレポートするツールです。
- [Profound](https://www.tryprofound.com) 💲 - ChatGPT、Perplexity、Google AI Mode、Gemini、Claude などの回答エンジンでのブランドの可視性を、毎日のプロンプト実行と引用分析で追跡するツールです。
- [Promptwatch](https://promptwatch.com) 💲 - ChatGPT、Google AI Overviews、Perplexity、Claude、Gemini などでプロンプトを実行してブランド可視性を追跡し、上位プランは AI クローラー分析付きです。
- [Rankscale](https://rankscale.ai) 💲 - 17以上の AI 検索エンジンでブランドの言及と引用を追跡するクレジット制のツールで、上位プランではブランドダッシュボードと API を利用できます。
- [Scrunch](https://scrunch.com) 💲 - 主要な AI プラットフォームでプロンプト、引用、競合の順位、AI ボットのクロール状況をモニタリングし、サイトの AI 向け最適化版も配信できるツールです。
- [Searchable](https://www.searchable.com) 💲 - ChatGPT、Google AI Overviews、Perplexity でブランド言及・競合比較・引用元を追跡するツールで、Claude や Gemini などは有料アドオンです。
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - ChatGPT や Google AI Mode などでのブランド言及と可視性をプロンプト追跡と競合モニタリングで追うツールで、Semrush の SEO・AI Search プランに含まれます。
- [Trakkr](https://trakkr.ai) 💲 - プロンプト追跡によって 8つの AI モデルでのブランドの見え方を追跡するツールで、上位プランでは複数ブランドの管理とクライアントポータルを利用できます。
- [Waikay](https://waikay.io) 🪙 - ChatGPT、Google、Claude、Perplexity がブランドをどう説明しているかを分析し、ハルシネーションや知識の欠落を指摘して対応策を提案するツールです。
- [Writesonic](https://writesonic.com) 💲 - AI 回答でのブランドの可視性をモニタリングするツールで、下位プランでは ChatGPT、Gemini、Google AI Overviews に対応し、記事作成やサイト監査の修正機能も備えています。
- [ZipTie](https://ziptie.ai) 💲 - ChatGPT、Google AI Overviews、AI Mode、Gemini、Perplexity、Copilot など 7エンジンで指定プロンプトを追跡し、チェックごとの従量課金です。

### コンテンツ監査と最適化

- [Clearscope](https://www.clearscope.io) 💲 - Google や AI 回答向けにコンテンツの改善点を提案し、ChatGPT と Gemini でクエリを追跡してブランドが言及されたかを示すツールです。
- [Frase](https://www.frase.io) 💲 - SEO と GEO の観点からコンテンツを採点し、ChatGPT や Google AI などの AI エンジンでのブランドの可視性をモニタリングするツールで、上位プランでは対象エンジンが増えます。
- [GeoReady](https://geoready.dev) 🪙 - ChatGPT、Perplexity、Claude、Gemini がサイトにアクセスし、読み取り、引用できるかを監査し、9カテゴリ・100点満点で採点して優先順位付きの修正案を示すツールです。
- [NEURONwriter](https://neuronwriter.com) 💲 - 上位ページをもとに用語と構成を提案して Google と AI 回答向けにコンテンツを最適化し、AI モデル全体でのブランドのシェア・オブ・ボイスもモニタリングするツールです。
- [Surfer](https://surfer.ai) 💲 - 競合比較で下書きを採点するエディターと、ChatGPT、Perplexity、Gemini、AI Overviews、AI Mode でのブランド言及を追う AI Tracker を備えたツールです。

### オープンソースのツールとライブラリ

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - AEO と GEO の業務向けのエージェントファーストな運用プラットフォームで、npm パッケージとして配布されています。
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - ChatGPT、Claude、Perplexity、Gemini、Copilot、Grok、Google AI Overviews でのブランドの言及・引用を追跡する、セルフホスト型のツールです。
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - 複数の LLM プロバイダーでプロンプトを定期実行し、ウェブ検索の引用を取得して、ダッシュボードと CLI でブランド言及を追跡するツールです。
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - AI エンジンがサイトをクロール・理解・引用できるかを 0〜100 で採点するツールで、CLI、Python ライブラリ、MCP サーバーとして利用できます。
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - ChatGPT、Perplexity、Gemini、Google AI Mode でのブランドの言及・引用を追跡するセルフホスト型ダッシュボードで、MCP サーバーと CLI も備えています。
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - ウェブサイトに AI クローラーがアクセスして読み取れるかを確認し、スコア化するツールで、PyPI パッケージと GitHub Action として提供されています。
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - 組み込みの戦略を備え、独自の戦略も登録できる、プラグイン式の Go 製 GEO フレームワークです。
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - CI やプリコミットで実行し、ドキュメントや静的サイトの構造・出典の問題を検出する決定論的なコンテンツリンターで、npm パッケージとして公開されています。
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - AI 回答におけるブランドの存在感を追跡・改善するためのオープンソースのプラットフォームです。
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - 主要な AI エンジンがブランドをどう言及・引用しているかを記録するセルフホスト型の可視性トラッカーで、SQLite と MCP サーバーを備えた単一の Go バイナリです。
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - HTTP のコンテンツネゴシエーションを通じて、AI エージェントにページの Markdown 版を配信する NGINX モジュールです。
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - ChatGPT、Perplexity、Gemini、Claude、Google AI Overviews が製品画面でブランドをどう言及・引用するかをモニタリングするセルフホスト型トラッカーです。
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - エージェントにとっての読みやすさでサイトを 0〜100 で採点し、ページの Markdown 版と robots.txt、llms.txt、sitemap.xml を生成するツールです。
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - React 向けに、型チェック付きで Schema.org の JSON-LD を記述できるライブラリです。
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - Schema.org の JSON-LD を記述するための TypeScript の型定義です。
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - JavaScript サイト向けに Schema.org の JSON-LD グラフを構築するライブラリで、Astro との統合も備えています。
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - Schema.org のタイプをメソッドチェーンで組み立て、JSON-LD を出力する PHP のビルダーです。

### llms.txt ジェネレーター

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - Vite、Astro、Next.js、Nuxt のサイト向けに、llms.txt、JSON-LD、Markdown ミラー、AI クローラー制御をビルド時に生成し、検証するツールです。
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - ウェブサイトをクロールしてコンテンツを抽出し、llms.txt ファイルを作成する Apify の Actor です。
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - サイトをクロールして llms.txt ファイルの下書きを作成するツールで、ページの検出、事業情報の追加、公開ファイルの毎日の更新に対応しています。
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - sitemap.xml を llms.txt ファイルに変換するコマンドラインツールです。
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - ドキュメントサイト用の /llms.txt ファイルを生成する MkDocs プラグインです。
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - アプリケーションの /llms.txt 形式の Markdown ドキュメントを自動生成する Nuxt モジュールです。
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - llms.txt ファイルを生成する Sphinx 拡張機能です。
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - LLM が扱いやすいドキュメントファイルを生成する VitePress プラグインです。
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - 公開されたホームページから、サイトマップと内部リンクで見つかる最大 30ページを確認して llms.txt の下書きを作成するツールで、登録は不要です。
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - 無料の Yoast SEO プラグイン内で llms.txt ファイルを自動生成・更新する機能で、主要コンテンツは自動でも手動でも選べます。

### クローラーのログ解析

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - AI クローラーのユーザーエージェントを集めたリストで、robots.txt の監査、到達性のテスト、アクセスログの読み取りを行う Node CLI と GitHub Action も備えています。
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - どの AI サービスがサイトをクロールしているかを表示し、クローラーごとの許可・ブロックや robots.txt の遵守状況の報告ができるツールで、Cloudflare の全プランで利用できます。
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - エッジで AI クローラーや LLM ボットのトラフィックを検出・追跡する Cloudflare Worker です。
- [Known Agents](https://knownagents.com) 🪙 - AI エージェントとボットのディレクトリ、robots.txt チェッカー、エージェント分析を提供するサービスで、無料プランは月 10万イベントまでです。

## AI 検索エンジンとアシスタント

地域別にまとめた AI 回答エンジンで、可能な限り公式サイト、ウェブマスター向けドキュメント、既知のクローラーのユーザーエージェントを併記しています。

### グローバル

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Microsoft Bing の対話型検索モードで、旧 Copilot Search が 2026年に AI Mode と、通常の結果に出る AI Overview の要約に分かれたものです。
- [Brave Search](https://brave.com/search/) 🪙 - 独自のインデックスを持つ Brave の検索エンジンで、引用元を示す Answer with AI の要約と、追加の質問ができるチャットモード Ask Brave を備えています。
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - OpenAI の ChatGPT にウェブ検索を組み込んだもので、会話の中で質問に答え、参照したページへのリンクを示します。
- [Claude](https://claude.ai) 🪙 - Anthropic のアシスタント Claude で、会話中にウェブを検索し、回答の根拠となったページを引用できます。
- [Duck.ai](https://duck.ai) 🪙 - DuckDuckGo が提供する、サードパーティの AI モデルと匿名で対話できるチャットで、検索結果から利用でき、DuckDuckGo の検索では任意で AI による回答も表示できます。
- [Gemini](https://gemini.google.com) 🪙 - Google の AI アシスタント Gemini で、Google 検索から最新の情報を取り入れて回答します。
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Gemini を基盤とする Google 検索の対話型モードで、複雑な質問に答え、追加の質問にも対応し、ウェブ上の情報源へのリンクを示します。
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Google 検索で通常の結果の上に表示される生成 AI の要約で、参照した情報源へのリンクを示し、120以上の国と地域で提供されています。
- [Grok](https://grok.com) 🪙 - 現在は SpaceX 傘下の xAI が提供する AI アシスタントで、ウェブと X の投稿を検索して時事的な質問に答えます。
- [Kagi Assistant](https://kagi.com/assistant) 💲 - 有料会員向けの Kagi のチャットアシスタントで、多数のプロバイダーのモデルと、任意で利用できる Kagi の広告なし検索結果を組み合わせています。
- [Meta AI](https://www.meta.ai) 🪙 - ウェブ版と WhatsApp、Instagram、Facebook 内で使える Meta の AI アシスタントで、時事的な質問にはウェブ検索の結果を取り込めます。
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Microsoft の一般消費者向けアシスタント Copilot で、Bing のウェブ検索結果を使って質問に答え、参照したページを引用します。
- [Perplexity](https://www.perplexity.ai) 🪙 - リアルタイムにウェブを検索し、番号付きの引用元を添えた対話形式の回答を返す AI 回答エンジンです。

### 中国

- [ChatGLM](https://chatglm.cn) 🆓 - Zhipu AI が GLM モデルを基盤に提供する中国の AI アシスタントで、ウェブ検索やエージェント機能を備えています。
- [DeepSeek](https://www.deepseek.com) 🆓 - DeepSeek のオープンウェイトモデルを基盤とするチャットアシスタントで、最新の情報で回答するためのウェブ検索モードを任意で利用できます。
- [Doubao](https://www.doubao.com) 🆓 - ByteDance の汎用 AI アシスタントで、チャットでの質問にウェブを検索して答え、参照した情報源を一覧で示します。
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - Baidu のアシスタント ERNIE Bot（旧称 Wenxin Yiyan）で、現在はウェブ上で Baidu Wenxin Assistant として提供され、Baidu 検索と連携しています。
- [Kimi](https://www.kimi.com) 🪙 - 長文の読解で知られる Moonshot AI のアシスタント Kimi で、ウェブを検索し、読んだページを引用します。
- [Metaso](https://metaso.cn) 🪙 - MetaSOTA が提供する広告なしの中国の AI 検索エンジンで、引用元を示して質問に答え、学術文献も検索できます。
- [Quark](https://www.quark.cn) 🪙 - Alibaba の検索・ブラウザアプリ Quark で、生成した結果で質問に答える AI アシスタントを中心に再構築されています。
- [Qwen](https://www.qianwen.com) 🆓 - Alibaba の Qwen モデルを基盤とし、ウェブ検索を備えた AI アシスタントアプリ Qwen（旧 Tongyi）で、海外向けのウェブ版は Qwen Chat です。
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - Tencent の AI アシスタントで、WeChat 公式アカウントの記事を含むウェブ検索結果をもとに回答します。
- [Yuanbao Search](https://so.qq.com) 🆓 - Tencent の AI ウェブ検索サイトで、引用元を示し、WeChat 公式アカウントや Channels のコンテンツも検索でき、追加質問向けの AI モードを備えています。

### 日本

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - Yahoo! JAPAN 検索の AI アシスタントと LINE AI を統合し、2026年4月に始まった LINEヤフーの AI エージェントで、ヤフーの検索窓や LINE から使えます。
- [Felo](https://felo.ai) 🪙 - 東京のスタートアップが開発した多言語 AI 検索エンジンで、引用付きで回答し、言語をまたいで情報源を検索できます。

### 韓国

- [A. (A-dot)](https://adot.ai) 🆓 - SK Telecom の AI パーソナルアシスタントで、複数のチャットモデルに加え、Perplexity と共同開発した AI 検索機能を備えています。
- [Kanana](https://kanana.ai) 🆓 - Kakao の AI ブランドで、Kanana in KakaoTalk、オープンソースモデル、2026年10月発表の KakaoTalk 上のエージェント Kanana Space を含みます。
- [Liner](https://liner.com) 🪙 - ソウルの企業が開発した AI 検索・リサーチアシスタントで、引用付きの回答と学術的な情報源に重点を置いています。
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - HyperCLOVA X を基盤とする Naver 検索の生成回答で、ページ上部に検索結果を要約し、使用した情報源のコンテンツを表示します。
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - Naver の対話型 AI 検索タブで、2026年6月に全ユーザーへ開放され、商品・場所・予約のカードを交えて対話形式で回答します。
- [Wrtn](https://wrtn.ai) 🆓 - Wrtn Technologies の韓国発 AI アシスタントで、リアルタイムのウェブ検索結果から回答して情報源を示す無料の AI 検索機能を備えています。

### ヨーロッパ

- [Ecosia AI search](https://www.ecosia.org) 🆓 - 植林を支援するベルリン発の検索エンジン Ecosia の AI 検索機能で、オフにして AI を使わない検索結果を得ることもできます。
- [Lumo](https://lumo.proton.me) 🪙 - スイスを拠点とする Proton のプライバシー重視の AI アシスタントで、ウェブ検索を内蔵し、クエリを広告ターゲティングに使わない方針です。
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - Le Chat から Vibe に名称を変更した Mistral AI のアシスタントで、チャットアシスタントにウェブ検索とコーディングエージェントを組み合わせています。

### その他の地域

- [Alice AI](https://alice.yandex.ru) 🆓 - Yandex の AI アシスタント Alice AI で、そのモデルは Yandex 検索で情報源へのリンク付きの AI 回答の生成にも使われています。

## 言語別の GEO リソース

英語以外の言語で公開されている記事、コミュニティ、ローカルツールで、代理店やサービス事業者は掲載していません。

### 中国語

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - 知的財産、アルゴリズムのバイアス、説明可能性、誤情報など GEO の倫理的リスクを論じ、5つの対応策を提案した中国語のプレプリントです。 (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - 信頼できる GEO を扱った 2026年5月の AIIA セミナーに関する新華社の記事で、CAICT の GEO サービス評価、GEO のリスク報告、業界の自主規制を取り上げています。 (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - GEO サービス事業者、信頼できる情報源、禁止される手法、成果報告についての要件を定めた中国広告協会の団体標準です。 (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - 2026年に中国で起きた GEO ブームを取り上げ、GEO が AI 回答の情報検索段階を狙う仕組みと、コンテンツの大量投下で架空の製品が AI の推薦に入り込んだ経緯を解説した特集記事です。 (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - ブラックハット GEO による AI データポイズニングを規制とプラットフォームの対策から論じた長文の分析記事で、湖南日報自身の信頼できる GEO サービスも取り上げています。 (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - AI の回答操作を対象とした Google の 2026年のスパムポリシー更新を分析し、GEO と有料のコンテンツ投下を区別したうえで、両者のグレーゾーンを論じた記事です。 (2026)

### 日本語

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - サイトを AI Overviews と AI Mode から 28日間オプトアウトした実験の報告で、両機能のクリック率がサイト平均の 2倍を超えると推定しています。 (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - 日本語の情報系キーワードを対象にした Ahrefs の調査で、2026年6月までに AI Overviews が検索 1位のクリック率を 62.7% 押し下げたと推計しています。 (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - AI 検索最適化に関する日経クロストレンドの連載の初回で、日本で AI Overviews がクリック数を減らしていることを示す Ahrefs のデータを引用し、本文の大部分は有料会員向けです。 (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - 日本語版 AI Mode の提供開始を告げる Google Japan の発表で、質問をサブトピックに分けてそれぞれを検索するクエリファンアウト技術を説明しています。 (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - GEO や LLMO は従来の SEO の上に成り立つと論じた鈴木謙一氏の講演レポートで、Google の AI 検索が回答を組み立てる仕組みの概念モデルも紹介しています。 (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - 日本で GEO を指す言葉として広く使われる LLMO と、SEO との違いを解説した日経クロステックの記事で、全文を読むには無料登録が必要です。 (2026)

### 韓国語

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - AI ブラウザとゼロクリック回答がニュースの流通構造とパブリッシャーの収益モデルをどう変えるかを論じた、韓国言論振興財団のレポートです。 (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - 英国 CMA が 2026年に Google に課した AI のオプトアウト、AI 検索データ、出典表示などの要件と、その韓国への示唆をまとめた韓国言論振興財団のレポートです。 (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - 韓国広告団体連合会の機関誌に掲載されたトレンドレビューで、GEO の概要、Perplexity や Gemini などのエンジンによる検索データの活用、E-E-A-T の役割を紹介しています。 (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - 韓国の決済会社による EC サイト向けの GEO ガイドで、Q&A コンテンツ、利用シーン別の商品説明、FAQ、外部での言及など 5つの施策を紹介しています。 (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - AI Briefing がクリエイターの投稿を情報源として表示する仕組みと、その引用に応じて毎月約 3000人に報酬を支払う Naver Mate を紹介した Naver のプレスリリースです。 (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - a16z の GEO に関するエッセイを韓国語で要約した GeekNews の投稿で、GEO と AEO という用語の重なりをめぐる短い読者の議論も含みます。 (2025)

### スペイン語

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - 一般的な旅行クエリ 1件を 3つの時点で複数の AI システムに入力し、ホテルブランドの可視性と引用元が大きく変動することを示した探索的研究です。 (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - GEO の文献をレビューし、可視性・影響力・検証可能性の指標と、構造、構造化データ、権威性といった定番の戦略に研究が収束しつつあることを示した論文です。 (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - AI Overviews と AI Mode がスペインのニュースサイトへのトラフィックを大きく減らしたとし、GEO、読者のロイヤルティ向上、集団ライセンスへの取り組みを促す記事です。 (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - 機関リポジトリ向けに初めての GEO ガイドラインを提案し、技術的な設定、意味構造、メタデータ、多言語コンテンツ、新しい指標を扱った論文です。 (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - スペイン語プロンプト 226万件から、ChatGPT、Gemini、Perplexity、Copilot、Grok、Google の AI 機能が最も引用するニュースメディアを順位づけした調査です。 (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - バルセロナ大学による 2699キーワードの研究の要約で、スペインの主要メディアに関する検索の 29.8% に AI Overviews が表示され、速報ではまれなことを示しています。 (2026)

### ドイツ語

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - 検索から AI 回答システムへの移行を扱ったドイツのデジタル業界団体 BVDW のホワイトペーパーで、GEO の標準的な定義案と SEO との関係を示しています。 (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - ドイツ語の ChatGPT 回答 380万件を分析し、2026年5月のモデル切り替えで引用ドメインの構成が 2日以内に 47% 変化したことを示した記事です。 (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - 25万件の AI 回答の調査をもとに、ChatGPT、AI Overviews、Perplexity が最も多く引用する情報源の上位は企業サイト、YouTube、Reddit だと伝える記事です。 (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - ChatGPT、Gemini、Copilot、Perplexity のページ探索と引用の仕組みをクエリファンアウト、検索インデックス、技術的アクセスから解説し、企業向けチェックリストも付けています。 (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - ドイツ語圏（DACH）の AI 回答で同じドメインの引用ページと非引用ページを比較し、構造とスキーマは引用と相関する一方、llms.txt には効果が見られないことを示した調査です。 (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - 生成検索でのブランドの可視性を測る 9つの GEO KPI を提案した BVDW の短いホワイトペーパーで、プロンプトセットや定期的な見直しについても助言しています。 (2026)

## 事例

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - Ahrefs 自社のアナリティクスをもとに、AI 検索からの訪問者がトラフィックの 0.5% にすぎない一方で、登録の 12.1% を占めたことを示した記事です。 (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - Ramp の買掛金管理製品の AI 検索での可視性が Profound の計測で 22.2% に上昇したことを、Ramp が狙ったページやクエリとともに報告したベンダーの事例です。 (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - Vercel が LLM による発見に向けて SEO をどう適応させているかを紹介し、新規登録の約 10% が ChatGPT 経由となり、半年前の 1% から増えたことを報告した記事です。 (2025)

## 講座・動画・ポッドキャスト

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Sam Oh による全 12回の無料動画講座で、AI 検索エンジンの引用元の選び方、プロンプト調査、AI 検索向けのコンテンツと YouTube、技術設定、AI トラフィックの追跡を扱います。
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - SkillUp による Coursera の 4時間・2モジュールの講座で、エンティティとトピックの権威性、AI に適したコンテンツ形式、GEO の指標、実践演習を扱い、修了証は有料です。
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - 回答エンジンに引用される方法、質問の調査、ページ内とスキーマの施策、AI 経由の流入とシェア・オブ・ボイスの測定を全 7回で学べる無料の認定講座です。
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Aleyda Solis が監修した無料の学習ロードマップで、AI 検索の基礎、計測、EC、ツールに関するガイドを順序立てて紹介し、コンテンツ最適化のチェックリストも付いています。
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - アーンドメディアが AI 回答に与える影響、プロンプトのテスト、GEO の知見のメディアターゲティングへの活用を学べる、PR・広報チーム向けの短い認定講座です。
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Google 検索の舞台裏を、AI 機能や SEO コミュニティの最新の話題も含めて語る、Google Search Relations チームのポッドキャストです。
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - プロンプト調査、シェア・オブ・ボイス、ブランド言及、LLM 向けのコンテンツ構成を扱う全 20本の修了証付き無料動画講座で、一部のレッスンでは Semrush のツールを実演しています。

## ニュースレターとコミュニティ

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Tom Critchlow による Substack のニュースレター（旧称 The SEO MBA）で、AI 検索に適応する検索チーム向けの戦略とリーダーシップを扱います。
- [brightonSEO](https://brightonseo.com/) 💲 - ブライトンとサンディエゴで開かれる大規模な検索マーケティングのカンファレンスシリーズで、SEO・コンテンツ・AI 検索の講演とトレーニングがあり、英国開催分は無料チケットの抽選もあります。
- [GEO Conference](https://geo-conference.com/) 💲 - 米国の各都市で開かれる生成エンジン最適化の 1日限りの対面カンファレンスシリーズで、各回の定員は 150席、主に GEO・SEO ツールベンダーが協賛しています。
- [Growth Memo](https://www.growth-memo.com/) 🪙 - Kevin Indig によるオーガニック成長のニュースレターで、AI 検索の行動、引用、トラフィックに関するデータ調査を定期的に掲載し、一部は有料購読者向けです。
- [MozCon](https://moz.com/mozcon) 💲 - SEO、AI 検索、GEO を扱う Moz のマーケティングカンファレンスで、2026年はロンドンとニューヨークを巡る対面のロードショー形式で開催されています。
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Barry Schwartz による日刊のニュースサイトで、検索コミュニティでの議論や、AI 検索機能を含む Google と Bing の変更を追っています。
- [SEOFOMO](https://seofomo.co/) 🆓 - Aleyda Solis による週刊ニュースレターで、SEO と AI 検索のニュース、ガイド、ツール、イベント、求人をまとめています。

## ほかの厳選リスト

GEO や AI 検索を扱う、本リストと関連の深いリストを感謝を込めて紹介します。

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - プラットフォーム別ガイド、エージェント型コマース、ツール、研究、ニュースレター、動画、イベントを幅広く集めた GEO リソースリストです。
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - GEO の論文を年ごとに整理した、研究中心のリストです。
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - GEO 向けの無料プラットフォームとオープンソースのリポジトリを集めたリストで、関連サイトではスコア、検索機能、無料ツールを提供しています。
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - GEO と AI 可視性の追跡ツールをアルファベット順に並べ、機能と料金の簡単なメモを添えたディレクトリです。
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - 学習リソース、ツール、AI 検索エンジン、戦略、モニタリング、事例、コミュニティ、プラットフォームのニュースを扱う、GEO の総合的なリストです。
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - 研究、プラットフォームの公式ドキュメント、ガイド、ツール、講座、ニュースレター、コミュニティを集めた GEO のリスト（旧 Tusko/awesome-geo）です。
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - 対応エンジン、更新頻度、価格、データエクスポートで GEO ツールを比較した表で、自社製品も掲載している GEO ツールベンダーが管理しています。

## コントリビューション

コントリビューションを歓迎します。プルリクエストを送る前に[コントリビューションガイド](CONTRIBUTING.md)をお読みください。説明文は英語だけで構いません。ほかの言語はメンテナーが追加します。

## ライセンス

法律で認められる範囲において、コントリビューターは [CC0 1.0 ユニバーサル](LICENSE) に基づき、このリストに関する著作権および関連する権利をすべて放棄しています。
