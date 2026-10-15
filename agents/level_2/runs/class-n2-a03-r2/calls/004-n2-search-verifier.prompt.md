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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre desinformação e educação midiática (ou competência em informação) em escolas e universidades brasileiras. Restrições: estudos empíricos feitos no Brasil com estudantes, professores, aulas, currículos ou livros didáticos (questionários, grupos focais, intervenções, relatos de experiência com coleta de dados ou análise documental); estudos comparativos internacionais valem se incluírem amostra brasileira; exclua estudos centrados em COVID-19, vacinas, eleições ou política partidária e estudos com públicos fora do ensino formal. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CANDIDATOS A VERIFICAR:
{
 "candidates": [
  {
   "doi": "10.22409/rmc.v19i2.66810",
   "title": "Educação midiática: o comportamento de estudantes nas redes sociais e a propagação de informações falsas",
   "authors": [
    "Paulo Henrique Soares Almeida",
    "Ana Carolina Kalume Maranhão"
   ],
   "year": 2025,
   "venue": "Revista Mídia e Cotidiano, v. 19, n. 2",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.22409/rmc.v19i2.66810,doi:10.12957/redoc.2023.68237,doi:10.59666/arete.1984-7505.v24.n38.5277,doi:10.35168/1980-5276.utp.interin.2025.vol30.n2.pp76-91&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: estudo empírico quantitativo, questionários estruturados (nov/2023–mar/2024)",
    "Amostra: 'questionnaires administered to 180 students from public and private schools'",
    "Achado: 'The results reveal a significant deficiency in media education among these young people'",
    "Contexto: estudantes do ensino médio do Distrito Federal (Brasil)",
    "Tema: educação midiática + propagação de informações falsas; sem foco em COVID/eleições",
    "Ano 2025 (Crossref); journal-article. Resumo disponível em inglês"
   ]
  },
  {
   "doi": "10.35168/1980-5276.utp.interin.2025.vol30.n2.pp76-91",
   "title": "Literacia midiática, cidadania e enfrentamento da desinformação entre os jovens paulistanos",
   "authors": [
    "Isabela Afonso Portas",
    "Egle Müller Spinelli"
   ],
   "year": 2025,
   "venue": "INTERIN, v. 30, n. 2",
   "checked_url": "https://seer.utp.br/index.php/i/article/view/3552",
   "criteria_met": [
    "Tipo: estudo qualitativo, entrevistas em profundidade",
    "Amostra: 'trinta e seis alunos de escolas públicas e privadas' em São Paulo",
    "Achado: 'Como resultados, revela-se a necessidade de aprofundar o uso de mídia na escola;'",
    "Contexto: alunos do ensino médio, Brasil",
    "Tema: literacia midiática + desinformação ('desordem informacional')",
    "Ano 2025 (publicado 27/06/2025)"
   ]
  },
  {
   "doi": "10.55738/alaic.v23i46.1118",
   "title": "Literacias e educação midiática (título na página do periódico: A identificação de desinformação por alunos e professores no Brasil)",
   "authors": [
    "Diego de Deus",
    "Adinan Nogueira",
    "Ariely Masetti"
   ],
   "year": 2024,
   "venue": "Revista Latinoamericana de Ciencias de la Comunicación, v. 23, n. 46",
   "checked_url": "https://revista.pubalaic.org/index.php/alaic/article/view/1118",
   "criteria_met": [
    "Tipo: estudo empírico com professores e alunos; teste de efeito de conteúdo educativo sobre desinformação (método detalhado não verificado no resumo)",
    "Amostra: não informado no resumo (apenas 'professores e alunos do Ensino Médio, de escolas públicas e privadas no Brasil')",
    "Achado: 'Os resultados apontam a insuficiência de apenas explicar o que é informação falsa e como verificar'",
    "Contexto: ensino médio, Brasil",
    "Tema: desinformação + educação midiática",
    "Ano 2024 (publicado 11/12/2024)"
   ]
  },
  {
   "doi": "10.22478/ufpb.1809-4775.2025v21n3.75047",
   "title": "A competência crítica em informação na web para o combate à fake news: uma perspectiva didático-pedagógica",
   "authors": [
    "Josef de Aquino Peruk",
    "Vanessa Levati Biff"
   ],
   "year": 2025,
   "venue": "Biblionline, v. 21, n. 3",
   "checked_url": "https://periodicos.ufpb.br/index.php/biblio/article/view/75047",
   "criteria_met": [
    "Tipo: relato de experiência / projeto de ação com coleta (questionários, atividades gamificadas, observações), abordagem construtivista",
    "Amostra: 'A atividade foi realizada com 20 estudantes do ensino médio'",
    "Achado: 'com 80% dos participantes declarando ter desenvolvido sua competência crítica em informação.' (autoavaliação)",
    "Contexto: biblioteca de escola pública no interior do RS",
    "Tema: competência crítica em informação + fake news",
    "Ano 2025"
   ]
  },
  {
   "doi": "10.17058/signo.v50i98.20198",
   "title": "A literacia como ferramenta no combate a fake news: promovendo o pensamento crítico em estudantes do Ensino Médio",
   "authors": [
    "Pâmela Roman",
    "Kári Lúcia Forneck"
   ],
   "year": 2025,
   "venue": "Signo, v. 50, n. 98",
   "checked_url": "https://seer.unisc.br/index.php/signo/article/view/20198",
   "criteria_met": [
    "Tipo: intervenção quase-experimental (5 oficinas; grupo experimental 1º ano e grupo controle 2º ano; avaliação antes/depois)",
    "Amostra: 'Participaram dois grupos, sendo um experimental (1º ano) e outro o controle (2º ano).' (total não informado)",
    "Achado: 'as oficinas não geraram o impacto esperado no reconhecimento de fake news.'",
    "Contexto: ensino médio; o resumo não nomeia estado/escola (periódico e autoras brasileiros, UNIVATES) — localização Brasil inferida, não lida no resumo",
    "Tema: literacia/pensamento crítico + fake news",
    "Ano 2025"
   ]
  },
  {
   "doi": "10.15847/obsOBS18520242446",
   "title": "Perceptions of University Students in Communication about Disinformation: (título completo no registro)",
   "authors": [
    "Juliana Colussi",
    "Paula de Souza Paes",
    "Rainer Rubira-García",
    "Thays Assunção Reis"
   ],
   "year": 2024,
   "venue": "Observatorio (OBS*), v. 18, n. 5",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.15847/obsOBS18520242446,doi:10.18616/rsp.v9i2.10154,doi:10.51891/rease.v10i11.16410,doi:10.22169/revint.v20.e25tl4004,doi:10.1590/1516-731320250028&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: survey online exploratório (mai–jul/2023)",
    "Amostra: 'answered by 231 students' (23 centros de ensino superior em Brasil, Colômbia e Espanha)",
    "Achado: 'university students are aware of what fake news are and most of them know how to identify disinformative content'",
    "Comparativo internacional com Brasil explícito na amostra (subamostra brasileira não separada no resumo)",
    "Contexto: graduação em Comunicação; tema desinformação + media literacy no currículo",
    "Ano 2024 (online 13/02/2024)"
   ]
  },
  {
   "doi": "10.23860/JMLE-2025-17-2-5",
   "title": "Media and information literacy strategies: A joint reflection with teenagers in Brazilian public school",
   "authors": [
    "Fábio Henrique Pereira",
    "Cristine Marquetto",
    "Liliane Maria Macedo Machado",
    "Nathália Coelho da Silva",
    "Rafiza Varão",
    "Mariana Fagundes Ausani"
   ],
   "year": 2025,
   "venue": "Journal of Media Literacy Education, v. 17, n. 2, pp. 66–79",
   "checked_url": "https://digitalcommons.uri.edu/jmle/vol17/iss2/5",
   "criteria_met": [
    "Tipo: survey + observação participante em oficina (out/2021)",
    "Amostra: não informado no resumo",
    "Achado: três estratégias, incluindo 'de-normalizing disinformation and the problems it causes by stressing the consequences they have on society'",
    "Contexto: estudantes de escola pública brasileira (o resumo diz 'elementary school students in Brazil'; o título diz teenagers)",
    "Tema: MIL + desinformação",
    "Ano 2025"
   ]
  },
  {
   "doi": "10.12957/teias.2025.83022",
   "title": "Educação midiática no combate à desinformação: percepções e proposições de ação dos professores",
   "authors": [
    "Késsia Mileny de Paulo Moura",
    "Luciana Silva Palmeira",
    "Samantha Morais de Oliveira Sousa"
   ],
   "year": 2025,
   "venue": "Revista Teias, v. 26, n. 81",
   "checked_url": "https://www.e-publicacoes.uerj.br/revistateias/article/view/83022",
   "criteria_met": [
    "Tipo: pesquisa qualitativa de campo, questionário online com professores",
    "Amostra: não informado no resumo",
    "Achado: 'os professores percebem as implicações pessoais, sociais e pedagógicas da chegada da fake news na escola'",
    "Contexto: professores da rede básica; autoras da UFMA (local não nomeado no resumo)",
    "Tema: educação midiática + desinformação/fake news",
    "Ano 2025 (publicado 09/07/2025)"
   ]
  },
  {
   "doi": "10.12957/redoc.2023.68237",
   "title": "Letramento informacional no combate às fake news na educação",
   "authors": [
    "Iracema Cristina Fernandes",
    "Terezinha Fernandes"
   ],
   "year": 2023,
   "venue": "Revista Docência e Cibercultura, v. 7, n. 2",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.22409/rmc.v19i2.66810,doi:10.12957/redoc.2023.68237,doi:10.59666/arete.1984-7505.v24.n38.5277,doi:10.35168/1980-5276.utp.interin.2025.vol30.n2.pp76-91&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: pesquisa-formação na cibercultura com estudantes de Pedagogia EaD",
    "Amostra: não informado no resumo (estudantes de Licenciatura em Pedagogia EaD da Universidade Federal de Mato Grosso)",
    "Achado: 'Os resultados mostraram que o letramento informacional é uma prática importante no combate à desinformação'",
    "Contexto: graduação/formação docente, UFMT",
    "Tema: letramento informacional + fake news",
    "Ano 2023"
   ]
  },
  {
   "doi": "10.59666/arete.1984-7505.v24.n38.5277",
   "title": "Formação inicial de professores e a desinformação: o papel transformador da educação midiática",
   "authors": [
    "Igor Pereira dos Santos",
    "José Ricardo e Souza Mafra"
   ],
   "year": 2025,
   "venue": "Revista Areté | Revista Amazônica de Ensino de Ciências, v. 24, n. 38",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.22409/rmc.v19i2.66810,doi:10.12957/redoc.2023.68237,doi:10.59666/arete.1984-7505.v24.n38.5277,doi:10.35168/1980-5276.utp.interin.2025.vol30.n2.pp76-91&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: pesquisa qualitativa com estudantes de Licenciatura em Informática Educacional (instrumento não detalhado no resumo)",
    "Amostra: não informado no resumo",
    "Achado: 'Conclui-se que a educação, embora não resolva sozinha o problema, é pilar fundamental na construção de uma sociedade crítica e informada.'",
    "Contexto: formação inicial de professores; o resumo não nomeia a instituição (Brasil inferido)",
    "Tema: desinformação + educação midiática",
    "Ano 2025 (online 31/12/2025, dentro do limite)"
   ]
  },
  {
   "doi": "10.22169/revint.v20.e25tl4004",
   "title": "Educação midiática na educação matemática na formação inicial de professores",
   "authors": [
    "Juliana Campos Sabino de Souza",
    "Achilles Alves de Oliveira",
    "Braian Veloso"
   ],
   "year": 2025,
   "venue": "Revista Intersaberes, v. 20",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.15847/obsOBS18520242446,doi:10.18616/rsp.v9i2.10154,doi:10.51891/rease.v10i11.16410,doi:10.22169/revint.v20.e25tl4004,doi:10.1590/1516-731320250028&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: experiência de ensino (oficina) com análise qualitativa de dados",
    "Amostra: 'uma experiência de ensino a nível de graduação com 46 discentes de um Curso de Licenciatura em Matemática no XX.'",
    "Achado: 'Discutimos e analisamos qualitativamente dados de uma oficina que demonstram que a oficina apresentou resultados positivos e pôde contribuir com o desenvolvimento crítico-reflexivo na formação inicial docente.'",
    "Contexto: licenciatura em Matemática; instituição mascarada como 'XX' no resumo (Brasil inferido)",
    "Tema: educação midiática + desinformação/fake news",
    "Ano 2025"
   ]
  },
  {
   "doi": "10.51891/rease.v10i11.16410",
   "title": "Desinformação e literacia midiática",
   "authors": [
    "Orlando Lyra de Carvalho Júnior",
    "Stela Silva Carvalho",
    "Bárbara Andrade de Sousa"
   ],
   "year": 2024,
   "venue": "Revista Ibero-Americana de Humanidades, Ciências e Educação, v. 10, n. 11",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.15847/obsOBS18520242446,doi:10.18616/rsp.v9i2.10154,doi:10.51891/rease.v10i11.16410,doi:10.22169/revint.v20.e25tl4004,doi:10.1590/1516-731320250028&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: survey, questionário online de múltipla escolha",
    "Amostra: 'um grupo de alunos e professores de Minas Gerais (MG)' — número não informado no resumo",
    "Achado: 'Correlações significativas foram encontradas entre literacia midiática e Fake News, “fonte confiável” e “informação confiável”.'",
    "Contexto: alunos e professores, Minas Gerais",
    "Tema: literacia midiática + fake news (vacinação aparece só como exemplo de tema)",
    "Ano 2024. Observação: qualidade da revisão por pares do periódico não verificada"
   ]
  },
  {
   "doi": "10.18616/rsp.v9i2.10154",
   "title": "O perigo das fake news em saúde e as ações básicas de mitigação na escola",
   "authors": [
    "Monica Erika Pardin Steinert"
   ],
   "year": 2025,
   "venue": "Revista Saberes Pedagógicos, v. 9, n. 2",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.15847/obsOBS18520242446,doi:10.18616/rsp.v9i2.10154,doi:10.51891/rease.v10i11.16410,doi:10.22169/revint.v20.e25tl4004,doi:10.1590/1516-731320250028&select=DOI,title,abstract,issued,container-title,volume,issue,author,type",
   "criteria_met": [
    "Tipo: prática pedagógica com instrumentos qualiquantitativos e estratégia interventiva (aulas de Biologia, 2023)",
    "Amostra: não informado no resumo ('estudantes do ensino médio')",
    "Achado: 'a ação sinaliza um limiar de construção de competências em educação midiática.'",
    "Contexto: ensino médio; local não nomeado no resumo",
    "Tema: fake news + Alfabetização Midiática Informacional (AMI). ATENÇÃO: o resumo abre com doenças evitáveis por vacina como contexto; o foco declarado é a checagem de falsidades nas redes — conferir se o pesquisador aceita",
    "Ano 2025"
   ]
  },
  {
   "doi": "10.15847/obsOBS18520242435",
   "title": "The perception of misinformation by young students from a Brazilian sociocultural context: reflections and clues for media education",
   "authors": [
    "Viviane Ongaro",
    "Monica Fantin",
    "José Douglas Alves dos Santos"
   ],
   "year": 2024,
   "venue": "Observatorio (OBS*), v. 18, n. 5",
   "checked_url": "https://obs.obercom.pt/index.php/obs/article/view/2435",
   "criteria_met": [
    "Tipo: pesquisa qualitativa exploratória com oficinas de educação midiática",
    "Amostra: 'young students from 14 to 21 years old in Curitiba and Colombo in Paraná, Brazil' — número não informado no resumo",
    "Achado: 'The workshop analyses suggested clues to build media competencies in the youth culture contexts and how schools can/should develop a work in the perspective of media education'",
    "Contexto: estudantes de escolas públicas e privadas, Paraná",
    "Tema: desinformação + media education",
    "Ano 2024 (online 13/02/2024)"
   ]
  },
  {
   "doi": "10.28998/cirev.2021v8n2e",
   "title": "As Fake News sob a perspectiva dos estudantes dos cursos de graduação e técnico em Biblioteconomia de Porto Alegre (RS): um estudo de caso",
   "authors": [
    "Bruno Fortes Luce",
    "Laura Valladares Soares",
    "Filipe Xerxeneski da Silveira",
    "Lizandra Brasil Estabel"
   ],
   "year": 2021,
   "venue": "Ciência da Informação em Revista, v. 8, n. 2, pp. 72–86",
   "checked_url": "https://periodicos.ufal.br/cir/article/view/11579",
   "criteria_met": [
    "Tipo: estudo de caso exploratório com questionário (o resumo diz 'entrevistados')",
    "Amostra: 'Foram entrevistados 44 sujeitos, oriundos dos cursos técnico e graduação em Biblioteconomia.'",
    "Achado: 'a importância de abordar a temática fake news e enfocar a alfabetização midiática e informacional (AMI)'",
    "Contexto: IFRS e UFRGS, Porto Alegre",
    "Tema: fake news + AMI",
    "Ano 2021 (publicado 12/11/2021). ATENÇÃO: o DOI vem do Crossref; a página do periódico mostra um DOI malformado, e a resolução do DOI não foi testada"
   ]
  },
  {
   "doi": "10.22478/ufpb.1809-4775.2019v15n1.43786",
   "title": "Bibliotecário escolar e fake news: evidências da contribuição da biblioteca escolar",
   "authors": [
    "Janaína Fialho",
    "Martha Suzana Cabral Nunes",
    "Paulo Roberto Fernandes Júnior",
    "Giovana Gabrielli Rocha Gois",
    "Maria Mirella Borges Santana",
    "Raphaela Mota Pereira Veloso",
    "Wictor Alexandre da Silva Santos"
   ],
   "year": 2019,
   "venue": "Biblionline, v. 15, n. 1, pp. 122–135",
   "checked_url": "https://periodicos.ufpb.br/index.php/biblio/article/view/43786",
   "criteria_met": [
    "Tipo: palestra/intervenção com abordagem quanti-qualitativa; questionário com perguntas fechadas e uma aberta",
    "Amostra: 'A palestra para 45 alunos do ensino médio'",
    "Achado: 'a palestra foi bastante esclarecedora para a turma'",
    "Contexto: colégio particular; parceria com a UFS (Sergipe inferido, não nomeado no resumo)",
    "Tema: fake news + letramento informacional",
    "Ano 2019"
   ]
  },
  {
   "doi": "10.22456/1679-1916.99532",
   "title": "O desenvolvimento de um e-book para identificar fake news: o bibliotecário como mediador na criação de critérios de avaliação da informação",
   "authors": [
    "Bruna Heller",
    "Joice Rejane Pardo Maurell"
   ],
   "year": 2019,
   "venue": "RENOTE – Revista Novas Tecnologias na Educação, v. 17, n. 3, pp. 488–497",
   "checked_url": "https://seer.ufrgs.br/index.php/renote/article/view/99532",
   "criteria_met": [
    "Tipo: projeto de ação qualitativo e descritivo com questionários (Ensino por Projetos)",
    "Amostra: não informado no resumo (alunos do 1º ano do ensino médio)",
    "Achado: 'observou-se apropriação em relação à tecnologia digital, à ferramenta e à importância de checar a informação'",
    "Contexto: escola particular em Estância Velha (RS)",
    "Tema: fake news + critérios de avaliação da informação (competência informacional implícita). ATENÇÃO: o termo competência/letramento informacional não aparece nos trechos lidos; o tema é aceito por inferência",
    "Ano 2019"
   ]
  },
  {
   "doi": "10.5007/2175-795X.2023.e95903",
   "title": "Mídias digitais e acesso a conteúdo acadêmico-científico: usos por licenciandos e indícios para (re)pensar a formação docente",
   "authors": [
    "Alessandra Rodrigues",
    "Mariona Grané"
   ],
   "year": 2023,
   "venue": "Perspectiva, v. 41, n. 3",
   "checked_url": "https://periodicos.ufsc.br/index.php/perspectiva/article/view/95903",
   "criteria_met": [
    "Tipo: estudo exploratório qualitativo, método survey",
    "Amostra: 'do qual participaram 108 estudantes de universidades públicas e privadas brasileiras.'",
    "Achado: 'Apesar disso, se consideram capazes de detectar Fake News nas redes e reconhecem que a desinformação pode interferir na relação da sociedade com a ciência.'",
    "Contexto: licenciandos, universidades brasileiras",
    "Tema: desinformação/Fake News + alfabetização midiática e informacional. ATENÇÃO: o foco principal é o uso de mídias para conteúdo científico; a desinformação é eixo parcial",
    "Ano 2023 (publicado 31/10/2023)"
   ]
  },
  {
   "doi": "10.22409/rmc.v13i3.38091",
   "title": "Educação midiática para notícias: histórico e mapeamento de iniciativas para combater a desinformação por meio da educação",
   "authors": [
    "Mônica Chaves",
    "Luísa Melo"
   ],
   "year": 2019,
   "venue": "Revista Mídia e Cotidiano, v. 13, n. 3, pp. 62–82",
   "checked_url": "https://periodicos.uff.br/midiaecotidiano/article/view/38091",
   "criteria_met": [
    "Tipo: artigo misto (conceito, histórico, mapeamento de iniciativas no Brasil e pesquisa com professores)",
    "Amostra: não informado no resumo ('pesquisa realizada com professores/as de educação básica')",
    "Achado: 'Conclui-se que a preocupação em relação à educação midiática para notícias precisa ser apoiada pela comunidade escolar'",
    "Contexto: professores da educação básica brasileira",
    "Tema: educação midiática + conteúdos falsos. ATENÇÃO: só parte do artigo é empírica, e o resumo não detalha instrumento nem amostra",
    "Ano 2019 (publicado 05/12/2019)"
   ]
  },
  {
   "doi": "10.58876/rbbd.2023.1911791",
   "title": "Desenvolvimento da competência em informação e combate à desinformação nos currículos de Biblioteconomia das universidades federais do Brasil",
   "authors": [
    "Flávio Silva Teixeira",
    "Júlia Schettino Jacob dos Santos",
    "Marta Leandro da Mata"
   ],
   "year": 2023,
   "venue": "Revista Brasileira de Biblioteconomia e Documentação, v. 19, n. 1",
   "checked_url": "https://api.crossref.org/works?filter=doi:10.58876/rbbd.2023.1911791,doi:10.5216/revufg.v20.65943,doi:10.34019/2237-9444.2024.v14.41039&select=DOI,title,abstract,issued,container-title,volume,issue,author,type,subject",
   "criteria_met": [
    "Tipo: pesquisa documental e descritiva (ementas, PPPs e planos de ensino), análise de conteúdo de Bardin",
    "Amostra: não informado no resumo (número de cursos/documentos não declarado; o resumo cita '82 disciplinas' como resultado)",
    "Achado: 'Contudo, apenas oito tratam especificamente da competência em informação e nenhuma das disciplinas trabalham diretamente a questão da desinformação.'",
    "Contexto: currículos de Biblioteconomia de IES federais brasileiras",
    "Tema: competência em informação + desinformação",
    "Ano 2023"
   ]
  }
 ],
 "notes": "RESULTADO: entreguei 20 candidatos, não os 25 pedidos. Faltam 5. Preferi não completar com artigos duvidosos.\n\nCOMO CONFERI: fiz buscas no Crossref (API), em páginas de periódicos e na web. A API do OpenAlex devolveu HTTP 429 e não pôde ser usada. O resumo e os metadados foram lidos em páginas de periódicos (Signo, ALAIC, Biblionline, Interin, OBS, JMLE, Teias, Biblionline 2019, RENOTE, Perspectiva, Mídia e Cotidiano, CIR/UFAL) ou no registro do Crossref (os demais). Em checked_url, as URLs longas do Crossref são as consultas que abri de fato. Não abri o DOI no resolvedor (doi.org) para todos. Só os DOIs que aparecem em registro do Crossref ou na página do periódico foram escritos. O DOI de Luce et al. (2021) vem do Crossref e não foi testado; a página do periódico mostra um DOI malformado.\n\nLIMITAÇÃO DOS TRECHOS: a ferramenta de leitura devolveu os resumos fragmentados em citações curtas. Os trechos entre aspas foram copiados dessas citações, mas não os comparei caractere a caractere com o PDF ou a página. Confira antes de citar. A revisão por pares não foi checada na política de cada periódico; só confirmei type=journal-article.\n\nITENS MAIS FRÁGEIS (decisão sua):\n- Steinert (2025): o resumo abre com doenças evitáveis por vacina como contexto. O foco declarado é checagem de falsidades e AMI.\n- Rodrigues & Grané (2023): a desinformação é eixo parcial; o foco é o uso de mídias para conteúdo científico.\n- Heller & Maurell (2019): o tema informacional é inferido (critérios de avaliação da informação).\n- Chaves & Melo (2019): artigo misto; só parte é empírica.\n- Signo (Roman), Areté (Santos), Intersaberes (Souza), Teias (Moura): o Brasil é inferido (periódico, autores ou termo 'Licenciatura'), não nomeado no resumo.\n- Carvalho Júnior (REASE): qualidade da revisão por pares do periódico não verificada.\n- Fialho et al. (2019): o estado (SE) não consta no resumo.\n- Ano: o Crossref indica 2025 para Areté (online 31/12/2025). O ano da edição foi usado nos demais.\n\nEXCLUÍDOS APÓS LEITURA (motivo):\n- Revisões, ensaios ou propostas: BiblioCanto 10.21680/2447-7842.2024v10n1id36807 (revisão sistemática); Cerigatto 10.20873/uft.2447-4266.2020v6n6a4pt (proposta); Gomes 10.18264/repdcec.v3i3.248 (argumentativo); Angelo 10.12957/redoc.2023.65040 (ensaio); Nagumo 10.20396/etd.v24i1.8665292 (ensaio); Araújo 10.5007/2175-7941.2025.e103084 (teórico).\n- Foco em COVID: AtoZ 10.5380/atoz.v13i0.89709 (quiz com conteúdo de COVID-19); Acosta 10.21527/2179-1309.2023.120.12927; Martins & Venturi 10.4025/rvc.v3i2.64494; Dias 10.54033/cadpedv21n12-212 (título).\n- Público fora do ensino formal: Gomes et al. 10.1590/1516-731320200018 (questionário online com 232 pessoas, público geral); Scarcella 10.69620/mlscj.v2i1.3300 (grupos focais em centro municipal de capacitação, Itaim Paulista; provável educação não formal); Pieranti 10.22409/rmc.v17i3.58703 (alunos e profissionais de oficina da BBC).\n- Fora do período: Interin 2026 ('Todos contra a desinformação'); Em Teia 2026 (10.51359/2177-9309.2026.264619); Góndola (jan/2026).\n- Anais ou congresso: Identidade! v.29 especial (10.. anais, PNLD Linguagens); trabalhos de Intercom, SIIEPE e FEBAB.\n- Desinformação não central ou educação midiática ausente no resumo: Liinc 10.18617/liinc.v17i1.5537 (fake news só de passagem); Sales 10.34019/2237-9444.2024.v14.41039; Nunes & Rocha 10.26843/rencima.v14n3a11 (alfabetização científica); Britto 10.4025/rvc.v3i2.64493 (pandemia, sem educação midiática); Nascimento 10.33237/2236-255x.2024.5986 (professores de geografia, sem educação midiática); Signo 10.17058/signo.v49i94.18842 (BNCC e LMI; desinformação só como motivação).\n- Sem como confirmar o método ou o abstract: Kneipp (Revista Mediação 2025, sem DOI nem método no resumo); Martins et al. (RIS 10.36661/2595-4520.2025v8n1.15332, método ausente do resumo); Revista ACB v.28 n.1 (alfabetização informacional, sem DOI e com conflito de autoria na página); Barros & Silva (Fake news no Facebook, FURG; sem termo de educação midiática e com duas versões da mesma página); Cisne (Biblos 2023, 10.14295/biblos.v37i2.16212; sem coleta de dados descrita).\n\nBORDERLINE PARA DECISÃO DO PESQUISADOR (textos sobre fake news em livros didáticos, sem 'educação midiática' no resumo): Oliveira, Bodart & Cigales (2024), Sociedade e Estado, DOI 10.1590/s0102-6992-20243901e51808 (2 coleções PNLD 2021 CHSA, Voyant Tools); Rocha & Biondo (2020), Revista UFG, DOI 10.5216/revufg.v20.65943 (coleção de Língua Portuguesa, Campo Grande/MS; letramentos críticos); Simioni & Pinton (2024), EccoS, DOI 10.5585/eccos.n70.25011 (turma de escola pública em Santa Maria/RS, questionário; letramento crítico). Se aceitar letramento crítico e análise de livro didático como eixo equivalente, esses três completam parte da lista.\n\nPara chegar a 25 seria preciso nova rodada em SciELO e Periódicos CAPES (a API do OpenAlex ficou indisponível), com foco em formação docente, ensino superior e livros didáticos."
}