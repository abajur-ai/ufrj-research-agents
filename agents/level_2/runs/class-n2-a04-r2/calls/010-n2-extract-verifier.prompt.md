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
   "doi": "10.1080/13669877.2018.1443491",
   "title": "The fake news game: actively inoculating against the risk of misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2018,
   "venue": "Journal of Risk Research",
   "study_type": "Estudo de campo randomizado (teste-piloto)",
   "method": "Jogo em que os participantes criam uma notícia falsa, testado em uma escola de ensino médio pública",
   "sample_size": "N = 95",
   "main_finding": "Jogar o jogo reduziu, de forma preliminar, a confiabilidade percebida e a persuasão de artigos de fake news.",
   "abstract_quote": "To pilot test the efficacy of the game, we conducted a randomized field study (N = 95) in a public high school setting. Results provide some preliminary evidence that playing the fake news game reduced the perceived reliability and persuasiveness of fake news articles."
  },
  {
   "doi": "10.1057/s41599-019-0279-9",
   "title": "Fake news game confers psychological resistance against online misinformation",
   "authors": [
    "Jon Roozenbeek",
    "Sander van der Linden"
   ],
   "year": 2019,
   "venue": "Palgrave Communications",
   "study_type": "Avaliação empírica em larga escala, com desenho pré e pós-jogo",
   "method": "Jogo de navegador Bad News, avaliado antes e depois da partida",
   "sample_size": "N = 15,000",
   "main_finding": "A capacidade de identificar e resistir à desinformação melhorou depois do jogo, independentemente de escolaridade, idade, ideologia política e estilo cognitivo.",
   "abstract_quote": "We conducted a large-scale evaluation of the game with N = 15,000 participants in a pre-post gameplay design. We provide initial evidence that people's ability to spot and resist misinformation improves after gameplay, irrespective of education, age, political ideology, and cognitive style."
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
   "study_type": "Experimento randomizado (replicação e extensão) com grupo de controle gamificado",
   "method": "Delineamento misto 2 (tratamento vs. controle) × 2 (pré vs. pós); Bad News vs. Tetris; 18 manchetes falsas",
   "sample_size": "N = 196",
   "main_finding": "Jogar o Bad News melhorou a capacidade de identificar técnicas de desinformação em relação ao controle gamificado e aumentou a confiança nos próprios julgamentos.",
   "abstract_quote": "We find that playing Bad News significantly improves people's ability to spot misinformation techniques compared to a gamified control group, and crucially, also increases people's level of confidence in their own judgments."
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
   "study_type": "Experimentos voluntários dentro do jogo, com desenho pré e pós (um por versão linguística do Bad News)",
   "method": "Bad News em quatro versões linguísticas; o desenho vem do texto do artigo, não do resumo",
   "sample_size": "não informado no resumo",
   "main_finding": "O Bad News confere resistência psicológica a estratégias comuns de desinformação online em diferentes culturas.",
   "abstract_quote": "can confer psychological resistance against common online misinformation strategies across different cultures"
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
   "study_type": "Quatro replicações estendidas, com dados novos coletados por equipes de estudantes de graduação",
   "method": "Avaliação antes e depois do Bad News, com análise de teoria de detecção de sinal",
   "sample_size": "não informado no resumo",
   "main_finding": "O Bad News reduziu a crença em tweets falsos, mas reduziu a crença em tweets verdadeiros na mesma medida, ou quase, e não melhorou a discriminação.",
   "abstract_quote": "But playing the BNG also reduced belief in true Tweets to the same or almost the same extent. Exploratory signal detection theory analyses indicated that the BNG increased response bias but did not improve discrimination."
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
   "study_type": "Dois experimentos com amostra de conveniência",
   "method": "Bad News, com teste de desinformação real que viralizou e de proteção cruzada",
   "sample_size": "total n = 2188",
   "main_finding": "Um jogo de 15 minutos confere resistência psicológica à desinformação do mundo real que usa as técnicas treinadas (d = 0,37), com proteção cruzada menor (d = 0,10).",
   "abstract_quote": "We find that playing a 15 min game confers psychological resistance against real-world misinformation that makes use of manipulation techniques against which people were inoculated"
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
   "study_type": "Três experimentos longitudinais (dois pré-registrados)",
   "method": "Bad News (inoculação) vs. Tetris (controle gamificado), com avaliação de longo prazo",
   "sample_size": "NExp1 = 151, NExp2 = 194, NExp3 = 170",
   "main_finding": "O efeito de inoculação do jogo ficou estável por pelo menos 3 meses no Experimento 1, mas decaiu de forma significativa em 2 meses no Experimento 2 sem testes regulares.",
   "abstract_quote": "In Experiment 1, we assessed participants at regular intervals to explore the longevity of this effect and found that the inoculation effect remains stable for at least 3 months. In Experiment 2, we sought to replicate these findings without regular testing and found significant decay over a 2-month time period"
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
   "method": "Bad News e Harmony Square, com e sem exercício de feedback",
   "sample_size": "N1 = 191, N2 = 321; N3 = 559, N4 = 2,558, N5 = 419, N6 = 882",
   "main_finding": "Acrescentar exercícios de feedback aos jogos aumenta o discernimento entre notícias falsas e verdadeiras, principalmente por melhorar a detecção de notícias reais.",
   "abstract_quote": "we implemented two different types of feedback exercises in the Harmony Square and Bad News games and find that this significantly boosts discernment compared with playing the game without a feedback exercise, primarily by improving accuracy at detecting real news."
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
   "method": "Jogo interativo de inoculação vs. inoculação gráfica vs. controle, com seguimento de 2 semanas",
   "sample_size": "A total of 180 Chinese participants",
   "main_finding": "As duas inoculações reduziram a credibilidade percebida e a intenção de compartilhar desinformação, e o jogo foi mais eficaz que a versão gráfica na credibilidade percebida, com efeito estável após 2 semanas.",
   "abstract_quote": "The results indicated that both types of inoculation interventions significantly decreased the perceived credibility and sharing intention of misinformation. Game-based inoculation was more effective than graphic-based inoculation in terms of misinformation perceived credibility, and the intervention effects were stable after 2 weeks."
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
   "study_type": "Ensaio controlado randomizado de campo (resultado nulo)",
   "method": "Intervenção em forma de jogo, baseada em inoculação psicológica, aplicada no norte da Índia",
   "sample_size": "n = 757",
   "main_finding": "O estudo não replicou os efeitos anteriores: a intervenção não teve efeito significativo sobre a confiabilidade percebida, os julgamentos de confiança nem a disposição de compartilhar.",
   "abstract_quote": "the present study conducted in north India (n = 757) did not replicate earlier findings. We found no significant impact of the intervention on the perceived reliability of messages containing misinformation, confidence judgments, and willingness to share information with others."
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
   "study_type": "Dois estudos online com delineamento de três grupos de Solomon",
   "method": "Bad News, testando efeitos de itens e efeitos de teste",
   "sample_size": "total N = 2,159",
   "main_finding": "Os efeitos de inoculação sofrem alguma influência dos itens, mas não de efeitos de teste, e o jogo melhora a capacidade de identificar técnicas de desinformação sem tornar as pessoas mais céticas com notícias reais.",
   "abstract_quote": "We find that inoculation interventions are somewhat influenced by item effects, and not by testing effects. We show that inoculation interventions are effective at improving people’s ability to spot misinformation techniques and that the Bad News game does not make people more skeptical of real news."
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
   "study_type": "Experimento randomizado (replicação conceitual) com grupo de controle",
   "method": "Jogo Cat Park (cinco técnicas de manipulação e desinformação por imagens), com o mesmo desenho do estudo do Harmony Square de 2020",
   "sample_size": "N = 380",
   "main_finding": "Os jogadores do Cat Park acharam a desinformação menos confiável e ficaram menos dispostos a compartilhá-la, mas não ganharam confiança significativa.",
   "abstract_quote": "people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001) compared to a control group, and are significantly less willing to share misinformation with people in their network (d = 0.54, p < 0.001)."
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
   "method": "Jogo digital sobre desinformação vs. jogo de linguagem de controle, com alunos do 7º e 8º anos",
   "sample_size": "N = 84 and N = 131",
   "main_finding": "Jogar o jogo de desinformação melhorou o discernimento de acurácia, o discernimento de compartilhamento e o conhecimento metaestratégico sobre corroboração, em comparação com o jogo de linguagem de controle.",
   "abstract_quote": "In two studies with 7th and 8th grade students (N = 84 and N = 131), we found that playing the misinformation game resulted in better accuracy discernment, sharing discernment, and metastrategic knowledge about corroboration, compared to playing a control language game."
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
   "study_type": "Estudo experimental em sala de aula, com pré e pós-intervenção",
   "method": "Bad News jogado individualmente, em duplas ou com a turma toda",
   "sample_size": "516 upper-secondary Swedish students",
   "main_finding": "Os estudantes melhoraram a capacidade de discernir técnicas de manipulação em postagens de redes sociais.",
   "abstract_quote": "We therefore evaluated its impact on 516 upper-secondary Swedish students playing individually, paired, or with the whole class. Results show that students improved their ability to discern manipulation techniques in social media posts."
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
   "study_type": "Desenho experimental em salas de aula reais, com seguimento de três meses",
   "method": "Bad News (jogo), oficina News Evaluator e intervenções disciplinares, em três tipos de intervenção (só o Bad News é jogo)",
   "sample_size": "459 students",
   "main_finding": "Nem o jogo Bad News nem a oficina News Evaluator melhoraram significativamente a capacidade dos estudantes de avaliar notícias confiáveis e enganosas (resultado nulo).",
   "abstract_quote": "Neither the Bad News game nor the News Evaluator workshop significantly improved students' ability to evaluate credible and misleading news."
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
   "study_type": "Estudo experimental (o resumo não diz se a alocação foi aleatória)",
   "method": "Jogo de computador sobre fake news desenvolvido em Singapura, com quem jogou comparado a quem não jogou",
   "sample_size": "college (n = 84) and junior high and secondary school (n = 30) students",
   "main_finding": "Quem jogou teve pontuação maior na detecção de fake news do que quem não jogou, e também ficou mais cético quanto à informação de redes sociais.",
   "abstract_quote": "We also found that those who played the game scored higher in detecting fake news than those who did not play the game –consistent with the predicted effects of message inoculation."
  },
  {
   "doi": "10.11645/18.2.13",
   "title": "Chaos creator",
   "authors": [
    "Mandi Goodsett"
   ],
   "year": 2024,
   "venue": "Journal of Information Literacy",
   "study_type": "Estudo quase-experimental",
   "method": "Técnicas de prebunking entregues pelo jogo competitivo Chaos Creator (baseado no Bad News), numa sessão de letramento informacional com estudantes de graduação, comparadas ao teste CRAP",
   "sample_size": "não informado no resumo",
   "main_finding": "As técnicas de inoculação ajudaram mais os estudantes a identificar desinformação do que o teste CRAP, mas podem gerar ceticismo excessivo diante de mensagens confiáveis.",
   "abstract_quote": "Results of the study show that misinformation inoculation techniques are more effective than the popular source evaluation tool, the CRAP test, in helping students identify misinformation. However, misinformation inoculation techniques can backfire, causing students to become overly sceptical of trustworthy messages."
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
   "study_type": "Desenho pré e pós-teste, sem grupo de controle",
   "method": "Escape game em realidade aumentada (Escape Fake) com professores em formação",
   "sample_size": "45 pre-service teachers",
   "main_finding": "Os professores em formação aumentaram o conhecimento sobre fake news, o senso crítico e a confiança, mas o jogo não melhorou a capacidade de distinguir informação real de falsa.",
   "abstract_quote": "However, playing the game did not promote the ability to discern real from false information."
  },
  {
   "doi": "10.1007/s10758-024-09749-y",
   "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2024,
   "venue": "Technology, Knowledge and Learning",
   "study_type": "Estudo de campo com desenho pré e pós-teste, sem grupo de controle",
   "method": "Escape game em realidade aumentada (Escape Fake) com estudantes",
   "sample_size": "A total of 28 students (14 girls, mean age = 14.71 years)",
   "main_finding": "O Escape Fake atingiu quatro objetivos de aprendizagem relevantes para detectar fake news, com maior efeito na aquisição de conhecimento (d = 1,34).",
   "abstract_quote": "The results show that Escape Fake can address four learning objectives relevant in fake news detection with educationally desired effect sizes: Knowledge acquisition (d = 1.34), ability to discern information (d = 0.39),"
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung",
   "study_type": "Estudo-piloto com desenho pré e pós-teste, sem grupo de controle",
   "method": "Escape game em realidade aumentada (Escape Fake) com estudantes",
   "sample_size": "27 Schüler:innen",
   "main_finding": "O Escape Fake conseguiu transmitir conhecimento sobre fake news, promover a capacidade de reconhecer a confiabilidade das informações, gerar uma postura mais crítica e reforçar a confiança.",
   "abstract_quote": "Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln, die Fähigkeit fördern, die Zuverlässigkeit von Informationen zu erkennen, zu einer kritischeren Haltung"
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
   "study_type": "Estudo de campo online randomizado, com pré e pós-testes",
   "method": "Serious game 'How to Spot Fake News', baseado no teste CRAAP, para aprendizagem móvel",
   "sample_size": "351 participants",
   "main_finding": "O jogo melhorou o conhecimento de letramento informacional necessário para avaliar fontes de informação online.",
   "abstract_quote": "The results revealed that using a serious game of \"How to Spot Fake News\" can improve the knowledge of information literacy needed to evaluate online sources of information."
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
   "study_type": "Estudo de campo online randomizado, mais discussão de usabilidade em uma turma",
   "method": "Serious game MAthE, aplicação web de checagem de notícias",
   "sample_size": "randomized online field study (n = 111); media class (n = 35)",
   "main_finding": "O jogo pode aumentar a conscientização, ensinar ferramentas de autenticação e destacar padrões que indicam a autenticidade dos artigos, com evidência preliminar.",
   "abstract_quote": "this paper reports the results of a randomized online field study (n = 111), which provides some preliminary evidence. Specifically, it is validated that the game can raise awareness, teach about authentication tools, and highlight the importance of patterns that include evidence regarding the authenticity of articles."
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
   "study_type": "Experimento escolar com medidas antes e depois",
   "method": "Intervenção ativa (jogo online) vs. passiva (folheto), ambas de inoculação lógica",
   "sample_size": "373 participants",
   "main_finding": "A diversão foi maior com o jogo; não houve diferença de desempenho entre as duas intervenções, e os estudantes melhoraram na identificação de notícias falsas, mas pioraram na de notícias reais.",
   "abstract_quote": "Findings show that enjoyment was significantly higher in the active intervention group compared to the passive one. However, our findings revealed no significant differences in credibility evaluation performance between the two intervention types over time. Moreover, we uncovered a paradoxical trend: while students improved in identifying fake news after the interventions, they demonstrated a decline in proficiency at identifying real news."
  }
 ],
 "search_notes": "Escolhi os 23 candidatos aprovados e não busquei fora da lista. Os 10.1002/acp.3995 e 10.3758/s13423-025-02827-x, que a checagem apontou na tentativa 3, ficaram de fora. Abri o resumo de cada um e copiei os trechos com a ferramenta de leitura, que devolve o texto em pedaços curtos. Cada trecho entre aspas é a junção de frases consecutivas do resumo, sem tradução nem paráfrase.\n\nDe onde veio cada resumo (para reverificar):\n- Páginas dos periódicos ou do repositório: joc.91 e joc.324 (journalofcognition.org); misinforeview.hks.harvard.edu; repository.cam.ac.uk/handle/1810/278736 (Roozenbeek 2018); cedtech.net; online-journals.org (iJIM); cris.iucc.ac.il (Barzilai).\n- Europe PMC: Graham (joc.324, metadados) e Neylan (s41598-023-43885-2).\n- API do Semanticscholar: Roozenbeek 2019, Hu 2023, Leder 2024, Roozenbeek 2022, Maertens 2021, Goodsett, Axelsson, Nygren & Efimova, Tandoc & Seet, Buchner 2024, Katsaounidou, Reinhardt e Roozenbeek (Solomon).\n- Crossref: Harjani (e12) e Buchner 2023 (mpaed).\nOs que vieram do Semanticscholar ou do Crossref não foram abertos na página do periódico, porque Nature e Springer exigem autenticação e a Royal Society retornou 403. O texto do resumo vem do registro do indexador.\n\nCorreções da rodada anterior:\n- Roozenbeek & van der Linden 2018: o trecho agora tem duas frases completas. O artigo é de 2018 (online) e sai no vol. 22 de 2019.\n- Barzilai: confirmei \"N = 84 and N = 131\" no resumo, na forma exata.\n- Reinhardt: acrescentei no trecho a parte sobre desempenho. O resumo diz que não houve diferença entre as intervenções, que os estudantes melhoraram nas notícias falsas e pioraram nas reais.\n- Graham et al. (joc.324): ano confirmado como 2023 (publicado em 9 out. 2023, vol. 6, nº 1). O Europe PMC lista o tipo como \"research-article; News\", mas a página do periódico o classifica como \"Research article, peer reviewed\". Os dados são novos, de quatro replicações.\n- Maertens: o resumo diz que o efeito ficou estável por pelo menos 3 meses no Experimento 1 e decaiu significativamente em 2 meses no Experimento 2. O achado está correto.\n- Leder et al.: o resumo dá N1 = 191, N2 = 321, N3 = 559, N4 = 2,558, N5 = 419 e N6 = 882. O Harmony Square aparece como um dos dois jogos, mas o foco do estudo é o efeito do feedback sobre o discernimento, e o resumo não menciona eleições nem política partidária. Mantive o artigo com essa ressalva.\n\nRessalvas de elegibilidade (cabe ao pesquisador decidir):\n- Hu et al. (2023): tem um braço gráfico, que não é jogo.\n- Reinhardt et al. (2025): o braço passivo é um folheto, que não é jogo.\n- Nygren & Efimova (2025): avalia três intervenções, e só o Bad News é jogo. O resultado é nulo.\n- Neylan et al. (2023): replica o desenho do estudo do Harmony Square de 2020, mas com um jogo novo (Cat Park) e dados próprios.\n- Roozenbeek 2018: o tema do jogo é uma questão politizada (a crise de refugiados na Europa), sem foco partidário.\n- Roozenbeek et al. 2020 (HKS Misinformation Review): o resumo não traz amostra. O DOI com barra dupla segue o registro da página.\n- Tandoc & Seet: o resumo não diz se a alocação foi aleatória.\n- Buchner (2023), Buchner (2024) e Buchner & Höfler (2024): usam o mesmo jogo, Escape Fake, com amostras diferentes (27, 28 e 45). Não são duplicatas, mas as amostras podem se sobrepor.\n- Buchner 2023 está em alemão. O trecho foi copiado do original e não foi traduzido."
}