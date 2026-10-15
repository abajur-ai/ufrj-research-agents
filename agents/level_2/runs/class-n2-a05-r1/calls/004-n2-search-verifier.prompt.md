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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2019 e 2025, sobre como as pessoas percebem, detectam ou avaliam a credibilidade de imagens, vídeos e áudios sintéticos gerados por inteligência artificial (deepfakes, rostos sintéticos e clones de voz). Restrições: apenas estudos empíricos com participantes humanos (experimentos, testes de detecção, surveys ou medidas fisiológicas); exclua artigos sobre algoritmos de detecção automática, estudos centrados em políticos, eleições ou propaganda política e estudos sobre saúde. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CANDIDATOS A VERIFICAR:
{
 "candidates": [
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.isci.2021.103364&resultType=core&format=json",
   "criteria_met": [
    "Tema: detecção humana de vídeos deepfake e superconfiança",
    "Período 2021; artigo de periódico (Crossref journal-article)",
    "Tipo de estudo e método: experimento comportamental online pré-registrado",
    "Amostra: N = 210",
    "Achado principal: as pessoas não detectam deepfakes de forma confiável, tendem a tomá-los por autênticos e superestimam a própria capacidade",
    "Trecho literal: \"people cannot reliably detect deepfakes and (2) neither raising awareness nor introducing financial incentives improves their detection accuracy\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1073/pnas.2120481119",
   "title": "AI-synthesized faces are indistinguishable from real faces and more trustworthy",
   "authors": [
    "Sophie J. Nightingale",
    "Hany Farid"
   ],
   "year": 2022,
   "venue": "Proceedings of the National Academy of Sciences",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2120481119&resultType=core&format=json",
   "criteria_met": [
    "Tema: rostos sintéticos (StyleGAN2): fotorrealismo, detecção e confiabilidade percebida",
    "Período 2022; artigo de periódico (Crossref journal-article; Europa PMC o classifica como brief report)",
    "Tipo de estudo e método: experimentos comportamentais com avaliadores humanos (detecção e notas de confiabilidade). O detalhe do desenho vem de fonte secundária, não do resumo",
    "Amostra: não informado no resumo",
    "Achado principal: rostos sintetizados por IA são indistinguíveis de rostos reais e mais confiáveis",
    "Trecho literal: \"have passed through the uncanny valley and are capable of creating faces that are indistinguishable-and more trustworthy-than real faces\" (os hifens estão como no registro do Europa PMC; no original podem ser travessões)",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1177/09567976231207095&resultType=core&format=json",
   "criteria_met": [
    "Tema: julgamento de rostos de IA versus rostos humanos (hiper-realismo)",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: dois experimentos com participantes, mais reanálise de dados publicados",
    "Amostra: N = 124 adults (Experimento 1); N = 610 adults (Experimento 2)",
    "Achado principal: rostos de IA brancos são julgados humanos com mais frequência que rostos humanos reais, e os participantes mais confiantes erraram mais",
    "Trecho literal: \"White AI faces are judged as human more often than actual human faces\"",
    "Sem foco em algoritmo (o aprendizado de máquina é apenas auxiliar), política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1371/journal.pone.0285333&resultType=core&format=json",
   "criteria_met": [
    "Tema: detecção humana de áudio deepfake de fala",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: experimento de detecção com ouvintes, em inglês e mandarim, com e sem exemplos de treino",
    "Amostra: n = 529 individuals",
    "Achado principal: os ouvintes só identificaram os deepfakes de fala em 73% das vezes, e os exemplos ajudaram pouco",
    "Trecho literal: \"Listeners only correctly spotted the deepfakes 73% of the time\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41598-025-94170-3&resultType=core&format=json",
   "criteria_met": [
    "Tema: clones de voz de IA, correspondência de identidade e naturalidade percebidas",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: série de estudos perceptivos com participantes",
    "Amostra: não informado no resumo",
    "Achado principal: os participantes não identificam de forma consistente vozes geradas por IA",
    "Trecho literal: \"We find human participants cannot consistently identify recordings of AI-generated voices.\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2110013119&resultType=core&format=json",
   "criteria_met": [
    "Tema: detecção humana de vídeos deepfake, comparada à de um modelo",
    "Período 2022; artigo de periódico",
    "Tipo de estudo e método: dois estudos online, incluindo intervenções randomizadas pré-registradas",
    "Amostra: 15,016 participants",
    "Achado principal: observadores humanos e o modelo líder têm acurácia semelhante, mas erram de modos diferentes",
    "Trecho literal: \"We compare the performance of ordinary human observers with the leading computer vision deepfake detection model and find them similarly accurate, while making different kinds of mistakes.\"",
    "O participante humano é a unidade central; o modelo é só comparador"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.3390/brainsci13091233&resultType=core&format=json",
   "criteria_met": [
    "Tema: processamento neural de rostos reais versus deepfake",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: EEG seco de 21 canais (espectro de potência e ERP) em tarefa de discriminação visual",
    "Amostra: 23 healthy participants",
    "Achado principal: o EEG distingue rostos reais de deepfake, com N250 de latência menor para rostos reais",
    "Trecho literal: \"ERP analysis hinted at the possibility of discriminating between real and synthetic faces\"",
    "Participantes saudáveis não tornam o estudo da área de saúde; sem foco em algoritmo ou política"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.visres.2022.108079&resultType=core&format=json",
   "criteria_met": [
    "Tema: rostos gerados por IA, respostas comportamentais e neurais",
    "Período 2022; artigo de periódico",
    "Tipo de estudo e método: comportamento mais imagem cerebral (decodificação de atividade neural)",
    "Amostra: não informado no resumo",
    "Achado principal: dá para decodificar rostos de IA pela atividade neural, mas no comportamento as pessoas ficam perto do acaso",
    "Trecho literal: \"while at a group level people performed near chance classifying real and realistic fakes\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s42003-024-06372-6&resultType=core&format=json",
   "criteria_met": [
    "Tema: clones de voz deepfake e aceitação ou rejeição de identidade",
    "Período 2024; artigo de periódico",
    "Tipo de estudo e método: tarefa de correspondência de identidade com neuroimagem (análises univariadas e multivariadas)",
    "Amostra: 25 participants",
    "Achado principal: os humanos são parcialmente enganados por vozes deepfake, e uma rede córtico-estriatal decodifica o nível de deepfake",
    "Trecho literal: \"participants show intermediate performance with deepfake voices, indicating levels of deception and resistance to deepfake identity spoofing\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41598-023-42802-x&resultType=core&format=json",
   "criteria_met": [
    "Tema: efeito da crença de que o rosto é deepfake sobre a percepção e a avaliação",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: experimento com EEG (ERP) e escalas de avaliação",
    "Amostra: (N = 30)",
    "Achado principal: sorrisos presumidos como falsos parecem menos positivos e geram avaliação mais lenta e processamento emocional atenuado",
    "Trecho literal: \"Smiling faces marked as fake appeared less positive, as reflected in expression ratings, and induced slower evaluations.\"",
    "Ressalva: os rostos eram reais, apenas rotulados como falsos; o tema é a percepção de mídia presumida como sintética",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1371/journal.pone.0332692",
   "title": "Voice clones sound realistic but not (yet) hyperrealistic",
   "authors": [
    "Nadine Lavan",
    "Michael Irvine",
    "Victor Rosi",
    "Carolyn McGettigan"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1371/journal.pone.0332692&resultType=core&format=json",
   "criteria_met": [
    "Tema: realismo, discriminação e traços sociais (confiabilidade e dominância) de vozes geradas por IA",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: experimentos de percepção com ouvintes humanos",
    "Amostra: não informado no resumo",
    "Achado principal: clones de voz soam tão reais quanto vozes humanas, mas não há efeito de hiper-realismo",
    "Trecho literal: \"We find that voice clones can sound as real as human voices, making it difficult for listeners to distinguish between them.\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1098/rsos.250921",
   "title": "Training human super-recognizers' detection and discrimination of AI-generated faces",
   "authors": [
    "Katie L. H. Gray",
    "Josh P. Davis",
    "Charlotte Bunce",
    "Eilidh Noyes",
    "Kay L. Ritchie"
   ],
   "year": 2025,
   "venue": "Royal Society Open Science",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1098/rsos.250921&resultType=core&format=json",
   "criteria_met": [
    "Tema: detecção e discriminação humana de rostos sintéticos de GAN, com treino",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: dois desenhos experimentais com super-reconhecedores e controles, com treino sobre artefatos de renderização",
    "Amostra: SRs (total N = 283) e controls (total N = 381)",
    "Achado principal: super-reconhecedores detectam rostos sintéticos melhor que os controles, e o treino melhora o desempenho em ambos os grupos",
    "Trecho literal: \"we found that SRs (total N = 283) were better at detecting and discriminating synthetic faces than controls (total N = 381)\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.3390/e27080868",
   "title": "Are Human Judgments of Real and Fake Faces Quantum-like Contextual?",
   "authors": [
    "Peter Bruza",
    "Alexandra Lee",
    "Patrick Hoyte"
   ],
   "year": 2025,
   "venue": "Entropy",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.3390/e27080868&resultType=core&format=json",
   "criteria_met": [
    "Tema: julgamento humano de qual de dois rostos (um real, um gerado por IA) é falso",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: experimento de crowdsourcing em pares com análise Contextuality-by-Default",
    "Amostra: não informado no resumo",
    "Achado principal: nove de 20 tentativas mostraram contextualidade tipo quântica, e comparar com exemplares reais conhecidos pode melhorar a detecção",
    "Trecho literal: \"bootstrap resampling (10,000 iterations per coin) revealed that nine trials demonstrated quantum-like contextuality\"",
    "Ressalva: enquadramento teórico incomum, mas há coleta própria e a tarefa é de detecção humana",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.3389/frai.2025.1707336",
   "title": "What you see is not what you get anymore: a mixed-methods approach on human perception of AI-generated images",
   "authors": [
    "Merlin Högemann",
    "Jan Betke",
    "Oliver Thomas"
   ],
   "year": 2025,
   "venue": "Frontiers in Artificial Intelligence",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.3389/frai.2025.1707336&resultType=core&format=json",
   "criteria_met": [
    "Tema: percepção e detecção humana de imagens geradas por IA (paisagens, arquitetura, interiores)",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: survey online com classificação de 50 imagens, confiança e justificativas; métodos mistos",
    "Amostra: A total of 104 participants",
    "Achado principal: os participantes identificaram corretamente as imagens de IA em 63,7% dos casos, com superconfiança em grupos mais experientes",
    "Trecho literal: \"participants correctly identified AI-generated images in 63.7% of cases overall\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1016/j.actpsy.2024.104670",
   "title": "Too beautiful to be fake: Attractive faces are less likely to be judged as artificially generated",
   "authors": [
    "Dominique Makowski",
    "An Shu Te",
    "Aurélie Neves",
    "Stephanie Kirk",
    "Nuoyi Zoe Liang",
    "Panagiotis Mavros",
    "S. H. Annabel Chen"
   ],
   "year": 2025,
   "venue": "Acta Psychologica",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.actpsy.2024.104670&resultType=core&format=json",
   "criteria_met": [
    "Tema: crença de que um rosto é real ou gerado por IA",
    "Período 2025 (Europa PMC); artigo de periódico",
    "Tipo de estudo e método: experimento com avaliações de 109 rostos e julgamento de real ou falso com confiança",
    "Amostra: 150 participants",
    "Achado principal: rostos avaliados como mais atraentes tendem a ser classificados como mais reais",
    "Trecho literal: \"with faces rated as more attractive being classified as more real\"",
    "Ressalva: todos os rostos eram fotos reais, apresentadas como possivelmente geradas por IA",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.3390/jimaging11070227&resultType=core&format=json",
   "criteria_met": [
    "Tema: identificação da origem, realismo e credibilidade de imagens de IA versus imagens feitas por humanos",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: experimento com 24 imagens de IA e 8 humanas avaliadas por profissionais visuais e não profissionais",
    "Amostra: 161 participants",
    "Achado principal: imagens humanas são vistas como mais realistas e mais críveis do que as de IA, e as pessoas não identificam bem a origem",
    "Trecho literal: \"human-made images are perceived as both more realistic and more credible than AI-generated ones\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1016/j.isci.2022.105441",
   "title": "On the realness of people who do not exist: The social processing of artificial faces",
   "authors": [
    "Rebecca Tucciarelli",
    "Nikola Vehar",
    "Shabnam Chandaria",
    "Manos Tsakiris"
   ],
   "year": 2022,
   "venue": "iScience",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.isci.2022.105441&resultType=core&format=json",
   "criteria_met": [
    "Tema: julgamentos de realidade de rostos GAN e consequências sociais (conformidade e confiança social)",
    "Período 2022; artigo de periódico",
    "Tipo de estudo e método: três estudos comportamentais",
    "Amostra: não informado no resumo",
    "Achado principal: rostos GAN foram percebidos como reais mais vezes que rostos reais, e saber da existência deles reduziu a confiança social",
    "Trecho literal: \"GAN faces were more likely to be perceived as real than REAL faces\"",
    "Caso limítrofe: o resumo cita propaganda política só como exemplo de uso de rostos GAN; o foco não é político",
    "Sem foco em algoritmo ou saúde"
   ]
  },
  {
   "doi": "10.1089/cyber.2020.0149",
   "title": "Deepfakes Unmasked: The Effects of Information Priming and Bullshit Receptivity on Deepfake Recognition and Sharing Intention",
   "authors": [
    "Serena Iacobucci",
    "Roberta De Cicco",
    "Francesca Michetti",
    "Riccardo Palumbo",
    "Stefano Pagliaro"
   ],
   "year": 2021,
   "venue": "Cyberpsychology, Behavior, and Social Networking",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1089/cyber.2020.0149&resultType=core&format=json",
   "criteria_met": [
    "Tema: reconhecimento de vídeos deepfake e intenção de compartilhar",
    "Período 2021; artigo de periódico",
    "Tipo de estudo e método: experimento randomizado com priming de informação e mediação serial",
    "Amostra: não informado no resumo",
    "Achado principal: o priming sobre deepfakes melhora o reconhecimento só em pessoas com menor receptividade a conversa fiada (bullshit receptivity)",
    "Trecho literal: \"Results indicate that the development of strategies to counter the deceitfulness of DFs from an educational and cultural perspective might work well, but only for people with a lower susceptibility to believe willfully misleading claims.\"",
    "O resumo não indica tema político ou de saúde; o conteúdo dos vídeos não foi checado no texto integral"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1098/rsos.231214&resultType=core&format=json",
   "criteria_met": [
    "Tema: alerta e capacidade de detectar um deepfake de alta qualidade entre vídeos",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: experimento com grupo controle e grupo com aviso de conteúdo",
    "Amostra: não informado no resumo",
    "Achado principal: sem aviso, a detecção não difere do controle, e com aviso só uma minoria identifica o deepfake",
    "Trecho literal: \"only 21.6% of respondents correctly identify the deepfake as the only inauthentic video\"",
    "Conteúdo do vídeo descrito como neutro; sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://researchonline.jcu.edu.au/79985",
   "criteria_met": [
    "Tema: detecção humana de vídeos deepfake e confiança",
    "Período 2023 (Crossref); artigo de periódico (Crossref journal-article); resumo lido no repositório JCU, pois o Crossref não traz resumo",
    "Tipo de estudo e método: experimento online pré-registrado com intervenção de estratégias de detecção versus controle",
    "Amostra: N = 454",
    "Achado principal: a lista de estratégias não alterou a acurácia nem a confiança, e a acurácia média ficou em 60,70%",
    "Trecho literal: \"The detection strategies intervention did not impact detection accuracy or detection confidence\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
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
   "checked_url": "https://academic.oup.com/cybersecurity/article/9/1/tyad011/7205694",
   "criteria_met": [
    "Tema: detecção humana de rostos StyleGAN2",
    "Período 2023 (Crossref: issued 2023-01-01, online em 23/06/2023); artigo de periódico",
    "Tipo de estudo e método: survey online com quatro grupos aleatórios (controle e três intervenções) e confiança",
    "Amostra: participants (N = 280)",
    "Achado principal: a acurácia ficou pouco acima do acaso, nenhuma intervenção ajudou e a confiança foi alta e não relacionada ao acerto",
    "Trecho literal: \"Overall detection accuracy was only just above chance and none of the interventions significantly improved this.\"",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1016/j.tele.2023.102093",
   "title": "Conspiracy thinking and social media use are associated with ability to detect deepfakes",
   "authors": [
    "Ewout Nas",
    "Roy de Kleijn"
   ],
   "year": 2024,
   "venue": "Telematics and Informatics",
   "checked_url": "https://www.universiteitleiden.nl/en/research/research-output/social-and-behavioural-sciences/nas--de-kleijn-conspiracy-thinking-and-social-media-use-are-associated-with-ability-to-detect-deepfakes",
   "criteria_met": [
    "Tema: preditores do desempenho humano em reconhecer vídeos deepfake",
    "Período: Crossref registra issued 2024-03 (vol. 87); o repositório de Leiden indica 2023. Divergência anotada, ano final 2024",
    "Tipo de estudo e método: estudo empírico de detecção com preditores individuais; o desenho não é descrito no resumo",
    "Amostra: não informado no resumo",
    "Achado principal: humanos reconhecem melhor deepfakes de pessoas familiares, e o pensamento conspiratório e o uso de redes sociais se associam a melhor detecção",
    "Trecho literal: \"humans perform better at recognizing deepfake videos of familiar persons compared to deepfakes of unfamiliar persons\"",
    "DOI e metadados confirmados no Crossref; resumo lido no repositório de Leiden",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1016/j.chbah.2025.100143",
   "title": "Perception and social evaluation of cloned and recorded voices: Effects of familiarity and self-relevance",
   "authors": [
    "Victor Rosi",
    "Emma Soopramanien",
    "Carolyn McGettigan"
   ],
   "year": 2025,
   "venue": "Computers in Human Behavior: Artificial Humans",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.chbah.2025.100143?fields=title,abstract,year,venue,authors",
   "criteria_met": [
    "Tema: avaliação social (confiabilidade, atratividade, competência, dominância) de clones de voz",
    "Período 2025 (Crossref issued 2025-05); artigo de periódico (Crossref journal-article)",
    "Tipo de estudo e método: experimento de avaliação por ouvintes familiares e não familiares de clones e gravações",
    "Amostra: Forty-seven of these experimental participants (and 47 unfamiliar controls)",
    "Achado principal: ouvintes familiares julgam os clones iguais ou piores que as gravações, e os não familiares os julgam melhores",
    "Trecho literal: \"familiar listeners found clones to sound less (or similarly) trustworthy, attractive, and competent than recordings, unfamiliar listeners showed an opposing profile in which clones tended to be rated higher than recordings\"",
    "Metadados do Crossref; o resumo veio do Semantic Scholar, porque o Crossref e o site do periódico não o devolveram",
    "Sem foco em algoritmo, política ou saúde"
   ]
  },
  {
   "doi": "10.1186/s41235-025-00648-z",
   "title": "Specific media literacy tips improve AI-generated visual misinformation discernment",
   "authors": [
    "Sean Guo",
    "Briony Swire-Thompson",
    "Xiaoqing Hu"
   ],
   "year": 2025,
   "venue": "Cognitive Research: Principles and Implications",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1186/s41235-025-00648-z&resultType=core&format=json",
   "criteria_met": [
    "Tema: crença em desinformação visual gerada por IA e discernimento entre manchetes verdadeiras e falsas",
    "Período 2025; artigo de periódico",
    "Tipo de estudo e método: experimento randomizado pré-registrado com três condições (dicas específicas, gerais e controle)",
    "Amostra: não informado no resumo",
    "Achado principal: dicas específicas reduzem mais a crença em desinformação visual de IA do que dicas gerais",
    "Trecho literal: \"Both media literacy interventions reduced belief in AIVM compared to control, but specific tips reduced belief in AIVM more than general tips.\"",
    "Texto integral (PMC): manchetes sem conteúdo político ou de saúde; o resumo não informa o tamanho da amostra",
    "Sem foco em algoritmo"
   ]
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41598-023-39944-3&resultType=core&format=json",
   "criteria_met": [
    "Tema: capacidade de distinguir vídeos autênticos de deepfakes de ciência (mudança climática)",
    "Período 2023; artigo de periódico",
    "Tipo de estudo e método: survey com cinco populações (estudantes, educadores e público adulto), amostra representativa de três delas",
    "Amostra: não informado no resumo (o resumo cita five populations, sem número)",
    "Achado principal: 27% a 50% das pessoas não distinguem vídeos autênticos de deepfakes, e a vulnerabilidade aumenta com a idade e a confiança nas fontes",
    "Trecho literal: \"We found that 27-50% of individuals cannot distinguish authentic videos from deepfakes.\"",
    "Caso limítrofe: o resumo cita vacinas como exemplo de desinformação científica e orientação política como covariável; o estudo se ancora em mudança climática, não em saúde nem em política eleitoral"
   ]
  }
 ],
 "notes": "Entreguei 25 artigos (o pedido), todos com DOI, título, autores, ano e periódico conferidos nesta tentativa no Crossref, no Europa PMC ou na página do periódico. Os resumos foram lidos em trechos literais. A margem de 1,5x não foi usada de propósito: os demais candidatos não passaram em todos os critérios ou não pude verificá-los.\n\nComo verifiquei:\n- A API do OpenAlex devolveu HTTP 429 em todas as chamadas, então não foi usada. As consultas rodaram no Crossref, no Europa PMC (consulta por resumo, similar às do plano) e na busca na web. A SciELO não foi consultada.\n- Resumos por fonte: Somoray (repositório JCU), Nas (repositório de Leiden), Bray (página da OUP) e Rosi (Semantic Scholar). Para os demais, Europa PMC.\n- O ano da Nas diverge entre fontes: Crossref indica 2024-03 (vol. 87) e Leiden indica 2023. Registrei 2024.\n- A ferramenta de leitura só devolve trechos curtos, e o Europa PMC mostra alguns travessões como hífen. Em Nightingale & Farid o trecho está como o registro mostra (\"indistinguishable-and more trustworthy-than\"). Nos demais evitei trechos com travessão.\n\nCasos limítrofes, que vale decidir com cautela:\n- Eiserbeck (2023): os rostos eram reais, apenas rotulados como falsos.\n- Makowski (2025): todos os rostos eram reais, apresentados como possivelmente de IA.\n- Bruza (2025): enquadramento teórico quântico, mas há coleta própria e tarefa de detecção humana.\n- Tucciarelli (2022): o resumo cita propaganda política só como exemplo de uso de rostos GAN.\n- Doss (2023): deepfakes de ciência climática. O resumo cita vacinas como exemplo e orientação política como covariável.\n- Iacobucci (2021): o resumo não indica tema político ou de saúde, mas não li o conteúdo dos vídeos.\n- Guo (2025): consta no texto integral que as manchetes não eram políticas nem de saúde.\n- Groh (2022): compara humanos com um modelo, mas o participante humano é a unidade central.\n\nExcluídos por motivo verificado:\n- Ahmed & Chua (Heliyon 2023): o estímulo era um deepfake político de Putin.\n- Chow et al. (JEP: General), Farooq & de Vreese (AI & Society) e Stockner et al. (IJHCI): a versão final é de 2026.\n- Pehlivanoglu et al. (Cognitive Research), por ser de 2026.\n- Nat Commun 2024 (Groh et al.), por tratar de deepfakes políticos de fala.\n- Revisões e meta-análises (Somoray 2025 em Human Behavior and Emerging Technologies, Diel 2024).\n- Preprints: Frank et al., Cooke et al. e vários no PsyArXiv.\n- Anais: Müller 2022, Shen 2021 e Tahir 2021.\n- Napshin (2024), Becker (2024), López-Gil (2022) e Abraham (F1000, 2022), por não medirem detecção ou credibilidade, ou por não terem participantes.\n- Hwang (2021): não consegui confirmar se o vídeo era político.\n- Lago et al. (IEEE Signal Processing Magazine 2022): não confirmei a revisão por pares da seção.\n- Resumos de congresso publicados no Journal of Vision (Fosco, Josephs).\n\nLacuna: não achei artigo de periódico, 2019 a 2025, com rastreamento ocular sobre mídia sintética. O que apareceu era preprint ou resumo de congresso. Os anos de 2019 e 2020 ficaram sem artigos empíricos que passassem em todos os critérios; os artigos entregues vão de 2021 a 2025."
}