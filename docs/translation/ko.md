# Korean translation style guide (ko)

For translators writing `desc.ko` from `desc.en` in `data/resources/*.yaml`, and for the Korean copy in `data/categories.yaml` and `data/i18n.yaml`.

## 1. Principles

- **Rewrite, do not transliterate.** Understand the fact the English sentence states, then write it the way a Korean technical writer would. The result should read like original Korean.
- **Same facts, nothing more, nothing less.** Do not add features, numbers or opinions that are not in the English; do not drop the key facts (subject, method, scale, year, platform). You may add a head noun that matches the resource `type`, e.g. 〜논문입니다, 〜도구입니다, 〜가이드입니다.
- **One sentence**, ending in a period.
- **Neutral and plain.** No marketing words (혁신적인, 최고의, 강력한, 손쉽게, 필수). No exclamation marks.
- **Do not address the reader** (no 당신, 여러분). Do not start with 이 글은 / 이 도구는.
- **Names stay as they are.** The `name` field, product, company and paper names are not translated (ChatGPT, Perplexity, Profound). Korean services use their Korean names: 네이버, 카카오, 네이버 서치어드바이저. Chinese products use the Latin names in the shared table [product-names.md](product-names.md) (e.g. Qwen, ERNIE Bot, Tencent Yuanbao, Metaso); never improvise a romanization or use a former name.
- **Plain text only**: no Markdown, links or emoji.

## 2. Glossary

| English | Korean | Notes |
|---|---|---|
| GEO / Generative Engine Optimization | 생성형 엔진 최적화(GEO) | Use the full form when the English spells it out or GEO is the main topic; otherwise GEO alone |
| SEO | SEO | Keep English |
| AEO / Answer Engine Optimization | 답변 엔진 최적화(AEO) | |
| LLMO / LLM Optimization | LLM 최적화(LLMO) | |
| AI Overviews | AI Overviews | Keep the English product name, "Google AI Overviews". Google's Korean UI says AI 개요; do not use it in descriptions. AI Mode is kept in English as well |
| answer engine | AI 답변 엔진 / 답변 엔진 | Not 응답 엔진 |
| answer / response | 답변 | Not 응답 |
| generative engine | 생성형 엔진 | Not 생성 엔진 |
| AI search | AI 검색 | AI search engine → AI 검색 엔진 |
| LLM / large language model | LLM / 대규모 언어 모델 | |
| citation / cite | 인용 / 인용되다 | |
| source (of an answer) | 출처 / 인용 출처 | Not 소스 |
| visibility | 가시성 | Not 노출도 |
| brand mention | 브랜드 언급 | |
| share of voice | 보이스 점유율(SOV) | |
| crawler / bot | 크롤러 | AI crawler → AI 크롤러; crawl → 크롤링 |
| user agent | 사용자 에이전트 | |
| structured data | 구조화된 데이터 | Google's official Korean term |
| schema markup | 스키마 마크업 | Schema.org stays as is |
| prompt | 프롬프트 | |
| prompt injection | 프롬프트 인젝션 | |
| benchmark | 벤치마크 | |
| dataset | 데이터셋 | |
| RAG / retrieval-augmented generation | 검색 증강 생성(RAG) | |
| ranking | 순위 | |
| query | 쿼리 | User-facing questions may be 검색어 or 질문 |
| zero-click search | 제로 클릭 검색 | |
| knowledge graph | 지식 그래프 | |
| monitoring / tracking | 모니터링 / 추적 | |
| audit | 진단 | content audit → 콘텐츠 진단 |
| open source | 오픈 소스 | With a space |
| webmaster | 웹마스터 | |
| tool | 도구 | Not 툴 |
| llms.txt / robots.txt | llms.txt / robots.txt | As is |
| survey (paper) | 서베이 논문 | |
| case study | 사례 연구 | |
| E-E-A-T | E-E-A-T | |

## 3. Tone

- **합니다체** throughout. End with 〜합니다. or 〜입니다.
- No 해요체, no noun-ending (명사형 종결) such as 〜제공. or 〜논문. Write 〜제공합니다. / 〜논문입니다.
- Avoid translationese: 〜에 있어서, 〜를 통해 (overused), 〜되어지다 (double passive), 〜를 가지고 있다 for "has", plural 〜들 on every noun.
- Prefer active verbs: 분석합니다, 정리합니다, 추적합니다.

## 4. Punctuation and spacing

- Korean uses **half-width** punctuation: . , ( ) ·. Do not use full-width 。、（） in Korean text; the CJK full-width rule applies to Chinese and Japanese only.
- Normal Korean word spacing (띄어쓰기). Particles attach directly to Latin words with no space: GEO는, ChatGPT에서, LLM을.
- Pick the particle by how the word is read aloud: GEO(지오)·SEO·AI·llms.txt end in a vowel → 는/를/와; LLM(엘엘엠)·RAG(래그) end in a consonant → 은/을/과.
- Use “…” if a quotation is unavoidable.
- One period at the end of the sentence.
- Numbers in Arabic numerals; use 만 for large numbers (10,000 → 1만 개).

## 5. Length

- Hard limit **100 characters** (checked by `validate.py`; spaces and punctuation count).
- Aim for 35 to 75. If it is too long, cut modifiers and minor details first.

## 6. Bad → good examples

1. EN: *Tracks how often a brand is mentioned and cited in ChatGPT, Perplexity and Google AI Overviews answers.*
   - ✗ ChatGPT, Perplexity 그리고 Google AI Overviews 응답들에서 브랜드가 얼마나 자주 언급되고 인용되는지를 추적하는 툴.
   - ✓ ChatGPT, Perplexity, Google AI Overviews 답변에서 브랜드가 언급·인용되는 빈도를 추적하는 도구입니다.
   - Why: noun ending; 그리고 in a list; 응답들/툴 instead of glossary terms.

2. EN: *A study of how generative engines select sources, based on 10,000 queries across five verticals.*
   - ✗ 생성형 엔진들이 어떻게 소스들을 선택하는지에 대한 연구로, 다섯 개의 버티컬에 걸친 10,000개의 쿼리들에 기반하고 있다.
   - ✓ 5개 업종의 쿼리 1만 개를 바탕으로 생성형 엔진이 인용 출처를 고르는 방식을 분석한 연구입니다.
   - Why: 〜에 대한 연구로 and 〜에 기반하고 있다 are translationese; 들 everywhere; 한다체 instead of 합니다체.

3. EN: *Explains how to write an llms.txt file and which engines currently read it.*
   - ✗ llms.txt 파일을 작성하는 방법과 어떤 엔진들이 현재 그것을 읽는지에 대해서 설명합니다.
   - ✓ llms.txt 파일 작성법과 현재 이 파일을 읽어 들이는 엔진을 설명합니다.
   - Why: 그것 copies the English pronoun; 〜에 대해서 is redundant.

## 7. Checklist

- [ ] Ends with 합니다. or 입니다., one sentence, ≤ 100 characters.
- [ ] Terms match the glossary (답변 not 응답, 출처 not 소스, 도구 not 툴).
- [ ] Half-width punctuation; particles match pronunciation.
- [ ] No marketing words, no reader address.
- [ ] Facts match the English exactly.
