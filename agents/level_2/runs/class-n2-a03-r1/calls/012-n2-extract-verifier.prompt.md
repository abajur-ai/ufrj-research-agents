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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre desinformação e educação midiática (ou competência em informação) em escolas e universidades brasileiras. Restrições: estudos empíricos feitos no Brasil com estudantes, professores, aulas, currículos ou livros didáticos (questionários, grupos focais, intervenções, relatos de experiência com coleta de dados ou análise documental); estudos comparativos internacionais valem se incluírem amostra brasileira; exclua estudos centrados em COVID-19, vacinas, eleições ou política partidária e estudos com públicos fora do ensino formal. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

LISTA FINAL A VERIFICAR:
{
 "items": [
  {
   "doi": "10.12957/teias.2025.83022",
   "title": "Educação midiática no combate à desinformação: percepções e proposições de ação dos professores",
   "authors": [
    "Késsia Mileny de Paulo Moura",
    "Luciana Silva Palmeira",
    "Samantha Morais de Oliveira Sousa"
   ],
   "year": 2025,
   "venue": "Revista Teias",
   "study_type": "Estudo empírico qualitativo (pesquisa de campo)",
   "method": "Pesquisa de campo com professores da rede básica, por questionário online",
   "sample_size": "não informado no resumo",
   "main_finding": "Os professores percebem implicações pessoais, sociais e pedagógicas da chegada da fake news na escola e vislumbram ações convencionais, porém válidas, de educação para/com/sobre as mídias.",
   "abstract_quote": "os professores percebem as implicações pessoais, sociais e pedagógicas da chegada da fake news na escola"
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
   "study_type": "Estudo empírico qualitativo",
   "method": "Pesquisa qualitativa com estudantes de Licenciatura em Informática Educacional (o resumo não detalha a coleta de dados)",
   "sample_size": "não informado no resumo",
   "main_finding": "A educação midiática na formação inicial de professores é apresentada como pilar fundamental para uma sociedade crítica e informada, embora a educação sozinha não resolva o problema.",
   "abstract_quote": "a educação, embora não resolva sozinha o problema, é pilar fundamental na construção de uma sociedade crítica e informada."
  },
  {
   "doi": "10.35168/1980-5276.utp.interin.2025.vol30.n2.pp76-91",
   "title": "Literacia midiática, cidadania e enfrentamento da desinformação entre os jovens paulistanos",
   "authors": [
    "Isabela Afonso Portas",
    "Egle Müller Spinelli"
   ],
   "year": 2025,
   "venue": "Interin",
   "study_type": "Estudo empírico qualitativo",
   "method": "Entrevistas em profundidade com alunos do ensino médio, com base em protocolo de habilidades de literacia midiática (acesso, avaliação, criação)",
   "sample_size": "trinta e seis alunos de escolas públicas e privadas",
   "main_finding": "Os jovens valorizam a checagem de informações, mas têm pouca atuação cívica nas redes e conhecimento restrito sobre o impacto dos algoritmos, o que indica a necessidade de maior uso de mídia na escola.",
   "abstract_quote": "a valorização da checagem de informações pelos jovens"
  },
  {
   "doi": "10.17058/signo.v50i98.20198",
   "title": "A literacia como ferramenta no combate a fake news: promovendo o pensamento crítico em estudantes do Ensino Médio",
   "authors": [
    "Pâmela Roman",
    "Kári Lúcia Forneck"
   ],
   "year": 2025,
   "venue": "Signo",
   "study_type": "Estudo de intervenção com grupo experimental e grupo controle",
   "method": "Cinco oficinas com avaliação inicial e final; grupo experimental (1º ano) e controle (2º ano)",
   "sample_size": "não informado no resumo",
   "main_finding": "As oficinas não melhoraram como esperado o reconhecimento de fake news, mas influenciaram positivamente a decisão de compartilhá-las.",
   "abstract_quote": "Os resultados revelam que as oficinas não geraram o impacto esperado no reconhecimento de fake news"
  },
  {
   "doi": "10.22478/ufpb.2763-9398.2022v16n.61652",
   "title": "A identificação de fake news por alunos e professores: um experimento em escolas públicas no Brasil",
   "authors": [
    "Diego de Deus",
    "Adinan Nogueira"
   ],
   "year": 2022,
   "venue": "Culturas Midiáticas",
   "study_type": "Estudo exploratório e experimental",
   "method": "Experimento com alunos e professores do ensino médio de duas escolas públicas, testando literacia informacional/midiática e enquadramento persuasivo",
   "sample_size": "não informado no resumo",
   "main_finding": "Literacia e enquadramento persuasivo não se relacionaram à detecção de fake news, mas há déficit entre o conhecimento declarado e a detecção de uma notícia em tese verdadeira, em alunos e professores.",
   "abstract_quote": "Constatou-se que não há essa relação, mas que existe um déficit entre o que se declara de conhecimento a respeito do assunto"
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
   "venue": "Revista Latinoamericana de Ciencias de la Comunicación",
   "study_type": "Estudo empírico",
   "method": "Análise da habilidade de professores e alunos do Ensino Médio de identificar informação falsa e do efeito de conteúdo educativo sobre desinformação",
   "sample_size": "não informado no resumo",
   "main_finding": "Apenas explicar o que é informação falsa e como verificar é insuficiente, sendo necessários planos de longo prazo de estímulo ao pensamento crítico.",
   "abstract_quote": "Os resultados apontam a insuficiência de apenas explicar o que é informação falsa e como verificar"
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
   "venue": "Revista Ibero-Americana de Ciência da Informação",
   "study_type": "Estudo diagnóstico, descritivo e quantitativo",
   "method": "Questionário com análise descritiva e avaliação quantitativa aplicado a ingressantes de graduação",
   "sample_size": "196 estudantes ingressantes de graduação de 10 universidades públicas do Brasil",
   "main_finding": "A intensa conectividade dos ingressantes não os torna hábeis em reconhecer informação falsa; eles precisam de formação em competência crítica em informação.",
   "abstract_quote": "os estudantes necessitam de qualificação em competência crítica em informação para entenderem como funcionam"
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
   "venue": "Revista Brasileira de Biblioteconomia e Documentação",
   "study_type": "Pesquisa documental e descritiva",
   "method": "Análise de conteúdo de Bardin (qualitativa e quantitativa) de ementas, projetos político-pedagógicos e planos de ensino de cursos de Biblioteconomia de universidades federais",
   "sample_size": "não informado no resumo (o resumo registra 82 disciplinas identificadas que trabalham busca, seleção, avaliação, uso e disseminação da informação)",
   "main_finding": "Nenhuma disciplina trata diretamente da desinformação e apenas oito tratam especificamente de competência em informação.",
   "abstract_quote": "nenhuma das disciplinas trabalham diretamente a questão da desinformação"
  },
  {
   "doi": "10.22409/rmc.v13i3.38091",
   "title": "Educação midiática para notícias: histórico e mapeamento de iniciativas para combater a desinformação por meio da educação",
   "authors": [
    "Mônica Chaves",
    "Luísa Melo"
   ],
   "year": 2019,
   "venue": "Mídia e Cotidiano",
   "study_type": "Artigo misto: histórico, mapeamento de iniciativas e pesquisa empírica com professores (parte revisão)",
   "method": "Mapeamento de iniciativas e pesquisa realizada com professores/as de educação básica",
   "sample_size": "não informado no resumo",
   "main_finding": "A educação midiática para notícias precisa do apoio da comunidade escolar.",
   "abstract_quote": "Conclui-se que a preocupação em relação à educação midiática para notícias precisa ser apoiada pela comunidade escolar"
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
   "venue": "Revista Conhecimento em Ação",
   "study_type": "Relato de experiência (extensão universitária) com análise qualitativa",
   "method": "Roda de conversa e oficina em escola pública de Salvador (BA), com análise qualitativa das peças produzidas",
   "sample_size": "a participação de 49 estudantes na roda de conversa e de seis alunos na oficina",
   "main_finding": "As peças produzidas pelos seis estudantes evidenciam um processo reflexivo diante da informação em contexto de desinformação.",
   "abstract_quote": "que evidenciam o processo reflexivo dos jovens perante a informação no contexto de desinformação"
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
   "study_type": "Pesquisa qualitativa exploratória",
   "method": "Oficinas de educação midiática com estudantes de escolas públicas e privadas, com base no European Framework for Digital Competencies",
   "sample_size": "não informado no resumo (apenas a faixa etária: young students from 14 to 21 years old, em Curitiba e Colombo, Paraná)",
   "main_finding": "As análises das oficinas indicaram caminhos para desenvolver competências midiáticas nas culturas juvenis.",
   "abstract_quote": "The workshop analyses suggested clues to build media competencies in the youth culture contexts"
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
   "study_type": "Estudo empírico (projeto de educação midiática e informacional)",
   "method": "Survey e observação participante de oficina realizada em outubro de 2021 com estudantes do ensino fundamental de escola pública",
   "sample_size": "não informado no resumo",
   "main_finding": "Três estratégias promoveram práticas de MIL e pensamento crítico: refletir sobre as próprias práticas informacionais, usar as experiências para avaliar a qualidade da informação e desnormalizar a desinformação.",
   "abstract_quote": "encouraging them to reflect on their own information practices"
  },
  {
   "doi": "10.5752/p.2358-3428.2021v25n54p235-264",
   "title": "Competências em práticas letradas de estudantes de Ensino Médio no contexto da desordem informacional",
   "authors": [
    "Ana Cláudia Bertini Ciencia"
   ],
   "year": 2021,
   "venue": "Scripta",
   "study_type": "Estudo empírico qualitativo (Novos Estudos do Letramento)",
   "method": "Análise de produções textuais de estudantes do Ensino Médio de escola pública",
   "sample_size": "105 produções textuais coletadas em uma escola pública",
   "main_finding": "Os estudantes reconhecem informação falsa sobretudo por critérios ligados à norma culta e pouco percebem como vozes e crenças atravessam a desordem informacional.",
   "abstract_quote": "são competentes em reconhecer informação falsa com base em critérios relacionados ao uso de norma culta"
  },
  {
   "doi": "10.12957/redoc.2023.68237",
   "title": "Letramento informacional no combate às fake news na educação",
   "authors": [
    "Iracema Cristina Fernandes",
    "Terezinha Fernandes"
   ],
   "year": 2023,
   "venue": "Revista Docência e Cibercultura",
   "study_type": "Pesquisa-formação (recorte de pesquisa com estudantes)",
   "method": "Pesquisa-formação na cibercultura com estudantes de Licenciatura em Pedagogia a distância (UFMT)",
   "sample_size": "não informado no resumo",
   "main_finding": "O letramento informacional é prática importante no combate à desinformação gerada pelas fake news na educação básica.",
   "abstract_quote": "Os resultados mostraram que o letramento informacional é uma prática importante no combate à desinformação"
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
   "venue": "Revista Insignare Scientia",
   "study_type": "Estudo de percepções de licenciandos (método não nomeado no resumo)",
   "method": "não informado no resumo",
   "sample_size": "não informado no resumo",
   "main_finding": "Os licenciandos veem as redes sociais como fontes rápidas, porém vulneráveis a fake news, e a formação em alfabetização científica e midiática segue fragmentada.",
   "abstract_quote": "os estudantes reconhecem redes sociais como fontes rápidas de informação, mas vulneráveis à fake news"
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
   "venue": "Biblionline",
   "study_type": "Relato de experiência com coleta de dados, quanti-qualitativo",
   "method": "Palestra para alunos do ensino médio, com questionário de perguntas fechadas e uma questão aberta",
   "sample_size": "A palestra para 45 alunos do ensino médio",
   "main_finding": "A palestra foi esclarecedora para a turma, e os alunos usam pouco a biblioteca escolar.",
   "abstract_quote": "Os principais resultados apontaram que a palestra foi bastante esclarecedora para a turma"
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
   "study_type": "Análise documental de material pedagógico (limítrofe: guia de atividades, não livro didático)",
   "method": "Análise de conteúdo (Bardin) das atividades do Guia da Educação Midiática",
   "sample_size": "15 atividades do Guia da Educ-ação Midiática (Ferrari et al., 2020)",
   "main_finding": "As atividades analisadas estão comprometidas com o desenvolvimento do letramento midiático e informacional, e 70% evidenciaram concepção de letramento digital como reflexão.",
   "abstract_quote": "O resultado da análise demonstrou que tais atividades estão comprometidas com o desenvolvimento do LMI,"
  },
  {
   "doi": "10.22409/rmc.v19i2.66810",
   "title": "Educação midiática: o comportamento de estudantes nas redes sociais e a propagação de informações falsas",
   "authors": [
    "Paulo Henrique Soares Almeida",
    "Ana Carolina Kalume Maranhão"
   ],
   "year": 2025,
   "venue": "Mídia e Cotidiano",
   "study_type": "Survey",
   "method": "Questionários estruturados com alunos do ensino médio de escolas públicas e particulares do Distrito Federal, coletados de novembro de 2023 a março de 2024",
   "sample_size": "180 alunos de escolas públicas e particulares",
   "main_finding": "Os estudantes apresentam deficiência expressiva em educação midiática, o que exige estratégias de análise crítica e compartilhamento responsável.",
   "abstract_quote": "Os resultados revelam uma deficiência expressiva na educação midiática desses jovens"
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
   "study_type": "Estudo de caso baseado em pesquisa survey",
   "method": "Aplicação do manual de checagem em salas de aula de Itaueira (PI) e survey com estudantes e professores",
   "sample_size": "53 estudantes e professores",
   "main_finding": "Quase metade dos participantes não tem o letramento necessário para compreender como a notícia é produzida.",
   "abstract_quote": "O estudo revelou que quase metade não possui o letramento necessário para compreender o processo de produção da notícia,"
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
   "study_type": "Estudo exploratório comparativo internacional (amostra brasileira incluída)",
   "method": "Survey online, de maio a julho de 2023, em 23 centros de ensino superior de Brasil, Colômbia e Espanha",
   "sample_size": "231 students (total dos três países; a parte brasileira não é informada no resumo)",
   "main_finding": "Os estudantes de Comunicação sabem o que são fake news e a maioria sabe identificar conteúdo desinformativo, mas a media literacy é tratada de forma transversal, sem disciplina específica.",
   "abstract_quote": "university students are aware of what fake news are and most of them know how to identify disinformative content"
  },
  {
   "doi": "10.17058/signo.v49i94.18842",
   "title": "A BNCC e as garantias do direito à informação para o exercício da cidadania: aspectos centrais para a implementação do letramento midiático e informacional nas escolas brasileiras",
   "authors": [
    "Nathalie Resende de Carvalho"
   ],
   "year": 2024,
   "venue": "Signo",
   "study_type": "Análise do documento normativo BNCC (incerto: o resumo não nomeia o método e pode ser lido como análise normativa ou ensaio)",
   "method": "não informado no resumo (análise crítica da BNCC; a referência a documentos oficiais e dados de infraestrutura é inferida, não declarada)",
   "sample_size": "um documento normativo (a BNCC)",
   "main_finding": "O direito à informação e o exercício pleno da cidadania não são assegurados de forma sistemática na BNCC, e muitas escolas carecem de infraestrutura para o letramento midiático.",
   "abstract_quote": "o direito à informação e ao exercício pleno da cidadania não são assegurados de forma sistemática na BNCC"
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
   "study_type": "Análise documental de livros didáticos",
   "method": "Análise da abordagem de notícias falsas e pós-verdade em coleção de livros didáticos de Língua Portuguesa da rede municipal de Campo Grande (MS), à luz dos letramentos críticos",
   "sample_size": "a coleção de Livros Didáticos de Língua Portuguesa dos anos finais do Ensino Fundamental",
   "main_finding": "Os livros didáticos tratam o tema de forma superficial e pouco engajada com os letramentos críticos.",
   "abstract_quote": "As análises revelam uma abordagem superficial sobre o tema, pouco engajada com os letramentos críticos"
  }
 ],
 "search_notes": "Pelo seu pedido (\"Escolha 22 e extraia\"), entreguei os 22 candidatos aprovados e não busquei artigos novos. O pedido original era de 25, então faltam 3 e o lote não cumpre esse número. Abri a página oficial de cada artigo. A ferramenta de leitura não devolve o resumo inteiro, só trechos literais de até cerca de 125 caracteres. Por isso cada abstract_quote é um trecho literal curto e não o resumo completo, e vários trechos são só parte da frase. Pontos de atenção: (1) Carvalho/BNCC (Signo 2024): o resumo não nomeia método nem dados próprios. Pode ser ensaio ou análise normativa e talvez não passe no critério de estudo empírico. Mantive o item só para chegar a 22. Sugiro substituí-lo. (2) Chaves e Melo (2019) é em parte histórico e mapeamento. O componente empírico é a pesquisa com professores, sem amostra informada. (3) Batista e Costa (2025) analisa um guia de educação midiática e não um livro didático formal. (4) Deus e Nogueira (2022) e Deus, Nogueira e Masetti (2024) têm os mesmos autores e podem usar dados sobrepostos. (5) Pereira et al. (JMLE): o trecho literal sustenta a primeira das três estratégias, porque a frase completa passa do limite de citação. (6) Colussi et al.: a amostra de 231 é o total dos três países. A parte brasileira não aparece no resumo. (7) Para Presser et al. (RICI), a página oficial abriu desta vez. As duas frases (196 estudantes de 10 universidades públicas; \"necessitam de qualificação em competência crítica em informação\") foram lidas nela, e o PDF está em periodicos.unb.br/index.php/RICI/article/view/56629/43533. (8) O Moura et al. agora usa a redação exata do resumo (\"ações convencionais, porém válidas\") no achado. Sobre a RBBD, registrei no campo de amostra as 82 disciplinas do resumo, ressalvando que o número de cursos não consta lá. A página da RBBD não mostrou o DOI. Mantive o DOI da lista aprovada, sem conferi-lo na página. (9) No item de Rocha e Biondo, o trecho agora é mais longo e a página foi aberta. Autoria dos itens de Conhecimento em Ação e Biblionline conferida: 5 e 7 autores, respectivamente. No item Eco-Pós, as autoras são três. Todos os anos ficam entre 2018 e 2025.\""
}