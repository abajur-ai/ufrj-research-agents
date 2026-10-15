PEDIDO DO PESQUISADOR:
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre os efeitos de manchetes caça-cliques (clickbait) sobre leitores e usuários de notícias. Restrições: apenas estudos empíricos com dados de leitores ou usuários (experimentos, questionários, medidas fisiológicas como EEG ou rastreamento ocular, ou dados de cliques e engajamento); exclua modelos computacionais de detecção ou classificação de clickbait, análises apenas linguísticas de manchetes sem dados de leitores e estudos com recorte político ou eleitoral. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO APROVADO:
{
 "criteria": [
  "Tema: efeitos de manchetes caça-cliques (clickbait) sobre leitores/usuários de notícias (atenção, cliques, engajamento, credibilidade, emoção, intenção de compartilhar, memória/compreensão, confiança, lacuna de curiosidade, etc.).",
  "Período: publicado entre 01/01/2018 e 31/12/2025 (conferir ano da versão publicada/final, não apenas o online-first ou preprint).",
  "Tipo de publicação: artigo de periódico revisado por pares; excluir preprints, anais de congresso, capítulos de livro, teses/dissertações, resenhas e editoriais.",
  "Tipo de estudo: estudo empírico com dados próprios (primários) de leitores ou usuários; excluir revisões de literatura, meta-análises, ensaios teóricos e reanálises sem coleta própria.",
  "Método/dados admitidos: experimentos (laboratório, survey experiment, online), questionários/surveys, medidas fisiológicas ou neurais (EEG, eye-tracking, GSR, etc.), ou dados de cliques/engajamento de usuários reais (inclusive testes A/B e dados de plataforma).",
  "Exclusão: modelos computacionais de detecção/classificação de clickbait (machine learning, NLP) sem foco em efeitos sobre leitores.",
  "Exclusão: análises apenas linguísticas/de conteúdo de manchetes sem dados de leitores ou usuários.",
  "Exclusão: estudos com recorte político ou eleitoral (campanhas, eleições, polarização partidária, desinformação política como foco central).",
  "Contexto: notícias/jornalismo (incluindo mídia social e agregadores de notícias); sem restrição geográfica ou de idioma do artigo, desde que o resumo permita verificação.",
  "Quantidade: 25 artigos distintos; cada um com DOI, título, autores, ano, periódico, tipo de estudo/método, tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'), achado principal em uma frase e trecho literal do resumo entre aspas."
 ],
 "queries": [
  {
   "query": "(clickbait OR \"click-bait\" OR \"curiosity gap\") AND (headline* OR news) AND (experiment OR survey OR \"eye tracking\" OR EEG OR \"user engagement\" OR \"click-through\")",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "title_and_abstract.search:(clickbait headline) AND type:article AND publication_year:2018-2025 AND primary_location.source.type:journal (filtrar depois por experiment/survey/participants/eye-tracking)",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "clickbait headlines effects on readers credibility trust sharing intention experiment participants",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "clickbait news headlines eye-tracking OR EEG OR \"neural\" OR \"physiological\" OR \"cognitive load\" reader attention",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "clickbait AND (\"A/B test\" OR \"field experiment\" OR \"click data\" OR \"audience metrics\" OR \"engagement data\") AND news publishers users",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "clickbait manchetes notícias leitores efeitos experimento OR questionário OR survey OR \"rastreamento ocular\" OR engajamento",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "caça-cliques OR clickbait jornalismo online credibilidade percepção leitores estudo empírico",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "clickbait headlines effect on readers journal article experiment survey 2018..2025 (sites: sciencedirect.com, tandfonline.com, journals.sagepub.com, link.springer.com, wiley.com) – busca de complemento e de lacunas, também em Google Scholar",
   "language": "en",
   "database": "busca na web"
  }
 ],
 "how_to_check": [
  "Tema: ler título e resumo; manter só se clickbait/manchete caça-cliques for variável central (manipulada, medida ou analisada) e o desfecho for sobre leitores/usuários.",
  "Período: conferir o ano de publicação no registro do Crossref/OpenAlex (published-print/issued) e na página do periódico; rejeitar fora de 2018–2025.",
  "Tipo de publicação: verificar no Crossref/OpenAlex type = journal-article e o ISSN/periódico; rejeitar preprints (SSRN, arXiv, OSF, ResearchGate), anais (proceedings, ACM/IEEE conference), capítulos e teses; confirmar revisão por pares no site do periódico.",
  "Estudo empírico com dados próprios: o resumo deve descrever coleta (participantes, amostra, experimento, survey, dados de plataforma); rejeitar se o resumo indicar revisão sistemática, meta-análise, ensaio ou reanálise de dados alheios sem coleta própria.",
  "Método: classificar cada candidato como experimento, survey, fisiológico/neural (EEG, eye-tracking), dados de cliques/engajamento, ou misto; registrar o método conforme o resumo.",
  "Exclusão computacional: rejeitar se a contribuição principal for um classificador/detector, mesmo com validação por humanos; aceitar apenas se houver efeito sobre leitores com dados próprios como foco.",
  "Exclusão linguística: rejeitar se o resumo só analisa texto das manchetes sem dados de leitores/usuários.",
  "Exclusão política/eleitoral: verificar título, resumo e palavras-chave por termos como election, political, partisan, campaign, voting, polarization; rejeitar se o recorte central for político.",
  "Tamanho da amostra: copiar exatamente do resumo (ex.: 'N = 240', '1.200 participantes'); se não houver número, escrever 'não informado no resumo'; não buscar no texto completo nem inferir.",
  "Achado principal e trecho literal: redigir uma frase a partir do resumo e copiar entre aspas um trecho verbatim do resumo que a sustente; comparar caractere a caractere com o resumo recuperado do Crossref/OpenAlex/página do periódico.",
  "DOI e metadados: validar DOI resolvendo em doi.org ou via API do Crossref e conferir que título, autores, ano e periódico batem; remover duplicatas (mesmo estudo em várias fontes ou versão preprint + publicada).",
  "Meta: se após triagem houver menos de 25 aprovados, ampliar com variantes (sensationalism, 'forward-referencing', 'curiosity-arousing headlines', 'headline framing'), snowballing por citações dos aprovados e busca em outros idiomas, e declarar o número real se não chegar a 25."
 ]
}





Entregue os candidatos.