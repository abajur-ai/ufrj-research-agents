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
   "study_type": "Pesquisa participante com questionário online (o resumo a enquadra como reflexão teórica; o método empírico consta só no texto completo)",
   "method": "No resumo: método weberiano (tipo ideal de 'jornalismo de verificação') e serviços de verificação como objeto empírico. No texto completo: questionário online com profissionais do projeto Truco nos Estados (Agência Pública).",
   "sample_size": "não informado no resumo",
   "main_finding": "A transparência se destaca como valor profissional e social no jornalismo contemporâneo, tomando-se os serviços de verificação como objeto empírico.",
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
   "study_type": "Estudo empírico de análise das checagens de duas agências (tipificação de fontes e critérios de seleção)",
   "method": "Análise do desempenho de duas agências brasileiras de checagem (Agência Lupa e Aos Fatos); técnica não detalhada no resumo.",
   "sample_size": "não informado no resumo",
   "main_finding": "As agências não explicitam os critérios de seleção do que checam e se apoiam muito em dados e estudos de fontes oficiais.",
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
   "study_type": "Estudo empírico quantitativo (survey)",
   "method": "Questionário autoaplicado com jornalistas checadores brasileiros, que indicaram o grau de concordância com afirmações.",
   "sample_size": "The sample (n=29) expressed their level of agreement with a group of statements.",
   "main_finding": "O propósito central da checagem no Brasil é detectar e combater conteúdo falso e enganoso em canais digitais.",
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
   "method": "Análise de conteúdo das checagens de Lupa e Aos Fatos sobre desinformação online, para ver o uso de ferramentas de transparência pública como fonte.",
   "sample_size": "63 checks were identified using transparency tools, which represented less than 7% of the total checks conducted (950).",
   "main_finding": "As ferramentas de transparência foram pouco usadas (menos de 7% das 950 checagens), mas decisivas nas verificações sobre agentes e autoridades públicas.",
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
   "study_type": "Estudo empírico qualitativo (análise documental e entrevistas)",
   "method": "Análise de declarações oficiais de jornalistas e parceiros de tecnologia, mais entrevistas semiestruturadas com representantes de sites de checagem.",
   "sample_size": "30 official statements published by journalists and their tech partners, and seven semi-structured interviews with representatives from five websites",
   "main_finding": "Surge um cenário de automação na checagem brasileira apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores e ampliou a influência dos tecnólogos.",
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
   "study_type": "Estudo empírico qualitativo (entrevistas)",
   "method": "Entrevistas semiestruturadas, com dados complementares coletados nos sites das iniciativas.",
   "sample_size": "semi-structured interviews with 16 fact-checkers from 13 active organizations",
   "main_finding": "A equipe reduzida e a crescente dependência de dinheiro das big techs levaram as iniciativas brasileiras a modularizar as correções por plataforma e a priorizar o debunking em vez da checagem política.",
   "abstract_quote": "Last, the limited staff of most fact-checking initiatives and their growing dependence on big tech money have led them to modularize their corrections to different platforms and publish debunking at the expense of political fact-checking."
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
   "study_type": "Estudo empírico qualitativo comparativo internacional (inclui Brasil)",
   "method": "Entrevistas em profundidade com representantes de organizações de checagem ibero-americanas (Polígrafo, Chequeado, Maldita e Aletheia).",
   "sample_size": "in-depth interviews were conducted with representatives of four fact-checking organizations: Polígrafo (Portugal), Chequeado (Argentina), Maldita (Spain), and Aletheia (Brazil).",
   "main_finding": "O uso de IA varia da ferramenta simples ao uso disruptivo, conforme a estrutura humana e a situação econômica de cada organização.",
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
   "study_type": "Estudo empírico qualitativo comparativo internacional (inclui Brasil)",
   "method": "Entrevistas em profundidade com gestores de plataformas independentes de checagem da América Latina e da Espanha, incluindo a Agência Lupa.",
   "sample_size": "In-depth interviews were conducted with decision-makers of the following independent platforms: Chequeado (Argentina), UYCheck (Uruguay), Maldita.es and Newtral (Spain), Fact Checking (Chile), Agência Lupa (Brazil), Ecuador Chequea (Ecuador), and ColombiaCheck (Colombia).",
   "main_finding": "Os entrevistados apontam três desafios centrais da prática de checagem: dificuldade de acesso a dados públicos, recursos limitados e necessidade de alcançar públicos mais amplos.",
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
   "study_type": "Estudo empírico qualitativo comparativo internacional (inclui Brasil); aderência parcial ao eixo de rotinas e métodos",
   "method": "Entrevistas semiestruturadas com jornalistas de agências de checagem (Chequeado, Colombiacheck, Fast Check CL e Aos Fatos) e revisão dos recursos de alfabetização midiática que elas publicam online.",
   "sample_size": "não informado no resumo",
   "main_finding": "Os checadores sul-americanos consideram a alfabetização midiática uma estratégia fundamental e a apoiam com oficinas, conferências e guias.",
   "abstract_quote": "The results of the interviews indicate that media literacy is a strategy considered fundamental by fact-checkers in South America."
  },
  {
   "doi": "10.51206/elegis.v15i38.758",
   "title": "Jornalismo de checagem de fatos como intermediário da transparência pública: uma análise comparada entre países",
   "authors": [
    "Paulo Ferracioli"
   ],
   "year": 2022,
   "venue": "E-Legis – Revista Eletrônica do Programa de Pós-Graduação da Câmara dos Deputados",
   "study_type": "Estudo empírico comparativo internacional (inclui Brasil)",
   "method": "Análise comparada de textos de checagem de quatro agências (Agência Lupa, Factcheck.org, Pagella Politica e Correctiv) quanto ao uso de recursos de transparência pública como fonte.",
   "sample_size": "não informado no resumo",
   "main_finding": "Em todas as agências a principal fonte foi a transparência ativa do Estado, com 63,5% dos textos no Brasil, 53,4% na Itália, 52,7% nos EUA e 29,2% na Alemanha.",
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
   "study_type": "Estudo empírico comparativo internacional (inclui Brasil)",
   "method": "Análise de conteúdo de checagens de FactCheck.org, Pagella Politica, Correctiv e Lupa, combinada com dados do survey Worlds of Journalism.",
   "sample_size": "a content analysis of 2,792 fact-checks published by FactCheck.org (United States)",
   "main_finding": "Na maioria dos casos há correspondência entre a concepção dos profissionais sobre seu papel e a postura de watchdog que as agências exercem; na Lupa o rótulo mais usado é 'true'.",
   "abstract_quote": "There is correspondence between professionals' conceptions about their role and the watchdog stance agencies perform in most cases."
  },
  {
   "doi": "10.21878/compolitica.2019.9.2.143",
   "title": "Fact-checking como possibilidade de media accountability sobre o discurso político? Uma análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco",
   "authors": [
    "Tatiana Maria Dourado"
   ],
   "year": 2019,
   "venue": "Compolítica",
   "study_type": "Estudo empírico de análise de conteúdo (conforme o título; o resumo não detalha o procedimento)",
   "method": "Análise de conteúdo das iniciativas de checagem Aos Fatos, Lupa e Truco quanto à fiscalização do discurso político e à prática de etiquetagem.",
   "sample_size": "não informado no resumo",
   "main_finding": "A prática de etiquetar não foi seguida à risca nas três iniciativas, e predominaram temas nacionais.",
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
   "study_type": "Estudo empírico qualitativo (análise documental com análise do discurso)",
   "method": "Análise do discurso de linha francesa dos textos de lançamento e de especificação dos métodos de trabalho de cinco agências brasileiras ligadas a conglomerados de mídia.",
   "sample_size": "os textos de lançamento e de especificação dos métodos de trabalho de cinco agências de fact-checking brasileiras ligadas a conglomerados de mídia",
   "main_finding": "O estudo caracteriza as principais sequências discursivas com que as agências reivindicam credibilidade e os sujeitos implicados em sua produção discursiva (o resumo não traz resultados numéricos).",
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
   "study_type": "Estudo empírico qualitativo (estudo de caso)",
   "method": "Estudo de caso complementado com entrevistas semiestruturadas, sobre a Rede Nacional de Combate à Desinformação (RNCD) e quatro iniciativas: COAR Noticias, Colectivo Bereia, Verifica RS e Agência Tatu.",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo não traz resultados; informa apenas que o estudo analisa as estratégias de implementação e verificação das iniciativas locais e as especificidades que elas enfrentam no contexto local.",
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
   "study_type": "Estudo comparativo de duas agências (Brasil e Argentina); a natureza empírica e a técnica não aparecem no resumo",
   "method": "Estudo comparativo das agências Lupa (Brasil) e Chequeado (Argentina) para verificar a mercantilização da checagem para empresas de jornalismo e outras organizações.",
   "sample_size": "não informado no resumo",
   "main_finding": "O fact-checking na América Latina é um modelo de negócio adotado pelas iniciativas, que promove o empreendedorismo jornalístico e combate a desinformação.",
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
   "method": "Estudo de caso a partir das diretrizes do Plano Editorial do Grupo Globo e da seção Fato ou Fake do Portal G1.",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo não traz resultados; indica que as diretrizes do Grupo Globo e a seção Fato ou Fake pontuam o fact-checking como estratégia de credibilidade.",
   "abstract_quote": "Para tanto, o trabalho realiza um estudo de caso a partir das diretrizes contidas no Plano Editorial do Grupo e na seção Fato ou Fake do Portal G1, que pontuam o fact-checking como estratégia de credibilidade."
  },
  {
   "doi": "10.59289/t7hc8w93",
   "title": "Desinformação, agências de fact-checking e identificação de fake news",
   "authors": [
    "Barbara Beatriccy Bentes Pinto",
    "Henry Poncio Cruz de Oliveira"
   ],
   "year": 2023,
   "venue": "Tendências da Pesquisa Brasileira em Ciência da Informação",
   "study_type": "Estudo empírico de análise documental",
   "method": "Análise das metodologias de identificação e categorização de conteúdos desinformacionais de cinco agências brasileiras (Lupa, Aos Fatos, E-farsas, UOL Confere e Estadão Verifica); coleta nos sites em maio e junho de 2022, segundo o registro do candidato.",
   "sample_size": "cinco Agências de Fact-Checking Brasileiras para identificar e categorizar conteúdos potencialmente desinformacionais: Lupa, Aos Fatos, Site E-farsas, Uol confere, Estadão Verifica",
   "main_finding": "As agências têm metodologias próprias e seus rótulos de classificação variam entre elas.",
   "abstract_quote": "As Agências possuem metodologias e suas etiquetas variam: Falso, Contraditório, Verdadeiro, Ainda e cedo pra dizer, Exagerado, Subestimado, Insustentável, Verdadeiro, mas, De olho, Não e bem assim, Sem contexto, Distorcido, Conteúdo inventado, manipulado, enganoso, impostor, Falsa conexão, Sátira ou paródia e Falso contexto."
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
   "study_type": "Estudo empírico de métodos mistos comparativo internacional (inclui Brasil)",
   "method": "Análise de conteúdo quantitativa de artigos de verificação combinada com entrevistas com especialistas.",
   "sample_size": "a quantitative content analysis of 136 verification articles (2023–2024) and 13 expert interviews",
   "main_finding": "Há variações relevantes entre os países em temas, alvos, intenções, elementos de IA, modelos generativos, métodos de detecção e estratégias de desmentido.",
   "abstract_quote": "The results revealed notable country-specific variations in topics, targets, intentions, AI elements, generative models, detection methods, and debunking strategies."
  }
 ],
 "search_notes": "Usei os 18 candidatos aprovados. Foram todos os que havia na lista, então não houve escolha entre eles. Nenhum artigo novo foi buscado. Abri os resumos nas páginas dos periódicos ou nos repositórios. A ferramenta de leitura só devolve trechos curtos de até uns 125 caracteres, então li cada resumo em partes. Onde o trecho está concatenado, ele vem de partes consecutivas lidas na página. Para os artigos de acesso bloqueado, usei: Crossref (Lelo 2023, Moreno-Gil, Canavilhas), o transcrito do commbox (Lelo 2022), o repositório da Univ. de Iowa (Ferracioli et al.) e o SSRC MediaWell (Cazzamatta). Não consegui reabrir a página de Cazzamatta no periódico, nem as da MDPI e da Taylor & Francis (403). Ressalvas de verificação: (1) Canavilhas: só reconfirmei literalmente o início da frase ('different levels of use were identified, from tooling'); o restante veio da leitura anterior do candidato e é coerente com o resumo reconfirmado em paráfrase. (2) Ferracioli et al.: o resumo completo não foi aberto no periódico, e a amostra literal cobre só o FactCheck.org (2,792 checagens); as demais agências (Pagella Politica, Correctiv, Lupa) vêm de outros trechos do resumo, sem n. A frase da citação foi lida em dois trechos consecutivos. (3) Lelo (2022): o campo main_finding vem só do trecho literal; a afirmação do candidato sobre 'ambiente organizacional' e fontes de receita não foi reconfirmada. Pontos que o pesquisador deve avaliar contra os critérios de exclusão e de empirismo: (a) Seibt & Fonseca (2019): o resumo se apresenta como reflexão teórica (tipo ideal weberiano), e o método empírico (questionário com 17 de 31 profissionais do Truco nos Estados) vem do texto completo. Esse texto situa o projeto nas eleições de 2018, o que pode ferir a exclusão de estudos centrados em eleições. (b) Nascimento et al. (2024): os dados são de 2022, ano eleitoral, mas o resumo não centra o estudo em eleições. (c) Alencar & Bittencourt (2022): o resumo não descreve corpus nem técnica, então a natureza empírica não está confirmada. (d) Dourado (2019): o período e o corpus não aparecem no resumo; o método vem do título. (e) Abuín-Penas et al. (2024): o foco é alfabetização midiática, com aderência parcial ao eixo de rotinas e métodos. (f) Nogales-Bocio et al. (2025) e Alencar & Dourado (2022): os resumos só descrevem o objetivo e o método, sem resultados, e o main_finding diz isso. (g) Anos: Lelo (2023) foi publicado online em nov/2023 e impresso em 2024, e usei 2023. Pinto & Oliveira consta como v. 16 (2023), publicado em 12/2024, e usei 2023. A Alencar & Bittencourt tem DOI 'vol25n53', mas a página do periódico traz v. 23, 2022. Todos os anos estão entre 2018 e 2025."
}