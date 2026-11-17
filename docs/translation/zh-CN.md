# 简体中文翻译规范（zh-CN）

适用对象：把 `data/resources/*.yaml` 中的 `desc.en` 译成 `desc.zh-CN` 的译者，也适用于 `data/categories.yaml` 与 `data/i18n.yaml` 的中文文案。

## 1. 基本原则

- **意译，不直译。** 先读懂英文句子要表达的事实，再用中文技术写作的习惯说法重写。读起来像中文原创，而不是英文的逐词替换。
- **只译事实，不增不减。** 不添加英文原文没有的信息（功能、数字、评价），也不丢掉原文的关键事实（对象、方法、规模、年份、平台）。允许按 `type` 补一个中心词，例如“……的论文”“……的开源工具”。
- **一句话。** 每条描述只有一个句子，以“。”结尾。
- **客观中立。** 不用营销词：强大、领先、一站式、全方位、赋能、助力、轻松、神器、必备。不用感叹号。
- **不称呼读者。** 不出现“你/您/我们”。不以“本文”“该工具”“这是一个”开头。
- **名称不译。** `name` 字段和产品名、公司名、论文标题保持原文（ChatGPT、Perplexity、Profound、Semrush）。中国产品一律使用 [product-names.md](product-names.md) 中的现行中文名称（如 千问 而非 通义，文心 而非 文心一言），不使用旧称。
- **纯文本。** 不写 Markdown、链接、引号包裹的强调，也不用 emoji。

## 2. 术语表

| 英文 | 中文标准写法 | 说明 |
|---|---|---|
| GEO / Generative Engine Optimization | 生成式引擎优化（GEO） / GEO | README 开头已解释全称，资源描述通常直接用 GEO；介绍术语本身时写全称 |
| SEO | SEO | 直接用 SEO；英文写出全称时译为“搜索引擎优化（SEO）” |
| AEO / Answer Engine Optimization | 答案引擎优化（AEO） | 行业惯用“答案引擎优化”；单说 answer engine 时用“回答引擎” |
| LLMO / LLM Optimization | 大语言模型优化（LLMO） | |
| AI Overviews | AI Overviews | 保留英文产品名，写作“Google AI Overviews”；AI Mode 同样保留英文 |
| answer engine | AI 回答引擎 / 回答引擎 | |
| generative engine | 生成式引擎 | |
| AI search | AI 搜索 | AI search engine 译“AI 搜索引擎” |
| LLM / large language model | 大语言模型 / LLM | 不写“大型语言模型” |
| citation / cite | 引用 / 被引用 | 指 AI 回答中注明的来源；不写“引证”“援引” |
| source (of an answer) | 引用来源 / 信息来源 | |
| visibility | 可见度 | 不写“可见性”“曝光度” |
| brand mention | 品牌提及 | |
| share of voice | 声量占比 | |
| crawler / bot | 爬虫 | AI crawler 译“AI 爬虫”；crawl 译“抓取” |
| user agent | User-Agent | 保留英文 |
| structured data | 结构化数据 | |
| schema markup | Schema 标记 | Schema.org 保留原文 |
| prompt | 提示词 | 不写“提示”“指令” |
| prompt injection | 提示词注入 | |
| benchmark | 基准 | 强调测试过程时可写“基准测试” |
| dataset | 数据集 | |
| RAG / retrieval-augmented generation | 检索增强生成（RAG） | |
| ranking | 排名 | |
| query | 查询 | 用户输入的问题也可写“提问” |
| zero-click search | 零点击搜索 | |
| knowledge graph | 知识图谱 | |
| monitoring / tracking | 监测 / 追踪 | |
| audit | 审计 | content audit 译“内容审计” |
| open source | 开源 | |
| webmaster | 站长 | webmaster tools 译“站长平台/站长工具” |
| sitemap | 网站地图（sitemap） | |
| llms.txt / robots.txt | llms.txt / robots.txt | 原样，不加代码格式 |
| survey (paper) | 综述 | |
| case study | 案例研究 | |
| E-E-A-T | E-E-A-T | 保留 |

## 3. 标点与排版

- 使用全角标点：，。、：；（）《》。括号一律用全角“（）”，包括“生成式引擎优化（GEO）”。
- 并列名词用顿号“、”：ChatGPT、Perplexity 和 Google AI Overviews。
- 中文与英文、数字之间加一个半角空格（“基于 1 万条查询”“AI 爬虫”）；全角标点前后不加空格。
- 句末用“。”，全句只有一个句号。
- 数字用阿拉伯数字；大数用“万”“亿”（10,000 → 1 万）。
- 尽量不用引号；需要时用“”。

## 4. 长度

- 上限 **100 个字符**（`validate.py` 强制检查，空格和标点都计入）。
- 建议 30 到 70 个字符。超长时删掉修饰语和次要细节，保留“是什么 + 做什么 + 关键对象”。

## 5. 句式

- 常用动词开头的无主句：“提出……”“监测……”“汇总……”“分析……”。
- 或用“……的 + 中心词”名词短语，再加句号：“根据网站地图生成 llms.txt 文件的开源 Python 库。”
- 避免英文式长定语和被动句：少用“被……所……”“对于……来说”“基于……的……的……”。

## 6. 反例与正例

1. 英文：*Tracks how often a brand is mentioned and cited in ChatGPT, Perplexity and Google AI Overviews answers.*
   - ✗ 跟踪一个品牌在 ChatGPT, Perplexity 和 Google AI Overviews 的答案中被提及和被引用的频率如何。
   - ✓ 追踪品牌在 ChatGPT、Perplexity 和 Google AI Overviews 回答中被提及和引用的频率。
   - 问题：“一个品牌”“频率如何”是直译腔；半角逗号；重复“被”。

2. 英文：*A study of how generative engines select sources, based on 10,000 queries across five verticals.*
   - ✗ 一个关于生成式引擎如何选择来源的研究，基于横跨五个垂直领域的 10,000 个查询。
   - ✓ 基于五个行业的 1 万条查询，研究生成式引擎如何选择引用来源。
   - 问题：“一个关于……的研究”照搬英文结构；“横跨……垂直领域”生硬；中文大数应写“1 万”。

3. 英文：*Open-source Python library for generating llms.txt files from a sitemap.*
   - ✗ 开源的Python库用于从一个sitemap生成llms.txt文件。
   - ✓ 根据网站地图（sitemap）生成 llms.txt 文件的开源 Python 库。
   - 问题：中英文之间缺空格；“用于”后置是英文语序；“一个”多余。

## 7. 自查清单

- [ ] GEO 的写法符合语境，没有在连续条目中反复解释全称。
- [ ] 术语与上表一致，没有混用“可见性/可见度”“爬虫/抓取器”。
- [ ] 一句话，全角标点，句末“。”，不超过 100 字符。
- [ ] 没有营销词，没有“你/您/本文/该工具”。
- [ ] 事实与英文原文一致，没有增删。
