PEDIDO DO PESQUISADOR:
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre o efeito de influência continuada da informação falsa (continued influence effect), isto é, o quanto as pessoas continuam a se apoiar em uma informação falsa depois de ela ser corrigida ou retratada. Restrições: apenas experimentos com participantes humanos que meçam crença ou raciocínio depois de uma correção ou retratação; os materiais devem ser neutros (cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde); exclua estudos com desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO APROVADO:
{
 "criteria": [
  "Tema: efeito de influência continuada da informação falsa (continued influence effect, CIE) — uso persistente de informação falsa no raciocínio/crença após correção ou retratação.",
  "Período: publicados entre 2018 e 2025 (ano de publicação do periódico, de 01/01/2018 a 31/12/2025).",
  "Tipo de publicação: artigo de periódico revisado por pares; excluir preprints, anais de congresso, capítulos de livro, teses/dissertações e resenhas.",
  "Tipo de estudo: estudo empírico com dados próprios; excluir revisões de literatura, meta-análises, ensaios teóricos e comentários.",
  "Método: experimento com participantes humanos que meça crença ou raciocínio (ex.: inferências, referências à informação falsa, avaliação de crença) após uma correção ou retratação.",
  "Materiais neutros: cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde.",
  "Exclusões temáticas: desinformação política, eleitoral, sobre vacinas ou sobre COVID-19 (e, por extensão da restrição de materiais neutros, outros materiais de saúde ou políticos).",
  "Meta de quantidade: 25 artigos distintos que atendam a todos os critérios (se a busca não alcançar 25, relatar o número real encontrado, sem completar com artigos que violem critérios).",
  "Campos a extrair por artigo: DOI; título; autores; ano; periódico; tipo de estudo e método; tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'); achado principal em uma frase; trecho literal do resumo, entre aspas, que sustente o achado."
 ],
 "queries": [
  {
   "query": "\"continued influence effect\" AND (retraction OR correction OR misinformation) AND experiment",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence\" (misinformation OR retraction) fictional event report inferential reasoning",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence effect\"",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "retraction misinformation \"continued influence\" reliance inference refutation explanation",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "\"efeito de influência continuada\" OR \"influência continuada\" informação falsa correção retratação",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "\"continued influence effect\" misinformation correction experimento",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "\"continued influence effect\" journal article experiment fictional scenario retraction 2018..2025 (Memory & Cognition OR Journal of Experimental Psychology OR Applied Cognitive Psychology OR Journal of Applied Research in Memory and Cognition)",
   "language": "en",
   "database": "Busca na web"
  },
  {
   "query": "efeito de influência continuada desinformação retratação experimento artigo periódico",
   "language": "pt",
   "database": "Busca na web"
  }
 ],
 "how_to_check": [
  "Tema (CIE): ler título e resumo de cada candidato; manter só se o estudo mede dependência/influência persistente da informação falsa após correção ou retratação (termos como continued influence, retraction, correction, reliance on misinformation).",
  "Período: conferir o ano de publicação nos metadados do OpenAlex/Crossref (publication_year / issued) e na página do periódico; descartar fora de 2018–2025 (atenção a divergência entre data online e data da edição).",
  "Revisado por pares e periódico: confirmar que o tipo no OpenAlex/Crossref é 'journal-article' e que o periódico tem revisão por pares; descartar preprints (PsyArXiv, OSF, SSRN), anais, capítulos, teses e resenhas, inclusive versões preprint de artigos já publicados (usar só o DOI do periódico).",
  "Estudo empírico com dados próprios: ler o resumo e, se preciso, a seção de métodos; descartar revisões, meta-análises, ensaios teóricos, comentários e reanálises sem dados novos.",
  "Método experimental com humanos: verificar no resumo/métodos que há participantes humanos, manipulação (correção vs. sem correção) e medida de crença ou raciocínio pós-correção; descartar simulações computacionais e modelagem sem participantes.",
  "Materiais neutros: verificar nos métodos o conteúdo dos estímulos (ex.: relato de incêndio fictício, evento inventado, alegações triviais); descartar estudos cujos materiais sejam políticos, eleitorais, de saúde, vacinas ou COVID-19; em caso de materiais mistos, excluir ou sinalizar para decisão do pesquisador.",
  "Exclusões temáticas: busca por palavras-chave no título/resumo (vaccine, COVID, election, political, health, politician, Trump, etc.) e confirmação nos métodos.",
  "Duplicatas: deduplicar por DOI normalizado e por título entre OpenAlex, Crossref, SciELO e web.",
  "DOI: copiar do registro do Crossref/OpenAlex e verificar que resolve (doi.org) para o artigo correto; não inventar nem inferir DOI.",
  "Amostra: copiar o N exatamente como escrito no resumo (ex.: 'N = 200'); se o resumo não trouxer, registrar 'não informado no resumo' sem buscar no corpo do texto.",
  "Trecho literal: copiar do resumo do registro (OpenAlex/Crossref/página do periódico) sem alteração e entre aspas, confirmando que sustenta o achado principal; se o resumo estiver indisponível, sinalizar em vez de parafrasear.",
  "Contagem final: se após as 8 consultas e o encadeamento de citações (referências e citantes dos artigos-núcleo, como Ecker et al. e Lewandowsky et al.) houver menos de 25 artigos válidos, reportar o número real e quais critérios limitaram o resultado."
 ]
}





Entregue os candidatos.