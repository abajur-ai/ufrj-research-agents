# Verificador dos termos de busca
Você é um verificador independente. Confira se as consultas e os critérios propostos cobrem o tema do pedido, em
inglês e em português, se o período extraído é exatamente o do pedido e se os critérios de inclusão e exclusão
traduzem o pedido sem acrescentar nem esquecer restrição. Não precisa buscar na web.

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

TERMOS E CRITÉRIOS A VERIFICAR:
{
 "year_from": 2018,
 "year_to": 2025,
 "queries_en": [
  "media literacy Brazilian students misinformation",
  "disinformation media education Brazil schools",
  "information literacy fake news Brazil university",
  "fake news teachers Brazil high school",
  "critical media literacy Brazilian classroom intervention",
  "misinformation textbooks Brazil analysis",
  "digital literacy Brazilian undergraduate students fake news",
  "Brazil teacher training media and information literacy",
  "news literacy Brazilian adolescents school",
  "fact-checking education Brazil students"
 ],
 "queries_pt": [
  "desinformação educação midiática escola",
  "competência em informação fake news estudantes",
  "educação midiática professores ensino básico",
  "desinformação ensino superior alfabetização midiática",
  "fake news sala de aula intervenção pedagógica",
  "letramento midiático informacional estudantes brasileiros"
 ],
 "include": [
  "Artigo de periódico revisado por pares publicado entre 2018 e 2025",
  "Estudo empírico com dados próprios (questionário, entrevista, grupo focal, intervenção, experimento, relato de experiência com coleta de dados, análise documental de currículos ou livros didáticos)",
  "Realizado no Brasil, ou estudo comparativo internacional que inclua amostra brasileira explícita",
  "Participantes ou objeto de análise: estudantes, professores, aulas, currículos ou livros didáticos da educação básica ou do ensino superior",
  "Tema central: desinformação/fake news e educação midiática, alfabetização/letramento midiático ou competência em informação",
  "Contexto de ensino formal (escolas, institutos federais, universidades)"
 ],
 "exclude": [
  "Revisões de literatura, revisões sistemáticas, meta-análises",
  "Ensaios teóricos, artigos de opinião sem dados empíricos próprios",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, livros, teses, dissertações, resenhas",
  "Estudos centrados em COVID-19, pandemia, vacinas ou saúde",
  "Estudos centrados em eleições, política partidária ou polarização política",
  "Públicos fora do ensino formal (população geral, idosos, jornalistas, redes sociais sem vínculo escolar)",
  "Estudos sem amostra brasileira ou realizados em outros países",
  "Publicações fora do período 2018–2025",
  "Estudos sobre desinformação sem componente educacional ou de ensino"
 ]
}