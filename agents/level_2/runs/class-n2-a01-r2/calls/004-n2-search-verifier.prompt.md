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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre o efeito de influência continuada da informação falsa (continued influence effect), isto é, o quanto as pessoas continuam a se apoiar em uma informação falsa depois de ela ser corrigida ou retratada. Restrições: apenas experimentos com participantes humanos que meçam crença ou raciocínio depois de uma correção ou retratação; os materiais devem ser neutros (cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde); exclua estudos com desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CANDIDATOS A VERIFICAR:
{
 "candidates": [
  {
   "doi": "10.3758/s13421-021-01232-8",
   "title": "The role of discomfort in the continued influence effect of misinformation",
   "authors": [
    "Mark W. Susmann",
    "Duane T. Wegener"
   ],
   "year": 2022,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-021-01232-8%22&resultType=core&format=json (resumo e metadados); texto completo: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8447889/fullTextXML",
   "criteria_met": [
    "Tema CIE: sim (retratação e uso continuado da informação falsa)",
    "Ano oficial: 2022 (vol. 50, n. 2); online-first em 2021",
    "Tipo: artigo de periódico (Journal Article); dados próprios",
    "Tipo de estudo e método: 3 experimentos online com participantes humanos, com e sem retratação, medindo crença e uso da informação falsa (inferências)",
    "Materiais neutros: sim, conferido nos métodos: relato fictício de incêndio em depósito (os 3 estudos). Não há tema político nem de saúde nos estímulos; a vacina só aparece como exemplo na introdução",
    "Amostra: não informado no resumo (nos métodos: N = 186, 231 e 192 recrutados; não vale como N do resumo)",
    "Achado principal: as retratações geram desconforto psicológico, que prediz a crença e o uso continuados da informação falsa; reinterpretar o desconforto tornou a retratação mais eficaz",
    "Trecho literal do resumo: \"this discomfort predicts continued belief in and use of misinformation\""
   ]
  },
  {
   "doi": "10.3758/s13421-020-01129-y",
   "title": "Can you believe it? An investigation into the impact of retraction source credibility on the continued influence effect",
   "authors": [
    "Ullrich K. H. Ecker",
    "Luke M. Antonio"
   ],
   "year": 2021,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-020-01129-y%22&resultType=core&format=json ; texto completo: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7810102/fullTextXML",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2021 (vol. 49, n. 4)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 2 experimentos online com participantes humanos; credibilidade da fonte da retratação manipulada (confiabilidade x expertise); perguntas de inferência sobre relatos com retratação",
    "Materiais neutros: sim, conferido no texto completo: relatos fictícios em estilo de notícia (p. ex., mortes de peixes e poluição). Não são políticos nem de saúde",
    "Amostra: não informado no resumo (o resumo diz só 'In two experiments'; nos métodos N = 53 e N = 68)",
    "Achado principal: a confiabilidade da fonte, mas não a expertise, influencia a eficácia da retratação; retratações de fontes pouco confiáveis foram ineficazes",
    "Trecho literal do resumo: \"source trustworthiness but not source expertise indeed influences retraction effectiveness\""
   ]
  },
  {
   "doi": "10.3758/s13421-019-00967-9",
   "title": "Failure to accept retractions: A contribution to the continued influence effect",
   "authors": [
    "Andrea E. O'Rear",
    "Gabriel A. Radvansky"
   ],
   "year": 2020,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-019-00967-9%22&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (aceitação ou não da retratação)",
    "Ano oficial: 2020 (vol. 48, n. 1); online-first em 2019",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 3 experimentos com participantes humanos, com narrativas sobre um evento, retratação explícita e perguntas de inferência",
    "Materiais neutros: sim, narrativas fictícias de evento, sem tema político nem de saúde (o resumo fala em narrativa de evento)",
    "Amostra: não informado no resumo",
    "Achado principal: parte da influência continuada vem de pessoas que não aceitam a retratação; quem aceitou dependeu menos da informação incorreta",
    "Trecho literal do resumo: \"some people not accepting the retraction, even in the absence of external motivation to disregard it\""
   ]
  },
  {
   "doi": "10.3758/s13421-020-01046-0",
   "title": "Is it smart to read on your phone? The impact of reading format and culture on the continued influence of misinformation",
   "authors": [
    "Yi Xu",
    "Roslyn Wong",
    "Shuhan He",
    "Aaron Veldre",
    "Sally Andrews"
   ],
   "year": 2020,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-020-01046-0%22&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2020 (vol. 48, n. 7)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: experimento com participantes humanos (leitores de inglês e de chinês); leitura no celular x outro formato; informação crítica retratada ou não; medidas de memória e de inferência",
    "Materiais neutros: sim; o resumo descreve artigos curtos em estilo de jornal com uma informação crítica, sem tema político nem de saúde. O tema exato não é dado no resumo",
    "Amostra: não informado no resumo",
    "Achado principal: ler no celular reduziu a chance de o leitor notar a retratação e atualizar a memória; os leitores chineses sofreram mais influência continuada",
    "Trecho literal do resumo: \"reading on a mobile phone reduced the likelihood that readers noticed the retraction\""
   ]
  },
  {
   "doi": "10.3758/s13428-018-1066-z",
   "title": "Comparing the use of open and closed questions for Web-based measures of the continued-influence effect",
   "authors": [
    "Saoirse Connor Desai",
    "Stian Reimers"
   ],
   "year": 2019,
   "venue": "Behavior Research Methods",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13428-018-1066-z%22&resultType=core&format=json ; texto completo: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6538818/fullTextXML",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2019 (vol. 51, n. 3)",
    "Tipo: artigo de periódico, empírico (comparative study)",
    "Tipo de estudo e método: experimentos online com participantes humanos; relato com correção; comparação de perguntas abertas e fechadas para medir o CIE",
    "Materiais neutros: sim, conferido no texto completo: relato fictício de incêndio em depósito (15 mensagens), adaptado de Johnson & Seifert (1994)",
    "Amostra: \"We implemented this basic procedure online (Exp. 1A, n = 78)\"; \"a larger preregistered study (Exps. 2A and 2B, n = 323)\"",
    "Achado principal: os participantes continuaram a se referir à informação falsa depois da correção, tanto com perguntas abertas quanto com fechadas",
    "Trecho literal do resumo: \"Participants continued to refer to the misinformation following a correction\""
   ]
  },
  {
   "doi": "10.1186/s41235-021-00335-9",
   "title": "Exploring factors that mitigate the continued influence of misinformation",
   "authors": [
    "Irene P. Kan",
    "Kendra L. Pizzonia",
    "Anna B. Drummey",
    "Eric J. V. Mikkelsen"
   ],
   "year": 2021,
   "venue": "Cognitive Research: Principles and Implications",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1186/s41235-021-00335-9%22&resultType=core&format=json ; texto completo: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8627545/fullTextXML",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2021 (vol. 6, n. 1)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 3 experimentos online (1A, 1B e 2) com participantes humanos; oferta de explicação alternativa, centralidade da informação falsa e retratação",
    "Materiais neutros: sim, conferido no texto completo: relatos fictícios em mensagens curtas (acidente de micro-ônibus, roubo em residência, incêndio em lavanderia); sem conteúdo político nem de saúde",
    "Amostra: não informado no resumo (nos métodos: N usável = 248, 258 e 148)",
    "Achado principal: oferecer uma explicação alternativa reduziu de forma consistente o CIE nos experimentos",
    "Trecho literal do resumo: \"alternative provision consistently resulted in CIE reduction\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0267463",
   "title": "Vaccination against misinformation: The inoculation technique reduces the continued influence effect",
   "authors": [
    "Klara Austeja Buczel",
    "Paulina D. Szyszka",
    "Adam Siwiak",
    "Malwina Szpitalak",
    "Romuald Polczyk"
   ],
   "year": 2022,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0267463",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2022 (vol. 17, n. 4)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: experimento com participantes humanos; técnica de inoculação x controle; correção vinda de fonte mais ou menos confiável; medida de dependência da informação falsa em perguntas de inferência",
    "Materiais neutros: sim, em geral, conferido no texto completo: 6 cenários narrativos fictícios (água contaminada, roubo de joias, incêndio em depósito, escândalo no futebol, acidente de carro e demissão de um político). A fase de inoculação usou um debate fictício sobre uma substância na produção de alimentos. SINALIZAÇÃO: um dos 6 cenários envolve um político, mas é um relato fictício, não desinformação política real. O 'vaccination' do título é metáfora",
    "Amostra: não informado no resumo",
    "Achado principal: participantes inoculados dependeram menos da informação falsa quando a correção vinha de fonte muito confiável",
    "Trecho literal do resumo: \"inoculated participants relied on misinformation less when the correction came from a highly credible source\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0282202",
   "title": "Effective mitigation of the belief perseverance bias after the retraction of misinformation: Awareness training and counter-speech",
   "authors": [
    "Jana Siebert",
    "Johannes Ulrich Siebert"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282202 ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1371/journal.pone.0282202%22&resultType=core&format=json",
   "criteria_met": [
    "Tema: perseverança de crença depois da retratação de informação falsa (construto do CIE)",
    "Ano oficial: 2023 (vol. 18, n. 3; 8 mar 2023)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: experimento com participantes humanos; retratação de um estudo inventado e comparação de 3 técnicas de redução (counter-speech, treinamento de consciência e contra-explicação); medida de crença depois da retratação",
    "Materiais neutros: sim, conferido no texto completo: resumo inventado de um estudo sobre propensão ao risco e sucesso de bombeiros, tema de baixa relevância pessoal, sem conotação política nem de saúde",
    "Amostra: \"an experiment with N = 251 participants\"",
    "Achado principal: a técnica de counter-speech foi a mais eficaz para atenuar a perseverança da crença depois da retratação",
    "Trecho literal do resumo: \"The CS technique, with a very large effect size, is the most effective among the three techniques.\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0271566",
   "title": "Examining the role of information integration in the continued influence effect using an event segmentation approach",
   "authors": [
    "Jasmyne A. Sanderson",
    "Simon Farrell",
    "Ullrich K. H. Ecker"
   ],
   "year": 2022,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0271566",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2022 (vol. 17, n. 7)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 2 experimentos com participantes humanos; fronteira de evento (segmentação espacial, incluindo realidade virtual) entre a informação falsa e a retratação; medida do CIE",
    "Materiais neutros: sim, conferido no texto completo: cenários fictícios (p. ex., pouso de emergência de avião; assalto fictício a uma casa em realidade virtual). O caso MMR-autismo aparece só na introdução",
    "Amostra: não informado no resumo",
    "Achado principal: o Experimento 2 mostrou que uma fronteira de evento reduziu o CIE; o Experimento 1 não mostrou efeito",
    "Trecho literal do resumo: \"Experiment 2 yielded evidence that an event boundary resulted in a reduced CIE\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0283951",
   "title": "Executive function and the continued influence of misinformation: A latent-variable analysis",
   "authors": [
    "Paul McIlhiney",
    "Gilles E. Gignac",
    "Ullrich K. H. Ecker",
    "Blake L. Kennedy",
    "Michael Weinborn"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283951",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2023 (vol. 18, n. 4)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: estudo de diferenças individuais com participantes humanos; tarefa de CIE (8 relatos de evento, com informação crítica retratada ou não, e questionário de inferência) combinada com tarefas de função executiva; modelo de variáveis latentes",
    "Materiais neutros: sim; relatos de evento sobre causas de eventos (p. ex., mortes de peixes em um rio), sem tema político nem de saúde. O texto lido não diz explicitamente que são fictícios",
    "Amostra: não informado no resumo",
    "Achado principal: a função executiva, em especial a atualização da memória de trabalho, prediz a suscetibilidade ao CIE",
    "Trecho literal do resumo: \"Results showed that EF can predict susceptibility to the CIE, especially the factor of working-memory updating.\""
   ]
  },
  {
   "doi": "10.3389/fpsyg.2024.1487146",
   "title": "The inhibitory impact of collaboration on the continued influence effect of misinformation",
   "authors": [
    "Gongxiang Chen",
    "Yuxuan Zhong",
    "Sujie Li"
   ],
   "year": 2024,
   "venue": "Frontiers in Psychology",
   "checked_url": "https://www.frontiersin.org/articles/10.3389/fpsyg.2024.1487146/full",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2024 (vol. 15; 25 out 2024)",
    "Tipo: Original Research, empírico",
    "Tipo de estudo e método: 3 experimentos com participantes humanos; recordação colaborativa (revezamento x livre) depois de relatos com correção; questionário de inferência",
    "Materiais neutros: sim, conferido nos métodos: artigos fictícios em estilo de jornal adaptados de Ecker et al. (2017), 4 cenários (p. ex., incêndio atribuído a raios), sem conteúdo político nem de saúde",
    "Amostra: não informado no resumo (nos métodos: 48, 116 e 40 participantes analisados)",
    "Achado principal: a colaboração por revezamento mitigou de forma consistente o CIE; o efeito da colaboração livre dependeu do tempo de recordação",
    "Trecho literal do resumo: \"turn-taking collaboration consistently mitigates the CIE\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0322045",
   "title": "Did he or didn't he? Mixed evidence for the continued influence of retracted misinformation on person impressions",
   "authors": [
    "Amy J. Mickelberg",
    "Bradley Walker",
    "Ullrich K. H. Ecker",
    "Piers D. L. Howe",
    "Andrew Perfors",
    "Nicolas Fay"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0322045",
   "criteria_met": [
    "Tema CIE: sim (influência continuada de uma afirmação retratada sobre impressões)",
    "Ano oficial: 2025 (vol. 20, n. 5)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 3 experimentos com participantes humanos; impressão sobre uma pessoa fictícia a partir de afirmações de comportamento, com uma afirmação negativa retratada ou não",
    "Materiais neutros: sim, com SINALIZAÇÃO: pessoa fictícia e afirmações inventadas (exemplo: chutar um cachorro); sem tema político nem de saúde, mas a afirmação é negativa",
    "Amostra: não informado no resumo",
    "Achado principal: houve evidência de influência continuada da afirmação retratada em um experimento; nos outros dois ela foi totalmente descontada",
    "Trecho literal do resumo: \"Evidence for the continued influence of the retracted behaviour statement was found in one experiment\""
   ]
  },
  {
   "doi": "10.1525/collabra.92332",
   "title": "Does Mud Really Stick? No Evidence for Continued Influence of Misinformation on Newly Formed Person Impressions",
   "authors": [
    "Amy Mickelberg",
    "Bradley Walker",
    "Ullrich Ecker",
    "Piers D. L. Howe",
    "Andrew Perfors",
    "Nicolas Fay"
   ],
   "year": 2024,
   "venue": "Collabra: Psychology",
   "checked_url": "https://api.crossref.org/works/10.1525/collabra.92332 (metadados); https://api.semanticscholar.org/graph/v1/paper/DOI:10.1525/collabra.92332?fields=title,abstract,year,venue (resumo)",
   "criteria_met": [
    "Tema CIE: sim (retratação de informação falsa e impressões posteriores)",
    "Ano oficial: 2024 (vol. 10, n. 1; jan 2024)",
    "Tipo: artigo de periódico (journal-article), empírico",
    "Tipo de estudo e método: 4 experimentos com participantes humanos; impressão sobre o protagonista fictício 'John' a partir de descrições de comportamento, com uma retratada, de valência negativa ou positiva",
    "Materiais neutros: sim, com SINALIZAÇÃO: pessoa fictícia, sem tema político nem de saúde",
    "Amostra: não informado no resumo (o resumo cita só 4 experimentos)",
    "Achado principal: a informação falsa retratada foi totalmente descontada nas impressões, sem evidência de influência continuada",
    "Trecho literal do resumo (conferido apenas na API do Semantic Scholar; a página do editor retornou 403): \"fully discounted the misinformation once retracted\""
   ]
  },
  {
   "doi": "10.1016/j.jarmac.2020.08.003",
   "title": "Do false allegations persist? Retracted misinformation does not continue to influence explicit person impressions",
   "authors": [
    "Ullrich K. H. Ecker",
    "Arnold E. Rodricks"
   ],
   "year": 2020,
   "venue": "Journal of Applied Research in Memory and Cognition",
   "checked_url": "https://api.crossref.org/works/10.1016/j.jarmac.2020.08.003 (metadados); https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jarmac.2020.08.003?fields=title,abstract,year,venue,authors,publicationTypes (resumo)",
   "criteria_met": [
    "Tema CIE: sim (influência de alegações retratadas)",
    "Ano oficial: 2020 (vol. 9, n. 4; dez 2020)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: experimento com participantes humanos; comportamentos atribuídos a uma pessoa fictícia, com e sem alegação retratada; medidas de traços, previsão de comportamento e medida indireta (avaliação do rosto)",
    "Materiais neutros: sim, com SINALIZAÇÃO: pessoa fictícia; a alegação retratada é de violência doméstica, sem tema político nem de saúde, mas com carga emocional",
    "Amostra: não informado no resumo",
    "Achado principal: a desinformação desacreditada não influenciou as avaliações explícitas de traços nem as previsões de comportamento; houve evidência tentativa em uma medida indireta",
    "Trecho literal do resumo: \"Discredited misinformation was found to influence neither trait ratings of the person nor behavior predictions.\""
   ]
  },
  {
   "doi": "10.1016/j.cognition.2024.106000",
   "title": "Relative source credibility affects the continued influence effect: Evidence of rationality in the CIE",
   "authors": [
    "Carolin V. Hey",
    "Marie Luisa Schaper",
    "Ute J. Bayen"
   ],
   "year": 2025,
   "venue": "Cognition",
   "checked_url": "https://api.crossref.org/works/10.1016/j.cognition.2024.106000 ; https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.cognition.2024.106000?fields=title,abstract",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial: 2025 (vol. 254, jan 2025). O DOI tem '2024' porque saiu online em 2024",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: 2 experimentos com participantes humanos; credibilidade do informante e do retratador manipulada de forma independente; grupo controle sem a informação nem a retratação",
    "Materiais neutros: sim, conferido no resumo: notícia fictícia. O tema exato não é dado no resumo",
    "Amostra: \"In two experiments (N = 151, N = 146), informant credibility and retractor credibility were independently manipulated.\"",
    "Achado principal: quando o informante era menos crível que o retratador não houve CIE, o que é coerente com uma explicação racional; no Experimento 2 houve CIE também com fontes igualmente críveis",
    "Trecho literal do resumo: \"When the informant was less credible than the retractor, participants showed no CIE, in line with a rational account.\""
   ]
  },
  {
   "doi": "10.1002/acp.4214",
   "title": "Combating false information in military situations: Striking the right balance between continued influence effect and overcorrection",
   "authors": [
    "Victor Laurent",
    "Thierry Kosinski",
    "Stéphane Rusinek"
   ],
   "year": 2024,
   "venue": "Applied Cognitive Psychology",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.1002/acp.4214&select=DOI,title,author,issued,container-title,abstract",
   "criteria_met": [
    "Tema CIE: sim (testa o CIE e a supercorreção)",
    "Ano oficial: 2024 (vol. 38, n. 3)",
    "Tipo: artigo de periódico, empírico",
    "Tipo de estudo e método: experimento com participantes humanos; cenários militares com informação falsa corrigida; medidas de inferência e de tomada de decisão",
    "Materiais neutros: sim, com SINALIZAÇÃO: cenários militares fictícios, sem tema político, eleitoral, de vacinas, COVID-19 nem saúde. O contexto militar é de domínio específico",
    "Amostra: \"A total of 61 participants read four military scenarios\"",
    "Achado principal: não houve evidência de CIE, mas surgiu um efeito de supercorreção na tomada de decisão",
    "Trecho literal do resumo: \"The results did not reveal any evidence of the CIE, but an overcorrection effect emerged in decision‐making.\""
   ]
  },
  {
   "doi": "10.1016/j.actpsy.2023.104094",
   "title": "I know It's false, but I keep thinking as if it were true: A replication study of Johnson and Seifert's (1994) continued influence effect",
   "authors": [
    "Victor Laurent",
    "Thierry Kosinski",
    "Stéphane Rusinek"
   ],
   "year": 2023,
   "venue": "Acta Psychologica",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.actpsy.2023.104094?fields=title,abstract,year,venue ; https://api.crossref.org/works/10.1016/j.actpsy.2023.104094",
   "criteria_met": [
    "Tema CIE: sim (réplica direta de Johnson & Seifert, 1994)",
    "Ano oficial: 2023 (vol. 241, nov 2023)",
    "Tipo: artigo de periódico, empírico (replicação com dados próprios)",
    "Tipo de estudo e método: experimento entre grupos com participantes humanos francófonos; grupo com informação falsa retratada x controle sem a informação; inferências sobre o texto",
    "Materiais neutros: sim, conferido no resumo: o mesmo texto do estudo original, com informação falsa retratada ou ausente. Não há tema político nem de saúde; o tema do texto não é dado no resumo",
    "Amostra: \"comparing the inferences drawn by an FI group (n = 21) to those made by a control group (n = 23)\"",
    "Achado principal: os resultados confirmam os do estudo original; quem leu a informação falsa retratada fez mais inferências ligadas a ela",
    "Trecho literal do resumo: \"The results confirm those of the original study, supporting the validity of Johnson and Seifert's paradigm\""
   ]
  }
 ],
 "notes": "RESULTADO: entreguei 17 artigos, e não os 25 pedidos. Faltam 8. Entreguei só os que consegui conferir em todos os critérios, em vez de completar a lista.\n\nCOMO CONFERI. Abri os registros por Europe PMC (REST), Crossref, Semantic Scholar e PLOS/Frontiers. As páginas da Springer, Sage, ScienceDirect, Taylor & Francis, PMC e UC Press bloqueiam a leitura (403 ou loop de cookies). A API do OpenAlex devolveu 429, então não a usei. Todos os DOIs entregues foram abertos nesta tentativa e confirmados por título, autores, ano e periódico. Nenhum é preprint, revisão ou meta-análise.\n\nLIMITAÇÃO DOS TRECHOS. A ferramenta de leitura só devolve citações de até cerca de 125 caracteres. Por isso cada 'trecho literal' é um fragmento contínuo do resumo, e não a frase inteira. Os fragmentos de Mickelberg (Collabra) e de Ecker & Rodricks vêm de resumos lidos só pela API do Semantic Scholar, e confirmei os metadados deles no Crossref. Para Susmann & Wegener, Ecker & Antonio, O'Rear & Radvansky e Xu et al., o fragmento veio de um resumo lido por uma ferramenta intermediária. Convém conferi-lo no site do periódico.\n\nANOS. Usei o ano da edição final. Susmann & Wegener = 2022 (online em 2021). Hey et al. = 2025 (vol. 254, jan 2025; o DOI traz '2024'). O'Rear & Radvansky = 2020 (online em 2019).\n\nITENS SINALIZADOS (atendem, mas merecem sua decisão):\n- Mickelberg 2024 e 2025 e Ecker & Rodricks 2020: pessoa fictícia com alegação negativa (violência doméstica no último). Não são políticas nem de saúde, mas têm carga emocional.\n- Buczel 2022: um dos 6 cenários fictícios envolve a demissão de um político. 'Vaccination' no título é só metáfora.\n- Laurent 2024: cenários militares fictícios; não houve CIE (achado nulo, ainda dentro do tema).\n- McIlhiney 2023: relatos de evento sobre causas de eventos; o texto lido não diz explicitamente que são fictícios.\n\nCANDIDATOS DESCARTADOS OU PENDENTES:\nSem confirmação de materiais neutros (provavelmente elegíveis se você puder conferir os métodos): Buczel et al. 2024, M&C, 10.3758/s13421-024-01520-z (N = 337 no resumo); Buczel et al. 2025, QJEP, 10.1177/17470218251336232 (N = 441); McIlhiney et al. 2022, QJEP, 10.1177/17470218211048986; Rich et al. 2023, JEP: Applied, 10.1037/xap0000454; Brydges et al. 2018, Intelligence, 10.1016/j.intell.2018.03.009 (N = 216); Brydges et al. 2020, J Cogn Psychol, 10.1080/20445911.2020.1849226; Jia et al. 2020, J Cogn Psychol, 10.1080/20445911.2020.1800019.\nSem abstract ou materiais acessíveis: Westbrook et al. 2023 (M&C, 10.3758/s13421-023-01402-w); Liu et al. 2023 e 2024 (J Cogn Psychol); Jia & Jin 2024 (Current Psychology); Jia 2024 (Soc Behav Personal); Butler et al. 2023 (JARMAC); Tan 2022 (Abacus, contexto financeiro).\nExcluídos: Miller et al. 2022 (ACP, 10.1002/acp.3939; o resumo não traz achado nem N); Connor Desai et al. 2020 (Cognition; estudo de modelagem normativa, com N = 101 só endossando suposições, sem medir crença depois da correção); Susmann & Wegener 2022 PSPB (atitudes prévias, possivelmente temas controversos); Walter & Tukachinsky 2019 (meta-análise); van Huijstee 2021 (COVID-19); Hu 2025 (saúde); Pluviano 2022 (vacinas); Jin 2022 (Acta Psychologica Sinica; em chinês, não conferi).\n\nCRITÉRIOS QUE MAIS ELIMINARAM: (1) materiais neutros não verificáveis sem acesso aos métodos; (2) abstract inacessível; (3) bloqueio de editoras.\n\nCONSULTAS NÃO EXECUTADAS: as buscas em português (SciELO e OpenAlex-pt) não foram rodadas. Não esperaria resultados, porque a literatura de CIE é quase toda em inglês."
}