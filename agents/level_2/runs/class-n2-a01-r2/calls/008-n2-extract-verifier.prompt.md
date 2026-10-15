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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre o efeito de influência continuada da informação falsa (continued influence effect), isto é, o quanto as pessoas continuam a se apoiar em uma informação falsa depois de ela ser corrigida ou retratada. Restrições: apenas experimentos com participantes humanos que meçam crença ou raciocínio depois de uma correção ou retratação; os materiais devem ser neutros (cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde); exclua estudos com desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

LISTA FINAL A VERIFICAR:
{
 "items": [
  {
   "doi": "10.3758/s13421-021-01232-8",
   "title": "The role of discomfort in the continued influence effect of misinformation",
   "authors": [
    "Mark W. Susmann",
    "Duane T. Wegener"
   ],
   "year": 2022,
   "venue": "Memory & Cognition",
   "study_type": "Estudo empírico experimental (3 estudos), artigo de periódico",
   "method": "Experimentos online com participantes humanos: retratação de desinformação em relato fictício de incêndio em depósito; medida do desconforto, da crença e do uso da desinformação; no Estudo 3, manipulação da interpretação do desconforto.",
   "sample_size": "não informado no resumo",
   "main_finding": "As retratações geram desconforto psicológico, que prediz a crença e o uso continuados da desinformação, e mudar a interpretação desse desconforto torna a retratação mais eficaz.",
   "abstract_quote": "Studies 1 and 2 found that retractions of misinformation elicit psychological discomfort, and this discomfort predicts continued belief in and use of misinformation."
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
   "study_type": "Estudo empírico experimental (2 experimentos), artigo de periódico",
   "method": "Experimentos online com relatos fictícios de eventos em estilo de notícia; manipulação da confiabilidade e da expertise da fonte da retratação; perguntas de inferência e medida da crença na retratação.",
   "sample_size": "não informado no resumo",
   "main_finding": "A confiabilidade da fonte, e não a expertise, influencia a eficácia da retratação, mas ainda ocorre influência continuada substancial mesmo com retratações muito críveis.",
   "abstract_quote": "In two experiments, we found that source trustworthiness but not source expertise indeed influences retraction effectiveness, with retractions from low-trustworthiness sources entirely ineffective."
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
   "study_type": "Estudo empírico experimental (3 experimentos), artigo de periódico",
   "method": "Paradigma de influência continuada com narrativas de evento, retratação explícita, sonda adicional sobre aceitar ou não a retratação e perguntas de inferência.",
   "sample_size": "não informado no resumo",
   "main_finding": "Parte da influência continuada vem de pessoas que não aceitam a retratação: quem a aceitou usou menos a informação incorreta, e quem não aceitou se saiu como o grupo sem correção.",
   "abstract_quote": "Overall, these findings suggest that at least some of the evidence for the continued use of retracted information may be due to some people not accepting the retraction, even in the absence of external motivation to disregard it."
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Leitores de inglês e de chinês leram textos em celular ou em outro formato, com informação crítica retratada ou não; medidas de memória e de inferência.",
   "sample_size": "não informado no resumo",
   "main_finding": "Ler no celular reduziu a chance de o leitor notar a retratação e a revisão das inferências, especialmente entre os leitores de chinês.",
   "abstract_quote": "reading on a mobile phone reduced the likelihood that readers noticed the retraction"
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
   "study_type": "Estudo empírico experimental (experimentos online, um deles pré-registrado), artigo de periódico",
   "method": "Paradigma de influência continuada online (relato de evento com uma afirmação corrigida depois), comparando perguntas de inferência abertas e fechadas.",
   "sample_size": "Exp. 1A, n = 78; Exp. 1B, n = 75; Exps. 2A and 2B, n = 323",
   "main_finding": "O efeito de influência continuada apareceu em todas as condições, com número semelhante de referências à desinformação em perguntas abertas e fechadas.",
   "abstract_quote": "We observed the CIE in all conditions: Participants continued to refer to the misinformation following a correction, and their references to the target misinformation were broadly similar in number across open- and closed-ended questions."
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
   "study_type": "Estudo empírico experimental (3 estudos), artigo de periódico",
   "method": "Estudos online com relatos fictícios curtos; manipulação de explicação alternativa, correção direta da desinformação e importância do conteúdo.",
   "sample_size": "não informado no resumo",
   "main_finding": "Oferecer uma explicação alternativa reduziu de forma consistente o efeito de influência continuada, às vezes eliminando-o quando combinada com a correção direta.",
   "abstract_quote": "alternative provision consistently resulted in CIE reduction"
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Experimento com inoculação x controle e correção de fonte mais ou menos confiável, usando cenários fictícios; medidas de crença na desinformação, crença na retratação e dependência da desinformação (inferências).",
   "sample_size": "não informado no resumo",
   "main_finding": "Participantes inoculados dependeram menos da desinformação quando a correção vinha de fonte muito confiável, e sem inoculação a confiabilidade da fonte não fez diferença.",
   "abstract_quote": "However, inoculated participants relied on misinformation less when the correction came from a highly credible source."
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Experimento em que a crença persiste depois da retratação de uma desinformação (resumo de estudo inventado sobre bombeiros); comparação de três técnicas de redução (counter-speech, awareness training e counter-explanation) com opiniões medidas quatro vezes.",
   "sample_size": "N = 251 participants",
   "main_finding": "A técnica de counter-speech foi a mais eficaz para reduzir a perseverança da crença após a retratação.",
   "abstract_quote": "The CS technique, with a very large effect size, is the most effective among the three techniques."
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
   "study_type": "Estudo empírico experimental (2 experimentos), artigo de periódico",
   "method": "Paradigma de influência continuada com relatos de evento fictícios e fronteira espacial de segmentação de evento entre a informação falsa e a retratação.",
   "sample_size": "não informado no resumo",
   "main_finding": "A fronteira de evento não teve efeito no Experimento 1 e reduziu o efeito de influência continuada no Experimento 2, o que favorece as explicações por recuperação.",
   "abstract_quote": "While Experiment 1 showed no impact of an event boundary, Experiment 2 yielded evidence that an event boundary resulted in a reduced CIE."
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
   "study_type": "Estudo empírico de diferenças individuais (correlacional/modelagem de variáveis latentes), artigo de periódico",
   "method": "Participantes fizeram tarefas de função executiva e uma tarefa de influência continuada (relatos de evento retratados ou não, com inferências); análise de correlação e modelagem de equações estruturais.",
   "sample_size": "não informado no resumo",
   "main_finding": "A função executiva prediz a suscetibilidade ao efeito de influência continuada, em especial a atualização da memória de trabalho.",
   "abstract_quote": "Results showed that EF can predict susceptibility to the CIE, especially the factor of working-memory updating."
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
   "study_type": "Estudo empírico experimental (3 experimentos), artigo de periódico",
   "method": "Experimentos de recordação colaborativa (revezamento x livre) depois de relatos com retratação, em diferentes intervalos de recordação; medidas de memória e inferência.",
   "sample_size": "não informado no resumo",
   "main_finding": "A colaboração por revezamento mitigou de forma consistente o efeito de influência continuada, enquanto o efeito da colaboração livre dependeu do tempo de recordação.",
   "abstract_quote": "Results revealed that turn-taking collaboration consistently mitigates the CIE, while the effect of free collaboration on misinformation correction is moderated by recall time."
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
   "study_type": "Estudo empírico experimental (3 experimentos), artigo de periódico",
   "method": "Participantes formaram impressões de uma pessoa fictícia a partir de afirmações de comportamento; uma afirmação negativa foi depois retratada ou não.",
   "sample_size": "não informado no resumo",
   "main_finding": "Houve influência continuada da afirmação retratada em um experimento, e nos outros dois ela foi totalmente descontada.",
   "abstract_quote": "Evidence for the continued influence of the retracted behaviour statement was found in one experiment."
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
   "study_type": "Estudo empírico experimental (4 experimentos), artigo de periódico",
   "method": "Participantes formaram uma impressão de um protagonista fictício (John) a partir de descrições de comportamento, com desinformação negativa ou positiva depois retratada; impressões registradas após cada descrição.",
   "sample_size": "não informado no resumo",
   "main_finding": "Em todos os experimentos a desinformação retratada foi totalmente descontada, sem influência continuada nas impressões sobre a pessoa.",
   "abstract_quote": "Furthermore, in each experiment participants fully discounted the misinformation once retracted, regardless of whether the misinformation was negative or positive."
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Participantes viram comportamentos atribuídos a uma pessoa fictícia, com ou sem um comportamento de violência doméstica retratado; avaliação de traços, previsão de comportamento e medida indireta (avaliação do rosto).",
   "sample_size": "não informado no resumo",
   "main_finding": "A alegação desacreditada não influenciou as avaliações explícitas de traços nem as previsões de comportamento, havendo apenas indício tentativo de efeito na medida indireta.",
   "abstract_quote": "Discredited misinformation was found to influence neither trait ratings of the person nor behavior predictions."
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
   "study_type": "Estudo empírico experimental (2 experimentos), artigo de periódico",
   "method": "Participantes leram uma notícia fictícia em que a informação original e a retratação vinham de fontes de alta ou baixa credibilidade, manipuladas de forma independente, e foram comparados a um grupo controle.",
   "sample_size": "In two experiments (N = 151, N = 146)",
   "main_finding": "Houve efeito de influência continuada quando o informante era mais crível que o retratador e não houve quando era menos crível, o que é coerente com uma explicação racional, mas houve CIE também com credibilidade igual no Experimento 2.",
   "abstract_quote": "When the informant was less credible than the retractor, participants showed no CIE, in line with a rational account."
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Participantes leram quatro cenários militares de tomada de decisão, dois com informação falsa depois retratada e dois sem; avaliação do raciocínio inferencial e da tomada de decisão.",
   "sample_size": "A total of 61 participants",
   "main_finding": "Não houve evidência de influência continuada, mas surgiu um efeito de supercorreção na tomada de decisão.",
   "abstract_quote": "The results did not reveal any evidence of the CIE, but an overcorrection effect emerged in decision‐making."
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
   "study_type": "Estudo empírico experimental (réplica direta), artigo de periódico",
   "method": "Delineamento entre grupos com amostra francófona: um grupo leu texto com informação falsa retratada e o controle leu o mesmo texto sem ela; comparação das inferências.",
   "sample_size": "FI group (n = 21) ... control group (n = 23)",
   "main_finding": "Os resultados confirmam os do estudo original de Johnson e Seifert (1994) e estendem o paradigma a uma população francófona.",
   "abstract_quote": "The results confirm those of the original study, supporting the validity of Johnson and Seifert's paradigm (1994) and extending its applicability to a French-speaking population."
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
   "study_type": "Estudo empírico experimental (2 experimentos), artigo de periódico",
   "method": "Experimentos online comparando correção simples com correção que explica a origem da desinformação (engano intencional ou erro); perguntas de inferência sobre eventos.",
   "sample_size": "não informado no resumo",
   "main_finding": "Explicar a origem da desinformação, deliberada ou acidental, provavelmente não torna a correção mais eficaz do que apenas dizer que ela é falsa.",
   "abstract_quote": "whether deliberate or accidental, may not be an effective correction strategy over and above stating that the misinformation is false."
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
   "study_type": "Estudo empírico experimental, artigo de periódico",
   "method": "Participantes ouviram relatos com correções que repetiam a desinformação num simulador de direção; número de correções (única x múltipla) e carga cognitiva (tarefa de matemática) manipulados; raciocínio inferencial.",
   "sample_size": "não informado no resumo",
   "main_finding": "Correções múltiplas foram mais eficazes que uma correção única, e a carga cognitiva reduziu a eficácia das correções, sem evidência de efeito backfire de familiaridade.",
   "abstract_quote": "Multiple corrections were more effective than a single correction; cognitive load reduced correction effectiveness, with a single correction entirely ineffective under load."
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
   "study_type": "Estudo empírico experimental (2 estudos), artigo de periódico",
   "method": "Estudos online que manipularam expertise, confiabilidade e interesse da fonte da retratação, com medidas de credibilidade da retratação, crença continuada na desinformação e inferências.",
   "sample_size": "não informado no resumo",
   "main_finding": "Retratações de fonte especialista são mais acreditadas e geram menos crença continuada na desinformação que as de fonte não especialista, mas só quando a fonte não tem interesse em emitir a retratação.",
   "abstract_quote": "Study 1 demonstrated that retractions from an expert source are believed more and lead to less continued belief in misinformation than retractions from an inexpert source while controlling for perceptions of trustworthiness."
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
   "study_type": "Estudo empírico experimental (3 estudos, o último pré-registrado), artigo de periódico",
   "method": "Estudos com correção externa, controle e derrogação da fonte da desinformação; medidas de percepção da fonte, crença na desinformação e raciocínio inferencial.",
   "sample_size": "não informado no resumo",
   "main_finding": "As percepções sobre a fonte da desinformação são um mecanismo pelo qual a correção muda a crença na desinformação.",
   "abstract_quote": "These studies suggest that perceptions of the misinformation source is one mechanism that can cause changes in belief in misinformation, and changes in the perception of a source can be achieved simply by correcting the source or through other means."
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
   "study_type": "Estudo empírico experimental (2 experimentos), artigo de periódico",
   "method": "Avisos dados antes ou depois da desinformação (entre a desinformação e a retratação, ou logo antes do teste), com reteste após 7 dias; dependência da desinformação medida por inferências.",
   "sample_size": "In two experiments (N = 337)",
   "main_finding": "O aviso prévio reduziu a dependência da desinformação, os avisos retrospectivos não, e o efeito protetor do aviso prévio não foi durável.",
   "abstract_quote": "However, the protective effect of the forewarning was not durable, as shown by the fact that reliance on the misinformation increased for over 7 days following the first testing, despite continued memory of the retraction."
  },
  {
   "doi": "10.2224/sbp.13662",
   "title": "The effect of correction timing on the continued influence effect of misinformation with different relevance",
   "authors": [
    "Lina Jia"
   ],
   "year": 2024,
   "venue": "Social Behavior and Personality: an international journal",
   "study_type": "Estudo empírico experimental (2 estudos), artigo de periódico",
   "method": "Delineamento misto com relevância da informação e intervalo da correção (imediata, 1 dia, 1 semana), usando histórias fictícias de incidentes cotidianos e estratégias de correção eficientes.",
   "sample_size": "two studies with 86 participants",
   "main_finding": "O efeito do intervalo entre desinformação e correção dependeu da relevância da informação e do método de correção, e o melhor momento para corrigir variou entre os métodos.",
   "abstract_quote": "Additionally, the best timing for corrections differed across various correction methods."
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
   "study_type": "Estudo empírico experimental de neuroimagem (fMRI de tarefa), artigo de periódico",
   "method": "Tarefa de fMRI com condição de retratação x controle; escores de inferência, ativação cerebral e conectividade funcional nas fases de codificação e recuperação.",
   "sample_size": "não informado no resumo",
   "main_finding": "Os escores de inferência foram maiores na condição de retratação que no controle (o efeito existe), com menor ativação do giro temporal médio esquerdo na codificação e menor ativação frontal e do cíngulo anterior na recuperação.",
   "abstract_quote": "The results showed that the inference scores of retraction condition were significantly higher than that of control condition, and the CIEM exists."
  }
 ],
 "search_notes": "Havia 24 candidatos aprovados, então usei todos. O pedido original falava em 25 artigos, e a lista aprovada tem 24, o que deixa uma vaga em aberto. Abri o resumo de cada artigo via Europe PMC, PMC, PubMed, Semantic Scholar, Crossref e os sites dos periódicos (Acta Psychologica Sinica e Social Behavior and Personality). Os trechos de abstract_quote e as amostras vêm do texto dos resumos. As páginas do editor (Springer, Wiley, Collabra) deram 403 ou redirecionamento. Por isso li o resumo de Collabra pelo Crossref e o de O'Rear pelo PubMed. Dois resumos vieram só por resumo parafraseado da ferramenta de leitura, sem texto integral: Xu et al. (2020) e Kan et al. (2021). Neles só o trecho citado foi confirmado como literal, e a ausência de amostra no resumo vem desse resumo parafraseado. McIlhiney et al. (2023) e Mickelberg et al. (2025) tiveram o trecho citado confirmado como literal, e a ausência de amostra vem do mesmo tipo de resumo parafraseado. Buczel et al. (2022) e outros 17 artigos tiveram o resumo conferido por inteiro: Susmann & Wegener 2022 e 2023, Westbrook et al., Siebert & Siebert, Chen et al., Sanderson et al. (2022 e 2023), Connor Desai & Reimers (2019 e 2023), Hey et al., Laurent et al. (2023 e 2024), Buczel et al. (2024), Ecker & Antonio, Ecker & Rodricks, Mickelberg et al. (2024), O'Rear & Radvansky, Jia e Jin et al. Tamanho de amostra só foi preenchido quando aparece no resumo. Nos outros casos usei \"não informado no resumo\". Sinalizações para o pesquisador decidir: (1) Ecker & Rodricks (2020) usa uma alegação fictícia de violência doméstica, que é emocionalmente carregada, embora sem tema político nem de saúde. (2) Buczel et al. (2022) tem \"vaccination\" só como metáfora no título. Um cenário envolve um político fictício, e a fase de inoculação usou um debate fictício sobre uma substância em alimentos. (3) Mickelberg et al. (2024, 2025) e Ecker & Rodricks tratam de impressões sobre pessoas fictícias, e não de relatos de eventos. (4) Laurent et al. (2024) usa cenários militares fictícios e encontrou supercorreção, não CIE. (5) Siebert & Siebert (2023) mede perseverança da crença depois da retratação, construto próximo do CIE e não o paradigma clássico. (6) Jia (2024) relata dois estudos com os mesmos 86 participantes. (7) Jin et al. (2022): o resumo não diz que o cenário é fictício. (8) Sanderson et al. (2023, JARMAC) tem como foco principal o backfire de familiaridade sob carga cognitiva. (9) Alguns resumos não informam o tema exato do material (Hey et al. 2025, Xu et al. 2020, McIlhiney et al. 2023), então a neutralidade veio dos métodos conferidos na etapa anterior. Os autores já estavam corrigidos na lista (Mikkelsen; Kennedy). Nada foi excluído por tema: nenhum artigo trata de política, eleições, vacinas nem COVID-19, e as menções a esses temas são só de introdução ou metáfora.\""
}