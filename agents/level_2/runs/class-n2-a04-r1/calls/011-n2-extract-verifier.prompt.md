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
   "study_type": "Estudo empírico (avaliação em larga escala)",
   "method": "Pré e pós-jogo com o jogo Bad News (inoculação)",
   "sample_size": "N = 15,000 participants",
   "main_finding": "A capacidade de identificar e resistir à desinformação melhora após jogar Bad News.",
   "abstract_quote": "We provide initial evidence that people's ability to spot and resist misinformation improves after gameplay, irrespective of education, age, political ideology, and cognitive style."
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
   "study_type": "Experimento controlado",
   "method": "Delineamento misto 2 (tratamento vs. controle gamificado) × 2 (pré vs. pós) com Bad News",
   "sample_size": "N = 196",
   "main_finding": "Jogar Bad News melhora a capacidade de identificar técnicas de desinformação e aumenta a confiança nos próprios julgamentos, em comparação com um controle gamificado.",
   "abstract_quote": "We find that playing Bad News significantly improves people’s ability to spot misinformation techniques compared to a gamified control group, and crucially, also increases people’s level of confidence in their own judgments."
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
   "study_type": "Estudo empírico (pesquisas intra-sujeitos pré e pós dentro do jogo; publicado como 'Essay' pela revista, com revisão por pares)",
   "method": "Bad News em quatro idiomas, com pesquisas pré e pós dentro do jogo (o resumo não descreve o desenho)",
   "sample_size": "não informado no resumo",
   "main_finding": "Bad News confere resistência psicológica a estratégias de desinformação em diferentes culturas.",
   "abstract_quote": "This study finds that the online \"fake news\" game, Bad News, can confer psychological resistance against common online misinformation strategies across different cultures."
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
   "method": "Bad News contra grupo de controle gamificado (Tetris), com avaliações em intervalos regulares",
   "sample_size": "NExp1 = 151, NExp2 = 194, NExp3 = 170",
   "main_finding": "O efeito de inoculação de Bad News permaneceu estável por pelo menos 3 meses no Experimento 1, mas decaiu de forma significativa em 2 meses no Experimento 2.",
   "abstract_quote": "In Experiment 1, we assessed participants at regular intervals to explore the longevity of this effect and found that the inoculation effect remains stable for at least 3 months."
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
   "study_type": "Dois estudos experimentais online com dados novos",
   "method": "Delineamento de três grupos de Solomon com Bad News",
   "sample_size": "total N = 2,159",
   "main_finding": "A inoculação melhora a capacidade de identificar técnicas de desinformação, e Bad News não torna as pessoas mais céticas com notícias reais.",
   "abstract_quote": "We show that inoculation interventions are effective at improving people's ability to spot misinformation techniques and that the Bad News game does not make people more skeptical of real news."
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
   "method": "Jogo Bad News de 15 minutos, avaliado com desinformação do mundo real",
   "sample_size": "n = 2188",
   "main_finding": "Jogar 15 minutos confere resistência a desinformação real que usa as técnicas inoculadas, com proteção cruzada bem menor.",
   "abstract_quote": "We find that playing a 15 min game confers psychological resistance against real-world misinformation that makes use of manipulation techniques against which people were inoculated"
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
   "method": "Três grupos (jogo, gráfico, controle) com seguimento de 2 semanas",
   "sample_size": "180 Chinese participants",
   "main_finding": "A inoculação por jogo foi mais eficaz que a por gráfico na credibilidade percebida da desinformação, com efeitos estáveis após 2 semanas.",
   "abstract_quote": "Game-based inoculation was more effective than graphic-based inoculation in terms of misinformation perceived credibility, and the intervention effects were stable after 2 weeks."
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
   "study_type": "Ensaio controlado randomizado de campo (a randomização vem do título)",
   "method": "Intervenção gamificada de inoculação no norte da Índia, com grupo de controle",
   "sample_size": "(n = 757)",
   "main_finding": "Resultado nulo: a intervenção não teve efeito significativo sobre a confiabilidade percebida de mensagens com desinformação, a confiança nos julgamentos nem a disposição de compartilhar.",
   "abstract_quote": "We found no significant impact of the intervention on the perceived reliability of messages containing misinformation, confidence judgments, and willingness to share information with others."
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
   "method": "Exercícios de feedback nos jogos Bad News e Harmony Square, comparados ao jogo sem feedback",
   "sample_size": "N1 = 191, N2 = 321, N3 = 559, N4 = 2,558, N5 = 419, N6 = 882",
   "main_finding": "Exercícios de feedback aumentam a discriminação entre desinformação e notícias reais nos jogos de inoculação, sobretudo por melhorar a detecção de notícias reais.",
   "abstract_quote": "In Experiments 3-6, we implemented two different types of feedback exercises in the Harmony Square and Bad News games and find that this significantly boosts discernment compared with playing the game without a feedback exercise, primarily by improving accuracy at detecting real news."
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
   "study_type": "Replicação conceitual com dados novos (experimento)",
   "method": "Jogo Cat Park contra grupo de controle, com medidas pré e pós",
   "sample_size": "(N = 380)",
   "main_finding": "Quem joga Cat Park acha a desinformação menos confiável e fica menos disposto a compartilhá-la, mas não fica mais confiante em identificá-la.",
   "abstract_quote": "Like the original study, we find that people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001) compared to a control group"
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
   "study_type": "Quatro replicações estendidas, cada uma com dados próprios",
   "method": "Bad News contra um jogo não relacionado, com avaliação pré e pós de tuítes",
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
   "study_type": "Experimento pré-registrado",
   "method": "Alocação aleatória a 4 condições: treino gamificado de aprendizado indutivo, treino não gamificado, controle sem tratamento e Bad News",
   "sample_size": "N = 282 Prolific users",
   "main_finding": "Não houve diferenças significativas entre as condições, com evidência muito forte para a hipótese nula.",
   "abstract_quote": "The analyses indicated that there were no significant differences between conditions and the Bayes factor indicated very strong evidence for the null."
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
   "method": "Pré-teste e pós-teste com o jogo de fuga em realidade aumentada Escape Fake",
   "sample_size": "A total of 28 students (14 girls, mean age = 14.71 years) participated",
   "main_finding": "O jogo produziu ganhos em conhecimento, discernimento, atitude crítica e confiança, com tamanhos de efeito desejáveis em educação.",
   "abstract_quote": "The results show that Escape Fake can address four learning objectives relevant in fake news detection with educationally desired effect sizes"
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
   "study_type": "Estudo com desenho pré e pós-teste, sem grupo de comparação",
   "method": "Escape Fake (jogo de fuga em realidade aumentada) com professores em formação",
   "sample_size": "a pre-/post-test design was conducted with 45 pre-service teachers",
   "main_finding": "Após o jogo houve mais conhecimento, atitude crítica e confiança, mas a capacidade de discernir informação real de falsa não melhorou.",
   "abstract_quote": "However, playing the game did not promote the ability to discern real from false information."
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung",
   "study_type": "Estudo piloto com desenho de pré e pós-teste",
   "method": "Escape Fake (jogo de fuga em realidade aumentada) com alunos",
   "sample_size": "Vortest-Nachtest Design mit 27 Schüler:innen durchgeführt",
   "main_finding": "O jogo transmite conhecimento sobre fake news, melhora o reconhecimento da confiabilidade da informação e a atitude crítica e aumenta a confiança.",
   "abstract_quote": "Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln, die Fähigkeit fördern, die Zuverlässigkeit von Informationen zu erkennen"
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
   "study_type": "Estudo de campo online com pré e pós-testes",
   "method": "Serious game 'How to Spot Fake News' (baseado no teste CRAAP) para m-learning",
   "sample_size": "pre-posttests involving 351 participants",
   "main_finding": "O jogo melhora o conhecimento de letramento informacional necessário para avaliar fontes online.",
   "abstract_quote": "The results revealed that using aserious game of “How to Spot Fake News” can improve the knowledge of information literacyneeded to evaluate online sources of information."
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
   "method": "Prebunking com o jogo Bad News, comparado a uma oficina de checagem (News Evaluator) e a lições disciplinares",
   "sample_size": "Using an experimental design with 459 students in authentic classroom settings",
   "main_finding": "Nem Bad News nem a oficina News Evaluator melhoraram de forma significativa a avaliação de notícias confiáveis e enganosas.",
   "abstract_quote": "Neither the Bad News game nor the News Evaluator workshop significantly improved students' ability to evaluate credible and misleading news."
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
   "study_type": "Experimento controlado randomizado, pré-registrado",
   "method": "Delineamento misto 2 × 2 (pré–pós, tratamento–controle) com o jogo online Radicalise",
   "sample_size": "randomized controlled experiment (n = 291)",
   "main_finding": "Jogar Radicalise melhora a capacidade e a confiança em identificar mensagens manipulativas e características associadas à vulnerabilidade.",
   "abstract_quote": "We find that playing Radicalise significantly improves participants’ ability and confidence in spotting manipulative messages and the characteristics associated with vulnerability."
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
   "study_type": "Experimento de campo randomizado controlado",
   "method": "Delineamento misto 2x2 (pré-pós / tratamento-controle) com o jogo Radicalise",
   "sample_size": "We conducted a field experiment (N = 191)",
   "main_finding": "O jogo melhorou a capacidade de identificar mensagens manipulativas, mas não a de identificar indivíduos vulneráveis.",
   "abstract_quote": "We find that playing the game significantly improved participants’ ability (p = 0.034, d = 0.31) in spotting manipulative messaging"
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
   "study_type": "Experimento com estudantes do ensino médio",
   "method": "Jogo de cartas Follow me contra fake news",
   "sample_size": "an experiment on a sample of 130 secondary school students from six different schools",
   "main_finding": "Não houve melhora global estatisticamente significativa na capacidade dos alunos de reconhecer fake news.",
   "abstract_quote": "although there was no global statistically significant improvement measured in students’ ability to recognize fake news"
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
   "study_type": "Estudo de campo online randomizado, mais feedback de uma turma de mídia",
   "method": "Serious game web de verificação de notícias, avaliado com participantes",
   "sample_size": "a randomized online field study (n = 111); a media class (n = 35)",
   "main_finding": "O jogo aumenta a conscientização e ensina ferramentas de autenticação.",
   "abstract_quote": "Specifically, it is validated that the game can raise awareness, teach about authentication tools, and highlight the importance of patterns that include evidence regarding the authenticity of articles."
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
   "study_type": "Replicação com dados próprios, desenho intra-sujeitos (o resumo não usa os termos pré/pós)",
   "method": "Bad News Game com amostra indiana",
   "sample_size": "an Indian sample (n = 1002)",
   "main_finding": "Houve melhora significativa na identificação de desinformação por Conspiração, Personificação e, em menor grau, Descrédito.",
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
   "method": "Jogo competitivo Chaos Creator (baseado em Bad News) em aula de letramento informacional, comparado ao teste CRAP",
   "sample_size": "não informado no resumo",
   "main_finding": "As técnicas de inoculação foram mais eficazes que o teste CRAP para ajudar os alunos a identificar desinformação.",
   "abstract_quote": "Results of the study show that misinformation inoculation techniques are more effective than the popular source evaluation tool, the CRAP test, in helping students identify misinformation."
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
   "method": "Jogo digital de avaliação e compartilhamento responsável de informação, comparado a um jogo de linguagem de controle",
   "sample_size": "In two studies with 7th and 8th grade students (N = 84 and N = 131)",
   "main_finding": "O jogo gerou melhor discernimento de acurácia e de compartilhamento e mais conhecimento metaestratégico, sem mudar as atitudes autorrelatadas.",
   "abstract_quote": "playing the misinformation game resulted in better accuracy discernment"
  }
 ],
 "search_notes": "Os candidatos aprovados eram 26, e eu devia entregar 25. Retirei Tandoc & Seet (10.5209/esmp.88599). O resumo dele (Crossref) só diz que quem jogou \"subsequently improved in their self-reported scores\" e que quem jogou pontuou mais que quem não jogou, com n = 84 e n = 30. Não usa os termos pré-teste, pós-teste, experimento ou controle. O texto completo não abriu (o PDF veio ilegível e a página em inglês deu erro 500), então não consegui confirmar o desenho exigido. DOI de Modirrousta-Galian: o DOI correto é 10.1037/xap0000458, e o Crossref confirma título, autores, periódico (JEP: Applied, 29(3)) e ano (2023). O Europe PMC confirma \"N = 282 Prolific users\" e a citação, letra por letra. O DOI 10.1002/acp.3995 é o de Iyengar et al., que está no item correspondente. Conferido letra por letra contra o resumo (Crossref, Europe PMC ou página do periódico/repositório): Basol (N = 196 e citação), Maertens (citação, Ns e decaimento no Exp. 2), Leder (citação e os seis Ns), Nygren & Efimova, os três de Buchner, Sureephong (inclui os espaços ausentes e as aspas curvas do original), os dois de Saleh, Pomichal (apóstrofo curvo), Katsaounidou, Iyengar (n = 1002, desenho intra-sujeitos), Goodsett (quase-experimental, sem N no resumo), Axelsson (516 alunos, linguagem pré/pós-intervenção, página da VU) e Barzilai (página do repositório IUCC). Os itens 1, 5, 6, 7, 8, 10 e 11 já tinham sido aprovados pelo verificador e não os reabri. Ressalvas: (1) Roozenbeek et al. 2020 (Misinformation Review) é classificado pela revista como \"Essay\" (com revisão por pares), mas é empírico, com pesquisas dentro do jogo. O resumo não traz amostra nem desenho (o N = 5.061 está só no sumário da página), então ficou \"não informado no resumo\". (2) Os dois estudos de Saleh usam o jogo Radicalise, sobre extremismo e não desinformação em sentido estrito, e o plano os aceitou. A revisão por pares do periódico advances.in/psychology não foi conferida. (3) Leder et al. inclui o Harmony Square, com enredo político, mas o resumo não cita eleição nem partido. (4) Nygren & Efimova avaliam Bad News ao lado de outras intervenções. Hu et al. compara jogo e gráfico. (5) Anos: usei o ano de publicação online para Buchner & Höfler (2024), Buchner (2024, edição de 2025), Axelsson (2024, edição de 2025) e Saleh 2021 (edição de 2024). Para Iyengar usei 2023 (edição; online em 2022). Todos estão dentro de 2018–2025. (6) O resumo de Harjani et al. não descreve a randomização, que vem do título. (7) Os Ns de Roozenbeek 2019 e 2022 e Hu, Harjani, Neylan e Graham seguem os candidatos já aprovados. (8) Não busquei artigos fora da lista aprovada.\""
}