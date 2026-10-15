# Verificador da busca e da triagem
Você é um verificador independente, com busca na web. Para CADA candidato da lista: abra o DOI (https://doi.org/...)
ou o registro do Crossref ou do OpenAlex e confira se o DOI existe e corresponde ao título, aos autores, ao ano e ao
periódico informados; confira no resumo se o artigo atende a cada critério do pedido (tema, período, artigo de
periódico revisado por pares, estudo empírico, recorte). Reprove a lista se houver qualquer DOI inexistente ou
trocado, artigo fora do período, que não é de periódico, que não é empírico ou que não é do tema. Diga qual
candidato falhou e por quê. Esta etapa é só busca e triagem: trecho literal, amostra, método e achado são cobrados
na etapa seguinte, de extração; não reprove por falta deles aqui.

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

CANDIDATOS A VERIFICAR:
{
 "candidates": [
  {
   "doi": "10.25200/bjr.v16n2.2020.1212",
   "title": "JOURNALISM AND FACT-CHECKING: typification of sources used for checking and criteria for selecting fact-checked material – an analysis by Agência Lupa and Aos Fatos",
   "authors": [
    "Daniel de Rezende Damasceno",
    "Edgard Patrício"
   ],
   "year": 2020,
   "venue": "Brazilian Journalism Research",
   "checked_url": "https://bjr.sbpjor.org.br/bjr/article/view/1212",
   "criteria_met": [
    "Tema: Agência Lupa e Aos Fatos",
    "Foco: fontes e critérios de seleção",
    "Período 2020; journal-article (Crossref)",
    "Tipo de estudo e método: estudo empírico de análise das checagens das duas agências; o resumo não detalha o método",
    "Amostra: não informado no resumo (o resumo cita apenas 'two Brazilian checking agencies, Aos Fatos and Agência Lupa')",
    "Achado principal: as agências não explicitam os critérios de seleção do que checam e dependem sobretudo de fontes oficiais",
    "Trecho literal do resumo: \"the agencies themselves do not lay out the criteria for selecting what is to be checked.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.25200/BJR.v18n2.2022.1510",
   "criteria_met": [
    "Tema: fact-checkers brasileiros (jornalistas de organizações brasileiras)",
    "Foco: propósitos, princípios, rotinas, transparência de fontes",
    "Período 2022; journal-article (Crossref); doi.org/10.25200/BJR.v18n2.2022.1510 redireciona para bjr.sbpjor.org.br/bjr/article/view/1510. A página SciELO exibia o sufixo 1497, mas o Crossref e o doi.org confirmam 1510",
    "Tipo de estudo e método: levantamento por questionário autoaplicado",
    "Amostra: \"The sample (n=29) expressed their level of agreement with a group of statements.\"",
    "Achado principal: o propósito central é detectar e combater conteúdo falso e enganoso nos canais digitais, com forte valorização da transparência sobre fontes e dados",
    "Trecho literal do resumo: \"The results show the central purpose is to detect and combat false and misleading content on digital channels.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.13037/ci.vol21n46.6388",
   "criteria_met": [
    "Tema: Agência Lupa",
    "Foco: modelo de negócio e comercialização das checagens (financiamento)",
    "Período 2020; journal-article (Crossref)",
    "Tipo de estudo e método: análise da comercialização das checagens da Lupa com base na Economia Política do Jornalismo. O resumo não explicita a técnica de coleta; confirmar no texto completo que há dados próprios",
    "Amostra: não informado no resumo",
    "Achado principal: o resumo declara só o objetivo, que é analisar a mercantilização das checagens da Lupa para veículos de comunicação. Não traz resultado",
    "Trecho literal do resumo: \"Partindo disso, o presente artigo tem como objetivo analisar a mercantilização das checagens da Agência Lupa\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.22478/ufpb.2763-9398.2022v17n.63545",
   "criteria_met": [
    "Tema: Agência Lupa",
    "Foco: estratégias de financiamento por projetos especiais",
    "Período 2022; journal-article (Crossref)",
    "Tipo de estudo e método: estudo de caso com identificação e análise das iniciativas de 2020 (análise documental)",
    "Amostra: não informado no resumo (iniciativas desenvolvidas ao longo de 2020)",
    "Achado principal: o estudo identifica as estratégias da Lupa para garantir financiamento por meio de projetos especiais, com as potencialidades e os limites da prática",
    "Trecho literal do resumo: \"as estratégias da Agência Lupa para garantir o financiamento do combate à desinformação por meio de projetos especiais.\""
   ]
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
   "checked_url": "https://bjr.sbpjor.org.br/bjr/article/view/1687",
   "criteria_met": [
    "Tema: Lupa e Aos Fatos",
    "Foco: fontes e transparência pública na verificação",
    "Período 2024; journal-article (Crossref). O recorte são checagens de 2022, mas o foco é o uso de ferramentas de transparência, não as eleições",
    "Tipo de estudo e método: análise de conteúdo",
    "Amostra: \"which represented less than 7% of the total checks conducted (950).\" Foram 63 checagens com ferramentas de transparência",
    "Achado principal: as ferramentas de transparência pública aparecem em menos de 7% das checagens, mas são decisivas nas que envolvem agentes e autoridades públicas",
    "Trecho literal do resumo: \"However, such tools proved decisive for verifications involving subjects, agents, and public authorities.\""
   ]
  },
  {
   "doi": "10.1177/10776990231207963",
   "title": "Fostering Artificial Intelligence to Face Misinformation: Discourses and Practices of Automated Fact-Checking in Brazil",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2024,
   "venue": "Journalism & Mass Communication Quarterly",
   "checked_url": "https://api.crossref.org/works/10.1177/10776990231207963",
   "criteria_met": [
    "Tema: fact-checking brasileiro (cinco sites)",
    "Foco: uso de IA e automação",
    "Período: publicado online em nov/2023 e na edição vol. 101(2) de jun/2024. Dentro de 2018–2025; divergência de ano anotada",
    "Tipo de estudo e método: análise documental de declarações oficiais e entrevistas semiestruturadas",
    "Amostra: \"30 official statements published by journalists and their tech partners,\" e \"seven semi-structured interviews with representatives from five websites.\"",
    "Achado principal: há um cenário emergente de automação no fact-checking brasileiro apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores",
    "Trecho literal do resumo: \"This article shows an emerging automation landscape in the Brazilian fact-checking venture supported by the tech industry.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.1177/27523543251344971",
   "criteria_met": [
    "Tema: comparativo que inclui o Brasil",
    "Foco: métodos de detecção e estratégias de checagem ligados a IA",
    "Período 2025; journal-article",
    "Tipo de estudo e método: estudo de caso de métodos mistos (análise de conteúdo quantitativa e entrevistas com especialistas)",
    "Amostra: \"a quantitative content analysis of 136 verification articles (2023–2024)\" e \"13 expert interviews\"",
    "Achado principal: o alcance da desinformação gerada por IA ainda é limitado, mas há variações por país em temas, métodos de detecção e estratégias de desmentido",
    "Trecho literal do resumo: \"The results revealed notable country-specific variations in topics, targets, intentions, AI elements, generative models,\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.3390/socsci14090514",
   "criteria_met": [
    "Tema: comparativo que inclui a organização brasileira Aletheia",
    "Foco: uso de IA no processo de checagem",
    "Período 2025; journal-article",
    "Tipo de estudo e método: estudo teórico-empírico com entrevistas em profundidade. O resumo traz dados próprios",
    "Amostra: \"in-depth interviews were conducted with representatives of four fact-checking organizations: Polígrafo (Portugal), Chequeado (Argentina), Maldita (Spain), and Aletheia (Brazil).\"",
    "Achado principal: cada organização usa a IA para necessidades específicas, em níveis que vão do uso simples ao disruptivo e ligados à estrutura humana e à situação econômica",
    "Trecho literal do resumo: \"it was concluded that each organization uses these technologies to respond to specific needs.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.13037/ci.vol25n53.8624",
   "criteria_met": [
    "Tema: Lupa (Brasil) comparada com Chequeado (Argentina)",
    "Foco: estratégias, negócios e mercantilização da checagem (modelo de negócio)",
    "Período 2022; journal-article (Crossref)",
    "Tipo de estudo e método: estudo comparativo das duas agências. O resumo não detalha a técnica de coleta",
    "Amostra: duas agências (Lupa e Chequeado); número de itens não informado no resumo",
    "Achado principal: o fact-checking na América Latina é um modelo de negócio que promove o empreendedorismo jornalístico",
    "Trecho literal do resumo: \"o artigo revela que o fact-checking na América Latina é um modelo de negócio\""
   ]
  },
  {
   "doi": "10.1080/1461670X.2022.2069588",
   "title": "The Rise of the Brazilian Fact-checking Movement: Between Economic Sustainability and Editorial Independence",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2022,
   "venue": "Journalism Studies",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/1461670X.2022.2069588?fields=title,abstract,year,venue,authors",
   "criteria_met": [
    "Tema: organizações brasileiras de checagem",
    "Foco: fontes de financiamento e autonomia editorial",
    "Período 2022 (vol. 23(9), Crossref); journal-article. Resumo lido no Semantic Scholar porque o site do periódico bloqueou o acesso",
    "Tipo de estudo e método: entrevistas semiestruturadas com dados complementares dos sites",
    "Amostra: \"semi-structured interviews with 16 fact-checkers from 13 active organizations,\"",
    "Achado principal: a principal estratégia de viabilidade econômica é a presença nas plataformas digitais, e a dependência do dinheiro das big techs leva a priorizar o debunking em vez da checagem política",
    "Trecho literal do resumo: \"Nevertheless, their chief business strategy to gain economic viability mainly translates into a solid presence on digital platforms.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.17645/mac.v9i1.3443",
   "criteria_met": [
    "Tema: comparativo que inclui a Agência Lupa (Brasil)",
    "Foco: padrões, metodologias, procedimentos e desafios (acesso a dados, recursos)",
    "Período 2021; journal-article",
    "Tipo de estudo e método: entrevistas em profundidade com gestores de plataformas independentes",
    "Amostra: o resumo lista 8 plataformas (Chequeado, UYCheck, Maldita.es, Newtral, Fact Checking Chile, Agência Lupa, Ecuador Chequea, ColombiaCheck); o número de entrevistados não é informado no resumo",
    "Achado principal: apesar das equipes pequenas, todas usam metodologias robustas e enfrentam três desafios: acesso a dados públicos, poucos recursos e alcance de públicos mais amplos",
    "Trecho literal do resumo: \"Interviewees identified three core challenges in fact-checking practice: difficulties in accessing public data,\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.5209/esmp.71235",
   "criteria_met": [
    "Tema: cinco organizações brasileiras de checagem ligadas a conglomerados de mídia",
    "Foco: apresentação dos métodos de trabalho e transparência para reivindicar credibilidade",
    "Período 2021; journal-article",
    "Tipo de estudo e método: análise documental e análise de discurso de linha francesa",
    "Amostra: \"of five Brazilian fact-checking organizations from media conglomerates.\" O corpus são os textos de apresentação e as descrições de métodos",
    "Achado principal: o estudo caracteriza as sequências discursivas com que essas iniciativas reivindicam credibilidade",
    "Trecho literal do resumo: \"We characterize the primary discursive sequences used by these initiatives and the subjects implicated\""
   ]
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
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/21670811.2021.2021377?fields=title,abstract,year,venue",
   "criteria_met": [
    "Tema: comparativo que inclui a Lupa (Brasil)",
    "Foco: papel de watchdog e práticas de classificação (rótulos)",
    "Período 2022 (vol. 10(5), Crossref); journal-article. Resumo lido no Semantic Scholar e conferido com o repositório da Universidade de Iowa (a Taylor & Francis bloqueou o acesso)",
    "Tipo de estudo e método: análise de conteúdo mais dados do Worlds of Journalism Survey",
    "Amostra: \"a content analysis of 2,792 fact-checks published by FactCheck.org (United States), Pagella Politica (Italy), Correctiv (Germany), and Lupa (Brazil).\"",
    "Achado principal: na maioria dos casos há correspondência entre a concepção do papel dos profissionais e a postura de watchdog das agências",
    "Trecho literal do resumo: \"There is correspondence between professionals’ conceptions about their role and the watchdog stance agencies perform in most cases.\""
   ]
  },
  {
   "doi": "10.51206/elegis.v15i38.758",
   "title": "JORNALISMO DE CHECAGEM DE FATOS COMO INTERMEDIÁRIO DA TRANSPARÊNCIA PÚBLICA: UMA ANÁLISE COMPARADA ENTRE PAÍSES",
   "authors": [
    "Paulo Ferracioli"
   ],
   "year": 2022,
   "venue": "E-Legis - Revista Eletrônica do Programa de Pós-Graduação da Câmara dos Deputados",
   "checked_url": "https://e-legis.camara.leg.br/cefor/index.php/e-legis/article/view/758",
   "criteria_met": [
    "Tema: comparativo que inclui a Agência Lupa (Brasil)",
    "Foco: fontes e transparência pública",
    "Período 2022 (v. 15, n. 38, mai/ago, Crossref e página do periódico); journal-article na seção Dossiê",
    "Tipo de estudo e método: investigação comparada com análise de conteúdo de textos de checagem",
    "Amostra: quatro agências (Lupa, Factcheck.org, Pagella Politica, Correctiv); o número de textos não é informado no resumo",
    "Achado principal: em todas as agências a principal fonte foram informações estatais publicadas em sites (transparência ativa), com 63,5% dos textos no Brasil",
    "Trecho literal do resumo: \"Em todas, informações fornecidas pelo Estado em suas páginas de Internet (ou seja, transparência ativa)\""
   ]
  },
  {
   "doi": "10.11606/issn.2236-4242.v38i2p221-239",
   "title": "Quem decide o que é \"Verdadeiro\"? Aos Fatos e os paradoxos do combate à desinformação",
   "authors": [
    "Thaís Cavalcanti dos Santos"
   ],
   "year": 2025,
   "venue": "Linha D'Água",
   "checked_url": "https://api.crossref.org/works/10.11606/issn.2236-4242.v38i2p221-239",
   "criteria_met": [
    "Tema: Aos Fatos",
    "Foco: critérios de verificação (métricas, selos, fontes 'confiáveis') e política editorial",
    "Período 2025; journal-article",
    "Tipo de estudo e método: análise documental e textual (interacionismo sociodiscursivo)",
    "Amostra: \"This article examines two institutional documents from the fact-checking organization “Aos Fatos” website,\"",
    "Achado principal: a política editorial da Aos Fatos apresenta vulnerabilidades nos critérios de verificação e na autoridade construída discursivamente",
    "Trecho literal do resumo: \"their editorial policy reveals some vulnerabilities regarding verification criteria and the authority discursively constructed by the institution\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.55028/rpe.v10in.1.18117",
   "criteria_met": [
    "Tema: Aos Fatos",
    "Foco: descrição de métodos e transparência ('Nosso Método')",
    "Período 2023; journal-article",
    "Tipo de estudo e método: análise de discurso (linha francesa) de recortes documentais",
    "Amostra: \"The research has as its corpus clippings from the editorial section Nosso Método from Aos Fatos,\" Número de recortes não informado no resumo",
    "Achado principal: o estudo analisa o funcionamento discursivo da Aos Fatos, contrapondo as sequências aos mitos de verdade, neutralidade, imparcialidade e objetividade. O resumo não traz resultado conclusivo",
    "Trecho literal do resumo: \"I analyze the discursive operation of Aos Fatos, counterposing the sequences to the deconstruction of the myths\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.1515/omgc-2022-0028",
   "criteria_met": [
    "Tema: 15 veículos ativos, 13 deles no Brasil",
    "Foco: métodos de verificação, fontes, classificação e financiamento",
    "Período 2022 (vol. 1(3)); journal-article",
    "Tipo de estudo e método: análise de conteúdo",
    "Amostra: \"Based on Content Analysis, we collected manually 318 posts during June 2019 from each fact-checking outlets website\"; \"There were 15 active fact-checking outlets in Brazil (13) and Portugal (2).\"",
    "Achado principal: a inventividade das práticas fica restrita aos modelos de classificação e à representação gráfica, e muitas checagens se apoiam só em fontes de assessorias de imprensa",
    "Trecho literal do resumo: \"Although there is room for inventiveness in fact-checking practices, it is restricted to the classification models adopted and the graphic representation demanded by them.\""
   ]
  },
  {
   "doi": "10.21878/compolitica.2019.9.2.143",
   "title": "Fact-checking como possibilidade de media accountability sobre o discurso político?",
   "authors": [
    "Tatiana Maria Dourado"
   ],
   "year": 2019,
   "venue": "Compolítica",
   "checked_url": "https://api.crossref.org/works/10.21878/compolitica.2019.9.2.143",
   "criteria_met": [
    "Tema: Aos Fatos, Lupa e Truco",
    "Foco: práticas de classificação (etiquetas), temas e limites da prática. É o mais fraco quanto ao foco, ver notas",
    "Período 2019; journal-article (Crossref)",
    "Tipo de estudo e método: análise da produção de checagens. O resumo não nomeia o método; confirmar no texto completo",
    "Amostra: não informado no resumo",
    "Achado principal: a ação de etiquetar não foi seguida à risca e predominaram temas nacionais",
    "Trecho literal do resumo: \"A análise mostrou que a ação de etiquetar não foi seguida à risca e a predominância de temas nacionais.\""
   ]
  },
  {
   "doi": "10.1080/1461670x.2025.2470177",
   "title": "Decoding Correction Strategies: How Fact-Checkers Uncover Falsehoods Across Countries",
   "authors": [
    "Regina Cazzamatta"
   ],
   "year": 2025,
   "venue": "Journalism Studies",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/1461670x.2025.2470177?fields=title,abstract,year,venue,authors",
   "criteria_met": [
    "Tema: comparativo de 8 países da Europa e da América Latina. O resumo não cita o Brasil; a inclusão foi confirmada na página do projeto DFG da autora (Uruguai, Argentina, Brasil e Venezuela na América Latina), ver notas",
    "Foco: técnicas de verificação e métodos de correção",
    "Período 2025 (vol. 26(7), Crossref); journal-article",
    "Tipo de estudo e método: análise de conteúdo de artigos de verificação",
    "Amostra: \"Utilizing a dataset of 3,154 verification articles from 23 organizations in eight countries\"",
    "Achado principal: as técnicas de desmentido variam conforme o alvo (boatos online ou declarações de figuras públicas), o país e a organização",
    "Trecho literal do resumo: \"significant variation exists depending on the target.\""
   ]
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
   "checked_url": "https://api.crossref.org/works/10.31921/doxacom.n41a2906",
   "criteria_met": [
    "Tema: iniciativas brasileiras de verificação (RNCD, COAR Noticias, Colectivo Bereia, Verifica RS, Agência Tatu)",
    "Foco: estratégias de implementação e verificação",
    "Período 2025; journal-article",
    "Tipo de estudo e método: estudo de caso qualitativo com entrevistas semiestruturadas",
    "Amostra: a Rede Nacional de Combate à Desinformação e 4 de suas iniciativas; o número de entrevistas não é informado no resumo",
    "Achado principal: o resumo declara só o objetivo, que é analisar as estratégias de implementação e verificação e as especificidades do contexto local",
    "Trecho literal do resumo: \"A través de un enfoque cualitativo, se adopta el diseño de estudio de caso, complementado con entrevistas semiestructuradas,\""
   ]
  }
 ],
 "notes": "Entreguei 20 artigos, não os 25 pedidos. Preferi entregar menos a completar com artigo que não atende aos critérios.\n\nCORREÇÃO DA TENTATIVA 1: o item reprovado por 'sem DOI' era Fossá & Müller, 'Estratégias das organizações de fact-checking brasileiras no contexto de desautorização da mediação jornalística' (Revista Líbero, n. 49, 2021). Procurei o DOI no Crossref, na página do periódico e no PDF, e não achei. Retirei o artigo. Nenhum DOI desta lista foi escrito sem abertura nesta tentativa: todos foram conferidos no Crossref ou na página do periódico.\n\nCONFERÊNCIA DE FONTES:\n- Os sites da Taylor & Francis e da SAGE bloqueiam o acesso automático (403). Nesses casos o resumo veio do Crossref ou do Semantic Scholar. O endereço usado está em checked_url.\n- Rodríguez-Pérez & Seibt (BJR 2022): a página SciELO mostrava o sufixo 1497, mas o Crossref e o doi.org confirmam 10.25200/bjr.v18n2.2022.1510.\n- Lelo 2023 (JMCQ): online em nov/2023 e edição de jun/2024. Registrei 2024.\n- Os trechos literais foram copiados dos resumos retornados pelas ferramentas, em segmentos curtos. Vale uma conferência rápida contra o resumo oficial antes de citar.\n\nRESSALVAS (itens fracos que mantive):\n- Dourado & Alencar 2020, Dourado 2019, Nogales-Bocio 2025 e Rodrigues 2023: o resumo não traz resultado claro, o método ou os dois. Dourado & Alencar e Dourado 2019 não nomeiam a técnica de coleta; Nogales-Bocio traz só o objetivo. Em Rodrigues, o corpus é claro, mas o resultado é vago. O achado informado é o que o resumo permite. Dourado 2019 também é o mais fraco quanto ao foco temático, porque trata de fiscalização do discurso político. Confirmar no texto completo antes de usar; se o rigor for prioridade, esses quatro são os primeiros a sair.\n- Cazzamatta, 'Decoding Correction Strategies' (Journalism Studies 2025): o resumo diz 'oito países da Europa e da América Latina' sem citar o Brasil. A página do projeto DFG da autora (Uni Erfurt) lista Brasil entre os 4 países latino-americanos. Esse é um cruzamento indireto.\n- Nascimento 2024: o corpus são checagens de 2022, mas o foco é o uso de ferramentas de transparência, não as eleições.\n- Ferracioli et al. 2022 menciona o presidente Trump, mas só como achado sobre um dos quatro veículos.\n\nEXCLUÍDOS (motivo):\n- Eleições, governos ou COVID-19 como foco: Kniess et al. 2024 (governos Bolsonaro e Lula), Cazzamatta & Santos 2023 (segundo turno de 2022), Conceição & Segurado 2020 (Truco, eleição de 2014), Joux & Teixeira 2024 (debates eleitorais), Bertoldo & Riffel 2021, Mediapolis/Comprova 2018 e Rocha Jr. 2019 (eleições); Martins & Teixeira, Pessôa & Carvalho, Carvalho 2024, Paganotti 2021 (robô Fátima), Lemos & Reis, Costa & Rêgo (COVID-19).\n- Efeito ou recepção: Oliveira & Assis 2020 (reação do público no Facebook).\n- Revisão ou ensaio: Vinhas & Bastos 2022 (revisão de literatura), Cazzamatta & Sarısakaloğlu 2025 (Journalism Practice, mapeamento de literatura), Spinelli & Santos 2018 (revisão de literatura), Santos & Maurer 2020 (base bibliográfica, tende a ensaio). Vinhas & Bastos 2023, Montaña-Niño et al. 2023 (AoIR) e Vinhas & Bastos 2023 (AoIR) são anais de congresso.\n- Brasil não confirmado no resumo, ou foco fora dos temas do plano: Koliska & Roberts 2024 e Roberts & Koliska 2025 (global), Rodríguez-Pérez et al. 2022 (Ibero-América; resumo sem Brasil), Vinhas & Bastos 2025 IJPP (Brasil não aparece no resumo), Palau-Sampio 2018 (nove iniciativas na América Latina, sem lista no resumo), Gutiérrez-Caneda 2024, Vu et al. 2022, Dafonte-Gómez 2022, Míguez-González 2023 (Twitter, vinculado à COVID-19). Montaña-Niño 2024 (fringe) tem um caso brasileiro, mas o objeto é checador marginal. Abuín-Penas 2024 e Trindade 2023 tratam de letramento midiático, fora da lista de focos do plano.\n- Datas ou DOI: Cazzamatta 2025 ('The truth game', Journalism): a edição final é vol. 27(8), 2026, fora do período. Cazzamatta, 'Objectively Engaged' (Journalism Practice 2025): não consegui ler o resumo. Fossá & Müller 2021: sem DOI.\n\nPara chegar a 25, as próximas buscas seriam: o resumo de Cazzamatta 2025 'Objectively Engaged' e o de Lelo 2022 em Journalism Practice (ambos sem resumo acessível nesta tentativa); conferir no texto completo se o Brasil está em Rodríguez-Pérez et al. 2022 e Vinhas & Bastos 2025; e consultas em SciELO e Redalyc, que não consegui consultar diretamente."
}