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
    "Supavich Fone Pengnate"
   ],
   "year": 2019,
   "venue": "Online Information Review",
   "checked_url": "https://api.openalex.org/works/doi:10.1108/OIR-05-2018-0172",
   "criteria_met": [
    "Tema: efeito de manchetes clickbait sobre excitação emocional e intenção de ler notícias",
    "Tipo/método: experimento com rastreamento ocular (dilatação pupilar) e escala SAM",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: o clickbait gera mais excitação que manchetes neutras e menos que manchetes noticiosas, e a excitação prediz a intenção de ler",
    "Trecho literal: \"Emotional arousal appears to be a significant predictor of intention to read news.\"",
    "Período 2019; artigo de periódico (OpenAlex type=article); sem recorte político"
   ]
  },
  {
   "doi": "10.58729/1941-6679.1440",
   "title": "Effects of Clickbait Headlines on User Responses: An Empirical Investigation",
   "authors": [
    "Supavich Fone Pengnate",
    "Jeffrey W. Chen",
    "Alex Young"
   ],
   "year": 2021,
   "venue": "Journal of International Technology and Information Management",
   "checked_url": "https://api.openalex.org/works/doi:10.58729/1941-6679.1440",
   "criteria_met": [
    "Tema: clickbait e respostas de usuários (excitação, curiosidade, intenção de ler e compartilhar)",
    "Tipo/método: experimento (manchetes tradicionais vs. clickbait) com modelagem de equações estruturais",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: o clickbait evoca excitação e curiosidade; a curiosidade determina a intenção de ler e a qualidade percebida do conhecimento determina a de compartilhar",
    "Trecho literal: \"The findings suggest that clickbait headlines can evoke users' arousal and curiosity.\"",
    "Período 2021; artigo de periódico; sem recorte político"
   ]
  },
  {
   "doi": "10.1371/journal.pone.0266743",
   "title": "Click me…! The influence of clickbait on user engagement in social media and the role of digital nudging",
   "authors": [
    "Anna-Katharina Jung",
    "Stefan Stieglitz",
    "Tobias Kißmer",
    "Milad Mirbabaie",
    "Tobias Kroll"
   ],
   "year": 2022,
   "venue": "PLOS ONE",
   "checked_url": "https://api.openalex.org/works/doi:10.1371/journal.pone.0266743",
   "criteria_met": [
    "Tema: efeito do clickbait sobre curtir, compartilhar e comentar no Facebook",
    "Tipo/método: dados de engajamento de usuários reais (posts de páginas de notícias no Facebook)",
    "Tamanho da amostra: \"more than 4,400 Facebook posts from 10 different news sources\"",
    "Achado principal: alguns traços de clickbait aumentam a interação dos usuários e outros a diminuem",
    "Trecho literal: \"certain features (e.g., unusual punctuation and common clickbait phrases) increase user interaction, whereas others decrease engagement with Facebook posts\"",
    "Período 2022; artigo de periódico; sem recorte político"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1080/17512786.2019.1628658",
   "criteria_met": [
    "Tema: clickbait e percepção de credibilidade e qualidade jornalística",
    "Tipo/método: dois experimentos online",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: manchetes clickbait podem reduzir a credibilidade e a qualidade percebidas",
    "Trecho literal: \"Results also suggest clickbait headlines may lower perceptions of credibility and quality.\"",
    "Período: online-first em 2019 (OpenAlex/Crossref), edição final vol. 14(4) em 2020; ambos dentro de 2018–2025",
    "Artigo de periódico; sem recorte político"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1027/1864-1105/a000298",
   "criteria_met": [
    "Tema: efeito de manchetes clickbait sobre aprendizado, reconhecimento e compreensão",
    "Tipo/método: dois experimentos online fatoriais 3×2 (tipo de manchete × exposição)",
    "Tamanho da amostra: \"N = 629\" (Estudo 1); \"N = 1,674\" (Estudo 2)",
    "Achado principal: ler o artigo completo com manchete precisa dá o maior reconhecimento e compreensão, e a correção no texto não basta para anular o dano da manchete clickbait",
    "Trecho literal: \"reading the full article with an accurate headline resulted in the highest recognition and comprehension\"",
    "Período: online em 2021, vol. 34(1) em 2022; dentro do intervalo",
    "Artigo de periódico; sem recorte político"
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
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/s11747-021-00830-x&resultType=core&format=json",
   "criteria_met": [
    "Tema: clickbait, compartilhamento, manipulação percebida e derrogação da fonte",
    "Tipo/método: experimento controlado mais dados secundários de compartilhamento de artigos, com dados de Twitter",
    "Tamanho da amostra: \"19,386 articles from 27 leading online publishers\" (o resumo não informa o n do experimento)",
    "Achado principal: em média, artigos clickbait recebem muito menos compartilhamentos que artigos não clickbait",
    "Trecho literal: \"We confirm that, on average, clickbait articles elicit far fewer shares than non-clickbait articles.\" (resumo do Europe PMC; OpenAlex tem resumo nulo; DOI e metadados conferidos no OpenAlex)",
    "Período 2022; artigo de periódico; sem recorte político"
   ]
  },
  {
   "doi": "10.1109/tts.2021.3073464",
   "title": "Clickbait—Trust and Credibility of Digital News",
   "authors": [
    "Vivek Kaushal",
    "Kavita Vemuri"
   ],
   "year": 2021,
   "venue": "IEEE Transactions on Technology and Society",
   "checked_url": "https://api.openalex.org/works/doi:10.1109/tts.2021.3073464",
   "criteria_met": [
    "Tema: efeito do clickbait sobre a credibilidade de notícias, com idade e curiosidade epistêmica",
    "Tipo/método: experimento com questionário de credibilidade",
    "Tamanho da amostra: \"200 participants (100 each of English-speaking American and English-speaking Indian)\"",
    "Achado principal: manchetes clickbait reduziram significativamente a credibilidade das notícias",
    "Trecho literal: \"Clickbait headlines significantly reduced the credibility of news items.\"",
    "Período 2021; artigo de periódico; sem recorte político"
   ]
  },
  {
   "doi": "10.1108/AJIM-07-2020-0214",
   "title": "\"This Will Blow Your Mind\": examining the urge to click clickbaits",
   "authors": [
    "Alton Y.K. Chua",
    "Anjan Pal",
    "Snehasish Banerjee"
   ],
   "year": 2021,
   "venue": "Aslib Journal of Information Management",
   "checked_url": "https://eprints.whiterose.ac.uk/id/eprint/168209/",
   "criteria_met": [
    "Tema: determinantes do impulso de clicar em clickbait (curiosidade, prazer, vigilância)",
    "Tipo/método: experimento entre participantes que manipula a riqueza da informação (só texto vs. miniatura)",
    "Tamanho da amostra: \"N=204\"",
    "Achado principal: curiosidade, prazer percebido e vigilância predizem o impulso de clicar, que é maior com miniaturas",
    "Trecho literal: \"Curiosity, perceived enjoyment, and surveillance were significant predictors of the urge to click.\"",
    "Período 2021; artigo de periódico (ISSN 2050-3806); sem recorte político. DOI lido na página do repositório; não resolvi o DOI separadamente em doi.org nem no Crossref"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1108/INTR-09-2019-0373",
   "criteria_met": [
    "Tema: quais traços das manchetes clickbait atraem cliques e o que acontece com o tráfego dos publicadores",
    "Tipo/método: dados longitudinais de cliques e tráfego de contas do WeChat, com análise econométrica (inclui mineração de texto para medir os traços retóricos)",
    "Tamanho da amostra: \"more than 500 WeChat official accounts in China\"",
    "Achado principal: hipérbole, insinuação e retórica visual aumentam os cliques, e há relação em U invertido entre o volume de clickbait e o tráfego do publicador",
    "Trecho literal: \"hyperbole, insinuation, and visual rhetoric entice users to click the baited headlines\"",
    "Período 2020; artigo de periódico; sem recorte político. Observação: o estudo propõe também uma estrutura de mineração de texto, mas o foco é o efeito sobre cliques e tráfego"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1002/acp.4134",
   "criteria_met": [
    "Tema: efeito da exposição prévia a conteúdo em formato clickbait sobre o julgamento de veracidade",
    "Tipo/método: dois experimentos com participantes",
    "Tamanho da amostra: \"Experiment 1 (N = 241)\"; \"Experiment 2 (N = 291)\"",
    "Achado principal: a exposição prévia a clickbait aumenta os julgamentos de verdade, porém menos do que para enunciados comuns",
    "Trecho literal: \"exposure to clickbait headlines can increase their content's truth judgments despite their overall lack of credibility, although to a lesser extent than for more regular statements\"",
    "Período 2023; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: os estímulos são enunciados em formato clickbait, e o contexto é menos claramente jornalístico"
   ]
  },
  {
   "doi": "10.3390/info16020150",
   "title": "AI vs. Human-Authored Headlines: Evaluating the Effectiveness, Trust, and Linguistic Features of ChatGPT-Generated Clickbait and Informative Headlines in Digital News",
   "authors": [
    "Vasile Gherheș",
    "Marcela Alina Fărcașiu",
    "Mariana Cernicova-Bucă",
    "Claudiu Coman"
   ],
   "year": 2025,
   "venue": "Information",
   "checked_url": "https://api.openalex.org/works/doi:10.3390/info16020150",
   "criteria_met": [
    "Tema: reação de leitores a manchetes clickbait vs. informativas (confiança, manipulação percebida)",
    "Tipo/método: survey com avaliação de manchetes escritas por humanos e geradas por ChatGPT, mais análise linguística complementar",
    "Tamanho da amostra: \"624 students from Timisoara, Romania\"",
    "Achado principal: manchetes clickbait, qualquer que seja a fonte, foram vistas como enganosas e manipuladoras, e a confiança caiu em publicações que as usam com frequência",
    "Trecho literal: \"Clickbait headlines, regardless of their source, were considered misleading and rated as manipulative (44.7%).\"",
    "Período 2025; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: o foco principal é IA vs. humano"
   ]
  },
  {
   "doi": "10.3390/journalmedia5040110",
   "title": "Are ChatGPT-Generated Headlines Better Attention Grabbers than Human-Authored Ones? An Assessment of Salient Features Driving Engagement with Online Media",
   "authors": [
    "Vasile Gherheș",
    "Marcela Alina Fărcașiu",
    "Mariana Cernicova-Bucă"
   ],
   "year": 2024,
   "venue": "Journalism and Media",
   "checked_url": "https://api.openalex.org/works/doi:10.3390/journalmedia5040110",
   "criteria_met": [
    "Tema: reação de leitores online a manchetes clickbait ou informativas (curiosidade e engajamento)",
    "Tipo/método: survey online com 100 trios de manchetes, mais análise linguística das manchetes preferidas",
    "Tamanho da amostra: \"600 participants\" (survey) e \"100 headline triplets\"",
    "Achado principal: o público rejeita o clickbait no plano cognitivo, mas na prática poucos preferem manchetes neutras",
    "Trecho literal: \"the investigated audience rejected clickbait headlines as being deceitful and frustrating, in practice less than 34% favored neutral and objective headlines\"",
    "Período 2024; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: o foco principal é IA vs. humano"
   ]
  },
  {
   "doi": "10.5897/jmcs2020.0715",
   "title": "Clickbait-style headlines and journalism credibility in Sub-Saharan Africa: Exploring audience perceptions",
   "authors": [
    "Judith Wanda",
    "Samson Chipanjilo Baraka",
    "Gregory Gondwe",
    "Joseph Kerunga"
   ],
   "year": 2021,
   "venue": "Journal of Media and Communication Studies",
   "checked_url": "https://api.openalex.org/works/doi:10.5897/jmcs2020.0715",
   "criteria_met": [
    "Tema: clickbait e credibilidade jornalística percebida (Zâmbia e Tanzânia)",
    "Tipo/método: estudo experimental com consumidores de notícias online",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: manchetes clickbait têm efeito negativo sobre a credibilidade jornalística percebida",
    "Trecho literal: \"The findings suggest strong statistical evidence that clickbait headlines pose negatives effects on the perceptions of journalistic credibility in Zambia and Tanzania.\"",
    "Período 2021; artigo de periódico; sem recorte político"
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
   "checked_url": "https://api.openalex.org/works/doi:10.24815/jr.v8i3.47278",
   "criteria_met": [
    "Tema: efeito de manchetes clickbait sobre o interesse de leitura (curiosidade e tédio/decepção)",
    "Tipo/método: survey quantitativo por questionário",
    "Tamanho da amostra: \"113 respondents\"",
    "Achado principal: o clickbait influencia significativamente o interesse de leitura, aumentando a curiosidade e também a decepção quando o conteúdo não corresponde",
    "Trecho literal: \"the use of clickbait headlines has a significant influence on reading interest.\" (o resumo diz \"the use of clickbait\" e depois \"headlines has a significant influence on reading interest\")",
    "Período 2025; artigo de periódico; sem recorte político. Revisão por pares não confirmada no site do periódico"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1080/21670811.2025.2505566",
   "criteria_met": [
    "Tema: tipos de clickbait (rage bait vs. information bait) e engajamento do público em redes sociais",
    "Tipo/método: dados de engajamento de usuários em posts de organizações jornalísticas",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: manchetes rage bait associaram-se a mais engajamento e information bait a menos",
    "Trecho literal: \"rage bait headlines were linked to higher levels of audience engagement, while information bait was associated with lower engagement.\"",
    "Período 2025; artigo de periódico; o resumo cita mídia conservadora só como variável descritiva, e o foco central não é político"
   ]
  },
  {
   "doi": "10.1089/cyber.2024.0295",
   "title": "Decoding Clickbait: The Impact of Clickbait Types and Structures on Cognitive and Emotional Responses in Online Interactions",
   "authors": [
    "Yikai Wang",
    "Bin Hu",
    "Chaolan Tang",
    "Xian Yang"
   ],
   "year": 2025,
   "venue": "Cyberpsychology, Behavior, and Social Networking",
   "checked_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1089/cyber.2024.0295&resultType=core&format=json",
   "criteria_met": [
    "Tema: tipos e estruturas de clickbait e respostas cognitivas e emocionais dos usuários",
    "Tipo/método: experimento com eletroencefalografia (EEG)",
    "Tamanho da amostra: \"32 internet-experienced participants\"",
    "Achado principal: hipérbole e retórica visual capturam a atenção rapidamente, enquanto insinuação e quebra-cabeça exigem mais esforço cognitivo",
    "Trecho literal: \"clickbait types such as hyperbole and visual rhetoric swiftly capture attention and enhance emotional engagement, whereas insinuative and puzzling clickbait demand more cognitive effort and deeper processing\"",
    "Período: online em 2024, vol. 28(1) em 2025; dentro do intervalo; artigo de periódico; sem recorte político. Contexto de interações online em geral, com menor ênfase em notícias"
   ]
  },
  {
   "doi": "10.58984/smb2201145s",
   "title": "Photography and Clickbait Headlines: Online Media Tools in the Process of Readers Manipulation",
   "authors": [
    "Uroš Selenić"
   ],
   "year": 2022,
   "venue": "Sports, Media and Business",
   "checked_url": "https://api.openalex.org/works/doi:10.58984/smb2201145s",
   "criteria_met": [
    "Tema: manchetes clickbait e fotografia como ferramentas de manipulação de leitores em notícias esportivas",
    "Tipo/método: survey com escala Likert",
    "Tamanho da amostra: \"200 respondents\"",
    "Achado principal: os participantes se declararam manipulados por fotos e manchetes clickbait",
    "Trecho literal: \"They were also manipulated by the photos and clickbait headlines, according to the results.\"",
    "Período 2022; artigo de periódico; sem recorte político. Revisão por pares não confirmada no site do periódico"
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
   "checked_url": "https://api.openalex.org/works/doi:10.1177/1461444819863408",
   "criteria_met": [
    "Tema: manchetes tradicionais, de resumo e clickbait/de curiosidade e busca de informação em notícias",
    "Tipo/método: experimento de laboratório mais teste de campo (seleção em 9 sites de jornais locais)",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: manchetes de resumo aumentam a percepção de adequação da informação e a expectativa de engajamento em comparação com algumas manchetes de curiosidade, e a seleção real também favorece manchetes de resumo",
    "Trecho literal: \"summary headlines heighten perceptions of headline information adequacy, which increase expectations that an article will provide clear information\"",
    "Período: online em 2019, vol. 22(3) em 2020; dentro do intervalo; artigo de periódico; sem recorte político"
   ]
  },
  {
   "doi": "10.1002/acp.4195",
   "title": "Curiosity in news consumption",
   "authors": [
    "Jingyi Qiu",
    "Russell Golman"
   ],
   "year": 2024,
   "venue": "Applied Cognitive Psychology",
   "checked_url": "https://api.openalex.org/works/doi:10.1002/acp.4195",
   "criteria_met": [
    "Tema: lacuna de curiosidade em manchetes e consumo de notícias (cliques)",
    "Tipo/método: dados reais de cliques em artigos do WeChat, com PLN e validação experimental das medidas",
    "Tamanho da amostra: \"over 100,000 WeChat news articles\"",
    "Achado principal: manchetes que despertam uma pergunta saliente atraem cliques, mas induzir curiosidade não necessariamente aumenta o engajamento de longo prazo",
    "Trecho literal: \"inducing curiosity can drive short-term news consumption, it doesn't necessarily enhance long-term reader engagement\"",
    "Período 2024; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: o termo clickbait não aparece no resumo; o foco é a lacuna de curiosidade em manchetes. Há análise computacional de texto, mas o desfecho vem de dados de cliques"
   ]
  },
  {
   "doi": "10.1080/10447318.2022.2158262",
   "title": "Attention Grabbing through Forward Reference: An ERP Study on Clickbait and Top News Stories",
   "authors": [
    "Xin Yan Li",
    "Jia Zhou",
    "Honglian Xiang",
    "Jingjing Cao"
   ],
   "year": 2022,
   "venue": "International Journal of Human-Computer Interaction",
   "checked_url": "https://api.openalex.org/works/doi:10.1080/10447318.2022.2158262",
   "criteria_met": [
    "Tema: manchetes clickbait com referência antecipatória e alocação de atenção",
    "Tipo/método: experimento com EEG (componentes N2b e P3a)",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: manchetes clickbait com recurso de referência antecipatória atraem mais atenção e a alocação involuntária de atenção ocorre mais rápido",
    "Trecho literal: \"the clickbait headlines with a forward-reference device attracted more attention and resources and induced the involuntary attention allocation more quickly\"",
    "Período: online em 2022, vol. 40(11) em 2024; dentro do intervalo; artigo de periódico; sem recorte político"
   ]
  },
  {
   "doi": "10.1080/21670811.2024.2394764",
   "title": "Analyzing Sensationalism in News on Twitter (X): Clickbait Journalism by Legacy vs. Online-Native Outlets and the Consequences for User Engagement",
   "authors": [
    "Salman Khawar",
    "Mark Boukes"
   ],
   "year": 2024,
   "venue": "Digital Journalism",
   "checked_url": "https://api.openalex.org/works/doi:10.1080/21670811.2024.2394764",
   "criteria_met": [
    "Tema: sensacionalismo/clickbait em tweets de veículos de notícias e consequências para o engajamento dos usuários",
    "Tipo/método: análise de conteúdo manual e automatizada de tweets ligada a métricas reais de engajamento (favoritos e retweets)",
    "Tamanho da amostra: \"1,440 tweets\" (manual) e \"25,600 tweets\" (automatizada)",
    "Achado principal: mais traços sensacionalistas associam-se a mais favoritos, e a análise automatizada mostra também mais retweets",
    "Trecho literal: \"a positive relationship was found between the number of sensationalist features employed and the favorite count, confirming the effectiveness of clickbaits.\"",
    "Período 2024; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: parte do estudo é análise de conteúdo, mas o desfecho principal usa dados de engajamento de usuários"
   ]
  },
  {
   "doi": "10.1080/17512786.2020.1793379",
   "title": "Here's What to Know About Clickbait: Effects of Image, Headline and Editing on Audience Attitudes",
   "authors": [
    "Fred Vultee",
    "G. Scott Burgess",
    "Darryl Frazier",
    "Kelsey R. Mesmer"
   ],
   "year": 2020,
   "venue": "Journalism Practice",
   "checked_url": "https://api.openalex.org/works/doi:10.1080/17512786.2020.1793379",
   "criteria_met": [
    "Tema: efeitos do estilo da manchete (tradicional vs. clickbait), da imagem e da edição sobre percepção de qualidade, credibilidade e memória",
    "Tipo/método: estudo experimental",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: a edição é a maior influência sobre qualidade e credibilidade percebidas e condiciona se manchetes tradicionais ou clickbait se associam a melhor memória",
    "Trecho literal: \"the presence of editing also influences whether traditional or clickbait headlines are associated with better memory for story details.\"",
    "Período 2020; artigo de periódico; sem recorte político"
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
   "checked_url": "https://api.openalex.org/works/doi:10.47233/jkomdis.v4i2.1777",
   "criteria_met": [
    "Tema: efeito de manchetes clickbait sobre o interesse de leitura de estudantes",
    "Tipo/método: pesquisa quantitativa (survey) com amostragem proposital",
    "Tamanho da amostra: não informado no resumo",
    "Achado principal: o uso de manchetes clickbait tem efeito significativo sobre o interesse de leitura",
    "Trecho literal: \"a significant effect on students’ reading interest\" (o resumo tem erros de digitação, como \"newsdan\")",
    "Período 2024; artigo de periódico; sem recorte político. Revisão por pares não confirmada no site do periódico"
   ]
  },
  {
   "doi": "10.3126/njdrs.v22i1.99390",
   "title": "Sensational Headlines, Engagement, and Credibility in Nepal's Online News",
   "authors": [
    "Sudhamshu Dahal"
   ],
   "year": 2025,
   "venue": "Nepalese Journal of Development and Rural Studies",
   "checked_url": "https://api.openalex.org/works/doi:10.3126/njdrs.v22i1.99390",
   "criteria_met": [
    "Tema: manchetes sensacionalistas (incluindo construção de lacuna de curiosidade), engajamento e credibilidade percebida",
    "Tipo/método: método misto, com engajamento visível no Facebook e survey de consumidores de notícias",
    "Tamanho da amostra: \"300 Facebook-posted headlines\" (o resumo não informa o n do survey)",
    "Achado principal: manchetes sensacionalistas receberam mais engajamento, mas o survey indicou custos de credibilidade",
    "Trecho literal: \"Sensational headlines received higher mean engagement than non-sensational headlines, especially for comments; however, survey responses indicated credibility costs\"",
    "Período 2025; artigo de periódico; sem recorte político. CANDIDATO LIMÍTROFE: usa \"sensacionalista\" e não \"clickbait\" como termo central. Revisão por pares não confirmada no site do periódico"
   ]
  },
  {
   "doi": "10.14421/hum.v4i2.3524",
   "title": "Pengaruh Penggunaan Clickbait pada Judul Berita di Ayobandung.com Terhadap Minat Baca Mahasiswa Fakultas Ilmu Sosial dan Politik Universitas Bhayangkara Surabaya",
   "authors": [
    "Kautsar Senja",
    "Julyanto Ekantoro",
    "Ratna Setyarahajoe"
   ],
   "year": 2025,
   "venue": "Jurnal Humanitaria: Jurnal Ilmu Sosial dan Humaniora",
   "checked_url": "https://api.openalex.org/works/doi:10.14421/hum.v4i2.3524",
   "criteria_met": [
    "Tema: efeito de clickbait em títulos de notícias sobre o interesse de leitura de estudantes",
    "Tipo/método: survey com modelagem de equações estruturais (PLS)",
    "Tamanho da amostra: \"100 respondents\"",
    "Achado principal: quanto mais se usa clickbait nos títulos, maior o interesse de leitura dos estudantes",
    "Trecho literal: \"the better use of clickbait in the online media news titles ayobandung.com, the more it increases students' interest in reading.\"",
    "Período 2025; artigo de periódico; sem recorte político. ATENÇÃO: o Crossref lista um registro com o mesmo título e outro DOI (10.24815/jimps.v10i3.35161, JIM: Jurnal Ilmiah Mahasiswa Pendidikan Sejarah, 2025), possível publicação duplicada. Só este foi aberto. Revisão por pares não confirmada no site do periódico"
   ]
  }
 ],
 "notes": "RESULTADO: entreguei 25 candidatos (o pedido era 25; o teto era 37). Cada um foi aberto nesta tentativa. Para 23 deles o endereço é o registro do OpenAlex por DOI. Mukherjee et al. 2022 e Wang et al. 2025 foram conferidos no Europe PMC, e Chua et al. 2021 no repositório White Rose. Mukherjee et al. 2022 também foi aberto no OpenAlex, mas o resumo lá é nulo.\n\nLIMITAÇÕES DE VERIFICAÇÃO (leia antes de usar):\n1) As APIs de listagem do OpenAlex e do Crossref ficaram intermitentemente bloqueadas (HTTP 429). Parte da busca foi por buscas na web e por listas do Crossref que funcionaram depois. Não cobri sistematicamente o SciELO nem o Google Scholar.\n2) Os trechos literais foram copiados de resumos reconstruídos pelo índice invertido do OpenAlex. Só os de Mukherjee et al. 2022 e Wang et al. 2025 vieram de texto verbatim (Europe PMC). Recomendo comparar caractere a caractere com a página do periódico antes de citar. Dois trechos têm ressalvas. O de Putra et al. 2025 está dividido pelo índice, e o de Mohammada et al. 2024 vem de um resumo com erros de digitação na origem.\n3) A revisão por pares não foi confirmada no site de cada periódico. A condição foi: type = journal article no OpenAlex/Crossref mais ISSN/periódico identificável. Isso é mais frágil nos periódicos menores: Riwayat, Sports Media and Business, JKOMDIS, Humanitaria, Nepalese J. Dev. Rural Studies.\n4) Anos: Molyneux & Coddington (online 2019, edição 2020), Scacco & Muddiman (online 2019, edição 2020), Carcioppolo et al. (online 2021, edição 2022), Li et al. (online 2022, edição 2024) e Wang et al. (online 2024, edição 2025). Registrei o ano do volume/edição ou do registro, e todos ficam dentro de 2018–2025.\n\nCANDIDATOS LIMÍTROFES, para decisão do pesquisador (marcados em criteria_met): Béna et al. 2023 (estímulos são enunciados em formato clickbait, contexto menos jornalístico); Gherheș et al. 2025 e 2024 (foco em IA vs. humano, com reação a clickbait); Qiu & Golman 2024 (lacuna de curiosidade, sem o termo clickbait no resumo); Dahal 2025 (termo \"sensacionalista\"); Khawar & Boukes 2024 (análise de conteúdo ligada a métricas de engajamento); Wang et al. 2025 (contexto de interações online em geral); Selenić 2022 e Zhang et al. 2020 (ver criteria_met). Se quiser rigor máximo, remova estes e o total cai para cerca de 16.\n\nEXCLUÍDOS (e motivo):\n- Munger et al. 2020, POQ (10.1093/poq/nfaa008): polarização afetiva é desfecho central, então caiu na exclusão de recorte político. Não abri o resumo e decidi só pelo título e pelas fontes secundárias; reavalie se achar que o recorte não é político.\n- Liu, Xue & Liu 2021, APJML (10.1108/apjml-08-2020-0562): experimentos (729 respondentes) sobre intenção de compra em comércio social, fora do contexto de notícias.\n- Lee 2020, Korean J. Commun. & Inf. (10.46407/kjci.2020.08.102.160): experimento online com cerca de 500 usuários de notícias, mas o resumo recuperado não traz achados.\n- Deng et al. 2025, Information & Management (10.1016/j.im.2025.104231), e Jiang et al. 2025, Univ. Access Inf. Soc. (10.1007/s10209-025-01198-3): temas pertinentes (clickbait e engajamento em saúde; ERP e rótulos de aviso), mas não consegui recuperar o resumo, então não há trecho literal verificável. Valem uma checagem manual.\n- Entrevistas ou estudos qualitativos, fora dos métodos admitidos: Lechpammer et al. 2024 (jornalistas), Lim & Wilson 2024 (jornalistas), Elsalsa 2023, Mutharoh 2022, Muliawan 2025.\n- Shrestha et al. 2024 e 2025 (IJHCI): clickbait como ameaça de segurança em redes sociais, não notícias.\n- Xu et al. 2022 (clima: recorte temático polarizado, análise computacional de texto), Scott 2023 e Scott 2021 (pragmática teórica), Apresjan & Orlov 2022 (abstract indisponível; foco linguístico), Jiang et al. 2019 (cliques sem foco em clickbait), Ng & Zhao 2018/2020 (palavras de alarme, não clickbait), Lamot et al. 2022 (computacional), Zhang & Clough 2020 (sem resumo), Kanižaj et al. 2022 (survey croata, N=1.009, em Media Literacy and Academic Research: não encontrei DOI, então não pude conferir), Lestari 2022 (alfabetização crítica, sem efeito do clickbait).\n- Fora do tipo de publicação: Muddiman & Scacco 2019 (relatório), Engaging News Project 2016, Bhowmik et al. (preprint arXiv), CHI 2021 \"Does Clickbait Actually Attract More Clicks?\" (anais), teses do IIIT Hyderabad e Radboud, CogSci 2022 (anais), AMCIS (anais), Hagar & Diakopoulos 2019 (entrevistas sobre testes A/B, sem efeitos do clickbait).\n\nNão encontrei estudo com GSR/condutância da pele sobre clickbait em notícias. Na busca por EEG, só apareceram Wang et al. 2025 e Li et al. 2022."
}