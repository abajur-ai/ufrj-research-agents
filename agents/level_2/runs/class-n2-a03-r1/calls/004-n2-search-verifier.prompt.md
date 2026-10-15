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
   "doi": "10.12957/teias.2025.83022",
   "title": "Educação midiática no combate à desinformação: percepções e proposições de ação dos professores",
   "authors": [
    "Késsia Mileny de Paulo Moura",
    "Luciana Silva Palmeira",
    "Samantha Morais de Oliveira Sousa"
   ],
   "year": 2025,
   "venue": "Revista Teias (UERJ)",
   "checked_url": "https://www.e-publicacoes.uerj.br/revistateias/article/view/83022",
   "criteria_met": [
    "Tema: desinformação/fake news + educação midiática (palavras-chave: desinformação, educação midiática)",
    "Ensino formal e Brasil: professores da rede básica (UFMA); sem foco em COVID/eleições",
    "Tipo/método: pesquisa de campo qualitativa, questionário online",
    "Amostra: não informado no resumo (apenas 'professores da rede básica de ensino')",
    "Achado: os professores percebem efeitos pessoais, sociais e pedagógicos das fake news na escola e propõem ações de educação para/com/sobre as mídias",
    "Trecho literal: \"os professores percebem as implicações pessoais, sociais e pedagógicas da chegada da fake news na escola\""
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
   "venue": "Revista Areté | Revista Amazônica de Ensino de Ciências",
   "checked_url": "https://periodicos.uea.edu.br/index.php/arete/article/view/5277",
   "criteria_met": [
    "Tema: desinformação/pós-verdade + educação midiática",
    "Ensino formal e Brasil: licenciandos (universidades UEAP/UFOPA)",
    "Tipo/método: pesquisa qualitativa com estudantes de Licenciatura em Informática Educacional",
    "Amostra: não informado no resumo (apenas 'estudantes de Licenciatura em Informática Educacional')",
    "Achado: a educação midiática na formação inicial é apresentada como pilar fundamental para uma sociedade crítica e informada, embora a educação sozinha não resolva o problema",
    "Trecho literal: \"é pilar fundamental na construção de uma sociedade crítica e informada\" (fragmento; a frase completa do resumo é mais longa). Atenção: o resumo não detalha a coleta de dados"
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
   "venue": "Interin (UTP)",
   "checked_url": "https://seer.utp.br/index.php/i/article/view/3552",
   "criteria_met": [
    "Tema: literacia midiática + desordem informacional/desinformação",
    "Ensino formal e Brasil: estudantes do ensino médio de escolas públicas e privadas de São Paulo",
    "Tipo/método: estudo empírico qualitativo, entrevistas em profundidade com protocolo de literacia midiática",
    "Amostra: \"trinta e seis alunos de escolas públicas e privadas, em São Paulo\"",
    "Achado: os jovens valorizam a checagem, mas têm pouco engajamento cívico nas redes e compreensão limitada dos algoritmos; falta uso aprofundado de mídia na escola",
    "Trecho literal: \"a valorização da checagem de informações pelos jovens\" (fragmento do resumo)"
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
   "venue": "Signo (UNISC)",
   "checked_url": "https://seer.unisc.br/index.php/signo/article/view/20198",
   "criteria_met": [
    "Tema: fake news/desinformação + literacia e pensamento crítico",
    "Ensino formal: estudantes do Ensino Médio; Brasil (Signo/UNIVATES; escola brasileira)",
    "Tipo/método: intervenção com grupo experimental (1º ano) e grupo controle (2º ano), avaliação inicial e final, cinco oficinas",
    "Amostra: não informado no resumo (apenas 'dois grupos, um experimental (1º ano) e outro controle (2º ano)')",
    "Achado: as oficinas não geraram a melhora esperada no reconhecimento de fake news, mas influenciaram positivamente a decisão de compartilhar",
    "Trecho literal: \"mas influenciaram positivamente na decisão sobre o seu compartilhamento\" (fragmento; também: \"não geraram o impacto esperado no reconhecimento de fake news\")"
   ]
  },
  {
   "doi": "10.22478/ufpb.2763-9398.2022v16n.61652",
   "title": "A identificação de fake news por alunos e professores: um experimento em escolas públicas no Brasil",
   "authors": [
    "Diego de Deus",
    "Adinan Nogueira"
   ],
   "year": 2022,
   "venue": "Culturas Midiáticas (UFPB)",
   "checked_url": "https://periodicos.ufpb.br/index.php/cm/article/view/61652",
   "criteria_met": [
    "Tema: fake news + literacia informacional e midiática",
    "Ensino formal e Brasil: alunos e professores do ensino médio de duas escolas públicas",
    "Tipo/método: estudo exploratório e experimental (framing persuasivo)",
    "Amostra: não informado no resumo (apenas 'duas escolas públicas')",
    "Achado: enquadramento persuasivo e fatores de literacia não se relacionaram à detecção de fake news; há déficit entre o conhecimento declarado e a capacidade de detectar notícia teoricamente verdadeira, em alunos e professores",
    "Trecho literal: \"Trata-se de um estudo exploratório e experimental.\" e \"existe um déficit entre o que se declara de conhecimento a respeito do assunto\" (fragmentos)"
   ]
  },
  {
   "doi": "10.55738/alaic.v23i46.1118",
   "title": "A Identificação De Desinformação Por Alunos E Professores No Brasil",
   "authors": [
    "Diego de Deus",
    "Adinan Nogueira",
    "Ariely Masetti"
   ],
   "year": 2024,
   "venue": "Revista Latinoamericana de Ciencias de la Comunicación (ALAIC)",
   "checked_url": "https://revista.pubalaic.org/index.php/alaic/article/view/1118",
   "criteria_met": [
    "Tema: desinformação + educação midiática/literacias (palavras-chave: Disinformation; Media Education; Literacies; High School)",
    "Ensino formal e Brasil: professores e alunos do Ensino Médio de escolas públicas e privadas",
    "Tipo/método: estudo empírico de habilidade de identificar fake news e efeito de conteúdo educativo sobre desinformação",
    "Amostra: não informado no resumo",
    "Achado: apenas explicar o que é informação falsa e como verificar é insuficiente; são necessários planos de longo prazo de pensamento crítico",
    "Trecho literal: \"Os resultados apontam a insuficiência de apenas explicar o que é informação falsa e como verificar.\" Atenção: mesma dupla de autores do estudo de 2022 (Culturas Midiáticas); possível sobreposição de dados"
   ]
  },
  {
   "doi": "10.26512/rici.v18.n2.2025.56629",
   "title": "Competência para reconhecer desinformação nas redes sociais: diagnóstico com estudantes ingressantes em cursos de graduação",
   "authors": [
    "Nadi Helena Presser",
    "Edla Barbosa de Santana",
    "Ana Reyes Pacios Lozano"
   ],
   "year": 2025,
   "venue": "Revista Ibero-Americana de Ciência da Informação (RICI)",
   "checked_url": "https://periodicos.unb.br/index.php/RICI/article/view/56629",
   "criteria_met": [
    "Tema: desinformação + competência crítica em informação",
    "Ensino superior e Brasil: ingressantes de 10 universidades públicas brasileiras",
    "Tipo/método: pesquisa diagnóstica, análise descritiva e avaliação quantitativa por questionário",
    "Amostra: \"196 estudantes ingressantes de graduação de 10 universidades públicas do Brasil\"",
    "Achado: a alta conectividade não torna os ingressantes especialistas em reconhecer informações falsas; precisam de formação em competência crítica em informação",
    "Trecho literal: \"os estudantes necessitam de qualificação em competência crítica em informação\""
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
   "venue": "Revista Brasileira de Biblioteconomia e Documentação (RBBD)",
   "checked_url": "https://rbbd.febab.org.br/rbbd/article/view/1791",
   "criteria_met": [
    "Tema: competência em informação + desinformação",
    "Ensino superior e Brasil: currículos de Biblioteconomia de universidades federais brasileiras",
    "Tipo/método: pesquisa documental e descritiva (ementas, PPPs, planos de ensino), análise de conteúdo de Bardin",
    "Amostra: \"documentos institucionais como ementas, projetos político-pedagógicos, e planos de ensino\" (número de cursos não informado no resumo; 82 disciplinas identificadas)",
    "Achado: nenhuma disciplina trata diretamente da desinformação e só oito tratam especificamente de competência em informação",
    "Trecho literal: \"nenhuma das disciplinas trabalham diretamente a questão da desinformação\" (fragmento)"
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
   "venue": "Mídia e Cotidiano (UFF)",
   "checked_url": "https://periodicos.uff.br/midiaecotidiano/article/view/38091",
   "criteria_met": [
    "Tema: desinformação/fake news + educação midiática/news literacy (palavras-chave)",
    "Ensino formal e Brasil: professores de educação básica; mapeamento de iniciativas no Brasil (PUC-Rio)",
    "Tipo/método: artigo com histórico, mapeamento de iniciativas e achados de survey com professores. Parte do artigo é de revisão; o componente empírico é o levantamento com professores",
    "Amostra: não informado no resumo ('professores/as de educação básica')",
    "Achado: a preocupação com a educação midiática para notícias precisa ser apoiada pela comunidade escolar",
    "Trecho literal: \"Conclui-se que a preocupação em relação à educação midiática para notícias precisa ser apoiada pela comunidade escolar\" (fragmento)"
   ]
  },
  {
   "doi": "10.47681/rca.v10i.63764",
   "title": "Ações formativas para o enfrentamento da desinformação: reflexões a partir de uma experiência com estudantes",
   "authors": [
    "Daniela de Assis Silva",
    "Gleise Brandão",
    "Allana Beatriz Mouta",
    "Laura Pita",
    "Letícia Neiva"
   ],
   "year": 2025,
   "venue": "Revista Conhecimento em Ação (UFRJ)",
   "checked_url": "https://revistas.ufrj.br/index.php/rca/article/view/63764",
   "criteria_met": [
    "Tema: desinformação + educação midiática/educação em informação (palavras-chave)",
    "Ensino formal e Brasil: escola pública estadual em Salvador (BA)",
    "Tipo/método: relato de experiência (extensão universitária) com roda de conversa e oficina; análise qualitativa da produção dos estudantes",
    "Amostra: \"a participação de 49 estudantes na roda de conversa e de seis alunos na oficina\"",
    "Achado: as peças produzidas pelos seis estudantes evidenciam processo reflexivo sobre a informação em contexto de desinformação",
    "Trecho literal: \"evidenciam o processo reflexivo dos jovens\" (fragmento). Este não é o relato 'Bora Checar' (esse saiu em anais)"
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
   "venue": "Observatorio (OBS*)",
   "checked_url": "http://obs.obercom.pt/index.php/obs/article/view/2435",
   "criteria_met": [
    "Tema: desinformação/fake news/pós-verdade + educação midiática",
    "Ensino formal e Brasil: estudantes de escolas públicas e privadas de Curitiba e Colombo (PR)",
    "Tipo/método: pesquisa qualitativa exploratória com oficinas de educação midiática",
    "Amostra: \"young students from 14 to 21 years old in Curitiba and Colombo in Paraná, Brazil\" (número não informado no resumo)",
    "Achado: as oficinas indicaram caminhos para desenvolver competências midiáticas nas culturas juvenis",
    "Trecho literal: \"The workshop analyses suggested clues to build media competencies in the youth culture contexts.\" (conforme a página; a pesquisa não é centrada em eleições ou COVID)"
   ]
  },
  {
   "doi": "10.23860/jmle-2025-17-2-5",
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
   "venue": "Journal of Media Literacy Education",
   "checked_url": "https://digitalcommons.uri.edu/jmle/vol17/iss2/5/",
   "criteria_met": [
    "Tema: educação midiática e informacional + desordem informacional/desinformação",
    "Ensino formal e Brasil: estudantes de escola pública brasileira (projeto da UnB)",
    "Tipo/método: survey e observação participante de oficina realizada em outubro de 2021",
    "Amostra: \"This study involves a survey and participant observation from a workshop conducted with these students in October 2021.\" (número não informado no resumo; estudantes do ensino fundamental)",
    "Achado: três estratégias (refletir sobre as próprias práticas informacionais, usar as experiências para avaliar a qualidade da informação e desnormalizar a desinformação) promovem a MIL",
    "Trecho literal: \"The major strategies used to promote MIL practices and critical thinking among the students were:\" (fragmento introdutório da lista de estratégias)"
   ]
  },
  {
   "doi": "10.5752/p.2358-3428.2021v25n54p235-264",
   "title": "Competências em práticas letradas de estudantes de Ensino Médio no contexto da desordem informacional",
   "authors": [
    "Ana Cláudia Bertini Ciencia"
   ],
   "year": 2021,
   "venue": "Scripta (PUC Minas)",
   "checked_url": "http://periodicos.pucminas.br/index.php/scripta/article/view/26661",
   "criteria_met": [
    "Tema: desordem informacional/informação falsa + letramentos midiáticos e informacionais (palavras-chave)",
    "Ensino formal e Brasil: aluno de escola pública de São José do Rio Preto (SP); referência à BNCC",
    "Tipo/método: análise de produções textuais dos estudantes (estudo empírico, Novos Estudos do Letramento)",
    "Amostra: \"105 produções textuais coletadas em uma escola pública de São José do Rio Preto\"",
    "Achado: os estudantes reconhecem informação falsa por critérios ligados à norma culta e pouco percebem as vozes e crenças que atravessam a desordem informacional",
    "Trecho literal: \"são competentes em reconhecer informação falsa com base em critérios relacionados ao uso de norma culta\" (fragmento). Os dados são de 2019, anteriores à pandemia; a COVID-19 só é mencionada na discussão"
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
   "venue": "Revista Docência e Cibercultura (UERJ)",
   "checked_url": "https://www.e-publicacoes.uerj.br/index.php/re-doc/article/view/68237",
   "criteria_met": [
    "Tema: fake news + letramento informacional",
    "Ensino superior e Brasil: estudantes de Pedagogia a distância da UFMT",
    "Tipo/método: pesquisa-formação na cibercultura, com percursos formativos",
    "Amostra: não informado no resumo (apenas 'estudantes do curso de Licenciatura em Pedagogia, modalidade à distância')",
    "Achado: o letramento informacional é prática importante contra a desinformação na educação básica e estimula reflexão e pensamento crítico",
    "Trecho literal: \"o letramento informacional é uma prática importante no combate à desinformação gerada pelas Fake News\" (fragmento)"
   ]
  },
  {
   "doi": "10.36661/2595-4520.2025v8n1.15332",
   "title": "Contribuições Formativas para Alfabetização Científica e Midiática: Percepções de Estudantes de Licenciatura em Ciências Exatas",
   "authors": [
    "Victoria Emilia Gomes Martins",
    "Tiago Venturi",
    "Roberta Chiesa Bartelmebs"
   ],
   "year": 2025,
   "venue": "Revista Insignare Scientia (UFFS)",
   "checked_url": "https://periodicos.uffs.edu.br/index.php/RIS/article/view/15332",
   "criteria_met": [
    "Tema: alfabetização midiática + fake news/desinformação",
    "Ensino superior e Brasil: licenciandos em Ciências Exatas (UFPR)",
    "Tipo/método: estudo de percepções de licenciandos. O resumo não nomeia o método",
    "Amostra: não informado no resumo (apenas 'licenciandos')",
    "Achado: os licenciandos veem as redes sociais como fontes rápidas, mas vulneráveis a fake news, e a formação em alfabetização científica e midiática é fragmentada",
    "Trecho literal: \"a formação ainda é fragmentada e limitada a experiências isoladas, em disciplinas específicas.\" Publicado em 16-12-2025, dentro do período"
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
   "venue": "Biblionline (UFPB)",
   "checked_url": "http://periodicos.ufpb.br/index.php/biblio/article/view/43786",
   "criteria_met": [
    "Tema: fake news + letramento informacional/competências de avaliação da informação (bibliotecário escolar)",
    "Ensino formal e Brasil: alunos do ensino médio de escola particular; estudantes de Biblioteconomia da UFS",
    "Tipo/método: relato de experiência com coleta de dados, abordagem quanti-qualitativa, questionário fechado e uma questão aberta após palestra",
    "Amostra: \"A palestra para 45 alunos do ensino médio teve participação direta dos discentes\" (fragmento)",
    "Achado: a palestra foi esclarecedora para os alunos, que usam pouco a biblioteca escolar",
    "Trecho literal: \"Os principais resultados apontaram que a palestra foi bastante esclarecedora para a turma, em diversos aspectos.\""
   ]
  },
  {
   "doi": "10.59616/cehd.v3i9.2715",
   "title": "Letramento midiático e informacional nas aulas de língua portuguesa: os desafios e as possibilidades de estimular o novo ethos do aluno do Ensino Médio na era da desinformação",
   "authors": [
    "Angela Maria Silveira Batista",
    "Rosekeyla de Araújo Costa"
   ],
   "year": 2025,
   "venue": "Convergências: estudos em Humanidades Digitais",
   "checked_url": "https://periodicos.ifg.edu.br/cehd/article/view/2715",
   "criteria_met": [
    "Tema: letramento midiático e informacional + desinformação (palavras-chave)",
    "Ensino formal e Brasil: material pedagógico para o Ensino Médio (Guia da Educação Midiática, Ferrari et al., 2020); autoras da UECE",
    "Tipo/método: análise de conteúdo (Bardin) de material didático. A análise documental não tem participantes",
    "Amostra: as 15 atividades do Guia da Educação Midiática (Ferrari et al., 2020)",
    "Achado: as atividades são orientadas ao letramento midiático e informacional; 70% mostram concepção reflexiva de letramento digital",
    "Trecho literal: \"70% das atividades propostas evidenciaram a concepção de LD quanto à reflexão.\" Limítrofe: o objeto é guia de atividades de educação midiática, não livro didático formal"
   ]
  },
  {
   "doi": "10.22409/rmc.v19i2.66810",
   "title": "Educação midiática: o comportamento de estudantes nas redes sociais e a propagação de informações falsas",
   "authors": [
    "Paulo Henrique Soares Almeida",
    "Ana Carolina Kalume Maranhão"
   ],
   "year": 2025,
   "venue": "Mídia e Cotidiano (UFF)",
   "checked_url": "https://www.periodicos.uff.br/midiaecotidiano/article/view/66810",
   "criteria_met": [
    "Tema: informações falsas + educação midiática (palavras-chave)",
    "Ensino formal e Brasil: estudantes do ensino médio de escolas públicas e particulares do Distrito Federal",
    "Tipo/método: survey com questionários estruturados, coleta entre novembro de 2023 e março de 2024",
    "Amostra: \"questionários estruturados aplicados a 180 alunos de escolas públicas e particulares\"",
    "Achado: os estudantes têm deficiência expressiva em educação midiática, e o estudo defende estratégias para análise crítica e compartilhamento responsável",
    "Trecho literal: \"Os resultados revelam uma deficiência expressiva na educação midiática desses jovens.\" O DOI foi lido na página do artigo; não abri a resolução doi.org"
   ]
  },
  {
   "doi": "10.29146/eco-ps.v28i1.28441",
   "title": "Letramento midiático em desertos de notícias: manual de checagem contra desinformação em Itaueira (PI)",
   "authors": [
    "Juliana Fernandes Teixeira",
    "Cristiane Portela de Carvalho",
    "Marta Thais Alencar"
   ],
   "year": 2025,
   "venue": "Revista Eco-Pós",
   "checked_url": "https://revistaecopos.eco.ufrj.br/eco_pos/article/view/28441",
   "criteria_met": [
    "Tema: letramento midiático + desinformação/checagem",
    "Ensino formal e Brasil: aplicação do manual em salas de aula de Itaueira (PI), com estudantes e professores",
    "Tipo/método: estudo de caso baseado em pesquisa survey",
    "Amostra: \"uma pesquisa survey com 53 estudantes e professores deste município\" (fragmento)",
    "Achado: quase metade dos participantes não tem o letramento necessário para entender como a notícia é produzida",
    "Trecho literal: \"O estudo revelou que quase metade não possui o letramento necessário para compreender o processo de produção da notícia\""
   ]
  },
  {
   "doi": "10.15847/obsOBS18520242446",
   "title": "Perceptions of University Students in Communication about Disinformation: An Exploratory Analysis in Brazil, Colombia and Spain",
   "authors": [
    "Juliana Colussi",
    "Paula de Souza Paes",
    "Rainer Rubira-García",
    "Thays Assunção Reis"
   ],
   "year": 2024,
   "venue": "Observatorio (OBS*)",
   "checked_url": "https://obs.obercom.pt/index.php/obs/article/view/2446",
   "criteria_met": [
    "Tema: desinformação + educação midiática no currículo (como a formação universitária trata a media literacy)",
    "Ensino superior; estudo comparativo internacional com amostra brasileira (Brasil no título; autores da UFPB e da UFT)",
    "Tipo/método: survey online exploratório, maio a julho de 2023, em 23 centros de ensino superior",
    "Amostra: \"answered by 231 students\" (total dos três países; a parte brasileira não é informada no resumo)",
    "Achado: os estudantes sabem o que são fake news e a maioria sabe identificá-las; a media literacy é tratada de forma transversal, sem disciplina específica",
    "Trecho literal: \"university students are aware of what fake news are and most of them know how to identify disinformative content.\" Foco de desinformação geral, não eleitoral ou de COVID. O DOI foi lido na página do artigo"
   ]
  },
  {
   "doi": "10.17058/signo.v49i94.18842",
   "title": "A BNCC e as garantias do direito à informação para o exercício da cidadania: aspectos centrais para a implementação do letramento midiático e informacional nas escolas brasileiras",
   "authors": [
    "Nathalie Resende de Carvalho"
   ],
   "year": 2024,
   "venue": "Signo (UNISC)",
   "checked_url": "http://seer.unisc.br/index.php/signo/article/view/18842",
   "criteria_met": [
    "Tema: letramento midiático e informacional + desinformação/fake news (BNCC)",
    "Ensino formal e Brasil: currículo nacional (BNCC) e escolas brasileiras",
    "Tipo/método: análise do documento normativo BNCC. O resumo não nomeia o método e o artigo pode ser lido como análise normativa/ensaística, então é o item mais incerto quanto ao tipo de estudo",
    "Amostra: \"um documento normativo que trata das aprendizagens em nível nacional\" (a BNCC)",
    "Achado: o direito à informação e à cidadania plena não é assegurado de forma sistemática na BNCC, e muitas escolas carecem de infraestrutura para o letramento midiático",
    "Trecho literal: \"o direito à informação e ao exercício pleno da cidadania não são assegurados de forma sistemática na BNCC\" (fragmento)"
   ]
  },
  {
   "doi": "10.5216/revufg.v20.65943",
   "title": "É fato ou é fake? Notícias falsas e pós-verdade no ensino de língua portuguesa",
   "authors": [
    "Patrícia Graciela Rocha",
    "Fabiana Biondo"
   ],
   "year": 2020,
   "venue": "Revista UFG",
   "checked_url": "https://www.revistas.ufg.br/revistaufg/article/view/65943",
   "criteria_met": [
    "Tema: notícias falsas/pós-verdade + letramentos críticos. A ligação com 'educação midiática' é indireta; o resumo fala em letramentos críticos, não em media literacy",
    "Ensino formal e Brasil: livros didáticos de Língua Portuguesa da rede municipal de Campo Grande (MS)",
    "Tipo/método: análise documental de coleção de livros didáticos",
    "Amostra: \"a coleção de Livros Didáticos de Língua Portuguesa dos anos finais do Ensino Fundamental\"",
    "Achado: os livros tratam o tema de forma superficial e pouco engajada com os letramentos críticos",
    "Trecho literal: \"As análises revelam uma abordagem superficial sobre o tema\" (fragmento)"
   ]
  }
 ],
 "notes": "RESULTADO: entreguei 22 artigos, menos que os 25 pedidos. Preferi não completar a cota com itens que não atendem a tudo. Busquei em Crossref (API), na web e nas páginas dos periódicos. A API do OpenAlex devolveu HTTP 429 em todas as tentativas, então a busca em OpenAlex não foi feita. As bases SciELO e Crossref foram consultadas pela API do Crossref e pela busca na web, não pelo buscador próprio do SciELO.\n\nCOMO CONFERI: abri cada DOI em doi.org e li o resumo na página do periódico. Exceção: nos itens Almeida & Maranhão (10.22409/rmc.v19i2.66810), Silva et al. (10.47681/rca.v10i.63764), Ongaro et al. (10.15847/obsOBS18520242435) e Colussi et al. (10.15847/obsOBS18520242446), li o DOI na página do artigo e não abri a resolução doi.org. Os 22 DOIs aparecem nas páginas oficiais ou nos metadados do Crossref.\n\nLIMITAÇÃO NOS TRECHOS LITERAIS: a ferramenta de leitura só devolve trechos curtos (cerca de 125 caracteres). Os trechos entre aspas são fragmentos do resumo e não frases completas. Os resumos em português vieram da página do periódico. Recomendo comparar cada trecho com o resumo online antes de citar.\n\nITENS INCERTOS (estão na lista, mas o verificador deve olhar com atenção):\n- Signo 2024, BNCC (10.17058/signo.v49i94.18842): o resumo não nomeia o método. Pode ser lido como análise normativa ou ensaio.\n- Rocha & Biondo 2020 (10.5216/revufg.v20.65943): o resumo fala em 'letramentos críticos' e não em 'educação midiática'.\n- Batista & Costa 2025 (10.59616/cehd.v3i9.2715): analisa um guia de atividades de educação midiática, não um livro didático formal, e não tem participantes.\n- Areté 2025 (10.59666/arete.1984-7505.v24.n38.5277): o resumo não detalha a coleta de dados nem o número de participantes.\n- Chaves & Melo 2019 (10.22409/rmc.v13i3.38091): artigo misto (histórico e mapeamento de iniciativas, mais survey com professores). O resumo não informa o tamanho da amostra.\n- Colussi et al. 2024 (10.15847/obsOBS18520242446): amostra internacional (231 estudantes de Brasil, Colômbia e Espanha). O resumo não separa o número de brasileiros.\n- De Deus & Nogueira 2022 e De Deus, Nogueira & Masetti 2024 (ALAIC) são trabalhos distintos, mas da mesma dupla de autores e com desenho parecido. Pode haver sobreposição de dados.\n- Martins et al. 2025 (RIS, 10.36661/2595-4520.2025v8n1.15332) saiu em 16/12/2025. O DOI é de 2025, dentro do período.\n\nDESCARTADOS (principais motivos):\n- Pieranti & Trindade 2023 (10.22409/rmc.v17i3.58703): oficina da BBC News Brasil, fora do ensino formal.\n- Cerigatto 2020 (10.20873/uft.2447-4266.2020v6n6a4pt): só proposta, sem dados.\n- Moura et al. 2025, Missioneira (10.46550/5ksm2h78): revisão bibliográfica.\n- Souza 2025, Ciência & Educação (10.1590/1516-731320250028): tarefa baseada em vídeo sobre óbitos por COVID-19 em 2020.\n- Dias, Furnival & Casarin 2024, A to Z (revistas.ufpr.br/atoz/article/view/89709): o resumo diz que o objeto são notícias sobre COVID-19 (aula quiz com 32 estudantes de Biblioteconomia da UFSCar) e a palavra-chave inclui COVID-19. Excluí pela regra da COVID-19. É o único candidato que atendia ao resto e foi descartado só por isso. O DOI não consta na página do repositório.\n- Meyrer & Frank Kersch 2022, JMLE: fake news sobre COVID-19.\n- Gomes, Penna & Arroio 2020 (10.1590/1516-731320200018): 232 pessoas do público geral, não escolar.\n- Nagumo et al. 2022 (10.20396/etd.v24i1.8665292): ensaio.\n- Aguiar et al. 2024 (10.21680/2447-7842.2024v10n1id36807): revisão sistemática.\n- Maciel et al. 2025 (10.29146/eco-ps.v28i1.28458) e Kabuenge et al. 2025 (10.29146/eco-ps.v28i1.28459): revisões.\n- Christofoletti 2025 (10.29146/eco-ps.v28i1.28436): proposta teórica.\n- Carvalho & Teixeira 2025 (10.36732/editoranovapaideia.2025.713): a página o classifica como capítulo de livro.\n- Guisardi & Ottoni 2020: proposta didática sem dados.\n- Pacheco & Paiva 2022 (Antígona): sem dados.\n- Nascimento & Lima-Neto 2023 (GELNE): trabalho de congresso, sem participantes.\n- Andrade & Cavalcanti 2022 (Interritórios): programas de rádio, público geral, durante a pandemia.\n- Santos & Sá 2021 (química): análise de notícias, parte sobre COVID-19, sem participantes.\n- Spera et al. 2022 (Biblionline): trata de fato versus opinião e o resumo não fala de desinformação.\n- Sousa et al. 2025 (Caderno Pedagógico, 10.54033/cadpedv22n7-207): experimento em escola de Fortaleza com fake news, mas o resumo só trata de 'letramento digital', sem foco em educação midiática ou informacional. Fica como possível inclusão se o pesquisador aceitar letramento digital como equivalente.\n- Santos & Carmona 2024 (EJA): revisão bibliográfica mais análise de documentos.\n- Ribeiro et al. 2024 (Identidade!): o item vem de anais de congresso e a página não traz DOI.\n- Agra et al. 2023 (R15O, 10.5281/zenodo.10072479): análise de livro didático sobre fake news, mas o resumo não menciona educação midiática ou letramento. Pode ser reavaliado, é um bom candidato de reserva.\n- Kneipp 2025 (Revista Mediação), Gonçales & Corbari 2025 (Aproximação) e Nunes & Ribeiro (Humanidades & Inovação): as páginas não trazem DOI.\n- Alencar & Pôrto Júnior (10.20873/uft.2447-4266.2026v12n1a09pt): ano ambíguo (2025 na publicação online, 2026 no fascículo e no DOI) e o resumo não diz que o estudo é no Brasil.\n- Catalina-García et al. 2019 (Revista de Comunicación): estudantes de Comunicação do Brasil, Espanha e Portugal. O foco é percepção de fake news, sem educação midiática.\n- Ribeiro et al. 2024 (Educação, Escola & Sociedade): foco em negacionismo, com público geral.\n- Cavalheiro & Parzianello 2024 (Missões): trata de alimentação escolar.\n- Scarcella 2024 (MLS Communication Journal): formação profissional não escolar.\n- Rondon do Pará, Mosaico/FGV: foco eleitoral.\n- Estudo de vacinas em Campinas: foco em vacinas.\n- Bora Checar, Pare e Pense e Verifato: trabalhos de anais ou seminário.\n- Dissertações e TCCs.\n\nSUGESTÃO para completar as 3 vagas restantes: reavaliar Agra et al. 2023 e Sousa et al. 2025 como reservas, se o pesquisador aceitar letramento crítico/digital como equivalente a educação midiática. Também vale rodar OpenAlex quando o limite de requisições for liberado e buscar em Comunicação & Educação, Educação & Sociedade e Revista Brasileira de Educação."
}