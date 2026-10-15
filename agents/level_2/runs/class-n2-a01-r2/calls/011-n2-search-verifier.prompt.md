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
   "year": 2021,
   "venue": "Memory & Cognition",
   "checked_url": "https://api.crossref.org/works/10.3758/s13421-021-01232-8",
   "criteria_met": [
    "Tema CIE: sim (retratação e uso continuado da desinformação)",
    "Período: sim (Crossref: online 2021-09-17; edição impressa 2022-02)",
    "Periódico revisado por pares, journal-article: sim",
    "Tipo de estudo e método: três experimentos online com participantes humanos (MTurk e estudantes), retratação vs. confirmação/controle; mede endosso da desinformação e inferências",
    "Materiais neutros: sim, relato fictício de incêndio em galpão (conferido nos métodos, PMC8447889)",
    "Amostra: não informado no resumo",
    "Achado principal: a retratação gera desconforto, e o desconforto prediz a crença e o uso continuados da desinformação",
    "Trecho literal do resumo: \"this discomfort predicts continued belief in and use of misinformation\""
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.3758/s13421-022-01374-3\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (credibilidade da retratação; mede endosso da desinformação e inferências após a retratação)",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim (Memory & Cognition, research-article)",
    "Tipo de estudo e método: dois experimentos com participantes humanos (MTurk, estudantes), manipulando especialização, confiabilidade e interesse da fonte da retratação",
    "Materiais neutros: sim, incêndio fictício em galpão; sem conteúdo político ou de saúde nos estímulos (PMC9718466)",
    "Amostra: não informado no resumo",
    "Achado principal: retratações de fonte especialista são mais acreditadas, mas só quando a fonte não tem interesse na retratação",
    "Trecho literal do resumo: \"Study 1 demonstrated that retractions from an expert source are believed more\""
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.3758/s13421-022-01354-7\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (eficácia da correção e referência à desinformação)",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: dois experimentos online com humanos (MTurk), quatro condições de correção, perguntas de inferência abertas",
    "Materiais neutros: sim, incêndio em galpão e acidente de van fictícios (PMC9487849)",
    "Amostra: não informado no resumo",
    "Achado principal: explicar se a desinformação foi deliberada ou acidental não torna a correção mais eficaz do que dizer que ela é falsa",
    "Trecho literal do resumo: \"may not be an effective correction strategy over and above stating that the misinformation is false.\""
   ]
  },
  {
   "doi": "10.3758/s13421-020-01129-y",
   "title": "Can you believe it? An investigation into the impact of retraction source credibility on the continued influence effect",
   "authors": [
    "Ullrich K. H. Ecker",
    "L. M. Antonio"
   ],
   "year": 2021,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.3758/s13421-020-01129-y\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2021)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: dois experimentos com humanos, manipulando credibilidade da fonte da retratação",
    "Materiais neutros: sim, notícias construídas para o estudo (ex.: fechamento de captação de água após mortes de peixes); sem conteúdo político ou de saúde nos métodos (PMC7810102). Os métodos não dizem explicitamente 'fictício'",
    "Amostra: não informado no resumo",
    "Achado principal: a confiabilidade da fonte, mas não a especialização, influencia a eficácia da retratação",
    "Trecho literal do resumo: \"source trustworthiness but not source expertise indeed influences retraction effectiveness\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0282202",
   "title": "Effective mitigation of the belief perseverance bias after the retraction of misinformation: Awareness training and counter-speech",
   "authors": [
    "J. Siebert",
    "J. U. Siebert"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282202",
   "criteria_met": [
    "Tema: persistência da crença após retratação (belief perseverance, fenômeno equivalente ao CIE; não confirmei se o resumo usa o termo 'continued influence')",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: experimento com humanos, opiniões medidas antes da desinformação, depois dela e depois da retratação, com três técnicas de mitigação",
    "Materiais neutros: sim, resumo de estudo inventado e casos de dois bombeiros sobre atitude ao risco e sucesso, retratado como nunca realizado (conferido nos métodos)",
    "Amostra: \"N = 251 participants\"",
    "Achado principal: a técnica de contra-argumentação (counter-speech) foi a mais eficaz para reduzir a persistência da crença após a retratação",
    "Trecho literal do resumo: \"The CS technique, with a very large effect size, is the most effective among the three techniques.\""
   ]
  },
  {
   "doi": "10.1037/mac0000057",
   "title": "Listening to Misinformation while Driving: Cognitive Load and the Effectiveness of (Repeated) Corrections",
   "authors": [
    "J. A. Sanderson",
    "V. Bowden",
    "B. Swire-Thompson",
    "S. Lewandowsky",
    "U. K. H. Ecker"
   ],
   "year": 2023,
   "venue": "Journal of Applied Research in Memory and Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.1037/mac0000057\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim (eficácia de correções simples e repetidas)",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: experimentos com humanos (estudo piloto, Exp. 1 e 2) em simulador de direção, correções em áudio e carga cognitiva",
    "Materiais neutros: sim, notícias construídas (ex.: captação de água desligada após morte de peixes); sem conteúdo político ou de saúde nos métodos (PMC7615113)",
    "Amostra: não informado no resumo",
    "Achado principal: múltiplas correções foram mais eficazes que uma única",
    "Trecho literal do resumo: \"Multiple corrections were more effective than a single correction\""
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
   "checked_url": "https://api.crossref.org/works/10.1186/s41235-021-00335-9",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (online 2021-11-27)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: três estudos com humanos, correção direta, explicação alternativa e centralidade causal",
    "Materiais neutros: sim, histórias fictícias (acidente de minibus, roubo, incêndio em lavanderia); sem conteúdo político ou de saúde (PMC8627545)",
    "Amostra: não informado no resumo",
    "Achado principal: fornecer uma explicação alternativa reduziu consistentemente o efeito de influência continuada",
    "Trecho literal do resumo: \"alternative provision consistently resulted in CIE reduction.\""
   ]
  },
  {
   "doi": "10.3758/s13428-018-1066-z",
   "title": "Comparing the use of open and closed questions for Web-based measures of the continued-influence effect",
   "authors": [
    "Saoirse Connor Desai",
    "Stian Reimers"
   ],
   "year": 2018,
   "venue": "Behavior Research Methods",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.3758/s13428-018-1066-z\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (Crossref: 2018 online; Europe PMC: 2019 na edição)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: experimentos online com humanos, formato de pergunta aberta vs. fechada, com e sem correção",
    "Materiais neutros: sim, notícia fictícia de incêndio em galpão (PMC6538818)",
    "Amostra: \"Exp. 1A, n = 78\"; \"Exp. 1B, n = 75\"; \"Exps. 2A and 2B, n = 323\"",
    "Achado principal: o efeito de influência continuada apareceu com perguntas abertas e fechadas",
    "Trecho literal do resumo: \"We observed the CIE in all conditions: Participants continued to refer to the misinformation following a correction\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0271566",
   "title": "Examining the role of information integration in the continued influence effect using an event segmentation approach",
   "authors": [
    "J. A. Sanderson",
    "S. Farrell",
    "U. K. H. Ecker"
   ],
   "year": 2022,
   "venue": "PLOS ONE",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.1371/journal.pone.0271566\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2022)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: dois experimentos com humanos, fronteira de evento espacial num relato com retratação",
    "Materiais neutros: sim, relatos fictícios (pouso de emergência, roubo de casa); sem conteúdo político ou de saúde nos métodos (PMC9292086)",
    "Amostra: não informado no resumo",
    "Achado principal: uma fronteira de evento reduziu o efeito de influência continuada no Experimento 2, o que apoia explicações baseadas em recuperação",
    "Trecho literal do resumo: \"Experiment 2 yielded evidence that an event boundary resulted in a reduced CIE.\""
   ]
  },
  {
   "doi": "10.3389/fpsyg.2024.1487146",
   "title": "The inhibitory impact of collaboration on the continued influence effect of misinformation",
   "authors": [
    "Gongxiang Chen",
    "Y. Zhong",
    "S. Li"
   ],
   "year": 2024,
   "venue": "Frontiers in Psychology",
   "checked_url": "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1487146/full",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2024)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: três experimentos com humanos (estudantes), colaboração (revezamento ou livre) vs. individual, com correção",
    "Materiais neutros: sim, relatos de notícias construídos (ex.: incêndio) com correção; sem conteúdo político ou de saúde nos métodos",
    "Amostra: não informado no resumo",
    "Achado principal: a colaboração por revezamento reduz o efeito de influência continuada",
    "Trecho literal do resumo: \"turn-taking collaboration consistently mitigates the CIE\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0322045",
   "title": "Did he or didn't he? Mixed evidence for the continued influence of retracted misinformation on person impressions",
   "authors": [
    "A. J. Mickelberg",
    "B. Walker",
    "U. K. H. Ecker",
    "P. D. L. Howe",
    "A. Perfors",
    "N. Fay"
   ],
   "year": 2025,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0322045",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2025)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: três experimentos online (Prolific) com humanos, impressões sobre uma pessoa fictícia após retratação",
    "Materiais neutros: sim, personagem fictício 'John' e afirmações de comportamento (caso extraconjugal, chute no cachorro, corte de árvore); sem conteúdo político ou de saúde",
    "Amostra: não informado no resumo (o resumo cita 'three experiments')",
    "Achado principal: a influência continuada da afirmação retratada apareceu em um experimento, e nos outros dois ela foi totalmente descartada",
    "Trecho literal do resumo: \"Evidence for the continued influence of the retracted behaviour statement was found in one experiment\""
   ]
  },
  {
   "doi": "10.1371/journal.pone.0283951",
   "title": "Executive function and the continued influence of misinformation: A latent-variable analysis",
   "authors": [
    "P. McIlhiney",
    "G. E. Gignac",
    "U. K. H. Ecker",
    "B. L. Kennedy",
    "M. Weinborn"
   ],
   "year": 2023,
   "venue": "PLOS ONE",
   "checked_url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283951",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: estudo com humanos, tarefa de CIE (retratação vs. controle) mais bateria de função executiva, análise de variável latente",
    "Materiais neutros: sim, oito relatos de eventos (ex.: mortes de peixes num rio) sem conteúdo político ou de saúde. Os métodos não dizem explicitamente 'fictício'",
    "Amostra: não informado no resumo",
    "Achado principal: a função executiva, em especial a atualização da memória de trabalho, prediz a suscetibilidade ao efeito de influência continuada",
    "Trecho literal do resumo: \"EF can predict susceptibility to the CIE, especially the factor of working-memory updating.\""
   ]
  },
  {
   "doi": "10.3758/s13421-023-01402-w",
   "title": "Mechanisms in continued influence: The impact of misinformation corrections on source perceptions",
   "authors": [
    "V. Westbrook",
    "D. T. Wegener",
    "M. W. Susmann"
   ],
   "year": 2023,
   "venue": "Memory & Cognition",
   "checked_url": "https://link.springer.com/article/10.3758/s13421-023-01402-w",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2023)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: três estudos com humanos (incluindo MTurk), controle vs. só correção vs. correção com desqualificação da fonte",
    "Materiais neutros: sim, incêndio fictício em galpão com fontes fictícias; sem conteúdo político ou de saúde (conferido nos métodos)",
    "Amostra: não informado no resumo",
    "Achado principal: as correções mudam a percepção da fonte da desinformação, e isso medeia a mudança de crença",
    "Trecho literal do resumo: \"perceptions of the misinformation source is one mechanism that can cause changes in belief in misinformation\""
   ]
  },
  {
   "doi": "10.3758/s13421-024-01520-z",
   "title": "How do forewarnings and post-warnings affect misinformation reliance? The impact of warnings on the continued influence effect and belief regression",
   "authors": [
    "K. A. Buczel",
    "A. Siwiak",
    "M. Szpitalak",
    "R. Polczyk"
   ],
   "year": 2024,
   "venue": "Memory & Cognition",
   "checked_url": "https://link.springer.com/article/10.3758/s13421-024-01520-z",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2024)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: dois experimentos com humanos, aviso prévio e aviso posterior, com teste de acompanhamento após uma semana",
    "Materiais neutros: sim, incêndio fictício em galpão, 13 mensagens; sem conteúdo político ou de saúde nos materiais (conferido nos métodos)",
    "Amostra: \"In two experiments (N = 337)\"",
    "Achado principal: o aviso prévio reduziu a dependência da desinformação, mas o aviso posterior não, e a proteção diminuiu ao longo da semana",
    "Trecho literal do resumo: \"while a forewarning did reduce reliance on misinformation\""
   ]
  },
  {
   "doi": "10.3758/s13421-020-01046-0",
   "title": "Is it smart to read on your phone? The impact of reading format and culture on the continued influence of misinformation",
   "authors": [
    "Y. Xu",
    "R. Wong",
    "S. He",
    "A. Veldre",
    "S. Andrews"
   ],
   "year": 2020,
   "venue": "Memory & Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.3758/s13421-020-01046-0\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2020)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: experimentos com humanos em duas culturas (Austrália e China), leitura no celular vs. outros formatos, relatos com retratação",
    "Materiais neutros: sim, relatos fictícios de eventos (ex.: incêndio), sem conteúdo político ou de saúde (conferido nos métodos)",
    "Amostra: não informado no resumo",
    "Achado principal: ler no celular reduziu a chance de o leitor notar a retratação",
    "Trecho literal do resumo: \"reading on a mobile phone reduced the likelihood that readers noticed the retraction\""
   ]
  },
  {
   "doi": "10.1016/j.cognition.2024.106000",
   "title": "Relative source credibility affects the continued influence effect: Evidence of rationality in the CIE",
   "authors": [
    "C. V. Hey",
    "M. L. Schaper",
    "U. J. Bayen"
   ],
   "year": 2025,
   "venue": "Cognition",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"10.1016/j.cognition.2024.106000\"&resultType=core&format=json",
   "criteria_met": [
    "Tema CIE: sim",
    "Período: sim (2025)",
    "Periódico revisado por pares: sim",
    "Tipo de estudo e método: dois experimentos com humanos, notícia com afirmação e retratação de fontes de alta ou baixa credibilidade, com controle",
    "Materiais neutros: sim, notícia fictícia (conforme descrição do resumo); não abri os métodos",
    "Amostra: \"N = 151, N = 146\"",
    "Achado principal: o efeito depende da credibilidade relativa do informante e do retratador, e com credibilidade igual ele persiste",
    "Trecho literal do resumo: \"When the informant was less credible than the retractor, participants showed no CIE, in line with a rational account.\""
   ]
  }
 ],
 "notes": "Entreguei 16 artigos, não os 25 pedidos. Preferi menos e certo a completar com artigos não conferidos ou que violam critérios. Todos os 16 estão entre 2018 e 2025, são artigos de periódico com experimento em humanos e retratação ou correção, e têm materiais neutros.\n\nComo conferi: abri metadados e resumos no Europe PMC e na Crossref. Para a maioria, li também os métodos (PMC, PLOS, Frontiers, Springer). A exceção é Hey et al. 2025, cujos métodos não abri; a neutralidade vem só da descrição \"notícia fictícia\" no resumo. Os DOIs vêm desses registros. Os links doi.org dos artigos da Springer, PLOS e Sage redirecionaram para o artigo certo.\n\nLimitações:\n- Os trechos literais têm no máximo ~125 caracteres. A ferramenta de leitura só devolve citações curtas, então cada trecho é uma frase ou oração do resumo que sustenta o achado.\n- Anos: usei o ano de emissão da Crossref quando o abri. Susmann & Wegener (10.3758/s13421-021-01232-8) saiu online em 2021 e na edição impressa de 2022. Connor Desai & Reimers (10.3758/s13428-018-1066-z) saiu em 2018 e na edição de 2019. Os demais usam o ano do Europe PMC. Todos ficam dentro de 2018–2025.\n- Siebert & Siebert 2023 trata de \"belief perseverance\" após retratação, fenômeno equivalente ao CIE. Não confirmei se o resumo usa o termo \"continued influence\". Susmann & Wegener 2023 (10.3758/s13421-022-01374-3) mede a credibilidade da retratação, além do endosso da desinformação e das inferências.\n- Em alguns estudos os métodos não dizem \"fictício\", mas descrevem relatos de eventos construídos para a pesquisa (Ecker & Antonio 2021, Sanderson et al. 2023, McIlhiney et al. 2023).\n\nExcluídos por materiais mistos, health ou político (decisão do pesquisador):\n- Buczel et al. 2022 (10.1371/journal.pone.0267463): um dos seis cenários é político (demissão de político) e a inoculação usa um debate sobre uma substância alimentar.\n- Ecker et al. 2024, source discreditation (10.1186/s41235-024-00581-7): inclui artigo fictício sobre tratamento da menopausa.\n- O'Rear & Radvansky (10.3758/s13421-019-00967-9): os Experimentos 1 e 2 são neutros, mas o Experimento 3 inclui paciente de esclerose múltipla e recall de espinafre contaminado.\n- Cohen et al. 2024 (política), Pluviano 2022 e van Huijstee 2021 (vacinas/COVID), Hu 2025 e Chang & van Swol 2023 (saúde), Greene & Murphy 2023 (notícias falsas políticas/COVID, não confirmado nos métodos).\n\nPlausíveis, mas não confirmados nos métodos e por isso não incluídos. O motivo é paywall, bloqueio de acesso ou PDF ilegível:\n- Brydges et al. 2018, Intelligence (10.1016/j.intell.2018.03.009; resumo \"Participants (N = 216)\").\n- Connor Desai et al. 2020, Cognition (10.1016/j.cognition.2020.104453; \"lay reasoners (N = 101)\").\n- Buczel et al. 2025, QJEP (10.1177/17470218251336232; \"In two experiments (N = 441)\").\n- McIlhiney et al. 2022, QJEP (10.1177/17470218211048986).\n- Mickelberg et al. 2024, Collabra (10.1525/collabra.92332).\n- Rich et al. 2023, JEP: Applied (10.1037/xap0000454).\n- Edelijn et al. 2024, JEP: Applied (10.1037/xap0000480).\n- Guo et al. 2025, Brain and Cognition (10.1016/j.bandc.2025.106290).\n- Sanna & Lagnado 2025, Cognition (10.1016/j.cognition.2025.106090).\n- Ecker & Rodricks 2020, JARMAC (10.1016/j.jarmac.2020.08.003; sem resumo na Crossref).\n- Miller et al. 2021, Applied Cognitive Psychology (10.1002/acp.3818). O DOI 10.1002/acp.3939 (2022) tem o mesmo título e é provável duplicata ou correção.\n- Jia et al. 2020, 2024; Liu et al. 2023, 2024; Jin et al. 2022; Susmann & Wegener 2023, PSPB (10.1177/01461672221077519; o tema dos estímulos é \"atitudes\" e não pude ver).\n\nFora do período ou do tipo de documento: Wilkes & Leatherbarrow 1988 e Johnson & Seifert 1994 (pré-2018), Walter & Tukachinsky 2019 (metanálise), Chan 2023 (metanálise), a edição de 2026 de Memory & Cognition (10.3758/s13421-026-01918-x) e as versões PsyArXiv.\n\nO OpenAlex devolveu HTTP 429 e o SciELO não foi consultado diretamente, então a cobertura em português (SciELO) não foi verificada. A rodada seguinte pode usar uma sessão com acesso institucional aos periódicos pagos para fechar os itens \"plausíveis\" acima e chegar mais perto de 25."
}