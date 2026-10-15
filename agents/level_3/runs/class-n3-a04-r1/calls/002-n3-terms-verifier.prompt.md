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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre jogos educativos e jogos de inoculação (prebunking) contra desinformação, como o Bad News. Restrições: apenas intervenções em forma de jogo (digital ou de tabuleiro) avaliadas com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção; exclua intervenções que não são jogos (vídeos, textos ou infográficos isolados), reanálises de dados de outros estudos e estudos centrados em COVID-19, vacinas, eleições ou política partidária (por exemplo, o Go Viral!). Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

TERMOS E CRITÉRIOS A VERIFICAR:
{
 "year_from": 2018,
 "year_to": 2025,
 "queries_en": [
  "Bad News game misinformation inoculation",
  "prebunking game misinformation experiment",
  "fake news game psychological inoculation",
  "educational game misinformation resilience",
  "serious game fake news detection",
  "board game disinformation media literacy",
  "gamified intervention misinformation susceptibility",
  "inoculation game manipulation techniques",
  "game-based learning fake news pre-post",
  "online game improves misinformation discernment"
 ],
 "queries_pt": [
  "jogo educativo desinformação",
  "jogo inoculação fake news",
  "jogo sério notícias falsas",
  "gamificação alfabetização midiática desinformação",
  "jogo de tabuleiro desinformação educação",
  "prebunking jogo desinformação"
 ],
 "include": [
  "Artigo de periódico revisado por pares com estudo empírico e dados próprios",
  "Publicado entre 2018 e 2025",
  "A intervenção é um jogo (digital, online ou de tabuleiro) voltado a desinformação, fake news, manipulação ou inoculação/prebunking (ex.: Bad News, Harmony Square, Cranky Uncle, Fake It to Make It, Factitious, Escape room educativo sobre desinformação)",
  "Avaliação com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção",
  "Desfechos relacionados à identificação de desinformação, resistência/imunidade, confiança, discernimento da verdade ou habilidades de checagem",
  "Tamanho da amostra identificável no resumo, ou registrar como não informado no resumo",
  "Resumo disponível com trecho que sustente o achado principal"
 ],
 "exclude": [
  "Intervenções que não são jogos (vídeos, textos, infográficos, anúncios, dicas ou cursos isolados)",
  "Reanálises de dados de outros estudos ou análises secundárias",
  "Estudos centrados em COVID-19, vacinas, eleições ou política partidária (ex.: Go Viral!)",
  "Revisões de literatura, revisões sistemáticas e meta-análises",
  "Ensaios teóricos, conceituais ou de opinião, propostas de design de jogo sem avaliação com participantes",
  "Preprints",
  "Trabalhos de anais de congresso",
  "Capítulos de livro, livros, teses e dissertações",
  "Resenhas e editoriais",
  "Publicações fora do período 2018 a 2025",
  "Estudos sobre jogos sem relação com desinformação (ex.: jogos educativos de outros conteúdos)"
 ]
}