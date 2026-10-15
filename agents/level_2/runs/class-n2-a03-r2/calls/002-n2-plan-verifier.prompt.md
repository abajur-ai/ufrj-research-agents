# Verificador do plano de busca
Você é um verificador independente. Confira se o plano cobre TODOS os critérios do pedido do pesquisador (tema,
período, tipo de publicação, método, recorte), se as consultas encontram o tema em inglês e em português, e se cada
critério tem um jeito concreto de ser conferido. Reprove plano que esquece um critério, muda o período ou o tema.
Não precisa buscar na web.

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

PLANO A VERIFICAR:
{
 "criteria": [
  "Tema: desinformação (fake news, notícias falsas, misinformation, disinformation) E educação midiática / alfabetização midiática / competência em informação / letramento informacional / letramento midiático e informacional (MIL) como tema central ou eixo da intervenção/análise",
  "Período: publicado entre 01/01/2018 e 31/12/2025 (conferir ano de publicação oficial do periódico/Crossref, não só data online first)",
  "Tipo de publicação: artigo de periódico revisado por pares (excluir preprints, anais de congresso, capítulos de livro, teses/dissertações, resenhas, editoriais)",
  "Tipo de estudo: estudo empírico com dados próprios (questionário, entrevista, grupo focal, intervenção/quase-experimento, relato de experiência COM coleta de dados, análise documental de currículos, BNCC ou livros didáticos). Excluir revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos",
  "Contexto: ensino formal brasileiro (educação básica, ensino médio, técnico, graduação, pós-graduação, formação docente) com estudantes, professores, aulas, currículos ou livros didáticos",
  "Recorte geográfico: estudo realizado no Brasil; estudos comparativos internacionais só se incluírem amostra brasileira explícita",
  "Exclusões temáticas: estudos centrados em COVID-19, vacinas, eleições ou política partidária",
  "Exclusão de público: estudos com públicos fora do ensino formal (ex.: idosos na comunidade, público geral online, jornalistas profissionais, usuários de redes sociais em geral)",
  "Meta: 25 artigos distintos, sem duplicatas (mesmo estudo em versões PT/EN conta uma vez)",
  "Dados a extrair por artigo: DOI; título; autores; ano; periódico; tipo de estudo e método; tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'); achado principal em uma frase; trecho literal do resumo entre aspas que sustente o achado"
 ],
 "queries": [
  {
   "query": "(disinformation OR misinformation OR \"fake news\") AND (\"media literacy\" OR \"information literacy\" OR \"media and information literacy\") AND (Brazil OR Brazilian) AND (school OR students OR teachers OR university)",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "(desinformação OR \"fake news\" OR \"notícias falsas\") AND (\"educação midiática\" OR \"competência em informação\" OR \"letramento informacional\" OR \"alfabetização midiática\" OR \"competência midiática\") AND (escola OR estudantes OR professores OR universidade OR \"ensino médio\")",
   "language": "pt",
   "database": "OpenAlex"
  },
  {
   "query": "Brazil AND (disinformation OR \"fake news\") AND (\"media literacy\" OR \"information literacy\") AND (curriculum OR textbook OR BNCC OR classroom OR intervention OR survey)",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "desinformação AND (\"educação midiática\" OR \"competência em informação\" OR \"educação para as mídias\") AND (\"ensino fundamental\" OR \"ensino médio\" OR \"ensino superior\" OR \"formação de professores\")",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "\"fake news\" AND (letramento OR \"competência crítica em informação\" OR \"educação midiática\") AND (\"grupo focal\" OR questionário OR entrevista OR \"sequência didática\" OR \"livro didático\" OR \"análise documental\")",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "(\"media and information literacy\" OR \"news literacy\" OR \"digital literacy\") AND (disinformation OR \"fake news\") AND Brazil AND (\"high school\" OR undergraduate OR \"teacher education\" OR \"teacher training\") AND (\"quasi-experimental\" OR \"focus group\" OR questionnaire OR \"survey\")",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "Brazil AND \"comparative\" AND (\"media literacy\" OR \"digital literacy\") AND (disinformation OR misinformation) AND students AND (countries OR cross-national)",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "site:scielo.br OR site:periodicos.ufsc.br OR site:periodicos.ufmg.br \"desinformação\" \"educação midiática\" escola estudo empírico artigo revista",
   "language": "pt",
   "database": "busca na web"
  }
 ],
 "how_to_check": [
  "Tema (desinformação + educação midiática/competência em informação): ler título, resumo e palavras-chave; exigir que ambos os conceitos apareçam e que sejam centrais, não apenas citados de passagem.",
  "Período 2018–2025: conferir o ano de publicação no registro Crossref/OpenAlex (publication_year e issued date) e no site do periódico; descartar 2026 ou anterior a 2018; em caso de divergência entre online first e edição, registrar e decidir pelo ano da edição, anotando a divergência.",
  "Revisado por pares e tipo de publicação: confirmar via Crossref/OpenAlex que type = journal-article e que a fonte é periódico (não anais, capítulo, preprint, tese); checar no site do periódico a política de avaliação por pares; excluir seções de resenha, editorial ou ensaio.",
  "Estudo empírico com dados próprios: ler resumo e, se ambíguo, a seção de metodologia; exigir menção a coleta (amostra, instrumento, corpus documental, intervenção). Descartar revisões, estados da arte, ensaios teóricos e relatos de experiência sem coleta/análise de dados.",
  "Contexto de ensino formal: verificar no resumo/método o público (estudantes de escola ou universidade, professores, currículos, livros didáticos); descartar estudos com público geral, idosos, jornalistas, comunidade ou educação não formal.",
  "Brasil: checar no resumo/método o local (instituição, estado, rede de ensino) ou, em estudos comparativos, que o Brasil conste explicitamente na amostra; descartar se Brasil apenas contextualiza.",
  "Exclusões temáticas: procurar nos título, resumo e palavras-chave termos como COVID-19, pandemia, vacina, eleições, eleitoral, partido, bolsonarismo; excluir se forem o foco central do estudo.",
  "Duplicatas: comparar DOI normalizado e título normalizado; juntar versões em PT/EN do mesmo estudo.",
  "DOI: confirmar existência e resolução do DOI em Crossref (doi.org); se não houver DOI, registrar 'sem DOI' e sinalizar, sem inventar.",
  "Tamanho da amostra: copiar exatamente a expressão do resumo (ex.: 'n=120 estudantes'); se ausente, escrever 'não informado no resumo'; não buscar no texto completo nem estimar.",
  "Trecho literal: copiar do resumo exatamente como publicado (idioma original, sem tradução ou paráfrase), entre aspas, e conferir caractere a caractere contra o resumo no Crossref/OpenAlex/site do periódico; o trecho deve sustentar o achado principal escrito.",
  "Autores, periódico, ano: extrair dos metadados do Crossref/OpenAlex e conferir com a página do artigo; não preencher campos por memória.",
  "Contagem final: se houver menos de 25 candidatos que cumpram todos os critérios, entregar apenas os verificados e informar quantos faltam, em vez de completar com itens duvidosos."
 ]
}