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
   "study_type": "Estudo empírico em larga escala com jogo online (Bad News), desenho pré e pós-jogo",
   "method": "Avaliação em larga escala do jogo Bad News, um jogo de navegador em que o jogador faz o papel de produtor de notícias falsas, com medidas antes e depois do jogo",
   "sample_size": "N = 15,000",
   "main_finding": "A capacidade de identificar e resistir à desinformação melhorou após jogar o Bad News, independentemente de escolaridade, idade, ideologia política e estilo cognitivo.",
   "abstract_quote": "We conducted a large-scale evaluation of the game with N = 15,000 participants in a pre-post gameplay design. We provide initial evidence that people’s ability to spot and resist misinformation improves after gameplay, irrespective of education, age, political ideology, and cognitive style."
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
   "study_type": "Experimento (replicação e extensão) com grupo de controle gamificado",
   "method": "Delineamento misto 2 (tratamento vs. controle) × 2 (pré vs. pós); 18 manchetes falsas avaliadas antes e depois de jogar o Bad News",
   "sample_size": "N = 196",
   "main_finding": "Jogar o Bad News melhorou a capacidade de identificar técnicas de desinformação em relação a um controle gamificado e aumentou a confiança nos próprios julgamentos.",
   "abstract_quote": "We find that playing Bad News significantly improves people’s ability to spot misinformation techniques compared to a gamified control group, and crucially, also increases people’s level of confidence in their own judgments."
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
   "method": "Participantes alocados aleatoriamente a inoculação por jogo interativo, inoculação gráfica ou grupo de controle",
   "sample_size": "A total of 180 Chinese participants",
   "main_finding": "Os dois tipos de inoculação, o jogo e o material gráfico, reduziram a credibilidade percebida e a intenção de compartilhar desinformação.",
   "abstract_quote": "A total of 180 Chinese participants were randomly assigned to game-based inoculation, graphic-based inoculation, and control groups. The results indicated that both types of inoculation interventions significantly decreased the perceived credibility and sharing intention of misinformation."
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
   "method": "Intervenção em jogo baseada em inoculação psicológica, testada no norte da Índia",
   "sample_size": "n = 757",
   "main_finding": "O estudo não replicou os efeitos anteriores: a intervenção não teve efeito significativo sobre a confiabilidade percebida da desinformação, a confiança nem a disposição de compartilhar.",
   "abstract_quote": "the present study conducted in north India (n = 757) did not replicate earlier findings. We found no significant impact of the intervention on the perceived reliability of messages containing misinformation, confidence judgments, and willingness to share information with others."
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
   "study_type": "Seis experimentos: dois de laboratório pré-registrados e quatro pesquisas quase-experimentais dentro do jogo",
   "method": "Bad News e Harmony Square, com e sem exercício de feedback depois do jogo; discernimento entre desinformação e notícias reais",
   "sample_size": "N1 = 191, N2 = 321; N3 = 559, N4 = 2,558, N5 = 419, N6 = 882",
   "main_finding": "Acrescentar exercícios de feedback ao jogo aumentou o discernimento entre notícias falsas e verdadeiras, principalmente por melhorar a identificação de notícias reais.",
   "abstract_quote": "In Experiments 3-6, we implemented two different types of feedback exercises in the Harmony Square and Bad News games and find that this significantly boosts discernment compared with playing the game without a feedback exercise, primarily by improving accuracy at detecting real news."
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
   "method": "Jogo Bad News de 15 minutos; desinformação viral do mundo real, com e sem as técnicas treinadas (proteção cruzada)",
   "sample_size": "total n = 2188",
   "main_finding": "Um jogo de 15 minutos conferiu resistência psicológica à desinformação real que usa as técnicas treinadas (d = 0,37), com proteção cruzada menor (d = 0,10) para desinformação sem essas técnicas.",
   "abstract_quote": "We find that playing a 15 min game confers psychological resistance against real-world misinformation that makes use of manipulation techniques against which people were inoculated (Cohen's d = 0.37, Cohen's U3 = 64.4%, p < 0.001)"
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
   "method": "Bad News (grupo de inoculação) vs. Tetris (controle gamificado); avaliação da confiabilidade de manchetes ao longo do tempo",
   "sample_size": "NExp1 = 151, NExp2 = 194, NExp3 = 170",
   "main_finding": "O efeito de inoculação do jogo permaneceu estável por pelo menos 3 meses no Experimento 1, mas decaiu ao longo de 2 meses no Experimento 2.",
   "abstract_quote": "We found that participants rate fake news as significantly less reliable after the intervention. In Experiment 1, we assessed participants at regular intervals to explore the longevity of this effect and found that the inoculation effect remains stable for at least 3 months."
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
   "study_type": "Quatro experimentos voluntários dentro do jogo, um por versão linguística, com desenho pré e pós",
   "method": "Versões do Bad News em alemão, grego, polonês e sueco, avaliadas antes e depois do jogo",
   "sample_size": "não informado no resumo",
   "main_finding": "O Bad News conferiu resistência psicológica a estratégias comuns de desinformação online em diferentes culturas.",
   "abstract_quote": "This study finds that the online “fake news” game, Bad News, can confer psychological resistance against common online misinformation strategies across different cultures."
  },
  {
   "doi": "10.11645/18.2.13",
   "title": "Chaos creator",
   "authors": [
    "Mandi Goodsett"
   ],
   "year": 2024,
   "venue": "Journal of Information Literacy",
   "study_type": "Estudo quase-experimental com estudantes de graduação",
   "method": "Técnicas de prebunking entregues pelo jogo competitivo Chaos Creator (baseado no Bad News) numa sessão de instrução em letramento informacional, comparadas ao teste CRAP",
   "sample_size": "não informado no resumo",
   "main_finding": "As técnicas de inoculação ajudaram os estudantes a identificar desinformação mais do que o teste CRAP, mas podem gerar ceticismo excessivo diante de mensagens confiáveis.",
   "abstract_quote": "Results of the study show that misinformation inoculation techniques are more effective than the popular source evaluation tool, the CRAP test, in helping students identify misinformation."
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
   "study_type": "Dois estudos experimentais com alunos do ensino fundamental",
   "method": "Jogo digital Misinformation Is Contagious vs. jogo de linguagem de controle, com discernimento de acurácia e de compartilhamento como desfechos",
   "sample_size": "N = 84 and N = 131",
   "main_finding": "Jogar o jogo de desinformação melhorou o discernimento de acurácia e de compartilhamento em relação ao jogo de controle, mas não alterou as posturas autorrelatadas sobre compartilhar desinformação.",
   "abstract_quote": "we found that playing the misinformation game resulted in better accuracy discernment, sharing discernment, compared to playing a control language game."
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
   "study_type": "Desenho pré e pós-teste (sem grupo de controle)",
   "method": "Escape game em realidade aumentada (Escape Fake) jogado por futuros professores",
   "sample_size": "45 pre-service teachers",
   "main_finding": "Após o jogo, os futuros professores tiveram mais conhecimento sobre fake news, mais senso crítico e mais confiança, mas o jogo não melhorou a capacidade de distinguir informação verdadeira de falsa.",
   "abstract_quote": "However, playing the game did not promote the ability to discern real from false information."
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
   "study_type": "Estudo experimental em sala de aula, com medidas pré e pós",
   "method": "Bad News jogado individualmente, em duplas ou com a turma toda, em aulas de educação cívica",
   "sample_size": "516 upper-secondary Swedish students",
   "main_finding": "Os estudantes melhoraram a capacidade de discernir técnicas de manipulação em postagens de redes sociais.",
   "abstract_quote": "Results show that students improved their ability to discern manipulation techniques in social media posts."
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
   "method": "Serious game móvel 'How to Spot Fake News', baseado no teste CRAAP, em que o jogador é bibliotecário",
   "sample_size": "351 participants",
   "main_finding": "O serious game melhorou o conhecimento de letramento informacional necessário para avaliar fontes de informação online.",
   "abstract_quote": "The results revealed that using a serious game of \"How to Spot Fake News\" can improve the knowledge of information literacy needed to evaluate online sources of information."
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
   "study_type": "Quatro replicações estendidas de Basol et al. (2020), com dados novos",
   "method": "Quatro equipes de estudantes de graduação em psicologia; avaliação de tweets falsos e verdadeiros antes e depois do Bad News ou de um jogo não relacionado; análise de teoria de detecção de sinal",
   "sample_size": "não informado no resumo",
   "main_finding": "Jogar o Bad News reduziu a crença em tweets falsos, mas reduziu na mesma medida (ou quase) a crença em tweets verdadeiros, alterando o viés de resposta sem melhorar a discriminação.",
   "abstract_quote": "Playing the BNG reduced belief in false Tweets. But playing the BNG also reduced belief in true Tweets to the same or almost the same extent."
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
   "study_type": "Replicação conceitual experimental, com dados próprios",
   "method": "Jogo Cat Park, com cinco técnicas de manipulação e desinformação multimodal, avaliado antes e depois do jogo",
   "sample_size": "N = 380",
   "main_finding": "Quem jogou Cat Park achou a desinformação menos confiável e ficou menos disposto a compartilhá-la, mas não ficou significativamente mais confiante.",
   "abstract_quote": "people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001)"
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
   "study_type": "Desenho experimental em salas de aula reais, com seguimento de três meses",
   "method": "Três tipos de intervenção: prebunking com o jogo Bad News, oficina de checagem News Evaluator (não é jogo) e intervenções de letramento disciplinar (não são jogos)",
   "sample_size": "459 students",
   "main_finding": "Nem o jogo Bad News nem a oficina News Evaluator melhoraram significativamente a capacidade dos estudantes de avaliar notícias confiáveis e enganosas.",
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
   "study_type": "Estudo experimental com quem jogou e quem não jogou, replicado em duas amostras (o resumo não diz se a alocação foi aleatória)",
   "method": "Jogo de computador sobre fake news desenvolvido em Singapura, com base na teoria da inoculação",
   "sample_size": "college (n = 84) and junior high and secondary school (n = 30) students",
   "main_finding": "Quem jogou teve pontuação maior na detecção de fake news do que quem não jogou, e também melhorou em percepção de ameaça, ceticismo e cautela diante de informação online.",
   "abstract_quote": "We also found that those who played the game scored higher in detecting fake news than those who did not play the game"
  },
  {
   "doi": "10.1007/s10758-024-09749-y",
   "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2024,
   "venue": "Technology, Knowledge and Learning",
   "study_type": "Estudo de campo com desenho pré e pós-teste (sem grupo de controle)",
   "method": "Escape game em realidade aumentada (Escape Fake) para educação midiática",
   "sample_size": "A total of 28 students (14 girls, mean age = 14.71 years)",
   "main_finding": "O Escape Fake atingiu quatro objetivos de aprendizagem relevantes para detectar fake news, com maior efeito na aquisição de conhecimento (d = 1,34).",
   "abstract_quote": "The results show that Escape Fake can address four learning objectives relevant in fake news detection with educationally desired effect sizes: Knowledge acquisition (d = 1.34), ability to discern information (d = 0.39), critical attitude toward trustworthiness of online information (d = 0.53), and confidence in recognizing fake news in the future (d = 0.41)."
  },
  {
   "doi": "10.21240/mpaed/51/2023.01.12.x",
   "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News",
   "authors": [
    "Josef Buchner"
   ],
   "year": 2023,
   "venue": "MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung",
   "study_type": "Estudo-piloto com desenho pré e pós-teste (sem grupo de controle)",
   "method": "Escape game em realidade aumentada (Escape Fake) com estudantes",
   "sample_size": "27 Schüler:innen",
   "main_finding": "O jogo Escape Fake conseguiu transmitir conhecimento sobre fake news, promover a capacidade de reconhecer a confiabilidade das informações e reforçar a confiança em reconhecer fake news no futuro.",
   "abstract_quote": "Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln, die Fähigkeit fördern, die Zuverlässigkeit von Informationen zu erkennen, zu einer kritischeren Haltung gegenüber der Vertrauenswürdigkeit von Onlineinformationen beitragen sowie die Zuversicht stärken, auch in Zukunft Fake News zu erkennen."
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
   "study_type": "Estudo de campo randomizado (teste-piloto)",
   "method": "Jogo em que os participantes criam uma notícia falsa assumindo a perspectiva de diferentes produtores de fake news, testado em uma escola de ensino médio pública",
   "sample_size": "N = 95",
   "main_finding": "Jogar o jogo reduziu a confiabilidade percebida e a persuasão de artigos de fake news, como evidência preliminar.",
   "abstract_quote": "To pilot test the efficacy of the game, we conducted a randomized field study (N = 95) in a public high school setting. Results provide some preliminary evidence that playing the fake news game reduced the perceived reliability and persuasiveness of fake news articles."
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
   "study_type": "Estudo de campo online randomizado, com avaliação complementar de usabilidade em uma turma",
   "method": "Serious game MAthE, em que os jogadores classificam notícias como falsas ou reais usando ferramentas de verificação",
   "sample_size": "n = 111 (estudo de campo online); n = 35 (discussão em turma de mídia)",
   "main_finding": "O jogo pode aumentar a conscientização e ensinar ferramentas de autenticação de notícias, como evidência preliminar.",
   "abstract_quote": "Specifically, it is validated that the game can raise awareness, teach about authentication tools, and highlight the importance of patterns that include evidence regarding the authenticity of articles."
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
   "study_type": "Experimento escolar com medidas pré e pós",
   "method": "Comparação entre intervenção ativa (jogo online) e passiva (folheto), ambas de inoculação baseada em lógica",
   "sample_size": "373 participants",
   "main_finding": "A diversão foi maior com o jogo, sem diferença de desempenho entre as duas intervenções; os alunos melhoraram na identificação de notícias falsas, mas pioraram na de notícias reais.",
   "abstract_quote": "Findings show that enjoyment was significantly higher in the active intervention group compared to the passive one."
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
   "study_type": "Dois estudos online experimentais",
   "method": "Jogo Bad News, com itens diferentes no pré e no pós-teste e delineamento de três grupos de Solomon",
   "sample_size": "total N = 2,159",
   "main_finding": "Os efeitos de inoculação sofrem alguma influência dos itens, mas não de efeitos de teste; o jogo melhora a capacidade de identificar técnicas de desinformação e não torna as pessoas mais céticas diante de notícias reais.",
   "abstract_quote": "We show that inoculation interventions are effective at improving people’s ability to spot misinformation techniques and that the Bad News game does not make people more skeptical of real news."
  }
 ],
 "search_notes": "Escolhi 23 artigos, todos da lista aprovada, que só tinha 23. Faltam 2 para chegar aos 25 pedidos, e não incluí artigos fora da lista aprovada.\n\nComo conferi: abri os resumos nas páginas de Crossref, Europe PMC, Semantic Scholar, no repositório de Cambridge, no HKS Misinformation Review, no CEDTECH e no iJIM. A ferramenta de leitura devolveu os resumos em trechos curtos. Por isso os trechos de abstract_quote são cópias literais desses trechos, e alguns juntam trechos contíguos do resumo.\n\nCorreção da reprovação anterior: no artigo 10.1080/13669877.2018.1443491 (Roozenbeek & van der Linden, 2018), o abstract_quote agora traz a frase do estudo de campo (N = 95) e a frase do resultado, completas e literais. O resumo menciona a crise de refugiados europeia como tema \"politicizado\", mas o foco é a produção de fake news, e não política partidária. Por isso mantive o artigo.\n\nPontos que não consegui confirmar ou que merecem atenção:\n- 10.1016/j.compedu.2023.104832 (Barzilai et al.): o resumo que recuperei era um conjunto de trechos selecionados e não trazia os tamanhos de amostra. \"N = 84 and N = 131\" vem da lista de candidatos aprovados e não foi reconferido no resumo oficial. O trecho citado é literal.\n- 10.1057/s41599-019-0279-9: o resumo no Crossref mostra \"N = 15,000\", o que resolve a dúvida sobre o formato.\n- 10.37016//mr-2020-008: o DOI com barra dupla é o do registro oficial. O resumo não informa amostra. A seção \"Essay Summary\" do artigo cita n = 5.061, mas ela não faz parte do resumo, então marquei \"não informado no resumo\".\n- 10.1037/xge0001603 (Leder et al.): um dos jogos, Harmony Square, é de desinformação política. O foco do estudo é o efeito do feedback e o Bad News predomina. Os experimentos 3 a 6 são quase-experimentais, em pesquisas dentro do jogo.\n- Intervenções que não são jogos: Hu et al. (braço gráfico), Reinhardt et al. (folheto) e Nygren & Efimova (oficina News Evaluator e intervenções de letramento disciplinar) incluem essas intervenções ao lado do jogo. O jogo é a intervenção principal ou um dos braços avaliados, e o achado e o trecho tratam o jogo.\n- 10.5209/esmp.88599 (Tandoc & Seet): o resumo não diz se a alocação foi aleatória.\n- 10.5334/joc.324 (Graham et al.): o Europe PMC lista o tipo como \"research-article; News\". Os dados são próprios (quatro replicações), então não é reanálise.\n- Buchner (2023, alemão; 2024, Technology, Knowledge and Learning) e Buchner & Höfler (2024): amostras diferentes (27, 28 e 45), mas o mesmo jogo, Escape Fake.\n- Ano: Roozenbeek & van der Linden saiu online em 2018 e no fascículo de 2019. Axelsson et al. saiu online em 2024 e no fascículo de 2025. Ambos estão dentro do período.\n- Na maioria dos artigos o período de 2018 a 2025 e o tipo de periódico vêm dos metadados do Crossref. Não reconferi cada um, e o único desvio que notei foi o Graham et al. (acima)."
}