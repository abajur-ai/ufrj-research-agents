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
  "Tema: efeito de influência continuada da informação falsa (continued influence effect, CIE; continued influence of misinformation): uso persistente de informação falsa no raciocínio/inferências/crença após correção ou retratação.",
  "Período: publicados entre 2018 e 2025 (inclusive), conferindo o ano de publicação do periódico (versão do registro), não o ano de preprint ou de publicação online antecipada, se divergirem; registrar o ano usado.",
  "Tipo de publicação: artigo de periódico revisado por pares que relate estudo empírico com dados próprios.",
  "Exclusões de tipo: revisões de literatura, meta-análises, ensaios teóricos/comentários, preprints (OSF, PsyArXiv, SSRN, arXiv), trabalhos de anais de congresso, capítulos de livro, teses/dissertações e resenhas.",
  "Método: experimento com participantes humanos que meça crença ou raciocínio (ex.: perguntas de inferência, referências à informação falsa, avaliações de crença) depois de uma correção ou retratação; estudos sem manipulação/comparação de correção não entram.",
  "Materiais neutros: cenários fictícios, relatos de eventos inventados (ex.: incêndio em depósito, relatos de notícias fictícias) ou alegações sem conotação política ou de saúde.",
  "Exclusões temáticas: desinformação política, eleitoral, sobre vacinas, sobre COVID-19 e outros materiais de saúde; excluir estudos cujos estímulos principais sejam desse tipo, mesmo que haja também condição neutra, a menos que os experimentos neutros sejam separáveis e o resumo deixe isso claro (caso duvidoso: sinalizar e não incluir sem confirmação).",
  "Meta de entrega: 25 artigos distintos que cumpram todos os critérios; se a busca não alcançar 25 verificáveis, entregar menos e declarar o déficit, sem completar com itens duvidosos.",
  "Campos exigidos por artigo: DOI; título; autores; ano; periódico; tipo de estudo e método; tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'); achado principal em uma frase; trecho literal do resumo entre aspas que sustente o achado.",
  "Sem restrição de idioma do artigo declarada; consultas em inglês e português, mas o corpus esperado é majoritariamente em inglês."
 ],
 "queries": [
  {
   "query": "TITLE-ABSTRACT: (\"continued influence effect\" OR \"continued influence of misinformation\" OR \"continued influence of misinformation\" OR \"continued reliance on misinformation\") AND (retraction OR correction); filtros: type=article, publication_year 2018-2025, source type=journal",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence effect\" retraction misinformation experiment inference reasoning fictional event",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "\"continued influence\" (\"misinformation\" OR \"retraction\" OR \"correction\") (\"warehouse fire\" OR \"fictional\" OR \"event report\") experiment belief inference",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "(\"continued influence effect\" OR \"belief perseverance\" OR \"misinformation correction\") AND (\"retraction\" OR \"corrections\") AND (\"mental model\" OR \"memory updating\" OR \"source credibility\" OR \"explanation\") experiment, 2018-2025",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "\"continued influence effect\" OR \"continued influence of misinformation\" journal article 2018..2025 psychology experiment retraction",
   "language": "en",
   "database": "Busca na web (Google Scholar, APA PsycNet, Semantic Scholar; para localizar candidatos e fechar lacunas, com verificação posterior do DOI no Crossref)"
  },
  {
   "query": "\"efeito de influência continuada\" OR \"influência continuada da desinformação\" OR \"informação falsa\" retratação correção experimento crença raciocínio",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "\"efeito de influência continuada\" OR \"continued influence effect\" desinformação correção retratação experimento participantes",
   "language": "pt",
   "database": "Busca na web (Google Acadêmico, Portal de Periódicos CAPES, Redalyc)"
  },
  {
   "query": "Busca por citação (snowballing): artigos que citam ou são citados por Johnson & Seifert (1994), Ecker et al. (2010, 2011), Lewandowsky et al. (2012), Walter & Tukachinsky (2020), Ecker et al. (2022 Nature Reviews Psychology) — usar o campo 'cited_by' / 'referenced_works' filtrando 2018-2025 e type=article",
   "language": "en",
   "database": "OpenAlex"
  }
 ],
 "how_to_check": [
  "Tema (CIE): ler título e resumo; exigir que o estudo meça explicitamente o uso residual da informação falsa após correção/retratação (ex.: inferências, referências à informação falsa, crença). Rejeitar se o foco for outro (ex.: apenas prevenção/prebunking sem condição de correção, ou apenas compartilhamento).",
  "Período: conferir o ano no registro do Crossref (published-print/published-online) e no OpenAlex (publication_year); aceitar apenas 2018-2025 e registrar qual data foi usada; se divergirem entre 2017/2018 ou 2025/2026, abrir a página do periódico para decidir.",
  "Tipo de publicação: no Crossref/OpenAlex, exigir type = journal-article e fonte do tipo periódico; descartar preprints (prefixos 10.31234, 10.31219, 10.48550, 10.2139 etc.), anais, capítulos e livros; conferir no resumo/texto que há 'Experiment', 'participants' e dados próprios, e que não é 'review', 'meta-analysis', 'commentary' ou 'theoretical'; confirmar revisão por pares na página do periódico quando houver dúvida.",
  "Método experimental com humanos: conferir no resumo (ou, se faltar, na seção de método via página do periódico) que há participantes humanos, manipulação de correção/retratação e medida de crença/raciocínio; descartar simulações computacionais ou modelagem sem participantes.",
  "Materiais neutros: verificar no resumo/método o tipo de estímulo (cenário fictício, evento inventado, alegações triviais); rejeitar se o estímulo principal for político, eleitoral, vacinas, COVID-19 ou saúde; marcar como 'duvidoso' quando o resumo não permitir decidir e só incluir após abrir o texto completo ou a página do artigo.",
  "DOI: validar cada DOI consultando a API do Crossref (api.crossref.org/works/{doi}) e confirmar que título, autores, ano e periódico batem com o que será informado; descartar candidatos cujo DOI não resolva.",
  "Amostra: copiar o N exatamente como aparece no resumo (ex.: 'N = 200'); se o resumo não trouxer o número, escrever 'não informado no resumo', sem buscar no corpo do texto nem estimar.",
  "Trecho literal: copiar do resumo (via Crossref, OpenAlex — reconstruindo o abstract_inverted_index com cuidado — ou página do periódico) um trecho entre aspas que sustente o achado; conferir caractere a caractere contra a fonte; se o resumo não estiver disponível, não incluir o artigo ou sinalizar a lacuna.",
  "Achado principal: redigir em uma frase apenas com base no que o resumo afirma, sem extrapolar além do texto citado.",
  "Duplicatas e contagem: deduplicar por DOI normalizado e por título (versão de periódico versus preprint, erratas e correções: manter só o artigo original); contar até 25 itens verificados e, se faltar, relatar quantos foram encontrados e por que os demais foram excluídos.",
  "Registro de triagem: manter uma tabela de candidatos com status (incluído / excluído + motivo / duvidoso) para cada critério, para que o verificador possa auditar."
 ]
}