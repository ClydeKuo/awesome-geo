# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | **Deutsch**

> Eine kuratierte Liste zu Generative Engine Optimization (GEO): Forschung, Leitfäden, Standards, Tools und KI-Suchmaschinen aus aller Welt.

## Inhalt

- [Was ist GEO](#was-ist-geo)
- [Einführung](#einführung)
- [Forschungsarbeiten](#forschungsarbeiten)
  - [Grundlagenarbeiten](#grundlagenarbeiten)
  - [Benchmarks und Datensätze](#benchmarks-und-datensätze)
  - [Angriffe und Manipulation](#angriffe-und-manipulation)
  - [Zitations- und Sichtbarkeitsanalysen](#zitations--und-sichtbarkeitsanalysen)
  - [Übersichtsarbeiten](#übersichtsarbeiten)
- [Leitfäden und Artikel](#leitfäden-und-artikel)
  - [Strategie](#strategie)
  - [Content-Erstellung](#content-erstellung)
  - [Technische Umsetzung](#technische-umsetzung)
  - [Branchenberichte und Daten](#branchenberichte-und-daten)
- [Standards und Spezifikationen](#standards-und-spezifikationen)
  - [llms.txt](#llmstxt)
  - [KI-Crawler und robots.txt](#ki-crawler-und-robotstxt)
  - [Strukturierte Daten](#strukturierte-daten)
  - [Offizielle Dokumentation der Anbieter](#offizielle-dokumentation-der-anbieter)
- [Tools](#tools)
  - [KI-Sichtbarkeits-Monitoring](#ki-sichtbarkeits-monitoring)
  - [Content-Audit und -Optimierung](#content-audit-und--optimierung)
  - [Open-Source-Tools und -Bibliotheken](#open-source-tools-und--bibliotheken)
  - [llms.txt-Generatoren](#llmstxt-generatoren)
  - [Crawler-Log-Analyse](#crawler-log-analyse)
- [KI-Suchmaschinen und -Assistenten](#ki-suchmaschinen-und--assistenten)
  - [International](#international)
  - [China](#china)
  - [Japan](#japan)
  - [Südkorea](#südkorea)
  - [Europa](#europa)
  - [Weitere Regionen](#weitere-regionen)
- [GEO-Ressourcen in weiteren Sprachen](#geo-ressourcen-in-weiteren-sprachen)
  - [Chinesisch](#chinesisch)
  - [Japanisch](#japanisch)
  - [Koreanisch](#koreanisch)
  - [Spanisch](#spanisch)
  - [Deutsch](#deutsch)
- [Fallstudien](#fallstudien)
- [Kurse, Videos und Podcasts](#kurse-videos-und-podcasts)
- [Newsletter und Communities](#newsletter-und-communities)
- [Weitere kuratierte Listen](#weitere-kuratierte-listen)
- [Lizenz](#lizenz)

**Legende:** 🆓 kostenlos, 🪙 Freemium, 💲 kostenpflichtig, 🔓 Open Source

## Was ist GEO

Generative Engine Optimization (GEO) umfasst alle Maßnahmen, mit denen Inhalte für KI-Antwortmaschinen wie ChatGPT, Perplexity oder Google AI Overviews leichter auffindbar, verständlich und zitierbar werden. Während es bei SEO um Rankings in einer Trefferliste geht, zielt GEO darauf ab, dass Inhalte direkt in der generierten Antwort zitiert oder erwähnt werden; der Erfolg bemisst sich daher eher an Zitationen und Sichtbarkeit als an Klicks. Der Begriff stammt aus dem Paper »GEO: Generative Engine Optimization« von Aggarwal et al. (Princeton University u. a., KDD 2024).

## Einführung

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - Einführung von Search Engine Land, die GEO als das Gewinnen von Zitationen und Erwähnungen in KI-Antworten definiert und beschreibt, wie es auf SEO-Grundlagen aufbaut.
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - Enzyklopädieeintrag, der GEO definiert, den Begriff auf die Forschungsarbeit von 2023 zurückführt, verwandte Bezeichnungen wie AEO und LLMO nennt und auf Kritik eingeht.
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - Bericht von Search Engine Journal über Googles Leitfaden vom Mai 2026, der AEO und GEO als Teil gewöhnlicher SEO behandelt und llms.txt und Chunking als Mythen entlarvt.
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - Googles eigener Leitfaden, nach dem die Optimierung für KI-Funktionen weiterhin SEO ist und Taktiken wie llms.txt und Chunking unnötig sind.
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - Vergleich von SEO und GEO bei Search Engine Land mit Blick auf Ziele, Messung und gemeinsame Praktiken.
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - Einführung, die den Begriff GEO auf das KDD-2024-Paper von Aggarwal et al. zurückführt, Branchendefinitionen vergleicht und den Wissensstand zur KI-Sichtbarkeit zusammenfasst.

## Forschungsarbeiten

### Grundlagenarbeiten

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - Zeigt ein agentenbasiertes System, das pro Inhalt neun GEO-Strategien bewertet und die Auswahl der besten mit einem Bandit-Verfahren beschleunigt. (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - Schlägt ein selbstlernendes agentenbasiertes GEO-System vor, das über statische Heuristiken und Umschreiben per Einzel-Prompt hinausgeht, um die Sichtbarkeit in zusammenfassenden Antworten zu erhöhen. (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - Formalisiert GEO als Strategieauswahl unter Berücksichtigung von Wettbewerbern und wählt Umschreibstrategien per Bayes'scher Optimierung über kombinatorische Strukturen. (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - Ermittelt, warum ein einzelnes Dokument von einer generativen Suchmaschine nicht zitiert wird, und behebt dies gezielt statt mit einheitlichen Umschreibregeln. (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - Behandelt GEO als Strategielernen, bei dem Planungs-, Bearbeitungs- und Bewertungsagenten wiederverwendbare Bearbeitungsstrategien über Aufgaben und Suchmaschinen hinweg herausarbeiten. (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - Löst widersprüchliche Überarbeitungswünsche aus vielen Suchanfragen mit einem Diverge-then-Converge-Framework, das Optimierungspräferenzen ermittelt und zu einer Überarbeitung zusammenführt. (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - Stellt GEO-SFE vor, ein Framework, das die Struktur von Inhalten auf mehreren Hierarchieebenen gestaltet, um zu beeinflussen, welche Seiten generative Suchmaschinen zitieren. (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - Stellt FeatGEO vor, das interpretierbare strukturelle, inhaltliche und sprachliche Merkmale von Seiten optimiert, um Zitationssichtbarkeit und Content-Qualität auszubalancieren. (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - Trainiert ein BART-base-Modell per Fine-Tuning mit synthetischen Textpaaren von Reise-Websites, um Inhalte für eine bessere Auffindbarkeit in LLM-Ausgaben umzuschreiben. (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - Optimiert Inhalte für generative Suchmaschinen ohne Kenntnis der Zielanfragen oder Rückmeldungen der Suchmaschine, indem Nutzerintentionen und -rollen vorab abgeleitet werden. (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - Stellt AutoGEO vor, das lernt, welche abgerufenen Inhalte generative Suchmaschinen bevorzugen, und Webseiten entsprechend umschreibt, um mehr Sichtbarkeit zu erzielen. (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - Stellt White-Hat-Techniken für Suchmaschinenoptimierung auf Basis generativer KI vor und berichtet über ihre empirisch gemessenen Verbesserungen. (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - Stellt GEO und einen Benchmark zur Messung der Sichtbarkeit von Inhalten in generativen Antworten vor. (2023)

### Benchmarks und Datensätze

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - Vergleicht Methoden für Conversational SEO über Aufgaben, Domänen und die Zahl der Anwender hinweg und stellt fest, dass die meisten wirkungslos sind und klassisches SEO oft besser funktioniert. (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - Bewertet Abwehrmaßnahmen gegen GEO-optimierte Dokumente mit gezielter Desinformation anhand manuell geprüfter Suchanfragen unter kontrollierten Bedingungen. (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - Stellt LIVE-GEO vor, um zu prüfen, ob GEO-Sichtbarkeitsgewinne im Live-Web standhalten, wo echte generative Suchmaschinen die Seiten abrufen und in eine Rangfolge bringen. (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - Stellt 13.746 Produktsuchanfragen von Verbrauchern samt abgerufenen Angeboten bereit, um GEO-Heuristiken zum Umschreiben mit mehreren generativen Suchmaschinen im E-Commerce zu testen. (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - Stellt ALCE vor, einen Benchmark mit automatischen Metriken für Flüssigkeit, Korrektheit und Zitationsqualität von LLM-Antworten, die abgerufene Belege zitieren. (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - Bewertet GEO-Angriffe zur Ranking-Manipulation nach einem einheitlichen Protokoll mit gemeinsamen Datensätzen und Metriken und vergleicht ihre Stärke und Erkennbarkeit. (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - Veröffentlicht einen Datensatz mit 11.500 Nutzeranfragen und vergleicht die Quellen und Informationen, die Google-Suche, AI Overviews und Gemini liefern. (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - Bietet eine Umgebung zur End-to-End-Bewertung suchgestützter GEO-Strategien, die neben der Generierung auch Retrieval und Ranking abdeckt. (2026)

### Angriffe und Manipulation

Forschung zu Adversarial GEO, also dazu, wie sich Antwortmaschinen etwa per Prompt-Injection oder Ranking-Angriffen manipulieren lassen und wie man sich dagegen schützt.

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - Stellt CORE vor, ein Optimierungsverfahren, das steuert, an welcher Position Produkte in LLM-generierten Produktempfehlungen erscheinen. (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - Prüft die Beweislage zu Manifesten im Stil von llms.txt für die KI-Suche, stellt kaum automatischen Abruf fest und bewertet ihre Sicherheitsfolgen. (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - Zeigt, dass GEO-Angriffe zu Zitationskriegen eskalieren können, die die Content-Qualität verschlechtern, und untersucht Mechanismusdesign für Win-win-Ergebnisse. (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - Zeigt, dass gemeinsam erstellte Bildperturbationen und Texte manipulieren können, wie Vision-Language-Modelle Produkte in eine Rangfolge bringen. (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - Warnt vor konzentriertem Einfluss, verdeckter kommerzieller Einflussnahme und blinden Flecken von Forschung und Industrie durch GEO und fordert Governance auf Antwortebene wie Offenlegung und Audits. (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - Schützt LLM-basierte Rankings, indem es die persuasive Struktur erkennt, die Händler in Inhalte einbetten, um ihre Produkte nach oben zu bringen. (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - Schützt generative Suche vor bösartigen GEO-Umschreibungen, die faktisch konsistent bleiben und dadurch Faktenprüfung und Perplexitätsfilter umgehen. (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - Modelliert Angriffe zur Ranking-Manipulation auf LLM-basierte Suchmaschinen als unendlich wiederholtes Gefangenendilemma und analysiert, wann Kooperation stabil bleiben kann. (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - Analysiert, welche Publisher generative Suchmaschinen zitieren und wie schwer es für Angreifer ist, schädliche Inhalte in die Quellen hinter den Antworten einzuschleusen. (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - Stellt einen Angriff vor, der mit energiebasierter Optimierung flüssige, schwer erkennbare Prompts erzeugt, um LLM-gestützte Rankings zu manipulieren. (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - Untersucht konkurrierende Poisoning-Angriffe auf RAG-Systeme, bei denen mehrere Angreifer dieselbe Suchanfrage zu unterschiedlichen Zielen lenken, und stellt den Benchmark PoisonArena vor. (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - Stellt Angriffe zur Präferenzmanipulation vor, die die Auswahl von LLMs auf Inhalte von Angreifern lenken, und zeigt, dass sie unter Händlern ein Gefangenendilemma erzeugen. (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - Untersucht SEO-artige Angriffe, bei denen manipulierte Textpassagen gezielt für den Abruf durch Dense-Embedding-Suche erstellt werden, die Retrieval-Schicht vieler RAG-Systeme. (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - Zeigt, dass eine gezielt erstellte strategische Textsequenz auf einer Produktseite eine LLM-basierte Suchmaschine dazu bringen kann, dieses Produkt an erster Stelle zu empfehlen. (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - Zeigt anhand echter Produktseiten, dass Prompt-Injections im Seitentext die Position einer Quelle in den Ergebnissen konversationeller Suchmaschinen verbessern können. (2024)

### Zitations- und Sichtbarkeitsanalysen

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - Berichtet über ein präregistriertes Feldexperiment (N = 1.100), nach dem das Entfernen von AI Overviews und AI Mode die Klicks auf Publisher-Seiten erhöht. (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - Untersucht in einem kausalen Audit, wie die Präsentation von Dokumenten beeinflusst, welche von zwei gleichermaßen stützenden Quellen eine agentenbasierte Suchmaschine zitiert. (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - Zeigt, dass Antworten der KI-Suche je nach Durchlauf, Prompt und Zeitpunkt variieren und Sichtbarkeit daher wiederholt statt einmalig gemessen werden muss. (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - Unterscheidet zwischen Zitationsauswahl und Zitationsabsorption und analysiert 602 Prompts in ChatGPT, Google AI und Perplexity. (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - Analysiert fast 35.000 Prompt-Beobachtungen und stellt fest, dass Markenerwähnungen stark zunehmen, sobald die eigene Domain einer Marke im Live-Retrieval auftaucht. (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - Untersucht, wie sich Markensichtbarkeit in ChatGPT, Claude, Perplexity und Gemini messen lässt und welche Quellen die Suchmaschinen beim Zitieren von Marken heranziehen. (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - Argumentiert, dass GEO-Sichtbarkeitswerte vom Prompt-Korpus und seiner Gewichtung abhängen, die einen Antwortmarkt definieren, der nicht der realen Nachfrage entsprechen muss. (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - Erfasst 55.393 Suchanfragen über 40 Tage, um zu messen, wann AI Overviews erscheinen, wie gut ihre Quellen sind, wie treu sie Aussagen wiedergeben und wie sie sich auf Publisher auswirken. (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - Beziffert, wie sich Google-Ergebnisse und Antworten generativer KI bei zitierten Domains, Domaintypen, Suchintention und Aktualität unterscheiden. (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - Prüft ChatGPT, Copilot, Google und Perplexity und stellt eine sehr geringe URL-Überschneidung zwischen den Suchmaschinen fest, die die Aussagekraft suchmaschinenunabhängiger GEO-Scores begrenzt. (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - Prüft vier generative Suchmaschinen anhand von 712 Suchanfragen und stellt fest, dass etwa 16 % der zitierten Quellen offenbar KI-generiert sind. (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - Zeigt anhand von Google AI Overviews und Reddit, dass KI-Suche das Engagement in zitierten Communities steigerte und dieser Effekt nach dem Start von AI Mode nachließ. (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - Beobachtet, wie vier Web-Einstellungen von ChatGPT Suchanfragen umschreiben, Seiten abrufen und Zitationen auswählen, wobei die Abrufhäufigkeit die Zitation vorhersagt. (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - Analysiert anhand von 614 Suchanfragen Zitationsverhalten, Quellenzuordnung und Sichtbarkeit von Entitäten auf vier chinesischsprachigen generativen Suchplattformen. (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - Analysiert 158.099 Antworten und zeigt, dass die Seiten, die ChatGPT für seine umgeschriebenen Teilanfragen abruft, Zitationen weit besser erklären als Seiteneigenschaften. (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - Führt ein Seiten-Audit mit 16 Säulen ein und zeigt, dass Metadaten, semantisches HTML und strukturierte Daten bei drei Suchmaschinen am stärksten mit Zitationen zusammenhängen. (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - Vergleicht KI-Suchmaschinen in kontrollierten Experimenten über Branchen und Sprachen hinweg mit Google und stellt eine starke Bevorzugung von Earned Media gegenüber markeneigenen Inhalten fest. (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - Entwickelt ConflictingQA und zeigt damit, dass LLMs stark auf die Relevanz einer Seite für die Anfrage achten, stilistische Signale wie wissenschaftliche Quellenangaben aber weitgehend ignorieren. (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - Prüft Bing Chat, NeevaAI, Perplexity und YouChat auf Recall und Precision der Zitationen und stellt fest, dass viele Aussagen nicht vollständig durch Quellen belegt sind. (2023)

### Übersichtsarbeiten

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - Wertet 45 Studien von 2023 bis 2026 aus, beschreibt GEO als mehrstufige stochastische Pipeline und bietet eine Checkliste zur Bewertung von GEO-Behauptungen. (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - Ordnet LLM-basierte Suchagenten systematisch nach Architektur, Optimierung, Anwendung und Evaluation und benennt offene Herausforderungen. (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - Übersichtsarbeit zu generativer Suche und Empfehlung mit großen Sprachmodellen aus technischer Sicht. (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - Untersucht, wie Suchmaschinen und LLMs voneinander profitieren können, sowohl durch Suche zur Verbesserung von LLMs als auch durch LLMs zur Verbesserung der Suche. (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - Übersichtsarbeit zum Einsatz großer Sprachmodelle in Information-Retrieval-Systemen, darunter Umschreiben von Suchanfragen, Retrieval, Reranking und Lesen. (2023)

## Leitfäden und Artikel

### Strategie

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - Praxisnahe Einführung dazu, wie Generative Engine Optimization Inhalten zu Sichtbarkeit in KI-gestützten Suchergebnissen verhilft. (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - Erklärt, was GEO ist, wie es sich von SEO unterscheidet und welche Techniken Inhalten zu Zitationen in KI-Antworten verhelfen, mit einer Audit-Checkliste zum Herunterladen. (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - Erklärt, wie sich KI-Suche von klassischer Suche unterscheidet, stellt fünf GEO-Taktiken vor und zeigt, wie sich GEO-Erfolg messen lässt, wobei KI-Suche weiterhin auf klassischer Suche aufbaut. (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - Argumentiert, dass sich die Suche von linkbasiertem Ranking hin zu Antworten von Sprachmodellen verlagert, und sieht GEO als nächste Phase des rund 80 Milliarden US-Dollar schweren SEO-Markts. (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - Stellt SEEN vor, ein GEO-Framework aus vier Schichten (Structure, Evidence, Entity, Notability) mit 41 Checklistenpunkten, die je mit 0 oder 1 bewertet werden, um die schwächste Schicht zu finden. (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - Beschreibt einen GEO-Prozess in zehn Schritten, von der Wahl prioritärer Themen und einer Ausgangsbasis über die Auswertung zitierter Quellen bis zur Content-Optimierung und Ergebnisberichterstattung. (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - Auftakt eines achtteiligen AEO-Leitfadens: Unterschiede zu SEO, Funktionsweise von Antwortmaschinen, Monitoring der KI-Sichtbarkeit, Prompt-Auswahl und Korrektur von Fehlern in KI-Antworten. (2025)

### Content-Erstellung

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - Erklärt, was Googles AI Overviews sind, wie sie aus Webquellen entstehen und wie Website-Betreiber dafür optimieren und ihre Sichtbarkeit darin erfassen können. (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - Beschreibt einen zweistufigen Weg zu Zitationen in ChatGPT (abgerufen werden, dann zitierfähig sein), gestützt auf eigene Messungen der Autoren, etwa welche zitierten Domains KI-Crawler zulassen. (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - Berichtet, was 13 Tests mit Käuferfragen in ChatGPT und die Serverlogs der Website zeigten, darunter ein negatives Ergebnis, und welche KI-Bots zugelassen werden sollten. (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - Beschreibt sieben Schritte, damit KI-Suchmaschinen wie ChatGPT und Google Inhalte zitieren, von der Keyword-Recherche bis zur Formatierung. (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - Nennt acht Schritte für bessere Rankings in der ChatGPT-Suche, die Inhalte für KI-Systeme leicht extrahierbar machen und externen Konsens aufbauen. (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - Nennt zehn Wege, die Sichtbarkeit einer Marke in LLM-generierten Antworten zu verbessern, eingeordnet als LLM-Optimierung (LLMO). (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - Microsoft-Advertising-Leitfaden zu nutzbaren Inhalten für KI-Suchantworten, etwa Schema-Markup, Überschriften und eigenständige Q&A-Blöcke, und zu Fehlern wie in Tabs oder PDFs versteckten Antworten. (2025)

### Technische Umsetzung

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - Berichtet über eine Untersuchung, nach der clientseitig eingefügtes JSON-LD, etwa über den Google Tag Manager, von KI-Crawlern ohne JavaScript-Ausführung übersehen wird. (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - Zeigt, wie sich Referral-Traffic aus KI-Tools wie ChatGPT und Gemini in Google Analytics 4 erfassen lässt. (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - Stellt die Auslieferung von Seiten als Markdown an KI-Agenten vor und zeigt die Token-Ersparnis, wobei ein Beitrag von 16.180 Tokens in HTML auf 3.150 in Markdown sinkt. (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - Stellt Daten von MERJ und Vercel dazu vor, wie ChatGPT, Claude und andere KI-Crawler mit JavaScript und Inhaltstypen umgehen, mit Empfehlungen für Website-Betreiber. (2024)

### Branchenberichte und Daten

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - Schätzt anhand von 3.000 Websites, wie viel Traffic KI-Chatbots liefern, und ermittelt, dass 63 % der Websites solchen Traffic erhalten und drei Chatbots 98 % davon ausmachen. (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - Erweitert Cloudflare Radar um branchenbezogene Daten und eine Aufschlüsselung des KI-Bot-Traffics nach Crawl-Zweck. (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - Analysiert 31 Millionen KI-Zitationen und die robots.txt-Dateien von 105 Publishern und stellt fest, dass das Blockieren von KI-Crawlern bei manchen Modellen wirkt und bei anderen nicht. (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - Wertet Daten aus 16 Monaten aus und zeigt, dass die Überschneidung von AI-Overview-Zitationen mit organischen Rankings von 32 % auf 54 % stieg, aufgeschlüsselt nach Branchen. (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - Stellt eine Ahrefs-Studie vor, nach der AI Overviews die Klicks um 34,5 % senken, entgegen Googles Aussage, sie würden die Klicks steigern. (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - Testet acht KI-Suchtools mit Auszügen aus Nachrichtenartikeln und stellt fest, dass sie bei mehr als 60 % der Anfragen Quellen falsch zitieren. (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - Sammelt Similarweb-Daten aus dem Jahr 2026 zu Marktanteilen von ChatGPT, Gemini und Claude, Referral-Traffic, Zitationen und Werbung in KI-Antworten. (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - Analysiert 75.000 Marken, um zu ermitteln, welche Suchfaktoren Markenerwähnungen in AI Overviews am wahrscheinlichsten beeinflussen. (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - Vergleicht das Verhalten von Google-Nutzern im März 2025 und stellt fest, dass Personen, die eine KI-Zusammenfassung sahen, seltener auf Links zu anderen Websites klickten. (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - Erfasst 37.500 Zitationen in ChatGPT, Gemini, Copilot und Google und stellt fest, dass die Hälfte am nächsten Tag verschwindet und die meisten wieder auftauchen. (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - Untersucht 300.000 Domains darauf, wie verbreitet llms.txt ist und ob die Datei beeinflusst, wie oft eine Domain von LLMs zitiert wird. (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - Analysiert rund 7 Milliarden Logdateien von November 2024 bis März 2026, um zu zeigen, wie die drei Crawler von OpenAI mit dem Web interagieren. (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - Berichtet über einen Anstieg der Nachrichtenanfragen in ChatGPT um 212 % und einen Rückgang des Publisher-Traffics um 26 %, während generative KI die Nachrichtenbranche umgestaltet. (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - Analysiert mehr als 10 Millionen Keywords, um zu zeigen, wie Googles AI Overviews die Suche verändern und was das für SEO bedeutet. (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - Ermittelt anhand von 863.000 SERPs, dass 38 % der Zitationen in AI Overviews von Seiten aus den Top 10 stammen, gegenüber 76 % ein Jahr zuvor. (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - Beobachtet 1.885 Seiten, die JSON-LD ergänzt haben, und misst die Auswirkung auf Zitationen in Google AI Overviews, AI Mode und ChatGPT. (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - Zeigt anhand von 1,4 Millionen Prompts, wie Seitentitel, URLs und Snippets beeinflussen, welche abgerufenen Seiten ChatGPT zitiert. (2026)

## Standards und Spezifikationen

Spezifikationen und offizielle Dokumentation dazu, wie KI-Crawler auf eine Website zugreifen und wie Antwortmaschinen ihre Inhalte auslesen.

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - Enthält den Quelltext des llms.txt-Vorschlags samt Referenz-Tooling und Diskussion.
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - Berichtet, dass John Mueller llms.txt derzeit als spekulativ bezeichnet und WebMCP bevorzugt, eine von Google unterstützte Alternative.
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - Berichtet über die Aussage von John Mueller, dass laut Serverlogs derzeit kein KI-System llms.txt nutzt. (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - Verzeichnis von Websites, die llms.txt umsetzen, mit Beispieldateien für APIs, Plattformen und Entwicklertools.
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - Misst in einer Studie vom September 2026 die Verbreitung von llms.txt unter den Top-1.000- und Top-10.000-Domains, mit Methodik und Daten zum Herunterladen. (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - Listet Websites auf, die eine llms.txt-Datei veröffentlichen, sodass Entwickler reale Beispiele des Formats durchsehen können.
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - Listet Websites auf, die llms.txt veröffentlichen, und zeigt die dort erklärten KI-Berechtigungen für Training, Retrieval und Zusammenfassung.
- [The /llms.txt file](https://llmstxt.org) 🆓 - Schlägt eine Markdown-Datei /llms.txt im Stammverzeichnis einer Website vor, die Sprachmodellen einen kuratierten Überblick über die Website und Links zu ihren nützlichsten Inhalten bietet. (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - Plädiert mit Beispielen von Vercel, Google und Anthropic für llms.txt und antwortet Kritikern, die allgemeine SEO-Praxis für ausreichend halten. (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - Erklärt, was die llms.txt-Datei ist, und prüft, ob sie Entwicklern und Marketern tatsächlich etwas bringt.

### KI-Crawler und robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - Listet 25 User-Agents von KI-Crawlern von 12 Betreibern in vier Gruppen auf und zeigt, wie viele von 157 Plattformen jeden davon per robots.txt blockieren. (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - Sammelt bekannte robots.txt-Einträge, Meta-Tags und weitere Einstellungen, mit denen Website-Betreiber dem KI-Training widersprechen können.
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - Pflegt eine Community-Liste zu blockierender KI-Agenten und -Crawler samt generierten robots.txt- und Serverkonfigurationsdateien.
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - Beschreibt Amazonbot, Amzn-SearchBot und Amzn-User sowie die voneinander unabhängigen robots.txt-Einstellungen, mit denen sich jeder einzeln steuern lässt.
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - Erklärt, wie Website-Betreiber KI-Crawlern mit Pay Per Crawl den Zugriff in Rechnung stellen und unbezahlte Anfragen mit HTTP 402 beantworten; die Funktion ist in einer geschlossenen Beta.
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - Listet die Google-Fetcher auf, die auf Anfrage von Nutzern tätig werden, etwa Google Read Aloud, und weist darauf hin, dass sie robots.txt-Regeln in der Regel ignorieren.
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - Dokumentiert die gängigen Google-Crawler, darunter Googlebot, mit ihren User-Agent-Strings und robots.txt-Tokens.
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - Listet rund 40 User-Agents der Yandex-Robots mit Zweck und Verhalten gegenüber robots.txt auf und erklärt, wie sie sich per Reverse-DNS verifizieren lassen.
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - Standardisiert ein gemeinsames Vokabular und Einbindungswege wie robots.txt und HTTP-Header, um Präferenzen zur Erfassung und Nutzung von Inhalten durch KI auszudrücken.
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - Standardisiert Verfahren zur kryptografischen Authentifizierung automatisierter Clients wie KI-Crawler und -Agenten als Ersatz für IP-Allowlists und User-Agent-Strings.
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - Erklärt, dass DuckAssistBot Quellen für die KI-gestützten Antworten von DuckDuckGo sammelt, nicht für KI-Training genutzt wird und per robots.txt blockiert werden kann.
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - Listet die Crawler von Meta auf, darunter Meta-WebIndexer für die Meta-AI-Suche und Meta-ExternalAgent für das Training von KI-Modellen, und wofür jeder genutzt wird.
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - Beschreibt die User-Agents MistralAI-User, MistralAI-Index und MistralAI-Training und wofür jeder genutzt wird.
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - Spezifiziert Syntax und Semantik von robots.txt, dem Robots Exclusion Protocol, das KI-Crawler einhalten sollen. (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - Kündigt an, dass Google einen gemeinsamen Opt-out für KI-Training in robots.txt auf Basis eines IETF-AIPREF-Entwurfs respektieren will, mit geplanter Unterstützung ab 2027. (2026)

### Strukturierte Daten

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - Erklärt, wie Google strukturierte Daten nutzt, um Inhalte zu verstehen, welche Formate unterstützt werden und wo das Markup platziert werden sollte.
- [JSON-LD](https://json-ld.org) 🆓 - Enthält die Spezifikationen von JSON-LD, dem JSON-basierten Linked-Data-Format, in dem Schema.org-Markup meist geschrieben wird.
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - Testet eine URL oder ein Code-Snippet und zeigt, welche Rich-Suchergebnisse von Google die enthaltenen strukturierten Daten erzeugen können.
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - Fasst einen Ahrefs-Bericht zusammen, der testete, ob Schema-Markup auf bereits von KI zitierten Seiten deren Zitationsraten verbessert. (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - Validiert strukturierte Daten beliebiger Schema.org-Typen in JSON-LD, Microdata oder RDFa.
- [Schema.org](https://schema.org) 🆓 - Enthält das gemeinsame Vokabular aus Typen und Eigenschaften, mit dem Webseiten für Suchmaschinen und andere Anwendungen annotiert werden.
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - Enthält den Quelltext des Schema.org-Vokabulars und die zugehörige Software.
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - Katalogisiert die Typen strukturierter Daten, auf denen Funktionen der Google-Suche beruhen, mit Beispielen und Hinweisen zur Implementierung.

### Offizielle Dokumentation der Anbieter

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - Beschreibt Applebot, der Suchfunktionen in Spotlight, Siri und Safari speist, und Applebot-Extended, den Publisher sperren können, um dem Training generativer KI zu widersprechen.
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - Erklärt, wie AI Overviews und AI Mode in der Google-Suche funktionieren und wie Website-Betreiber die Aufnahme ihrer Inhalte dort angehen können.
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - Webmaster-Plattform von Baidu mit Einreichung von Website-Ressourcen, Crawl- und robots-Daten, Such-Widgets und Analyse des KI-Traffics.
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - Beschreibt CCBot, den Crawler hinter dem offenen Webarchiv Common Crawl, mit seinem User-Agent und Möglichkeiten, ihn zu verifizieren und zu blockieren.
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - Beschreibt die Crawler ClaudeBot, Claude-User und Claude-SearchBot und wie Website-Betreiber jeden davon per robots.txt blockieren können.
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - Dokumentiert das IndexNow-Protokoll, mit dem teilnehmende Suchmaschinen über neue, geänderte oder gelöschte URLs benachrichtigt werden.
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - Kündigt einen Bericht in den Bing Webmaster Tools an, der zeigt, wann eine Website in Antworten von Microsoft Copilot und in KI-generierten Zusammenfassungen von Bing zitiert wird. (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - Kündigt Berichte in der Search Console an, die zeigen, wie oft Seiten in generativen KI-Funktionen wie AI Overviews und AI Mode erscheinen, nach Seite, Land, Gerät und Datum. (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - Kündigt das Programm an, über das Perplexity Einnahmen mit teilnehmenden Publishern teilt und sie mit API-Zugang und Entwicklerhilfe unterstützt. (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - Webmaster-Leitfaden und Tools von Naver dazu, was eine Website braucht, damit die Naver-Suche sie findet und indexiert; AI Briefing greift auf Webdokumente aus demselben Index zurück.
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - Beschreibt die User-Agents OAI-SearchBot, GPTBot, ChatGPT-User und OAI-AdsBot und wofür jeder genutzt wird.
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - Beschreibt PerplexityBot, der Websites in den Suchergebnissen von Perplexity sichtbar macht, und Perplexity-User, der Seiten auf Nutzeranfrage abruft und robots.txt in der Regel ignoriert.
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - Beantwortet Fragen von Publishern und Entwicklern zur Präsenz in der ChatGPT-Suche, zum Crawler OAI-SearchBot und zu Referral-Traffic aus ChatGPT.
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - Erklärt die Search-Console-Einstellung, die Inhalte in AI Overviews, AI Mode und generativer KI in Discover ein- oder ausschließt, und betont, dass sie das KI-Training nicht betrifft.
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Hilfeseite von Yandex, die erklärt, wie die KI-Antworten eine Frage in Teile zerlegen, Quellen auswählen und analysieren und in der Antwort auf sie verlinken.
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Fasst Googles empfohlene Vorgehensweisen zusammen, damit Inhalte in den KI-Funktionen der Google-Suche gut abschneiden. (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Webmaster-Dienst von Yandex zum Verifizieren von Websites, zum Monitoring der Indexierung und zur Diagnose von Crawl-Problemen in der Yandex-Suche.
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - Kündigt getrennte Publisher-Einstellungen für KI-Training und KI-Grounding an, die per robots.txt, Meta-Tags oder X-Robots-Tag-Header gesetzt und von Microsoft ab Februar 2027 ausgewertet werden. (2026)

## Tools

### KI-Sichtbarkeits-Monitoring

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - Prüft ohne Registrierung, wie ChatGPT, Gemini, Perplexity, Copilot und AI Overviews eine Marke erwähnen und als Quelle zitieren.
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - Zeigt, wie oft eine Marke in Antworten von Google AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini und Copilot vorkommt, auf Basis einer Prompt-Datenbank oder eigener Prompts.
- [AthenaHQ](https://athenahq.ai) 🪙 - Erfasst die Markensichtbarkeit in KI-Modellen wie ChatGPT, Perplexity, Gemini, AI Overviews und Copilot und schlägt Content-Änderungen vor; der kostenlose Plan enthält ein Startguthaben.
- [Geoptie](https://geoptie.com) 💲 - Zeigt, wie ChatGPT, Gemini, Claude, Perplexity und Google AI auf Prompts von Kaufinteressenten antworten und welche Quellen sie zitieren.
- [Goodie](https://higoodie.com) 💲 - Erfasst die Markensichtbarkeit in KI-Suchmaschinen wie ChatGPT, AI Overviews, Perplexity und Copilot und empfiehlt Optimierungen, in höheren Tarifen mit weiteren Suchmaschinen.
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - Bewertet in einer kostenlosen einmaligen Prüfung, wie ChatGPT, Perplexity und Gemini eine Marke beschreiben; wöchentliches Monitoring wird als kostenpflichtiges HubSpot AEO angeboten.
- [Knowatoa](https://www.knowatoa.com) 💲 - Erfasst die Markensichtbarkeit in ChatGPT, Google AI Overviews, AI Mode und weiteren KI-Suchdiensten, mit Prompt-Monitoring und Integrationen für das Reporting.
- [Otterly.AI](https://otterly.ai) 💲 - Überwacht Markenerwähnungen und Zitationen von Websites in ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity und Copilot, mit Wettbewerbsvergleich und Prompt-Recherche.
- [Peec AI](https://peec.ai) 💲 - Erfasst Sichtbarkeit, Position und Stimmung einer Marke in KI-Suchplattformen wie ChatGPT, Perplexity, AI Overviews, AI Mode und Gemini, mit Berichten auf Prompt-Ebene.
- [Profound](https://www.tryprofound.com) 💲 - Erfasst die Markensichtbarkeit in Antwortmaschinen wie ChatGPT, Perplexity, Google AI Mode, Gemini und Claude über tägliche Prompt-Durchläufe und Zitationsanalysen.
- [Promptwatch](https://promptwatch.com) 💲 - Erfasst die Markensichtbarkeit in KI-Modellen wie ChatGPT, Google AI Overviews, Perplexity, Claude und Gemini durch das Ausführen von Prompts, in höheren Tarifen mit Analysen zu KI-Crawlern.
- [Rankscale](https://rankscale.ai) 💲 - Erfasst Markenerwähnungen und Zitationen in mehr als 17 KI-Suchmaschinen in Credit-basierten Tarifen, mit Marken-Dashboards und einer API in höheren Tarifen.
- [Scrunch](https://scrunch.com) 💲 - Überwacht Prompts, Zitationen, Wettbewerber-Rankings und Crawl-Aktivität von KI-Bots auf großen KI-Plattformen und kann eine für KI optimierte Version einer Website ausliefern.
- [Searchable](https://www.searchable.com) 💲 - Erfasst Markenerwähnungen, Wettbewerbsvergleiche und zitierte Quellen in ChatGPT, Google AI Overviews und Perplexity; Claude, Gemini und weitere KI-Suchmaschinen sind kostenpflichtig zubuchbar.
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - Erfasst Markenerwähnungen und Sichtbarkeit in ChatGPT, Google AI Mode und weiteren KI-Plattformen per Prompt- und Wettbewerbs-Monitoring, enthalten in den Semrush-Tarifen SEO plus AI Search.
- [Trakkr](https://trakkr.ai) 💲 - Erfasst per Prompt-Monitoring, wie eine Marke in acht KI-Modellen erscheint, im höheren Tarif mit Plänen für mehrere Marken und Kundenportalen.
- [Waikay](https://waikay.io) 🪙 - Analysiert, wie ChatGPT, Google, Claude und Perplexity eine Marke beschreiben, weist auf Halluzinationen und Wissenslücken hin und schlägt Maßnahmenpläne vor.
- [Writesonic](https://writesonic.com) 💲 - Überwacht die Markensichtbarkeit in KI-Antworten, in niedrigeren Tarifen für ChatGPT, Gemini und Google AI Overviews, ergänzt um Artikelerstellung und Korrekturen aus Website-Audits.
- [ZipTie](https://ziptie.ai) 💲 - Erfasst ausgewählte Prompts in sieben Suchmaschinen, darunter ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity und Copilot, mit nutzungsbasierter Abrechnung pro Prüfung.

### Content-Audit und -Optimierung

- [Clearscope](https://www.clearscope.io) 💲 - Empfiehlt Content-Verbesserungen für Google und KI-Antworten und erfasst Suchanfragen in ChatGPT und Gemini, um zu zeigen, wann eine Marke erwähnt wird.
- [Frase](https://www.frase.io) 💲 - Bewertet Inhalte für SEO und GEO und überwacht die Markensichtbarkeit in KI-Suchmaschinen wie ChatGPT und Google AI, in höheren Tarifen mit weiteren Suchmaschinen.
- [GeoReady](https://geoready.dev) 🪙 - Prüft, ob ChatGPT, Perplexity, Claude und Gemini eine Website erreichen, lesen und zitieren können, und bewertet sie mit bis zu 100 Punkten in neun Kategorien samt priorisierten Korrekturen.
- [NEURONwriter](https://neuronwriter.com) 💲 - Schlägt anhand der Seiten mit den besten Rankings Begriffe und Struktur vor, um Inhalte für Google und KI-Antworten zu optimieren, und überwacht den Share of Voice einer Marke in KI-Modellen.
- [Surfer](https://surfer.ai) 💲 - Kombiniert einen Content-Editor, der Entwürfe im Vergleich zu Wettbewerbern bewertet, mit einem AI Tracker für Markenerwähnungen in ChatGPT, Perplexity, Gemini, AI Overviews und AI Mode.

### Open-Source-Tools und -Bibliotheken

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - Auf Agenten ausgerichtete Plattform für die Arbeit an AEO und GEO, die als npm-Paket ausgeliefert wird.
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - Selbst hostbare Plattform, die erfasst, wie ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok und Google AI Overviews eine Marke erwähnen und als Quelle zitieren.
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - Führt Prompts nach Zeitplan über mehrere LLM-Anbieter aus, erfasst deren Zitationen aus der Websuche und überwacht Markenerwähnungen über ein Dashboard und eine CLI.
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - Bewertet eine Website auf einer Skala von 0 bis 100 danach, ob KI-Suchmaschinen sie crawlen, verstehen und zitieren können, per CLI, Python-Bibliothek und MCP-Server.
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - Erfasst, wie ChatGPT, Perplexity, Gemini und Google AI Mode eine Marke erwähnen und als Quelle zitieren, als selbst gehostetes Dashboard mit MCP-Server und CLI.
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - Prüft, ob eine Website für KI-Crawler erreichbar und lesbar ist, und vergibt eine Bewertung, als PyPI-Paket und GitHub Action.
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - Stellt ein erweiterbares Go-Framework für GEO mit integrierten Strategien bereit, in dem sich eigene Strategien registrieren lassen.
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - Deterministischer Content-Linter für CI oder Pre-Commit, der Probleme bei Struktur und Quellenangaben in Dokumentationen und statischen Websites meldet, veröffentlicht als npm-Paket.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - Open-Source-Plattform, um die Präsenz einer Marke in KI-Antworten zu erfassen und zu verbessern.
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - Selbst gehostetes Monitoring-Tool als einzelnes Go-Binary mit SQLite und MCP-Server, das festhält, wie große KI-Suchmaschinen eine Marke erwähnen und zitieren.
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - NGINX-Modul, das KI-Agenten per HTTP-Content-Negotiation Markdown-Versionen von Seiten ausliefert.
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - Selbst hostbares Tool, das über die Produktoberflächen überwacht, wie ChatGPT, Perplexity, Gemini, Claude und Google AI Overviews eine Marke erwähnen und als Quelle zitieren.
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - Bewertet eine Website auf einer Skala von 0 bis 100 nach ihrer Lesbarkeit für Agenten und erzeugt Markdown-Kopien der Seiten sowie robots.txt, llms.txt und sitemap.xml.
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - Typgeprüftes Schema.org-JSON-LD für React.
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - TypeScript-Typen zum Schreiben von Schema.org-JSON-LD.
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - Erzeugt einen Schema.org-JSON-LD-Graphen für JavaScript-Websites, mit einer Astro-Integration.
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - Fluent Builder in PHP für Schema.org-Typen, der JSON-LD ausgibt.

### llms.txt-Generatoren

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - Erzeugt beim Build llms.txt, JSON-LD, Markdown-Kopien und Regeln für KI-Crawler für Websites mit Vite, Astro, Next.js und Nuxt und validiert sie.
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - Apify-Actor, der eine Website crawlt und ihre Inhalte extrahiert, um eine llms.txt-Datei zu erstellen.
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - Crawlt eine Website, um eine llms.txt-Datei zu entwerfen, mit Seitenerkennung, ergänztem Unternehmenskontext und täglicher Aktualisierung der öffentlichen Datei.
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - Kommandozeilen-Tool, das eine sitemap.xml in eine llms.txt-Datei umwandelt.
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - MkDocs-Plugin, das eine /llms.txt-Datei für eine Dokumentationswebsite erzeugt.
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - Nuxt-Modul, das automatisch eine /llms.txt-Dokumentation in Markdown für eine Anwendung erzeugt.
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - Sphinx-Erweiterung, die eine llms.txt-Datei erzeugt.
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - VitePress-Plugin, das LLM-freundliche Dokumentationsdateien erzeugt.
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - Erstellt ohne Registrierung einen llms.txt-Entwurf aus einer öffentlichen Startseite, indem bis zu 30 über Sitemap und interne Links gefundene Seiten geprüft werden.
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - Erzeugt und aktualisiert im kostenlosen Plugin Yoast SEO automatisch eine llms.txt-Datei, wobei die wichtigsten Inhalte automatisch oder manuell ausgewählt werden.

### Crawler-Log-Analyse

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - Kuratierte Liste von User-Agents der KI-Crawler mit einer Node-CLI und einer GitHub Action, die robots.txt prüfen, die Erreichbarkeit testen und Access-Logs auswerten.
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - Zeigt, welche KI-Dienste eine Website crawlen, ermöglicht das Zulassen oder Blockieren jedes einzelnen Crawlers und meldet, welche Crawler robots.txt einhalten; in allen Cloudflare-Tarifen verfügbar.
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - Cloudflare Worker, der Traffic von KI-Crawlern und LLM-Bots am Edge erkennt und erfasst.
- [Known Agents](https://knownagents.com) 🪙 - Bietet ein Verzeichnis von KI-Agenten und Bots, einen robots.txt-Checker und Agent-Analytics, mit einem kostenlosen Plan für bis zu 100.000 Ereignisse pro Monat.

## KI-Suchmaschinen und -Assistenten

KI-Antwortmaschinen nach Region, soweit verfügbar mit offizieller Website, Webmaster-Dokumentation und bekannten Crawler-User-Agents.

### International

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Konversationeller Suchmodus von Microsoft Bing, früher Copilot Search, der 2026 in AI Mode und die in den regulären Ergebnissen angezeigten AI-Overview-Zusammenfassungen aufgeteilt wurde.
- [Brave Search](https://brave.com/search/) 🪙 - Suchmaschine von Brave auf Basis eines eigenen, unabhängigen Index mit Answer with AI, das Zusammenfassungen mit Quellenangaben erstellt, und dem Chatmodus Ask Brave für Folgefragen.
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - ChatGPT von OpenAI mit integrierter Websuche, das Fragen im Gespräch beantwortet und die genutzten Seiten verlinkt.
- [Claude](https://claude.ai) 🪙 - Claude-Assistent von Anthropic, der während eines Gesprächs im Web suchen und die Seiten hinter seiner Antwort zitieren kann.
- [Duck.ai](https://duck.ai) 🪙 - Anonymisierter Chat von DuckDuckGo mit KI-Modellen von Drittanbietern, erreichbar aus den Suchergebnissen; die DuckDuckGo-Suche bietet zudem optionale KI-gestützte Antworten.
- [Gemini](https://gemini.google.com) 🪙 - KI-Assistent Gemini von Google, der für aktuelle Informationen in seinen Antworten auf die Google-Suche zurückgreift.
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Konversationeller Modus der Google-Suche auf Basis von Gemini, der komplexe Fragen beantwortet, Folgefragen zulässt und auf Quellen im Web verlinkt.
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Generative Zusammenfassungen der Google-Suche über den regulären Ergebnissen, mit Links zu den verwendeten Quellen, verfügbar in mehr als 120 Ländern und Gebieten.
- [Grok](https://grok.com) 🪙 - KI-Assistent von xAI, inzwischen Teil von SpaceX, der im Web und in Beiträgen auf X sucht, um Fragen zu aktuellen Ereignissen zu beantworten.
- [Kagi Assistant](https://kagi.com/assistant) 💲 - Chat-Assistent von Kagi für zahlende Mitglieder, der Modelle vieler Anbieter mit optionalem Zugriff auf die werbefreien Suchergebnisse von Kagi kombiniert.
- [Meta AI](https://www.meta.ai) 🪙 - KI-Assistent von Meta im Web und in WhatsApp, Instagram und Facebook, der für aktuelle Fragen Ergebnisse der Websuche einbeziehen kann.
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Copilot-Assistent von Microsoft für Privatnutzer, der Fragen mithilfe von Bing-Webergebnissen beantwortet und die herangezogenen Seiten zitiert.
- [Perplexity](https://www.perplexity.ai) 🪙 - KI-Antwortmaschine, die das Web in Echtzeit durchsucht und Antworten im Dialogstil mit nummerierten Quellenangaben liefert.

### China

- [ChatGLM](https://chatglm.cn) 🆓 - Chinesischer Assistent von Zhipu AI auf Basis der eigenen GLM-Modelle, mit Websuche und Agentenfunktionen.
- [DeepSeek](https://www.deepseek.com) 🆓 - Chat-Assistent von DeepSeek auf Basis der eigenen Open-Weight-Modelle mit optionalem Websuchmodus für aktuelle Antworten.
- [Doubao](https://www.doubao.com) 🆓 - Universeller KI-Assistent von ByteDance, der für Antworten im Chat im Web sucht und die herangezogenen Quellen auflistet.
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - Assistent ERNIE Bot von Baidu (früher Wenxin Yiyan), der im Web inzwischen als Baidu Wenxin Assistant läuft und an die Baidu-Suche angebunden ist.
- [Kimi](https://www.kimi.com) 🪙 - Kimi-Assistent von Moonshot AI, bekannt für das Lesen langer Kontexte, der im Web sucht und die gelesenen Seiten zitiert.
- [Metaso](https://metaso.cn) 🪙 - Werbefreie chinesische KI-Suchmaschine von MetaSOTA, die Fragen mit Quellenangaben beantwortet und auch wissenschaftliche Literatur durchsuchen kann.
- [Quark](https://www.quark.cn) 🪙 - Quark von Alibaba, eine Such- und Browser-App, die rund um einen KI-Assistenten neu aufgebaut wurde und Suchanfragen mit generierten Ergebnissen beantwortet.
- [Qwen](https://www.qianwen.com) 🆓 - Qwen-App von Alibaba (früher Tongyi), ein KI-Assistent auf Basis der eigenen Qwen-Modelle mit Websuche; die internationale Webversion heißt Qwen Chat.
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - KI-Assistent von Tencent, der mit Ergebnissen der Websuche antwortet, darunter Artikel aus WeChat Official Accounts.
- [Yuanbao Search](https://so.qq.com) 🆓 - KI-Websuche von Tencent, die ihre Quellen angibt, Inhalte aus WeChat Official Accounts und Channels durchsuchen kann und einen KI-Modus für Folgefragen bietet.

### Japan

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - KI-Agent der LY Corporation, im April 2026 aus dem AI Assistant der Suche von Yahoo! JAPAN und LINE AI zusammengeführt und über das Suchfeld von Yahoo! JAPAN und LINE aufrufbar.
- [Felo](https://felo.ai) 🪙 - Mehrsprachige KI-Suchmaschine eines Tokioter Start-ups, die mit Quellenangaben antwortet und sprachübergreifend nach Quellen suchen kann.

### Südkorea

- [A. (A-dot)](https://adot.ai) 🆓 - Persönlicher KI-Assistent von SK Telecom mit einer gemeinsam mit Perplexity entwickelten KI-Suchfunktion und mehreren Chatmodellen.
- [Kanana](https://kanana.ai) 🆓 - KI-Marke von Kakao mit dem Assistenten Kanana in KakaoTalk und den Kanana-Modellen als Open Source; im Oktober 2026 wurde der auf KakaoTalk basierende Agent Kanana Space angekündigt.
- [Liner](https://liner.com) 🪙 - KI-Such- und Rechercheassistent eines Unternehmens aus Seoul mit Fokus auf Antworten mit Quellenangaben und wissenschaftliche Quellen.
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - Generative Antworten der Naver-Suche auf Basis von HyperCLOVA X, die Ergebnisse oben auf der Seite zusammenfassen und die verwendeten Quellinhalte anzeigen.
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - Konversationeller KI-Suchtab von Naver, seit Juni 2026 für alle Nutzer geöffnet, der im Dialog mit Infokarten zu Produkten, Orten und Buchungen antwortet.
- [Wrtn](https://wrtn.ai) 🆓 - Koreanischer KI-Assistent von Wrtn Technologies mit kostenloser KI-Suchfunktion, die auf Basis aktueller Webergebnisse antwortet und ihre Quellen auflistet.

### Europa

- [Ecosia AI search](https://www.ecosia.org) 🆓 - KI-Suchfunktionen von Ecosia, der Berliner Suchmaschine, die Baumpflanzungen finanziert; Nutzer können sie für Ergebnisse ohne KI abschalten.
- [Lumo](https://lumo.proton.me) 🪙 - Datenschutzorientierter KI-Assistent von Proton mit Sitz in der Schweiz, der eine integrierte Websuche bietet und Anfragen nicht für zielgerichtete Werbung nutzt.
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - KI-Assistent von Mistral AI, der von Le Chat in Vibe umbenannt wurde und einen Chat mit Websuche und einen Coding-Agenten verbindet.

### Weitere Regionen

- [Alice AI](https://alice.yandex.ru) 🆓 - Assistent Alice AI von Yandex, dessen Modelle auch die KI-Antworten mit Quellenlinks in der Yandex-Suche erzeugen.

## GEO-Ressourcen in weiteren Sprachen

Artikel, Communities und lokale Tools in anderen Sprachen als Englisch; Agenturen und Dienstleister werden nicht aufgenommen.

### Chinesisch

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - Chinesischsprachiger Preprint zu ethischen Risiken von GEO wie geistigem Eigentum, algorithmischer Verzerrung, Erklärbarkeit und Desinformation, mit fünf vorgeschlagenen Gegenmaßnahmen. (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - Xinhua-Bericht über das AIIA-Seminar zu vertrauenswürdigem GEO im Mai 2026 mit Bewertungen von GEO-Diensten durch die CAICT, einem Bericht über GEO-Risiken und der Selbstregulierung der Branche. (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - Verbandsstandard der China Advertising Association, der Anforderungen an GEO-Dienstleister, vertrauenswürdige Inhaltsquellen, unzulässige Techniken und die Berichterstattung über Ergebnisse festlegt. (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - Beitrag über den GEO-Boom 2026 in China, der erklärt, wie GEO beim Abruf der Quellen für KI-Antworten ansetzt und wie massenhaft gestreute Inhalte ein gefälschtes Produkt in KI-Empfehlungen brachten. (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - Ausführliche Analyse zur Vergiftung von KI-Daten durch Black-Hat-GEO mit Blick auf Regulierung und Gegenmaßnahmen der Plattformen, einschließlich des eigenen Trusted-GEO-Dienstes der Hunan Daily. (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - Analyse von Googles Spam-Richtlinien-Update 2026 gegen die Manipulation von KI-Antworten, die GEO von bezahlter Content-Platzierung abgrenzt und die Grauzonen dazwischen erörtert. (2026)

### Japanisch

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - Bericht über einen 28-tägigen Test, bei dem eine Website von AI Overviews und AI Mode ausgeschlossen wurde; die Klickrate dort wird auf mehr als das Doppelte des Website-Durchschnitts geschätzt. (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - Ahrefs-Studie zu informationsorientierten japanischen Keywords, die schätzt, dass AI Overviews die Klickrate des ersten Treffers bis Juni 2026 um 62,7 % gesenkt haben. (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - Auftakt einer Serie von Nikkei xTrend zur Optimierung für die KI-Suche, die Ahrefs-Daten zum Klickrückgang durch AI Overviews in Japan zitiert; der Großteil ist zahlenden Mitgliedern vorbehalten. (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - Ankündigung von Google Japan zu AI Mode auf Japanisch, die beschreibt, wie das Fan-out-Verfahren eine Frage in Unterthemen zerlegt und für jedes eine eigene Suche ausführt. (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - Bericht über einen Vortrag von Kenichi Suzuki, nach dem GEO und LLMO auf klassischem SEO beruhen, mit einem konzeptionellen Modell, wie die KI-Suche von Google ihre Antworten aufbaut. (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - Einführung von Nikkei xTECH zu LLMO, dem in Japan verbreiteten Begriff für GEO, und zum Unterschied zu SEO; für den vollständigen Text ist eine kostenlose Registrierung nötig. (2026)

### Koreanisch

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - Bericht der Korea Press Foundation darüber, wie KI-Browser und Zero-Click-Antworten die Verbreitung von Nachrichten und die Erlösmodelle von Verlagen verändern. (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - Bericht der Korea Press Foundation zu den Auflagen der britischen CMA für Google von 2026, etwa KI-Opt-outs, Daten zur KI-Suche und Quellenangaben, und zu ihrer Bedeutung für Korea. (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - Trendbeitrag in der Zeitschrift der Korea Federation of Advertising Associations zu GEO, zur Nutzung von Suchdaten durch Suchmaschinen wie Perplexity und Gemini sowie zur Rolle von E-E-A-T. (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - GEO-Leitfaden eines koreanischen Zahlungsdienstleisters für Onlineshops mit fünf Taktiken wie Q&A-Content, anwendungsbezogenen Produktbeschreibungen, FAQs und externen Erwähnungen. (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - Pressemitteilung von Naver dazu, wie AI Briefing Beiträge von Creators als Quellen anzeigt, und zu Naver Mate, das monatlich rund 3.000 Creators auf Basis von AI-Briefing-Zitationen vergütet. (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - GeekNews-Beitrag, der den a16z-Essay zu GEO auf Koreanisch zusammenfasst, mit einer kurzen Leserdiskussion darüber, wie sich die Begriffe GEO und AEO überschneiden. (2025)

### Spanisch

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - Explorative Studie, die eine allgemeine Reiseanfrage zu drei Zeitpunkten an mehrere KI-Systeme stellte und eine stark schwankende Sichtbarkeit von Hotelmarken und zitierten Quellen feststellte. (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - Wertet die GEO-Literatur aus, die bei Metriken für Sichtbarkeit, Einfluss und Überprüfbarkeit sowie bei wiederkehrenden Strategien wie Struktur, strukturierten Daten und Autorität konvergiert. (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - Argumentiert, dass AI Overviews und AI Mode den Traffic spanischer Nachrichtenseiten stark verringert haben und Verlage auf GEO, Leserbindung und kollektive Lizenzierung setzen sollten. (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - Schlägt die ersten GEO-Richtlinien für institutionelle Repositorien vor, mit technischer Einrichtung, semantischer Struktur, Metadaten, mehrsprachigen Inhalten und neuen Metriken. (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - Analyse von 2,26 Millionen spanischen Prompts mit einem Ranking der Nachrichtenmedien, die ChatGPT, Gemini, Perplexity, Copilot, Grok und Googles KI-Funktionen am häufigsten zitieren. (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - Zusammenfassung einer Studie der Universität Barcelona zu 2.699 Keywords, die AI Overviews bei 29,8 % der Suchen zu großen spanischen Nachrichtenmedien fand, bei Eilmeldungen aber selten. (2026)

### Deutsch

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - Whitepaper des deutschen Digitalverbands BVDW zum Wandel von der Suche zu KI-Antwortsystemen mit einer vorgeschlagenen Standarddefinition von GEO und ihrer Abgrenzung zu SEO. (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - Analyse von 3,8 Millionen deutschsprachigen ChatGPT-Antworten, nach der ein Modellwechsel im Mai 2026 die Verteilung der zitierten Domains binnen zwei Tagen um 47 % verschob. (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - Bericht über eine Studie zu 250.000 KI-Antworten, die zeigt, welche Quellen ChatGPT, AI Overviews und Perplexity am häufigsten zitieren, angeführt von Unternehmenswebsites, YouTube und Reddit. (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - Erklärt, wie ChatGPT, Gemini, Copilot und Perplexity Seiten finden und zitieren, vom Fan-out von Suchanfragen über Suchindizes bis zum technischen Zugriff, mit einer Checkliste für Unternehmen. (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - Vergleicht zitierte und nicht zitierte Seiten derselben Domains in KI-Antworten im DACH-Raum und zeigt, dass Struktur und Schema mit Zitationen korrelieren, llms.txt aber keinen Effekt hat. (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - Kurzes Whitepaper des BVDW mit neun KPIs zur Messung der Markensichtbarkeit in der generativen Suche sowie Empfehlungen zu Prompt-Sets und regelmäßiger Überprüfung. (2026)

## Fallstudien

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - Zeigt anhand eigener Analytics-Daten von Ahrefs, dass Besucher aus der KI-Suche 0,5 % des Traffics, aber 12,1 % der Registrierungen ausmachten. (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - Fallstudie eines Anbieters, laut der die von Profound gemessene Sichtbarkeit von Ramps Kreditorenprodukt in der KI-Suche auf 22,2 % stieg, mit den Seiten und Suchanfragen, auf die Ramp abzielte. (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - Beschreibt, wie Vercel SEO für die Auffindbarkeit in LLMs anpasst, und berichtet, dass rund 10 % der neuen Registrierungen über ChatGPT kamen, gegenüber 1 % sechs Monate zuvor. (2025)

## Kurse, Videos und Podcasts

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Kostenloser Videokurs von Sam Oh mit 12 Lektionen zur Quellenauswahl von KI-Suchmaschinen, Prompt-Recherche, Content und YouTube für die KI-Suche, technischem Setup und Erfassung des KI-Traffics.
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - Vierstündiger Coursera-Kurs von SkillUp in zwei Modulen zu Entitäten und thematischer Autorität, KI-gerechten Content-Formaten, GEO-Metriken und Praxisübungen; das Zertifikat ist kostenpflichtig.
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - Kostenloser Zertifikatskurs mit sieben Lektionen zur Zitation durch Antwortmaschinen, Fragenrecherche, On-Page- und Schema-Optimierung sowie Messung von KI-Referrals und Share of Voice.
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Kostenlose, von Aleyda Solis kuratierte Lern-Roadmap, die Leitfäden zu Grundlagen der KI-Suche, Messung, E-Commerce und Tools ordnet, mit einer Checkliste zur Content-Optimierung.
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - Kurzer Zertifikatskurs für PR- und Kommunikationsteams dazu, wie Earned Media KI-Antworten prägt, zum Testen von Prompts und zur Nutzung von GEO-Erkenntnissen bei der Medienauswahl.
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Podcast des Google-Search-Relations-Teams darüber, wie die Google-Suche hinter den Kulissen funktioniert, einschließlich ihrer KI-Funktionen und aktueller Themen der SEO-Community.
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - Kostenloser Kurs mit 20 Videos und Zertifikat zu Prompt-Recherche, Share of Voice, Markenerwähnungen und der Formatierung von Inhalten für LLMs; mehrere Lektionen zeigen Semrush-Tools.

## Newsletter und Communities

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Substack-Newsletter von Tom Critchlow, früher The SEO MBA, über Strategie und Führung für Suchteams, die sich auf die KI-Suche einstellen.
- [brightonSEO](https://brightonseo.com/) 💲 - Große Konferenzreihe zum Suchmaschinenmarketing in Brighton und San Diego mit Vorträgen und Trainings zu SEO, Content und KI-Suche sowie einer Ticketverlosung für die britische Veranstaltung.
- [GEO Conference](https://geo-conference.com/) 💲 - Reihe eintägiger Präsenzkonferenzen zu Generative Engine Optimization in US-Städten mit höchstens 150 Plätzen pro Veranstaltung, gesponsert vor allem von Anbietern von GEO- und SEO-Tools.
- [Growth Memo](https://www.growth-memo.com/) 🪙 - Newsletter von Kevin Indig zu organischem Wachstum mit regelmäßigen Datenstudien zu Nutzerverhalten in der KI-Suche, Zitationen und Traffic; einige Ausgaben sind zahlenden Abonnenten vorbehalten.
- [MozCon](https://moz.com/mozcon) 💲 - Marketingkonferenz von Moz zu SEO, KI-Suche und GEO, 2026 als Roadshow mit Präsenzveranstaltungen in London und New York.
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Tägliche News-Website von Barry Schwartz, die Diskussionen in der Search-Community und Änderungen bei Google und Bing verfolgt, einschließlich ihrer KI-Suchfunktionen.
- [SEOFOMO](https://seofomo.co/) 🆓 - Wöchentlicher Newsletter von Aleyda Solis mit News, Leitfäden, Tools, Events und Jobs zu SEO und KI-Suche.

## Weitere kuratierte Listen

Listen zu GEO und KI-Suche mit ähnlichem Themenzuschnitt, die wir hier dankend verlinken.

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - Umfangreiche GEO-Ressourcenliste mit plattformspezifischen Leitfäden, Agentic Commerce, Tools, Forschung, Newslettern, Videos und Events.
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - Forschungsorientierte Liste von Arbeiten zu GEO, nach Jahren geordnet.
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - Liste kostenloser Plattformen und Open-Source-Repositories für GEO mit Bewertungen, Suche und kostenlosen Tools auf einer begleitenden Website.
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - Alphabetisches Verzeichnis von Tools für GEO und das Monitoring der KI-Sichtbarkeit mit kurzen Hinweisen zu Funktionen und Preisen.
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - Allgemeine GEO-Liste mit Lernressourcen, Tools, KI-Suchmaschinen, Strategien, Monitoring, Fallstudien, Communities und Plattform-News.
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - GEO-Liste (früher Tusko/awesome-geo) mit Forschung, offizieller Plattformdokumentation, Leitfäden, Tools, Kursen, Newslettern und Communities.
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - Vergleichstabelle von GEO-Tools nach abgedeckten Suchmaschinen, Aktualisierungsrate, Preis und Datenexport, gepflegt von einem GEO-Tool-Anbieter, der sich selbst ebenfalls aufführt.

## Mitwirken

Beiträge sind willkommen. Bitte lies vor einem Pull Request die [Hinweise zum Mitwirken](CONTRIBUTING.md); eine englische Beschreibung genügt, die übrigen Sprachen ergänzen die Maintainer.

## Lizenz

Soweit gesetzlich zulässig, haben die Mitwirkenden mit [CC0 1.0 Universal](LICENSE) auf alle Urheber- und verwandten Schutzrechte an dieser Liste verzichtet.
