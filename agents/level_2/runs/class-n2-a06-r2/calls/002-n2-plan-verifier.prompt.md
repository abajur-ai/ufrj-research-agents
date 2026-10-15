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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre os efeitos de manchetes caça-cliques (clickbait) sobre leitores e usuários de notícias. Restrições: apenas estudos empíricos com dados de leitores ou usuários (experimentos, questionários, medidas fisiológicas como EEG ou rastreamento ocular, ou dados de cliques e engajamento); exclua modelos computacionais de detecção ou classificação de clickbait, análises apenas linguísticas de manchetes sem dados de leitores e estudos com recorte político ou eleitoral. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO A VERIFICAR:
{
 "criteria": [
  "Tema: efeitos de manchetes caça-cliques (clickbait) sobre leitores/usuários de notícias (atenção, cliques, intenção de clicar, compartilhamento, credibilidade percebida, emoção, curiosidade, compreensão, memória, confiança na mídia, engajamento).",
  "Período: publicado entre 2018-01-01 e 2025-12-31 (conferir o ano de publicação oficial do periódico, não só o online-first).",
  "Tipo de publicação: artigo de periódico revisado por pares. Excluir preprints (arXiv, SSRN, OSF, ResearchGate), anais de congresso, capítulos de livro, teses/dissertações e resenhas.",
  "Tipo de estudo: empírico, com dados próprios coletados de leitores ou usuários (experimento, survey/questionário, entrevistas, EEG/fMRI/eye tracking/outras medidas fisiológicas, ou dados reais de cliques e engajamento, como testes A/B e logs de plataforma).",
  "Excluir revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos e comentários.",
  "Excluir modelos computacionais de detecção/classificação de clickbait (machine learning, NLP) e estudos que só analisam a linguagem das manchetes sem dados de leitores.",
  "Excluir estudos com recorte político ou eleitoral (campanhas, eleições, polarização partidária, desinformação política como foco central).",
  "Contexto: notícias e jornalismo (portais, mídias sociais com notícias). Sem restrição geográfica ou de idioma, desde que o periódico seja revisado por pares.",
  "Meta: 25 artigos que cumpram todos os critérios acima. Se a busca render menos de 25 elegíveis, relatar o número real e não completar a lista com itens que violem critérios.",
  "Campos exigidos por artigo: DOI; título; autores; ano; periódico; tipo de estudo e método; tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'); achado principal em uma frase; trecho literal do resumo entre aspas que sustente o achado."
 ],
 "queries": [
  {
   "query": "(clickbait OR \"click-bait\") AND (headline* OR news) AND (experiment OR survey OR \"eye tracking\" OR EEG OR \"user study\" OR \"click-through\")",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "clickbait headlines effects on readers experiment credibility curiosity sharing intention news",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "clickbait news headlines eye-tracking OR EEG OR neurophysiological OR \"event-related potentials\" readers attention",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "clickbait headline news A/B test engagement click-through rate audience behavior field data",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "clickbait news headlines survey users perception trust news media \"curiosity gap\"",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "clickbait manchetes notícias leitores efeitos experimento OR questionário OR \"rastreamento ocular\" OR engajamento",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "caça-cliques OR \"caça-clique\" OR clickbait jornalismo recepção leitores cliques credibilidad",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "clickbait headlines effects readers peer-reviewed journal experiment 2018..2025 -detection -classification",
   "language": "en",
   "database": "busca na web (Google Scholar, ScienceDirect, SAGE, Taylor & Francis, Wiley, Springer)"
  }
 ],
 "how_to_check": [
  "Período (2018–2025): ler o ano de publicação nos metadados do Crossref/OpenAlex (publication_year e issued date) e confirmar na página do periódico; descartar 2017 ou anterior e 2026 em diante. Em caso de divergência entre online-first e edição, registrar o ano oficial da edição e anotar a divergência.",
  "Revisado por pares e tipo de publicação: confirmar que o tipo é 'journal-article' no Crossref e que a fonte é um periódico (OpenAlex source type = journal). Descartar proceedings, book-chapter, posted-content/preprint, dissertation e review. Checar a página do periódico se houver dúvida.",
  "Estudo empírico com dados próprios de leitores/usuários: ler o resumo (e os métodos, se necessário) e confirmar a presença de participantes ou usuários, ou de logs reais, com método explícito (experimento, survey, EEG, eye tracking, teste A/B, dados de cliques). Descartar se o resumo indicar revisão, meta-análise, ensaio, ou apenas análise de conteúdo das manchetes.",
  "Exclusão de modelos computacionais: descartar se o objetivo central for detectar ou classificar clickbait com algoritmo, mesmo que use rótulos de anotadores. Manter apenas se o estudo medir efeitos em leitores.",
  "Exclusão do recorte político/eleitoral: verificar título, resumo e palavras-chave para eleição, candidato, partido, campanha ou polarização política como foco; descartar se for o enquadramento central.",
  "Tema (efeitos sobre leitores): confirmar que clickbait é variável central (manipulada ou medida) e que há um desfecho do lado do leitor (clique, atenção, credibilidade, emoção, compartilhamento, confiança etc.).",
  "Tamanho da amostra: copiar literalmente do resumo (ex.: 'N = 312', '1.200 participantes'); se o resumo não trouxer, escrever 'não informado no resumo'. Não puxar o N do corpo do texto.",
  "Trecho literal: copiar do resumo oficial, entre aspas, sem parafrasear. Conferir caractere a caractere com o resumo da página do periódico ou do Crossref. O trecho deve sustentar o achado principal.",
  "DOI e metadados: resolver cada DOI (doi.org) e comparar título, autores, periódico e ano com o registro do Crossref. Descartar duplicatas, incluindo a mesma pesquisa em versões diferentes.",
  "Contagem: manter uma tabela de candidatos com o status de cada critério (aprovado/reprovado/dúvida). Parar em 25 aprovados em todos os critérios; se não chegar a 25, informar o número real e os critérios que mais eliminaram candidatos."
 ]
}