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
   "checked_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=8447889&rettype=xml ; https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2022 (vol. 50, n. 2); online-first em 2021",
    "Artigo de periódico, dados próprios",
    "Tipo/método: 3 experimentos online com participantes humanos, retratação x confirmação, medidas de crença e de inferências",
    "Materiais neutros: relato fictício de incêndio em depósito (conferido nos métodos). A vacina só aparece como exemplo motivador",
    "Amostra: não informado no resumo",
    "Achado: o desconforto causado pelas retratações prediz a crença e o uso continuados da informação falsa",
    "Trecho do resumo: \"this discomfort predicts continued belief in and use of misinformation\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2021 (vol. 49, n. 4)",
    "Artigo de periódico empírico",
    "Tipo/método: 2 experimentos online; credibilidade da fonte da retratação (confiabilidade x expertise); perguntas de inferência",
    "Materiais neutros: relatos fictícios em estilo de notícia (conferido no texto completo, tentativa anterior)",
    "Amostra: não informado no resumo",
    "Achado: a confiabilidade da fonte, e não a expertise, influencia a eficácia da retratação",
    "Trecho do resumo: \"source trustworthiness but not source expertise indeed influences retraction effectiveness\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2020 (vol. 48, n. 1); online-first em 2019",
    "Artigo de periódico empírico",
    "Tipo/método: 3 experimentos com narrativas de evento, retratação explícita e perguntas de inferência",
    "Materiais neutros: narrativas de evento sem tema político nem de saúde (conforme resumo)",
    "Amostra: não informado no resumo",
    "Achado: parte da influência continuada vem de pessoas que não aceitam a retratação",
    "Trecho do resumo: \"some people not accepting the retraction, even in the absence of external motivation to disregard it\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2020 (vol. 48, n. 7)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento com leitores de inglês e de chinês; celular x outro formato; informação crítica retratada ou não; memória e inferência",
    "Materiais neutros: artigos curtos em estilo de jornal, sem tema político nem de saúde (o tema exato não consta no resumo)",
    "Amostra: não informado no resumo",
    "Achado: ler no celular reduziu a chance de o leitor notar a retratação",
    "Trecho do resumo: \"reading on a mobile phone reduced the likelihood that readers noticed the retraction\""
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
   "checked_url": "https://api.crossref.org/works/10.3758/s13428-018-1066-z (issued online 2018-06-25; print 2019-06, vol. 51, n. 3)",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2019 (vol. 51, n. 3); online-first em 2018",
    "Artigo de periódico empírico",
    "Tipo/método: experimentos online; relato com correção; perguntas abertas x fechadas",
    "Materiais neutros: relato fictício de incêndio em depósito (conferido no texto completo, tentativa anterior)",
    "Amostra: \"We implemented this basic procedure online (Exp. 1A, n = 78)\"; \"a larger preregistered study (Exps. 2A and 2B, n = 323)\"",
    "Achado: os participantes continuaram a se referir à informação falsa depois da correção, com perguntas abertas e fechadas",
    "Trecho do resumo: \"Participants continued to refer to the misinformation following a correction\""
   ]
  },
  {
   "doi": "10.1186/s41235-021-00335-9",
   "title": "Exploring factors that mitigate the continued influence of misinformation",
   "authors": [
    "Irene P. Kan",
    "Kendra L. Pizzonia",
    "Anna B. Drummey",
    "Eli J. V. Mikkelsen"
   ],
   "year": 2021,
   "venue": "Cognitive Research: Principles and Implications",
   "checked_url": "https://api.crossref.org/works/10.1186/s41235-021-00335-9 (autor corrigido: Eli J. V. Mikkelsen)",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2021 (vol. 6, n. 1)",
    "Artigo de periódico empírico",
    "Tipo/método: 3 estudos online; explicação alternativa, centralidade e retratação",
    "Materiais neutros: relatos fictícios curtos (micro-ônibus, roubo, incêndio em lavanderia), conferido no texto completo na tentativa anterior",
    "Amostra: não informado no resumo",
    "Achado: oferecer uma explicação alternativa reduziu de forma consistente o CIE",
    "Trecho do resumo: \"alternative provision consistently resulted in CIE reduction\"",
    "CORREÇÃO aplicada: quarto autor é Eli J. V. Mikkelsen (não Eric)"
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9049321",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2022 (vol. 17, n. 4)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento; inoculação x controle; correção de fonte mais ou menos confiável; inferências",
    "Materiais neutros: 6 cenários fictícios (água contaminada, roubo, incêndio etc.). SINALIZAÇÃO: um cenário envolve um político fictício; 'vaccination' no título é metáfora; a fase de inoculação usou um debate fictício sobre uma substância em alimentos",
    "Amostra: não informado no resumo",
    "Achado: participantes inoculados dependeram menos da informação falsa quando a correção vinha de fonte muito confiável",
    "Trecho do resumo: \"inoculated participants relied on misinformation less when the correction came from a highly credible source\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60 ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28ABSTRACT%3A%22misinformation%22...%29 (PMC9994702)",
   "criteria_met": [
    "Tema: perseverança da crença depois da retratação (construto do CIE)",
    "Ano oficial 2023 (vol. 18, n. 3)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento; retratação de um estudo inventado; 3 técnicas de redução; crença depois da retratação",
    "Materiais neutros: resumo inventado de estudo sobre bombeiros (conferido no texto completo, tentativa anterior)",
    "Amostra: \"an experiment with N = 251 participants\"",
    "Achado: o counter-speech foi a técnica mais eficaz",
    "Trecho do resumo: \"The CS technique, with a very large effect size, is the most effective among the three techniques.\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2022 (vol. 17, n. 7)",
    "Artigo de periódico empírico",
    "Tipo/método: 2 experimentos; fronteira de evento entre informação falsa e retratação; medida do CIE",
    "Materiais neutros: cenários fictícios (pouso de emergência; assalto em realidade virtual). MMR só na introdução",
    "Amostra: não informado no resumo",
    "Achado: o Experimento 2 mostrou CIE reduzido com fronteira de evento; o 1 não",
    "Trecho do resumo: \"Experiment 2 yielded evidence that an event boundary resulted in a reduced CIE\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0283951",
   "title": "Executive function and the continued influence of misinformation: A latent-variable analysis",
   "authors": [
    "Paul McIlhiney",
    "Gilles E. Gignac",
    "Ullrich K. H. Ecker",
    "Briana L. Kennedy",
    "Michael Weinborn"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "checked_url": "https://api.crossref.org/works/10.1371/journal.pone.0283951 (autora corrigida: Briana L. Kennedy)",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2023 (vol. 18, n. 4)",
    "Artigo de periódico empírico",
    "Tipo/método: diferenças individuais; tarefa de CIE (8 relatos de evento, retratados ou não, com inferências) + tarefas de função executiva; variáveis latentes",
    "Materiais neutros: relatos de evento sobre causas (p. ex., mortes de peixes), sem tema político ou de saúde; o resumo não diz explicitamente que são fictícios",
    "Amostra: não informado no resumo",
    "Achado: a função executiva, em especial a atualização da memória de trabalho, prediz a suscetibilidade ao CIE",
    "Trecho do resumo: \"Results showed that EF can predict susceptibility to the CIE, especially the factor of working-memory updating.\"",
    "CORREÇÃO aplicada: quarta autora é Briana L. Kennedy (não Blake)"
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60 ; PMC11549669",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2024 (vol. 15)",
    "Artigo de pesquisa original",
    "Tipo/método: 3 experimentos; recordação colaborativa depois de relatos com correção; inferências",
    "Materiais neutros: artigos fictícios em estilo de jornal (p. ex., incêndio atribuído a raios), conferido nos métodos na tentativa anterior",
    "Amostra: não informado no resumo",
    "Achado: a colaboração por revezamento mitigou o CIE de forma consistente",
    "Trecho do resumo: \"turn-taking collaboration consistently mitigates the CIE\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60 ; PMC12058158",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2025 (vol. 20, n. 5)",
    "Artigo de periódico empírico",
    "Tipo/método: 3 experimentos; impressão sobre pessoa fictícia com afirmação negativa retratada ou não",
    "Materiais neutros, com SINALIZAÇÃO: pessoa fictícia e afirmações inventadas, valência negativa; sem tema político ou de saúde",
    "Amostra: não informado no resumo",
    "Achado: influência continuada em um experimento; nos outros dois a afirmação foi descontada",
    "Trecho do resumo: \"Evidence for the continued influence of the retracted behaviour statement was found in one experiment\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2024 (vol. 10, n. 1)",
    "Artigo de periódico empírico (versão publicada; o preprint PsyArXiv não foi usado)",
    "Tipo/método: 4 experimentos; impressão sobre protagonista fictício com comportamento retratado, negativo ou positivo",
    "Materiais neutros, com SINALIZAÇÃO: pessoa fictícia, sem tema político ou de saúde",
    "Amostra: não informado no resumo",
    "Achado: a informação retratada foi totalmente descontada, sem influência continuada",
    "Trecho do resumo (conferido na tentativa anterior via Semantic Scholar; a página do editor deu 403): \"fully discounted the misinformation once retracted\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=misinformation+correction+timing+retraction+reliance+false+information+memory&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=50",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2020 (vol. 9, n. 4)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento; comportamentos de pessoa fictícia, com e sem alegação retratada; traços, previsão de comportamento e medida indireta",
    "Materiais neutros, com SINALIZAÇÃO: pessoa fictícia; a alegação retratada é de violência doméstica (carga emocional), sem tema político ou de saúde",
    "Amostra: não informado no resumo",
    "Achado: a alegação desacreditada não influenciou as avaliações explícitas nem as previsões de comportamento",
    "Trecho do resumo: \"Discredited misinformation was found to influence neither trait ratings of the person nor behavior predictions.\""
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.cognition.2024.106000%22&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2025 (vol. 254, jan 2025); DOI com 2024 por causa do online-first",
    "Artigo de periódico empírico",
    "Tipo/método: 2 experimentos; credibilidade do informante e do retratador manipulada de forma independente",
    "Materiais neutros: notícia fictícia (conforme resumo); o tema exato não consta no resumo",
    "Amostra: \"In two experiments (N = 151, N = 146), informant credibility and retractor credibility were independently manipulated.\"",
    "Achado: não houve CIE quando o informante era menos crível que o retratador, o que é coerente com uma explicação racional",
    "Trecho do resumo: \"When the informant was less credible than the retractor, participants showed no CIE, in line with a rational account.\""
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
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60",
   "criteria_met": [
    "Tema CIE: sim (CIE e supercorreção)",
    "Ano oficial 2024 (vol. 38, n. 3)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento; cenários militares com informação falsa corrigida; inferência e tomada de decisão",
    "Materiais neutros, com SINALIZAÇÃO: cenários militares fictícios de domínio específico, sem tema político, eleitoral, de vacinas, COVID-19 nem de saúde",
    "Amostra: \"A total of 61 participants read four military scenarios\"",
    "Achado: não houve evidência de CIE, mas surgiu supercorreção na tomada de decisão",
    "Trecho do resumo: \"The results did not reveal any evidence of the CIE, but an overcorrection effect emerged in decision‐making.\""
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22continued%20influence%22%20OR%20ABSTRACT:%22continued%20influence%22)%20AND%20PUB_YEAR:[2018%20TO%202025] (registro com DOI, título, ano e periódico)",
   "criteria_met": [
    "Tema CIE: sim (réplica direta de Johnson & Seifert, 1994)",
    "Ano oficial 2023 (vol. 241)",
    "Artigo de periódico empírico (replicação com dados próprios)",
    "Tipo/método: experimento entre grupos com francófonos; informação falsa retratada x controle; inferências",
    "Materiais neutros: o mesmo texto do estudo original, sem tema político ou de saúde (conferido na tentativa anterior)",
    "Amostra: \"comparing the inferences drawn by an FI group (n = 21) to those made by a control group (n = 23)\"",
    "Achado: os resultados confirmam os do estudo original",
    "Trecho do resumo: \"The results confirm those of the original study, supporting the validity of Johnson and Seifert's paradigm\""
   ]
  },
  {
   "doi": "10.3758/s13421-022-01354-7",
   "title": "Does explaining the origins of misinformation improve the effectiveness of a given correction?",
   "authors": [
    "Saoirse Connor Desai",
    "Stian Reimers"
   ],
   "year": 2023,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9487849/fullTextXML ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-022-01354-7%22&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (raciocínio sobre eventos após correção, com explicação da origem da desinformação)",
    "Ano oficial 2023 (vol. 51, n. 2); online-first em 2022",
    "Artigo de periódico empírico",
    "Tipo/método: 2 experimentos online; correção simples x correção com explicação do erro/da mentira; perguntas de inferência abertas (referências à desinformação)",
    "Materiais neutros: tweets fictícios sobre incêndio em depósito (Exp. 1 e 2) e acidente de van (Exp. 2); conferido no texto completo; o exemplo de vacina COVID-19 é só da introdução",
    "Amostra: não informado no resumo (nos métodos: N = 365 e 158 analisados)",
    "Achado: explicar a origem da desinformação provavelmente não torna a correção mais eficaz do que dizer que ela é falsa",
    "Trecho do resumo: \"may not be an effective correction strategy over and above stating that the misinformation is false.\""
   ]
  },
  {
   "doi": "10.1037/mac0000057",
   "title": "Listening to Misinformation while Driving: Cognitive Load and the Effectiveness of (Repeated) Corrections",
   "authors": [
    "Jasmyne A. Sanderson",
    "Vanessa Bowden",
    "Briony Swire-Thompson",
    "Stephan Lewandowsky",
    "Ullrich K. H. Ecker"
   ],
   "year": 2023,
   "venue": "Journal of Applied Research in Memory and Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1037/mac0000057%22&resultType=core&format=json ; texto completo: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=7615113&rettype=xml",
   "criteria_met": [
    "Tema CIE: sim (inferências após correção; carga cognitiva e correções repetidas)",
    "Ano oficial 2023 (vol. 12, n. 3, set 2023)",
    "Artigo de periódico empírico",
    "Tipo/método: experimento com participantes humanos; 6 relatos auditivos com causa crítica retratada ou não, correção única x múltipla, carga cognitiva (simulador de direção); escore de inferência",
    "Materiais neutros: 6 relatos de eventos fictícios em formato de noticiário de rádio (p. ex., pouso de emergência de avião); sem tema político ou de saúde (conferido no texto completo)",
    "Amostra: não informado no resumo (nos métodos: 259 testados, 233 analisados)",
    "Achado: a carga cognitiva reduziu a eficácia das correções; uma correção única foi ineficaz sob carga",
    "Trecho do resumo: \"cognitive load reduced correction effectiveness\""
   ]
  },
  {
   "doi": "10.3758/s13421-022-01374-3",
   "title": "The independent effects of source expertise and trustworthiness on retraction believability: The moderating role of vested interest",
   "authors": [
    "Mark W. Susmann",
    "Duane T. Wegener"
   ],
   "year": 2023,
   "venue": "Memory & Cognition",
   "checked_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9718466&rettype=xml ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-022-01374-3%22&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (crença continuada na desinformação depois da retratação, conforme o resumo)",
    "Ano oficial 2023 (vol. 51, n. 4); online-first em dez 2022",
    "Artigo de periódico empírico",
    "Tipo/método: 2 estudos online com participantes humanos; expertise, confiabilidade e interesse da fonte da retratação manipulados; medidas de credibilidade da retratação, endosso da desinformação e inferências",
    "Materiais neutros: cenário construído de incêndio em depósito de empresa de papel, adaptado de Wilkes & Leatherbarrow (1988); sem tema político ou de saúde (conferido no texto completo)",
    "Amostra: não informado no resumo (nos métodos: 226 e 353 participantes)",
    "Achado: retratações de fonte especialista geram menos crença continuada na desinformação, mas só quando a fonte não tem interesse na retratação",
    "Trecho do resumo: \"and lead to less continued belief in misinformation than retractions from an inexpert source\""
   ]
  },
  {
   "doi": "10.3758/s13421-023-01402-w",
   "title": "Mechanisms in continued influence: The impact of misinformation corrections on source perceptions",
   "authors": [
    "Victoria Westbrook",
    "Duane T. Wegener",
    "Mark W. Susmann"
   ],
   "year": 2023,
   "venue": "Memory & Cognition",
   "checked_url": "https://api.crossref.org/works/10.3758/s13421-023-01402-w ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-023-01402-w%22&resultType=core&format=json ; https://link.springer.com/article/10.3758/s13421-023-01402-w (métodos)",
   "criteria_met": [
    "Tema CIE: sim (título e resumo: continued influence, correção e crença na desinformação)",
    "Ano oficial 2023 (vol. 51, n. 6; online mar 2023)",
    "Artigo de periódico empírico",
    "Tipo/método: 3 estudos com participantes humanos (o 3 é réplica pré-registrada); correção x controle x correção com derrogação da fonte; endosso da desinformação, percepção da fonte e inferências",
    "Materiais neutros: 12–13 afirmações fictícias sobre incêndio em depósito de empresa de papel; sem tema político ou de saúde (conferido nos métodos)",
    "Amostra: não informado no resumo (nos métodos: 125, 138 e 251 analisados)",
    "Achado: as percepções sobre a fonte da desinformação são um mecanismo que muda a crença nela depois da correção",
    "Trecho do resumo: \"perceptions of the misinformation source is one mechanism that can cause changes in belief in misinformation\""
   ]
  },
  {
   "doi": "10.3758/s13421-024-01520-z",
   "title": "How do forewarnings and post-warnings affect misinformation reliance? The impact of warnings on the continued influence effect and belief regression",
   "authors": [
    "Klara Austeja Buczel",
    "Adam Siwiak",
    "Malwina Szpitalak",
    "Romuald Polczyk"
   ],
   "year": 2024,
   "venue": "Memory & Cognition",
   "checked_url": "https://api.crossref.org/works/10.3758/s13421-024-01520-z ; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.3758/s13421-024-01520-z%22&resultType=core&format=json ; https://link.springer.com/article/10.3758/s13421-024-01520-z (métodos)",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2024 (vol. 52, n. 5)",
    "Artigo de periódico empírico",
    "Tipo/método: 2 experimentos com participantes humanos; aviso antes ou depois da desinformação; reteste após 7 dias; inferências abertas",
    "Materiais neutros: cenário fictício de incêndio em depósito (13 mensagens, Wilkes & Leatherbarrow, 1988); sem tema político ou de saúde (conferido nos métodos)",
    "Amostra: \"In two experiments (N = 337)\"",
    "Achado: o aviso prévio reduziu a dependência da desinformação, mas o efeito protetor não durou",
    "Trecho do resumo: \"However, the protective effect of the forewarning was not durable\""
   ]
  },
  {
   "doi": "10.2224/sbp.13662",
   "title": "The effect of correction timing on the continued influence effect of misinformation with different relevance",
   "authors": [
    "Lina Jia"
   ],
   "year": 2024,
   "venue": "Social Behavior and Personality: an international journal",
   "checked_url": "https://api.crossref.org/works?query.bibliographic=misinformation+correction+timing+retraction+reliance+false+information+memory&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=50 ; https://www.sbp-journal.com/index.php/sbp/article/view/13662",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2024 (vol. 52, n. 12, dez 2024)",
    "Artigo de periódico, pesquisa empírica",
    "Tipo/método: 2 estudos experimentais, delineamento misto 2 (relevância) × 3 (intervalo da correção: imediata, 1 dia, 1 semana); correção por explicação alternativa ou fonte de alta autoridade",
    "Materiais neutros: histórias fictícias de incidentes cotidianos (incêndio em fábrica têxtil, incêndio em cabine, problemas no refeitório); sem tema político ou de saúde (conferido no site do periódico)",
    "Amostra: \"two studies with 86 participants\"",
    "Achado: o melhor momento para corrigir dependeu da relevância da informação e do método de correção",
    "Trecho do resumo: \"the best timing for corrections differed across various correction methods\"",
    "SINALIZAÇÃO: o resumo pode ser conferido de novo no site do periódico; os dois estudos usaram os mesmos 86 participantes"
   ]
  },
  {
   "doi": "10.3724/sp.j.1041.2022.00343",
   "title": "The neural basis of the continued influence effect of misinformation",
   "authors": [
    "Hua Jin",
    "Lina Jia",
    "Xiaojuan Yin",
    "Shizhen Yan",
    "Shilin Wei",
    "Juntao Chen"
   ],
   "year": 2022,
   "venue": "Acta Psychologica Sinica",
   "checked_url": "https://api.crossref.org/works?query.bibliographic=continued+influence+effect+misinformation+retraction&filter=from-pub-date:2018,until-pub-date:2025,type:journal-article&rows=60 ; https://journal.psych.ac.cn/acps/EN/Y2022/V54/I4/343",
   "criteria_met": [
    "Tema CIE: sim",
    "Ano oficial 2022 (vol. 54, n. 4; publicado em 25/04/2022)",
    "Artigo de periódico, estudo empírico (fMRI de tarefa)",
    "Tipo/método: experimento de neuroimagem com participantes humanos; condição de retratação x controle; escores de inferência e ativação cerebral",
    "Materiais neutros: cenário de colapso de um prédio de escritórios com relato de incêndio retratado por bombeiros, seguido de problemas de inferência; sem tema político ou de saúde. SINALIZAÇÃO: a página não diz explicitamente que o cenário é fictício",
    "Amostra: não informado no resumo",
    "Achado: os escores de inferência na condição de retratação foram maiores que no controle, e a ativação do giro temporal médio esquerdo foi menor",
    "Trecho do resumo: \"the inference scores of retraction condition were significantly higher than that of control condition\""
   ]
  }
 ],
 "notes": "Entrego 24 artigos, não 25: falta 1 para a meta.\n\nCORREÇÕES PEDIDAS (feitas):\n- McIlhiney et al. 2023 (PLOS ONE): a quarta autora é Briana L. Kennedy. Conferido no Crossref e na lista do Crossref.\n- Kan et al. 2021 (Cogn. Res. Princ. Implic.): o quarto autor é Eli J. V. Mikkelsen. Conferido no Crossref.\n- Os outros 15 itens da tentativa anterior foram mantidos. Reabri todos nesta tentativa, pelas listas do Crossref ou do Europe PMC. Nos 15 itens mantidos não troquei dados, e a conferência de materiais e amostra dos métodos vem da tentativa anterior.\n- Connor Desai & Reimers 2019 (Behav. Res. Methods): o Crossref mostra online-first em 2018 e edição impressa em 2019 (vol. 51, n. 3). Mantive 2019 como ano oficial.\n\nITENS NOVOS (8; todos com materiais conferidos nos métodos ou no site do periódico): Connor Desai & Reimers 2023; Sanderson et al. 2023 (JARMAC); Susmann & Wegener 2023 (Mem. Cogn.); Westbrook et al. 2023; Buczel et al. 2024 (Mem. Cogn.); Jia 2024 (Soc. Behav. Pers.); Jin et al. 2022 (Acta Psychol. Sinica). São 7 novos; 17 + 7 = 24.\n\nCANDIDATOS PENDENTES QUE NÃO ENTRARAM, porque não consegui conferir nos métodos que os materiais são neutros (os sites dos editores Sage, Wiley, APA, Taylor & Francis e Elsevier bloquearam a leitura com 403 ou 'loading'):\n- Brydges, Gignac & Ecker 2018 (Intelligence, 10.1016/j.intell.2018.03.009): resumo com N = 216, mas materiais não conferidos.\n- Brydges et al. 2020 (J. Cogn. Psychol., 10.1080/20445911.2020.1849226).\n- Jia et al. 2020 (J. Cogn. Psychol., 10.1080/20445911.2020.1800019).\n- McIlhiney et al. 2022 (QJEP, 10.1177/17470218211048986).\n- Buczel et al. 2025 (QJEP, 10.1177/17470218251336232; resumo com N = 441).\n- Rich, Donovan & Rapp 2023 (JEP: Applied, 10.1037/xap0000454).\n- Rich & Zaragoza 2020 (JARMAC, 10.1037/h0101850).\n- Sanderson, Gignac & Ecker 2021 (J. Cogn. Psychol., 10.1080/20445911.2021.1931243).\n- Miller et al. 2022 (Appl. Cogn. Psychol., 10.1002/acp.3939; o DOI 10.1002/acp.3818 parece ser a versão online-first duplicada, em 2021).\n- Liu et al. 2023 e 2024 (J. Cogn. Psychol.), Clinton-Lisell & Langowski 2024 (Reading Psychology) e Connor Desai, Pilditch & Madsen 2020 (Cognition; resumo com N = 101, mas materiais não conferidos).\n- Jia & Jin 2024 (Curr. Psychol.): o resumo não descreve os materiais.\n- Jia 2024 (Psychology of China): a página não diz os temas nem se são fictícios.\nSe o pesquisador puder abrir o texto desses itens, vários provavelmente atendem. Os pares Brydges/Sanderson/McIlhiney/Rich usam relatos de evento do paradigma padrão, mas não afirmo isso sem conferir.\n\nEXCLUÍDOS POR CRITÉRIO (conferido):\n- Ecker et al. 2024 (CRPI, 'Don't believe them!'): um dos artigos fictícios trata de tratamento da menopausa (saúde).\n- Ecker, Butler & Hamby 2020 (narrativas): os Exps. 2 e 3 usam alegações de saúde e controversas (políticas).\n- Siebert & Siebert 2024 (PLOS ONE, 10.1371/journal.pone.0299139): a desinformação é um blog fictício sobre trabalho remoto, mas uma variante da intervenção usa o caso MMR-autismo; excluí por cautela de saúde.\n- Cohen et al. 2024 (candidatos políticos), van Huijstee 2021 (COVID-19), Pluviano 2022 (vacinas) e Susmann & Wegener 2023 PSPB (atitudes; tema dos estímulos não conferido) ficaram fora.\n- Também excluí preprints (PsyArXiv, Research Square), meta-análises (Walter & Tukachinsky 2019), revisões e correções (erratum da PLOS ONE).\n\nLimitações: o OpenAlex devolveu HTTP 429, então usei Crossref e Europe PMC. As citações literais dos itens novos vieram de leitura via ferramenta que só devolve trechos curtos. Elas são fragmentos contíguos do resumo, mas vale conferi-las no site do periódico. Em dois itens (Mickelberg 2024 e Connor Desai 2023), o trecho veio de fonte secundária ou é um fragmento. Para o item da Collabra, a página do editor deu 403 na tentativa anterior e o trecho veio do Semantic Scholar."
}