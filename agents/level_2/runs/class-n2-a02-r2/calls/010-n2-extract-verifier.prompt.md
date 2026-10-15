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
   "study_type": "Estudo empírico (análise das checagens publicadas pelas duas agências)",
   "method": "O resumo não detalha o método; analisa as fontes e os critérios de seleção de Agência Lupa e Aos Fatos.",
   "sample_size": "não informado no resumo",
   "main_finding": "As agências não explicitam os critérios de seleção do que checam e se apoiam principalmente em dados e estudos de fontes oficiais e instituições públicas.",
   "abstract_quote": "the agencies themselves do not lay out the criteria for selecting what is to be checked."
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
   "study_type": "Estudo empírico quantitativo (survey)",
   "method": "Questionário autoaplicado em que os checadores brasileiros indicaram seu nível de concordância com um conjunto de afirmações.",
   "sample_size": "n=29",
   "main_finding": "O propósito central da checagem é detectar e combater conteúdo falso e enganoso nos canais digitais, e a transparência sobre fontes e dados que sustentam a avaliação é fortemente valorizada.",
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
   "study_type": "Estudo sobre modelo de negócio (referencial da Economia Política do Jornalismo); o resumo não indica se há dados próprios",
   "method": "O resumo não informa técnica de coleta; declara apenas o objetivo de analisar a mercantilização das checagens da Agência Lupa para veículos de comunicação.",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo não relata resultado; declara apenas o objetivo de analisar a comercialização das checagens da Lupa para veículos de comunicação (item com ressalva, ver search_notes).",
   "abstract_quote": "analisar a mercantilização das checagens da Agência Lupa para veículos de comunicação"
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
   "study_type": "Estudo de caso",
   "method": "Identificação e análise das iniciativas da Agência Lupa desenvolvidas ao longo de 2020, para apontar potencialidades e limites da prática.",
   "sample_size": "não informado no resumo",
   "main_finding": "O estudo identifica as estratégias da Lupa para garantir o financiamento do combate à desinformação por meio de projetos especiais, com suas potencialidades e limites.",
   "abstract_quote": "as estratégias da Agência Lupa para garantir o financiamento do combate à desinformação por meio de projetos especiais."
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
   "method": "Análise de conteúdo das checagens de Lupa e Aos Fatos de 2022 quanto ao uso de ferramentas de transparência pública.",
   "sample_size": "63 checagens com ferramentas de transparência, \"less than 7% of the total checks conducted (950)\"",
   "main_finding": "As ferramentas de transparência pública aparecem em menos de 7% das checagens, mas foram decisivas nas verificações que envolviam sujeitos, agentes e autoridades públicas.",
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
   "method": "Análise documental de declarações oficiais e entrevistas semiestruturadas com representantes de sites de checagem.",
   "sample_size": "30 official statements published by journalists and their tech partners; seven semi-structured interviews with representatives from five websites",
   "main_finding": "Há um cenário emergente de automação no fact-checking brasileiro apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores ao ampliar a influência dos tecnólogos sobre o jornalismo.",
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
   "study_type": "Estudo de caso de métodos mistos, comparativo (Brasil, Alemanha e Reino Unido)",
   "method": "Análise de conteúdo quantitativa de artigos de verificação e entrevistas com especialistas.",
   "sample_size": "a quantitative content analysis of 136 verification articles (2023–2024); 13 expert interviews",
   "main_finding": "Há variações marcantes entre os três países em temas, alvos, intenções, elementos de IA, modelos generativos, métodos de detecção e estratégias de desmentido.",
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
   "study_type": "Estudo empírico qualitativo, comparativo (inclui a organização brasileira Aletheia)",
   "method": "Entrevistas em profundidade com representantes de quatro organizações de checagem.",
   "sample_size": "in-depth interviews were conducted with representatives of four fact-checking organizations: Polígrafo (Portugal), Chequeado (Argentina), Maldita (Spain), and Aletheia (Brazil)",
   "main_finding": "Cada organização usa a IA para necessidades específicas, em níveis que vão de ferramentas simples a usos mais disruptivos, conforme sua estrutura de pessoal e situação financeira.",
   "abstract_quote": "it was concluded that each organization uses these technologies to respond to specific needs."
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
   "study_type": "Estudo comparativo das estratégias e negócios de duas agências (Lupa, Brasil; Chequeado, Argentina)",
   "method": "Comparação das duas agências; o resumo não detalha a técnica de coleta.",
   "sample_size": "não informado no resumo",
   "main_finding": "O fact-checking na América Latina funciona como um modelo de negócio que sustenta o empreendedorismo jornalístico e, ao mesmo tempo, combate a desinformação.",
   "abstract_quote": "o artigo revela que o fact-checking na América Latina é um modelo de negócio"
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
   "method": "Entrevistas semiestruturadas com checadores, complementadas por dados dos sites das organizações.",
   "sample_size": "semi-structured interviews with 16 fact-checkers from 13 active organizations",
   "main_finding": "A principal estratégia de viabilidade econômica das organizações brasileiras é a forte presença nas plataformas digitais, e a dependência do financiamento das big techs leva a priorizar o debunking em vez da checagem política.",
   "abstract_quote": "Nevertheless, their chief business strategy to gain economic viability mainly translates into a solid presence on digital platforms."
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
   "study_type": "Estudo empírico qualitativo, comparativo (inclui a Agência Lupa)",
   "method": "Entrevistas em profundidade com gestores de plataformas independentes de checagem da América Latina e da Espanha.",
   "sample_size": "não informado no resumo",
   "main_finding": "Apesar das equipes pequenas, as plataformas usam metodologias rigorosas de verificação e enfrentam três desafios: acesso a dados públicos, poucos recursos e alcance de públicos mais amplos.",
   "abstract_quote": "Interviewees identified three core challenges in fact-checking practice: difficulties in accessing public data,"
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
   "method": "Análise de discurso de linha francesa dos textos de apresentação e das descrições de métodos de trabalho de organizações de checagem ligadas a conglomerados de mídia.",
   "sample_size": "five Brazilian fact-checking organizations from media conglomerates",
   "main_finding": "O estudo caracteriza as principais sequências discursivas com que essas iniciativas reivindicam credibilidade e os sujeitos nelas implicados.",
   "abstract_quote": "We characterize the primary discursive sequences used by these initiatives and the subjects implicated"
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
   "study_type": "Estudo empírico quantitativo, comparativo (inclui a Lupa)",
   "method": "Análise de conteúdo de checagens, combinada com dados do Worlds of Journalism Survey.",
   "sample_size": "a content analysis of 2,792 fact-checks published by FactCheck.org (United States), Pagella Politica (Italy), Correctiv (Germany), and Lupa (Brazil)",
   "main_finding": "Na maioria dos casos há correspondência entre a concepção que os profissionais têm do seu papel e a postura de watchdog que as agências exercem.",
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
   "method": "Análise comparada de textos de checagem de quatro agências (Lupa, Factcheck.org, Pagella Politica e Correctiv) quanto ao uso de dados públicos.",
   "sample_size": "não informado no resumo",
   "main_finding": "Em todas as agências a principal fonte foram informações estatais publicadas em sites (transparência ativa); os textos que usaram dados públicos foram 63,5% no Brasil, 53,4% na Itália, 52,7% nos EUA e 29,2% na Alemanha.",
   "abstract_quote": "Em todas, informações fornecidas pelo Estado em suas páginas de Internet (ou seja, transparência ativa)"
  },
  {
   "doi": "10.11606/issn.2236-4242.v38i2p221-239",
   "title": "Quem decide o que é \"Verdadeiro\"? Aos Fatos e os paradoxos do combate à desinformação",
   "authors": [
    "Thaís Cavalcanti dos Santos"
   ],
   "year": 2025,
   "venue": "Linha D'Água",
   "study_type": "Estudo empírico qualitativo (análise documental e textual)",
   "method": "Análise de documentos institucionais da Aos Fatos com base no interacionismo sociodiscursivo, examinando métricas, selos de classificação e fontes \"confiáveis\".",
   "sample_size": "two institutional documents from the fact-checking organization “Aos Fatos” website",
   "main_finding": "Embora represente um avanço contra a desinformação, a política editorial da Aos Fatos apresenta vulnerabilidades nos critérios de verificação e na autoridade construída discursivamente.",
   "abstract_quote": "their editorial policy reveals some vulnerabilities regarding verification criteria and the authority discursively constructed by the institution"
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
   "study_type": "Estudo empírico qualitativo (análise documental e de discurso)",
   "method": "Análise de discurso de linha francesa de recortes da seção editorial \"Nosso Método\" da Aos Fatos.",
   "sample_size": "não informado no resumo (o corpus são recortes da seção \"Nosso Método\", sem número)",
   "main_finding": "O resumo não traz resultado conclusivo: analisa o funcionamento discursivo da Aos Fatos na descrição do seu método, contrapondo as sequências aos mitos de verdade, neutralidade, imparcialidade e objetividade (item com ressalva, ver search_notes).",
   "abstract_quote": "the journalistic discourses are also crossed and have their meanings guided."
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
   "study_type": "Estudo empírico quantitativo/qualitativo (análise de conteúdo)",
   "method": "Análise de conteúdo de posts coletados manualmente nos sites das iniciativas, quanto a discurso, fontes, contexto, classificação, representação gráfica e financiamento.",
   "sample_size": "318 posts collected manually during June 2019; 15 active fact-checking outlets in Brazil (13) and Portugal (2)",
   "main_finding": "A inventividade das práticas fica restrita aos modelos de classificação e à representação gráfica, e muitas checagens se apoiam apenas em fontes de assessorias de imprensa.",
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
   "study_type": "Estudo empírico (análise de conteúdo, segundo o subtítulo \"Uma análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco\")",
   "method": "Análise de conteúdo das checagens de Aos Fatos, Lupa e Truco quanto a etiquetas de classificação e temas.",
   "sample_size": "não informado no resumo",
   "main_finding": "A ação de etiquetar não foi seguida à risca nas três iniciativas e predominaram temas nacionais.",
   "abstract_quote": "A análise mostrou que a ação de etiquetar não foi seguida à risca e a predominância de temas nacionais."
  },
  {
   "doi": "10.1080/1461670X.2025.2470177",
   "title": "Decoding Correction Strategies: How Fact-Checkers Uncover Falsehoods Across Countries",
   "authors": [
    "Regina Cazzamatta"
   ],
   "year": 2025,
   "venue": "Journalism Studies",
   "study_type": "Estudo empírico quantitativo, comparativo internacional",
   "method": "Análise de conteúdo de artigos de verificação, com identificação de 17 técnicas de desmentido.",
   "sample_size": "a dataset of 3,154 verification articles from 23 organizations in eight countries",
   "main_finding": "As técnicas de desmentido variam conforme o alvo (boatos online ou declarações de figuras públicas), o país e a organização.",
   "abstract_quote": "significant variation exists depending on the target."
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
   "method": "Estudo de caso complementado com entrevistas semiestruturadas, sobre a Rede Nacional de Combate à Desinformação e quatro de suas iniciativas.",
   "sample_size": "não informado no resumo (a Rede Nacional de Combate à Desinformação e 4 iniciativas; número de entrevistas não indicado)",
   "main_finding": "O resumo não relata resultado: declara apenas o objetivo de analisar como as iniciativas implementam a verificação e as especificidades do contexto local (item com ressalva, ver search_notes).",
   "abstract_quote": "A través de un enfoque cualitativo, se adopta el diseño de estudio de caso, complementado con entrevistas semiestructuradas"
  }
 ],
 "search_notes": "Entreguei 20 artigos, que são todos os da lista aprovada. Não fiz buscas novas, porque a regra do passo é usar só a lista aprovada. Por isso Estadão Verifica, Fato ou Fake e Comprova continuam sem artigo próprio, e o universo aprovado não chega a 25. Reabri os resumos pelo Crossref, pelas páginas das revistas e pelo Semantic Scholar. O acesso às páginas da Taylor & Francis e da SAGE foi bloqueado (403). Algumas ferramentas de leitura só devolveram paráfrases dos resumos, então as citações dos itens 1, 2, 3, 5, 9, 10, 11, 12, 13, 14, 15, 17, 18 e 19 foram conferidas só em parte contra o texto original. As dos itens 10 e 13 foram confirmadas pelo Semantic Scholar.\n\nRessalvas que o pesquisador deve avaliar. Se quiser aplicar rigorosamente os critérios, remova estes itens:\n- Item 3 (Dourado e Alencar 2020): o resumo traz só o objetivo e o referencial teórico. Não informa método, dados nem resultado, e não dá para confirmar que há estudo empírico com dados próprios.\n- Item 16 (Rodrigues et al. 2023): o resumo, lido no Crossref (inglês) e na página da revista (português), não traz resultado conclusivo. O \"achado\" descreve o objetivo analítico. A citação vem do resumo em inglês do Crossref.\n- Item 20 (Nogales-Bocio et al. 2025): o resumo informa objetivo e método (a citação foi confirmada na página da revista), mas nenhum resultado.\n- Item 19 (Cazzamatta 2025): o resumo não nomeia o Brasil. A página do projeto DFG da autora e o Semantic Scholar indicam que o corpus cobre oito países, e o projeto inclui o Brasil. Não consegui confirmar no texto do artigo a presença de organizações brasileiras, então o item pode não atender ao critério de comparativo com o Brasil.\n\nOutras observações:\n- Item 5 (Nascimento et al. 2024): as 950 checagens são de 2022, ano eleitoral. O resumo e o foco são o uso de ferramentas de transparência, e o estudo não é centrado em eleições.\n- Item 6 (Lelo 2024): publicado online em nov/2023 e na edição de jun/2024 (vol. 101, n. 2); usei 2024. A afirmação de que a IA desafiou a autoridade dos checadores veio do resumo no Crossref. Não consegui reabrir o resumo na SAGE para conferir a frase literal.\n- Item 13 (Ferracioli et al.): o Crossref mostra publicação online em fev/2022 e edição impressa em mai/2022 (vol. 10, n. 5). O ano 2022 está confirmado.\n- Item 11 (Moreno-Gil et al.): o número de entrevistados não aparece no resumo.\n- Item 18 (Dourado 2019): o método (análise de conteúdo) vem do subtítulo do artigo no Crossref, não do corpo do resumo."
}