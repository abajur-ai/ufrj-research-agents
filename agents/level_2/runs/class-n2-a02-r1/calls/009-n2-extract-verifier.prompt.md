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
   "doi": "10.4000/cp.4806",
   "title": "Transparência como princípio normativo do jornalismo: a prática de fact-checking no Brasil",
   "authors": [
    "Taís Seibt",
    "Virginia Pradelina da Silveira Fonseca"
   ],
   "year": 2019,
   "venue": "Comunicação Pública",
   "study_type": "Estudo sobre a prática de fact-checking no Brasil. O resumo o apresenta como reflexão normativa (método weberiano, tipo ideal). O texto completo traz pesquisa participante. INCLUSÃO COM RESSALVA (ver search_notes).",
   "method": "Resumo: método weberiano, com os serviços de verificação como objeto empírico. Texto completo (não consta no resumo): questionário online anônimo com profissionais do projeto Truco nos Estados (Agência Pública), observação na redação e entrevistas exploratórias.",
   "sample_size": "não informado no resumo",
   "main_finding": "A transparência é destacada como valor profissional e social do jornalismo de verificação contemporâneo.",
   "abstract_quote": "Ao tomar os serviços de verificação como objeto empírico de análise, destacamos a transparência como valor profissional e social no jornalismo contemporâneo."
  },
  {
   "doi": "10.25200/bjr.v16n2.2020.1212",
   "title": "Journalism and Fact-Checking: typification of sources used for checking and criteria for selecting fact-checked material – an analysis by Agência Lupa and Aos Fatos",
   "authors": [
    "Daniel de Rezende Damasceno",
    "Edgard Patrício"
   ],
   "year": 2020,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico de análise das checagens de duas agências",
   "method": "Análise das checagens da Agência Lupa e do Aos Fatos (tipificação de fontes e critérios de seleção); o resumo não detalha a técnica.",
   "sample_size": "não informado no resumo",
   "main_finding": "As agências não explicitam os critérios de seleção do que checam e se apoiam sobretudo em fontes oficiais.",
   "abstract_quote": "the agencies themselves do not lay out the criteria for selecting what is to be checked."
  },
  {
   "doi": "10.25200/BJR.v18n2.2022.1510",
   "title": "The Brazilian fact-checkers criteria: an analysis of the guiding purposes, principles, and routines of this journalistic practice",
   "authors": [
    "Carlos Rodríguez-Pérez",
    "Taís Seibt"
   ],
   "year": 2022,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico por survey",
   "method": "Questionário autoaplicado com checadores brasileiros sobre propósitos, princípios e rotinas",
   "sample_size": "n=29",
   "main_finding": "O propósito central do fact-checking brasileiro é detectar e combater conteúdo falso e enganoso em canais digitais.",
   "abstract_quote": "The results show the central purpose is to detect and combat false and misleading content on digital channels."
  },
  {
   "doi": "10.25200/BJR.v20n3.2024.1687",
   "title": "Transparência contra a desinformação? (Transparency against misinformation?)",
   "authors": [
    "Thatiany Nascimento",
    "Diógenes Lycarião",
    "Suzete Nocrato"
   ],
   "year": 2024,
   "venue": "Brazilian Journalism Research",
   "study_type": "Estudo empírico de análise de conteúdo",
   "method": "Análise de conteúdo das checagens da Lupa e do Aos Fatos, para identificar o uso de ferramentas de transparência pública",
   "sample_size": "63 checks were identified using transparency tools, which represented less than 7% of the total checks conducted (950).",
   "main_finding": "As ferramentas de transparência foram pouco usadas (menos de 7% das checagens), mas decisivas nas verificações sobre agentes e autoridades públicas.",
   "abstract_quote": "However, such tools proved decisive for verifications involving subjects, agents, and public authorities."
  },
  {
   "doi": "10.1177/10776990231207963",
   "title": "Fostering Artificial Intelligence to Face Misinformation: Discourses and Practices of Automated Fact-Checking in Brazil",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2023,
   "venue": "Journalism & Mass Communication Quarterly",
   "study_type": "Estudo empírico qualitativo",
   "method": "Análise documental de declarações oficiais e entrevistas semiestruturadas",
   "sample_size": "30 official statements published by journalists and their tech partners, and seven semi-structured interviews with representatives from five websites",
   "main_finding": "Surge um cenário de automação na checagem brasileira apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores.",
   "abstract_quote": "Nonetheless, AI has challenged fact-checkers’ authority and increased the technologists’ influence over journalism."
  },
  {
   "doi": "10.1080/1461670x.2022.2069588",
   "title": "The Rise of the Brazilian Fact-checking Movement: Between Economic Sustainability and Editorial Independence",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2022,
   "venue": "Journalism Studies",
   "study_type": "Estudo empírico qualitativo",
   "method": "Entrevistas semiestruturadas, complementadas por dados dos sites das organizações",
   "sample_size": "semi-structured interviews with 16 fact-checkers from 13 active organizations",
   "main_finding": "O ambiente organizacional define as fontes de receita, e a dependência crescente do dinheiro das big techs leva as organizações a modularizar as correções por plataforma.",
   "abstract_quote": "Last, the limited staff of most fact-checking initiatives and their growing dependence on big tech money have led them to modularize their corrections to different platforms"
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
   "study_type": "Estudo empírico qualitativo, comparativo internacional que inclui o Brasil (Aletheia)",
   "method": "Entrevistas em profundidade com representantes de organizações de checagem",
   "sample_size": "representatives of four fact-checking organizations: Polígrafo (Portugal), Chequeado (Argentina), Maldita (Spain), and Aletheia (Brazil)",
   "main_finding": "O uso de IA ocorre em níveis diferentes, do simples ao avançado, ligados à estrutura humana e à situação econômica de cada organização.",
   "abstract_quote": "This is why different levels of use were identified, from tooling (simple) to disruptive (advanced), which are related to their human structure and economic situation."
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
   "study_type": "Estudo empírico qualitativo, comparativo internacional que inclui o Brasil (Agência Lupa)",
   "method": "Entrevistas em profundidade com gestores de plataformas independentes de checagem",
   "sample_size": "decision-makers of the following independent platforms: Chequeado (Argentina), UYCheck (Uruguay), Maldita.es and Newtral (Spain), Fact Checking (Chile), Agência Lupa (Brazil), Ecuador Chequea (Ecuador), and ColombiaCheck (Colombia)",
   "main_finding": "Os entrevistados apontam três desafios centrais: acesso a dados públicos, recursos limitados e alcance de públicos mais amplos.",
   "abstract_quote": "Interviewees identified three core challenges in fact-checking practice: difficulties in accessing public data, limited resources, and the need to reach wider audiences."
  },
  {
   "doi": "10.15847/obsobs18520242436",
   "title": "Media literacy against disinformation: the vision of South American fact-checkers",
   "authors": [
    "Javier Abuín-Penas",
    "Francisco Fernández-Medina",
    "Juan-Manuel Corbacho-Valencia"
   ],
   "year": 2024,
   "venue": "Observatorio (OBS*)",
   "study_type": "Estudo empírico qualitativo, comparativo internacional que inclui o Brasil (Aos Fatos)",
   "method": "Entrevistas semiestruturadas com jornalistas de agências de verificação de dados (Chequeado, Colombiacheck, Fast Check CL e Aos Fatos)",
   "sample_size": "não informado no resumo",
   "main_finding": "Os checadores sul-americanos consideram a alfabetização midiática uma estratégia fundamental.",
   "abstract_quote": "The results of the interviews indicate that media literacy is a strategy considered fundamental"
  },
  {
   "doi": "10.51206/elegis.v15i38.758",
   "title": "Jornalismo de checagem de fatos como intermediário da transparência pública: uma análise comparada entre países",
   "authors": [
    "Paulo Ferracioli"
   ],
   "year": 2022,
   "venue": "E-Legis – Revista Eletrônica do Programa de Pós-Graduação da Câmara dos Deputados",
   "study_type": "Estudo empírico comparado, que inclui o Brasil (Agência Lupa)",
   "method": "Investigação comparada de textos de checagem de quatro agências (Lupa, Factcheck.org, Pagella Politica e Correctiv), com percentuais de textos que usam dados públicos",
   "sample_size": "não informado no resumo",
   "main_finding": "Informações oficiais de transparência ativa foram a principal fonte das checagens nos quatro países, com 63,5% dos textos no Brasil.",
   "abstract_quote": "Em todas, informações fornecidas pelo Estado em suas páginas de Internet (ou seja, transparência ativa) foram a principal fonte: em ordem, 63,5% (Brasil), 53,4% (Itália), 52,7% (EUA) e 29,2% (Alemanha) dos textos se valiam de dados públicos para suas conclusões."
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
   "study_type": "Estudo empírico comparado, que inclui o Brasil (Lupa)",
   "method": "Análise de conteúdo das checagens de FactCheck.org, Pagella Politica, Correctiv e Lupa, combinada com dados do survey Worlds of Journalism",
   "sample_size": "a content analysis of 2,792 fact-checks (o trecho que li não deixa claro se o total cobre as quatro agências)",
   "main_finding": "A concepção dos profissionais sobre seu papel corresponde, em geral, à postura de watchdog das agências; na Lupa o rótulo mais usado é \"true\".",
   "abstract_quote": "There is correspondence between professionals' conceptions about their role"
  },
  {
   "doi": "10.21878/compolitica.2019.9.2.143",
   "title": "Fact-checking como possibilidade de media accountability sobre o discurso político? Uma análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco",
   "authors": [
    "Tatiana Maria Dourado"
   ],
   "year": 2019,
   "venue": "Compolítica",
   "study_type": "Estudo empírico de análise de conteúdo",
   "method": "Análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco (rotulagem e fiscalização do discurso político); o resumo não descreve corpus nem procedimento",
   "sample_size": "não informado no resumo",
   "main_finding": "A prática de etiquetar as checagens não foi seguida à risca, e predominaram temas nacionais.",
   "abstract_quote": "A análise mostrou que a ação de etiquetar não foi seguida à risca e a predominância de temas nacionais."
  },
  {
   "doi": "10.5209/esmp.71235",
   "title": "Credibilidade em disputa no jornalismo digital: estratégias discursivas das agências de fact-checking brasileiras vinculadas aos conglomerados de mídia",
   "authors": [
    "Thales Vilela Lelo",
    "Fernando Pachi Filho"
   ],
   "year": 2021,
   "venue": "Estudios sobre el Mensaje Periodístico",
   "study_type": "Estudo empírico qualitativo de análise documental",
   "method": "Análise do discurso de linha francesa dos textos de lançamento e de especificação dos métodos de trabalho das agências",
   "sample_size": "os textos de lançamento e de especificação dos métodos de trabalho de cinco agências de fact-checking brasileiras ligadas a conglomerados de mídia",
   "main_finding": "O estudo caracteriza as principais sequências discursivas com que as agências ligadas a conglomerados de mídia reivindicam credibilidade (o resumo não traz resultados numéricos).",
   "abstract_quote": "Por meio da análise do discurso de linha francesa, caracterizamos as principais sequências discursivas utilizadas por estas iniciativas e os sujeitos implicados em sua produção discursiva."
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
   "method": "Estudo de caso complementado com entrevistas semiestruturadas, sobre estratégias de implementação e verificação de iniciativas locais",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo só informa o objetivo: analisar as estratégias de implementação e verificação das iniciativas locais e as especificidades do contexto local. Não traz resultados.",
   "abstract_quote": "A través de un enfoque cualitativo, se adopta el diseño de estudio de caso, complementado con entrevistas semiestructuradas, para analizar las estrategias de implementación y verificación de estas iniciativas de combate a la desinformación y las especificidades que enfrentan en el contexto local."
  },
  {
   "doi": "10.13037/ci.vol25n53.8624",
   "title": "Mercantilização da checagem nas agências Chequeado e Lupa na América Latina",
   "authors": [
    "Marta Thaís Alencar",
    "Maria Clara Aquino Bittencourt"
   ],
   "year": 2022,
   "venue": "Comunicação & Inovação",
   "study_type": "Estudo comparativo de duas agências, que inclui o Brasil (Lupa). O caráter empírico não é detalhado no resumo.",
   "method": "Estudo comparativo das agências Lupa e Chequeado sobre estratégias, negócios e mercantilização da checagem",
   "sample_size": "não informado no resumo",
   "main_finding": "O fact-checking na América Latina funciona como modelo de negócio que promove o empreendedorismo jornalístico e combate a desinformação.",
   "abstract_quote": "Com base nos resultados, o artigo revela que o fact-checking na América Latina é um modelo de negócio adotado pelas iniciativas, que promove o empreendedorismo jornalístico e atua ao mesmo tempo, no combate à desinformação e na defesa pela democracia."
  },
  {
   "doi": "10.19132/1807-8583202253.101015",
   "title": "Credibilidade em jogo: o uso do fact-checking no portal G1 e a checagem colaborativa nas Organizações Globo",
   "authors": [
    "Marta Thaís Alencar",
    "Jacqueline Lima Dourado"
   ],
   "year": 2022,
   "venue": "Intexto",
   "study_type": "Estudo de caso com análise documental",
   "method": "Estudo de caso a partir do Plano Editorial do Grupo Globo e da seção Fato ou Fake do Portal G1",
   "sample_size": "não informado no resumo",
   "main_finding": "As diretrizes do Grupo Globo apresentam o fact-checking (Fato ou Fake) como estratégia de credibilidade. O resumo não traz outros resultados.",
   "abstract_quote": "Para tanto, o trabalho realiza um estudo de caso a partir das diretrizes contidas no Plano Editorial do Grupo e na seção Fato ou Fake do Portal G1, que pontuam o fact-checking como estratégia de credibilidade."
  },
  {
   "doi": "10.59289/t7hc8w93",
   "title": "Desinformação, agências de fact-checking e identificação de fake news",
   "authors": [
    "Barbara Beatriccy Bentes Pinto",
    "Henry Poncio Cruz de Oliveira"
   ],
   "year": 2024,
   "venue": "Tendências da Pesquisa Brasileira em Ciência da Informação",
   "study_type": "Estudo empírico de análise documental",
   "method": "Coleta de dados nos sites de cinco agências brasileiras (Lupa, Aos Fatos, E-farsas, UOL Confere e Estadão Verifica), em maio e junho de 2022, para comparar metodologias de identificação e categorização",
   "sample_size": "cinco Agências de Fact-Checking Brasileiras para identificar e categorizar conteúdos potencialmente desinformacionais: Lupa, Aos Fatos, Site E-farsas, Uol confere, Estadão Verifica",
   "main_finding": "As agências têm metodologias próprias, e os rótulos de classificação variam entre elas.",
   "abstract_quote": "As Agências possuem metodologias e suas etiquetas variam: Falso, Contraditório, Verdadeiro, Ainda e cedo pra dizer,"
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
   "study_type": "Estudo empírico de métodos mistos, comparativo internacional que inclui o Brasil",
   "method": "Análise de conteúdo quantitativa de artigos de verificação, mais entrevistas com especialistas",
   "sample_size": "a quantitative content analysis of 136 verification articles (2023–2024) and 13 expert interviews",
   "main_finding": "Há variações relevantes entre países em temas, alvos, elementos de IA, métodos de detecção e estratégias de desmentido.",
   "abstract_quote": "The results revealed notable country-specific variations in topics, targets, intentions, AI elements, generative models, detection methods, and debunking strategies."
  }
 ],
 "search_notes": "Entreguei 18 itens, que são os 18 da lista aprovada. Pediram 18 e a lista tem exatamente 18, então não houve escolha possível. Conferi os resumos em páginas dos periódicos, no OpenAlex ou no Crossref. Corrigi os pontos da reprovação anterior.\n\n1) Seibt e Fonseca (2019) é a inclusão mais frágil.\n- O resumo se apresenta como \"reflexão\" normativa, pelo método weberiano. Não traz amostra nem procedimento empírico. Marquei \"não informado no resumo\".\n- O texto completo, lido via página do periódico, relata pesquisa participante. Ela inclui um questionário online respondido por 17 dos 31 profissionais do Truco nos Estados e uma semana de observação na redação da Agência Pública. Também inclui entrevistas exploratórias com Lupa, Aos Fatos e Truco.\n- Esse trabalho de campo foi feito na primeira volta das eleições de 2018, e o texto completo menciona as eleições. O resumo não menciona. O foco declarado é a transparência como princípio da prática de checagem, e não as eleições.\n- Mesmo assim, o artigo pode violar a exclusão de ensaios teóricos e a de estudos centrados em eleições. Não havia substituto na lista aprovada. Se o pesquisador preferir, ele pode ser retirado, e a lista fica com 17.\n\n2) Lelo (2023), J&MCQ. O OpenAlex e o Crossref dão publicação online em 27/11/2023 (ano 2023). A edição impressa é de junho de 2024, vol. 101(2), e é por isso que a SAGE mostra 2024. Mantive 2023 por ser a primeira publicação.\n\n3) Lelo (2022), Journalism Studies. O OpenAlex confirma \"16 fact-checkers from 13 active organizations\" e que os dados dos sites são complementares. A frase citada vem de uma transcrição do resumo no commbox. O site da T&F continuou bloqueado, e o OpenAlex só fornece paráfrase.\n\n4) Confirmei a citação literal do resumo, por reconstrução do OpenAlex ou leitura da página do periódico, nestes casos:\n- Lelo (2023).\n- Canavilhas e Ito.\n- Moreno-Gil et al.\n- Abuín-Penas et al. A frase correta é \"The results of the interviews indicate that media literacy is a strategy considered fundamental…\". O resumo não informa o número de entrevistas.\n- Ferracioli (E-Legis).\n- Dourado.\n- Alencar e Bittencourt.\n- Alencar e Dourado.\n- Lelo e Pachi Filho.\n- Nogales-Bocio et al. A grafia é \"semiestructuradas\", e não \"semiestruturadas\" como estava antes.\n- Cazzamatta e Sarısakaloğlu.\n- Pinto e Oliveira.\nOs resumos de Damasceno e Patrício, de Rodríguez-Pérez e Seibt e de Nascimento et al. foram confirmados pelo verificador na rodada anterior. Não os abri de novo.\n\n5) Ferracioli, Kniess e Marques (Digital Journalism). Só consegui ver fragmentos do resumo. A citação é o início verificável de uma frase mais longa. O total de 2.792 checagens aparece no resumo, mas não ficou claro se cobre as quatro agências. O resumo menciona Trump no FactCheck.org, o que não é o foco do estudo.\n\n6) Anos divergentes.\n- Pinto e Oliveira: o volume é de 2023, mas a publicação foi em 18/12/2024. Usei 2024.\n- Alencar e Bittencourt: o DOI diz vol25, e a página do periódico diz v. 23, n. 53, 2022. Usei 2022.\n\n7) Limites de conteúdo.\n- Os resumos de Nogales-Bocio et al., de Alencar e Dourado e, em parte, de Alencar e Bittencourt não trazem resultados. O achado informado é o objetivo ou o escopo, e avisei isso no campo.\n- A natureza empírica de Alencar e Bittencourt não está detalhada no resumo e precisa ser confirmada no texto completo.\n- O artigo de Nascimento et al. usa dados de 2022 (ano eleitoral). O resumo não cita eleições.\n- Abuín-Penas et al. aderem só em parte ao eixo de rotinas e métodos."
}