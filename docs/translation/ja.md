# Japanese translation style guide (ja)

For translators writing `desc.ja` from `desc.en` in `data/resources/*.yaml`, and for the Japanese copy in `data/categories.yaml` and `data/i18n.yaml`.

## 1. Principles

- **Rewrite, do not transliterate.** Understand the fact the English sentence states, then write it the way a Japanese technical writer would. The result should read like original Japanese, not English word order with Japanese words.
- **Same facts, nothing more, nothing less.** Do not add features, numbers or opinions that are not in the English; do not drop the key facts (subject, method, scale, year, platform). You may add a head noun that matches the resource `type`, e.g. 〜論文です, 〜ツールです, 〜ガイドです.
- **One sentence**, ending in 「。」.
- **Neutral and plain.** No marketing words (革新的, 最強, 圧倒的, 簡単に, 必見, 徹底解説). No exclamation marks.
- **Do not address the reader** (no あなた, 皆さん). Do not start with この記事は / このツールは.
- **Names stay as they are.** The `name` field, product, company and paper names are not translated (ChatGPT, Perplexity, Profound). Korean products use their Latin names (Naver, Kakao). Chinese products use the Latin names in the shared table [product-names.md](product-names.md) (e.g. Qwen, ERNIE Bot, Tencent Yuanbao, Metaso); never improvise a romanization or use a former name.
- **Plain text only**: no Markdown, links or emoji.

## 2. Glossary

| English | Japanese | Notes |
|---|---|---|
| GEO / Generative Engine Optimization | 生成エンジン最適化（GEO） | Use the full form when the English spells it out or GEO is the main topic; otherwise GEO alone |
| SEO | SEO | Keep English |
| AEO / Answer Engine Optimization | アンサーエンジン最適化（AEO） | |
| LLMO / LLM Optimization | LLMO（LLM 最適化） | LLMO is widely used in the Japanese industry (LLMO 対策); keep it |
| AI Overviews | AI Overviews | Keep the English product name, "Google の AI Overviews". Google's Japanese UI says AI による概要; do not use it in descriptions. AI Mode is kept in English as well |
| answer engine | AI 回答エンジン / 回答エンジン | |
| generative engine | 生成エンジン | |
| AI search | AI 検索 | AI search engine → AI 検索エンジン |
| LLM / large language model | LLM / 大規模言語モデル | |
| citation / cite | 引用 / 引用される | Do **not** use サイテーション: in Japanese SEO it means a brand mention |
| source (of an answer) | 引用元 / 情報源 | |
| visibility | 可視性 | Not 視認性 or 露出度 |
| brand mention | ブランド言及 | |
| share of voice | シェア・オブ・ボイス（SOV） | |
| crawler / bot | クローラー | AI crawler → AI クローラー; crawl → クロール |
| user agent | ユーザーエージェント | |
| structured data | 構造化データ | |
| schema markup | スキーママークアップ | Schema.org stays as is |
| prompt | プロンプト | |
| prompt injection | プロンプトインジェクション | |
| benchmark | ベンチマーク | |
| dataset | データセット | |
| RAG / retrieval-augmented generation | 検索拡張生成（RAG） | |
| ranking | 順位 / ランキング | |
| query | クエリ | |
| zero-click search | ゼロクリック検索 | |
| knowledge graph | ナレッジグラフ | |
| monitoring / tracking | モニタリング / 追跡 | |
| audit | 監査 | content audit → コンテンツ監査 |
| open source | オープンソース | |
| webmaster | ウェブマスター | |
| llms.txt / robots.txt | llms.txt / robots.txt | As is |
| survey (paper) | サーベイ論文 | |
| case study | 事例 | |
| E-E-A-T | E-E-A-T | |

## 3. Tone

- **です・ます体** throughout. End the sentence with 〜です。 or 〜ます。
- No 体言止め (ending on a bare noun such as 〜を提案した論文。). Write 〜を提案した論文です。
- Prefer 〜できます over 〜することができます, and 〜を分析した over 〜についての分析を行った.
- Do not stack katakana where an established kanji term exists (検証 rather than ベリフィケーション).

## 4. Punctuation and spacing

- Full-width punctuation: 、。（）「」・. Parentheses are always full-width （）.
- Use 「」 if a quotation is unavoidable. Use 、 or ・ to list items (言及・引用).
- Put a half-width space between Japanese and Latin letters or digits (AI 検索, GPT-4 の) — this matches the rest of the project. No space next to full-width punctuation. Do not put a space between a number and its Japanese counter or unit (5業界・1万件, 3回, 2024年).
- One 「。」 at the end of the sentence.
- Numbers in Arabic numerals; use 万 for large numbers (10,000 → 1万).

## 5. Length

- Hard limit **100 characters** (checked by `validate.py`; spaces and punctuation count).
- Aim for 35 to 75. If it is too long, cut modifiers and minor details first.

## 6. Bad → good examples

1. EN: *Tracks how often a brand is mentioned and cited in ChatGPT, Perplexity and Google AI Overviews answers.*
   - ✗ ブランドが ChatGPT、Perplexity、Google AI Overviews の回答においてどれだけ頻繁に言及され、引用されるかを追跡する。
   - ✓ ChatGPT、Perplexity、Google AI Overviews の回答でブランドが言及・引用される頻度を追跡できるツールです。
   - Why: である調; English word order (どれだけ頻繁に); においての多用.

2. EN: *A study of how generative engines select sources, based on 10,000 queries across five verticals.*
   - ✗ 生成エンジンがどのようにソースを選択するかについての研究で、5つのバーティカルにわたる10,000のクエリに基づいている。
   - ✓ 5業界・1万件のクエリをもとに、生成エンジンが引用元をどう選ぶかを分析した研究です。
   - Why: どのように〜かについての is translationese; バーティカル is jargon; missing spaces; である調.

3. EN: *Explains how to write an llms.txt file and which engines currently read it.*
   - ✗ llms.txtファイルをどのように書くか、そしてどのエンジンが現在それを読むかを説明する。
   - ✓ llms.txt の書き方と、現在どのエンジンが読み込んでいるかを解説したガイドです。
   - Why: そして and それ copy English connectives and pronouns; no spaces around llms.txt; である調.

## 7. Checklist

- [ ] Ends with です。 or ます。, one sentence, ≤ 100 characters.
- [ ] Terms match the glossary (引用 not サイテーション, 可視性 not 視認性).
- [ ] Full-width punctuation, half-width space around Latin words and digits.
- [ ] No marketing words, no reader address.
- [ ] Facts match the English exactly.
