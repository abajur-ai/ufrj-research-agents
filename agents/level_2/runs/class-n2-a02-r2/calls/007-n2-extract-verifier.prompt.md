# Verificador da extração de dados
Você é um verificador independente, com busca na web. Para CADA artigo da lista final: abra o resumo na página
oficial e confira se o trecho entre aspas está no resumo, letra por letra (diferença só de aspas, pontuação ou
espaço é aceitável); se a amostra informada aparece no resumo como escrita; se o método e o tipo de estudo estão
certos; e se o achado principal diz o que o resumo diz, sem exagerar nem acrescentar. Confira também se DOI, título,
ano e periódico continuam certos. Reprove qualquer citação parafraseada, número de amostra que não está no resumo ou
achado que vai além do resumo, e diga em qual artigo.

COMO RESPONDER
- approved: false só por ERRO REAL que compromete o resultado (dado errado, critério do pedido violado ou
  esquecido, fonte que não existe, citação que não está na fonte, afirmação que a fonte não sustenta).
  Sugestão de melhoria, preferência de estilo ou cobertura que poderia ser maior não reprova: aprove e ponha a
  sugestão em feedback.
- checked: o que você conferiu, um item por linha, concreto (por exemplo: 'DOI 10.x abre e o título confere').
- issues: cada problema numa frase curta que um estudante entenda: o que está errado ou faltou, e onde.
- feedback: o que o executor precisa fazer na próxima tentativa.
- Escreva em português do Brasil, sem travessão.

PEDIDO DO PESQUISADOR:
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre organizações brasileiras de checagem de fatos (fact-checking), como Agência Lupa, Aos Fatos, Estadão Verifica, Fato ou Fake e Comprova, e suas rotinas, métodos, critérios, fontes, transparência, financiamento ou uso de inteligência artificial. Restrições: estudos empíricos (entrevistas, questionários, análise de conteúdo ou análise documental) sobre a prática das organizações; estudos comparativos internacionais valem se incluírem organizações brasileiras; exclua estudos centrados em eleições, em governos específicos ou na pandemia de COVID-19 e estudos sobre o efeito das checagens no público. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

LISTA FINAL A VERIFICAR:
{
 "items": [
  {
   "doi": "10.25200/bjr.v16n2.2020.1212",
   "title": "JOURNALISM AND FACT-CHECKING: typification of sources used for checking and criteria for selecting fact-checked material – an analysis by Agência Lupa and Aos Fatos",
   "authors": [
    "Daniel de Rezende Damasceno",
    "Edgard Patrício"
   ],
   "year": 2020,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico de análise da atuação de duas agências brasileiras de checagem",
   "method": "Análise das checagens da Agência Lupa e do Aos Fatos; o resumo não descreve coleta nem técnica de análise (não informado no resumo)",
   "sample_size": "não informado no resumo",
   "main_finding": "As agências não explicitam os critérios de seleção do que checam e dependem sobretudo de dados e estudos de fontes oficiais e instituições públicas.",
   "abstract_quote": "the agencies themselves do not lay out the criteria for selecting what is to be checked"
  },
  {
   "doi": "10.25200/bjr.v18n2.2022.1510",
   "title": "The Brazilian factcheckers criteria: an analysis of the guiding purposes, principles, and routines of this journalistic practice",
   "authors": [
    "Carlos Rodríguez-Pérez",
    "Taís Seibt"
   ],
   "year": 2022,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico quantitativo (levantamento)",
   "method": "Questionário autoaplicado com checadores brasileiros, que indicaram o grau de concordância com afirmações",
   "sample_size": "The sample (n=29) expressed their level of agreement with a group of statements.",
   "main_finding": "O propósito central dos checadores brasileiros é detectar e combater conteúdo falso e enganoso nos canais digitais.",
   "abstract_quote": "The results show the central purpose is to detect and combat false and misleading content on digital channels."
  },
  {
   "doi": "10.13037/ci.vol21n46.6388",
   "title": "AGÊNCIA LUPA: FACT-CHECKING COMO MODELO DE NEGÓCIO NA INTERNET",
   "authors": [
    "Jacqueline Lima Dourado",
    "Marta Thaís Alencar"
   ],
   "year": 2020,
   "venue": "Comunicação & Inovação",
   "study_type": "não informado no resumo (referencial da Economia Política do Jornalismo)",
   "method": "não informado no resumo",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo não traz resultado. Só declara o objetivo de analisar a mercantilização das checagens da Agência Lupa para veículos de comunicação. É candidato fraco, porque não há evidência no resumo de dados próprios.",
   "abstract_quote": "o presente artigo tem como objetivo analisar a mercantilização das checagens da Agência Lupa"
  },
  {
   "doi": "10.22478/ufpb.2763-9398.2022v17n.63545",
   "title": "Fact-checking e financiamento: os projetos da Agência Lupa no combate à desinformação",
   "authors": [
    "Lizete Nóbrega",
    "Luciana Miranda Costa",
    "Antonino Condorelli"
   ],
   "year": 2022,
   "venue": "Culturas Midiáticas",
   "study_type": "Estudo de caso (análise documental das iniciativas)",
   "method": "Estudo de caso que identifica e analisa as iniciativas da Agência Lupa ao longo de 2020, com suas potencialidades e limites",
   "sample_size": "não informado no resumo",
   "main_finding": "O estudo identifica as estratégias da Lupa para garantir financiamento por meio de projetos especiais, apontando potencialidades e limites da prática.",
   "abstract_quote": "as estratégias da Agência Lupa para garantir o financiamento do combate à desinformação por meio de projetos especiais"
  },
  {
   "doi": "10.25200/bjr.v20n3.2024.1687",
   "title": "TRANSPARÊNCIA CONTRA A DESINFORMAÇÃO? Análise de como as agências Lupa e Aos Fatos usam mecanismos de transparência pública na verificação de conteúdos duvidosos disseminados digitalmente",
   "authors": [
    "Thatiany Nascimento",
    "Diógenes Lycarião",
    "Suzete Nocrato"
   ],
   "year": 2024,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico quantitativo (análise de conteúdo)",
   "method": "Análise de conteúdo das checagens de 2022 da Lupa e do Aos Fatos para identificar o uso de ferramentas de transparência pública",
   "sample_size": "Through content analysis, 63 checks were identified using transparency tools, which represented less than 7% of the total checks conducted (950).",
   "main_finding": "As ferramentas de transparência pública aparecem em menos de 7% das checagens, mas são decisivas nas que envolvem sujeitos, agentes e autoridades públicas.",
   "abstract_quote": "However, such tools proved decisive for verifications involving subjects, agents, and public authorities."
  },
  {
   "doi": "10.1177/10776990231207963",
   "title": "Fostering Artificial Intelligence to Face Misinformation: Discourses and Practices of Automated Fact-Checking in Brazil",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2024,
   "venue": "Journalism & Mass Communication Quarterly",
   "study_type": "Estudo empírico qualitativo",
   "method": "Análise documental de declarações oficiais e entrevistas semiestruturadas com representantes de sites brasileiros de checagem",
   "sample_size": "30 official statements published by journalists and their tech partners; seven semi-structured interviews with representatives from five websites",
   "main_finding": "Há um cenário emergente de automação no fact-checking brasileiro, apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores.",
   "abstract_quote": "This article shows an emerging automation landscape in the Brazilian fact-checking venture supported by the tech industry."
  },
  {
   "doi": "10.1177/27523543251344971",
   "title": "AI-Generated Misinformation: A Case Study on Emerging Trends in Fact-Checking Practices Across Brazil, Germany, and the United Kingdom",
   "authors": [
    "Regina Cazzamatta",
    "Aynur Sarısakaloğlu"
   ],
   "year": 2025,
   "venue": "Emerging Media",
   "study_type": "Estudo de caso comparativo de métodos mistos",
   "method": "Análise de conteúdo quantitativa de artigos de verificação combinada com entrevistas com especialistas",
   "sample_size": "a quantitative content analysis of 136 verification articles (2023–2024) and 13 expert interviews",
   "main_finding": "Há variações por país em temas, alvos, intenções, elementos de IA, modelos generativos, métodos de detecção e estratégias de desmentido de desinformação gerada por IA.",
   "abstract_quote": "The results revealed notable country-specific variations in topics, targets, intentions, AI elements, generative models,"
  },
  {
   "doi": "10.3390/socsci14090514",
   "title": "On Fact-Checking Service: Artificial Intelligence's Uses in Ibero-American Fact-Checkers",
   "authors": [
    "João Canavilhas",
    "Liliane Ito"
   ],
   "year": 2025,
   "venue": "Social Sciences",
   "study_type": "Estudo empírico qualitativo",
   "method": "Entrevistas em profundidade com representantes de organizações de checagem",
   "sample_size": "in-depth interviews were conducted with representatives of four fact-checking organizations (Polígrafo, Chequeado, Maldita e Aletheia, esta do Brasil); número de entrevistados não informado no resumo",
   "main_finding": "Cada organização usa a IA para necessidades específicas, em níveis que vão de ferramentas simples a usos disruptivos e que acompanham sua estrutura de pessoal e situação econômica.",
   "abstract_quote": "each organization uses these technologies to respond to specific needs"
  },
  {
   "doi": "10.13037/ci.vol25n53.8624",
   "title": "MERCANTILIZAÇÃO DA CHECAGEM NAS AGÊNCIAS CHEQUEADO E LUPA NA AMÉRICA LATINA",
   "authors": [
    "Marta Thaís Alencar",
    "Maria Clara Aquino Bittencourt"
   ],
   "year": 2022,
   "venue": "Comunicação & Inovação",
   "study_type": "Estudo comparativo de duas agências",
   "method": "Estudo comparativo das agências Lupa (Brasil) e Chequeado (Argentina); o resumo não detalha técnica de coleta",
   "sample_size": "não informado no resumo (duas agências comparadas)",
   "main_finding": "O fact-checking na América Latina é um modelo de negócio adotado pelas iniciativas e promove o empreendedorismo jornalístico.",
   "abstract_quote": "o fact-checking na América Latina é um modelo de negócio"
  },
  {
   "doi": "10.1080/1461670X.2022.2069588",
   "title": "The Rise of the Brazilian Fact-checking Movement: Between Economic Sustainability and Editorial Independence",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2022,
   "venue": "Journalism Studies",
   "study_type": "Estudo empírico qualitativo",
   "method": "Entrevistas semiestruturadas, com dados complementares dos sites das organizações",
   "sample_size": "semi-structured interviews with 16 fact-checkers from 13 active organizations",
   "main_finding": "A principal estratégia de viabilidade econômica das organizações brasileiras é ter presença sólida nas plataformas digitais, e a dependência do dinheiro das big techs leva a priorizar o debunking em vez da checagem política.",
   "abstract_quote": "their chief business strategy to gain economic viability mainly translates into a solid presence on digital platforms"
  },
  {
   "doi": "10.17645/mac.v9i1.3443",
   "title": "Fact-Checking Interventions as Counteroffensives to Disinformation Growth: Standards, Values, and Practices in Latin America and Spain",
   "authors": [
    "Victoria Moreno-Gil",
    "Xavier Ramon",
    "Ruth Rodríguez-Martínez"
   ],
   "year": 2021,
   "venue": "Media and Communication",
   "study_type": "Estudo empírico qualitativo comparativo (inclui a Agência Lupa)",
   "method": "Entrevistas em profundidade com gestores de plataformas independentes de checagem",
   "sample_size": "não informado no resumo (o resumo lista oito plataformas, entre elas a Agência Lupa, mas não o número de entrevistados)",
   "main_finding": "Os gestores relatam três desafios centrais na prática de checagem, entre eles a dificuldade de acesso a dados públicos, e todos usam metodologias robustas apesar das equipes pequenas.",
   "abstract_quote": "Interviewees identified three core challenges in fact-checking practice:"
  },
  {
   "doi": "10.5209/esmp.71235",
   "title": "Disputed credibility in digital journalism (Credibilidad en disputa en periodismo digital)",
   "authors": [
    "Thales Vilela Lelo",
    "Fernando Pachi Filho"
   ],
   "year": 2021,
   "venue": "Estudios sobre el Mensaje Periodístico",
   "study_type": "Estudo empírico qualitativo (análise documental e de discurso)",
   "method": "Análise de discurso de linha francesa dos textos de apresentação e das descrições de métodos de trabalho das organizações",
   "sample_size": "five Brazilian fact-checking organizations from media conglomerates",
   "main_finding": "O estudo caracteriza as sequências discursivas com que as iniciativas de checagem de conglomerados de mídia reivindicam credibilidade.",
   "abstract_quote": "We characterize the primary discursive sequences"
  },
  {
   "doi": "10.1080/21670811.2021.2021377",
   "title": "The Watchdog Role of Fact-Checkers in Different Media Systems",
   "authors": [
    "Paulo Ferracioli",
    "Andressa Butture Kniess",
    "Francisco Paulo Jamil Marques"
   ],
   "year": 2022,
   "venue": "Digital Journalism",
   "study_type": "Estudo empírico comparativo quantitativo (inclui a Lupa)",
   "method": "Análise de conteúdo de checagens, combinada com dados do Worlds of Journalism Survey",
   "sample_size": "a content analysis of 2,792 fact-checks published by FactCheck.org (United States), Pagella Politica (Italy), Correctiv (Germany), and Lupa (Brazil)",
   "main_finding": "Na maioria dos casos, a concepção de papel dos profissionais corresponde à postura de watchdog das agências.",
   "abstract_quote": "There is correspondence between professionals’ conceptions about their role and the watchdog stance agencies perform in most cases."
  },
  {
   "doi": "10.51206/elegis.v15i38.758",
   "title": "JORNALISMO DE CHECAGEM DE FATOS COMO INTERMEDIÁRIO DA TRANSPARÊNCIA PÚBLICA: UMA ANÁLISE COMPARADA ENTRE PAÍSES",
   "authors": [
    "Paulo Ferracioli"
   ],
   "year": 2022,
   "venue": "E-Legis - Revista Eletrônica do Programa de Pós-Graduação da Câmara dos Deputados",
   "study_type": "Estudo empírico comparativo (inclui a Agência Lupa)",
   "method": "Investigação comparada com análise de conteúdo de textos de checagem de quatro agências",
   "sample_size": "quatro agentes de países distintos (Agência Lupa, Factcheck.org, Pagella Politica e Correctiv); número de textos não informado no resumo",
   "main_finding": "Em todas as agências a principal fonte das conclusões foram informações fornecidas pelo Estado em seus sites (transparência ativa), com 63,5% dos textos da Lupa no Brasil.",
   "abstract_quote": "informações fornecidas pelo Estado em suas páginas de Internet (ou seja, transparência ativa)"
  },
  {
   "doi": "10.11606/issn.2236-4242.v38i2p221-239",
   "title": "Quem decide o que é \"Verdadeiro\"? Aos Fatos e os paradoxos do combate à desinformação",
   "authors": [
    "Thaís Cavalcanti dos Santos"
   ],
   "year": 2025,
   "venue": "Linha D'Água",
   "study_type": "Estudo qualitativo de análise documental e textual",
   "method": "Análise textual com base no interacionismo sociodiscursivo de Bronckart de documentos institucionais do site do Aos Fatos",
   "sample_size": "This article examines two institutional documents (do site do Aos Fatos)",
   "main_finding": "A política editorial do Aos Fatos apresenta vulnerabilidades nos critérios de verificação e na autoridade que a instituição constrói discursivamente.",
   "abstract_quote": "their editorial policy reveals some vulnerabilities regarding verification criteria"
  },
  {
   "doi": "10.55028/rpe.v10in.1.18117",
   "title": "Mídia alternativa digital e a checagem de fatos: um funcionamento em análise",
   "authors": [
    "Lucas Andrey Rodrigues",
    "Márcia Vorpagel Serschön",
    "Pamera Francieli Corrêa Pereira"
   ],
   "year": 2023,
   "venue": "Revista Primeira Escrita",
   "study_type": "Estudo qualitativo de análise documental e de discurso",
   "method": "Análise de discurso de linha francesa (Pêcheux, Orlandi) de recortes da seção editorial \"Nosso Método\" do Aos Fatos",
   "sample_size": "recortes da seção editorial Nosso Método do Aos Fatos; número de recortes não informado no resumo",
   "main_finding": "O estudo analisa o funcionamento discursivo do Aos Fatos, confrontando as sequências com os mitos de verdade, neutralidade, imparcialidade e objetividade. O resumo não traz resultado conclusivo.",
   "abstract_quote": "I analyze the discursive operation of Aos Fatos"
  },
  {
   "doi": "10.1515/omgc-2022-0028",
   "title": "Fact-checking initiatives in Portuguese language countries: checking methods and financing strategies",
   "authors": [
    "Lucas Durr Missau",
    "Laura Strelow Storch"
   ],
   "year": 2022,
   "venue": "Online Media and Global Communication",
   "study_type": "Estudo empírico (análise de conteúdo)",
   "method": "Análise de conteúdo de postagens coletadas manualmente nos sites das organizações de checagem do Brasil e de Portugal",
   "sample_size": "we collected manually 318 posts during June 2019 from each fact-checking outlets website; There were 15 active fact-checking outlets in Brazil (13) and Portugal (2).",
   "main_finding": "A inventividade das práticas de checagem fica restrita aos modelos de classificação adotados e à representação gráfica que eles exigem.",
   "abstract_quote": "Although there is room for inventiveness in fact-checking practices, it is restricted to the classification models adopted and the graphic representation demanded by them."
  },
  {
   "doi": "10.21878/compolitica.2019.9.2.143",
   "title": "Fact-checking como possibilidade de media accountability sobre o discurso político?",
   "authors": [
    "Tatiana Maria Dourado"
   ],
   "year": 2019,
   "venue": "Compolítica",
   "study_type": "Estudo empírico (análise de conteúdo)",
   "method": "Análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco; a técnica consta do subtítulo, e o resumo não a nomeia",
   "sample_size": "não informado no resumo",
   "main_finding": "A ação de etiquetar as checagens não foi seguida à risca e predominaram temas nacionais.",
   "abstract_quote": "A análise mostrou que a ação de etiquetar não foi seguida à risca e a predominância de temas nacionais."
  },
  {
   "doi": "10.1080/1461670x.2025.2470177",
   "title": "Decoding Correction Strategies: How Fact-Checkers Uncover Falsehoods Across Countries",
   "authors": [
    "Regina Cazzamatta"
   ],
   "year": 2025,
   "venue": "Journalism Studies",
   "study_type": "Estudo empírico comparativo quantitativo",
   "method": "Análise de conteúdo de artigos de verificação de organizações de checagem",
   "sample_size": "Utilizing a dataset of 3,154 verification articles from 23 organizations in eight countries across Europe and Latin America",
   "main_finding": "As técnicas de desmentido variam conforme o alvo da checagem, o país e a organização.",
   "abstract_quote": "significant variation exists depending on the target"
  },
  {
   "doi": "10.31921/doxacom.n41a2906",
   "title": "Estrategias locales de verificación y fact-checking en Brasil: la Red Nacional de Combate a la Desinformación, COAR Noticias, Colectivo Bereia, Verifica RS y Agência Tatu",
   "authors": [
    "Antonia Isabel Nogales-Bocio",
    "Julieti Sussi De Oliveira",
    "Carmen Marta-Lazo"
   ],
   "year": 2025,
   "venue": "Doxa Comunicación. Revista Interdisciplinar de Estudios de Comunicación y Ciencias Sociales",
   "study_type": "Estudo de caso qualitativo",
   "method": "Estudo de caso complementado por entrevistas semiestruturadas",
   "sample_size": "a Red Nacional de Combate a la Desinformación (RNCD) e cuatro de sus iniciativas más destacadas y proactivas; número de entrevistas não informado no resumo",
   "main_finding": "O resumo não relata resultados. Declara só o objetivo de analisar o papel da RNCD e as estratégias de implementação e verificação de quatro iniciativas locais, com os desafios do contexto local.",
   "abstract_quote": "A través de un enfoque cualitativo, se adopta el diseño de estudio de caso"
  }
 ],
 "search_notes": "Os 20 candidatos aprovados foram todos extraídos. Eram exatamente 20, então não houve corte. Não fiz buscas novas. Abri a página do periódico ou o registro Crossref/Semantic Scholar de cada um, quando o site do periódico estava bloqueado. A ferramenta de leitura limita citações a cerca de 125 caracteres. Por isso conferi letra por letra apenas trechos curtos e, em alguns casos, só o início de frases longas. Ajustes: (1) Canavilhas, Santos (Aos Fatos) e Watchdog (amostra): usei os trechos que consegui conferir. A citação de Santos ficou mais curta que a do candidato. A amostra do Watchdog (2.792 checagens de FactCheck.org, Pagella Politica, Correctiv e Lupa) veio do candidato e foi conferida só no início. (2) Missau: a frase completa da citação veio do candidato, e só seu início foi reconfirmado. O mesmo vale para a lista completa de veículos na amostra do Watchdog. (3) Retirei do achado de Missau a afirmação, não verificada, sobre fontes de assessorias de imprensa. (4) Retirei o ponto final da citação de Damasceno e Patrício, que no resumo é trecho de frase. Pontos fracos que o pesquisador deve revisar: (a) Dourado e Alencar 2020 (Lupa como negócio): o resumo não traz método nem resultado, só o objetivo. Não há evidência no resumo de dados próprios, e esse artigo pode não atender ao critério de estudo empírico. (b) Nogales-Bocio 2025 e Rodrigues 2023: o resumo não traz resultado conclusivo, e o campo de achado descreve o objetivo. (c) Cazzamatta, Decoding (2025): o resumo não nomeia o Brasil, e a inclusão se apoia na página do projeto da autora, citada pelo verificador e não reaberta por mim. (d) Nascimento et al. 2024: as checagens são de 2022. O resumo não menciona eleições, mas o recorte pode se sobrepor ao período eleitoral. (e) Dourado 2019: a técnica (análise de conteúdo) aparece no subtítulo, não no resumo, e o foco em discurso político pode se aproximar do critério de exclusão (eleições/governos). Não verifiquei isso. (f) Damasceno e Patrício 2020 não descrevem o método no resumo. (g) Lelo 2024: o ano de publicação online é 2023 e o da edição impressa é 2024. Mantive 2024, como na lista aprovada. Não cheguei aos 25 pedidos originalmente, porque a lista aprovada tinha 20 itens."
}