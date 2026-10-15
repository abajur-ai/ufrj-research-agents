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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre jogos educativos e jogos de inoculação (prebunking) contra desinformação, como o Bad News. Restrições: apenas intervenções em forma de jogo (digital ou de tabuleiro) avaliadas com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção; exclua intervenções que não são jogos (vídeos, textos ou infográficos isolados), reanálises de dados de outros estudos e estudos centrados em COVID-19, vacinas, eleições ou política partidária (por exemplo, o Go Viral!). Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO A VERIFICAR:
{
 "criteria": [
  "Tema: jogos educativos e jogos de inoculação (prebunking) contra desinformação/fake news/manipulação de informação (ex.: Bad News, Harmony Square, Cranky Uncle, Fake It to Make It, Cat Park, Escape-room/tabuleiro sobre desinformação, jogos de literacia midiática).",
  "Formato da intervenção: o jogo (digital, de tabuleiro, de cartas, escape room, role-play lúdico) deve ser a intervenção avaliada; excluir intervenções que sejam apenas vídeos, textos, infográficos, quizzes ou aulas sem mecânica de jogo.",
  "Período: publicado entre 2018 e 2025 (conferir ano de publicação oficial do periódico, não apenas a data online antecipada).",
  "Tipo de publicação: artigo de periódico revisado por pares; excluir preprints (OSF, PsyArXiv, SSRN, arXiv), anais de congresso, capítulos, teses/dissertações, resenhas.",
  "Tipo de estudo: estudo empírico com dados próprios; excluir revisões de literatura (sistemáticas ou narrativas), meta-análises, ensaios teóricos e reanálises de dados de outros estudos.",
  "Desenho: experimento, quase-experimento, ensaio controlado randomizado ou desenho pré e pós-intervenção, com participantes humanos que jogaram o jogo.",
  "Exclusão temática: estudos centrados em COVID-19, vacinas, eleições ou política partidária (ex.: Go Viral!, jogos sobre eleições); manter jogos sobre desinformação geral, climática, de saúde não ligada a COVID/vacinas, extremismo, etc., se não forem centrados nos temas excluídos.",
  "Meta: 25 artigos que atendam a todos os critérios, cada um com DOI, título, autores, ano, periódico, tipo de estudo e método, tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'), achado principal em uma frase e trecho literal do resumo entre aspas que sustente o achado.",
  "Idioma: sem restrição declarada; buscar em inglês e português (e aceitar outros idiomas se o resumo estiver acessível)."
 ],
 "queries": [
  {
   "query": "(\"inoculation\" OR \"prebunking\") AND (game OR gamified OR \"serious game\") AND (misinformation OR disinformation OR \"fake news\")",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"Bad News\" game misinformation inoculation experiment",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "(\"Harmony Square\" OR \"Cranky Uncle\" OR \"Fake It to Make It\" OR \"Cat Park\" OR \"Bad News\") game randomized OR experiment OR \"pre-post\"",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "(\"serious game\" OR \"educational game\" OR \"board game\" OR \"escape room\") AND (\"media literacy\" OR misinformation OR disinformation OR \"fake news\") AND (quasi-experimental OR \"pre-test\" OR \"post-test\" OR randomized)",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "game-based intervention fake news resistance psychological inoculation journal article",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "jogo educativo OR \"jogo sério\" OR \"jogo de tabuleiro\" desinformação OR \"fake news\" OR \"notícias falsas\" letramento midiático experimento OR \"pré e pós-teste\" OR quase-experimental",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "jogos de inoculação prebunking desinformação gamificação avaliação com participantes",
   "language": "pt",
   "database": "OpenAlex"
  },
  {
   "query": "Bad News game Roozenbeek van der Linden prebunking game peer-reviewed study replication cross-cultural",
   "language": "en",
   "database": "busca na web"
  }
 ],
 "how_to_check": [
  "Tema: ler título e resumo de cada candidato e confirmar que a intervenção é um jogo voltado a desinformação/fake news/manipulação (não apenas menciona 'gamificação' de passagem).",
  "Formato de jogo: no resumo/método, confirmar que a intervenção é um jogo (digital, tabuleiro, cartas, escape room); descartar se for vídeo, texto, infográfico, quiz ou aula isolada.",
  "Período: conferir o ano de publicação no registro do DOI (Crossref/OpenAlex 'publication_year' e data da edição); descartar fora de 2018–2025 e anotar divergência entre data online e da edição.",
  "Tipo de publicação: verificar no Crossref/OpenAlex que o tipo é 'journal-article' e que a fonte é periódico (não repositório de preprint, anais, capítulo ou tese); confirmar no site do periódico se é revisado por pares.",
  "Estudo empírico com dados próprios: confirmar no resumo/método que há coleta de dados nova; descartar revisões, meta-análises, ensaios teóricos, reanálises de dados de estudos anteriores (checar termos como 'reanalysis', 'secondary analysis', 'pooled data', 'meta-analysis').",
  "Desenho: confirmar no resumo a presença de grupo de controle/randomização, pré e pós-teste ou comparação experimental/quase-experimental com participantes; descartar estudos só de desenho do jogo, de opinião ou de usabilidade sem avaliação de efeito.",
  "Exclusões temáticas: verificar título, resumo e palavras-chave por COVID-19, vaccine/vacina, election/eleição, partisan/política partidária (inclui Go Viral!); descartar quando esses temas forem o foco da intervenção ou da avaliação.",
  "Duplicatas: deduplicar por DOI; se houver versão preprint e versão de periódico, manter apenas a do periódico; usar DOI da versão publicada.",
  "Tamanho da amostra: copiar literalmente do resumo (ex.: 'N = 15.000'); se não houver número no resumo, registrar 'não informado no resumo'. Não usar números do corpo do artigo.",
  "Trecho literal: copiar do resumo recuperado (via Crossref/OpenAlex/site do periódico) entre aspas, sem paráfrase, e conferir que sustenta o achado principal; se o resumo estiver indisponível, marcar como pendente em vez de inventar.",
  "Metadados: validar DOI resolvendo em doi.org/Crossref e conferir título, autores, ano e periódico com o registro; descartar candidatos sem DOI verificável.",
  "Cobertura: se menos de 25 candidatos passarem, registrar quantos passaram e quais critérios eliminaram os demais, em vez de completar com itens que violem os critérios."
 ]
}