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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre jogos educativos e jogos de inoculação (prebunking) contra desinformação, como o Bad News. Restrições: apenas intervenções em forma de jogo (digital ou de tabuleiro) avaliadas com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção; exclua intervenções que não são jogos (vídeos, textos ou infográficos isolados), reanálises de dados de outros estudos e estudos centrados em COVID-19, vacinas, eleições ou política partidária (por exemplo, o Go Viral!). Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CANDIDATOS A VERIFICAR:
{
 "candidates": [
  {
   "doi": "10.1057/s41599-019-0279-9",
   "title": "Fake news game confers psychological resistance against online misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2019,
   "venue": "Palgrave Communications",
   "checked_url": "https://api.crossref.org/works/10.1057/s41599-019-0279-9 (metadados); https://api.semanticscholar.org/graph/v1/paper/DOI:10.1057/s41599-019-0279-9 (resumo)",
   "criteria_met": [
    "Tipo de estudo e método: estudo empírico com desenho pré e pós-jogo (Bad News, jogo online de navegador)",
    "Amostra: N = 15,000 (o fragmento recuperado do resumo veio truncado em 'with N'; o Crossref indica cerca de 15.000, então confira o formato exato)",
    "Achado principal: a capacidade de identificar e resistir à desinformação melhorou após jogar o Bad News, independentemente de escolaridade, idade, ideologia e estilo cognitivo",
    "Trecho do resumo: \"people’s ability to spot and resist misinformation improves after gameplay\"",
    "Jogo; periódico revisado por pares (journal-article); 2019; sem foco em COVID, vacinas ou eleições"
   ]
  },
  {
   "doi": "10.5334/joc.91",
   "title": "Good News about Bad News: Gamified Inoculation Boosts Confidence and Cognitive Immunity Against Fake News",
   "authors": [
    "Melisa Basol",
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2020,
   "venue": "Journal of Cognition",
   "checked_url": "https://www.journalofcognition.org/articles/10.5334/joc.91 e Europe PMC (DOI:10.5334/joc.91)",
   "criteria_met": [
    "Tipo de estudo e método: experimento com delineamento misto 2 (tratamento vs. controle) × 2 (pré vs. pós); replicação e extensão com grupo de controle gamificado",
    "Amostra: N = 196",
    "Achado principal: jogar o Bad News melhorou a capacidade de identificar técnicas de desinformação em comparação com o controle gamificado e aumentou a confiança nos próprios julgamentos",
    "Trecho do resumo: \"We find that playing Bad News significantly improves people's ability to spot misinformation techniques\"",
    "Jogo; periódico; 2020; tema geral de fake news"
   ]
  },
  {
   "doi": "10.1186/s41235-023-00505-x",
   "title": "Game-based inoculation versus graphic-based inoculation to combat misinformation: a randomized controlled trial",
   "authors": [
    "Bo Hu",
    "Xing-Da Ju",
    "Huan-Huan Liu",
    "Han-Qian Wu",
    "Chao Bi",
    "Chang Lu"
   ],
   "year": 2023,
   "venue": "Cognitive Research: Principles and Implications",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1186/s41235-023-00505-x&resultType=core&format=json; https://api.crossref.org/works/10.1186/s41235-023-00505-x",
   "criteria_met": [
    "Tipo de estudo e método: ensaio controlado randomizado (jogo de inoculação vs. inoculação gráfica vs. controle), com seguimento de duas semanas",
    "Amostra: 180 participantes chineses (resumo: 'A total of 180 Chinese participants were randomly assigned')",
    "Achado principal: o jogo reduziu a credibilidade percebida e a intenção de compartilhar desinformação, e foi mais eficaz que a intervenção gráfica na credibilidade percebida",
    "Trecho do resumo: \"significantly decreased the perceived credibility and sharing intention of misinformation\"",
    "Há um braço gráfico (não jogo), mas o jogo é a intervenção principal avaliada; periódico; 2023"
   ]
  },
  {
   "doi": "10.36850/e12",
   "title": "Gamified Inoculation Against Misinformation in India: A Randomized Control Trial",
   "authors": [
    "Trisha Harjani",
    "Melisa-Sinem Basol",
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2023,
   "venue": "Journal of Trial and Error",
   "checked_url": "https://api.crossref.org/works/10.36850/e12; https://api.semanticscholar.org/graph/v1/paper/DOI:10.36850/e12",
   "criteria_met": [
    "Tipo de estudo e método: ensaio controlado randomizado de campo no norte da Índia com jogo de inoculação (resultado nulo)",
    "Amostra: n = 757",
    "Achado principal: o estudo não replicou os efeitos anteriores; a intervenção não teve efeito significativo sobre a confiabilidade percebida, a confiança nem a disposição de compartilhar",
    "Trecho do resumo: \"We found no significant impact of the intervention on the perceived reliability of messages containing misinformation\"",
    "Jogo; periódico; 2023; desinformação geral"
   ]
  },
  {
   "doi": "10.1037/xge0001603",
   "title": "Feedback exercises boost discernment of misinformation for gamified inoculation interventions",
   "authors": [
    "Johannes Leder",
    "Lukas Valentin Schellinger",
    "Rakoen Maertens",
    "Sander van der Linden",
    "Breanne Chryst",
    "Jon Roozenbeek"
   ],
   "year": 2024,
   "venue": "Journal of Experimental Psychology: General",
   "checked_url": "https://api.crossref.org/works/10.1037/xge0001603; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/xge0001603&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: seis experimentos (dois de laboratório pré-registrados e quatro de pesquisa dentro do jogo) com Bad News e Harmony Square, com e sem exercício de feedback",
    "Amostra: N1 = 191, N2 = 321 nos experimentos de laboratório; os experimentos 3–6 têm N = 559, 2,558, 419 e 882 (valores recuperados do resumo, a conferir)",
    "Achado principal: acrescentar exercícios de feedback depois do jogo aumenta o discernimento entre notícias falsas e verdadeiras, principalmente por melhorar a identificação de notícias reais",
    "Trecho do resumo: \"this significantly boosts discernment compared with playing the game without a feedback exercise\"",
    "Jogo; periódico; 2024 (agosto); um dos jogos (Harmony Square) é de política, mas o foco do estudo é o efeito do feedback e o Bad News predomina"
   ]
  },
  {
   "doi": "10.1098/rsos.211719",
   "title": "Technique-based inoculation against real-world misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Cecilie S. Traberg",
    "Sander van der Linden"
   ],
   "year": 2022,
   "venue": "Royal Society Open Science",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1098/rsos.211719&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: dois experimentos com o jogo Bad News, com amostra de conveniência recrutada pela plataforma do jogo",
    "Amostra: total n = 2188 (dois experimentos)",
    "Achado principal: um jogo de 15 minutos confere resistência psicológica à desinformação do mundo real (d = 0,37), com proteção cruzada menor para técnicas não treinadas",
    "Trecho do resumo: \"We find that playing a 15 min game confers psychological resistance against real-world misinformation\"",
    "Jogo; periódico; 2022 (há uma errata de 2023, 10.1098/rsos.231235, que não conta)"
   ]
  },
  {
   "doi": "10.1037/xap0000315",
   "title": "Long-term effectiveness of inoculation against misinformation: Three longitudinal experiments",
   "authors": [
    "Rakoen Maertens",
    "Jon Roozenbeek",
    "Melisa Basol",
    "Sander van der Linden"
   ],
   "year": 2021,
   "venue": "Journal of Experimental Psychology: Applied",
   "checked_url": "https://api.crossref.org/works/10.1037/xap0000315 (publicado em 2021-03, vol. 27, nº 1); https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/xap0000315&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: três experimentos longitudinais; Bad News (inoculação) vs. Tetris (controle gamificado)",
    "Amostra: Experimento 1 (n=151), Experimento 2 (n=194), Experimento 3 (n=170) (valores recuperados do resumo, a conferir)",
    "Achado principal: o efeito de inoculação do jogo ficou estável por pelo menos 3 meses no Experimento 1, mas decaiu em 2 meses no Experimento 2",
    "Trecho do resumo: \"participants rate fake news as significantly less reliable after the intervention\"",
    "Jogo; periódico; 2021 (ano oficial do fascículo); estudo empírico, não reanálise"
   ]
  },
  {
   "doi": "10.37016//mr-2020-008",
   "title": "Prebunking interventions based on the psychological theory of \"inoculation\" can reduce susceptibility to misinformation across cultures",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden",
    "Thomas Nygren"
   ],
   "year": 2020,
   "venue": "Harvard Kennedy School Misinformation Review",
   "checked_url": "https://misinforeview.hks.harvard.edu/article/global-vaccination-badnews/ (a página exibe o DOI com barra dupla, igual ao registro do Crossref)",
   "criteria_met": [
    "Tipo de estudo e método: quatro experimentos voluntários dentro do jogo, um por versão linguística do Bad News (desenho pré e pós)",
    "Amostra: não informado no resumo",
    "Achado principal: o Bad News confere resistência psicológica a estratégias de desinformação em diferentes culturas",
    "Trecho do resumo: \"can confer psychological resistance against common online misinformation strategies across different cultures\"",
    "Jogo; periódico; 2020; o DOI tem barra dupla no registro oficial"
   ]
  },
  {
   "doi": "10.62758/re.302",
   "title": "Jogo Meias#Verdades: o método prebunking no combate à desinformação no contexto brasileiro",
   "authors": [
    "Karoline Maria Fernandes",
    "Nadi Helena Presser",
    "Luciana Monteiro Krebs",
    "R. F. Carmo"
   ],
   "year": 2025,
   "venue": "Revista EDICIC",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.62758/re.302 e https://api.crossref.org/works?query.bibliographic=... (registro com data 2025-12-12)",
   "criteria_met": [
    "Tipo de estudo e método: avaliação com voluntários, com questionário antes e depois do jogo e teste t pareado (sem grupo de controle descrito no resumo)",
    "Amostra: (N=55)",
    "Achado principal: após jogar, os voluntários reduziram a vulnerabilidade às estratégias de desinformação",
    "Trecho do resumo: \"os voluntários reduziram seu grau de vulnerabilidade frente às estratégias de desinformação\"",
    "Jogo de prebunking; periódico; 2025; desinformação geral; o desenho pré e pós foi inferido do teste t pareado e de 'após jogarem'"
   ]
  },
  {
   "doi": "10.11645/18.2.13",
   "title": "Chaos creator",
   "authors": [
    "Mandi Goodsett"
   ],
   "year": 2024,
   "venue": "Journal of Information Literacy",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.11645/18.2.13",
   "criteria_met": [
    "Tipo de estudo e método: estudo quase-experimental com estudantes de graduação; técnicas de prebunking entregues pelo jogo competitivo Chaos Creator (baseado no Bad News), comparadas ao teste CRAP",
    "Amostra: não informado no resumo",
    "Achado principal: as técnicas de inoculação ajudaram mais os estudantes a identificar desinformação do que o teste CRAP, mas podem gerar ceticismo excessivo",
    "Trecho do resumo: \"Via a quasi-experimental study, this research explores the effect of prebunking techniques\"",
    "Jogo; periódico; 2024 (29 nov. 2024)"
   ]
  },
  {
   "doi": "10.1016/j.compedu.2023.104832",
   "title": "Misinformation Is Contagious: Middle school students learn how to evaluate and share information responsibly through a digital game",
   "authors": [
    "Sarit Barzilai",
    "Shiri Mor-Hagani",
    "Fayez Abed",
    "Danna Tal-Savir",
    "Na'ama Goldik",
    "Ina Talmon",
    "Ohad Davidow"
   ],
   "year": 2023,
   "venue": "Computers & Education",
   "checked_url": "https://cris.iucc.ac.il/en/publications/misinformation-is-contagious-middle-school-students-learn-how-to-/ ; https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.compedu.2023.104832",
   "criteria_met": [
    "Tipo de estudo e método: dois estudos experimentais com jogo digital vs. jogo de linguagem de controle, com alunos do 7º e 8º anos",
    "Amostra: (N = 84 and N = 131)",
    "Achado principal: jogar o jogo de desinformação melhorou o discernimento de acurácia e de compartilhamento, mas não alterou as posturas autorrelatadas sobre compartilhar desinformação",
    "Trecho do resumo: \"playing the misinformation game resulted in better accuracy discernment, sharing discernment\"",
    "Jogo; periódico; 2023"
   ]
  },
  {
   "doi": "10.30935/cedtech/14335",
   "title": "Can pre-service teachers learn about fake news by playing an augmented reality escape game?",
   "authors": [
    "Josef Buchner",
    "Elke Höfler"
   ],
   "year": 2024,
   "venue": "Contemporary Educational Technology",
   "checked_url": "https://www.cedtech.net/article/can-pre-service-teachers-learn-about-fake-news-by-playing-an-augmented-reality-escape-game-14335",
   "criteria_met": [
    "Tipo de estudo e método: desenho pré e pós-teste com um escape game em realidade aumentada (Escape Fake)",
    "Amostra: \"a pre-/post-test design was conducted with 45 pre-service teachers\"",
    "Achado principal: aumentaram o conhecimento sobre fake news, o senso crítico e a confiança, mas o jogo não melhorou a capacidade de distinguir informação verdadeira de falsa",
    "Trecho do resumo: \"playing the game did not promote the ability to discern real from false information\"",
    "Jogo (escape game); periódico; 2024"
   ]
  },
  {
   "doi": "10.1080/15391523.2024.2338451",
   "title": "Bad News in the civics classroom: How serious gameplay fosters teenagers' ability to discern misinformation techniques",
   "authors": [
    "Carl-Anton Werner Axelsson",
    "Thomas Nygren",
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2024,
   "venue": "Journal of Research on Technology in Education",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/15391523.2024.2338451; https://api.crossref.org/works/10.1080/15391523.2024.2338451 (online 2024-04-19; impresso 2025-09-03, vol. 57, nº 5)",
   "criteria_met": [
    "Tipo de estudo e método: estudo experimental em sala de aula com o Bad News (individual, em duplas e com a turma toda), pré e pós",
    "Amostra: \"We therefore evaluated its impact on 516 upper-secondary Swedish students\"",
    "Achado principal: os estudantes melhoraram a capacidade de discernir técnicas de manipulação em postagens de redes sociais",
    "Trecho do resumo: \"Results show that students improved their ability to discern manipulation techniques in social media posts.\"",
    "Jogo; periódico; ano 2024 (online) e 2025 (fascículo), ambos dentro do período"
   ]
  },
  {
   "doi": "10.3991/ijim.v17i15.40865",
   "title": "Enhancing Information Literacy for Spotting Fake News: A Study on the Efficacy of a Serious Game for M-Learning Across Different Age Groups",
   "authors": [
    "Pradorn Sureephong",
    "Suepphong Chernbumroong",
    "Sumalee Sangamuang",
    "Orasa Sirasakamol",
    "Kannikar Intawong",
    "Kitti Puritat"
   ],
   "year": 2023,
   "venue": "International Journal of Interactive Mobile Technologies (iJIM)",
   "checked_url": "https://online-journals.org/index.php/i-jim/article/view/40865",
   "criteria_met": [
    "Tipo de estudo e método: estudo de campo online randomizado com pré e pós-testes, com o serious game 'How to Spot Fake News'",
    "Amostra: \"quantitative research based on pre-posttests involving 351 participants\"",
    "Achado principal: o jogo melhorou o conhecimento de letramento informacional para avaliar fontes online",
    "Trecho do resumo: \"using a serious game of 'How to Spot Fake News' can improve the knowledge of information literacy needed to evaluate online sources\"",
    "Jogo; periódico; 2023"
   ]
  },
  {
   "doi": "10.5334/joc.324",
   "title": "Mixed News about the Bad News Game",
   "authors": [
    "Graham ME",
    "Skov B",
    "Gilson Z",
    "Heise C",
    "Fallow KM",
    "Mah EY",
    "Lindsay DS"
   ],
   "year": 2023,
   "venue": "Journal of Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.5334/joc.324&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: quatro replicações estendidas, com dados novos coletados por equipes de estudantes de graduação (não é reanálise)",
    "Amostra: não informado no resumo",
    "Achado principal: o Bad News reduziu a crença em tweets falsos, mas também em tweets verdadeiros na mesma medida, deslocando o viés de resposta sem melhorar a discriminação",
    "Trecho do resumo: \"But playing the BNG also reduced belief in true Tweets to the same or almost the same extent.\"",
    "Jogo; periódico; 2023; o Europe PMC lista o tipo como 'research-article; News', então confirme se o periódico o trata como artigo empírico"
   ]
  },
  {
   "doi": "10.1038/s41598-023-43885-2",
   "title": "How to \"inoculate\" against multimodal misinformation: A conceptual replication of Roozenbeek and van der Linden (2020)",
   "authors": [
    "J. Neylan",
    "M. Biddlestone",
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2023,
   "venue": "Scientific Reports",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41598-023-43885-2&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: experimento randomizado (replicação conceitual) com o jogo Cat Park, que cobre técnicas de manipulação e desinformação multimodal",
    "Amostra: \"conceptual replication (N = 380)\"",
    "Achado principal: os jogadores consideraram a desinformação menos confiável e se mostraram menos dispostos a compartilhá-la, sem ganho significativo de confiança",
    "Trecho do resumo: \"people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001)\"",
    "Jogo; periódico; 2023; é replicação conceitual, com dados próprios"
   ]
  },
  {
   "doi": "10.1371/journal.pone.0326928",
   "title": "Investigating the long-term impact of misinformation interventions in upper secondary education",
   "authors": [
    "Thomas Nygren",
    "Elena Efimova"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1371/journal.pone.0326928&resultType=core&format=json",
   "criteria_met": [
    "Tipo de estudo e método: desenho experimental em salas de aula, com Bad News (jogo) e oficina News Evaluator (não é jogo) vs. controle, com seguimento de três meses",
    "Amostra: \"Using an experimental design with 459 students in authentic classroom settings\"",
    "Achado principal: nem o jogo Bad News nem a oficina melhoraram significativamente a capacidade dos estudantes de avaliar notícias",
    "Trecho do resumo: \"Neither the Bad News game nor the News Evaluator workshop significantly improved students' ability\"",
    "Jogo é um dos braços avaliados; periódico; 2025; resultado nulo"
   ]
  },
  {
   "doi": "10.5209/esmp.88599",
   "title": "Winning the game against fake news? Using games to inoculate adolescents and young adults in Singapore against fake news",
   "authors": [
    "Edson C. Tandoc",
    "Seth Seet"
   ],
   "year": 2023,
   "venue": "Estudios sobre el Mensaje Periodístico",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.5209/esmp.88599",
   "criteria_met": [
    "Tipo de estudo e método: estudo experimental comparando quem jogou um jogo de fake news com quem não jogou (o resumo não diz se a alocação foi aleatória)",
    "Amostra: \"college (n = 84) and junior high and secondary school (n = 30) students\"",
    "Achado principal: quem jogou teve pontuação maior na detecção de fake news do que quem não jogou",
    "Trecho do resumo: \"those who played the game scored higher in detecting fake news than those who did not play the game.\"",
    "Jogo; periódico; 2023 (dez.)"
   ]
  },
  {
   "doi": "10.1007/s10758-024-09749-y",
   "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2024,
   "venue": "Technology, Knowledge and Learning",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10758-024-09749-y",
   "criteria_met": [
    "Tipo de estudo e método: estudo de campo com desenho pré e pós-teste (sem grupo de controle no resumo) do escape game em realidade aumentada Escape Fake",
    "Amostra: \"A total of 28 students (14 girls, mean age = 14.71 years) participated.\"",
    "Achado principal: o jogo atingiu quatro objetivos de aprendizagem sobre detecção de fake news, com maior efeito na aquisição de conhecimento",
    "Trecho do resumo: \"The results show that Escape Fake can address four learning objectives relevant in fake news detection\"",
    "Jogo (escape game); periódico; 2024 (online em 19 jun. 2024)"
   ]
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.21240/mpaed/51/2023.01.12.x",
   "criteria_met": [
    "Tipo de estudo e método: estudo-piloto com desenho pré e pós-teste (sem grupo de controle) do escape game Escape Fake",
    "Amostra: \"wurde ein Vortest-Nachtest Design mit 27 Schüler:innen durchgeführt\"",
    "Achado principal: o jogo conseguiu transmitir conhecimento sobre fake news e promover a capacidade de reconhecer a confiabilidade das informações",
    "Trecho do resumo: \"Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln\"",
    "Jogo (escape game); periódico; 2023; amostra (27) diferente da de Buchner 2024 (28) e da de Buchner & Höfler 2024 (45), então não é duplicata, mas o mesmo jogo pode se repetir entre os artigos"
   ]
  },
  {
   "doi": "10.1080/13669877.2018.1443491",
   "title": "The fake news game: actively inoculating against the risk of misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2018,
   "venue": "Journal of Risk Research",
   "checked_url": "https://www.repository.cam.ac.uk/handle/1810/278736 ; https://api.crossref.org/works?query.bibliographic=... (ano 2018; o fascículo impresso é vol. 22, 2019)",
   "criteria_met": [
    "Tipo de estudo e método: estudo de campo randomizado (teste-piloto) com um jogo em que os participantes criam uma notícia falsa, em um liceu público",
    "Amostra: \"we conducted a randomized field study (N = 95)\"",
    "Achado principal: jogar reduziu a confiabilidade percebida (e, de forma preliminar, a persuasão) de artigos de fake news",
    "Trecho do resumo: \"Results provide some preliminary evidence that playing the fake news game reduced the perceived reliability\"",
    "Jogo; periódico; ano 2018 (online) ou 2019 (fascículo), ambos dentro do período; o resumo não apresenta o estudo como centrado em política partidária"
   ]
  },
  {
   "doi": "10.3390/educsci9020155",
   "title": "MAthE the Game: A Serious Game for Education and Training in News Verification",
   "authors": [
    "Anastasia Katsaounidou",
    "Lazaros Vrysis",
    "Rigas Kotsakis",
    "Charalampos A. Dimoulas",
    "Andreas Veglis"
   ],
   "year": 2019,
   "venue": "Education Sciences",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/educsci9020155",
   "criteria_met": [
    "Tipo de estudo e método: estudo de campo online randomizado com o serious game MAthE, mais uma avaliação de usabilidade com uma turma",
    "Amostra: \"a randomized online field study (n = 111)\"",
    "Achado principal: o jogo pode aumentar a conscientização e ensinar ferramentas de autenticação de notícias, com evidência preliminar",
    "Trecho do resumo: \"it is validated that the game can raise awareness, teach about authentication tools\"",
    "Jogo; periódico; 2019 (24 jun.); o resumo também descreve o desenvolvimento do jogo, mas inclui avaliação empírica"
   ]
  },
  {
   "doi": "10.1027/1864-1105/a000471",
   "title": "Experimental Testing of Active vs. Passive Inoculation Interventions on Adolescents' News Discernment and Learning Enjoyment",
   "authors": [
    "Anne Reinhardt",
    "Claudia Wilhelm",
    "Sophie Mayen"
   ],
   "year": 2025,
   "venue": "Journal of Media Psychology",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1027/1864-1105/a000471",
   "criteria_met": [
    "Tipo de estudo e método: experimento escolar com pré e pós, comparando intervenção ativa (jogo online) e passiva (folheto)",
    "Amostra: \"In a school experiment involving 373 participants\"",
    "Achado principal: a diversão foi maior com o jogo, sem diferença de desempenho entre as duas intervenções; os alunos melhoraram em notícias falsas e pioraram em notícias reais",
    "Trecho do resumo: \"enjoyment was significantly higher in the active intervention group compared to the passive one\"",
    "Jogo (braço ativo); periódico; 2025 (20 mai. 2025); o folheto não é jogo, mas o jogo é uma das duas intervenções avaliadas"
   ]
  },
  {
   "doi": "10.1177/0013164420940378",
   "title": "Disentangling Item and Testing Effects in Inoculation Research on Online Misinformation: Solomon Revisited",
   "authors": [
    "Jon Roozenbeek",
    "Rakoen Maertens",
    "William McClanahan",
    "Sander van der Linden"
   ],
   "year": 2020,
   "venue": "Educational and Psychological Measurement",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1177/0013164420940378",
   "criteria_met": [
    "Tipo de estudo e método: dois estudos online com delineamento de três grupos de Solomon, usando o jogo Bad News",
    "Amostra: \"two online studies (total N = 2,159) using the Bad News game\"",
    "Achado principal: os efeitos de inoculação sofrem alguma influência dos itens, mas não de efeitos de teste, e o jogo melhora a capacidade de identificar técnicas de desinformação",
    "Trecho do resumo: \"inoculation interventions are effective at improving people’s ability to spot misinformation techniques\"",
    "Jogo; periódico; 2020 (16 jul. 2020); dados próprios (dois estudos online), não reanálise"
   ]
  }
 ],
 "notes": "RESULTADO: entreguei 24 artigos que atendem a todos os critérios, 1 a menos que os 25 pedidos. Preferi ficar abaixo do número a incluir artigos duvidosos.\n\nCOMO VERIFIQUEI: os metadados vieram do Crossref, do Semantic Scholar e do Europe PMC, e algumas páginas de periódicos abriram. Muitos sites de editoras (Springer, Wiley, APA, Sage, MDPI, ScienceDirect) devolveram 403 ou redirecionamento. Por isso os trechos entre aspas são fragmentos literais de até cerca de 120 caracteres devolvidos pela ferramenta de leitura, não o resumo completo. Vale conferir 3 pontos nos resumos oficiais:\n- Roozenbeek & van der Linden 2019: o fragmento do N veio truncado ('N'), e o valor 15,000 vem do Crossref/Semantic Scholar.\n- Leder 2024: os N dos experimentos 3–6 vêm do resumo recuperado, mas não foram reconferidos palavra por palavra.\n- Maertens 2021: os n dos três experimentos (151, 194, 170) vêm do resumo recuperado.\n\nEXCLUÍDOS DE PROPÓSITO (por motivo):\n- Harmony Square (10.37016/mr-2020-47): o corpo do artigo trata de desinformação eleitoral, embora o resumo diga só 'política'. Pelo plano, exclui-se.\n- Traberg et al. 2024 (10.37016/mr-2020-141): o foco é desinformação vinda de fontes políticas alinhadas ou não ao leitor (endogrupo partidário), o que é política partidária.\n- Seabrooke et al. (10.3758/s13423-025-02827-x): online em dez. 2025, mas fascículo impresso em jan. 2026. O ano oficial do periódico seria 2026, fora do período. Se aceitar a data online, o artigo entra.\n- Wong & Wu 2023 (10.1080/13669877.2023.2249909): replicação em Singapura feita durante a pandemia e enquadrada como risco de saúde pública. Pode ser incluída se a regra de COVID for lida de forma estrita ao conteúdo.\n- Barzilai & Stadtler 2025 (10.1016/j.compedu.2024.105210): não consegui abrir o resumo (sem abstract no Crossref/Semantic Scholar e 403 no ScienceDirect), então não há trecho literal. Fontes secundárias indicam 132 alunos do 8º e 9º anos em um experimento 2×2, e o artigo provavelmente atende aos critérios.\n- Maertens et al. 2025 (Nature Communications, 10.1038/s41467-025-57205-x): compara texto, vídeo e jogo, então a intervenção não é só jogo.\n- Cranky Uncle (Cook et al., 10.1080/13504622.2022.2085671): estudos de caso qualitativos, sem experimento.\n- Fakey (10.1145/3449080): análise de registros de uso e entrevistas, sem desenho experimental.\n- LAMBOOZLED (10.23860/jmle-2021-13-1-5): resumo só de desenho e desenvolvimento.\n- Musi et al. 2023 (10.1177/20563051221150407): chatbots, não jogos.\n- Modirrousta-Galian & Higham 2023 (10.1037/xge0001395): reanálise de dados.\n- Escape rooms de bibliotecas (Wedlake 2024; Cho 2023; EBLIP 2025): pesquisa pós-jogo ou estudo misto, sem pré e pós nem grupo de controle; o EBLIP é um evidence summary, não estudo primário.\n- Pimmer et al. (IADIS): trabalho de anais.\n- Cunha et al. (J. Interactive Systems): publicado em 2026.\n- Mateus et al., Bad News no Peru: 2026.\n- Jogos sobre COVID ou vacinas (Go Viral!, Bad Vaxx, COVID-19 Fake News game, Super Gotinha): excluídos pelo tema.\n- Estudos de extremismo (Saleh et al.): fora do tema de desinformação.\n\nPONTOS DE ATENÇÃO NA LISTA:\n- Tipo de estudo: Buchner 2023 e Buchner 2024 são estudos-piloto pré e pós sem grupo de controle, e Fernandes 2025 (N=55) tem pré e pós inferido do teste t pareado. Se o pesquisador exigir grupo de controle, esses três saem.\n- Duplicidade: Buchner & Höfler 2024, Buchner 2024 (TKL) e Buchner 2023 (MedienPädagogik) avaliam o mesmo jogo (Escape Fake), mas com amostras diferentes (45, 28 e 27), então os contei como artigos distintos. Se preferir, conte-os como um só.\n- Anos: Axelsson 2024 tem online em 2024 e fascículo em 2025; Roozenbeek & van der Linden (JRR) tem online em 2018 e fascículo em 2019 (vol. 22). Registrei 2024 e 2018, e ambos os anos de cada artigo estão dentro de 2018–2025.\n- Graham 2023: o Europe PMC lista o tipo como 'research-article; News'. Os dados são próprios (quatro replicações), mas vale confirmar o tratamento editorial.\n- DOI 10.37016//mr-2020-008 tem barra dupla, que é a forma registrada no Crossref e exibida na página do periódico.\n- Hu 2023, Reinhardt 2025 e Nygren & Efimova 2025 têm um braço que não é jogo (gráfico, folheto, oficina). Mantive-os porque o jogo é uma das intervenções avaliadas.\n- Para chegar a 25, as melhores opções são Barzilai & Stadtler 2025 (se o resumo for conferido no site da editora) e Seabrooke 2025 (se aceitar a data online)."
}