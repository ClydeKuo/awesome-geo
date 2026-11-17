# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | **Español** | [Deutsch](README.de.md)

> Una lista curada de recursos sobre optimización para motores generativos (GEO): investigación, guías, estándares, herramientas y buscadores de IA de todo el mundo.

## Contenido

- [Qué es GEO](#qué-es-geo)
- [Introducción](#introducción)
- [Artículos de investigación](#artículos-de-investigación)
  - [Trabajos fundacionales](#trabajos-fundacionales)
  - [Benchmarks y conjuntos de datos](#benchmarks-y-conjuntos-de-datos)
  - [Ataques y manipulación](#ataques-y-manipulación)
  - [Análisis de citas y visibilidad](#análisis-de-citas-y-visibilidad)
  - [Revisiones](#revisiones)
- [Guías y artículos](#guías-y-artículos)
  - [Estrategia](#estrategia)
  - [Redacción de contenidos](#redacción-de-contenidos)
  - [Implementación técnica](#implementación-técnica)
  - [Informes y datos del sector](#informes-y-datos-del-sector)
- [Estándares y especificaciones](#estándares-y-especificaciones)
  - [llms.txt](#llmstxt)
  - [Rastreadores de IA y robots.txt](#rastreadores-de-ia-y-robotstxt)
  - [Datos estructurados](#datos-estructurados)
  - [Documentación oficial de los motores](#documentación-oficial-de-los-motores)
- [Herramientas](#herramientas)
  - [Seguimiento de la visibilidad en IA](#seguimiento-de-la-visibilidad-en-ia)
  - [Auditoría y optimización de contenidos](#auditoría-y-optimización-de-contenidos)
  - [Herramientas y bibliotecas de código abierto](#herramientas-y-bibliotecas-de-código-abierto)
  - [Generadores de llms.txt](#generadores-de-llmstxt)
  - [Análisis de logs de rastreadores](#análisis-de-logs-de-rastreadores)
- [Buscadores y asistentes de IA](#buscadores-y-asistentes-de-ia)
  - [Global](#global)
  - [China](#china)
  - [Japón](#japón)
  - [Corea del Sur](#corea-del-sur)
  - [Europa](#europa)
  - [Otras regiones](#otras-regiones)
- [Recursos de GEO en otros idiomas](#recursos-de-geo-en-otros-idiomas)
  - [En chino](#en-chino)
  - [En japonés](#en-japonés)
  - [En coreano](#en-coreano)
  - [En español](#en-español)
  - [En alemán](#en-alemán)
- [Estudios de caso](#estudios-de-caso)
- [Cursos, videos y podcasts](#cursos-videos-y-podcasts)
- [Boletines y comunidades](#boletines-y-comunidades)
- [Otras listas curadas](#otras-listas-curadas)
- [Licencia](#licencia)

**Leyenda:** 🆓 gratis, 🪙 freemium, 💲 de pago, 🔓 código abierto

## Qué es GEO

La optimización para motores generativos (GEO, por sus siglas en inglés) consiste en lograr que motores de respuestas con IA como ChatGPT, Perplexity o Google AI Overviews encuentren, entiendan y citen un contenido con facilidad. Mientras que el SEO compite por posiciones en una lista de enlaces, el GEO busca que el contenido aparezca citado o mencionado dentro de la propia respuesta generada, por lo que el éxito se mide en citas y visibilidad más que en clics. El término procede del artículo «GEO: Generative Engine Optimization» de Aggarwal et al. (Universidad de Princeton y otras instituciones, KDD 2024).

## Introducción

- [Generative Engine Optimization (GEO): What It Is and How to Do It](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) 🆓 - Texto divulgativo de Search Engine Land que define el GEO como la obtención de citas y menciones en las respuestas de IA y explica cómo se apoya en los fundamentos del SEO.
- [Generative engine optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization) 🆓 - Entrada enciclopédica que define el GEO, remonta el término al artículo de investigación de 2023, enumera nombres afines como AEO y LLMO y recoge las críticas.
- [Google's New AI Search Guide Calls AEO and GEO 'Still SEO'](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/) 🆓 - Artículo de Search Engine Journal sobre la guía de Google de mayo de 2026 que trata el AEO y el GEO como parte del SEO habitual y desmiente la utilidad de llms.txt y la fragmentación del contenido.
- [Optimizing your website for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) 🆓 - Guía de la propia Google que afirma que optimizar para las funciones de IA sigue siendo SEO y considera innecesarias tácticas como llms.txt o la fragmentación del contenido.
- [SEO vs. GEO: What's different? What's the same?](https://searchengineland.com/seo-vs-geo-459474) 🆓 - Comparación de Search Engine Land entre el SEO y el GEO que abarca objetivos, medición y las prácticas que comparten.
- [What is generative engine optimization (GEO)?](https://geo.deeflect.com/guides/what-is-generative-engine-optimization) 🆓 - Texto divulgativo que remonta el término GEO al artículo de Aggarwal et al. presentado en KDD 2024, compara definiciones del sector y resume lo que se sabe sobre la visibilidad en IA.

## Artículos de investigación

### Trabajos fundacionales

- [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063) 🆓 - Muestra un sistema agéntico que evalúa nueve estrategias de GEO para cada pieza de contenido y acelera la elección de la mejor con un enfoque de bandidos multibrazo. (2026)
- [AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213) 🆓 - Propone un sistema agéntico de GEO que evoluciona por sí mismo y va más allá de las heurísticas estáticas y la reescritura con un solo prompt para ganar visibilidad en las respuestas resumidas. (2026)
- [Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization](https://arxiv.org/abs/2608.27631) 🆓 - Formaliza el GEO como selección de estrategias que tiene en cuenta a la competencia y aplica optimización bayesiana sobre estructuras combinatorias para elegir estrategias de reescritura. (2026)
- [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://arxiv.org/abs/2603.09296) 🆓 - Diagnostica por qué un motor generativo no cita un documento concreto y aplica correcciones específicas en lugar de reglas de reescritura uniformes. (2026)
- [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516) 🆓 - Plantea el GEO como aprendizaje de estrategias, con agentes de planificación, edición y evaluación que destilan estrategias de edición reutilizables entre tareas y motores. (2026)
- [IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization](https://arxiv.org/abs/2601.13938) 🆓 - Resuelve demandas de revisión contradictorias entre muchas consultas con un marco de divergencia y convergencia que extrae preferencias de optimización y las fusiona en una sola revisión. (2026)
- [Structural Feature Engineering for Generative Engine Optimization: How Content Structure Shapes Citation Behavior](https://arxiv.org/abs/2603.29979) 🆓 - Propone GEO-SFE, un marco que diseña la estructura del contenido en varios niveles jerárquicos para influir en qué páginas citan los motores generativos. (2026)
- [Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility](https://aclanthology.org/2026.acl-long.929) 🆓 - Propone FeatGEO, que optimiza características interpretables de estructura, contenido y lenguaje de una página para equilibrar la visibilidad en citas con la calidad del contenido. (2026)
- [Beyond SEO: A Transformer-Based Approach for Reinventing Web Content Optimisation](https://arxiv.org/abs/2507.03169) 🆓 - Ajusta un modelo BART-base con pares sintéticos de textos de sitios de viajes para reescribir contenido y hacerlo más visible en las respuestas de los LLM. (2025)
- [Role-Augmented Intent-Driven Generative Search Engine Optimization](https://arxiv.org/abs/2508.11158) 🆓 - Optimiza contenido para buscadores generativos sin conocer las consultas objetivo ni disponer de retroalimentación del motor, infiriendo de antemano las intenciones y los roles de los usuarios. (2025)
- [What Generative Search Engines Like and How to Optimize Web Content Cooperatively](https://arxiv.org/abs/2510.11438) 🆓 - Presenta AutoGEO, que aprende qué prefieren los motores generativos en el contenido recuperado y reescribe las páginas web en consecuencia para ganar visibilidad. (2025)
- [White Hat Search Engine Optimization using Large Language Models](https://arxiv.org/abs/2502.07315) 🆓 - Presenta técnicas de optimización para buscadores de sombrero blanco basadas en IA generativa y expone sus mejoras empíricas. (2025)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) 🆓 - Presenta GEO y un benchmark para medir la visibilidad del contenido en las respuestas de motores generativos. (2023)

### Benchmarks y conjuntos de datos

- [C-SEO Bench: Does Conversational SEO Work?](https://arxiv.org/abs/2506.11097) 🆓 - Evalúa métodos de SEO conversacional en distintas tareas, dominios y números de adoptantes, y concluye que la mayoría son ineficaces y que el SEO clásico suele funcionar mejor. (2025)
- [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](https://arxiv.org/abs/2609.02316) 🆓 - Evalúa defensas frente a documentos optimizados con GEO que contienen desinformación dirigida, con consultas verificadas por personas en condiciones controladas. (2026)
- [Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO](https://arxiv.org/abs/2611.01126) 🆓 - Presenta LIVE-GEO para comprobar si las mejoras de visibilidad del GEO se mantienen en la web real, donde motores generativos reales obtienen y ordenan las páginas. (2026)
- [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://arxiv.org/abs/2511.20867) 🆓 - Ofrece 13 746 consultas de productos de consumo con los listados recuperados para probar heurísticas de reescritura de GEO en varios motores generativos de comercio electrónico. (2025)
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627) 🆓 - Presenta ALCE, un benchmark con métricas automáticas de fluidez, corrección y calidad de las citas para respuestas de LLM que citan evidencias recuperadas. (2023)
- [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/abs/2605.29107) 🆓 - Evalúa los ataques de manipulación del ranking mediante GEO con un mismo protocolo y conjuntos de datos y métricas unificados, y compara su eficacia y su detectabilidad. (2026)
- [How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews](https://arxiv.org/abs/2604.27790) 🆓 - Publica un conjunto de datos de 11 500 consultas de usuarios y compara las fuentes y la información que devuelven la Búsqueda de Google, AI Overviews y Gemini. (2026)
- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](https://arxiv.org/abs/2602.12187) 🆓 - Ofrece un entorno para evaluar de extremo a extremo estrategias de GEO aumentadas con búsqueda, que abarca la recuperación y el ranking además de la generación. (2026)

### Ataques y manipulación

Investigación sobre GEO adversarial, es decir, cómo se puede manipular un motor de respuestas mediante inyección de prompts o ataques al ranking, y cómo defenderse.

- [Controlling Output Rankings in LLM-Based Search via Generative Engine Optimization](https://arxiv.org/abs/2602.03608) 🆓 - Propone CORE, un método de optimización que controla en qué posición aparecen los artículos en las recomendaciones de productos generadas por LLM. (2026)
- [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361) 🆓 - Revisa la evidencia sobre manifiestos de tipo llms.txt para la búsqueda con IA, constata que apenas se obtienen de forma automática y evalúa sus implicaciones de seguridad. (2026)
- [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390) 🆓 - Muestra que los ataques de GEO pueden desembocar en guerras de citas que degradan la calidad del contenido y estudia el diseño de mecanismos para lograr resultados en que todos ganen. (2026)
- [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263) 🆓 - Muestra que perturbaciones de imagen y texto diseñadas conjuntamente pueden manipular cómo ordenan productos los modelos de visión y lenguaje. (2026)
- [Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots](https://arxiv.org/abs/2606.12439) 🆓 - Sostiene que el GEO conlleva riesgos de influencia concentrada, influencia comercial oculta y puntos ciegos entre academia e industria, y pide gobernar las respuestas con transparencia y auditorías. (2026)
- [SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines](https://arxiv.org/abs/2605.21948) 🆓 - Protege los rankings basados en LLM detectando la estructura persuasiva que los vendedores insertan en el contenido para colocar sus artículos en primer lugar. (2026)
- [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](https://arxiv.org/abs/2609.02964) 🆓 - Defiende la búsqueda generativa frente a reescrituras maliciosas de GEO que mantienen la coherencia factual y así eluden la verificación de datos y los filtros de perplejidad. (2026)
- [Dynamics of Adversarial Attacks on Large Language Model-Based Search Engines](https://arxiv.org/abs/2501.00745) 🆓 - Modela los ataques de manipulación del ranking en la búsqueda con LLM como un dilema del prisionero repetido infinitamente y analiza cuándo puede mantenerse la cooperación. (2025)
- [Exposing Citation Vulnerabilities in Generative Engines](https://arxiv.org/abs/2510.06823) 🆓 - Analiza qué medios citan los motores generativos y lo difícil que resulta para un atacante inyectar contenido malicioso en las fuentes de sus respuestas. (2025)
- [StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization](https://arxiv.org/abs/2504.05804) 🆓 - Presenta un ataque que usa optimización basada en energía para crear prompts fluidos y difíciles de detectar que manipulan los rankings generados por LLM. (2025)
- [Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.12574) 🆓 - Estudia ataques de envenenamiento en competencia contra sistemas RAG, en los que varios adversarios dirigen la misma consulta hacia objetivos distintos, y presenta el benchmark PoisonArena. (2025)
- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) 🆓 - Presenta ataques de manipulación de preferencias que inclinan las elecciones de los LLM hacia el contenido del atacante y muestra que generan un dilema del prisionero entre vendedores. (2024)
- [GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search](https://arxiv.org/abs/2412.20953) 🆓 - Estudia ataques de tipo SEO en los que se crean pasajes adversariales para que los recupere la búsqueda por embeddings densos, la capa de recuperación de muchos sistemas RAG. (2024)
- [Manipulating Large Language Models to Increase Product Visibility](https://arxiv.org/abs/2404.07981) 🆓 - Muestra que añadir una secuencia de texto estratégica a la página de un producto puede hacer que un buscador basado en LLM lo recomiende en primer lugar. (2024)
- [Ranking Manipulation for Conversational Search Engines](https://arxiv.org/abs/2406.03589) 🆓 - Muestra, con páginas reales de productos de consumo, que las inyecciones de prompts en el texto de una página pueden mejorar la posición de una fuente en los resultados de la búsqueda conversacional. (2024)

### Análisis de citas y visibilidad

- [AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence](https://arxiv.org/abs/2608.18352) 🆓 - Presenta un experimento de campo prerregistrado (N = 1100) que concluye que quitar AI Overviews y AI Mode aumenta los clics hacia los medios. (2026)
- [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164) 🆓 - Realiza una auditoría causal de cómo la presentación de un documento cambia cuál de dos fuentes con el mismo respaldo cita un motor de búsqueda agéntico. (2026)
- [Don't Measure Once: Measuring Visibility in AI Search (GEO)](https://arxiv.org/abs/2604.07585) 🆓 - Muestra que las respuestas de la búsqueda con IA varían entre ejecuciones, prompts y momentos, por lo que la visibilidad debe medirse repetidamente y no una sola vez. (2026)
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) 🆓 - Distingue entre la selección y la absorción de citas y analiza 602 prompts en ChatGPT, Google AI y Perplexity. (2026)
- [From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search](https://arxiv.org/abs/2609.23162) 🆓 - Analiza casi 35 000 observaciones de prompts y concluye que la tasa de menciones de una marca se dispara cuando su propio dominio aparece en la recuperación en tiempo real. (2026)
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) 🆓 - Estudia cómo medir la visibilidad de marca en ChatGPT, Claude, Perplexity y Gemini, incluidas las fuentes en las que se apoyan estos motores al citar marcas. (2026)
- [Measuring GEO Visibility: Prompt Corpora Define the Answer Market](https://arxiv.org/abs/2609.06811) 🆓 - Sostiene que las puntuaciones de visibilidad en GEO dependen del corpus de prompts y de sus pesos, que definen un mercado de respuestas que puede no coincidir con la demanda real. (2026)
- [Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact](https://arxiv.org/abs/2605.14021) 🆓 - Sigue 55 393 consultas durante 40 días para medir cuándo aparecen los AI Overviews, la calidad de sus fuentes, la fidelidad de sus afirmaciones y su efecto en los medios. (2026)
- [Navigating the Shift: A Comparative Analysis of Web Search and Generative AI Response Generation](https://arxiv.org/abs/2601.16858) 🆓 - Cuantifica en qué se diferencian los resultados de Google y las respuestas de IA generativa en dominios citados, tipos de dominio, intención de búsqueda y actualidad. (2026)
- [Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores](https://arxiv.org/abs/2609.22655) 🆓 - Audita ChatGPT, Copilot, Google y Perplexity y halla una coincidencia muy baja de URL entre motores, lo que limita las puntuaciones de GEO independientes del motor. (2026)
- [Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) 🆓 - Audita cuatro buscadores generativos con 712 consultas y halla que alrededor del 16 % de las fuentes citadas parecen generadas por IA. (2026)
- [The Impact of AI Search on the Online Content Ecosystem: Evidence from Google and Reddit](https://arxiv.org/abs/2605.16428) 🆓 - A partir de Google AI Overviews y Reddit, muestra que la búsqueda con IA aumentó la participación en las comunidades citadas y que el efecto se diluyó tras el lanzamiento de AI Mode. (2026)
- [Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations](https://arxiv.org/abs/2610.15382) 🆓 - Observa cómo cuatro configuraciones de ChatGPT Web reescriben consultas, recuperan páginas y eligen citas, y muestra que la frecuencia de recuperación predice la cita. (2026)
- [What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study](https://arxiv.org/abs/2607.15771) 🆓 - Analiza el comportamiento de citas, la atribución de fuentes y la exposición de entidades en cuatro plataformas de búsqueda generativa en chino a partir de 614 consultas. (2026)
- [What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)](https://arxiv.org/abs/2610.15033) 🆓 - Analiza 158 099 respuestas y concluye que las páginas que recupera ChatGPT para sus subconsultas reescritas explican las citas mucho mejor que las propiedades de las páginas. (2026)
- [AI Answer Engine Citation Behavior: An Empirical Analysis of the GEO16 Framework](https://arxiv.org/abs/2509.10762) 🆓 - Presenta una auditoría de páginas con 16 pilares y concluye que los metadatos, el HTML semántico y los datos estructurados son lo que más se relaciona con las citas en tres motores. (2025)
- [Generative Engine Optimization: How to Dominate AI Search](https://arxiv.org/abs/2509.08919) 🆓 - Compara buscadores de IA con Google mediante experimentos controlados en varios sectores e idiomas y halla un fuerte sesgo a favor de los medios ganados frente al contenido propio de las marcas. (2025)
- [What Evidence Do Language Models Find Convincing?](https://arxiv.org/abs/2402.11782) 🆓 - Crea ConflictingQA para mostrar que los LLM se basan mucho en la pertinencia de una página para la consulta y apenas tienen en cuenta rasgos de estilo como las referencias científicas. (2024)
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) 🆓 - Audita la exhaustividad y la precisión de las citas de Bing Chat, NeevaAI, Perplexity y YouChat, y concluye que muchas afirmaciones carecen de un respaldo completo. (2023)

### Revisiones

- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035) 🆓 - Revisa 45 estudios de 2023 a 2026, plantea el GEO como un proceso estocástico de varias etapas y ofrece una lista de verificación para valorar las afirmaciones sobre el GEO. (2026)
- [A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges](https://arxiv.org/abs/2508.05668) 🆓 - Clasifica sistemáticamente los agentes de búsqueda basados en LLM por arquitectura, optimización, aplicación y evaluación, y enumera los retos abiertos. (2025)
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) 🆓 - Revisión técnica de la búsqueda y la recomendación generativas con modelos de lenguaje grandes. (2024)
- [When Search Engine Services meet Large Language Models: Visions and Challenges](https://arxiv.org/abs/2407.00128) 🆓 - Examina cómo pueden beneficiarse mutuamente los buscadores y los LLM, tanto la búsqueda para mejorar los LLM como los LLM para mejorar la búsqueda. (2024)
- [Large Language Models for Information Retrieval: A Survey](https://arxiv.org/abs/2308.07107) 🆓 - Revisión de cómo se usan los modelos de lenguaje grandes en los sistemas de recuperación de información, incluida la reescritura de consultas, la recuperación, el reordenamiento y la lectura. (2023)

## Guías y artículos

### Estrategia

- [Generative Engine Optimization (GEO): A Practical Guide](https://www.semrush.com/blog/generative-engine-optimization/) 🆓 - Introducción práctica a cómo la optimización para motores generativos ayuda a que el contenido aparezca en los resultados de búsqueda con IA. (2026)
- [Generative Engine Optimization (GEO): How to Win in AI Search](https://backlinko.com/generative-engine-optimization-geo) 🆓 - Explica qué es el GEO, en qué se diferencia del SEO y qué técnicas ayudan a que el contenido se cite en las respuestas de IA, con una lista de verificación de auditoría descargable. (2025)
- [Generative Engine Optimization: Growth Strategies and Metrics For the AI Era](https://ahrefs.com/blog/generative-engine-optimization/) 🆓 - Explica en qué se diferencia la búsqueda con IA de la tradicional, expone cinco tácticas de GEO y cómo medir su éxito, y señala que la búsqueda con IA sigue apoyándose en la tradicional. (2025)
- [How Generative Engine Optimization (GEO) Rewrites the Rules of Search](https://a16z.com/geo-over-seo) 🆓 - Sostiene que la búsqueda pasa del ranking basado en enlaces a las respuestas de modelos de lenguaje y presenta el GEO como la siguiente fase de un mercado del SEO de unos 80 000 millones de dólares. (2025)
- [SEEN GEO checklist: 41 items across four layers](https://geo.deeflect.com/guides/geo-framework-checklist) 🆓 - Presenta SEEN, un marco de GEO de cuatro capas (Structure, Evidence, Entity y Notability), con una lista de verificación de 41 ítems que se puntúan con 0 o 1 para detectar la capa más débil. (2026)
- [The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026](https://superlines.io/articles/generative-engine-optimization-geo-guide-2025) 🆓 - Recorre un proceso de GEO en diez pasos, desde elegir los temas prioritarios y una línea de base hasta analizar las fuentes citadas, mejorar el contenido e informar de los resultados. (2025)
- [What is Answer Engine Optimization (AEO)?](https://ahrefs.com/blog/answer-engine-optimization/) 🆓 - Abre una guía de AEO en ocho partes: diferencias con el SEO, funcionamiento de los motores de respuestas, seguimiento de la visibilidad en IA, elección de prompts y corrección de errores de la IA. (2025)

### Redacción de contenidos

- [AI Overviews: What Are They & How to Optimize for Them](https://www.semrush.com/blog/ai-overviews/) 🆓 - Explica qué son los AI Overviews de Google, cómo se generan a partir de fuentes web y cómo pueden los propietarios de sitios optimizar para ellos y hacer seguimiento de su visibilidad. (2026)
- [How to get cited by ChatGPT in 2026, from our own measurements](https://glotier.com/how-to-get-cited-by-chatgpt) 🆓 - Describe un método en dos fases para lograr citas en ChatGPT (ser recuperado y luego citable), cada una respaldada por mediciones propias, como la de qué dominios citados admiten rastreadores de IA. (2026)
- [How to Get Your Website Cited by ChatGPT and Other AI Search Engines](https://startupfortune.com/how-to-get-your-website-cited-by-chatgpt-and-ai-search/) 🆓 - Expone lo que mostraron 13 pruebas con preguntas de compradores en ChatGPT y los logs del servidor del sitio, incluido un resultado negativo, y qué bots de IA conviene permitir. (2026)
- [How to Optimize Content for AI Search Engines \[2026 Guide\]](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) 🆓 - Recorre siete pasos, desde la investigación de palabras clave hasta el formato, para que buscadores de IA como ChatGPT y Google citen un contenido. (2026)
- [How to rank in ChatGPT search: 8 steps to improve visibility](https://semrush.com/blog/chatgpt-search) 🆓 - Propone ocho pasos para posicionarse en ChatGPT Search, haciendo que los sistemas de IA puedan extraer el contenido con facilidad y generando consenso fuera del sitio. (2025)
- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization) 🆓 - Enumera diez formas de mejorar la visibilidad de una marca en las respuestas generadas por LLM, planteadas como optimización para LLM (LLMO). (2024)
- [Optimizing Your Content for Inclusion in AI Search Answers](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) 🆓 - Guía de Microsoft Advertising sobre qué hace útil un contenido en la búsqueda con IA (Schema, títulos claros, bloques autónomos de preguntas y respuestas) y errores como ocultarlas en pestañas o PDF. (2025)

### Implementación técnica

- [AI Search Optimization: Make Your Structured Data Accessible](https://searchenginejournal.com/ai-search-optimization-make-your-structured-data-accessible/537843) 🆓 - Informa de una investigación según la cual los rastreadores de IA que no ejecutan JavaScript no ven el JSON-LD insertado en el cliente, por ejemplo mediante Google Tag Manager. (2025)
- [How to Track AI Search Traffic to Your Site in GA4](https://seoclarity.net/blog/track-ai-search-traffic) 🆓 - Muestra cómo hacer seguimiento en Google Analytics 4 del tráfico de referencia procedente de herramientas de IA como ChatGPT y Gemini. (2025)
- [Introducing Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 🆓 - Presenta el envío de páginas en Markdown a agentes de IA y muestra cómo reduce el uso de tokens: una entrada pasa de 16 180 tokens en HTML a 3150 en Markdown. (2026)
- [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) 🆓 - Presenta datos de MERJ y Vercel sobre cómo tratan el JavaScript y los tipos de contenido ChatGPT, Claude y otros rastreadores de IA, con recomendaciones para propietarios de sitios. (2024)

### Informes y datos del sector

- [63% of Websites Receive AI Traffic (New Study of 3,000 Sites)](https://ahrefs.com/blog/ai-traffic-study) 🆓 - Estudia 3000 sitios web para estimar cuánto tráfico envían los chatbots de IA y concluye que el 63 % de los sitios recibe algo y que tres chatbots generan el 98 % de ese tráfico. (2025)
- [A deeper look at AI crawlers: breaking down traffic by purpose and industry](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) 🆓 - Amplía Cloudflare Radar con datos por sector y un desglose del tráfico de bots de IA según la finalidad del rastreo. (2025)
- [AI Citations & News Publishers: 2026 Study](https://higoodie.com/blog/publishers-and-ai-search-study) 🆓 - Analiza 31 millones de citas de IA y los robots.txt de 105 medios, y concluye que bloquear los rastreadores de IA funciona con algunos modelos y no tiene ningún efecto en otros. (2026)
- [AI Overview Citations Now 54% from Organic Rankings](https://brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio) 🆓 - Sigue 16 meses de datos que muestran cómo la coincidencia entre las citas de AI Overviews y el posicionamiento orgánico pasó del 32 % al 54 %, con desglose por sector. (2025)
- [AI Overviews Reduce Clicks by 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks) 🆓 - Presenta un estudio de Ahrefs según el cual AI Overviews reduce los clics un 34,5 %, lo que contradice la afirmación de Google de que los aumenta. (2025)
- [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) 🆓 - Pone a prueba ocho herramientas de búsqueda con IA mediante fragmentos de noticias y concluye que citan mal las fuentes en más del 60 % de las consultas. (2025)
- [AI Search Stats in 2026](https://aisearch.similarweb.com/blog/gen-ai-stats/) 🆓 - Recopila datos de Similarweb de 2026 sobre la cuota de mercado de ChatGPT, Gemini y Claude, el tráfico de referencia, las citas y los anuncios dentro de las respuestas de IA. (2026)
- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation) 🆓 - Analiza 75 000 marcas para identificar qué factores de búsqueda influyen más en las menciones de marca en AI Overviews. (2025)
- [Do people click on links in Google AI summaries?](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) 🆓 - Compara el comportamiento de usuarios de Google en marzo de 2025 y constata que quienes vieron un resumen de IA hicieron clic con menos frecuencia en enlaces a otros sitios web. (2025)
- [How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations](https://ahrefs.com/blog/how-stable-are-ai-citations/) 🆓 - Sigue 37 500 citas en ChatGPT, Gemini, Copilot y Google y concluye que la mitad desaparece al día siguiente y que la mayoría vuelve después. (2026)
- [LLMs.txt: Why Brands Rely On It and Why It Doesn't Work](https://seranking.com/blog/llms-txt/) 🆓 - Examina 300 000 dominios para ver cuánto se usa llms.txt y si influye en la frecuencia con que los LLM citan un dominio. (2026)
- [OpenAI Has Tripled Their Crawl of the Web: An Analysis of 7B+ Log Files](https://botify.com/blog/openai-tripled-web-crawl) 🆓 - Analiza unos 7000 millones de archivos de log, de noviembre de 2024 a marzo de 2026, para mostrar cómo interactúan con la web los tres rastreadores de OpenAI. (2026)
- [Report: The Impact of Generative AI on Publishers](https://www.similarweb.com/corp/reports/generative-ai-publishers/) 🆓 - Informa de un aumento del 212 % de las consultas de noticias en ChatGPT y una caída del 26 % del tráfico de los medios mientras la IA generativa transforma el sector informativo. (2025)
- [Semrush Report: AI Overviews' Impact on Search in 2025](https://semrush.com/blog/semrush-ai-overviews-study) 🆓 - Analiza más de 10 millones de palabras clave para mostrar cómo están cambiando la búsqueda los AI Overviews de Google y qué implica para el SEO. (2025)
- [Update: 38% of AI Overview Citations Pull From The Top 10](https://ahrefs.com/blog/ai-overview-citations-top-10) 🆓 - Concluye, a partir de 863 000 SERP, que el 38 % de las citas de AI Overviews proceden de páginas del top 10, frente al 76 % de un año antes. (2026)
- [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.](https://ahrefs.com/blog/schema-ai-citations/) 🆓 - Sigue 1885 páginas que añadieron JSON-LD y mide su efecto en las citas de Google AI Overviews, AI Mode y ChatGPT. (2026)
- [Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)](https://ahrefs.com/blog/why-chatgpt-cites-pages/) 🆓 - Estudia 1,4 millones de prompts para mostrar cómo influyen los títulos, las URL y los fragmentos en qué páginas recuperadas cita ChatGPT. (2026)

## Estándares y especificaciones

Especificaciones y documentación oficial que determinan cómo acceden los rastreadores de IA a un sitio y cómo leen su contenido los motores de respuestas.

### llms.txt

- [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) 🆓 🔓 - Aloja el código fuente de la propuesta llms.txt junto con sus herramientas de referencia y el debate sobre ella.
- [Google Confirms LLMs.txt Has No Current Implementation](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) 🆓 - Recoge que John Mueller considera llms.txt especulativo por ahora y que prefiere WebMCP, una alternativa respaldada por Google.
- [Google Says No AI System Currently Uses LLMs.txt](https://www.seroundtable.com/google-ai-llms-txt-39607.html) 🆓 - Recoge la afirmación de John Mueller de que ningún sistema de IA usa llms.txt en la actualidad, según lo que muestran los logs del servidor. (2025)
- [llms-txt-hub](https://llmstxthub.com) 🆓 🔓 - Directorio de sitios web que implementan llms.txt, con archivos de ejemplo de API, plataformas y herramientas para desarrolladores.
- [LLMS.txt Adoption Research Report](https://rankability.com/data/llms-txt-adoption) 🆓 - Mide la adopción de llms.txt entre los 1000 y los 10 000 dominios principales en un estudio de septiembre de 2026, con metodología y datos descargables. (2026)
- [llms.txt directory](https://directory.llmstxt.cloud) 🆓 - Recoge sitios web que publican un archivo llms.txt para que los desarrolladores puedan consultar ejemplos reales del formato.
- [llms.txt Directory (StackFox)](https://stackfox.co/llms-txt) 🆓 - Recoge sitios que publican llms.txt y muestra los permisos de IA que declaran para entrenamiento, recuperación y resumen.
- [The /llms.txt file](https://llmstxt.org) 🆓 - Propone un archivo Markdown /llms.txt en la raíz del sitio que ofrezca a los modelos de lenguaje una visión general curada del sitio y enlaces a su contenido más útil. (2024)
- [The value of llms.txt: Hype or real?](https://mintlify.com/blog/the-value-of-llms-txt-hype-or-real) 🆓 - Defiende el valor de llms.txt con ejemplos de Vercel, Google y Anthropic y responde a quienes sostienen que basta con las prácticas generales de SEO. (2025)
- [What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt) 🆓 - Explica qué es el archivo llms.txt y analiza si añadirlo aporta algo a desarrolladores y profesionales del marketing.

### Rastreadores de IA y robots.txt

- [25 AI crawler user agents and what each does in robots.txt](https://geo.deeflect.com/guides/ai-crawler-user-agents) 🆓 - Enumera 25 user agents de rastreadores de IA de 12 operadores en cuatro grupos e indica cuántas de 157 plataformas bloquean cada uno en robots.txt. (2026)
- [AI Training Opt-Out](https://github.com/healsdata/ai-training-opt-out) 🆓 🔓 - Recopila las entradas de robots.txt, metaetiquetas y otros ajustes conocidos con los que los propietarios de sitios pueden excluirse del entrenamiento de IA.
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) 🆓 🔓 - Mantiene una lista comunitaria de agentes y rastreadores de IA que bloquear, con archivos robots.txt y de configuración de servidor generados a partir de ella.
- [Amazon Web Search crawlers](https://developer.amazon.com/docs/amazonbot/amazonbot.html) 🆓 - Describe Amazonbot, Amzn-SearchBot y Amzn-User, y las reglas independientes de robots.txt que controlan cada uno de ellos.
- [Cloudflare: What is Pay Per Crawl?](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl) 🆓 - Explica cómo Pay Per Crawl permite a los propietarios cobrar a los rastreadores de IA por el acceso y responder con HTTP 402 a las solicitudes no pagadas; está en beta cerrada.
- [Google User-Triggered Fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) 🆓 - Enumera los fetchers de Google que actúan a petición de un usuario, como Google Read Aloud, y señala que por lo general ignoran las reglas de robots.txt.
- [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) 🆓 - Documenta los rastreadores comunes de Google, incluido Googlebot, con sus cadenas de user agent y tokens de robots.txt.
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots) 🆓 - Enumera unos 40 user agents de robots de Yandex con su finalidad y su comportamiento ante robots.txt, y explica cómo verificarlos mediante DNS inverso.
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about) 🆓 - Normaliza un vocabulario común y mecanismos de vinculación, como robots.txt y cabeceras HTTP, para expresar preferencias sobre cómo recopila y usa la IA el contenido.
- [IETF Web Bot Auth working group](https://datatracker.ietf.org/wg/webbotauth/about) 🆓 - Normaliza métodos para autenticar criptográficamente clientes automatizados, como rastreadores y agentes de IA, en sustitución de las listas de IP permitidas y las cadenas de user agent.
- [Is DuckAssistBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) 🆓 - Explica que DuckAssistBot recopila fuentes para las respuestas asistidas por IA de DuckDuckGo, no se usa para entrenar IA y se puede bloquear en robots.txt.
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) 🆓 - Enumera los rastreadores de Meta, como Meta-WebIndexer para la búsqueda de Meta AI y Meta-ExternalAgent para el entrenamiento de modelos de IA, y para qué sirve cada uno.
- [Mistral crawlers](https://docs.mistral.ai/robots) 🆓 - Describe los user agents MistralAI-User, MistralAI-Index y MistralAI-Training y para qué sirve cada uno.
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) 🆓 - Especifica la sintaxis y la semántica de robots.txt, el protocolo de exclusión de robots que se espera que respeten los rastreadores de IA. (2022)
- [Supporting a shared AI training control for websites](https://developers.google.com/search/blog/2026/10/ai-training-control) 🆓 - Anuncia que Google prevé respetar en robots.txt una exclusión común del entrenamiento de IA basada en un borrador de AIPREF del IETF, con soporte previsto para 2027. (2026)

### Datos estructurados

- [Intro to How Structured Data Markup Works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) 🆓 - Explica cómo usa Google el marcado de datos estructurados para entender el contenido, qué formatos admite y dónde colocar el marcado.
- [JSON-LD](https://json-ld.org) 🆓 - Aloja las especificaciones de JSON-LD, el formato de datos enlazados basado en JSON en el que suele escribirse el marcado Schema.org.
- [Rich Results Test](https://search.google.com/test/rich-results) 🆓 - Prueba una URL o un fragmento de código e indica qué resultados enriquecidos de Google pueden generar sus datos estructurados.
- [Schema Markup Didn't Move AI Citations In Ahrefs Test](https://www.searchenginejournal.com/schema-markup-didnt-move-ai-citations-in-ahrefs-test/574568/) 🆓 - Resume un informe de Ahrefs que comprobó si añadir marcado Schema a páginas ya citadas por la IA mejoraba su tasa de citas. (2026)
- [Schema Markup Validator](https://validator.schema.org) 🆓 - Valida datos estructurados de cualquier tipo de Schema.org en JSON-LD, Microdata o RDFa.
- [Schema.org](https://schema.org) 🆓 - Aloja el vocabulario compartido de tipos y propiedades con el que se marcan las páginas web para buscadores y otros consumidores.
- [schemaorg/schemaorg](https://github.com/schemaorg/schemaorg) 🆓 🔓 - Aloja el código fuente del vocabulario Schema.org y el software que lo acompaña.
- [Structured Data Markup that Google Search Supports](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 🆓 - Cataloga los tipos de datos estructurados que activan funciones en la Búsqueda de Google, con ejemplos e indicaciones de implementación.

### Documentación oficial de los motores

- [About Applebot](https://support.apple.com/en-us/119829) 🆓 - Describe Applebot, que alimenta las funciones de búsqueda de Spotlight, Siri y Safari, y Applebot-Extended, que los editores pueden bloquear para excluirse del entrenamiento de IA generativa.
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) 🆓 - Explica cómo funcionan AI Overviews y AI Mode en la Búsqueda de Google y cómo pueden plantearse los propietarios de sitios la inclusión de su contenido en ellos.
- [Baidu Search Resource Platform](https://ziyuan.baidu.com) 🆓 - Plataforma para webmasters de Baidu con envío de recursos del sitio, datos de rastreo y robots, widgets de búsqueda y análisis del tráfico de IA.
- [Common Crawl - CCBot](https://commoncrawl.org/ccbot) 🆓 - Describe CCBot, el rastreador del archivo web abierto Common Crawl, con su user agent y formas de verificarlo y bloquearlo.
- [Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) 🆓 - Describe los rastreadores ClaudeBot, Claude-User y Claude-SearchBot y cómo pueden bloquear cada uno los propietarios de sitios mediante robots.txt.
- [IndexNow documentation](https://indexnow.org/documentation) 🆓 - Documenta el protocolo IndexNow, que sirve para avisar a los buscadores participantes de URL nuevas, actualizadas o eliminadas.
- [Introducing AI Performance in Bing Webmaster Tools Public Preview](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) 🆓 - Anuncia un informe de Bing Webmaster Tools que muestra cuándo se cita un sitio en las respuestas de Microsoft Copilot y en los resúmenes generados por IA de Bing. (2026)
- [Introducing Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) 🆓 - Anuncia informes de Search Console que muestran con qué frecuencia aparecen las páginas en funciones de IA generativa como AI Overviews y AI Mode, por página, país, dispositivo y fecha. (2026)
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) 🆓 - Anuncia el programa con el que Perplexity comparte ingresos con los medios participantes y les ofrece acceso a la API y ayuda para desarrolladores. (2024)
- [Naver Search Advisor](https://searchadvisor.naver.com/guide) 🆓 - Guía y herramientas para webmasters de Naver sobre lo que necesita un sitio para que Naver Search lo descubra e indexe; AI Briefing usa documentos web del mismo índice.
- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) 🆓 - Describe los user agents OAI-SearchBot, GPTBot, ChatGPT-User y OAI-AdsBot y para qué sirve cada uno.
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) 🆓 - Describe PerplexityBot, que muestra sitios en los resultados de Perplexity, y Perplexity-User, que obtiene páginas a petición del usuario y por lo general ignora el robots.txt.
- [Publishers and Developers FAQ (OpenAI)](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) 🆓 - Responde preguntas de editores y desarrolladores sobre cómo aparecer en ChatGPT Search, el rastreador OAI-SearchBot y el tráfico de referencia desde ChatGPT.
- [Search generative AI control](https://support.google.com/webmasters/answer/16908024) 🆓 - Explica el control de Search Console para incluir o excluir contenido de AI Overviews, AI Mode y la IA generativa de Discover, y aclara que no afecta al entrenamiento de IA.
- [Search with Yandex AI](https://yandex.com/support/search/en/yandex-ai) 🆓 - Página de ayuda de Yandex que explica cómo sus respuestas de IA dividen una pregunta en partes, eligen y analizan fuentes y las enlazan en la respuesta.
- [Top ways to ensure your content performs well in Google's AI experiences on Search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) 🆓 - Recoge las prácticas que recomienda Google para que el contenido funcione bien en sus funciones de IA de la Búsqueda. (2025)
- [Yandex Webmaster](https://webmaster.yandex.com/) 🆓 - Servicio para webmasters de Yandex para verificar sitios, hacer seguimiento de la indexación y diagnosticar problemas de rastreo en Yandex Search.
- [Your content, your choice: clearer preferences for training and grounding](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding) 🆓 - Anuncia preferencias separadas para el entrenamiento y el anclaje (grounding) de IA, que se fijan con robots.txt, metaetiquetas o cabeceras X-Robots-Tag y que Microsoft leerá desde febrero de 2027. (2026)

## Herramientas

### Seguimiento de la visibilidad en IA

- [Ahrefs AI Visibility Checker](https://ahrefs.com/ai-visibility-checker) 🆓 - Comprueba sin registro cómo mencionan y citan una marca ChatGPT, Gemini, Perplexity, Copilot y AI Overviews.
- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) 💲 - Informa de con qué frecuencia aparece una marca en las respuestas de Google AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini y Copilot, con una base de datos de prompts o prompts propios.
- [AthenaHQ](https://athenahq.ai) 🪙 - Sigue la visibilidad de marca en modelos de IA como ChatGPT, Perplexity, Gemini, AI Overviews y Copilot y sugiere cambios de contenido; tiene un plan gratuito con créditos iniciales.
- [Geoptie](https://geoptie.com) 💲 - Muestra cómo responden ChatGPT, Gemini, Claude, Perplexity y Google AI a los prompts de compradores y qué fuentes citan.
- [Goodie](https://higoodie.com) 💲 - Hace seguimiento de la visibilidad de marca en motores de IA como ChatGPT, AI Overviews, Perplexity y Copilot y recomienda optimizaciones; los planes superiores incluyen más motores.
- [HubSpot AI Search Grader](https://www.hubspot.com/aeo-grader) 🪙 - Puntúa en una comprobación gratuita y puntual cómo describen una marca ChatGPT, Perplexity y Gemini; el seguimiento semanal de pago se ofrece como HubSpot AEO.
- [Knowatoa](https://www.knowatoa.com) 💲 - Hace seguimiento de la visibilidad de marca en ChatGPT, Google AI Overviews, AI Mode y otros servicios de búsqueda con IA, con seguimiento de prompts e integraciones de informes.
- [Otterly.AI](https://otterly.ai) 💲 - Hace seguimiento de menciones de marca y citas del sitio web en ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity y Copilot, con comparación con la competencia e investigación de prompts.
- [Peec AI](https://peec.ai) 💲 - Hace seguimiento de la visibilidad, la posición y el sentimiento de una marca en plataformas de búsqueda con IA como ChatGPT, Perplexity, AI Overviews, AI Mode y Gemini, con informes por prompt.
- [Profound](https://www.tryprofound.com) 💲 - Hace seguimiento de la visibilidad de marca en motores de respuestas como ChatGPT, Perplexity, Google AI Mode, Gemini y Claude mediante ejecuciones diarias de prompts y análisis de citas.
- [Promptwatch](https://promptwatch.com) 💲 - Sigue la visibilidad de marca en modelos de IA como ChatGPT, Google AI Overviews, Perplexity, Claude y Gemini ejecutando prompts; los planes superiores añaden analítica de rastreadores de IA.
- [Rankscale](https://rankscale.ai) 💲 - Hace seguimiento de menciones de marca y citas en más de 17 buscadores de IA con planes basados en créditos; los niveles superiores incluyen paneles por marca y una API.
- [Scrunch](https://scrunch.com) 💲 - Hace seguimiento de prompts, citas, posiciones de la competencia y actividad de rastreo de bots de IA en las principales plataformas de IA, y puede servir una versión del sitio optimizada para IA.
- [Searchable](https://www.searchable.com) 💲 - Hace seguimiento de menciones de marca, comparaciones con la competencia y fuentes citadas en ChatGPT, Google AI Overviews y Perplexity, con Claude, Gemini y otros motores como complementos de pago.
- [Semrush AI Visibility Toolkit](https://www.semrush.com/features/ai-visibility/) 💲 - Sigue las menciones y la visibilidad de una marca en ChatGPT, Google AI Mode y otras plataformas de IA mediante prompts y análisis de la competencia; incluido en los planes SEO + AI Search de Semrush.
- [Trakkr](https://trakkr.ai) 💲 - Hace seguimiento de cómo aparece una marca en ocho modelos de IA a partir de prompts; el nivel superior incluye planes multimarca y portales para clientes.
- [Waikay](https://waikay.io) 🪙 - Analiza cómo describen una marca ChatGPT, Google, Claude y Perplexity, señala alucinaciones y lagunas de conocimiento y sugiere planes de acción.
- [Writesonic](https://writesonic.com) 💲 - Sigue la visibilidad de marca en respuestas de IA, con ChatGPT, Gemini y Google AI Overviews en los planes básicos, además de redacción de artículos y correcciones de auditoría del sitio.
- [ZipTie](https://ziptie.ai) 💲 - Hace seguimiento de prompts elegidos en siete motores, entre ellos ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity y Copilot, con precios por uso según cada comprobación.

### Auditoría y optimización de contenidos

- [Clearscope](https://www.clearscope.io) 💲 - Recomienda mejoras de contenido para Google y las respuestas de IA y sigue consultas en ChatGPT y Gemini para mostrar cuándo se menciona una marca.
- [Frase](https://www.frase.io) 💲 - Puntúa el contenido para SEO y GEO y hace seguimiento de la visibilidad de marca en motores de IA como ChatGPT y Google AI; los planes superiores incluyen más motores.
- [GeoReady](https://geoready.dev) 🪙 - Audita si ChatGPT, Perplexity, Claude y Gemini pueden acceder a un sitio, leerlo y citarlo, y lo puntúa sobre 100 en nueve categorías con correcciones priorizadas.
- [NEURONwriter](https://neuronwriter.com) 💲 - Sugiere términos y estructura a partir de las páginas mejor posicionadas para optimizar el contenido para Google y las respuestas de IA, y sigue la cuota de voz de la marca en modelos de IA.
- [Surfer](https://surfer.ai) 💲 - Combina un editor de contenido que puntúa los borradores frente a la competencia con AI Tracker, que sigue las menciones de marca en ChatGPT, Perplexity, Gemini, AI Overviews y AI Mode.

### Herramientas y bibliotecas de código abierto

- [Canonry](https://github.com/Canonry/canonry) 🆓 🔓 - Plataforma operativa orientada a agentes para trabajo de AEO y GEO, distribuida como paquete npm.
- [Elmo](https://github.com/elmohq/elmo) 🆓 🔓 - Plataforma autoalojable que hace seguimiento de cómo mencionan y citan una marca ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok y Google AI Overviews.
- [gego](https://github.com/AI2HU/gego) 🆓 🔓 - Programa prompts en varios proveedores de LLM, recoge las citas de sus búsquedas web y hace seguimiento de las menciones de marca mediante un panel y una CLI.
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) 🆓 🔓 - Puntúa de 0 a 100 si los motores de IA pueden rastrear, entender y citar un sitio, mediante una CLI, una biblioteca de Python y un servidor MCP.
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) 🆓 🔓 - Hace seguimiento de cómo mencionan y citan una marca ChatGPT, Perplexity, Gemini y Google AI Mode, como panel autoalojado con servidor MCP y CLI.
- [geo-check](https://github.com/vasco-branco06/geo-check) 🆓 🔓 - Comprueba si los rastreadores de IA pueden acceder a un sitio web y leerlo, y le asigna una puntuación; se distribuye como paquete de PyPI y GitHub Action.
- [geo-optimizer (Go)](https://github.com/geo-team-red/geo-optimizer) 🆓 🔓 - Framework modular de GEO en Go con estrategias integradas y la posibilidad de registrar otras personalizadas.
- [geoptimize](https://github.com/cucuwang/geoptimize) 🆓 🔓 - Linter de contenido determinista que se ejecuta en CI o pre-commit para señalar problemas de estructura y de fuentes en documentación y sitios estáticos; se publica como paquete npm.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) 🆓 🔓 - Plataforma de código abierto para hacer seguimiento de la presencia de una marca en las respuestas de IA y mejorarla.
- [Limelit Open](https://github.com/limelit-co/open) 🆓 🔓 - Herramienta autoalojada de seguimiento de la visibilidad, un único binario de Go con SQLite y servidor MCP, que registra cómo mencionan y citan una marca los principales motores de IA.
- [NGINX Markdown for Agents](https://github.com/cnkang/nginx-markdown-for-agents) 🆓 🔓 - Módulo de NGINX que sirve versiones en Markdown de las páginas a los agentes de IA mediante negociación de contenido HTTP.
- [OneGlanse](https://github.com/oneglanse/oneglanse) 🆓 🔓 - Herramienta autoalojable que hace seguimiento de cómo mencionan y citan una marca ChatGPT, Perplexity, Gemini, Claude y Google AI Overviews mediante sus interfaces de producto.
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) 🆓 🔓 - Puntúa de 0 a 100 la legibilidad de un sitio para agentes y genera copias en Markdown de las páginas, además de robots.txt, llms.txt y sitemap.xml.
- [react-schemaorg](https://github.com/google/react-schemaorg) 🆓 🔓 - JSON-LD de Schema.org con comprobación de tipos para React.
- [schema-dts](https://github.com/google/schema-dts) 🆓 🔓 - Tipos de TypeScript para escribir JSON-LD de Schema.org.
- [seo-graph](https://github.com/jdevalk/seo-graph) 🆓 🔓 - Construye un grafo JSON-LD de Schema.org para sitios en JavaScript, con integración para Astro.
- [spatie/schema-org](https://github.com/spatie/schema-org) 🆓 🔓 - Constructor fluido en PHP para tipos de Schema.org que genera JSON-LD.

### Generadores de llms.txt

- [agentmarkup](https://github.com/agentmarkup/agentmarkup) 🆓 🔓 - Genera en tiempo de compilación llms.txt, JSON-LD, copias en Markdown y controles para rastreadores de IA en sitios con Vite, Astro, Next.js y Nuxt, y los valida.
- [Apify llms.txt Generator Actor](https://github.com/apify/actor-llmstxt-generator) 🆓 🔓 - Actor de Apify que rastrea un sitio web y extrae su contenido para crear un archivo llms.txt.
- [LLMs.txt Generator](https://llmstxtgenerator.co) 💲 - Rastrea un sitio para generar un borrador de archivo llms.txt, con descubrimiento de páginas, contexto de negocio añadido y actualización diaria del archivo público.
- [llmstxt (dotenvx)](https://github.com/dotenvx/llmstxt) 🆓 🔓 - Herramienta de línea de comandos que convierte un sitemap.xml en un archivo llms.txt.
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) 🆓 🔓 - Plugin de MkDocs que genera un archivo /llms.txt para un sitio de documentación.
- [Nuxt LLMs](https://github.com/nuxt-content/nuxt-llms) 🆓 🔓 - Módulo de Nuxt que genera automáticamente la documentación /llms.txt en Markdown de una aplicación.
- [sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) 🆓 🔓 - Extensión de Sphinx que genera un archivo llms.txt.
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) 🆓 🔓 - Plugin de VitePress que genera archivos de documentación adaptados a los LLM.
- [WordLift llms.txt Generator](https://wordlift.io/generate-llms-txt) 🆓 - Genera un borrador de llms.txt a partir de una página de inicio pública revisando hasta 30 páginas encontradas en el sitemap y los enlaces internos, sin registro.
- [Yoast llms.txt feature](https://yoast.com/features/llms-txt/) 🆓 - Genera y actualiza automáticamente un archivo llms.txt dentro del plugin gratuito Yoast SEO, con selección automática o manual del contenido clave.

### Análisis de logs de rastreadores

- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) 🆓 🔓 - Lista curada de user agents de rastreadores de IA con una CLI de Node y una GitHub Action que auditan el robots.txt, prueban la accesibilidad y leen los logs de acceso.
- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) 🪙 - Muestra qué servicios de IA rastrean un sitio, permite autorizar o bloquear cada rastreador e indica cuáles respetan el robots.txt; disponible en todos los planes de Cloudflare.
- [cloudflare-ai-crawler-tracker](https://github.com/Cairrot-Inc/cloudflare-ai-crawler-tracker) 🆓 🔓 - Cloudflare Worker que detecta y hace seguimiento del tráfico de rastreadores de IA y bots de LLM en el edge.
- [Known Agents](https://knownagents.com) 🪙 - Ofrece un directorio de agentes y bots de IA, un comprobador de robots.txt y analítica de agentes, con un plan gratuito limitado a 100 000 eventos al mes.

## Buscadores y asistentes de IA

Motores de respuestas con IA agrupados por región, con su sitio oficial, documentación para webmasters y los user agents conocidos de sus rastreadores cuando existen.

### Global

- [Bing AI Mode](https://www.bing.com/copilotsearch) 🆓 - Modo de búsqueda conversacional de Microsoft Bing, antes Copilot Search, que en 2026 se dividió en AI Mode y los resúmenes AI Overview que aparecen en los resultados normales.
- [Brave Search](https://brave.com/search/) 🪙 - Buscador de Brave con índice propio e independiente, resúmenes Answer with AI que citan sus fuentes y un modo de chat, Ask Brave, para preguntas de seguimiento.
- [ChatGPT Search](https://chatgpt.com/search) 🪙 - ChatGPT de OpenAI con búsqueda web integrada, que responde preguntas en la conversación y enlaza a las páginas que ha usado.
- [Claude](https://claude.ai) 🪙 - Asistente Claude de Anthropic, que puede buscar en la web durante la conversación y citar las páginas en las que se basa su respuesta.
- [Duck.ai](https://duck.ai) 🪙 - Chat anonimizado de DuckDuckGo con modelos de IA de terceros, accesible desde los resultados de búsqueda; el buscador también ofrece respuestas opcionales asistidas por IA.
- [Gemini](https://gemini.google.com) 🪙 - Asistente de IA Gemini de Google, que recurre a la Búsqueda de Google para incluir información actual en sus respuestas.
- [Google AI Mode](https://search.google/ways-to-search/ai-mode/) 🆓 - Modo conversacional de la Búsqueda de Google, basado en Gemini, que responde preguntas complejas, admite preguntas de seguimiento y enlaza a fuentes de la web.
- [Google AI Overviews](https://search.google/ways-to-search/ai-overviews/) 🆓 - Resúmenes generativos de la Búsqueda de Google que aparecen sobre los resultados normales, con enlaces a las fuentes en que se basan, en más de 120 países y territorios.
- [Grok](https://grok.com) 🪙 - Asistente de IA de xAI, ahora parte de SpaceX, que busca en la web y en las publicaciones de X para responder preguntas sobre la actualidad.
- [Kagi Assistant](https://kagi.com/assistant) 💲 - Asistente de chat de Kagi para miembros de pago, que combina modelos de muchos proveedores con acceso opcional a los resultados de búsqueda sin anuncios de Kagi.
- [Meta AI](https://www.meta.ai) 🪙 - Asistente de IA de Meta en la web y dentro de WhatsApp, Instagram y Facebook, que puede incorporar resultados de búsqueda web para preguntas actuales.
- [Microsoft Copilot](https://copilot.microsoft.com) 🪙 - Asistente Copilot de Microsoft para consumidores, que usa resultados web de Bing para responder y cita las páginas en que se basa.
- [Perplexity](https://www.perplexity.ai) 🪙 - Motor de respuestas con IA que busca en la web en tiempo real y ofrece respuestas conversacionales con citas numeradas de las fuentes.

### China

- [ChatGLM](https://chatglm.cn) 🆓 - Asistente chino de Zhipu AI (Zhipu Qingyan), basado en sus modelos GLM, con búsqueda web y funciones de agente.
- [DeepSeek](https://www.deepseek.com) 🆓 - Asistente de chat de DeepSeek basado en sus modelos de pesos abiertos, con un modo opcional de búsqueda web para obtener respuestas actualizadas.
- [Doubao](https://www.doubao.com) 🆓 - Asistente de IA de uso general de ByteDance, que busca en la web para responder en el chat y muestra las fuentes consultadas.
- [ERNIE Bot](https://wenxin.baidu.com) 🆓 - Asistente ERNIE Bot de Baidu (antes Wenxin Yiyan), que ahora se ofrece en la web como Baidu Wenxin Assistant y está conectado a Baidu Search.
- [Kimi](https://www.kimi.com) 🪙 - Asistente Kimi de Moonshot AI, conocido por su lectura de contextos largos, que busca en la web y cita las páginas que lee.
- [Metaso](https://metaso.cn) 🪙 - Buscador chino de IA sin anuncios de MetaSOTA, que responde con fuentes citadas y también permite buscar literatura académica.
- [Quark](https://www.quark.cn) 🪙 - Quark de Alibaba, una aplicación de búsqueda y navegador rediseñada en torno a un asistente de IA que responde a las consultas con resultados generados.
- [Qwen](https://www.qianwen.com) 🆓 - Aplicación Qwen de Alibaba (antes Tongyi), un asistente de IA basado en sus modelos Qwen con búsqueda web; la versión web internacional es Qwen Chat.
- [Tencent Yuanbao](https://yuanbao.tencent.com) 🆓 - Asistente de IA de Tencent, que responde con resultados de búsqueda web que incluyen artículos de cuentas oficiales de WeChat.
- [Yuanbao Search](https://so.qq.com) 🆓 - Sitio de búsqueda web con IA de Tencent que cita sus fuentes, permite buscar contenido de las cuentas oficiales y de Channels de WeChat y ofrece un modo de IA para preguntas de seguimiento.

### Japón

- [Agent i](https://search.yahoo.co.jp/chat) 🆓 - Agente de IA de LY Corporation, lanzado en abril de 2026 al fusionar el AI Assistant de Yahoo! JAPAN Search y LINE AI, accesible desde el cuadro de búsqueda de Yahoo! JAPAN y LINE.
- [Felo](https://felo.ai) 🪙 - Buscador de IA multilingüe de una startup de Tokio que responde con citas y puede buscar fuentes en varios idiomas.

### Corea del Sur

- [A. (A-dot)](https://adot.ai) 🆓 - Asistente personal de IA de SK Telecom que ofrece, junto a varios modelos de chat, una función de búsqueda con IA desarrollada con Perplexity.
- [Kanana](https://kanana.ai) 🆓 - Marca de IA de Kakao que abarca el asistente Kanana in KakaoTalk y los modelos de código abierto Kanana, con el agente Kanana Space, basado en KakaoTalk, anunciado en octubre de 2026.
- [Liner](https://liner.com) 🪙 - Buscador y asistente de investigación con IA de una empresa con sede en Seúl, centrado en respuestas con citas y fuentes académicas.
- [Naver AI Briefing](https://www.navercorp.com/story/storyDetail?seq=32525) 🆓 - Respuestas generativas de Naver Search basadas en HyperCLOVA X, que resumen los resultados en la parte superior de la página y muestran el contenido de origen que han usado.
- [Naver AI Tab](https://www.navercorp.com/media/pressReleasesDetail?seq=10034429) 🆓 - Pestaña de búsqueda conversacional con IA de Naver, abierta a todos los usuarios en junio de 2026, que responde en forma de diálogo con fichas de productos, lugares y reservas.
- [Wrtn](https://wrtn.ai) 🆓 - Asistente de IA coreano de Wrtn Technologies, con una función gratuita de búsqueda con IA que responde a partir de resultados web en tiempo real y muestra sus fuentes.

### Europa

- [Ecosia AI search](https://www.ecosia.org) 🆓 - Funciones de búsqueda con IA de Ecosia, el buscador con sede en Berlín que financia la plantación de árboles; se pueden desactivar para obtener resultados sin IA.
- [Lumo](https://lumo.proton.me) 🪙 - Asistente de IA de Proton centrado en la privacidad y con sede en Suiza, con búsqueda web integrada, que no usa las consultas para segmentar anuncios.
- [Mistral Vibe](https://mistral.ai/products/vibe/) 🪙 - Asistente de Mistral AI, que pasó de llamarse Le Chat a Vibe y combina un asistente de chat con búsqueda web y un agente de programación.

### Otras regiones

- [Alice AI](https://alice.yandex.ru) 🆓 - Asistente Alice AI de Yandex, cuyos modelos también generan las respuestas de IA con enlaces a fuentes de Yandex Search.

## Recursos de GEO en otros idiomas

Artículos, comunidades y herramientas locales publicados en idiomas distintos del inglés; no se incluyen agencias ni proveedores de servicios.

### En chino

- [生成式引擎优化实践中的风险与信息生态重塑](https://airaxiv.com/papers/pdf/2509.0006/) 🆓 - Preprint en chino sobre los riesgos éticos del GEO, como la propiedad intelectual, el sesgo algorítmico, la explicabilidad y la desinformación, con cinco medidas propuestas. (2025)
- [AIIA可信GEO专题研讨会在京成功召开](https://www.xinhuanet.com/digital/20260518/5b81c242155a44da9a69d69f90410c57/c.html) 🆓 - Crónica de Xinhua sobre el seminario de la AIIA de mayo de 2026 sobre GEO fiable: evaluaciones de servicios de GEO de la CAICT, un informe sobre riesgos del GEO y autorregulación del sector. (2026)
- [T/CAAAD 046—2026 生成式引擎优化服务要求](https://digitalad.china-caa.org/TechLab/pdf/TCAAAD%20046-2026.pdf) 🆓 - Norma de grupo de la Asociación de Publicidad de China que fija requisitos para proveedores de servicios de GEO, fuentes de contenido fiables, técnicas prohibidas e informes de resultados. (2026)
- [为什么说GEO正在摧毁AI营销？](https://www.36kr.com/p/3701404201677189) 🆓 - Reportaje sobre el auge del GEO en China en 2026: cómo actúa sobre la fase de recuperación de las respuestas de IA y cómo la siembra masiva de contenido coló un producto falso en sus recomendaciones. (2026)
- [对AI投毒说不！可信GEO的破局之道](https://hunan.voc.com.cn/news/202610/33940183.html) 🆓 - Análisis extenso del envenenamiento de datos de IA con GEO de sombrero negro, que trata la regulación y contramedidas de las plataformas e incluye el servicio de GEO fiable del propio Hunan Daily. (2026)
- [谷歌对“AI投毒”重拳出击](https://www.huxiu.com/article/4861290.html) 🆓 - Análisis de la actualización de 2026 de la política de spam de Google contra la manipulación de respuestas de IA, que distingue el GEO de la siembra pagada de contenido y aborda las zonas grises. (2026)

### En japonés

- [AI Overviews・AI ModeのCTRは検索全体の2倍以上、28日間のオプトアウト実験で推定](https://www.suzukikenichi.com/blog/ctr-for-ai-overviews-and-ai-mode-estimated-at-more-than-double-the-site-wide-search-ctr-in-a-28-day-opt-out-experiment/) 🆓 - Relato de una prueba de 28 días que excluyó un sitio de AI Overviews y AI Mode y estimó que la tasa de clics de ambas funciones era más del doble de la media del sitio. (2026)
- [AI 概要で検索 1 位の CTR が半年で -62.7 % に激減](https://ahrefs.com/ja/blog/ai-overviews-reduce-clicks-june-2026/) 🆓 - Estudio de Ahrefs sobre palabras clave informativas en japonés que estima que AI Overviews redujo un 62,7 % el CTR del primer resultado hasta junio de 2026. (2026)
- [AI検索で推される企業と外される企業 AIOで重要なたった一つのこと](https://xtrend.nikkei.com/atcl/contents/18/01354/00001/) 💲 - Primera parte de una serie de Nikkei xTrend sobre optimización para la búsqueda con IA, con datos de Ahrefs sobre cómo AI Overviews reduce los clics en Japón; casi todo es para miembros de pago. (2026)
- [Google 検索における「AI モード」を日本語で提供開始](https://blog.google/intl/ja-jp/products/explore-get-answers/ai-mode-search/) 🆓 - Anuncio de Google Japón del lanzamiento de AI Mode en japonés, que describe cómo su técnica de query fan-out divide una pregunta en subtemas y lanza una búsqueda para cada uno. (2025)
- [そのGEO／LLMO間違ってるかも！？ AI検索時代でも変わらない「王道SEO」に取り組むべき理由](https://webtan.impress.co.jp/e/2026/08/24/52930) 🆓 - Crónica de una charla de Kenichi Suzuki que sostiene que el GEO y el LLMO se basan en el SEO convencional, con un modelo conceptual de cómo construye sus respuestas la búsqueda con IA de Google. (2026)
- [生成AIに自社情報を引用されやすくする「LLMO」、SEOとの違いと対策](https://xtech.nikkei.com/atcl/nxt/column/18/01679/073000298/) 🆓 - Texto divulgativo de Nikkei xTECH sobre el LLMO, término muy usado en Japón para el GEO, y en qué se diferencia del SEO; para leerlo completo hace falta un registro gratuito. (2026)

### En coreano

- [AI 브라우저 시대, 뉴스 유통 구조 변화와 언론사 수익 모델 재편](https://www.kpf.or.kr/front/research/trendDetail.do?seq=600699) 🆓 - Informe de la Korea Press Foundation sobre cómo los navegadores con IA y las respuestas sin clic transforman la distribución de noticias y los modelos de ingresos de los medios. (2026)
- [AI로 뉴스를 검색하는 시대, 영국 CMA의 구글 규제와 의미](https://www.kpf.or.kr/front/board/boardContentsView.do?board_id=246&contents_id=662358c31eb94c8eba60267a69ab3262) 🆓 - Informe de la Korea Press Foundation sobre lo que la CMA británica exigió a Google en 2026, como exclusión de la IA, datos de búsqueda con IA y atribución de fuentes, y lo que supone para Corea. (2026)
- [From SEO to GEO: 미국 디지털 마케팅의 새로운 전쟁터](https://www.kaa.or.kr/k/mag/2025/winter/KAA_journal_2025_winter_Chapter4_3.pdf) 🆓 - Reseña de tendencias en la revista de la Federación Coreana de Asociaciones de Publicidad que presenta el GEO, cómo usan datos de búsqueda motores como Perplexity y Gemini y el papel del E-E-A-T. (2025)
- [SEO를 넘어 GEO로, 생성형 AI 시대 이커머스 대응 전략](https://www.tosspayments.com/blog/articles/39461) 🆓 - Guía de GEO para tiendas en línea de una empresa coreana de pagos, con cinco tácticas como contenido de preguntas y respuestas, descripciones por caso de uso, FAQ y menciones externas. (2025)
- [네이버, AI 브리핑 도입 이후 창작자 지원 규모 약 2배 확대](https://navercorp.com/media/pressReleasesDetail?seq=10034578) 🆓 - Nota de prensa de Naver sobre cómo AI Briefing muestra publicaciones de creadores como fuentes y sobre Naver Mate, que paga a unos 3000 creadores al mes según las citas en AI Briefing. (2026)
- [생성형 엔진 최적화(GEO), 검색의 규칙을 어떻게 바꾸는가](https://news.hada.io/topic?id=21260) 🆓 - Entrada de GeekNews que resume en coreano el ensayo de a16z sobre GEO, con un breve debate de los lectores sobre cómo se solapan los términos GEO y AEO. (2025)

### En español

- [Generative Engine Optimization (GEO) y visibilidad de marcas en recomendaciones turísticas generadas por IA](https://revistaprismasocial.es/ps/article/view/5975) 🆓 - Estudio exploratorio que lanzó una consulta genérica de viajes en varios sistemas de IA en tres momentos y halló una gran volatilidad en la visibilidad de las marcas hoteleras y las fuentes citadas. (2026)
- [Generative Engine Optimization (GEO): revisión de enfoques, métricas y estrategias](https://www.ibersid.eu/ojs/index.php/ibersid/article/view/5156) 🆓 - Revisa la literatura sobre GEO y constata que converge en métricas de visibilidad, influencia y verificabilidad y en estrategias recurrentes como la estructura, los datos estructurados y la autoridad. (2026)
- [Google AI Overviews y los medios](https://thinkepi.scimagoepi.com/index.php/ThinkEPI/en/article/view/91722) 🆓 - Sostiene que AI Overviews y AI Mode han reducido mucho el tráfico de los medios de noticias españoles y que los editores deberían sumar GEO, fidelización de lectores y licencias colectivas. (2026)
- [Generative Engine Optimization en repositorios digitales: optimización de la visibilidad para la IA generativa](https://doi.org/10.3145/infonomy.25.034) 🆓 - Propone las primeras pautas de GEO para repositorios institucionales, que abarcan configuración técnica, estructura semántica, metadatos, contenido multilingüe y nuevas métricas. (2025)
- [Cuáles son los medios más citados por la IA en España](https://ahrefs.com/blog/es/top-medios-citados-ia/) 🆓 - Análisis de 2,26 millones de prompts en español que clasifica los medios de noticias más citados por ChatGPT, Gemini, Perplexity, Copilot, Grok y las funciones de IA de Google. (2026)
- [Impacto de AI Overviews en España: Google activa resúmenes generativos en el 29,8% de búsquedas sobre medios](https://laboratoriodeperiodismo.org/impacto-de-ai-overviews-en-espana-google-activa-resumenes-generativos-en-el-298-de-busquedas-sobre-medios/) 🆓 - Resume un estudio de la Universidad de Barcelona sobre 2699 palabras clave: AI Overviews aparece en el 29,8 % de las búsquedas sobre grandes medios españoles, pero rara vez en noticias de última hora. (2026)

### En alemán

- [BVDW Whitepaper: The Answer Economy](https://www.bvdw.org/news-und-publikationen/bvdw-ordnet-ki-getriebenen-wandel-der-informationsoekonomie-ein/) 🆓 - Informe técnico de la asociación alemana del sector digital sobre el paso de la búsqueda a los sistemas de respuestas con IA, con una propuesta de definición estándar de GEO y su relación con el SEO. (2026)
- [ChatGPT Core Updates: Auch Chatbots haben Algorithmus-Änderungen](https://www.sistrix.de/news/chatgpt-core-update/) 🆓 - Análisis de 3,8 millones de respuestas de ChatGPT en alemán que muestra que un cambio de modelo en mayo de 2026 alteró en un 47 % la combinación de dominios citados en dos días. (2026)
- [ChatGPT, Perplexity & Co.: Diese Quellen nutzen KI-Tools am häufigsten](https://t3n.de/news/chatgpt-perplexity-co-diese-quellen-nutzen-ki-tools-am-haeufigsten-und-das-ist-ein-problem-1754013/) 🆓 - Artículo sobre un estudio de 250 000 respuestas de IA que muestra cuáles son las fuentes más citadas por ChatGPT, AI Overviews y Perplexity, encabezadas por webs corporativas, YouTube y Reddit. (2026)
- [GEO und Technik für Websites: Wie sich der KI-Chatbot Infos sucht](https://t3n.de/news/geo-und-website-check-wie-sich-der-ki-chatbot-infos-sucht-und-was-unternehmen-daraus-lernen-koennen-1766802/) 🆓 - Explica cómo encuentran y citan páginas ChatGPT, Gemini, Copilot y Perplexity, desde el query fan-out y los índices de búsqueda hasta el acceso técnico, con una lista de verificación para empresas. (2026)
- [GEO-Mythen im Datencheck: Was 96.418 URLs über AI-Citations verraten](https://www.sistrix.de/news/geo-mythen-im-datencheck/) 🆓 - Compara páginas citadas y no citadas de los mismos dominios en respuestas de IA de la región DACH: la estructura y el marcado Schema se correlacionan con las citas, mientras que llms.txt no influye. (2026)
- [Search im Umbruch: Die neun wichtigsten GEO-KPI](https://www.bvdw.org/news-und-publikationen/die-neun-wichtigsten-geo-kpi/) 🆓 - Breve informe técnico de la BVDW que propone nueve KPI para medir la visibilidad de marca en la búsqueda generativa, con consejos sobre conjuntos de prompts y revisión periódica. (2026)

## Estudios de caso

- [Does AI Search Traffic Convert Better Than Traditional Search? For Ahrefs, Yes](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) 🆓 - Comparte datos de analítica de Ahrefs que muestran que los visitantes procedentes de la búsqueda con IA eran el 0,5 % de su tráfico, pero el 12,1 % de sus registros. (2025)
- [How Ramp increased AI brand visibility 7x in accounts payable](https://www.tryprofound.com/customers/ramp-case-study) 🆓 - Estudio de caso de un proveedor: la visibilidad en la búsqueda con IA del producto de cuentas por pagar de Ramp, medida con Profound, subió al 22,2 %, con las páginas y consultas que Ramp priorizó. (2025)
- [How Vercel's adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search) 🆓 - Describe cómo adapta Vercel su SEO al descubrimiento por LLM e indica que ChatGPT generó cerca del 10 % de sus nuevos registros, frente al 1 % de seis meses antes. (2025)

## Cursos, videos y podcasts

- [Ahrefs Answer Engine Optimization (AEO) Course](https://ahrefs.com/academy/aeo-course) 🆓 - Curso gratuito de 12 lecciones en video de Sam Oh sobre cómo eligen citas los buscadores de IA, investigación de prompts, contenido y YouTube, configuración técnica y seguimiento del tráfico de IA.
- [AI SEO: Mastering Generative Engine Optimization (GEO)](https://www.coursera.org/learn/seo-mastering-generative-engine-optimization-geo) 🪙 - Curso de Coursera de cuatro horas de SkillUp en dos módulos sobre entidades y autoridad temática, formatos de contenido aptos para IA, métricas de GEO y prácticas; el certificado es de pago.
- [HubSpot Academy AEO Fundamentals](https://academy.hubspot.com/courses/aeo-fundamentals-certification-en) 🆓 - Curso gratuito con certificado de siete lecciones sobre cómo lograr citas de motores de respuestas, análisis de preguntas, on-page y Schema, y medición del tráfico de referencia de IA y cuota de voz.
- [Learning AI Search](https://learningaisearch.com/) 🆓 - Itinerario gratuito de Aleyda Solis que ordena guías sobre fundamentos de la búsqueda con IA, medición, comercio electrónico y herramientas, con una lista de verificación para optimizar el contenido.
- [Muck Rack Fundamentals of Generative Engine Optimization (GEO)](https://academy.muckrack.com/fundamentals-of-generative-engine-optimization-geo) 🆓 - Curso breve con certificado para equipos de relaciones públicas y comunicación sobre cómo influyen los medios ganados en las respuestas de IA, pruebas de prompts y datos de GEO para elegir medios.
- [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) 🆓 - Pódcast del equipo de Search Relations de Google sobre el funcionamiento interno de la Búsqueda de Google, incluidas sus funciones de IA y temas de actualidad de la comunidad SEO.
- [Semrush Academy AI Visibility Essentials](https://www.semrush.com/academy/courses/ai-visibility-essentials-with-semrush/) 🆓 - Curso gratuito de 20 videos con certificado sobre investigación de prompts, cuota de voz, menciones de marca y formato del contenido para LLM; varias lecciones muestran herramientas de Semrush.

## Boletines y comunidades

- [AI Search Leaders](https://newsletter.searchleaders.ai/) 🆓 - Boletín en Substack de Tom Critchlow, antes llamado The SEO MBA, sobre estrategia y liderazgo para equipos de búsqueda que se adaptan a la búsqueda con IA.
- [brightonSEO](https://brightonseo.com/) 💲 - Serie de grandes conferencias de marketing de búsqueda en Brighton y San Diego, con charlas y cursos sobre SEO, contenido y búsqueda con IA, y un sorteo gratuito de entradas para el evento británico.
- [GEO Conference](https://geo-conference.com/) 💲 - Serie de conferencias presenciales de un día sobre optimización para motores generativos en ciudades de EE. UU., de 150 plazas como máximo y patrocinadas sobre todo por proveedores de GEO y SEO.
- [Growth Memo](https://www.growth-memo.com/) 🪙 - Boletín de Kevin Indig sobre crecimiento orgánico, con estudios de datos periódicos sobre el comportamiento de la búsqueda con IA, las citas y el tráfico; algunos números son de pago.
- [MozCon](https://moz.com/mozcon) 💲 - Conferencia de marketing de Moz sobre SEO, búsqueda con IA y GEO, celebrada en 2026 como gira presencial con eventos en Londres y Nueva York.
- [Search Engine Roundtable](https://www.seroundtable.com/) 🆓 - Sitio de noticias diario de Barry Schwartz que sigue los debates de la comunidad de búsqueda y los cambios en Google y Bing, incluidas sus funciones de búsqueda con IA.
- [SEOFOMO](https://seofomo.co/) 🆓 - Boletín semanal de Aleyda Solis que recopila noticias, guías, herramientas, eventos y empleos de SEO y búsqueda con IA.

## Otras listas curadas

Listas sobre GEO y búsqueda con IA que abarcan temas afines a esta, mencionadas aquí con agradecimiento.

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) 🆓 🔓 - Lista amplia de recursos de GEO con guías por plataforma, comercio agéntico, herramientas, investigación, boletines, videos y eventos.
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) 🆓 🔓 - Lista de artículos de investigación sobre GEO, ordenados por año.
- [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) 🆓 🔓 - Lista de plataformas gratuitas y repositorios de código abierto para GEO, con puntuaciones, búsqueda y herramientas gratuitas en un sitio web complementario.
- [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) 🆓 🔓 - Directorio alfabético de herramientas de GEO y de seguimiento de la visibilidad en IA, con breves notas sobre funciones y precios.
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) 🆓 🔓 - Lista general de GEO con recursos de aprendizaje, herramientas, buscadores de IA, estrategias, seguimiento, estudios de caso, comunidades y novedades de plataformas.
- [marketingtoolslist/awesome-geo](https://github.com/marketingtoolslist/awesome-geo) 🆓 🔓 - Lista de GEO (antes Tusko/awesome-geo) con investigación, documentación oficial de plataformas, guías, herramientas, cursos, boletines y comunidades.
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) 🆓 🔓 - Tabla comparativa de herramientas de GEO según motores cubiertos, frecuencia de actualización, precio y exportación de datos, mantenida por un proveedor de GEO que también se incluye a sí mismo.

## Cómo contribuir

Las contribuciones son bienvenidas. Antes de abrir un pull request, lee la [guía de contribución](CONTRIBUTING.md); basta con escribir la descripción en inglés y los mantenedores añaden el resto de idiomas.

## Licencia

En la medida en que lo permita la ley, los colaboradores han renunciado a todos los derechos de autor y derechos conexos sobre esta lista conforme a [CC0 1.0 Universal](LICENSE).
