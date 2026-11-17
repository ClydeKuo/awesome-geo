# German translation style guide (de)

For translators writing `desc.de` from `desc.en` in `data/resources/*.yaml`, and for the German copy in `data/categories.yaml` and `data/i18n.yaml`.

## 1. Principles

- **Rewrite, do not calque.** Understand the fact the English sentence states, then write it the way a German technical writer would. The result should read like original German.
- **Same facts, nothing more, nothing less.** Do not add features, numbers or opinions that are not in the English; do not drop the key facts (subject, method, scale, year, platform).
- **One sentence**, ending with a period.
- **Neutral, objective statement (sachlich).** No marketing words (leistungsstark, revolutionär, ultimativ, führend, mühelos, Must-have). No exclamation marks.
- **Do not address the reader** (no du/Sie in descriptions). Do not start with *Dieser Artikel* / *Dieses Tool*.
- **Names stay as they are.** The `name` field, product, company and paper names are not translated (ChatGPT, Perplexity, Profound). Korean products use their Latin names (Naver, Kakao). Chinese products use the Latin names in the shared table [product-names.md](product-names.md) (e.g. Qwen, ERNIE Bot, Tencent Yuanbao, Metaso); never improvise a romanization or use a former name.
- **Plain text only**: no Markdown, links or emoji.

## 2. Glossary

| English | German | Notes |
|---|---|---|
| GEO / Generative Engine Optimization | Generative Engine Optimization (GEO) | Not translated; this is the established term in German. Avoid an article where possible |
| SEO | SEO | Keep English; avoid an article (*die/das SEO* are both used) |
| AEO / Answer Engine Optimization | Answer Engine Optimization (AEO) | |
| LLMO / LLM Optimization | LLM-Optimierung (LLMO) | |
| AI | KI | Always *KI* (KI-Suche, KI-Crawler), except inside product names (Google AI Overviews, AI Mode) |
| AI Overviews | AI Overviews | Keep the English product name; Google's German UI calls it *Übersicht mit KI* (since 2025-03); do not use that label in descriptions. AI Mode is kept in English as well |
| answer engine | Antwortmaschine | *KI-Antwortmaschine* |
| generative engine | generative Suchmaschine | Not *generative Engine* |
| AI search / AI search engine | KI-Suche / KI-Suchmaschine | |
| LLM / large language model | LLM / großes Sprachmodell | *das LLM*, plural *die LLMs* |
| citation / cite | Zitation / zitieren | "cited in answers" → *als Quelle zitiert* or *als Quelle genannt* |
| source (of an answer) | Quelle | |
| visibility | Sichtbarkeit | |
| brand mention | Markenerwähnung | |
| share of voice | Share of Voice | |
| crawler / bot | Crawler | *der Crawler*; crawl → *crawlen* |
| user agent | User-Agent | |
| structured data | strukturierte Daten | |
| schema markup | Schema-Markup | Schema.org stays as is |
| prompt | Prompt | *der Prompt*, plural *die Prompts* |
| prompt injection | Prompt-Injection | |
| benchmark | Benchmark | *der Benchmark* |
| dataset | Datensatz | |
| RAG / retrieval-augmented generation | Retrieval-Augmented Generation (RAG) | |
| ranking | Ranking | |
| query | Suchanfrage / Anfrage | Not *Query* |
| zero-click search | Zero-Click-Suche | |
| knowledge graph | Knowledge Graph | |
| monitoring / tracking | Monitoring / erfassen | Do not use *tracken* |
| audit | Audit | *Content-Audit* |
| open source | Open Source | Adjectival compounds: *Open-Source-Tool*, *Open-Source-Bibliothek* |
| webmaster | Webmaster | |
| tool | Tool | *das Tool* |
| dashboard | Dashboard | |
| llms.txt / robots.txt | llms.txt / robots.txt | As is; compounds *llms.txt-Datei* |
| survey (paper) | Übersichtsarbeit | |
| case study | Fallstudie | |
| E-E-A-T | E-E-A-T | |

## 3. Tone and grammar

- Neutral, objective third person. Either verb-first without a subject (*Analysiert …*, *Erfasst …*, *Stellt … vor.*) or a short noun phrase (*Studie zur …*, *Python-Bibliothek, die …*). Keep one pattern per sentence.
- Avoid long noun chains (*Nominalstil*): prefer one verb over three genitives.
- Avoid Denglisch verbs (*tracken*, *checken*, *releasen*); English nouns from the glossary are fine.
- Ergänzungsstrich (suspended hyphen): when a hyphenated compound is coordinated, write the dash on the dropped part (*KI-Suchmaschinen und -Assistenten*, *Open-Source-Tools und -Bibliotheken*, *Content-Audit und -Optimierung*), not *KI-Suchmaschinen und Assistenten*.
- Couple compounds with hyphens (*Durchkopplung*): *KI-Crawler*, *llms.txt-Datei*, *ChatGPT-Antworten*. Never leave an open compound (*llms.txt Datei*, *Open Source Tool*).
- Nouns capitalized; sentence otherwise in normal sentence case.

## 4. Punctuation and numbers

- One sentence, final period. A comma before every subordinate clause (*…, wie oft …*).
- Avoid quotation marks; if unavoidable use »…«.
- Thousands with a dot (*10.000*), decimals with a comma (*2,5 %*).
- No serial comma before *und*.

## 5. Length

- Hard limit **200 characters** (checked by `validate.py`).
- German runs about 20 to 30 % longer than English; aim for ≤ 170. If it is too long, cut modifiers and minor details first.

## 6. Bad → good examples

1. EN: *Tracks how often a brand is mentioned and cited in ChatGPT, Perplexity and Google AI Overviews answers.*
   - ✗ Trackt, wie oft eine Marke in ChatGPT-, Perplexity- und Google AI Overviews Antworten erwähnt und zitiert wird.
   - ✓ Erfasst, wie oft eine Marke in Antworten von ChatGPT, Perplexity und Google AI Overviews erwähnt und als Quelle zitiert wird.
   - Why: *tracken* is Denglisch; the broken compound with an open *Overviews Antworten* is hard to read.

2. EN: *A study of how generative engines select sources, based on 10,000 queries across five verticals.*
   - ✗ Eine Studie davon, wie generative Engines Quellen selektieren, basierend auf 10,000 Queries über fünf Verticals.
   - ✓ Studie zur Quellenauswahl generativer Suchmaschinen auf Basis von 10.000 Suchanfragen aus fünf Branchen.
   - Why: *Studie davon* and *über fünf Verticals* are calques; English number format; unnecessary anglicisms.

3. EN: *Explains how to write an llms.txt file and which engines currently read it.*
   - ✗ Erklärt, wie man eine llms.txt Datei schreibt und welche Engines sie aktuell lesen.
   - ✓ Erklärt den Aufbau einer llms.txt-Datei und welche Suchmaschinen sie derzeit auswerten.
   - Why: open compound; *man* construction; *Engines* instead of the glossary term.

## 7. Checklist

- [ ] One sentence, final period, ≤ 200 characters.
- [ ] *KI* not *AI* (except product names); terms match the glossary.
- [ ] Compounds hyphenated; no Denglisch verbs.
- [ ] No marketing words, no reader address.
- [ ] Facts match the English exactly.
