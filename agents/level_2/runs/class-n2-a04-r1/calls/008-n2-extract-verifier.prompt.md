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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre jogos educativos e jogos de inoculação (prebunking) contra desinformação, como o Bad News. Restrições: apenas intervenções em forma de jogo (digital ou de tabuleiro) avaliadas com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção; exclua intervenções que não são jogos (vídeos, textos ou infográficos isolados), reanálises de dados de outros estudos e estudos centrados em COVID-19, vacinas, eleições ou política partidária (por exemplo, o Go Viral!). Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

LISTA FINAL A VERIFICAR:
{
 "items": [
  {
   "doi": "10.1057/s41599-019-0279-9",
   "title": "Fake news game confers psychological resistance against online misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2019,
   "venue": "Palgrave Communications",
   "study_type": "Estudo empírico de avaliação em larga escala (pré e pós-jogo)",
   "method": "Avaliação pré e pós-intervenção do jogo online Bad News (inoculação)",
   "sample_size": "N = 15,000 participants",
   "main_finding": "A capacidade de identificar e resistir à desinformação melhora após jogar Bad News.",
   "abstract_quote": "We provide initial evidence that people's ability to spot and resist misinformation improves after gameplay"
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
   "study_type": "Experimento com grupo de controle gamificado",
   "method": "Delineamento misto 2 (tratamento vs. controle) × 2 (pré vs. pós); 18 manchetes falsas avaliadas antes e depois do jogo Bad News",
   "sample_size": "N = 196",
   "main_finding": "Jogar Bad News melhora a capacidade de identificar técnicas de desinformação em comparação com um controle gamificado e aumenta a confiança nos próprios julgamentos.",
   "abstract_quote": "We find that playing Bad News significantly improves people’s ability to spot misinformation techniques"
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
   "study_type": "Estudo empírico com avaliação pré e pós dentro do jogo",
   "method": "Bad News em quatro versões de idioma, com pesquisas intra-sujeitos antes e depois do jogo (desenho extraído do corpo da página; o resumo não o descreve)",
   "sample_size": "não informado no resumo",
   "main_finding": "O jogo Bad News confere resistência psicológica a estratégias comuns de desinformação em diferentes culturas.",
   "abstract_quote": "This study finds that the online “fake news” game, Bad News, can confer psychological resistance"
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
   "study_type": "Três experimentos longitudinais com grupo de controle",
   "method": "Participantes avaliados em intervalos regulares após jogar Bad News (controle: Tetris)",
   "sample_size": "NExp1 = 151, NExp2 = 194, NExp3 = 170",
   "main_finding": "No Experimento 1, o efeito de inoculação do Bad News permaneceu estável por pelo menos 3 meses.",
   "abstract_quote": "the inoculation effect remains stable for at least 3 months"
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
   "venue": "Educational and Psychological Measurement",
   "study_type": "Dois estudos online experimentais, com dados novos",
   "method": "Delineamento de três grupos de Solomon com o jogo Bad News, para separar efeitos de item e de teste",
   "sample_size": "total N = 2,159",
   "main_finding": "As intervenções de inoculação melhoram a capacidade de identificar técnicas de desinformação, com influência de efeitos de item e não de efeitos de teste.",
   "abstract_quote": "We show that inoculation interventions are effective at improving people's ability to spot misinformation techniques"
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
   "study_type": "Dois experimentos",
   "method": "Jogo Bad News de 15 minutos; resistência a desinformação real, amostra de conveniência recrutada na plataforma do jogo",
   "sample_size": "total n = 2188",
   "main_finding": "Um jogo de 15 minutos confere resistência psicológica a desinformação real que usa as técnicas de manipulação inoculadas.",
   "abstract_quote": "playing a 15 min game confers psychological resistance against real-world misinformation"
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
   "study_type": "Ensaio controlado randomizado",
   "method": "Três grupos (inoculação por jogo, por gráfico e controle), com seguimento de 2 semanas",
   "sample_size": "180 Chinese participants",
   "main_finding": "A inoculação por jogo foi mais eficaz que a inoculação por gráfico na credibilidade percebida da desinformação.",
   "abstract_quote": "Game-based inoculation was more effective than graphic-based inoculation in terms of misinformation perceived credibility"
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
   "study_type": "Ensaio controlado randomizado (campo, norte da Índia)",
   "method": "Intervenção em jogo baseada em inoculação; medidas de confiabilidade percebida, confiança e disposição a compartilhar",
   "sample_size": "n = 757",
   "main_finding": "Resultado nulo: a intervenção não teve impacto significativo na confiabilidade percebida, na confiança nem na disposição a compartilhar.",
   "abstract_quote": "We found no significant impact of the intervention on the perceived reliability of messages containing misinformation"
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
   "study_type": "Dois experimentos de laboratório pré-registrados e quatro pesquisas quase-experimentais dentro do jogo",
   "method": "Exercícios de feedback implementados nos jogos Harmony Square e Bad News, comparados a jogar sem o exercício",
   "sample_size": "N1 = 191, N2 = 321; N3 = 559 (Harmony Square); N4 = 2,558, N5 = 419, N6 = 882 (Bad News)",
   "main_finding": "Exercícios de feedback aumentam significativamente a discriminação entre desinformação e notícias reais nos jogos de inoculação.",
   "abstract_quote": "this significantly boosts discernment compared with playing the game without a feedback exercise"
  },
  {
   "doi": "10.1038/s41598-023-43885-2",
   "title": "How to \"inoculate\" against multimodal misinformation: A conceptual replication of Roozenbeek and van der Linden (2020)",
   "authors": [
    "Julian Neylan",
    "Mikey Biddlestone",
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2023,
   "venue": "Scientific Reports",
   "study_type": "Replicação conceitual com dados novos (jogo versus grupo de controle)",
   "method": "Jogo Cat Park sobre desinformação multimodal, com medidas pré e pós",
   "sample_size": "N = 380",
   "main_finding": "Quem joga Cat Park acha a desinformação menos confiável depois do jogo e fica menos disposto a compartilhá-la, mas não fica mais confiante em identificá-la.",
   "abstract_quote": "people who play Cat Park find misinformation significantly less reliable post-gameplay"
  },
  {
   "doi": "10.5334/joc.324",
   "title": "Mixed News about the Bad News Game",
   "authors": [
    "Megan E. Graham",
    "Brittany Skov",
    "Zoë Gilson",
    "Calvin Heise",
    "Kaitlyn M. Fallow",
    "Eric Y. Mah",
    "D. Stephen Lindsay"
   ],
   "year": 2023,
   "venue": "Journal of Cognition",
   "study_type": "Quatro replicações estendidas (dados próprios)",
   "method": "Bad News versus Tetris; ANOVA mista 2 (BNG vs. Tetris) × 2 (pré vs. pós) × 2 (tuíte verdadeiro vs. falso)",
   "sample_size": "não informado no resumo",
   "main_finding": "As quatro replicações reproduziram a redução da crença em tuítes falsos, mas o jogo também reduziu a crença em tuítes verdadeiros e não melhorou a discriminação.",
   "abstract_quote": "Despite many departures from the Basol et al. method, all four teams replicated their key finding: Playing the BNG reduced belief in false Tweets."
  },
  {
   "doi": "10.1037/xap0000458",
   "title": "Effects of inductive learning and gamification on news veracity discernment",
   "authors": [
    "Ariana Modirrousta-Galian",
    "Philip A. Higham",
    "Tina Seabrooke"
   ],
   "year": 2023,
   "venue": "Journal of Experimental Psychology: Applied",
   "study_type": "Experimento pré-registrado com alocação aleatória",
   "method": "Quatro condições: treino de aprendizado indutivo gamificado, não gamificado, controle sem tratamento e Bad News",
   "sample_size": "N = 282 Prolific users",
   "main_finding": "Não houve diferenças significativas entre as condições, com evidência bayesiana muito forte para a hipótese nula.",
   "abstract_quote": "there were no significant differences between conditions"
  },
  {
   "doi": "10.5209/esmp.88599",
   "title": "Winning the game against fake news? Using games to inoculate adolescents and young adults in Singapore against fake news",
   "authors": [
    "Edson Tandoc",
    "Seth Seet"
   ],
   "year": 2023,
   "venue": "Estudios sobre el Mensaje Periodístico",
   "study_type": "Estudo com jogadores versus não jogadores, replicado em duas amostras",
   "method": "Jogo de computador sobre fake news desenvolvido em Singapura, baseado na teoria da inoculação",
   "sample_size": "college (n = 84) and junior high and secondary school (n = 30)",
   "main_finding": "Quem jogou detectou mais fake news do que quem não jogou, e melhorou as atitudes autorrelatadas em relação a fake news.",
   "abstract_quote": "We also found that those who played the game scored higher in detecting fake news"
  },
  {
   "doi": "10.1007/s10758-024-09749-y",
   "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2024,
   "venue": "Technology, Knowledge and Learning",
   "study_type": "Estudo de campo",
   "method": "Desenho de pré-teste e pós-teste com o escape game de realidade aumentada Escape Fake",
   "sample_size": "A total of 28 students (14 girls, mean age = 14.71 years) participated.",
   "main_finding": "O jogo abordou quatro objetivos de aprendizagem relevantes para detectar fake news, com tamanhos de efeito educacionalmente desejáveis.",
   "abstract_quote": "The results show that Escape Fake can address four learning objectives"
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
   "study_type": "Estudo pré e pós-teste, sem grupo de comparação",
   "method": "Desenho de pré e pós-teste com o escape game de realidade aumentada Escape Fake",
   "sample_size": "45 pre-service teachers",
   "main_finding": "Após o jogo, os professores em formação tiveram mais conhecimento, atitude mais crítica e mais confiança, mas a capacidade de discernir informação real de falsa não melhorou.",
   "abstract_quote": "However, playing the game did not promote the ability to discern real from false information."
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik",
   "study_type": "Estudo piloto com desenho de pré e pós-teste",
   "method": "Vortest-Nachtest-Design com o escape game de realidade aumentada Escape Fake",
   "sample_size": "27 Schüler:innen",
   "main_finding": "O jogo Escape Fake transmite conhecimento sobre fake news, melhora a capacidade de reconhecer a confiabilidade da informação, favorece uma atitude mais crítica e aumenta a confiança.",
   "abstract_quote": "Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln,"
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
   "venue": "International Journal of Interactive Mobile Technologies",
   "study_type": "Estudo de campo online randomizado",
   "method": "Testes quantitativos de pré e pós-intervenção com o serious game 'How to Spot Fake News' (teste CRAAP)",
   "sample_size": "351 participants",
   "main_finding": "O serious game melhora o conhecimento de letramento informacional necessário para avaliar fontes de informação online.",
   "abstract_quote": "can improve the knowledge of information literacy"
  },
  {
   "doi": "10.1371/journal.pone.0326928",
   "title": "Investigating the long-term impact of misinformation interventions in upper secondary education",
   "authors": [
    "Thomas Nygren",
    "Evgenia Efimova"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "study_type": "Experimento em sala de aula com seguimento de longo prazo",
   "method": "Três abordagens comparadas: jogo de prebunking Bad News, oficina de checagem News Evaluator e lições disciplinares",
   "sample_size": "Using an experimental design with 459 students in authentic classroom settings",
   "main_finding": "Nem o jogo Bad News nem a oficina News Evaluator melhoraram de forma significativa a capacidade dos alunos de avaliar notícias confiáveis e enganosas.",
   "abstract_quote": "Neither the Bad News game nor the News Evaluator workshop significantly improved students' ability"
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
   "venue": "Behavioural Public Policy",
   "study_type": "Experimento controlado randomizado pré-registrado",
   "method": "Delineamento misto 2 × 2 (pré–pós) com o jogo de inoculação Radicalise contra técnicas de recrutamento extremista",
   "sample_size": "n = 291",
   "main_finding": "Jogar Radicalise melhora a capacidade e a confiança dos participantes em identificar mensagens manipulativas e características associadas à vulnerabilidade.",
   "abstract_quote": "We find that playing Radicalise significantly improves participants' ability and confidence in spotting"
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
   "study_type": "Experimento com alunos do ensino médio",
   "method": "Jogo de cartas Follow me, para desenvolver pensamento crítico contra fake news",
   "sample_size": "130 secondary school students from six different schools",
   "main_finding": "Não houve melhora estatisticamente significativa global na capacidade dos alunos de reconhecer fake news, embora tenham mostrado ceticismo saudável.",
   "abstract_quote": "although there was no global statistically significant improvement measured in students' ability to recognize fake news"
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
   "venue": "Education Sciences",
   "study_type": "Estudo de campo online randomizado, mais discussão em uma turma de mídia",
   "method": "Serious game web para verificação de notícias; o artigo também apresenta o design do jogo",
   "sample_size": "randomized online field study (n = 111); media class (n = 35)",
   "main_finding": "O jogo aumenta a conscientização e ensina sobre ferramentas de autenticação de notícias.",
   "abstract_quote": "Specifically, it is validated that the game can raise awareness"
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
   "venue": "Applied Cognitive Psychology",
   "study_type": "Replicação com dados próprios, desenho intra-sujeitos",
   "method": "Bad News Game com amostra indiana, medidas antes e depois do jogo",
   "sample_size": "an Indian sample (n = 1002)",
   "main_finding": "Houve melhora significativa na identificação de desinformação produzida com Conspiração e Personificação e, em menor grau, Descrédito, além de maior discernimento de notícias verdadeiras.",
   "abstract_quote": "We provide evidence of significant improvement in the ability of participants to identify the misinformation produced using Conspiracy, Impersonation, and to a lesser extent, the Discrediting technique"
  },
  {
   "doi": "10.11645/18.2.13",
   "title": "Chaos creator: Misinformation inoculation in information literacy instruction",
   "authors": [
    "Mandi Goodsett"
   ],
   "year": 2024,
   "venue": "Journal of Information Literacy",
   "study_type": "Estudo quase-experimental com estudantes de graduação",
   "method": "Sessão de letramento informacional com o jogo competitivo Chaos Creator (baseado em Bad News), comparada ao teste CRAP",
   "sample_size": "não informado no resumo",
   "main_finding": "As técnicas de inoculação ajudaram os alunos a identificar desinformação melhor que o teste CRAP, mas podem torná-los excessivamente céticos com mensagens confiáveis.",
   "abstract_quote": "Results of the study show that misinformation inoculation techniques are more effective"
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
   "study_type": "Avaliação pré e pós-intervenção em sala de aula",
   "method": "Bad News jogado individualmente, em duplas ou com a turma toda",
   "sample_size": "516 upper-secondary Swedish students",
   "main_finding": "Os alunos melhoraram a capacidade de discernir técnicas de manipulação em postagens de redes sociais.",
   "abstract_quote": "Results show that students improved their ability to discern manipulation techniques in social media posts."
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
   "study_type": "Dois estudos experimentais",
   "method": "Jogo digital que modela estratégias de avaliação e compartilhamento responsável, comparado a um jogo de linguagem de controle",
   "sample_size": "N = 84 and N = 131",
   "main_finding": "O jogo gerou melhor discernimento de acurácia e de compartilhamento e mais conhecimento metaestratégico, sem mudar as atitudes autorrelatadas.",
   "abstract_quote": "playing the misinformation game resulted in better accuracy discernment"
  }
 ],
 "search_notes": "Os candidatos aprovados eram 26 e o pedido era de 25. Deixei de fora um: Saleh et al. 2023 (10.56296/aip00005), experimento de campo com o jogo Radicalise no Iraque, publicado em advances.in/psychology. O motivo é que a revisão por pares desse periódico não foi confirmada, e o pedido exige artigos revisados por pares. Se o pesquisador aceitar o periódico, esse é o item a recolocar. Todos os outros 25 foram mantidos.\n\nVerificação dos resumos:\n- Abri as páginas dos periódicos ou o Europe PMC para: Basol 2020, HKS Misinformation Review, Maertens 2021, Solomon, Royal Society, Hu, Harjani, Leder, Neylan, Graham, Modirrousta-Galian, Tandoc & Seet, Buchner 2024, Buchner & Höfler, Buchner (MedienPädagogik), Sureephong, Nygren & Efimova, Pomichal & Trnka, Goodsett, Axelsson e Barzilai.\n- As páginas de Roozenbeek 2019, Saleh 2021, Katsaounidou e Iyengar não abriram (o Europe PMC não tinha o registro de Roozenbeek 2019 nem de Saleh 2021). Para elas, usei o campo de resumo do Crossref.\n- A ferramenta de leitura só devolve trechos literais curtos (até cerca de 125 caracteres). Por isso, em vários itens a abstract_quote é um trecho contínuo e literal, mas mais curto que a frase completa do resumo, por exemplo em Roozenbeek 2019, Basol, HKS, Nygren, Saleh 2021, Buchner (MedienPädagogik) e Axelsson.\n\nPontos de atenção:\n1. Graham et al. (10.5334/joc.324): a frase da abstract_quote vem da leitura da tentativa anterior. Na verificação atual, só confirmei literalmente o trecho até \"key finding:\". O restante (\"Playing the BNG reduced belief in false Tweets.\") é coerente com o resumo lido, mas não foi reconferido letra por letra.\n2. Graham et al.: os números N = 422 e 353 participantes estão na seção de métodos, não no resumo. Por isso, sample_size é \"não informado no resumo\".\n3. HKS Misinformation Review: o resumo não traz amostra. O n = 5,061 está só no \"Essay Summary\", e não o usei. O DOI está como registrado no Crossref, com barra dupla.\n4. Solomon Revisited: o resumo também diz que os efeitos de item influenciam a inoculação, e os efeitos de teste não. A abstract_quote é a frase sobre eficácia.\n5. Maertens et al.: no Experimento 1 o efeito ficou estável por 3 meses. O decaimento no Experimento 2 vem da leitura anterior e não o reconferi, por isso não o incluí.\n6. Escopo:\n   - Leder et al. inclui Harmony Square, cujo enredo é político. O resumo não menciona eleição nem partido, e o foco é o feedback. Mantive o artigo, mas o pesquisador pode excluí-lo se for estrito.\n   - O resumo de Pomichal & Trnka cita a COVID-19 só como contexto, e o estudo não é centrado nela.\n   - Nygren & Efimova avaliam três intervenções, e Bad News é uma delas.\n   - Hu et al. comparam jogo e gráfico, e o jogo é uma das intervenções avaliadas.\n   - Saleh 2021 trata de extremismo violento, que não é política partidária.\n7. Katsaounidou et al. também apresentam o design do jogo, mas incluem avaliação com participantes.\n8. Resultados nulos ou negativos foram mantidos de propósito: Harjani, Modirrousta-Galian, Buchner & Höfler (discernimento), Pomichal & Trnka e Nygren & Efimova.\n9. Axelsson et al.: a edição do periódico é de 2025 (VU), mas o artigo saiu online em 2024 (Crossref). Usei 2024. Buchner 2024 e Iyengar têm datas online e de edição diferentes, ambas dentro de 2018–2025.\n10. Tandoc & Seet: a página mostrou só o resumo em espanhol. O trecho em inglês e a amostra vêm do campo de resumo do Crossref, que traz o resumo em inglês.\n11. Os resumos de Buchner (MedienPädagogik) e Sureephong foram lidos na página do periódico. O alemão é literal. Em Sureephong, o trecho veio com espaços corrigidos pelo leitor, porque a página original tem espaços ausentes.\n12. Não fiz buscas novas fora da lista aprovada."
}