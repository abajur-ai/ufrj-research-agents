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
   "venue": "Palgrave Communications (hoje Humanities and Social Sciences Communications), vol. 5",
   "checked_url": "https://www.nature.com/articles/s41599-019-0279-9",
   "criteria_met": [
    "Tema/jogo: Bad News (jogo online de desinformação, inoculação)",
    "Tipo de estudo e método: estudo empírico, avaliação em larga escala com desenho pré e pós-jogo",
    "Amostra: N = 15,000 participants",
    "Achado principal: a capacidade de identificar e resistir à desinformação melhora após jogar Bad News",
    "Trecho: \"We provide initial evidence that people's ability to spot and resist misinformation improves after gameplay, irrespective of education, age, political ideology, and cognitive style.\"",
    "Periódico revisado por pares, 2019, sem tema excluído"
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
   "checked_url": "https://www.journalofcognition.org/articles/10.5334/joc.91",
   "criteria_met": [
    "Tema/jogo: Bad News",
    "Tipo de estudo e método: replicação com dados novos, experimento misto 2 (tratamento vs. controle) × 2 (pré vs. pós) com grupo de controle gamificado",
    "Amostra: N = 196",
    "Achado principal: jogar Bad News melhora a capacidade de identificar técnicas de desinformação e aumenta a confiança nos próprios julgamentos, em comparação com o controle gamificado",
    "Trecho: \"We find that playing Bad News significantly improves people’s ability to spot misinformation techniques compared to a gamified control group, and crucially, also increases people’s level of confidence in their own judgments.\"",
    "Ano 2020 (Crossref issued 2020-01-10)"
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
   "checked_url": "https://misinforeview.hks.harvard.edu/article/global-vaccination-badnews/",
   "criteria_met": [
    "Tema/jogo: Bad News em quatro idiomas",
    "Tipo de estudo e método: estudo empírico com pesquisas pré e pós dentro do jogo (intra-sujeitos), conforme o corpo do artigo; o resumo não descreve o desenho",
    "Amostra: não informado no resumo (o corpo do artigo cita n = 5,061)",
    "Achado principal: Bad News confere resistência psicológica a estratégias de desinformação em diferentes culturas",
    "Trecho: \"This study finds that the online \"fake news\" game, Bad News, can confer psychological resistance against common online misinformation strategies across different cultures.\"",
    "DOI registrado no Crossref com barra dupla (10.37016//mr-2020-008). A forma com barra simples dá 404 em doi.org, e a com barra dupla redireciona para o artigo."
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
   "venue": "Journal of Experimental Psychology: Applied, 27(1)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Long-term%20effectiveness%20of%20inoculation%20against%20misinformation%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Bad News versus Tetris (controle gamificado)",
    "Tipo de estudo e método: 3 experimentos longitudinais (2 pré-registrados) com grupo de controle",
    "Amostra: NExp1 = 151, NExp2 = 194, NExp3 = 170",
    "Achado principal: o efeito de inoculação do Bad News permanece estável por pelo menos 3 meses no Experimento 1, mas decai no Experimento 2, sem teste repetido",
    "Trecho: \"In Experiment 1, we assessed participants at regular intervals to explore the longevity of this effect and found that the inoculation effect remains stable for at least 3 months.\"",
    "Ano 2021 (Crossref e Europe PMC)"
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
   "year": 2021,
   "venue": "Educational and Psychological Measurement, 81(2)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Disentangling%20item%20and%20testing%20effects%20in%20inoculation%20research%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Bad News",
    "Tipo de estudo e método: dois estudos online com delineamento de três grupos de Solomon, com dados novos",
    "Amostra: total N = 2,159",
    "Achado principal: as intervenções de inoculação melhoram a capacidade de identificar técnicas de desinformação, sofrem alguma influência dos itens e não do efeito do pré-teste, e Bad News não torna as pessoas mais céticas com notícias reais",
    "Trecho: \"We show that inoculation interventions are effective at improving people's ability to spot misinformation techniques and that the Bad News game does not make people more skeptical of real news.\"",
    "Online em 2020 e edição impressa em abril de 2021; ambos dentro do período"
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
   "venue": "Royal Society Open Science, 9(5)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Technique-based%20inoculation%20against%20real-world%20misinformation%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Bad News, jogo de 15 minutos",
    "Tipo de estudo e método: dois experimentos",
    "Amostra: total n = 2188; convenience sample recruited via the Bad News online game platform",
    "Achado principal: jogar 15 min confere resistência a desinformação real que usa as técnicas inoculadas, com proteção cruzada menor",
    "Trecho: \"We find that playing a 15 min game confers psychological resistance against real-world misinformation that makes use of manipulation techniques against which people were inoculated\"",
    "Há uma errata (10.1098/rsos.231235), que não foi usada"
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
   "venue": "Cognitive Research: Principles and Implications, 8(1)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Game-based%20inoculation%20versus%20graphic-based%20inoculation%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: jogo interativo em que o jogador é um disseminador de desinformação",
    "Tipo de estudo e método: ensaio controlado randomizado com 3 grupos (jogo, gráfico, controle) e seguimento de 2 semanas",
    "Amostra: 180 Chinese participants",
    "Achado principal: o jogo reduziu a credibilidade percebida e a intenção de compartilhar desinformação, e foi mais eficaz que o gráfico na credibilidade percebida",
    "Trecho: \"Game-based inoculation was more effective than graphic-based inoculation in terms of misinformation perceived credibility, and the intervention effects were stable after 2 weeks.\"",
    "Sem tema excluído"
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
   "venue": "Journal of Trial and Error, 3(1)",
   "checked_url": "https://api.crossref.org/works/10.36850/e12",
   "criteria_met": [
    "Tema/jogo: intervenção em jogo baseada em inoculação, norte da Índia",
    "Tipo de estudo e método: ensaio controlado randomizado de campo; a randomização vem do título e o resumo não a descreve",
    "Amostra: (n = 757)",
    "Achado principal: resultado nulo, o estudo não replicou os efeitos de estudos ocidentais",
    "Trecho: \"We found no significant impact of the intervention on the perceived reliability of messages containing misinformation, confidence judgments, and willingness to share information with others.\"",
    "Resumo lido no registro Crossref; o site do periódico deu 403"
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
   "venue": "Journal of Experimental Psychology: General, 153(8)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Feedback%20exercises%20boost%20discernment%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Bad News e Harmony Square com exercícios de feedback",
    "Tipo de estudo e método: 2 experimentos de laboratório pré-registrados e 4 pesquisas quase-experimentais dentro do jogo; dados novos",
    "Amostra: N1 = 191, N2 = 321; N3 = 559 (Harmony Square); N4 = 2,558, N5 = 419, N6 = 882 (Bad News)",
    "Achado principal: exercícios de feedback aumentam a discriminação entre desinformação e notícias reais em jogos de inoculação",
    "Trecho: \"In Experiments 3-6, we implemented two different types of feedback exercises in the Harmony Square and Bad News games and find that this significantly boosts discernment compared with playing the game without a feedback exercise, primarily by improving accuracy at detecting real news.\"",
    "Harmony Square tem enredo político, mas o foco do estudo é o efeito do feedback, e o resumo não cita eleição nem partido"
   ]
  },
  {
   "doi": "10.1038/s41598-023-43885-2",
   "title": "How to \"inoculate\" against multimodal misinformation: A conceptual replication of Roozenbeek and van der Linden (2020)",
   "authors": [
    "J. Neylan",
    "M. Biddlestone",
    "J. Roozenbeek",
    "S. van der Linden"
   ],
   "year": 2023,
   "venue": "Scientific Reports, 13(1)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41598-023-43885-2%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Cat Park, novo jogo sobre desinformação multimodal",
    "Tipo de estudo e método: replicação conceitual com dados novos, jogo versus grupo de controle, medidas pré e pós",
    "Amostra: (N = 380)",
    "Achado principal: quem joga Cat Park acha a desinformação menos confiável e fica menos disposto a compartilhá-la, mas não fica mais confiante em identificá-la",
    "Trecho: \"Like the original study, we find that people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001) compared to a control group\"",
    "Autores conferidos só com iniciais no Europe PMC"
   ]
  },
  {
   "doi": "10.5334/joc.324",
   "title": "Mixed News about the Bad News Game",
   "authors": [
    "Megan E. Graham",
    "Bryan Skov",
    "Zoe Gilson",
    "Cassandra Heise",
    "Kelsey M. Fallow",
    "Eva Y. Mah",
    "D. Stephen Lindsay"
   ],
   "year": 2023,
   "venue": "Journal of Cognition, 6(1)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.5334/joc.324%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: Bad News",
    "Tipo de estudo e método: quatro replicações estendidas, cada uma com dados próprios, jogo versus jogo não relacionado, avaliação pré e pós de tuítes",
    "Amostra: não informado no resumo",
    "Achado principal: as quatro replicações reproduziram a redução da crença em tuítes falsos, mas o jogo também reduziu a crença em tuítes verdadeiros e não melhorou a discriminação",
    "Trecho: \"Despite many departures from the Basol et al. method, all four teams replicated their key finding: Playing the BNG reduced belief in false Tweets.\"",
    "Nomes conferidos só com iniciais no Europe PMC; os prenomes são do formato de citação"
   ]
  },
  {
   "doi": "10.1037/xap0000458",
   "title": "Effects of inductive learning and gamification on news veracity discernment",
   "authors": [
    "Alexander Modirrousta-Galian",
    "Philip A. Higham",
    "Tina Seabrooke"
   ],
   "year": 2023,
   "venue": "Journal of Experimental Psychology: Applied, 29(3)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1037/xap0000458%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: treino gamificado de aprendizado indutivo e Bad News, contra desinformação",
    "Tipo de estudo e método: experimento pré-registrado com alocação aleatória a 4 condições (gamificada, não gamificada, controle sem tratamento, Bad News)",
    "Amostra: N = 282 Prolific users",
    "Achado principal: sem diferenças significativas entre as condições, com evidência muito forte para a hipótese nula",
    "Trecho: \"The analyses indicated that there were no significant differences between conditions and the Bayes factor indicated very strong evidence for the null.\"",
    "Sem tema excluído"
   ]
  },
  {
   "doi": "10.5209/esmp.88599",
   "title": "Winning the game against fake news? Using games to inoculate adolescents and young adults in Singapore against fake news",
   "authors": [
    "Edson Tandoc",
    "Seth Seet"
   ],
   "year": 2023,
   "venue": "Estudios sobre el Mensaje Periodístico, 29(4)",
   "checked_url": "https://api.crossref.org/works/10.5209/esmp.88599",
   "criteria_met": [
    "Tema/jogo: jogo de computador sobre fake news desenvolvido em Singapura, baseado em inoculação",
    "Tipo de estudo e método: estudo com jogadores versus não jogadores, replicado em duas amostras",
    "Amostra: college (n = 84) and junior high and secondary school (n = 30)",
    "Achado principal: quem jogou melhorou as atitudes em relação a fake news e detectou mais fake news do que quem não jogou",
    "Trecho: \"We also found that those who played the game scored higher in detecting fake news than those who did not play the game –consistent with the predicted effects of message inoculation.\"",
    "Resumo lido no registro Crossref"
   ]
  },
  {
   "doi": "10.1007/s10758-024-09749-y",
   "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2024,
   "venue": "Technology, Knowledge and Learning, 30(1) (edição de março de 2025)",
   "checked_url": "https://api.crossref.org/works/10.1007/s10758-024-09749-y",
   "criteria_met": [
    "Tema/jogo: Escape Fake, escape game de realidade aumentada para educação midiática",
    "Tipo de estudo e método: estudo de campo com desenho de pré-teste e pós-teste",
    "Amostra: A total of 28 students (14 girls, mean age = 14.71 years) participated",
    "Achado principal: o jogo produziu ganhos em conhecimento, discernimento, atitude crítica e confiança, com tamanhos de efeito desejáveis",
    "Trecho: \"The results show that Escape Fake can address four learning objectives relevant in fake news detection with educationally desired effect sizes\"",
    "Online em 2024 e edição impressa em 2025; ambos dentro do período"
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
   "venue": "Contemporary Educational Technology, 16(2)",
   "checked_url": "https://api.crossref.org/works/10.30935/cedtech/14335",
   "criteria_met": [
    "Tema/jogo: Escape Fake (escape game de realidade aumentada)",
    "Tipo de estudo e método: desenho de pré e pós-teste, sem grupo de comparação",
    "Amostra: a pre-/post-test design was conducted with 45 pre-service teachers",
    "Achado principal: após o jogo houve mais conhecimento, atitude crítica e confiança, mas a capacidade de discernir informação real de falsa não melhorou",
    "Trecho: \"However, playing the game did not promote the ability to discern real from false information.\"",
    "Resumo lido no registro Crossref"
   ]
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik, vol. 51",
   "checked_url": "https://api.crossref.org/works/10.21240/mpaed/51/2023.01.12.x",
   "criteria_met": [
    "Tema/jogo: Escape Fake (escape game de realidade aumentada)",
    "Tipo de estudo e método: estudo piloto com desenho de pré e pós-teste",
    "Amostra: Vortest-Nachtest Design mit 27 Schüler:innen durchgeführt",
    "Achado principal: o jogo transmite conhecimento sobre fake news, melhora o reconhecimento da confiabilidade da informação e a atitude crítica e aumenta a confiança",
    "Trecho: \"Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln, die Fähigkeit fördern, die Zuverlässigkeit von Informationen zu erkennen\"",
    "Resumo em alemão, lido no registro Crossref"
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
   "venue": "International Journal of Interactive Mobile Technologies, 17(15)",
   "checked_url": "https://api.crossref.org/works/10.3991/ijim.v17i15.40865",
   "criteria_met": [
    "Tema/jogo: serious game 'How to Spot Fake News' (teste CRAAP)",
    "Tipo de estudo e método: estudo de campo online randomizado com pré e pós-testes",
    "Amostra: pre-posttests involving 351 participants",
    "Achado principal: o jogo melhora o conhecimento de letramento informacional necessário para avaliar fontes",
    "Trecho: \"The results revealed that using aserious game of \"How to Spot Fake News\" can improve the knowledge of information literacyneeded to evaluate online sources of information.\"",
    "Trecho copiado com os espaços ausentes do registro original"
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
   "venue": "PLoS ONE, 20(7)",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1371/journal.pone.0326928%22&resultType=core&format=json",
   "criteria_met": [
    "Tema/jogo: prebunking com o jogo Bad News, comparado a oficina de checagem e a intervenções disciplinares",
    "Tipo de estudo e método: desenho experimental em sala de aula com seguimento de longo prazo",
    "Amostra: Using an experimental design with 459 students in authentic classroom settings",
    "Achado principal: nem Bad News nem a oficina News Evaluator melhoraram de forma significativa a avaliação de notícias confiáveis e enganosas",
    "Trecho: \"Neither the Bad News game nor the News Evaluator workshop significantly improved students' ability to evaluate credible and misleading news.\"",
    "Ressalva: Bad News é uma de três intervenções avaliadas"
   ]
  },
  {
   "doi": "10.1017/bpp.2020.60",
   "title": "Active inoculation boosts attitudinal resistance against extremist persuasion techniques: a novel approach towards the prevention of violent extremism",
   "authors": [
    "Nabil F. Saleh",
    "Jon Roozenbeek",
    "Fadi A. Makki",
    "William P. McClanahan",
    "Sander van der Linden"
   ],
   "year": 2021,
   "venue": "Behavioural Public Policy (online 2021; vol. 8, n. 3)",
   "checked_url": "https://api.crossref.org/works/10.1017/bpp.2020.60",
   "criteria_met": [
    "Tema/jogo: Radicalise, jogo online de inoculação contra técnicas de recrutamento extremista",
    "Tipo de estudo e método: experimento controlado randomizado misto 2 × 2 (pré–pós), pré-registrado",
    "Amostra: randomized controlled experiment (n = 291)",
    "Achado principal: jogar Radicalise melhora a capacidade e a confiança em identificar mensagens manipulativas e características de vulnerabilidade",
    "Trecho: \"We find that playing Radicalise significantly improves participants’ ability and confidence in spotting manipulative messages and the characteristics associated with vulnerability.\"",
    "Tema extremismo, permitido pelo plano"
   ]
  },
  {
   "doi": "10.56296/aip00005",
   "title": "Inoculating against extremist persuasion techniques – Results from a randomised controlled trial in post-conflict areas in Iraq",
   "authors": [
    "Nabil Saleh",
    "Fadi Makki",
    "Sander Van der Linden",
    "Jon Roozenbeek"
   ],
   "year": 2023,
   "venue": "advances.in/psychology",
   "checked_url": "https://api.crossref.org/works/10.56296/aip00005",
   "criteria_met": [
    "Tema/jogo: Radicalise, jogo de inoculação",
    "Tipo de estudo e método: experimento de campo randomizado controlado (pré-pós / tratamento-controle), replicação conceitual",
    "Amostra: We conducted a field experiment (N = 191)",
    "Achado principal: o jogo melhorou a capacidade de identificar mensagens manipulativas, mas não a de identificar indivíduos vulneráveis",
    "Trecho: \"We find that playing the game significantly improved participants’ ability (p = 0.034, d = 0.31) in spotting manipulative messaging\"",
    "Revisão por pares do periódico advances.in/psychology não conferida no site"
   ]
  },
  {
   "doi": "10.34135/mlar-23-01-04",
   "title": "With Games Against Fake News – Developing Critical Thinking with the Help of the Card Game Follow Me",
   "authors": [
    "Vajk Pomichal",
    "Andrej Trnka"
   ],
   "year": 2023,
   "venue": "Media Literacy and Academic Research",
   "checked_url": "https://api.crossref.org/works/10.34135/mlar-23-01-04",
   "criteria_met": [
    "Tema/jogo: jogo de cartas Follow me contra fake news",
    "Tipo de estudo e método: experimento com alunos do ensino médio",
    "Amostra: an experiment on a sample of 130 secondary school students from six different schools",
    "Achado principal: não houve melhora global significativa na capacidade de reconhecer fake news",
    "Trecho: \"although there was no global statistically significant improvement measured in students' ability to recognize fake news\"",
    "Resumo lido no registro Crossref"
   ]
  },
  {
   "doi": "10.3390/educsci9020155",
   "title": "MAthE the Game: A Serious Game for Education and Training in News Verification",
   "authors": [
    "Anastasia Katsaounidou",
    "Lazaros Vrysis",
    "Rigas Kotsakis",
    "Charalampos Dimoulas",
    "Andreas Veglis"
   ],
   "year": 2019,
   "venue": "Education Sciences, 9(2)",
   "checked_url": "https://api.crossref.org/works/10.3390/educsci9020155",
   "criteria_met": [
    "Tema/jogo: serious game web para verificação de notícias",
    "Tipo de estudo e método: estudo de campo online randomizado, além de discussão em aula de mídia para feedback",
    "Amostra: randomized online field study (n = 111); media class (n = 35)",
    "Achado principal: o jogo aumenta a conscientização e ensina ferramentas de autenticação",
    "Trecho: \"Specifically, it is validated that the game can raise awareness, teach about authentication tools, and highlight the importance of patterns that include evidence regarding the authenticity of articles.\"",
    "Ressalva: o estudo também apresenta o design do jogo, mas inclui avaliação com participantes"
   ]
  },
  {
   "doi": "10.1002/acp.3995",
   "title": "Inoculation against conspiracy theories: A consumer side approach to India's fake news problem",
   "authors": [
    "Ananya Iyengar",
    "Poorvi Gupta",
    "Nidhi Priya"
   ],
   "year": 2023,
   "venue": "Applied Cognitive Psychology, 37(2) (online 2022)",
   "checked_url": "https://api.crossref.org/works/10.1002/acp.3995",
   "criteria_met": [
    "Tema/jogo: Bad News Game com amostra indiana",
    "Tipo de estudo e método: replicação com dados próprios, desenho intra-sujeitos pré e pós-jogo",
    "Amostra: an Indian sample (n = 1002)",
    "Achado principal: melhora significativa na identificação de desinformação por Conspiração, Personificação e, em menor grau, Descrédito, com maior discernimento de notícias verdadeiras",
    "Trecho: \"We provide evidence of significant improvement in the ability of participants to identify the misinformation produced using Conspiracy, Impersonation, and to a lesser extent, the Discrediting technique\"",
    "Online em setembro de 2022, edição de março de 2023; ambos dentro do período"
   ]
  },
  {
   "doi": "10.11645/18.2.13",
   "title": "Chaos creator",
   "authors": [
    "Mandi Goodsett"
   ],
   "year": 2024,
   "venue": "Journal of Information Literacy, 18(2)",
   "checked_url": "https://api.crossref.org/works/10.11645/18.2.13",
   "criteria_met": [
    "Tema/jogo: jogo competitivo Chaos Creator, baseado em Bad News, em aula de letramento informacional",
    "Tipo de estudo e método: estudo quase-experimental com estudantes de graduação",
    "Amostra: não informado no resumo",
    "Achado principal: as técnicas de inoculação foram mais eficazes que o teste CRAP, mas podem tornar os alunos excessivamente céticos com mensagens confiáveis",
    "Trecho: \"Results of the study show that misinformation inoculation techniques are more effective than the popular source evaluation tool, the CRAP test, in helping students identify misinformation.\"",
    "Resumo lido no registro Crossref"
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
   "venue": "Journal of Research on Technology in Education, 57(5) (edição de 2025)",
   "checked_url": "https://research.vu.nl/en/publications/bad-news-in-the-civics-classroom-how-serious-gameplay-fosters-tee/",
   "criteria_met": [
    "Tema/jogo: Bad News em sala de aula",
    "Tipo de estudo e método: avaliação pré e pós-intervenção em sala, jogo individual, em duplas ou com a turma toda",
    "Amostra: 516 upper-secondary Swedish students",
    "Achado principal: os alunos melhoraram a capacidade de discernir técnicas de manipulação em postagens",
    "Trecho: \"Results show that students improved their ability to discern manipulation techniques in social media posts.\"",
    "Metadados do DOI conferidos via doi.org e Crossref (online em abril de 2024, edição de 2025); resumo lido na página da Vrije Universiteit (research.vu.nl)"
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
   "venue": "Computers & Education, 202, 104832",
   "checked_url": "https://cris.iucc.ac.il/en/publications/misinformation-is-contagious-middle-school-students-learn-how-to-/",
   "criteria_met": [
    "Tema/jogo: jogo digital que modela estratégias de avaliação e compartilhamento responsável",
    "Tipo de estudo e método: dois estudos experimentais comparando o jogo com um jogo de linguagem de controle",
    "Amostra: In two studies with 7th and 8th grade students (N = 84 and N = 131)",
    "Achado principal: o jogo gerou melhor discernimento de acurácia, de compartilhamento e conhecimento metaestratégico, sem mudar as atitudes autorrelatadas",
    "Trecho: \"playing the misinformation game resulted in better accuracy discernment\"",
    "O trecho é um fragmento literal curto do resumo, lido na página cris.iucc.ac.il; o resumo completo não foi reproduzível pela ferramenta de leitura"
   ]
  }
 ],
 "notes": "Entreguei 26 candidatos que atendem aos critérios, acima dos 25 pedidos, dentro do limite de 1,5 vez. Os resumos foram lidos nas fontes indicadas em checked_url. As citações são trechos literais de resumos que a ferramenta de leitura devolveu em partes. Cada citação é um trecho contínuo ou trechos adjacentes juntados.\n\nPontos de atenção:\n- Roozenbeek et al. 2020 (HKS Misinformation Review): o DOI registrado tem barra dupla (10.37016//mr-2020-008), e é esse que redireciona ao artigo. A forma com barra simples dá 404. O resumo não informa amostra nem desenho. O desenho pré e pós dentro do jogo e n = 5,061 vêm do corpo do artigo.\n- Barzilai et al. 2023: o resumo completo não pôde ser reproduzido pela ferramenta de leitura. A citação é um fragmento literal curto e a amostra vem de trecho literal, mas o texto completo do resumo não foi conferido.\n- Harjani et al. 2023 e os dois estudos Buchner e Höfler: os resumos vêm do registro Crossref.\n- Hu 2023 e Neylan 2023 não têm o ano de edição conferido fora do Europe PMC e do Crossref.\n- Leder 2024 inclui Harmony Square, de enredo político, mas o estudo trata do efeito do feedback, e o resumo não cita eleição ou partido. Foi mantido.\n- Nygren & Efimova 2025 avalia Bad News como uma das três intervenções. O achado é nulo para o jogo.\n\nExcluí por critério:\n- Seabrooke et al. (10.3758/s13423-025-02827-x): publicado online em dez/2025, mas a edição oficial é vol. 33(1), jan/2026, fora do período 2018–2025.\n- Roozenbeek et al. 2020, Harmony Square (10.37016/mr-2020-47), e Traberg et al. 2024 (10.37016/mr-2020-141): centrados em desinformação política e ingroups políticos.\n- Half#Truths (10.62758/re.302): jogo aplicado à realidade política brasileira, com extrema-direita e governo Bolsonaro.\n- Spot the Troll Quiz (10.1093/pnasnexus/pgad094): é quiz e trata de eleição e política.\n- Modirrousta-Galian & Higham 2023 (10.1037/xge0001395): reanálise de dados.\n- Rędzio et al. 2023, Ma et al. 2023 e Basol et al. 2021 (Go Viral!): centrados em COVID ou vacinas.\n- Cook et al. 2022, Cranky Uncle (10.1080/13504622.2022.2085671): estudos de caso qualitativos, sem resumo no Crossref e sem desenho experimental ou pré-pós confirmado.\n- Real ou Fake (10.22409/contracampo.v42i3.58268): pesquisa-ação sem avaliação experimental.\n- JEDi (10.5753/rbie.2021.29.0.634): estudo de caso.\n- LAMBOOZLED (10.23860/jmle-2021-13-1-5): artigo de design e desenvolvimento.\n- Roozenbeek et al. 2025 (10.1098/rsos.251377) e Maertens et al. 2025 (10.1038/s41467-025-57205-x): intervenções em vídeo ou texto, ou mistas.\n- Latinos Unidos (10.1080/10810730.2024.2339238): estudo de aceitabilidade durante a pandemia de COVID-19.\n- Martini et al. 2025 (10.1038/s41598-025-16565-6): o resumo não confirma que a intervenção de inoculação seja um jogo.\n- Johnson & Madsen 2024: usa vídeos e não é um jogo.\n- Revisões e comentários (Barabas 2023, Golay 2020 e outros): fora do critério de estudo empírico.\n\nLimitações da busca:\n- O OpenAlex devolveu HTTP 429, então usei Crossref e Europe PMC. A busca em SciELO em português não foi feita como base própria; só rodei uma consulta em português no Crossref. Portanto, a cobertura em português pode estar incompleta.\n- A revisão por pares é inferida do tipo journal-article no Crossref. Não foi conferida no site de cada periódico, em especial advances.in/psychology e Media Literacy and Academic Research."
}