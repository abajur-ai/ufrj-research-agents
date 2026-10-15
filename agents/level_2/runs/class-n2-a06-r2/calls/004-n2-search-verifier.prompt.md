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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre os efeitos de manchetes caça-cliques (clickbait) sobre leitores e usuários de notícias. Restrições: apenas estudos empíricos com dados de leitores ou usuários (experimentos, questionários, medidas fisiológicas como EEG ou rastreamento ocular, ou dados de cliques e engajamento); exclua modelos computacionais de detecção ou classificação de clickbait, análises apenas linguísticas de manchetes sem dados de leitores e estudos com recorte político ou eleitoral. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CANDIDATOS A VERIFICAR:
{
 "candidates": [
  {
   "doi": "10.1108/oir-05-2018-0172",
   "title": "Shocking secret you won't believe! Emotional arousal in clickbait headlines: An eye-tracking analysis",
   "authors": [
    "Supavich (Fone) Pengnate"
   ],
   "year": 2019,
   "venue": "Online Information Review",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1108/OIR-05-2018-0172?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1108/oir-05-2018-0172): journal-article, v.43 n.7, 2019.",
    "Tipo/método: experimento de laboratório com eye tracker (dilatação pupilar) + Self-Assessment Manikin, comparando manchetes de notícia, clickbait e controle neutro.",
    "Amostra: não informado no resumo.",
    "Achado: manchetes clickbait geram mais excitação emocional que as neutras, porém menos que as manchetes de notícia, e a excitação prediz a intenção de ler.",
    "Trecho: \"In general, clickbait headlines generate a higher level of emotional arousal than do the neutral headlines but a lower level than the news headlines.\"",
    "Critérios: tema (leitor), 2019, periódico, dados próprios de usuários, sem recorte político."
   ]
  },
  {
   "doi": "10.58729/1941-6679.1440",
   "title": "Effects of Clickbait Headlines on User Responses: An Empirical Investigation",
   "authors": [
    "Supavich Fone Pengnate",
    "Jeffrey Chen",
    "Alex Young"
   ],
   "year": 2021,
   "venue": "Journal of International Technology and Information Management",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.58729/1941-6679.1440?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.58729/1941-6679.1440): journal-article, v.30 n.3, 2021.",
    "Tipo/método: experimento com dois grupos de manchetes (notícia tradicional vs. clickbait) e modelagem de equações estruturais.",
    "Amostra: não informado no resumo.",
    "Achado: clickbait provoca excitação e curiosidade; a curiosidade é o principal determinante da intenção de ler e a qualidade percebida do conhecimento, da intenção de compartilhar.",
    "Trecho: \"The findings suggest that clickbait headlines can evoke users' arousal and curiosity.\"",
    "Critérios: tema, 2021, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.1027/1864-1105/a000298",
   "title": "Exaggerated and Questioning Clickbait Headlines and Their Influence on Media Learning",
   "authors": [
    "Nick Carcioppolo",
    "Di Lun",
    "Soroya Julian McFarlane"
   ],
   "year": 2022,
   "venue": "Journal of Media Psychology",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1027/1864-1105/a000298?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1027/1864-1105/a000298): journal-article, v.34 n.1, 2022.",
    "Tipo/método: dois experimentos online fatoriais 3 (tipo de manchete: precisa, clickbait-pergunta, clickbait-exagerada) × 2 (exposição: só manchete, artigo completo).",
    "Amostra: \"N = 629\" (Estudo 1, adultos dos EUA) e \"N = 1,674\" (Estudo 2, replicação).",
    "Achado: ler o artigo completo com manchete precisa dá o melhor reconhecimento e compreensão, e a correção dentro do texto não anula o efeito negativo da manchete clickbait.",
    "Trecho: \"Key results suggest that reading the full article with an accurate headline resulted in the highest recognition and comprehension, and reading correcting information within an article is likely not enough to overcome the deleterious impact of a clickbait headline.\"",
    "Critérios: tema (memória/compreensão), 2022, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.1002/acp.4134",
   "title": "You won't believe it! Truth judgments for clickbait headlines benefit (but less so) from prior exposure",
   "authors": [
    "Jérémy Béna",
    "Martin Rouard",
    "Olivier Corneille"
   ],
   "year": 2023,
   "venue": "Applied Cognitive Psychology",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/acp.4134?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1002/acp.4134): journal-article, v.37 n.6, 2023 (online set/2023).",
    "Tipo/método: dois experimentos comportamentais sobre o efeito de verdade ilusória (exposição prévia a enunciados em formato clickbait).",
    "Amostra: \"N = 241\" (Exp. 1) e \"N = 291\" (Exp. 2).",
    "Achado: a exposição prévia aumenta os julgamentos de verdade de manchetes clickbait, embora menos do que de enunciados regulares.",
    "Trecho: \"The present findings suggest that exposure to clickbait headlines can increase their content's truth judgments despite their overall lack of credibility, although to a lesser extent than for more regular statements.\"",
    "Critérios: tema (credibilidade/verdade percebida), 2023, periódico, dados próprios, sem recorte político. Observação: o resumo fala em 'clickbait headlines', mas os estímulos são enunciados em formato clickbait."
   ]
  },
  {
   "doi": "10.1371/journal.pone.0266743",
   "title": "Click me…! The influence of clickbait on user engagement in social media and the role of digital nudging",
   "authors": [
    "Anna-Katharina Jung",
    "Stefan Stieglitz",
    "Tobias Kissmer",
    "Milad Mirbabaie",
    "Tobias Kroll"
   ],
   "year": 2022,
   "venue": "PLOS ONE",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1371/journal.pone.0266743&resultType=core&format=json",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1371/journal.pone.0266743): journal-article, v.17 n.6, 2022.",
    "Tipo/método: análise de dados reais de engajamento (curtidas, compartilhamentos, comentários) de posts de veículos de notícias no Facebook.",
    "Amostra: \"more than 4,400 Facebook posts from 10 different news sources\".",
    "Achado: certas características (pontuação incomum, frases típicas de clickbait) aumentam a interação dos usuários e outras a reduzem.",
    "Trecho: \"certain features (e.g., unusual punctuation and common clickbait phrases) increase user interaction, whereas others decrease engagement with Facebook posts.\"",
    "Critérios: tema (engajamento), 2022, periódico, dados reais de usuários, notícias em mídia social, sem recorte político."
   ]
  },
  {
   "doi": "10.1080/21670811.2025.2505566",
   "title": "Emotion Sells: Rage Bait vs. Information Bait in Clickbait News Headlines on Social Media",
   "authors": [
    "Jieun Shin",
    "Chris DeFelice",
    "Soojong Kim"
   ],
   "year": 2025,
   "venue": "Digital Journalism",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/21670811.2025.2505566?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1080/21670811.2025.2505566): journal-article, 2025 (online 22/05/2025; edição v.13 n.7, 2025).",
    "Tipo/método: estudo com manchetes de notícias em mídia social e dados de engajamento da audiência, distinguindo 'information bait' e 'rage bait'.",
    "Amostra: não informado no resumo.",
    "Achado: manchetes 'rage bait' associam-se a maior engajamento e 'information bait' a menor engajamento.",
    "Trecho: \"rage bait headlines were linked to higher levels of audience engagement, while information bait was associated with lower engagement.\"",
    "Critérios: tema (engajamento), 2025, periódico, dados de engajamento. Observação: o resumo cita mídia 'conservadora' só como variável de caracterização do veículo, sem foco político."
   ]
  },
  {
   "doi": "10.1080/21670811.2024.2394764",
   "title": "Analyzing Sensationalism in News on Twitter (X): Clickbait Journalism by Legacy vs. Online-Native Outlets and the Consequences for User Engagement",
   "authors": [
    "Salman Khawar",
    "Mark Boukes"
   ],
   "year": 2025,
   "venue": "Digital Journalism",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/21670811.2024.2394764?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1080/21670811.2024.2394764): journal-article, v.13 n.8; online 24/09/2024, edição impressa 14/09/2025. Ano oficial da edição = 2025 (divergência com o online-first de 2024).",
    "Tipo/método: análise de conteúdo manual e automatizada de tuítes de veículos de notícias, ligada a métricas reais de engajamento (favoritos, retuítes).",
    "Amostra: \"1,440 tweets\" (análise manual) e \"25,600 tweets\" (análise automatizada).",
    "Achado: mais recursos sensacionalistas (clickbait) se associam a mais favoritos, e a análise automatizada mostrou efeito positivo também nos retuítes.",
    "Trecho: \"a positive relationship was found between the number of sensationalist features employed and the favorite count, confirming the effectiveness of clickbaits.\"",
    "Critérios: tema (engajamento), período, periódico, dados reais de engajamento, sem recorte político. Observação: parte do estudo é análise de conteúdo; o teste do efeito usa dados de usuários."
   ]
  },
  {
   "doi": "10.5897/jmcs2020.0715",
   "title": "Clickbait-style headlines and journalism credibility in Sub-Saharan Africa: Exploring audience perceptions",
   "authors": [
    "Flora Wanda Judith",
    "Samson Chipanjilo Baraka",
    "Gondwe Gregory",
    "Kerunga Joseph"
   ],
   "year": 2021,
   "venue": "Journal of Media and Communication Studies",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.5897/JMCS2020.0715?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.5897/jmcs2020.0715): journal-article, v.13 n.2, 31/05/2021.",
    "Tipo/método: estudo experimental com consumidores de notícias online na Zâmbia e na Tanzânia.",
    "Amostra: não informado no resumo.",
    "Achado: manchetes clickbait têm efeito negativo sobre a credibilidade jornalística percebida.",
    "Trecho: \"The findings suggest strong statistical evidence that clickbait headlines pose negatives effects on the perceptions of journalistic credibility in Zambia and Tanzania.\"",
    "Critérios: tema (credibilidade), 2021, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.1080/17512786.2019.1628658",
   "title": "Aggregation, Clickbait and Their Effect on Perceptions of Journalistic Credibility and Quality",
   "authors": [
    "Logan Molyneux",
    "Mark Coddington"
   ],
   "year": 2020,
   "venue": "Journalism Practice",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/17512786.2019.1628658?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1080/17512786.2019.1628658): journal-article, v.14 n.4; online 16/06/2019, edição impressa 20/04/2020. Ano oficial da edição = 2020 (divergência com o online-first de 2019).",
    "Tipo/método: dois experimentos online com artigos de notícias originais e agregados como estímulos.",
    "Amostra: não informado no resumo.",
    "Achado: manchetes clickbait podem reduzir a credibilidade e a qualidade percebidas.",
    "Trecho: \"Results also suggest clickbait headlines may lower perceptions of credibility and quality.\"",
    "Critérios: tema (credibilidade), período, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.1177/1461444819863408",
   "title": "The curiosity effect: Information seeking in the contemporary news environment",
   "authors": [
    "Joshua M. Scacco",
    "Ashley Muddiman"
   ],
   "year": 2020,
   "venue": "New Media & Society",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1177/1461444819863408?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1177/1461444819863408): journal-article, v.22 n.3; online 06/08/2019, edição impressa mar/2020. Ano oficial da edição = 2020 (divergência com o online-first de 2019).",
    "Tipo/método: experimento de laboratório + teste de campo (comportamento real de seleção em sites de jornais) comparando manchetes-resumo e manchetes de curiosidade (clickbait).",
    "Amostra: não informado no resumo (o resumo cita apenas 'nine local newspaper websites' no estudo de campo).",
    "Achado: manchetes-resumo elevam a adequação de informação percebida e a expectativa de engajamento, e a seleção de notícias nos sites também as favorece em relação às de curiosidade.",
    "Trecho: \"Study 2 determines that individuals' selection behavior on nine local newspaper websites also favors summary headlines.\"",
    "Critérios: tema (curiosidade, cliques), período, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.3390/info16020150",
   "title": "AI vs. Human-Authored Headlines: Evaluating the Effectiveness, Trust, and Linguistic Features of ChatGPT-Generated Clickbait and Informative Headlines in Digital News",
   "authors": [
    "Vasile Gherheș",
    "Marcela Alina Fărcășiu",
    "Mariana Cernicova-Buca",
    "Claudiu Coman"
   ],
   "year": 2025,
   "venue": "Information",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/info16020150?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.3390/info16020150): journal-article, v.16 n.2, 18/02/2025.",
    "Tipo/método: levantamento (questionário) sobre reações dos leitores a manchetes clickbait e informativas, escritas por humanos e geradas por IA, com análise linguística complementar.",
    "Amostra: \"a sample of 624 students from Timisoara, Romania\".",
    "Achado: os leitores consideram as manchetes clickbait enganosas e manipuladoras, e mais da metade relata queda de confiança em veículos que as usam com frequência.",
    "Trecho: \"In addition, 54.5% of respondents reported a decrease in trust regarding publications that frequently use clickbait techniques.\"",
    "Critérios: tema (confiança), 2025, periódico, dados próprios de leitores, sem recorte político."
   ]
  },
  {
   "doi": "10.1080/10447318.2022.2158262",
   "title": "Attention Grabbing through Forward Reference: An ERP Study on Clickbait and Top News Stories",
   "authors": [
    "Xin Li",
    "Jia Zhou",
    "Honglian Xiang",
    "Jingjing Cao"
   ],
   "year": 2024,
   "venue": "International Journal of Human–Computer Interaction",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/10447318.2022.2158262?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1080/10447318.2022.2158262): journal-article, v.40 n.11; online 28/12/2022, edição impressa 02/06/2024. Ano oficial da edição = 2024 (divergência com o online-first de 2022).",
    "Tipo/método: experimento de EEG/potenciais relacionados a eventos (N2b e P3a) com manchetes de notícias.",
    "Amostra: não informado no resumo.",
    "Achado: manchetes clickbait com recurso de referência antecipada (forward reference) atraem mais recursos atencionais e induzem alocação involuntária de atenção mais rápida.",
    "Trecho: \"the clickbait headlines with a forward-reference device attracted more attention resources and induced the involuntary attention allocation more quickly, compared with those without a forward-reference device.\"",
    "Critérios: tema (atenção), período, periódico, medida fisiológica, notícias, sem recorte político."
   ]
  },
  {
   "doi": "10.1080/17512786.2020.1793379",
   "title": "Here's What to Know About Clickbait: Effects of Image, Headline and Editing on Audience Attitudes",
   "authors": [
    "Fred Vultee",
    "G. Scott Burgess",
    "Darryl Frazier",
    "Kelsey Mesmer"
   ],
   "year": 2022,
   "venue": "Journalism Practice",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/17512786.2020.1793379?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1080/17512786.2020.1793379): journal-article, v.16 n.1; online 16/07/2020, edição impressa 02/01/2022. Ano oficial da edição = 2022 (divergência com o online-first de 2020).",
    "Tipo/método: estudo experimental sobre estilo de manchete (tradicional vs. clickbait), ilustração e edição do texto.",
    "Amostra: não informado no resumo.",
    "Achado: a edição é a maior influência sobre qualidade/credibilidade percebidas e condiciona se manchetes tradicionais ou clickbait se associam a melhor memória dos detalhes da notícia.",
    "Trecho: \"the presence of editing also influences whether traditional or clickbait headlines are associated with better memory for story details.\"",
    "Critérios: tema (credibilidade, memória), período, periódico, dados próprios, sem recorte político."
   ]
  },
  {
   "doi": "10.1108/intr-09-2019-0373",
   "title": "Seeing is not always believing: an exploratory study of clickbait in WeChat",
   "authors": [
    "Wenping Zhang",
    "Wei Du",
    "Yiyang Bian",
    "Chih-Hung Peng",
    "Qiqi Jiang"
   ],
   "year": 2020,
   "venue": "Internet Research",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1108/INTR-09-2019-0373?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1108/intr-09-2019-0373): journal-article, v.30 n.3, 2020 (online 13/03/2020). Ao verificar, o resumo recuperado pelo Semantic Scholar para este DOI descreve o estudo de dados longitudinais do WeChat; o Crossref confirma o mesmo conteúdo.",
    "Tipo/método: dados longitudinais reais de cliques/visitas de mais de 500 contas oficiais do WeChat, com mineração de texto para medir recursos retóricos e análise econométrica.",
    "Amostra: \"more than 500 WeChat official accounts\" (conforme o resumo; sem N de leitores).",
    "Achado: hipérbole, insinuação e retórica visual levam usuários a clicar, e há relação em U invertido entre o número de manchetes clickbait de um publicador e seu tráfego.",
    "Trecho: \"hyperbole, insinuation, and visual rhetoric entice users to click the baited headlines\"",
    "Critérios: tema (cliques), período, periódico, dados reais de cliques. Observação: contexto de mídia online/contas de publicação no WeChat; a mineração de texto serve para medir as variáveis, não para detectar clickbait."
   ]
  },
  {
   "doi": "10.1007/s11747-021-00830-x",
   "title": "Did clickbait crack the code on virality?",
   "authors": [
    "Prithwiraj Mukherjee",
    "Souvik Dutta",
    "Arnaud De Bruyn"
   ],
   "year": 2022,
   "venue": "Journal of the Academy of Marketing Science",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11747-021-00830-x?fields=title,abstract,year,venue,publicationTypes",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.1007/s11747-021-00830-x): journal-article, v.50 n.3, edição mai/2022 (online 29/01/2022).",
    "Tipo/método: experimento controlado + análise de dados secundários de compartilhamento (Twitter) de artigos de editores online.",
    "Amostra: \"19,386 articles from 27 leading online publishers\" (o N do experimento não aparece no resumo).",
    "Achado: artigos clickbait geram bem menos compartilhamentos que os não clickbait, e o clickbait leva a inferências de intenção manipuladora e depreciação da fonte.",
    "Trecho: \"We confirm that, on average, clickbait articles elicit far fewer shares than non-clickbait articles.\"",
    "Critérios: tema (compartilhamento, confiança na fonte), período, periódico, dados de usuários, sem recorte político. Observação: publicação de marketing; o contexto são artigos de editores online (mídia digital), o que pode merecer revisão do pesquisador."
   ]
  },
  {
   "doi": "10.24815/jr.v8i3.47278",
   "title": "The Effect of Clickbait Headlines on Tribunnews.Com Online News Articles on the Reading Interest of Generation Z at FKI UMS",
   "authors": [
    "Dedy Pradana Putra",
    "Budi Santoso"
   ],
   "year": 2025,
   "venue": "Riwayat: Educational Journal of History and Humanities",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.24815/jr.v8i3.47278?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.24815/jr.v8i3.47278): journal-article, v.8 n.3, 03/07/2025.",
    "Tipo/método: levantamento quantitativo por questionário com estudantes da Geração Z sobre manchetes clickbait do portal Tribunnews.com.",
    "Amostra: \"113 respondents\".",
    "Achado: o uso de manchetes clickbait influencia significativamente o interesse de leitura, aumentando a curiosidade mas também gerando tédio ou decepção quando o conteúdo não corresponde.",
    "Trecho: \"The results indicate that the use of clickbait headlines has a significant influence on reading interest.\"",
    "Critérios: tema, 2025, periódico (de menor impacto), dados próprios de leitores, sem recorte político."
   ]
  },
  {
   "doi": "10.29240/ajis.v10i2.13175",
   "title": "The Impact of Clickbait News on Online Media Audiences from the Perspective of Islamic Communication: A Case Study of PALTV.disway.id Palembang",
   "authors": [
    "Juan Muliawan",
    "K.A Bukhori",
    "Fifi Hasmawati"
   ],
   "year": 2025,
   "venue": "AJIS: Academic Journal of Islamic Studies",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.29240/ajis.v10i2.13175?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.29240/ajis.v10i2.13175): journal-article, 09/11/2025, pp. 471–494.",
    "Tipo/método: estudo de caso qualitativo com observação, entrevistas em profundidade com leitores ativos, jornalistas e líderes religiosos, e análise documental.",
    "Amostra: não informado no resumo.",
    "Achado: notícias clickbait geram mal-entendidos e queda na qualidade da compreensão dos leitores, além de maior ceticismo em relação aos veículos.",
    "Trecho: \"The findings indicate that clickbait news frequently leads to information misunderstanding and a decline in the quality of readers' Islamic understanding, especially when headlines are not aligned with the content.\"",
    "Critérios: tema (compreensão, confiança), 2025, periódico, entrevistas com leitores, sem recorte político."
   ]
  },
  {
   "doi": "10.14710/anuva.6.4.455-464",
   "title": "Perspektif Mahasiswa S-1 Ilmu Perpustakaan Universitas Diponegoro dalam Menanggapi Judul Clickbait pada Portal Berita Online di Indonesia",
   "authors": [
    "Nurul Chakimah Mutharoh",
    "Rukiyah"
   ],
   "year": 2022,
   "venue": "Anuva: Jurnal Kajian Budaya, Perpustakaan, dan Informasi",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.14710/anuva.6.4.455-464?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.14710/anuva.6.4.455-464): journal-article, v.6 n.4, 14/11/2022.",
    "Tipo/método: estudo de caso qualitativo com observação, entrevistas e estudo documental com informantes selecionados por snowball sampling.",
    "Amostra: não informado no resumo.",
    "Achado: os estudantes consideram que os títulos clickbait usam palavras bombásticas demais e que os jornalistas priorizam o título, deixando o conteúdo às vezes impreciso.",
    "Trecho: \"terhadap judul clickbait yang ada saat ini menurut mereka terlalu banyak menggunakan kata yang bombastis dan jurnalis saat ini hanya mementingkan judul sehingga isi berita terkadang kurang akurat.\"",
    "Critérios: tema (percepção de leitores), 2022, periódico, entrevistas, portais de notícias, sem recorte político."
   ]
  },
  {
   "doi": "10.47233/jkomdis.v4i2.1777",
   "title": "Dampak Penggunaan Clickbait pada Judul Berita di Tribunnews.com terhadap Minat Baca Mahasiswa Ilmu Komunikasi Universitas Singaperbangsa Karawang Angkatan 2020",
   "authors": [
    "Sheila Mohammada",
    "Mayasari Mayasari",
    "Tri Widya Budhiharti"
   ],
   "year": 2024,
   "venue": "JKOMDIS: Jurnal Ilmu Komunikasi dan Media Sosial",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.47233/jkomdis.v4i2.1777?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.47233/jkomdis.v4i2.1777): journal-article, v.4 n.2, 04/07/2024.",
    "Tipo/método: pesquisa quantitativa com amostragem não probabilística intencional (purposive) entre estudantes de comunicação.",
    "Amostra: não informado no resumo.",
    "Achado: o uso de manchetes clickbait no Tribunnews.com tem efeito significativo sobre o interesse de leitura dos estudantes.",
    "Trecho (com os erros de grafia do original): \"The results of research and discussion showed that the use of clickbait headline newsdan a significant effect on students' reading interest.\"",
    "Critérios: tema, 2024, periódico (de menor impacto), dados próprios de leitores, sem recorte político."
   ]
  },
  {
   "doi": "10.35967/jkms.v12i2.7526",
   "title": "Opini Pembaca Berita dalam Menggunakan Clickbait di Media Online Tribunnews.com",
   "authors": [
    "Lobrianti Elsalsa",
    "Tutut Ismi Wahidar"
   ],
   "year": 2023,
   "venue": "Jurnal Ilmu Komunikasi (JKMS)",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.35967/jkms.v12i2.7526?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.35967/jkms.v12i2.7526): journal-article, v.12 n.2, 2023.",
    "Tipo/método: pesquisa qualitativa descritiva com observação, entrevistas e documentação com leitores.",
    "Amostra: não informado no resumo.",
    "Achado: os leitores formam opinião só pelo título, ficam mais curiosos e se decepcionam quando título e conteúdo divergem.",
    "Trecho: \"pembaca menyimpulkan pendapatnya sendiri ketika baru membaca judul dan dampak yang dirasakan menjadi semakin penasaran untuk membaca berita tersebut dan merasa kecewa jika judul dan isi yang dituliskan berbeda.\"",
    "Critérios: tema (curiosidade, emoção), 2023, periódico (de menor impacto), entrevistas com leitores, sem recorte político."
   ]
  },
  {
   "doi": "10.36080/ag.v10i2.1947",
   "title": "Pengaruh Berita Clickbait Terhadap Kepercayaan pada Media di Era Attention Economy",
   "authors": [
    "Nurisma Rahmatika",
    "Guntur Prisanto"
   ],
   "year": 2022,
   "venue": "Avant Garde",
   "checked_url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.36080/ag.v10i2.1947?fields=title,abstract,year,venue",
   "criteria_met": [
    "Metadados (Crossref https://api.crossref.org/works/10.36080/ag.v10i2.1947): journal-article, v.10 n.2, 12/12/2022.",
    "Tipo/método: levantamento quantitativo com questionário fechado entre millennials de Jacarta Leste que leem notícias em portais online.",
    "Amostra: \"A purposive sample technique was used to select 100 respondents\".",
    "Achado: segundo o resumo, o clickbait reduziu a confiança na mídia em 28,4%, embora os respondentes continuem confiando em veículos que o publicam, desde que a notícia seja confiável.",
    "Trecho: \"The findings demonstrated that clickbait news reduced media confidence by 28.4%.\"",
    "Critérios: tema (confiança na mídia), 2022, periódico (de menor impacto), dados próprios de leitores, sem recorte político. Observação: o resumo é ambíguo ao interpretar o resultado ('favorable effect')."
   ]
  }
 ],
 "notes": "Entreguei 21 artigos, não os 25 pedidos. Não completei a lista com artigos que não atendem a todos os critérios.\n\nComo conferi: abri os metadados no Crossref e li os resumos pelo Semantic Scholar. No caso de Jung, usei o Europe PMC. Os trechos são cópias literais de partes contíguas dos resumos, e todos têm menos de 125 caracteres, exceto quando o resumo exigiu trecho mais longo. Duas ressalvas: o ferramental de leitura fragmentou as frases, e eu as juntei sem alterar palavras. Em Mohammada et al., mantive os erros de grafia do original. O ano informado é o da edição oficial. Onde ele diverge do online-first, está anotado (Khawar, Molyneux, Scacco, Li e Vultee).\n\nExcluídos ou não confirmados:\n- Kaushal & Vemuri 2021 (IEEE Trans. Technol. Soc., 10.1109/tts.2021.3073464) é um bom candidato: experimento com 200 participantes e credibilidade reduzida. Não consegui abrir o resumo no IEEE, no ADS nem no Crossref, e só vi o conteúdo em resumos de busca. Para não inventar trecho literal, deixei de fora. Convém conferir manualmente.\n- Wang et al. 2025 (Cyberpsychology, Behavior, and Social Networking, 10.1089/cyber.2024.0295) é um estudo de EEG com 32 participantes sobre clickbait. O resumo fala em 'online interactions', 'content creators' e 'marketers', sem citar notícias. Ficou fora por não atender ao contexto de notícias.\n- Munger et al. 2020 (Public Opinion Quarterly, 10.1093/poq/nfaa008) foi excluído porque o desfecho central é a polarização política.\n- Xu et al. 2022 (10.1080/1369118x.2022.2050416) trata de emoções em manchetes sobre clima, em análise computacional. O foco não é clickbait nem seus efeitos sobre leitores.\n- 10.1038/s41598-024-81575-9 (Sci. Rep. 2025) se descreve como meta-análise de 8.977 experimentos de manchetes, com dados secundários. Foi excluído por isso.\n- Zelianskaia 2023 (10.21638/spbu22.2023.104) é uma análise semântico-linguística de manchetes com CTR. Ficou em dúvida e foi excluído.\n- Diversita 2022 (10.31289/diversita.v8i1.5536) estuda 'misleading headline' sem usar o termo clickbait. Foi excluído.\n- Não consegui abrir os resumos de Lee 2020 (10.46407/kjci.2020.08.102.160), Zhang 2024 (Current Psychology, 10.1007/s12144-024-06646-6), Jiang et al. 2025 (Univ. Access Inf. Soc., 10.1007/s10209-025-01198-3) e Deng et al. 2025 (Information & Management, 10.1016/j.im.2025.104231). Ficaram de fora por falta de verificação.\n- Outros itens eliminados:\n  - detecção ou classificação computacional;\n  - análises apenas linguísticas ou de conteúdo;\n  - entrevistas só com jornalistas (Malaysia SEARCH 2024);\n  - revisões (Bagosy 2018, Jácobo-Morales 2024);\n  - anais de congresso (CAIS 2018, CogSci 2022, CHI 2021);\n  - teses;\n  - estudos de segurança ou compras, sem contexto de notícias (IJHCI 2024 e 2025; APJML 2021).\n\nLimitações: os critérios que mais eliminaram candidatos foram 'dados de leitores' e 'contexto de notícias'. A busca dependeu do Crossref, porque o OpenAlex devolveu 429. Os seis últimos itens da lista, em indonésio ou de periódicos regionais, são de menor impacto, e os de Mohammada, Elsalsa e Rahmatika têm resumos pouco precisos. Os artigos de Mukherjee (marketing) e Béna (estímulos em formato clickbait) têm observações sobre o contexto, para o pesquisador decidir. O artigo de Zhang et al. (Internet Research) tem uma observação sobre o resumo recuperado por DOI. Para chegar a 25, seria preciso uma busca manual no Scopus ou na Web of Science, ou mais acesso a bases com resumos completos.\""
}