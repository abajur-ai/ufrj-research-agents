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
   "study_type": "Artigo de periódico. O resumo se apresenta como reflexão teórica pelo método weberiano (tipo ideal), e não como estudo empírico. ITEM COM RESSALVA: provavelmente não atende ao critério de estudo empírico.",
   "method": "Segundo o resumo: construção do 'jornalismo de verificação' como tipo ideal (método weberiano), com serviços de verificação como objeto empírico. Segundo o texto completo (não o resumo): pesquisa participante com questionário online no projeto Truco nos Estados (Agência Pública).",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo destaca a transparência como valor profissional e social no jornalismo contemporâneo, a partir da prática dos serviços de verificação.",
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
   "study_type": "Estudo empírico, análise das checagens de duas agências",
   "method": "Análise do desempenho da Agência Lupa e do Aos Fatos quanto às fontes usadas e aos critérios de seleção do material checado",
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
   "study_type": "Estudo empírico quantitativo (survey)",
   "method": "Questionário autoaplicado com jornalistas checadores brasileiros sobre propósitos, princípios e rotinas",
   "sample_size": "The sample (n=29) expressed their level of agreement with a group of statements.",
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
   "study_type": "Estudo empírico, análise de conteúdo das checagens da Lupa e do Aos Fatos",
   "method": "Análise de conteúdo do uso de ferramentas de transparência pública como fonte nas checagens",
   "sample_size": "63 checks were identified using transparency tools, which represented less than 7% of the total checks conducted (950).",
   "main_finding": "As ferramentas de transparência foram pouco usadas, mas decisivas nas verificações sobre agentes e autoridades públicas.",
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
   "study_type": "Estudo empírico qualitativo (análise documental e entrevistas)",
   "method": "Análise de declarações oficiais e entrevistas semiestruturadas com representantes de sites de checagem. Publicado online em 27/11/2023 (Crossref/OpenAlex); edição impressa vol. 101, n. 2, jun/2024. O campo 'year' usa 2024, a edição impressa exibida pela SAGE.",
   "sample_size": "30 official statements published by journalists and their tech partners, and seven semi-structured interviews with representatives from five websites",
   "main_finding": "Surge um cenário de automação apoiado pela indústria de tecnologia, e a IA desafiou a autoridade dos checadores e ampliou a influência dos tecnólogos sobre o jornalismo.",
   "abstract_quote": "Nonetheless, AI has challenged fact-checkers’ authority and increased technologists’ influence over journalism."
  },
  {
   "doi": "10.1080/1461670x.2022.2069588",
   "title": "The Rise of the Brazilian Fact-checking Movement: Between Economic Sustainability and Editorial Independence",
   "authors": [
    "Thales Lelo"
   ],
   "year": 2022,
   "venue": "Journalism Studies",
   "study_type": "Estudo empírico qualitativo (entrevistas semiestruturadas)",
   "method": "Entrevistas semiestruturadas, com dados complementares coletados nos sites das iniciativas",
   "sample_size": "semi-structured interviews with 16 fact-checkers from 13 active organizations",
   "main_finding": "A equipe reduzida e a crescente dependência de dinheiro das big techs levaram as iniciativas a modularizar as correções por plataforma.",
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
   "study_type": "Estudo empírico qualitativo comparativo (o resumo o chama de 'theoretical and empirical study')",
   "method": "Entrevistas em profundidade com representantes de quatro organizações de checagem (inclui a Aletheia, do Brasil)",
   "sample_size": "in-depth interviews were conducted with representatives of four fact-checking organizations: Polígrafo (Portugal), Chequeado (Argentina), Maldita (Spain), and Aletheia (Brazil).",
   "main_finding": "Há níveis diferentes de uso de IA, do simples ao avançado, ligados à estrutura humana e à situação econômica de cada organização.",
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
   "study_type": "Estudo empírico qualitativo comparativo (inclui a Agência Lupa, do Brasil)",
   "method": "Entrevistas em profundidade com gestores de plataformas independentes de checagem",
   "sample_size": "In-depth interviews were conducted with decision-makers of the following independent platforms: Chequeado (Argentina), UYCheck (Uruguay), Maldita.es and Newtral (Spain), Fact Checking (Chile), Agência Lupa (Brazil), Ecuador Chequea (Ecuador), and ColombiaCheck (Colombia).",
   "main_finding": "Os entrevistados apontam três desafios centrais da prática: acesso a dados públicos, recursos limitados e alcance de públicos mais amplos.",
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
   "study_type": "Estudo empírico qualitativo comparativo (inclui o Aos Fatos, do Brasil). Aderência parcial ao eixo de rotinas e métodos.",
   "method": "Entrevistas semiestruturadas com jornalistas de agências de verificação, mais exame dos sites das agências",
   "sample_size": "não informado no resumo",
   "main_finding": "Os checadores sul-americanos consideram a alfabetização midiática uma estratégia fundamental e realizam ações como oficinas, conferências, guias e ferramentas.",
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
   "study_type": "Estudo empírico comparativo (inclui a Agência Lupa, do Brasil)",
   "method": "Investigação comparada dos textos de quatro agências (Lupa, Factcheck.org, Pagella Politica e Correctiv) quanto ao uso de dados de transparência pública",
   "sample_size": "não informado no resumo",
   "main_finding": "Informações de transparência ativa foram a principal fonte das checagens em todas as agências, em 63,5% dos textos no Brasil.",
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
   "study_type": "Estudo empírico comparativo (inclui a Lupa, do Brasil)",
   "method": "Análise de conteúdo das checagens, combinada com dados do survey Worlds of Journalism sobre a percepção do papel de watchdog",
   "sample_size": "a content analysis of 2,792 fact-checks published by FactCheck.org (United States), Pagella Politica (Italy), Correctiv (Germany), and Lupa (Brazil)",
   "main_finding": "Na maioria dos casos, a concepção dos profissionais sobre seu papel corresponde à postura de watchdog que as agências exercem.",
   "abstract_quote": "There is correspondence between professionals’ conceptions about their role"
  },
  {
   "doi": "10.21878/compolitica.2019.9.2.143",
   "title": "Fact-checking como possibilidade de media accountability sobre o discurso político? Uma análise de conteúdo das iniciativas Aos Fatos, Lupa e Truco",
   "authors": [
    "Tatiana Maria Dourado"
   ],
   "year": 2019,
   "venue": "Compolítica",
   "study_type": "Estudo empírico, análise de conteúdo",
   "method": "Análise de conteúdo das práticas de rotulagem em Aos Fatos, Lupa e Truco",
   "sample_size": "não informado no resumo",
   "main_finding": "A prática de etiquetar não foi seguida à risca e predominaram os temas nacionais.",
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
   "study_type": "Estudo empírico qualitativo, análise documental",
   "method": "Análise do discurso de linha francesa dos textos de lançamento e de especificação dos métodos de trabalho das agências",
   "sample_size": "os textos de lançamento e de especificação dos métodos de trabalho de cinco agências de fact-checking brasileiras ligadas a conglomerados de mídia",
   "main_finding": "O estudo caracteriza as principais sequências discursivas com que as agências ligadas a conglomerados de mídia buscam credibilidade, e os sujeitos envolvidos nessa produção discursiva.",
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
   "method": "Estudo de caso qualitativo com entrevistas semiestruturadas",
   "sample_size": "não informado no resumo",
   "main_finding": "O resumo não traz resultados; informa apenas o objetivo, que é analisar as estratégias de implementação e verificação de iniciativas locais brasileiras e as especificidades que enfrentam no contexto local. Não consegui abrir o texto completo para extrair um resultado.",
   "abstract_quote": "A través de un enfoque cualitativo, se adopta el diseño de estudio de caso, complementado con entrevistas semiestruturadas, para analizar las estrategias de implementación y verificación de estas iniciativas de combate a la desinformación y las especificidades que enfrentan en el contexto local."
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
   "study_type": "Estudo comparativo de duas agências (inclui a Lupa, do Brasil). O resumo não detalha técnica nem corpus, então a natureza empírica com dados próprios não está confirmada.",
   "method": "Estudo comparativo das agências Chequeado e Lupa sobre a mercantilização da checagem (verificação como serviço para empresas de jornalismo e outras organizações)",
   "sample_size": "não informado no resumo",
   "main_finding": "O fact-checking na América Latina funciona como modelo de negócio que promove o empreendedorismo jornalístico e, ao mesmo tempo, combate a desinformação e defende a democracia.",
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
   "study_type": "Estudo empírico qualitativo, estudo de caso com análise documental",
   "method": "Estudo de caso a partir do Plano Editorial do Grupo Globo e da seção Fato ou Fake do Portal G1",
   "sample_size": "não informado no resumo",
   "main_finding": "As diretrizes do Plano Editorial e da seção Fato ou Fake tratam o fact-checking como estratégia de credibilidade. É o único resultado que o resumo traz.",
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
   "study_type": "Estudo empírico, análise documental dos sites das agências",
   "method": "Coleta de dados nos sites de cinco agências brasileiras em maio e junho de 2022, para levantar metodologias de identificação e categorização de fake news",
   "sample_size": "cinco Agências de Fact-Checking Brasileiras: Lupa, Aos Fatos, Site E-farsas, Uol confere, Estadão Verifica",
   "main_finding": "As cinco agências têm metodologias próprias e seus rótulos de classificação variam.",
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
   "study_type": "Estudo empírico de métodos mistos, comparativo (inclui o Brasil)",
   "method": "Análise de conteúdo quantitativa de artigos de verificação, combinada com entrevistas com especialistas",
   "sample_size": "a quantitative content analysis of 136 verification articles (2023–2024) and 13 expert interviews",
   "main_finding": "Há variações relevantes entre os países em temas, alvos, intenções, elementos de IA, modelos generativos, métodos de detecção e estratégias de desmentido.",
   "abstract_quote": "The results revealed notable country-specific variations"
  }
 ],
 "search_notes": "Entreguei 18 itens, que são todos os candidatos aprovados. Não havia candidato reserva e eu só podia usar a lista aprovada, então não troquei nenhum artigo.\n\n**Ressalvas que o pesquisador deve avaliar**\n- **Seibt e Fonseca (10.4000/cp.4806), item 1:** o resumo se apresenta como reflexão teórica pelo método weberiano, sem amostra nem procedimento empírico. O questionário com profissionais do Truco nos Estados (17 de 31 respostas) está só no texto completo, e o projeto atuou nas eleições de 2018. Não consigo justificar formalmente que ele cumpre o pedido. Mantive o item só para chegar às 18 vagas. Recomendo trocá-lo por outro estudo claramente empírico, se o pesquisador autorizar um candidato novo.\n- **Nogales-Bocio et al. (Doxa Comunicación):** o resumo não traz resultados, e o campo de achado diz isso. Tentei o texto completo, mas os PDFs vieram ilegíveis e o HTML retornou erro 429. O achado de fato continua sem extração.\n- **Alencar e Bittencourt (Comunicação & Inovação):** o resumo não informa corpus nem técnica, então não está confirmado que o estudo usa dados próprios. O ano segue o registro de 19/12/2022. O DOI diz \"vol25\" e a página diz v. 23.\n- **Alencar e Dourado (Intexto):** o único resultado do resumo é que as diretrizes tratam o fact-checking como estratégia de credibilidade.\n\n**Pontos que as reprovações anteriores levantaram**\n- **Ferracioli, Kniess e Marques (Digital Journalism):** abri o resumo reconstruído pelo OpenAlex. A amostra agora traz só texto do resumo (2.792 checagens, em quatro agências). O achado é a correspondência entre a concepção do papel e a postura de watchdog, e retirei o detalhe sobre o rótulo \"true\" da Lupa. A citação é só o trecho que tenho certeza de ser literal. O final da frase aparece no OpenAlex separado em dois pedaços, e não consegui confirmar a palavra de ligação entre eles.\n- **Pinto e Oliveira:** a página oficial descreve a revista como periódico científico (ISSN 1983-5116) com avaliação duplo-cega, e o Crossref a classifica como journal-article. Não é coletânea. A citação agora está completa, sem vírgula solta. Os rótulos \"Ainda e cedo\", \"Não e bem assim\" e \"Exagerado\" estão sem acento, como no Crossref. Usei 2024, a data de publicação e a que a página sugere para citação. O volume 16 é rotulado como 2023.\n- **Lelo (J&MCQ):** o campo de ano usa 2024, a edição impressa (v. 101, n. 2, jun/2024). O online first foi em 27/11/2023 (Crossref e OpenAlex) e está registrado no campo de método.\n- **Lelo (Journalism Studies):** a amostra \"16 fact-checkers from 13 active organizations\" e o trecho final \"to different platforms\" estão confirmados pelo resumo reconstruído no OpenAlex.\n- **Canavilhas e Ito:** a frase \"This is why different levels of use were identified…\" está confirmada por inteiro no OpenAlex.\n- **Cazzamatta e Sarısakaloğlu:** a citação é só o fragmento verificado, \"The results revealed notable country-specific variations\". O restante da frase do resumo ficou fora.\n\n**Limites da verificação**\n- Os resumos de Ferracioli (E-Legis), Moreno-Gil, Abuín-Penas, Lelo e Pachi, Alencar (duas), Pinto, Cazzamatta e Lelo (duas) foram conferidos nesta rodada em páginas oficiais, no Crossref ou no OpenAlex. A ferramenta de leitura limita as citações a cerca de 125 caracteres, então algumas frases longas foram remontadas a partir de trechos. Quem for conferir deve ver a pontuação e as palavras de ligação nos originais.\n- Os itens de Damasceno e Patrício, Rodríguez-Pérez e Seibt, e de Nascimento et al., já constavam como confirmados pelo verificador. Reabri o de Seibt e Fonseca, e não reabri os outros.\n- A citação de Dourado (Compolítica) vem da lista aprovada. Desta vez a página só devolveu paráfrase, coerente com ela, e a frase literal não foi reconfirmada.\n- Na amostra, escrevi \"não informado no resumo\" quando o resumo só cita as agências analisadas, sem contagem de textos ou entrevistas. Isso vale para Ferracioli (E-Legis) e Abuín-Penas."
}