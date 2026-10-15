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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2019 e 2025, sobre como as pessoas percebem, detectam ou avaliam a credibilidade de imagens, vídeos e áudios sintéticos gerados por inteligência artificial (deepfakes, rostos sintéticos e clones de voz). Restrições: apenas estudos empíricos com participantes humanos (experimentos, testes de detecção, surveys ou medidas fisiológicas); exclua artigos sobre algoritmos de detecção automática, estudos centrados em políticos, eleições ou propaganda política e estudos sobre saúde. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

TERMOS E CRITÉRIOS A VERIFICAR:
{
 "year_from": 2019,
 "year_to": 2025,
 "queries_en": [
  "deepfake detection human participants experiment",
  "human ability to detect deepfake videos",
  "perceived credibility of deepfake videos",
  "synthetic faces trustworthiness human perception",
  "AI-generated faces indistinguishable from real faces",
  "voice clone detection listeners",
  "audio deepfake human perception detection",
  "deepfake susceptibility survey experiment",
  "people identify AI-generated images accuracy",
  "physiological responses to deepfakes"
 ],
 "queries_pt": [
  "detecção de deepfakes por humanos",
  "credibilidade de vídeos deepfake percepção",
  "percepção de rostos sintéticos gerados por IA",
  "clonagem de voz inteligência artificial percepção",
  "experimento deepfake participantes",
  "imagens geradas por inteligência artificial credibilidade"
 ],
 "include": [
  "Artigo de periódico revisado por pares publicado entre 2019 e 2025",
  "Estudo empírico com dados próprios coletados de participantes humanos (experimento, teste de detecção, survey, medidas fisiológicas como eye-tracking, EEG, condutância da pele)",
  "Tema: percepção, detecção ou avaliação de credibilidade/confiabilidade/autenticidade de imagens, vídeos ou áudios sintéticos gerados por IA (deepfakes, rostos sintéticos, clones de voz)",
  "Resumo permite identificar método e, se possível, tamanho da amostra",
  "Inclui estudos de detecção humana, confiança em mídia sintética, efeito de alertas ou treinamento sobre a capacidade humana de detectar"
 ],
 "exclude": [
  "Artigos sobre algoritmos ou modelos de detecção automática de deepfakes (machine learning, deep learning, benchmarks)",
  "Estudos centrados em políticos, eleições, campanhas ou propaganda política",
  "Estudos sobre saúde ou contexto médico",
  "Revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos ou conceituais, resenhas",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, teses e dissertações",
  "Estudos sem participantes humanos ou sem dados empíricos próprios (ex.: análise apenas de conteúdo, análise jurídica, proposta técnica)",
  "Publicações fora do período 2019 a 2025"
 ]
}