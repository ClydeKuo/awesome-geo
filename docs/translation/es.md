# Spanish translation style guide (es)

For translators writing `desc.es` from `desc.en` in `data/resources/*.yaml`, and for the Spanish copy in `data/categories.yaml` and `data/i18n.yaml`.

## 1. Principles

- **Rewrite, do not calque.** Understand the fact the English sentence states, then write it the way a Spanish-speaking technical writer would. The result should read like original Spanish.
- **Neutral international Spanish**, understandable in Spain and Latin America. Avoid regionalisms (ordenador/computadora, coger, platicar). Choose forms shared by both where possible: *seguimiento* (not *monitorización* or *monitoreo*), *video* (no accent).
- **Same facts, nothing more, nothing less.** Do not add features, numbers or opinions that are not in the English; do not drop the key facts (subject, method, scale, year, platform).
- **One sentence**, ending with a period.
- **Neutral and plain.** No marketing words (potente, revolucionario, líder, definitivo, imprescindible, fácilmente). No exclamation marks.
- **Do not address the reader** (no tú/usted in descriptions). Do not start with *Este artículo* / *Esta herramienta*.
- **Names stay as they are.** The `name` field, product, company and paper names are not translated (ChatGPT, Perplexity, Profound). Korean products use their Latin names (Naver, Kakao). Chinese products use the Latin names in the shared table [product-names.md](product-names.md) (e.g. Qwen, ERNIE Bot, Tencent Yuanbao, Metaso); never improvise a romanization or use a former name.
- **Plain text only**: no Markdown, links or emoji.

## 2. Glossary

| English | Spanish | Notes |
|---|---|---|
| GEO / Generative Engine Optimization | optimización para motores generativos (GEO) | Full form when the English spells it out; otherwise *el GEO* (masculine, like *el SEO*) |
| SEO | el SEO | Keep English acronym |
| AEO / Answer Engine Optimization | optimización para motores de respuestas (AEO) | |
| LLMO / LLM Optimization | optimización para LLM (LLMO) | |
| AI | IA | Always *IA*, except inside product names (Google AI Overviews, AI Mode) |
| AI Overviews | AI Overviews | Keep the English product name; do not use the localized UI name in descriptions. AI Mode is kept in English as well |
| answer engine | motor de respuestas | *motores de respuestas con IA* |
| generative engine | motor generativo | |
| AI search / AI search engine | búsqueda con IA / buscador de IA | |
| LLM / large language model | LLM / modelo de lenguaje grande | Plural *los LLM* (no -s) |
| citation / cite | cita / citar | Not *citación* (legal summons) |
| source (of an answer) | fuente | |
| visibility | visibilidad | |
| brand mention | mención de marca | |
| share of voice | cuota de voz (share of voice) | |
| crawler / bot | rastreador | crawl → *rastrear* |
| user agent | user agent | Keep English |
| structured data | datos estructurados | |
| schema markup | marcado Schema | Schema.org stays as is |
| prompt | prompt | Plural *los prompts* |
| prompt injection | inyección de prompts | |
| benchmark | benchmark | Plural *los benchmarks* |
| dataset | conjunto de datos | |
| RAG / retrieval-augmented generation | generación aumentada por recuperación (RAG) | |
| ranking | posicionamiento / ranking | |
| query | consulta | |
| zero-click search | búsqueda sin clic | |
| knowledge graph | grafo de conocimiento | |
| monitoring / tracking | seguimiento | |
| audit | auditoría | |
| open source | código abierto | *herramienta de código abierto* |
| webmaster | webmaster | |
| tool | herramienta | |
| dashboard | panel | |
| llms.txt / robots.txt | llms.txt / robots.txt | As is; *el archivo llms.txt* |
| survey (paper) | revisión | |
| case study | estudio de caso | |
| E-E-A-T | E-E-A-T | |

## 3. Tone and grammar

- Present tense, third person, usually verb-first and subject-less: *Analiza…*, *Recopila…*, *Explica…*, *Presenta…*. A noun phrase is also fine: *Estudio sobre…*, *Biblioteca de Python que…*.
- Sentence case: capitalize only the first word and proper nouns. Never English-style Title Case.
- Avoid anglicisms in structure: gerund openings (*Mostrando…*), passive *es usado/es mencionada* (use *se usa*, *se menciona*), redundant possessives where an article is enough (*el contenido del sitio*, not *su contenido de su sitio*), *basado en* chains, *a través de* for "across".
- Avoid redundant articles and *un/una* where English has "a/an" at the start (*Un estudio de…* → *Estudio sobre…*).

## 4. Punctuation and numbers

- One sentence, final period. Use ¿? and ¡! in pairs if ever needed (rare).
- Use «…» if a quotation is unavoidable.
- Thousands: *10 000* (space, per RAE); decimals with a comma: *2,5 %*.
- No serial (Oxford) comma before *y*: *ChatGPT, Perplexity y Google AI Overviews*.

## 5. Length

- Hard limit **200 characters** (checked by `validate.py`).
- Spanish runs about 15 to 25 % longer than English; aim for ≤ 170. If it is too long, cut modifiers and minor details first.

## 6. Bad → good examples

1. EN: *Tracks how often a brand is mentioned and cited in ChatGPT, Perplexity and Google AI Overviews answers.*
   - ✗ Rastrea cuán a menudo una marca es mencionada y citada en respuestas de ChatGPT, Perplexity, y Google AI Overviews.
   - ✓ Mide con qué frecuencia se menciona y se cita una marca en las respuestas de ChatGPT, Perplexity y Google AI Overviews.
   - Why: English passive (*es mencionada*), *cuán a menudo* is a calque, Oxford comma.

2. EN: *A study of how generative engines select sources, based on 10,000 queries across five verticals.*
   - ✗ Un estudio de cómo los motores generativos seleccionan fuentes, basado en 10,000 consultas a través de cinco verticales.
   - ✓ Estudio sobre cómo eligen sus fuentes los motores generativos a partir de 10 000 consultas de cinco sectores.
   - Why: *Un estudio de* copies the English article; *a través de* and *verticales* are calques; English number format.

3. EN: *Explains how to write an llms.txt file and which engines currently read it.*
   - ✗ Explica cómo escribir un archivo llms.txt y cuáles motores actualmente lo leen.
   - ✓ Explica cómo redactar un archivo llms.txt y qué motores lo leen en la actualidad.
   - Why: *cuáles motores* is non-standard before a noun (use *qué*); adverb placement follows English.

## 7. Checklist

- [ ] One sentence, final period, ≤ 200 characters.
- [ ] *IA* not *AI* (except product names); terms match the glossary.
- [ ] No passive *ser + participio* where *se* works; no English Title Case.
- [ ] No marketing words, no reader address.
- [ ] Facts match the English exactly.
