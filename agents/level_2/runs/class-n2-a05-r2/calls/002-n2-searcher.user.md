PEDIDO DO PESQUISADOR:
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2019 e 2025, sobre como as pessoas percebem, detectam ou avaliam a credibilidade de imagens, vídeos e áudios sintéticos gerados por inteligência artificial (deepfakes, rostos sintéticos e clones de voz). Restrições: apenas estudos empíricos com participantes humanos (experimentos, testes de detecção, surveys ou medidas fisiológicas); exclua artigos sobre algoritmos de detecção automática, estudos centrados em políticos, eleições ou propaganda política e estudos sobre saúde. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

PLANO APROVADO:
{
 "criteria": [
  "Tema: percepção, detecção ou avaliação de credibilidade (confiabilidade, autenticidade, realismo) de mídia sintética gerada por IA: deepfakes em vídeo, imagens/rostos sintéticos (ex.: GAN, StyleGAN, difusão) e áudio/clones de voz.",
  "Período: publicado entre 2019 e 2025 (inclusive). Conferir o ano da versão final publicada no periódico, não o do preprint.",
  "Tipo de publicação: artigo de periódico revisado por pares. Excluir preprints (arXiv, SSRN, OSF, PsyArXiv), anais de congresso, capítulos de livro, teses e dissertações, resenhas.",
  "Tipo de estudo: estudo empírico com dados primários próprios. Excluir revisões de literatura (sistemáticas ou narrativas), meta-análises, ensaios teóricos e comentários.",
  "Método: estudo com participantes humanos, isto é, experimento, teste de detecção/discriminação, survey ou medida fisiológica (eye-tracking, EEG, condutância da pele, frequência cardíaca etc.).",
  "Exclusão: artigos cujo foco é algoritmo de detecção automática. Admite-se comparação humano vs. máquina somente se o núcleo for o desempenho ou a percepção humana. Em caso de dúvida, sinalizar o caso em vez de incluí-lo em silêncio.",
  "Exclusão: estudos centrados em políticos, eleições ou propaganda política (ex.: deepfake de candidato, desinformação eleitoral).",
  "Exclusão: estudos sobre saúde (desinformação em saúde, vídeos médicos, saúde mental ou pública). Verificar também o contexto do estímulo e da amostra.",
  "Meta: 25 artigos distintos e elegíveis. Se a busca render menos de 25, informar o déficit em vez de completar com itens que não atendam aos critérios.",
  "Dados exigidos por artigo: DOI; título; autores; ano; periódico; tipo de estudo e método; tamanho da amostra exatamente como no resumo (ou 'não informado no resumo'); achado principal em uma frase; trecho literal do resumo, entre aspas, que sustente o achado."
 ],
 "queries": [
  {
   "query": "(deepfake OR \"synthetic media\" OR \"AI-generated\" OR \"synthetic faces\") AND (detection OR perception OR credibility OR trust OR \"human judgment\") AND (experiment OR participants OR survey)",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "humans ability to detect AI-generated faces StyleGAN GAN-generated faces trustworthiness realism participants experiment",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "voice clone OR \"audio deepfake\" OR \"synthetic speech\" human detection OR perception OR listeners participants",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "deepfake video credibility perceived authenticity eye-tracking OR EEG OR \"skin conductance\" OR physiological",
   "language": "en",
   "database": "OpenAlex"
  },
  {
   "query": "deepfake detection by humans experiment participants accuracy confidence",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "synthetic faces perception trust \"AI-generated\" images people cannot distinguish journal article",
   "language": "en",
   "database": "Crossref"
  },
  {
   "query": "deepfakes percepção credibilidade detecção participantes experimento OR survey OR questionário",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "vídeos sintéticos OR \"imagens geradas por inteligência artificial\" OR \"clonagem de voz\" credibilidade percepção usuários estudo empírico",
   "language": "pt",
   "database": "SciELO"
  },
  {
   "query": "deepfake perception study participants peer-reviewed journal \"we conducted\" experiment detect fake video audio image 2019..2025",
   "language": "en",
   "database": "busca na web"
  }
 ],
 "how_to_check": [
  "Tema: ler título e resumo. Incluir só se o objeto for a percepção, detecção ou avaliação de credibilidade de deepfakes, rostos sintéticos ou áudio/voz sintéticos por pessoas.",
  "Período: conferir o ano de publicação no registro do Crossref ou OpenAlex (publication_year e issued date). Descartar o que ficar fora de 2019–2025 e verificar casos de 'online first' em 2018 ou 2026.",
  "Tipo de publicação: conferir no Crossref se type = journal-article e se há periódico (container-title). Rejeitar preprints, anais (proceedings-article), capítulos, teses e resenhas. Verificar na página do periódico se o texto é revisado por pares e se a seção não é editorial ou comentário.",
  "Estudo empírico com dados próprios: o resumo deve descrever coleta (participantes, N, tarefa, medidas). Descartar o que se declarar revisão, meta-análise, scoping review, ensaio, framework teórico ou análise só de dados secundários.",
  "Participantes humanos e método: identificar no resumo ou nos métodos se há experimento, tarefa de detecção, survey ou medida fisiológica, e registrar o método. Rejeitar estudos só computacionais.",
  "Exclusão de algoritmos: descartar se a contribuição principal for um modelo ou detector automático. Manter comparações humano vs. máquina só se o desempenho humano for central, e anotar a decisão.",
  "Exclusão política e eleitoral: procurar no título, no resumo e nas palavras-chave termos como election, politician, political, propaganda, campaign, candidate, partisan. Descartar se o estímulo ou o enquadramento principal for político.",
  "Exclusão de saúde: procurar health, medical, COVID, vaccine, patient, mental health, clinical. Descartar se o tema ou o contexto do estímulo for de saúde.",
  "DOI: confirmar a existência e a resolução do DOI no Crossref (api.crossref.org/works/DOI), comparando título, autores, ano e periódico com o OpenAlex. Não inferir nem inventar DOIs.",
  "Tamanho da amostra: copiar do resumo, do OpenAlex ou do Crossref, exatamente como escrito (ex.: 'N = 1.276'). Se o resumo não trouxer o número, escrever 'não informado no resumo' e não consultar o texto completo para preencher.",
  "Trecho literal: copiar do resumo, entre aspas, sem parafrasear, e conferir caractere a caractere que a frase sustenta o achado principal. O achado de uma frase deve decorrer do trecho.",
  "Deduplicação e contagem: remover duplicatas por DOI e por título normalizado (versão preprint versus versão publicada, mantendo só a publicada). Parar em 25 elegíveis ou relatar o déficit com os motivos de exclusão."
 ]
}





Entregue os candidatos.