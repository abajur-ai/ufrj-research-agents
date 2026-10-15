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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2019 e 2025, sobre como as pessoas percebem, detectam ou avaliam a credibilidade de imagens, vídeos e áudios sintéticos gerados por inteligência artificial (deepfakes, rostos sintéticos e clones de voz). Restrições: apenas estudos empíricos com participantes humanos (experimentos, testes de detecção, surveys ou medidas fisiológicas); exclua artigos sobre algoritmos de detecção automática, estudos centrados em políticos, eleições ou propaganda política e estudos sobre saúde. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

LISTA FINAL A VERIFICAR:
{
 "items": [
  {
   "doi": "10.1073/pnas.2120481119",
   "title": "AI-synthesized faces are indistinguishable from real faces and more trustworthy",
   "authors": [
    "Sophie J. Nightingale",
    "Hany Farid"
   ],
   "year": 2022,
   "venue": "Proceedings of the National Academy of Sciences",
   "study_type": "Estudo empírico com participantes humanos (experimentos comportamentais)",
   "method": "Avaliação do fotorrealismo de rostos sintetizados por IA (GAN): classificação de rostos como reais ou sintéticos e avaliação de confiabilidade. Descrição detalhada além do resumo não verificada.",
   "sample_size": "não informado no resumo",
   "main_finding": "Rostos sintetizados por IA não são distinguíveis de rostos reais e são avaliados como mais confiáveis.",
   "abstract_quote": "synthesis engines have passed through the uncanny valley and are capable of creating faces that are indistinguishable"
  },
  {
   "doi": "10.1073/pnas.2110013119",
   "title": "Deepfake detection by human crowds, machines, and machine-informed crowds",
   "authors": [
    "Matthew Groh",
    "Ziv Epstein",
    "Chaz Firestone",
    "Rosalind Picard"
   ],
   "year": 2022,
   "venue": "Proceedings of the National Academy of Sciences",
   "study_type": "Dois estudos online com participantes humanos (detecção de deepfakes em vídeo; comparação humano vs. modelo)",
   "method": "Participantes viam vídeos autênticos e deepfakes e os classificavam, com e sem acesso à previsão de um modelo de visão computacional; manipulações que perturbam o processamento visual de rostos.",
   "sample_size": "15,016 participants",
   "main_finding": "Humanos e o modelo líder têm acurácia semelhante, mas erram de formas diferentes, e participantes com acesso à previsão do modelo são mais precisos que cada um isolado, embora previsões erradas do modelo muitas vezes reduzam a acurácia.",
   "abstract_quote": "Together, participants with access to the model's prediction are more accurate than either alone"
  },
  {
   "doi": "10.1371/journal.pone.0285333",
   "title": "Warning: Humans cannot reliably detect speech deepfakes",
   "authors": [
    "Kimberly T. Mai",
    "Sergi Bray",
    "Toby Davies",
    "Lewis D. Griffin"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "study_type": "Experimento com ouvintes (detecção de fala deepfake)",
   "method": "Áudio genuíno e deepfake apresentado a ouvintes em inglês e mandarim, com teste do efeito de exposição a exemplos de deepfake.",
   "sample_size": "n = 529 individuals",
   "main_finding": "Ouvintes identificaram corretamente os deepfakes de fala em apenas 73% das vezes, sem diferença entre idiomas, e a capacidade de detecção é pouco confiável.",
   "abstract_quote": "Listeners only correctly spotted the deepfakes 73% of the time"
  },
  {
   "doi": "10.1016/j.isci.2021.103364",
   "title": "Fooled twice: People cannot detect deepfakes but think they can",
   "authors": [
    "Nils C. Köbis",
    "Barbora Doležalová",
    "Ivan Soraperra"
   ],
   "year": 2021,
   "venue": "iScience",
   "study_type": "Experimento comportamental pré-registrado",
   "method": "Tarefa de detecção de vídeos deepfake com participantes humanos, avaliando também o efeito de conscientização e incentivos financeiros e a autoavaliação da habilidade.",
   "sample_size": "N = 210",
   "main_finding": "As pessoas não detectam deepfakes de forma confiável, tendem a julgá-los autênticos e superestimam a própria capacidade de detecção.",
   "abstract_quote": "In a pre-registered behavioral experiment (N = 210), we show that (1) people cannot reliably detect deepfakes"
  },
  {
   "doi": "10.1016/j.chb.2023.107917",
   "title": "Providing detection strategies to improve human detection of deepfakes: An experimental study",
   "authors": [
    "Klaire Somoray",
    "Dan J. Miller"
   ],
   "year": 2023,
   "venue": "Computers in Human Behavior",
   "study_type": "Experimento online pré-registrado",
   "method": "Participantes classificaram 20 vídeos como reais ou deepfake; um grupo recebeu lista de estratégias de detecção e outro serviu de controle.",
   "sample_size": "N = 454",
   "main_finding": "A acurácia ficou acima do acaso (60,70% em média), mas a lista de estratégias de detecção não alterou acurácia nem confiança.",
   "abstract_quote": "The sample performed above chance on the detection activity, correctly categorizing 60.70% of videos on average"
  },
  {
   "doi": "10.1038/s41598-025-94170-3",
   "title": "People are poorly equipped to detect AI-powered voice clones",
   "authors": [
    "Sarah Barrington",
    "Emily A. Cooper",
    "Hany Farid"
   ],
   "year": 2025,
   "venue": "Scientific Reports",
   "study_type": "Série de estudos perceptuais com participantes humanos (clones de voz)",
   "method": "Estudos perceptuais sobre o realismo de vozes geradas por IA (correspondência de identidade e naturalidade).",
   "sample_size": "não informado no resumo",
   "main_finding": "Participantes não conseguem identificar de forma consistente gravações de vozes geradas por IA e muitas vezes atribuem a elas a mesma identidade da voz real.",
   "abstract_quote": "We find human participants cannot consistently identify recordings of AI-generated voices."
  },
  {
   "doi": "10.1098/rsos.231214",
   "title": "Deepfake detection with and without content warnings",
   "authors": [
    "Andrew Lewis",
    "Patrick Vu",
    "Raymond M. Duch",
    "Areeq Chowdhury"
   ],
   "year": 2023,
   "venue": "Royal Society Open Science",
   "study_type": "Experimento com espectadores (detecção de deepfake em vídeo)",
   "method": "Espectadores viam um conjunto de vídeos com um deepfake de conteúdo neutro, com e sem aviso de que um dos cinco vídeos era falso.",
   "sample_size": "não informado no resumo",
   "main_finding": "Sem aviso, os espectadores notaram o deepfake tanto quanto o controle; com aviso, só 21,6% o identificaram corretamente como o único vídeo inautêntico.",
   "abstract_quote": "only 21.6% of respondents correctly identify the deepfake as the only inauthentic video"
  },
  {
   "doi": "10.1177/09567976231207095",
   "title": "AI Hyperrealism: Why AI Faces Are Perceived as More Real Than Human Ones",
   "authors": [
    "Elizabeth J. Miller",
    "Ben A. Steward",
    "Zak Witkower",
    "Clare A. M. Sutherland",
    "Eva G. Krumhuber",
    "Amy Dawel"
   ],
   "year": 2023,
   "venue": "Psychological Science",
   "study_type": "Dois experimentos com participantes adultos (julgamento de rostos como humanos ou IA)",
   "method": "Experimento 1 com reanálise de dados; Experimento 2 com teoria do espaço facial para identificar atributos faciais interpretados como sinal de humanidade.",
   "sample_size": "N = 124 adults (Experimento 1); N = 610 adults (Experimento 2)",
   "main_finding": "Rostos brancos gerados por IA são julgados como humanos mais vezes que rostos humanos reais (hiper-realismo da IA).",
   "abstract_quote": "White AI faces are judged as human more often than actual human faces"
  },
  {
   "doi": "10.1016/j.visres.2022.108079",
   "title": "Are you for real? Decoding realistic AI-generated faces from neural activity",
   "authors": [
    "Michoel L. Moshel",
    "Amanda K. Robinson",
    "Thomas A. Carlson",
    "Tijl Grootswagers"
   ],
   "year": 2022,
   "venue": "Vision Research",
   "study_type": "Estudo com medida fisiológica (EEG) e tarefa comportamental",
   "method": "Registro de atividade neural e julgamentos comportamentais de rostos reais e rostos realistas gerados por IA, com decodificação a partir do sinal neural.",
   "sample_size": "não informado no resumo",
   "main_finding": "A atividade neural permitiu decodificar de forma confiável rostos gerados por IA, embora o desempenho comportamental no nível do grupo ficasse próximo do acaso.",
   "abstract_quote": "We found that we could reliably decode AI generated faces using people's neural activity."
  },
  {
   "doi": "10.1371/journal.pone.0332692",
   "title": "Voice clones sound realistic but not (yet) hyperrealistic",
   "authors": [
    "Nadine Lavan",
    "Mairi Irvine",
    "Victor Rosi",
    "Carolyn McGettigan"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "study_type": "Experimento de percepção com ouvintes (clones de voz)",
   "method": "Ouvintes avaliaram realismo e traços sociais (dominância, confiabilidade) de vozes humanas, clones de voz e vozes geradas sem contraparte humana, para testar um efeito de hiper-realismo.",
   "sample_size": "não informado no resumo",
   "main_finding": "Clones de voz soam tão reais quanto vozes humanas, dificultando a distinção pelos ouvintes, mas sem efeito de hiper-realismo.",
   "abstract_quote": "voice clones can sound as real as human voices, making it difficult for listeners to distinguish between them"
  },
  {
   "doi": "10.1098/rsos.250921",
   "title": "Training human super-recognizers' detection and discrimination of AI-generated faces",
   "authors": [
    "Katie L. H. Gray",
    "Josh P. Davis",
    "Carl Bunce",
    "Eilidh Noyes",
    "Kay L. Ritchie"
   ],
   "year": 2025,
   "venue": "Royal Society Open Science",
   "study_type": "Dois experimentos de detecção/discriminação com e sem treino, comparando super-reconhecedores e controles",
   "method": "Participantes detectaram e discriminaram rostos sintéticos (GAN) antes e depois de um treino sobre artefatos de renderização.",
   "sample_size": "SRs (total N = 283); controls (total N = 381)",
   "main_finding": "Super-reconhecedores detectaram e discriminaram rostos sintéticos melhor que controles; o treino melhorou o desempenho de ambos os grupos.",
   "abstract_quote": "were better at detecting and discriminating synthetic faces than controls"
  },
  {
   "doi": "10.3389/frai.2025.1707336",
   "title": "What you see is not what you get anymore: a mixed-methods approach on human perception of AI-generated images",
   "authors": [
    "Malte Högemann",
    "Jonas Betke",
    "Oliver Thomas"
   ],
   "year": 2025,
   "venue": "Frontiers in Artificial Intelligence",
   "study_type": "Estudo de métodos mistos (survey quantitativo com análise qualitativa de justificativas)",
   "method": "Participantes classificaram 50 imagens (metade reais, metade geradas por cinco modelos texto-imagem), informaram confiança e justificaram as escolhas.",
   "sample_size": "A total of 104 participants",
   "main_finding": "Os participantes identificaram corretamente imagens geradas por IA em 63,7% dos casos, com detecção muito pior para as imagens de um dos modelos e sinais de má calibração da confiança.",
   "abstract_quote": "participants correctly identified AI-generated images in 63.7% of cases overall"
  },
  {
   "doi": "10.3390/brainsci13091233",
   "title": "Real and Deepfake Face Recognition: An EEG Study on Cognitive and Emotive Implications",
   "authors": [
    "Pietro Tarchi",
    "Maria Chiara Lanini",
    "Lorenzo Frassineti",
    "Antonio Lanatà"
   ],
   "year": 2023,
   "venue": "Brain Sciences",
   "study_type": "Estudo com medida fisiológica (EEG)",
   "method": "EEG (headset seco de 21 canais) durante tarefa de discriminação visual de rostos reais e deepfake com expressões positivas, negativas e neutras; análise de espectro de potência e potenciais relacionados a eventos.",
   "sample_size": "23 healthy participants",
   "main_finding": "Rostos reais produziram dominância do hemisfério direito, enquanto os deepfakes afetaram principalmente áreas frontais e occipitais na banda delta, e os potenciais sugerem que rostos reais e sintéticos podem ser diferenciados.",
   "abstract_quote": "deepfakes mainly affected the frontal and occipital areas in the delta band"
  },
  {
   "doi": "10.1038/s42003-024-06372-6",
   "title": "Cortical-striatal brain network distinguishes deepfake from real speaker identity",
   "authors": [
    "Claudia Roswandowitz",
    "Thayabaran Kathiresan",
    "Elisa Pellegrino",
    "Volker Dellwo",
    "Sascha Frühholz"
   ],
   "year": 2024,
   "venue": "Communications Biology",
   "study_type": "Estudo de neuroimagem funcional com participantes humanos",
   "method": "Participantes aceitaram ou rejeitaram identidades de falantes em vozes naturais e clones de voz deepfake de alta qualidade, com análise de padrões cerebrais.",
   "sample_size": "25 participants",
   "main_finding": "Humanos podem ser parcialmente enganados por vozes deepfake, e uma rede córtico-estriatal distingue voz deepfake de identidade de falante real.",
   "abstract_quote": "Humans can thus be partly tricked by deepfakes."
  },
  {
   "doi": "10.1093/cybsec/tyad011",
   "title": "Testing human ability to detect 'deepfake' images of human faces",
   "authors": [
    "Sergi D. Bray",
    "Shane D. Johnson",
    "Bennett Kleinberg"
   ],
   "year": 2023,
   "venue": "Journal of Cybersecurity",
   "study_type": "Survey/experimento online com grupos de intervenção randomizados",
   "method": "Participantes distinguiram rostos gerados por StyleGAN2 de fotos reais (FFHQ), divididos aleatoriamente em controle e três grupos com intervenções simples para melhorar a detecção.",
   "sample_size": "N = 280",
   "main_finding": "A acurácia geral ficou pouco acima do acaso e nenhuma das intervenções a melhorou significativamente.",
   "abstract_quote": "Overall detection accuracy was only just above chance and none of the interventions significantly improved this."
  },
  {
   "doi": "10.5771/2192-4007-2025-4-550",
   "title": "Spotting fakes: How do non-experts approach deepfake video detection?",
   "authors": [
    "Mary Holmes",
    "Klaire Somoray",
    "Jonathan D. Connor",
    "Darcy W. Goodall",
    "Lynsey Beaumont",
    "Jordan Bugeja",
    "Isabelle E. Eljed",
    "Sarah Sai Wan Ng",
    "Ryan Ede",
    "Dan J. Miller"
   ],
   "year": 2025,
   "venue": "SCM Studies in Communication and Media",
   "study_type": "Dois estudos empíricos: experimento online e estudo de laboratório com eye-tracking",
   "method": "Estudo 1: experimento online com grupo controle e grupo com lista de estratégias de detecção; Estudo 2: estudo de laboratório com rastreamento ocular.",
   "sample_size": "Study 1 (N = 391); Study 2 (N = 32)",
   "main_finding": "A acurácia de detecção foi modesta (cerca de .61–.65), as estratégias mudaram a atenção dos participantes sem melhorar a acurácia, e o olhar não diferiu entre vídeos reais e falsos.",
   "abstract_quote": "Study 2 found similar levels of detection accuracy (M = .65, SD = .20)."
  },
  {
   "doi": "10.1002/acp.4245",
   "title": "Crowds Improve Human Detection of AI-Synthesised Faces",
   "authors": [
    "Robin S. S. Kramer",
    "Charlotte Cartledge"
   ],
   "year": 2024,
   "venue": "Applied Cognitive Psychology",
   "study_type": "Dois experimentos com participantes humanos (detecção de rostos sintéticos)",
   "method": "Comparação de desempenho individual e agregado (multidões) na detecção de rostos sintetizados por IA.",
   "sample_size": "não informado no resumo",
   "main_finding": "Agregar os julgamentos de muitas pessoas melhora a detecção de rostos sintetizados por IA em relação ao desempenho individual.",
   "abstract_quote": "outer crowds as a robust method of improvement during synthetic face detection"
  },
  {
   "doi": "10.1186/s41235-025-00683-w",
   "title": "AI-generated images of familiar faces are indistinguishable from real photographs",
   "authors": [
    "Robin S. S. Kramer",
    "Alex L. Jones",
    "Daniel Fitousi",
    "Jeremy J. Tree"
   ],
   "year": 2025,
   "venue": "Cognitive Research: Principles and Implications",
   "study_type": "Quatro experimentos de discriminação com participantes humanos",
   "method": "Imagens de identidades fictícias e de celebridades geradas com ChatGPT/DALL·E comparadas a fotos reais, com fotos adicionais de comparação e efeito da familiaridade.",
   "sample_size": "não informado no resumo",
   "main_finding": "As imagens geradas, de identidades fictícias e de celebridades, não puderam ser distinguidas de fotos reais, com ganhos apenas limitados de fotos de comparação e da familiaridade.",
   "abstract_quote": "generated images of both fictional (Experiment 1) and celebrity identities (Experiment 2) could not be distinguished from real photographs"
  },
  {
   "doi": "10.1038/s41598-023-42802-x",
   "title": "Deepfake smiles matter less—the psychological and neural impact of presumed AI-generated faces",
   "authors": [
    "Anna Eiserbeck",
    "Martin Maier",
    "Julia Baum",
    "Rasha Abdel Rahman"
   ],
   "year": 2023,
   "venue": "Scientific Reports",
   "study_type": "Estudo com medida fisiológica (EEG) e avaliações psicológicas",
   "method": "EEG e avaliações de rostos reais com expressões positivas, neutras e negativas, informados aos participantes como reais ou deepfakes.",
   "sample_size": "N = 30",
   "main_finding": "Sorrisos presumidos como deepfake têm o processamento perceptual, emocional e avaliativo atenuado, o que não ocorre com expressões de raiva.",
   "abstract_quote": "Our findings demonstrate a dampening effect on perceptual, emotional, and evaluative processing of presumed deepfake smiles, but not angry expressions"
  },
  {
   "doi": "10.1177/14614448231199664",
   "title": "Assessing the perceived credibility of deepfakes: The impact of system-generated cues and video characteristics",
   "authors": [
    "Xinyi Jin",
    "Zhuoyue Zhang",
    "Bowen Gao",
    "Shuqing Gao",
    "Wenbo Zhou",
    "Nenghai Yu",
    "Guoyan Wang"
   ],
   "year": 2023,
   "venue": "New Media & Society",
   "study_type": "Dois experimentos randomizados 2×2×2",
   "method": "Experimentos manipulando pistas geradas pelo sistema (como seguidores da fonte e popularidade do vídeo) e características do vídeo (como definição) sobre a credibilidade percebida de deepfakes.",
   "sample_size": "N = 518",
   "main_finding": "Pistas do sistema, como o número de seguidores da fonte e a popularidade do vídeo, elevam a credibilidade percebida, e deepfakes em alta definição enganam mais os espectadores.",
   "abstract_quote": "high-definition deepfakes are more efficient at deceiving viewers"
  },
  {
   "doi": "10.3390/jimaging11070227",
   "title": "Interpretation of AI-Generated vs. Human-Made Images",
   "authors": [
    "Daniela Velásquez-Salamanca",
    "Miguel Ángel Martín-Pascual",
    "Celia Andreu-Sánchez"
   ],
   "year": 2025,
   "venue": "Journal of Imaging",
   "study_type": "Experimento de avaliação com participantes humanos",
   "method": "Profissionais visuais e não profissionais avaliaram 24 imagens geradas por IA (Midjourney, DALL·E, Firefly) e 8 feitas por humanos quanto à origem, realismo e credibilidade percebidos.",
   "sample_size": "161 participants—71 visual professionals and 90 non-professionals",
   "main_finding": "Imagens de IA foram frequentemente tomadas como feitas por humanos, e as imagens feitas por humanos foram percebidas como mais realistas e mais credíveis.",
   "abstract_quote": "We also find that human-made images are perceived as both more realistic and more credible than AI-generated ones."
  },
  {
   "doi": "10.3389/frai.2025.1568267",
   "title": "Training humans for synthetic face image detection",
   "authors": [
    "Ramlah Sara Rehman",
    "Ewald Meier",
    "Mathias Ibsen",
    "Christian Rathgeb",
    "Robert Nichols",
    "Christoph Busch"
   ],
   "year": 2025,
   "venue": "Frontiers in Artificial Intelligence",
   "study_type": "Experimento online com grupo experimental e grupo controle",
   "method": "Participantes detectaram imagens de rostos sintéticos; o grupo experimental recebeu treinamento durante a tarefa.",
   "sample_size": "we recruited 184 participants",
   "main_finding": "O treinamento melhora moderadamente a detecção humana de rostos sintéticos, mas o grupo treinado também classificou mais rostos autênticos como sintéticos.",
   "abstract_quote": "The study shows that training may moderately enhance human capabilities to detect synthetic face images."
  },
  {
   "doi": "10.1016/j.actpsy.2024.104670",
   "title": "Too beautiful to be fake: Attractive faces are less likely to be judged as artificially generated",
   "authors": [
    "Dominique Makowski",
    "An Shu Te",
    "Ana Neves",
    "Stephanie Kirk",
    "Ngoi Zi Liang",
    "Panagiotis Mavros",
    "S. H. Annabel Chen"
   ],
   "year": 2025,
   "venue": "Acta Psychologica",
   "study_type": "Experimento com avaliações de participantes humanos",
   "method": "Participantes avaliaram imagens de rostos em quatro características e julgaram se cada imagem era real ou falsa (gerada por IA), embora todas fossem rostos reais.",
   "sample_size": "150 participants rated 109 pictures of faces",
   "main_finding": "Rostos avaliados como mais atraentes foram classificados como reais com mais frequência, com efeito dependente do gênero, e muitos rostos reais foram chamados de falsos.",
   "abstract_quote": "Our results suggest a gender-dependent role of attractiveness on reality judgements, with faces rated as more attractive being classified as more real."
  },
  {
   "doi": "10.1016/j.isci.2022.105441",
   "title": "On the realness of people who do not exist: The social processing of artificial faces",
   "authors": [
    "Raffaele Tucciarelli",
    "Neza Vehar",
    "Shamil Chandaria",
    "Manos Tsakiris"
   ],
   "year": 2022,
   "venue": "iScience",
   "study_type": "Três estudos com participantes humanos",
   "method": "Participantes distinguiram rostos GAN de rostos reais e tiveram o comportamento social (conformidade, confiança) avaliado diante desses rostos.",
   "sample_size": "não informado no resumo",
   "main_finding": "Rostos GAN foram percebidos como reais com mais frequência que rostos reais, e saber da presença deles reduziu a confiança social.",
   "abstract_quote": "GAN faces were more likely to be perceived as real than REAL faces"
  },
  {
   "doi": "10.1038/s41598-023-39944-3",
   "title": "Deepfakes and scientific knowledge dissemination",
   "authors": [
    "Christopher Doss",
    "Jared Mondschein",
    "Dule Shu",
    "Tal Wolfson",
    "Denise Kopecky",
    "Valerie A. Fitton-Kane",
    "Lance Bush",
    "Conrad Tucker"
   ],
   "year": 2023,
   "venue": "Scientific Reports",
   "study_type": "Survey com participantes de cinco populações (estudantes, educadores, público adulto)",
   "method": "Survey em que os participantes distinguiam vídeos autênticos de deepfakes sobre mudança climática, com análise de idade, confiança nas fontes e exposição.",
   "sample_size": "não informado no resumo",
   "main_finding": "27–50% das pessoas não distinguem vídeos autênticos de deepfakes, e a vulnerabilidade aumenta com a idade e a confiança nas fontes.",
   "abstract_quote": "We found that 27–50% of individuals cannot distinguish authentic videos from deepfakes."
  }
 ],
 "search_notes": "Selecionei os 25 candidatos aprovados e não incluí nenhum artigo de fora da lista. Conferi cada trecho literal contra o resumo (Crossref, Europe PMC ou repositório do autor), e todos os 25 aparecem no resumo. O leitor de páginas não reproduz resumos inteiros, então confirmei cada trecho pedindo um sim/não sobre a frase exata e a amostra, não por cópia integral do resumo.\n\nCorreções feitas em relação à lista de candidatos:\n- Nomes de autores: usei os nomes do Crossref. Mudaram Högemann (Malte, Jonas), Lavan (Mairi Irvine, Victor Rosi), Rehman (Ramlah Sara, Ewald), Velásquez-Salamanca (Daniela), Kramer et al. 2025 (Alex L. Jones, Daniel Fitousi), Makowski et al., Miller et al. (Zak Witkower), Gray et al. (Carl Bunce) e Tucciarelli (Neza Vehar). Nos nomes de Makowski, o Crossref é a única fonte que consultei.\n- Groh et al.: o trecho do candidato estava sem o \"Together,\" inicial. O Crossref marca 2021 como ano de publicação online. Mantive 2022, ano do volume 119, nº 1.\n- Doss et al.: o resumo usa travessão \"27–50%\", não hífen. Usei o caractere do resumo.\n- Velásquez-Salamanca et al.: a amostra usa travessão (\"161 participants—71 …\"), não hífen.\n- Köbis, Eiserbeck, Jin e Tucciarelli: o HTML do resumo traz o \"N\" ou \"REAL\" em itálico. Os trechos estão em texto simples.\n- Holmes et al.: a amostra do Estudo 2 (N = 32) consta no resumo, conforme o Crossref.\n\nCasos sinalizados que mantive:\n- Tucciarelli: o resumo cita propaganda política só como implicação, e o enquadramento não é político.\n- Doss et al.: o estímulo são deepfakes sobre mudança climática. O resumo cita vacinas como exemplo e orientação política como moderador. Considero que o tema não é saúde nem político, mas o pesquisador pode excluir se preferir ser mais estrito.\n- Groh et al. e Rehman et al.: comparam humanos com um modelo ou treinam humanos, mas o foco é o desempenho humano, e não um algoritmo de detecção.\n- Nightingale/Farid, Moshel et al., Lewis et al., Barrington et al., Lavan et al., Kramer et al. (dois artigos) e Tucciarelli et al.: o resumo não informa a amostra, então ficou \"não informado no resumo\".\n\nOs campos de método e tipo de estudo vêm da leitura do resumo, que só consegui parafrasear. Detalhes além do resumo não foram verificados no texto completo."
}