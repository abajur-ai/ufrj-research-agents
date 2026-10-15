# Conferência da bibliografia do deck (método do nível 3)

Código procura cada obra (OpenAlex, DBLP, arXiv, OpenLibrary, web) e os números e frases no texto da fonte; um júri de três empresas (DeepSeek, Qwen, Google) lê os trechos achados e decide por maioria.

## Obras

| Obra | Existe | Autor | Ano | Veículo | Lido |
| --- | --- | --- | --- | --- | --- |
| anthropic_agents | sim | sim | sim | - | web: https://github.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/README.md; web: https://simonwillison.net/2024/Dec/20/building-effe |
| russell_norvig | sim | sim | NÃO | NÃO | web: https://agentplex.substack.com/p/agentplex-weekly-issue-8; web: https://classpages.cselabs.umn.edu/Fall-2017/csci8551/notes1.pdf |
| react | sim | sim | sim | NÃO | resumo (arXiv 2210.03629v3); texto completo (arXiv 2210.03629v3) |
| wang_survey | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2308.11432v7); texto completo (arXiv 2308.11432v7) |
| google_dr | sim | NÃO | NÃO | - | web: https://blog.google/products/gemini/google-gemini-deep-research/ |
| openai_dr | NÃO | NÃO | NÃO | - | web: https://en.wikipedia.org/wiki/ChatGPT_Deep_Research |
| storm | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2402.14207v2); texto completo (arXiv 2402.14207v2) |
| paperqa2 | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2409.13740v2); texto completo (arXiv 2409.13740v2) |
| kalai_2025 | sim | sim | sim | sim | resumo (Crossref 10.20944/preprints202601.1447.v1); resumo (OpenAlex); resumo (arXiv 2509.04664v1); texto completo (arXiv 2509.04664v1) |
| sharma | sim | sim | sim | NÃO | resumo (arXiv 2310.13548v4); texto completo (arXiv 2310.13548v4) |
| walters | sim | sim | sim | sim | resumo (Crossref 10.1038/s41598-023-41032-5); resumo (OpenAlex); página da editora (doi 10.1038/s41598-023-41032-5) |
| tow | sim | NÃO | sim | - | web: https://x.com/SciNewsRo/status/1900451264195973233; web: https://laurayost.substack.com/p/digital-wild-goose-chase-the-serious |
| kalai_vempala | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2311.14648v3); texto completo (arXiv 2311.14648v3) |
| pal | sim | sim | sim | NÃO | resumo (OpenAlex); resumo (arXiv 2211.10435v2); texto completo (arXiv 2211.10435v2) |
| llm_modulo | sim | sim | sim | NÃO | resumo (OpenAlex); página da editora (doi 10.48550/arxiv.2402.01817) |
| nist | NÃO | NÃO | NÃO | - | web: https://www.itl.nist.gov/div898/handbook/apr/apr_d.htm |
| dziri | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2305.18654v3); texto completo (arXiv 2305.18654v3) |
| huang | sim | sim | sim | NÃO | resumo (OpenAlex); resumo (arXiv 2310.01798v2); texto completo (arXiv 2310.01798v2) |
| lightman | sim | sim | sim | NÃO | resumo (OpenAlex); página da editora (doi 10.48550/arxiv.2305.20050) |
| stechly | sim | sim | sim | NÃO | resumo (OpenAlex); resumo (arXiv 2402.08115v2); texto completo (arXiv 2402.08115v2) |
| panickssery | sim | sim | sim | sim | resumo (arXiv 2404.13076v1); texto completo (arXiv 2404.13076v1) |
| cnpq | sim | sim | sim | - | web: https://ppgartes.unespar.edu.br/nova-portaria-do-cnpq-define-limites-para-o-uso-de-inteligencia-artificial-na-pesquisa-academica; web: https://www4.ifsc.us |
| parasuraman | sim | sim | sim | sim | resumo (Crossref 10.1177/0018720810376055); resumo (OpenAlex) |
| verga | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2404.18796v2); texto completo (arXiv 2404.18796v2) |
| fact_score | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2305.14251v2); texto completo (arXiv 2305.14251v2) |
| nosek | sim | sim | sim | sim | resumo (Crossref 10.31219/osf.io/2dxu5); resumo (OpenAlex) |
| holm | sim | sim | sim | sim | resumo (OpenAlex) |
| cameron_miller | sim | sim | sim | sim | página da editora (doi 10.3368/jhr.50.2.317) |
| zheng | sim | sim | sim | sim | resumo (OpenAlex); resumo (arXiv 2306.05685v4); texto completo (arXiv 2306.05685v4) |
| wu_hitl | sim | sim | sim | sim | resumo (arXiv 2108.00941v3); texto completo (arXiv 2108.00941v3) |
| jergas | sim | sim | sim | sim | resumo (Crossref 10.7717/peerj.1364); resumo (OpenAlex) |
| messeri | sim | sim | sim | sim | página da editora (doi 10.1038/s41586-024-07146-0) |
| nature_2023 | sim | sim | sim | - | web: https://www.nature.com/articles/d41586-023-00191-1; web: https://x.com/Nature/status/1617942047293411329 |
| unesco | sim | sim | sim | - | web: https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence; web: https://dig.watch/resource/unesco-recommendation-on-the-ethics- |
| anthropic_pricing | sim | sim | sim | - | web: https://platform.claude.com/docs/en/about-claude/pricing; web: https://benchlm.ai/anthropic/api-pricing; web: https://www.sentra.app/articles/claude-api-pr |

## Afirmações

### c01 (p. 6): **sustenta**

> Um agente recebe uma tarefa, planeja e opera de forma independente, decide os próprios passos e usa ferramentas até concluir.

Código: dynamically direct their own processes and tool usage: achado, plan and operate independently: achado

- DeepSeek V4 Pro: sustenta_em_parte. O slide afirma que o agente opera de forma independente e decide os próprios passos até concluir, mas o trecho da fonte indica que o agente pode retornar ao humano para mais informações ou julgamento, pausar para feedback e que a tarefa frequentemente termina ao ser concluída, mas também é comum incluir condições de parada. Portanto, o slide omite a interação humana e as condições de parada, exage
- Qwen3.7 Plus: sustenta. O slide parafraseia com precisão a definição de agentes apresentada no texto, cobrindo o recebimento da tarefa (comando ou discussão), o planejamento e operação independente, a direção dinâmica dos próprios processos e uso de ferramentas, e a conclusão da tarefa.
- Gemini 3.1 Flash-Lite: sustenta. A fonte descreve os agentes como entidades que recebem comandos ou discutem com humanos, planejam e operam de forma independente, direcionam dinamicamente seus processos e uso de ferramentas, e encerram a tarefa após a conclusão, o que valida integralmente a afirmação do slide.

### c02 (p. 7): **sustenta**

> Citação traduzida: "O modelo de linguagem dirige dinamicamente o próprio processo e o uso de ferramentas."

Código: dynamically direct their own processes and tool usage: achado

- DeepSeek V4 Pro: sustenta. O slide cita literalmente a definição de agentes fornecida pela fonte, com tradução fiel. A fonte afirma exatamente que os LLMs 'dynamically direct their own processes and tool usage', o que corresponde à citação traduzida.
- Qwen3.7 Plus: sustenta. O trecho da fonte contém exatamente a afirmação entre aspas ("dynamically direct their own processes and tool usage"), referindo-se aos agentes onde os LLMs (modelos de linguagem) atuam. A tradução apresentada no slide é fiel ao original em inglês.
- Gemini 3.1 Flash-Lite: sustenta. O trecho da fonte define explicitamente 'agents' como sistemas onde os LLMs 'dynamically direct their own processes and tool usage', o que corresponde exatamente à afirmação do slide.

### c03 (p. 7): **sustenta**

> Definição clássica de agente: tudo o que pode ser visto como percebendo o seu ambiente por sensores e agindo sobre ele por efetores (Russell e Norvig, 1995, p. 31).

Código: perceiving its environment through sensors and acting upon that environment through effectors: achado

- DeepSeek V4 Pro: sustenta_em_parte. Os trechos fornecem a definição exata citada no slide (tradução fiel), mas não confirmam a página 31 mencionada na referência.
- Qwen3.7 Plus: sustenta. O trecho confirma que Russell e Norvig, em 'AI: A Modern Approach', definiram agente exatamente como o slide apresenta ('anything that can be viewed as perceiving its environment through sensors and acting upon that environment through effectors'). A tradução apresentada no slide é fiel ao original em inglês citado na fonte.
- Gemini 3.1 Flash-Lite: sustenta. A definição apresentada no slide é uma tradução fiel da definição de agente atribuída a Russell e Norvig no trecho da fonte fornecido.

### c04 (p. 9): **sustenta**

> O ciclo do agente alterna raciocínio (pensar), ação (usar uma ferramenta, como busca) e observação do resultado, e repete.

Código: interleaved: achado, reasoning traces: achado, actions: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma que o modelo gera raciocínio e ações de forma intercalada, e que as ações permitem obter informações adicionais de fontes externas. Isso corresponde a alternar raciocínio, ação e observação do resultado. A repetição está implícita no caráter intercalado e na atualização de planos de ação mencionada no resumo.
- Qwen3.7 Plus: sustenta. O texto afirma que o modelo gera 'reasoning traces' (raciocínio) e 'task-specific actions' (ação) de maneira intercalada ('interleaved manner', o que implica o ciclo que se repete), e que as ações permitem interagir com fontes externas (como a API do Wikipedia, citada adiante) para 'gather additional information' (observação do resultado). Isso sustenta a afirmação do slide sobre o ciclo de racioc
- Gemini 3.1 Flash-Lite: sustenta. O texto descreve o método ReAct como a geração de 'reasoning traces' (raciocínio) e 'task-specific actions' (ações) de forma 'interleaved' (intercalada). A menção de que as ações permitem interagir com fontes externas para 'gather additional information' (obter informações adicionais) sustenta a ideia de observação do resultado, e a natureza do método (intercalado para resolver tarefas) implica a 

### c05 (p. 8): **sustenta**

> Agentes baseados em LLM têm quatro módulos: perfil, memória, planejamento e ação.

Código: profiling module: achado, memory module: achado, planning module: achado, action module: achado

- DeepSeek V4 Pro: sustenta. O trecho da fonte declara explicitamente que o framework unificado é composto por um módulo de perfil (profiling), memória (memory), planejamento (planning) e ação (action), correspondendo exatamente aos quatro módulos mencionados no slide.
- Qwen3.7 Plus: sustenta. O texto afirma explicitamente que a estrutura do framework é composta por um módulo de perfil (profiling module), um módulo de memória (memory module), um módulo de planejamento (planning module) e um módulo de ação (action module), o que corresponde exatamente à afirmação do slide.
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que o framework proposto para agentes baseados em LLM é composto por quatro módulos: profiling (perfil), memory (memória), planning (planejamento) e action (ação).

### c06 (p. 10): **sustenta**

> Deep Research do Google (dez. 2024): pesquisa em várias etapas, navega pela web, lê as páginas e devolve um relatório com as fontes.

Código: Deep Research: achado, report: achado

- DeepSeek V4 Pro: sustenta. O trecho menciona explicitamente: plano de pesquisa em várias etapas (multi-step research plan), navegação pela web (browsing the web), análise profunda das informações (lê as páginas) e geração de relatório com links para as fontes originais. Todos os elementos da afirmação do slide estão presentes.
- Qwen3.7 Plus: sustenta. Os trechos confirmam que a ferramenta cria um "plano de pesquisa em várias etapas" (multi-step research plan), "navega pela web" (browsing the web) para "analisar profundamente informações relevantes" (deeply analyzing relevant information, o que equivale a ler as páginas) e gera um "relatório abrangente" organizado com "links para as fontes originais" (comprehensive report... neatly organized wit
- Gemini 3.1 Flash-Lite: sustenta. A fonte descreve exatamente o funcionamento do Deep Research: a criação de um plano de pesquisa de várias etapas, a navegação pela web para encontrar e analisar informações, e a geração de um relatório final que inclui links para as fontes originais.

### c07 (p. 10): **sustenta**

> Deep research da OpenAI (fev. 2025): pesquisa em várias etapas na internet e devolve um relatório com as fontes.

Código: multi-step research: NÃO achado, deep research: achado, February: achado

- DeepSeek V4 Pro: sustenta. Os trechos afirmam que o Deep Research gera relatórios citados (com fontes) ao navegar autonomamente na web, e que seu framework organiza as ações em etapas (steps). Isso corresponde exatamente ao que o slide afirma: pesquisa em várias etapas na internet e devolve um relatório com as fontes. A data de lançamento (fevereiro de 2025) também é confirmada pela fonte.
- Qwen3.7 Plus: sustenta. Os trechos confirmam que o Deep Research foi introduzido em fevereiro de 2025, que ele navega na internet ("browsing the web") organizando suas operações em uma série de etapas ("organize its operations in a series of steps") e gera relatórios com citações/fontes ("generates cited reports").
- Gemini 3.1 Flash-Lite: sustenta. Os trechos confirmam que o Deep Research foi lançado pela OpenAI em fevereiro de 2025, que ele realiza pesquisas na internet de forma autônoma (organizando ações em etapas) e que gera relatórios com citações (fontes).

### c08 (p. 10): **sustenta**

> STORM escreve artigos no formato da Wikipédia a partir de perguntas feitas de várias perspectivas.

Código: perspective: achado, Wikipedia: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma que o STORM gera artigos longos comparáveis a páginas da Wikipédia e que seu processo de pré-escrita inclui simular conversas com perguntas feitas a partir de diferentes perspectivas. Isso corresponde exatamente ao que o slide afirma: escrever artigos no formato da Wikipédia a partir de perguntas de várias perspectivas.
- Qwen3.7 Plus: sustenta. O texto afirma que o STORM escreve artigos longos com 'comparable breadth and depth to Wikipedia pages' (alinhado com 'artigos no formato da Wikipédia', também refletido no título da obra como 'Wikipedia-like Articles') e que o sistema é baseado em 'Multi-perspective Question Asking', simulando conversas onde 'writers carrying different perspectives pose questions'. Isso sustenta diretamente a afi
- Gemini 3.1 Flash-Lite: sustenta. O texto descreve o STORM como um sistema que utiliza 'Multi-perspective Question Asking' (perguntas de múltiplas perspectivas) para pesquisar tópicos e criar artigos longos com profundidade e abrangência comparáveis às páginas da Wikipédia.

### c09 (p. 10): **sustenta**

> PaperQA2 busca e lê artigos científicos e responde com citações; superou doutorandos e pós-doutores em duas de três tarefas, segundo os autores (preprint).

Código: PhD: achado, postdoc: achado, superhuman: achado

- DeepSeek V4 Pro: sustenta. O trecho da fonte afirma explicitamente que o PaperQA2 supera o desempenho de doutorandos e pós‑doutores em duas das três tarefas (recuperação e sumarização), exatamente como o slide indica. Além disso, a descrição de que o sistema escreve resumos citados corrobora a primeira parte da afirmação (busca, leitura e resposta com citações).
- Qwen3.7 Plus: sustenta. O slide afirma que o sistema busca/lê artigos, responde com citações e supera doutorandos/pós-doutores em duas de três tarefas. Os trechos confirmam que o PaperQA2 realiza tarefas de busca e resumo com citações ("writes cited, Wikipedia-style summaries"), que foram avaliadas três tarefas (recuperação, sumarização e detecção de contradições) e que o sistema superou o desempenho de doutorandos e pós
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma que o PaperQA2 realiza busca e resumo com citações, e afirma explicitamente que o sistema supera doutorandos e pós-doutores nas tarefas de recuperação (retrieval) e sumarização, que compõem duas das três tarefas avaliadas (sendo a terceira a detecção de contradições).

### c10 (p. 11): **sustenta**

> Modelos aprenderam a chutar: os testes que avaliam os modelos premiam o acerto e não premiam a dúvida, então chutar rende mais pontos que dizer não sei.

Código: guessing: achado, uncertainty: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma explicitamente que os procedimentos de treinamento e avaliação recompensam o chute em vez de admitir incerteza, e que chutar quando incerto melhora o desempenho nos testes. Isso corresponde integralmente à afirmação do slide, sem distorção ou exagero.
- Qwen3.7 Plus: sustenta. O slide afirma que os modelos aprendem a chutar porque os testes premiam o acerto e não a dúvida, fazendo com que chutar renda mais pontos do que dizer 'não sei'. O texto da fonte sustenta exatamente essa ideia ao afirmar que os procedimentos de treinamento e avaliação recompensam o 'chute' (guessing) em detrimento do reconhecimento da incerteza (acknowledging uncertainty), e que a forma como as a
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que os modelos são otimizados para serem bons realizadores de testes e que o ato de 'chutar' (guessing) quando há incerteza melhora o desempenho nos testes, confirmando a premissa de que os métodos de avaliação recompensam o chute em vez de premiar o reconhecimento da dúvida.

### c11 (p. 11): **sustenta**

> Bajulação: pessoas (e modelos de preferência) tendem a preferir respostas que concordam com elas, e isso ajuda a moldar o modelo a concordar.

Código: sycophan: achado, preference: achado

- DeepSeek V4 Pro: sustenta. O slide afirma que pessoas e modelos de preferência tendem a preferir respostas concordantes, e que isso molda o modelo a concordar. Os trechos mostram exatamente isso: respostas que batem com a visão do usuário são preferidas; humanos e PMs preferem respostas bajuladoras; e otimizar contra PMs sacrifica veracidade em favor da bajulação. A tradução 'bajulação' é fiel ao termo 'sycophancy'.
- Qwen3.7 Plus: sustenta. O texto afirma explicitamente que o feedback humano pode encorajar respostas do modelo que correspondem às crenças do usuário (bajulação). Além disso, os trechos indicam que tanto humanos quanto modelos de preferência (PMs) tendem a preferir respostas bajuladoras que concordam com as visões do usuário, e que a otimização contra esses modelos de preferência impulsiona o comportamento de bajulação n
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma explicitamente que tanto humanos quanto modelos de preferência tendem a preferir respostas que concordam com as visões do usuário (bajulação) e que o uso desse feedback no ajuste fino (finetuning) incentiva o modelo a adotar esse comportamento.

### c12 (p. 12): **sustenta**

> 55% das referências do ChatGPT-3.5 eram inventadas; 18% no ChatGPT-4, no mesmo teste; 636 referências somando os dois modelos.

Código: 55%: achado, 18%: achado, 636: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma exatamente as porcentagens (55% e 18%) e o total de 636 citações analisadas, que corresponde à soma das referências dos dois modelos. A tradução 'inventadas' para 'fabricated' é fiel.
- Qwen3.7 Plus: sustenta. O slide reproduz com exatidão os dados numéricos e o contexto apresentados no resumo do artigo. O texto confirma o total de 636 referências analisadas, bem como as taxas de 55% de citações inventadas para o GPT-3.5 e 18% para o GPT-4. Não há distorções, exageros ou omissões que alterem o sentido da fonte.
- Gemini 3.1 Flash-Lite: sustenta. O slide reflete com precisão os dados apresentados na fonte: a porcentagem de citações fabricadas para cada modelo (55% para GPT-3.5 e 18% para GPT-4) e o número total de referências analisadas (636).

### c13 (p. 12): **sustenta**

> Mais de 60% das respostas de oito buscadores com IA erraram a matéria original de um trecho de notícia (Tow Center, CJR, mar. 2025).

Código: 60 percent: achado, eight: achado

- DeepSeek V4 Pro: sustenta. O slide afirma que mais de 60% das respostas de oito buscadores com IA erraram a matéria original de um trecho de notícia. Os trechos fornecidos mostram que o estudo testou oito ferramentas de busca generativas ("We compared eight AI search engines") e que, coletivamente, elas forneceram respostas incorretas a mais de 60% das consultas ("incorrect answers to more than 60 percent of queries"). Isso
- Qwen3.7 Plus: sustenta. O texto afirma explicitamente que, coletivamente, os buscadores forneceram respostas incorretas em mais de 60% das consultas e que falharam em recuperar os artigos corretos, o que sustenta a afirmação do slide sobre a taxa de erro e a natureza da falha (errar a matéria original/artigo correto). A autoria e a data também conferem.
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma que, coletivamente, os oito buscadores testados pelo Tow Center forneceram respostas incorretas em mais de 60% das consultas sobre a recuperação e citação de notícias.

### c14 (p. 13): **sustenta**

> Mesmo um modelo de linguagem bem calibrado alucina: há uma taxa mínima de fatos inventados, ligada aos fatos que aparecem raramente nos dados de treino.

Código: hallucinat: achado, calibrat: achado, arbitrary facts: achado

- DeepSeek V4 Pro: sustenta. A fonte afirma explicitamente que modelos de linguagem calibrados têm uma taxa mínima de alucinações em certos fatos, e que a probabilidade de alucinar é próxima à fração de fatos que aparecem exatamente uma vez (i.e., raramente) nos dados de treino. Portanto, o slide é fiel ao conteúdo.
- Qwen3.7 Plus: sustenta. O slide afirma que modelos calibrados alucinam com uma taxa mínima ligada a fatos que aparecem raramente no treino. Os trechos sustentam exatamente isso: mostram um "lower-bound" (taxa mínima) de alucinação para modelos que satisfazem uma "statistical calibration condition" (modelo bem calibrado), e que essa probabilidade é próxima da fração de fatos que ocorrem exatamente uma vez no treino (fatos
- Gemini 3.1 Flash-Lite: sustenta. A fonte afirma explicitamente que existe um limite inferior estatístico inerente para alucinações em modelos calibrados e conecta essa taxa à fração de fatos que ocorrem exatamente uma vez nos dados de treinamento.

### c15 (p. 13): **sustenta**

> PAL: o modelo escreve o programa e o cálculo é feito por código (interpretador), no lugar do cálculo da IA.

Código: interpreter: achado, program: achado

- DeepSeek V4 Pro: sustenta. sustenta
- Qwen3.7 Plus: sustenta. Os trechos afirmam explicitamente que o PAL utiliza o LLM para gerar programas ('generate programs', ou seja, o modelo escreve o programa) e transfere a etapa de resolução para um ambiente de execução como um interpretador Python ('offloads the solution step to a runtime such as a Python interpreter', ou seja, o cálculo é feito pelo interpretador). Além disso, o texto reforça que a tarefa de resol
- Gemini 3.1 Flash-Lite: sustenta. A fonte confirma explicitamente que o PAL utiliza o LLM para gerar programas e delega a etapa de solução (cálculo) para um interpretador, substituindo a execução do cálculo pelo próprio LLM.

### c16 (p. 13): **sustenta**

> Verificadores externos e sólidos, em laço com quem gera, dão garantia ao resultado; LLMs sozinhos não planejam nem se verificam.

Código: verifier: achado, LLM-Modulo: achado

- DeepSeek V4 Pro: sustenta_em_parte. O slide afirma que 'LLMs sozinhos não planejam nem se verificam', o que é diretamente sustentado pelo trecho. Contudo, a afirmação de que verificadores externos em laço 'dão garantia ao resultado' não aparece nos excertos; o texto propõe uma integração mais estreita como uma abordagem melhor, mas não menciona garantia. Portanto, o slide vai além do que a fonte diz, caracterizando sustentação parci
- Qwen3.7 Plus: sustenta. O slide resume fielmente a tese central do artigo apresentada nos trechos. A afirmação de que 'LLMs sozinhos não planejam nem se verificam' corresponde literalmente a 'LLMs cannot, by themselves, do planning or self-verification'. A proposta de 'Verificadores externos... em laço' corresponde à visão de 'LLM-Modulo Frameworks' com 'external model-based verifiers' em 'bi-directional interaction regi
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que LLMs sozinhos não conseguem planejar nem se verificar. Além disso, propõe o 'LLM-Modulo Framework' como uma solução que combina LLMs com verificadores externos baseados em modelos em um regime de interação bidirecional, o que sustenta a afirmação do slide sobre a estrutura e a necessidade desses verificadores para o sucesso da tarefa.

### c17 (p. 14): **sustenta**

> Num sistema em série com componentes independentes, a confiabilidade é o produto das confiabilidades (regra do produto).

Código: multiply reliabilities: achado, independently: achado

- DeepSeek V4 Pro: sustenta. O trecho apresenta explicitamente a fórmula da confiabilidade do sistema em série como o produto das confiabilidades dos componentes, sob a suposição de independência.
- Qwen3.7 Plus: sustenta. O texto afirma explicitamente que, sob as premissas do modelo em série (incluindo a independência dos componentes e a falha do sistema na primeira falha de componente), a confiabilidade do sistema é o produto das confiabilidades dos componentes, apresentando inclusive a fórmula matemática correspondente ($R_S(t) = \prod_{i=1}^n R_i(t)$).
- Gemini 3.1 Flash-Lite: sustenta. A fonte confirma explicitamente a premissa de independência dos componentes e apresenta a fórmula matemática onde a confiabilidade do sistema (Rs) é o produto das confiabilidades dos componentes individuais (Ri), validando a regra do produto citada no slide.

### c18 (p. 14): **sustenta**

> Em tarefas composicionais de vários passos, os erros se acumulam e o desempenho cai à medida que a tarefa cresce.

Código: compositional: achado, error: achado

- DeepSeek V4 Pro: sustenta_em_parte. O trecho afirma que o desempenho decai rapidamente com o aumento da complexidade da tarefa, o que sustenta a segunda parte do slide ('o desempenho cai à medida que a tarefa cresce'). No entanto, não há menção explícita de que 'os erros se acumulam', apenas que o desempenho decai. O slide, portanto, vai além do que o trecho diz, acrescentando uma explicação (acumulação de erros) não presente na fon
- Qwen3.7 Plus: sustenta. O trecho afirma explicitamente que, em problemas de raciocínio de múltiplos passos, o desempenho das gerações autoregressivas pode decair rapidamente com o aumento da complexidade da tarefa. Isso sustenta diretamente a afirmação do slide de que, em tarefas composicionais de vários passos, o desempenho cai à medida que a tarefa cresce (o que, no contexto do artigo, ocorre porque o modelo não desenv
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que o desempenho das gerações autorregressivas pode decair rapidamente com o aumento da complexidade da tarefa em problemas de raciocínio de vários passos, o que sustenta a afirmação do slide.

### c19 (p. 15): **sustenta**

> Sem retorno de fora, o modelo tem dificuldade em corrigir o próprio raciocínio, e às vezes piora depois da autocorreção.

Código: self-correct: achado, external feedback: achado

- DeepSeek V4 Pro: sustenta. O slide afirma exatamente o que o resumo diz: dificuldade em corrigir o próprio raciocío ('struggle to self-correct') e piora do desempenho ('performance degrades') sem retorno externo ('without external feedback').
- Qwen3.7 Plus: sustenta. O slide é uma tradução fiel e direta das conclusões centrais apresentadas no resumo do artigo. A expressão 'sem retorno de fora' corresponde a 'without external feedback'; 'tem dificuldade em corrigir o próprio raciocínio' corresponde a 'In the context of reasoning... LLMs struggle to self-correct'; e 'às vezes piora depois da autocorreção' corresponde exatamente a 'at times, their performance eve
- Gemini 3.1 Flash-Lite: sustenta. O texto da fonte afirma explicitamente que, no contexto de raciocínio, os LLMs têm dificuldade em se autocorrigir sem feedback externo e que, por vezes, o desempenho piora após a autocorreção, o que corresponde exatamente ao que o slide afirma.

### c20 (p. 15): **sustenta**

> Conferir passo a passo (supervisão de processo) funciona melhor do que conferir só o resultado final.

Código: process supervision: achado, outcome supervision: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma explicitamente que a supervisão de processo supera significativamente a supervisão de resultado, o que corresponde à afirmação do slide de que funciona melhor.
- Qwen3.7 Plus: sustenta. O resumo define explicitamente a 'supervisão de resultado' (outcome supervision) como o feedback dado apenas para o resultado final, e a 'supervisão de processo' (process supervision) como o feedback dado para cada passo intermediário do raciocínio. Em seguida, o texto afirma categoricamente que a supervisão de processo supera significativamente a supervisão de resultado ('process supervision sign
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que a supervisão de processo (process supervision) supera significativamente a supervisão de resultado (outcome supervision) no treinamento de modelos para resolver problemas do dataset MATH, o que valida a afirmação do slide.

### c21 (p. 15): **sustenta**

> No GPT-4, a autocrítica derrubou o desempenho; um verificador externo e sólido trouxe grandes ganhos.

Código: GPT-4: achado, sound: achado, verifier: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma diretamente, em estudo com GPT-4, que houve colapso significativo de desempenho com autocrítica e ganhos significativos com verificação externa sólida. Isso corresponde exatamente ao que o slide afirma.
- Qwen3.7 Plus: sustenta. O texto afirma explicitamente que, no estudo empírico com o GPT-4, a autocrítica ('self-critique') resultou em um colapso significativo de desempenho ('significant performance collapse'), enquanto a verificação externa sólida ('sound external verification') trouxe ganhos significativos de desempenho ('significant performance gains'). A formulação do slide é uma tradução fiel e precisa das conclusõ
- Gemini 3.1 Flash-Lite: sustenta. O texto da fonte afirma explicitamente que observaram um colapso significativo no desempenho com a autocrítica e ganhos significativos com a verificação externa sólida, o que corrobora exatamente o que o slide afirma.

### c22 (p. 15): **sustenta**

> Modelos avaliadores reconhecem e tendem a preferir as próprias respostas.

Código: self-preference: achado, recogni: achado

- DeepSeek V4 Pro: sustenta. Os trechos indicam explicitamente que os modelos avaliadores reconhecem suas próprias gerações (self-recognition) e que existe um viés de autopreferência (self-preference), no qual eles avaliam suas próprias respostas como superiores. A afirmação do slide é uma tradução fiel desses achados.
- Qwen3.7 Plus: sustenta. O título do artigo e o resumo confirmam explicitamente que os avaliadores LLM reconhecem suas próprias gerações ("distinguishing themselves") e as favorecem ("scores its own outputs higher").
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma explicitamente que os modelos possuem capacidade de reconhecimento de suas próprias gerações ('self-recognition') e que exibem um viés de preferência ('self-preference'), atribuindo notas mais altas às suas próprias respostas em comparação com as de outros modelos.

### c24 (p. 41): **sustenta**

> Portaria CNPq nº 2.664/2026, art. 9º, I: c) declarar o uso de IA generativa, com a ferramenta e a finalidade; d) vedado submeter conteúdo gerado por IA como de autoria humana; e) vedado inserir projetos de terceiros em IA para pareceres; f) quem pesquisa responde pelo conteúdo final, inclusive plágios ou imprecisões da IA. Publicada no DOU, seção 1, p. 4, em 11/03/2026.

Código: 2.664: achado, inteligência artificial: achado, pareceres: achado

- DeepSeek V4 Pro: sustenta. O slide reproduz de forma fiel as alíneas c, d, e e f do artigo 9, I, da Portaria CNPq nº 2.664/2026. A alínea c exige declarar o uso de IA generativa, especificando ferramenta e finalidade; as alíneas d e e contêm as vedações mencionadas; a alínea f estabelece a responsabilização integral do pesquisador. Ademais, o cabeçalho do documento confirma a publicaçao no DOU, seçao 1, pág.4, em 11/03/2026
- Qwen3.7 Plus: sustenta. O slide reproduz fielmente o teor dos incisos c, d, e e f do art. 9º da Portaria CNPq nº 2.664/2026, bem como os dados de publicação (DOU, seção 1, página 4, em 11/03/2026). A única diferença é a omissão, no slide, da expressão 'de qualquer espécie e em qualquer fase do desenvolvimento da pesquisa (concepção, redação, análise de dados, submissão)' presente no inciso c, o que não descaracteriza a f
- Gemini 3.1 Flash-Lite: sustenta. O slide descreve corretamente as alíneas 'c', 'd', 'e' e 'f' do inciso I do Art. 9º da Portaria CNPq nº 2.664/2026, bem como os dados de publicação (DOU, 11/03/2026, Seção 1, p. 4).

### c34 (p. 38): **sustenta**

> Com um assistente automático, a pessoa aceita a resposta e deixa de conferir, seja novata ou especialista; treino e instrução não bastam para evitar.

Código: complacency: achado, automation bias: achado, experts: NÃO achado

- DeepSeek V4 Pro: sustenta. O slide afirma que, com um assistente automático, a pessoa aceita a resposta e deixa de conferir, seja novata ou especialista, e que treino e instrução não bastam para evitar. Os trechos sustentam isso para o fenômeno de automation bias: ele ocorre em participantes novatos e especialistas, não pode ser prevenido por treinamento ou instruções, e resulta em erros de omissão (deixar de agir/conferir)
- Qwen3.7 Plus: sustenta. O slide afirma que o viés/complacência ocorre tanto em novatos quanto em especialistas e que treino e instrução não são suficientes para evitá-lo. O resumo do artigo sustenta exatamente isso ao afirmar que a complacência e o viés de automação ocorrem em participantes tanto ingênuos (novatos) quanto especialistas, e que não podem ser superados com prática simples nem prevenidos por treinamento ou i
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma explicitamente que o viés de automação (que leva à aceitação da resposta do sistema e erros de omissão/comissão) ocorre tanto em novatos quanto em especialistas e que não pode ser evitado por meio de treinamento ou instruções.

### c35 (p. 30): **sustenta_em_parte**

> Um painel de juízes de famílias de modelos diferentes, agregado por voto (para julgamentos binários, o voto da maioria), avalia melhor e com menos viés que um único juiz grande.

Código: panel: achado, max voting: achado, intra-model bias: achado

- DeepSeek V4 Pro: sustenta_em_parte. Os trechos da fonte confirmam que um painel de modelos menores de famílias disjuntas (PoLL) supera um juiz único grande e apresenta menos viés intramodelo. No entanto, não especificam o método de agregação por voto majoritário para julgamentos binários mencionado no slide, portanto o slide é sustentado apenas em parte.
- Qwen3.7 Plus: sustenta_em_parte. O slide afirma que o painel é "agregado por voto (para julgamentos binários, o voto da maioria)". Embora os trechos fornecidos (que consistem apenas no resumo do artigo) sustentem que o painel é composto por famílias de modelos disjuntas ("disjoint model families"), que avalia melhor ("outperforms a single large judge") e com menos viés ("exhibits less intra-model bias"), eles não mencionam em nen
- Gemini 3.1 Flash-Lite: sustenta_em_parte. A fonte sustenta que o painel (PoLL) supera um juiz único e apresenta menos viés devido à composição de famílias de modelos distintas. Contudo, os trechos fornecidos não mencionam o método de agregação por voto (voto da maioria para julgamentos binários), tornando a afirmação parcialmente sustentada.

### c36 (p. 31): **sustenta**

> FActScore avalia a precisão factual item a item: quebra o texto em fatos atômicos e confere cada um contra uma fonte.

Código: atomic facts: achado

- DeepSeek V4 Pro: sustenta. sustenta
- Qwen3.7 Plus: sustenta. O trecho afirma explicitamente que o FActScore quebra a geração em uma série de fatos atômicos e calcula a porcentagem de fatos atômicos suportados por uma fonte de conhecimento confiável. Isso corresponde exatamente à afirmação do slide de que a métrica avalia a precisão factual item a item, decompondo o texto em fatos atômicos e conferindo cada um contra uma fonte.
- Gemini 3.1 Flash-Lite: sustenta. O trecho da fonte descreve exatamente o funcionamento do FACTSCORE como uma avaliação que divide a geração em fatos atômicos e calcula a porcentagem desses fatos suportados por uma fonte de conhecimento confiável, o que valida a afirmação do slide.

### m01 (p. 30): **sustenta**

> Registrar hipótese, métodos e análise antes de ver os dados (pré-registro) separa o teste confirmatório da exploração e protege contra ajustar a análise ao resultado.

Código: preregistration: achado, confirmatory: NÃO achado, exploratory: NÃO achado

- DeepSeek V4 Pro: sustenta. A fonte define claramente o pré-registro como a definição das questões de pesquisa e plano de análise antes da observação dos dados. Ela afirma que o pré-registro distingue análises e resultados decorrentes de predições (teste confirmatório) daqueles decorrentes de postdições (exploração), e que isso evita o viés retrospectivo responsável por ajustar a análise ao resultado. Portanto, o slide refle
- Qwen3.7 Plus: sustenta. O slide afirma que o pré-registro consiste em registrar hipóteses, métodos e análise antes de ver os dados, o que é sustentado por 'define the research questions and analysis plan before observing the research outcomes-a process called preregistration'. A separação entre teste confirmatório e exploração é sustentada por 'increase distinctiveness between hypothesis generation and hypothesis testing
- Gemini 3.1 Flash-Lite: sustenta. O texto da fonte confirma que o pré-registro envolve definir questões de pesquisa e planos de análise antes de observar os resultados. Além disso, estabelece que esse processo distingue predições (testes confirmatórios) de pós-dições (geração de hipóteses/exploração), o que mitiga vieses de raciocínio (como o viés de retrospectiva) que levam ao ajuste indevido da análise aos dados.

### m04 (p. 35): **sustenta**

> O procedimento de Holm é um teste múltiplo sequencial que controla o erro do tipo I entre várias comparações feitas ao mesmo tempo.

Código: sequentially rejective: achado, multiple test: achado, type I: NÃO achado

- DeepSeek V4 Pro: sustenta. O trecho descreve um procedimento de teste múltiplo do tipo sequencialmente rejectivo, que controla o erro do tipo I (primeira espécie) em um nível de significância prescrito, exatamente como afirma o slide: um teste múltiplo sequencial que controla o erro do tipo I em várias comparações.
- Qwen3.7 Plus: sustenta. O trecho afirma explicitamente que o artigo apresenta um 'multiple test procedure of the sequentially rejective type' (procedimento de teste múltiplo de tipo sequencialmente rejeitivo) e que o teste possui 'protection against error of the first kind' (proteção contra o erro do primeiro tipo, ou seja, erro do tipo I) para qualquer combinação de hipóteses verdadeiras (várias comparações). A afirmaçã
- Gemini 3.1 Flash-Lite: sustenta. O trecho confirma que o procedimento é um teste múltiplo do tipo sequencial e que ele garante proteção contra o erro do tipo I para qualquer combinação de hipóteses, o que sustenta a afirmação de controle de erro em comparações múltiplas.

### m05 (p. 35): **sustenta**

> Quando as observações de um mesmo grupo (por exemplo, os artigos de uma mesma rodada) não são independentes, o erro-padrão agrupado por grupo corrige a inferência.

Código: cluster: achado, robust: achado

- DeepSeek V4 Pro: sustenta. A fonte afirma que, quando há correlação entre observações dentro de clusters, os erros-padrão comuns superestimam a precisão do estimador, e a inferência deve ser baseada em erros-padrão cluster-robustos. Isso sustenta plenamente a afirmação do slide de que o erro-padrão agrupado por grupo corrige a inferência quando as observações do grupo não são independentes.
- Qwen3.7 Plus: sustenta. O trecho do abstract do artigo afirma exatamente que, quando os dados são agrupados em clusters e os erros do modelo de regressão são correlacionados dentro dos clusters (ou seja, as observações de um mesmo grupo não são independentes), os erros-padrão padrão superestimam a precisão e a inferência estatística deve ser baseada em erros-padrão robustos a clusters (cluster-robust standard errors), o 
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma que, quando os dados estão agrupados (o que implica correlação dentro dos grupos e falta de independência), os erros-padrão padrão podem superestimar a precisão, sendo necessário utilizar erros-padrão robustos por cluster para a inferência estatística.

### m08 (p. 31): **sustenta**

> Usar um modelo de linguagem como juiz funciona, mas o juiz tem vieses conhecidos, como preferir as próprias respostas e ser influenciado pela posição e pela extensão da resposta.

Código: self-enhancement: achado, position bias: achado, verbosity: achado

- DeepSeek V4 Pro: sustenta. O slide afirma que usar LLM como juiz funciona (sustentado pela alta concordância com preferências humanas) e que há vieses de posição, extensão e preferência pelas próprias respostas. Os resumos listam exatamente esses três vieses (position, verbosity, self-enhancement) e confirmam a eficácia do método. A tradução dos termos é fiel.
- Qwen3.7 Plus: sustenta. O slide afirma que usar um LLM como juiz funciona, mas apresenta vieses como preferir as próprias respostas (self-enhancement), posição (position) e extensão (verbosity). O resumo do artigo confirma explicitamente que o método funciona para aproximar preferências humanas e lista exatamente esses três vieses (position, verbosity, and self-enhancement biases) como limitações examinadas.
- Gemini 3.1 Flash-Lite: sustenta. O texto confirma que o uso de LLMs como juízes funciona (atingindo alta concordância com humanos) e lista explicitamente os vieses de posição (position), verbosidade (extensão da resposta) e auto-enaltecimento (self-enhancement, que se refere a preferir as próprias respostas).

### n01 (p. 38): **sustenta**

> Human in the loop: pessoas atuam dentro do fluxo de um sistema de aprendizado de máquina e fazem as tarefas difíceis para o computador, com a ajuda da máquina.

Código: human-in-the-loop: achado, hard for computers: achado

- DeepSeek V4 Pro: sustenta. O trecho afirma explicitamente que humanos realizam tarefas difíceis para computadores no pipeline, com a ajuda de abordagens baseadas em máquina, em total acordo com o slide.
- Qwen3.7 Plus: sustenta. O slide traduz e parafraseia fielmente a definição apresentada no resumo do artigo. O texto original afirma que os humanos podem realizar tarefas difíceis para os computadores no pipeline (fluxo) com a ajuda de abordagens baseadas em máquina ('directly accomplish tasks that are hard for computers in the pipeline with the help of machine-based approaches'), o que corresponde exatamente à afirmação 
- Gemini 3.1 Flash-Lite: sustenta. O slide reflete fielmente a definição apresentada no texto, que afirma que humanos podem realizar tarefas difíceis para computadores dentro do fluxo (pipeline) com o auxílio de abordagens baseadas em máquina.

### n02 (p. 39): **sustenta**

> Em artigos de revistas médicas, 25% das citações têm erro e 12% têm erro grave (revisão sistemática e meta-análise).

Código: 25.4: achado, 11.9: NÃO achado, 11,9: achado

- DeepSeek V4 Pro: sustenta. O slide afirma 25% de citações com erro e 12% com erro grave. O resumo reporta taxa total de erro de citação de 25,4% e taxa de erro grave (major) de 11,9%. Os valores do slide são arredondamentos fiéis (25% ≈ 25,4%; 12% ≈ 11,9%) e a fonte é de fato uma revisão sistemática e meta-análise. Portanto, o slide é sustentado pelos trechos.
- Qwen3.7 Plus: sustenta. O slide afirma que 25% das citações têm erro e 12% têm erro grave. O resumo da fonte apresenta exatamente esses dados: taxa de erro total ('total quotation error rates') de 25,4% e taxa de erro grave ('major quotation error rates') de 11,9%. O arredondamento para números inteiros (25% e 12%) é uma prática padrão e aceitável em slides, não configurando exagero ou distorção. A tradução de 'major' pa
- Gemini 3.1 Flash-Lite: sustenta. O slide apresenta os valores de 25% para o total de erros e 12% para erros graves, que correspondem aos valores de 25,4% e 11,9% reportados na fonte, respectivamente, após arredondamento.

### n03 (p. 40): **sustenta**

> Citação traduzida: "A proliferação de ferramentas de IA na ciência arrisca inaugurar uma fase da pesquisa científica em que produzimos mais, mas entendemos menos."

Código: produce more but understand less: achado

- DeepSeek V4 Pro: sustenta. A frase original em inglês, localizada nos trechos fornecidos, corresponde exatamente à afirmação traduzida no slide. A tradução é fiel.
- Qwen3.7 Plus: sustenta. A citação traduzida no slide corresponde exatamente ao trecho original em inglês. A tradução é fiel ('risks introducing' para 'arrisca inaugurar', 'scientific enquiry' para 'pesquisa científica', etc.).
- Gemini 3.1 Flash-Lite: sustenta. O trecho da fonte é idêntico à afirmação do slide, sendo uma tradução fiel e direta.

### n04 (p. 40): **sustenta**

> Citação traduzida da Recomendação da UNESCO sobre a Ética da IA (2021), § 36: "Um sistema de IA nunca pode substituir a responsabilidade e a prestação de contas humanas finais."

Código: never replace ultimate human responsibility: achado

- DeepSeek V4 Pro: sustenta. A citação traduzida é fiel ao original: 'ultimate human responsibility and accountability' foi corretamente vertido como 'responsabilidade e a prestação de contas humanas finais'. O slide apenas reproduz a afirmação do § 36, sem acréscimos ou distorções.
- Qwen3.7 Plus: sustenta. O trecho do parágrafo 36 afirma literalmente que "an AI system can never replace ultimate human responsibility and accountability". A tradução apresentada no slide ("Um sistema de IA nunca pode substituir a responsabilidade e a prestação de contas humanas finais") é fiel ao original em inglês.
- Gemini 3.1 Flash-Lite: sustenta. A citação traduzida no slide é fiel ao texto original do parágrafo 36 da Recomendação da UNESCO sobre a Ética da IA, que afirma que 'an AI system can never replace ultimate human responsibility and accountability'.

### n05 (p. 40): **sustenta**

> Citação traduzida do editorial da Nature (2023): "Qualquer atribuição de autoria traz consigo a responsabilidade pelo trabalho, e ferramentas de IA não podem assumir tal responsabilidade."

Código: accountability for the work: achado, cannot take such responsibility: achado

- DeepSeek V4 Pro: sustenta. A citação traduzida reproduz exatamente o conteúdo do trecho original em inglês. A tradução é fiel: 'qualquer atribuição de autoria traz consigo a responsabilidade pelo trabalho' corresponde a 'any attribution of authorship carries with it accountability for the work', e 'ferramentas de IA não podem assumir tal responsabilidade' corresponde a 'AI tools cannot take such responsibility'.
- Qwen3.7 Plus: sustenta. O slide apresenta uma tradução fiel da frase encontrada no texto original.
- Gemini 3.1 Flash-Lite: sustenta. A tradução apresentada no slide é fiel ao texto original da fonte, que afirma explicitamente que a atribuição de autoria implica responsabilidade pelo trabalho e que ferramentas de IA não podem assumir essa responsabilidade.

### n06 (p. 33): **sustenta**

> Preço público da API do Claude Sonnet 5.5: US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de tokens de saída; buscas na web a US$ 10 por mil.

Código: Sonnet 5.5: achado, $10: achado

- DeepSeek V4 Pro: sustenta_em_parte. O preço de entrada ($2/MTok) é sustentado indiretamente pelo custo de cache read. O preço de buscas na web ($10/mil) é sustentado literalmente. O preço de saída ($10/MTok) não é confirmado diretamente por nenhum trecho da documentação oficial fornecida; a tabela de Batch API é ambígua e reflete preços com desconto, e a fonte externa não é a citada. Portanto, o slide é sustentado apenas em parte.
- Qwen3.7 Plus: sustenta. Os trechos confirmam que o preço de entrada do Sonnet 5.5 é US$ 2 (já que 5% do preço padrão de entrada é US$ 0,10) e o preço de saída é US$ 10 (conforme o resumo de preços que lista explicitamente "$2/$10 for Sonnet 5.5"). Além disso, confirmam que a busca na web custa US$ 10 por mil buscas ("$10 per 1,000 searches"). A tradução dos valores e termos para o slide está fiel.
- Gemini 3.1 Flash-Lite: sustenta. A fonte confirma explicitamente que o preço do Claude Sonnet 5.5 é de US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de tokens de saída, além de confirmar que as buscas na web custam US$ 10 por 1.000 buscas.

### n07 (p. 39): **sustenta**

> Mesmo bem calibrado, um modelo de linguagem inventa parte dos fatos raros: o erro faz parte do método.

Código: calibrated: achado, hallucinat: achado

- DeepSeek V4 Pro: sustenta. sustenta
- Qwen3.7 Plus: sustenta. O slide resume corretamente a tese central do artigo. O texto afirma que modelos calibrados ('satisfy a statistical calibration condition') têm um limite inferior estatístico inerente ('inherent statistical lower-bound') para a taxa de alucinação de fatos arbitrários e raros ('fraction of facts that occur exactly once in the training data'), o que equivale a dizer que o erro (alucinação) é uma con
- Gemini 3.1 Flash-Lite: sustenta. O texto afirma explicitamente que modelos de linguagem que satisfazem uma condição de calibração estatística possuem um limite inferior inerente para a taxa de alucinação em fatos 'arbitrários' (que ocorrem raramente, como uma vez no conjunto de treinamento), confirmando que o erro é uma consequência estatística do método de calibração.

### n08 (p. 34): **sustenta**

> Código onde dá e IA com conferência onde precisa é o verificador externo e sólido de Kambhampati; IA conferindo IA tem limites (Huang et al.; Stechly et al.).

Código: verifier: achado, self-correct: achado, self-critique: achado

- DeepSeek V4 Pro: sustenta_em_parte. Os trechos sustentam que verificação externa sólida traz ganhos e que autoavaliação/autocorreção de LLMs tem limites. Porém, a formulação do slide 'código onde dá e IA com conferência onde precisa' não aparece nos trechos; a fonte fala em 'external model-based verifiers', sem mencionar código ou a divisão específica proposta no slide.
- Qwen3.7 Plus: sustenta. Os trechos de Kambhampati sustentam a proposta de um verificador externo ("external model-based verifiers", "sound external verification") em contraste com a auto-verificação. Os demais trechos (que correspondem aos trabalhos de Huang et al. e Stechly et al. citados) sustentam que a IA conferindo a si mesma ("self-correction", "self-critique") tem limites e pode até degradar o desempenho sem feedb
- Gemini 3.1 Flash-Lite: sustenta. O texto de Kambhampati defende o uso de 'external model-based verifiers' (verificadores externos, tipicamente simbólicos ou baseados em código) para complementar LLMs, o que sustenta a primeira parte do slide. Os trechos adicionais confirmam que a auto-correção (IA conferindo IA) é ineficaz e pode causar degradação de desempenho, validando a segunda parte do slide sobre os limites da auto-verifica
