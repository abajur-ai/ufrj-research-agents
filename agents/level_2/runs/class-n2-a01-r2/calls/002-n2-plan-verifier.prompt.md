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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre o efeito de influência continuada da informação falsa (continued influence effect), isto é, o quanto as pessoas continuam a se apoiar em uma informação falsa depois de ela ser corrigida ou retratada. Restrições: apenas experimentos com participantes humanos que meçam crença ou raciocínio depois de uma correção ou retratação; os materiais devem ser neutros (cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde); exclua estudos com desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO A VERIFICAR:
{
 "criteria": [
  "Tema: efeito de influência continuada da informação falsa (continued influence effect, CIE) — uso continuado de informação falsa em inferências, raciocínio ou crença depois de correção/retratação.",
  "Período: publicados entre 2018 e 2025 (inclusive); conferir o ano de publicação oficial (versão final no periódico), não só o online-first.",
  "Tipo de publicação: artigo de periódico revisado por pares. Excluir preprints (PsyArXiv, OSF, SSRN, arXiv), anais de congresso, capítulos de livro, teses/dissertações e resenhas.",
  "Tipo de estudo: relato empírico com dados próprios. Excluir revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos/conceituais e comentários.",
  "Método: experimento com participantes humanos que meça crença ou raciocínio (p. ex., perguntas de inferência, avaliação de crença, referências à informação falsa) depois de uma correção ou retratação.",
  "Materiais neutros: cenários fictícios, relatos de eventos inventados (p. ex., incêndio em depósito) ou alegações sem conotação política ou de saúde.",
  "Exclusões temáticas: desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Em dúvida sobre saúde em geral, excluir ou sinalizar, pois o pedido pede materiais sem conotação de saúde.",
  "Entregáveis por artigo: DOI, título, autores, ano, periódico, tipo de estudo e método, tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'), achado principal em uma frase e trecho literal do resumo entre aspas que sustente o achado.",
  "Meta: 25 artigos que atendam a todos os critérios. Se houver menos de 25 elegíveis, entregar só os elegíveis e dizer quantos faltam, sem preencher com itens que não se qualificam."
 ],
 "queries": [
  {
   "query": "\"continued influence effect\" misinformation correction retraction experiment",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence\" AND (retraction OR correction) AND (inference OR reasoning OR belief)",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "\"continued influence effect\" fictional event report corrections misinformation memory",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "retractions of misinformation reliance on false information inferential reasoning event report experiment",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "\"continued influence effect\" OR \"continued influence\" corrections 2018..2025 journal article \"Journal of Experimental Psychology\" OR \"Memory & Cognition\" OR \"Applied Cognitive Psychology\" OR \"Journal of Applied Research in Memory and Cognition\"",
   "language": "en",
   "database": "busca na web"
  },
  {
   "query": "\"efeito de influência continuada\" OR \"influência continuada\" informação falsa correção retratação experimento",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "\"efeito de influência continuada\" desinformação correção crença raciocínio experimento",
   "language": "pt",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence effect\" (explanation OR causal OR \"alternative account\" OR \"source credibility\" OR \"correction format\") misinformation experiment",
   "language": "en",
   "database": "OpenAlex"
  }
 ],
 "how_to_check": [
  "Período e tipo de publicação: usar os metadados do OpenAlex/Crossref (publication_year 2018–2025; type = journal-article; tipo de fonte = journal). Rejeitar itens marcados como preprint, posted-content, proceedings-article, book-chapter ou dissertation. Conferir no site do periódico o ano da versão final.",
  "Revisado por pares e empírico: confirmar no site do periódico que é artigo de pesquisa original. Ler o resumo e a seção de métodos procurando 'Experiment', 'participants', 'N =' e dados próprios. Descartar 'review', 'meta-analysis', 'commentary', 'theoretical' e 'registered report' só com protocolo e sem dados.",
  "Tema CIE: o resumo ou as palavras-chave devem citar continued influence, correção/retratação de informação falsa e uso posterior dessa informação. Descartar estudos que medem só exposição ou compartilhamento, sem medir crença ou raciocínio depois da correção.",
  "Método e desfecho: conferir no resumo ou nos métodos que houve manipulação experimental (p. ex., com e sem correção) e medida de crença ou raciocínio (perguntas de inferência, avaliação de crença, referências à informação falsa) depois da correção.",
  "Materiais neutros: ler o resumo e os métodos para ver os estímulos (relatos fictícios, cenários inventados, alegações triviais). Excluir qualquer estudo cujo estímulo principal seja político, eleitoral, de vacinas ou de COVID-19. Se os materiais forem mistos (neutros e políticos), excluir ou sinalizar e explicar.",
  "Amostra: copiar o 'N =' exatamente como está no resumo. Se o resumo não trouxer o tamanho da amostra, escrever 'não informado no resumo' e não buscar no corpo do texto nem estimar.",
  "Trecho literal: copiar do resumo, entre aspas, a frase que sustenta o achado principal. Conferir caractere por caractere no resumo da página do editor ou do Crossref. Não parafrasear nem juntar frases separadas.",
  "DOI e metadados: resolver cada DOI em doi.org ou no Crossref e conferir que título, autores, ano e periódico batem. Eliminar duplicatas por DOI e por título, inclusive versão preprint e versão publicada do mesmo trabalho (manter só a do periódico).",
  "Contagem final: parar quando houver 25 artigos verificados. Se a busca esgotar os candidatos elegíveis antes disso, informar o número exato encontrado e quais critérios eliminaram mais candidatos. Não completar a lista com itens que não se qualificam."
 ]
}