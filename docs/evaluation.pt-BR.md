[Read in English](evaluation.md)

# Avaliação: como cada artigo é julgado

## Em poucas palavras

Todo nível recebe o mesmo pedido: 25 artigos de periódico revisados por pares e empíricos sobre um tema estreito, com
9 campos cada. Depois conferimos cada artigo entregue, do mesmo jeito para os quatro níveis. O código confere tudo o
que tem resposta certa num registro público (o DOI, o título, o autor, o ano, a revista, o período, o tipo de
publicação, o trecho e a amostra). Um júri de três IAs de três empresas diferentes, que não sabem qual nível produziu o
artigo, lê o resumo e decide o resto: o artigo é do tema, é empírico, o método é o que foi dito, o resumo sustenta o
achado. Um artigo só conta como certo quando passa em todas as conferências. Um campo errado e o artigo inteiro conta
como erro.

A métrica principal é a **precisão**: dos artigos entregues, quantos estão 100% certos. Ao lado dela, informamos
tempo, chamadas de IA, tokens, custo em reais e como os 25 artigos pedidos se dividem em certos, errados e não
entregues.

As métricas e os critérios de julgamento foram fixados antes das rodadas.

## A tarefa e o desenho

- **Tarefa.** Uma revisão bibliográfica. Cada rodada pede 25 artigos de periódico revisados por pares e empíricos
  sobre um tema estreito, publicados de 2018 a 2025, e para cada um 9 campos: DOI, título, autores, ano, periódico,
  tipo de estudo e método, tamanho da amostra como aparece no resumo, achado principal em uma frase e um trecho
  literal do resumo.
- **Desenho.** 4 níveis x 6 temas x 2 repetições = 48 rodadas, 12 rodadas por nível. Uma rodada é um nível em um
  tema, uma vez. Cada tema roda duas vezes em cada nível porque a IA é probabilística: a mesma entrada pode dar saídas
  diferentes.
- **Executor.** Claude Sonnet 5.5, o mesmo em todos os níveis, chamado pelo Claude Agent SDK (Claude Code). A única
  coisa que muda entre os níveis é a arquitetura.
- **Cinco empresas.** Claude (Anthropic) executa, GLM (Z.ai) confere dentro dos Níveis 2 e 3; DeepSeek, Qwen
  (Alibaba) e Gemini (Google) julgam.

Os seis temas (ids como em `benchmark/topics.json`):

| Id | Tema |
| --- | --- |
| a04 | Jogos contra a desinformação, como o Bad News (o tema de exemplo) |
| a01 | Influência continuada da informação falsa |
| a02 | Agências de checagem brasileiras |
| a03 | Educação midiática na escola e na universidade |
| a05 | Percepção de imagens, vídeos e áudios feitos por IA |
| a06 | Manchetes caça-cliques |

## O que conta como certo

Um artigo está certo quando os 9 campos estão certos e ele atende ao pedido. A regra é rígida de propósito: numa
revisão bibliográfica, uma referência com o ano errado, um trecho que não está no resumo ou um achado que o resumo não
sustenta é uma referência que quem pesquisa não pode usar como foi entregue. Por isso, um campo errado e o artigo
inteiro conta como erro. Isso segue a lógica item a item do FActScore (Min et al., 2023): quebrar a saída em unidades
que podem ser conferidas uma a uma e medir a parte que se sustenta.

Cada campo tem um dono:

| Campo | Quem confere | O que se confere |
| --- | --- | --- |
| DOI | código | existe no Crossref ou no OpenAlex |
| Título | código | bate com o título do registro |
| Autores | código | o primeiro autor informado bate com um dos primeiros autores do registro |
| Ano | código | bate com um ano do registro; cai no período pedido |
| Periódico | código | bate com o periódico do registro; o registro é de artigo de periódico |
| Tipo de estudo e método | júri | o estudo é empírico, e o tipo e o método batem com o resumo |
| Tamanho da amostra | código | como foi escrito, está no resumo (ou o agente declara que não é informado) |
| Achado principal | júri | o resumo o sustenta |
| Trecho literal | código | está no resumo |

Além dos campos, o júri decide se o artigo é **do tema**: dentro do recorte pedido (assunto, plataforma, país,
público).

### Por que precisão, e por que os desfechos aparecem à parte

A precisão é medida sobre os artigos **entregues**. Um agente que entrega menos artigos não é punido na precisão
pelos que deixou de fora. Isso é deliberado: uma métrica que premia completar a lista empurra o agente a chutar, e o
chute é justamente o comportamento que produz referências inventadas (Kalai et al., 2025). Um agente que diz
"encontrei 20 que se sustentam" é mais útil do que um que completa a lista até 25 com 5 errados.

Para manter o quadro completo à vista, cada rodada também é dividida em três partes dos **25 artigos pedidos**, que
sempre somam 100%:

- **Certos:** entregues e 100% corretos.
- **Errados:** entregues com pelo menos uma conferência reprovada.
- **Não entregues:** pedidos, mas fora da entrega. Uma rodada pausada (o verificador recusou a quinta tentativa de um
  passo, e a rodada não entregou relatório) conta os seus 25 artigos como não entregues.

Um exemplo, com o Nível 3 pelo júri: de cada 100 artigos pedidos, 81 chegam certos, 2 chegam errados e 17 não chegam;
de cada 100 artigos entregues, 97 estão certos. A precisão é a média dos seis temas (em cada tema, os certos sobre os
entregues), e certos, errados e não entregues são médias por rodada sobre os 25 pedidos. Por isso uma não sai da
outra com os números já arredondados.

## As conferências por código, em detalhe

O código confere o que tem resposta certa fora da IA. Ele é determinístico: a mesma entrada sempre dá o mesmo
veredito, e cada veredito pode ser rastreado. Fica em `evaluation/evaluate.py`, com a leitura de páginas, a
normalização de texto e a busca do trecho em `evaluation/verify.py`, e os clientes dos registros em
`benchmark/scholar.py`.

1. **O DOI existe.** O avaliador procura o DOI no Crossref e no OpenAlex. Quando nenhum dos dois o conhece, o
   avaliador busca o título no OpenAlex para separar dois erros: um artigo real com o DOI errado, ou uma referência
   que não se encontra em lugar nenhum. É a separação que Walters e Wilder (2023) usam entre referências inventadas e
   erros de conteúdo em referências reais.
2. **Título.** Comparado com todos os títulos que os registros e a editora têm para aquele DOI (Crossref, OpenAlex,
   Semantic Scholar e a página da editora). A comparação tolera subtítulo, pontuação e maiúsculas, e também o título do
   próprio artigo em outro idioma, quando a editora o declara.
3. **Autor.** O primeiro autor informado precisa bater com um dos primeiros autores do registro. Qualquer estilo de
   citação é aceito: "Nome Sobrenome", "Sobrenome, Nome" ou "Sobrenome Iniciais".
4. **Ano.** Precisa ser um dos anos que o registro guarda para o artigo (as datas impressa e online podem diferir).
5. **Periódico.** Precisa bater com o periódico do registro.
6. **Período.** O ano do registro precisa cair dentro do período pedido, 2018 a 2025.
7. **Tipo de publicação.** O registro no Crossref precisa ser de artigo de periódico. Artigo de congresso, capítulo de
   livro e preprint não contam.
8. **Trecho.** O trecho literal precisa estar no resumo. O avaliador reúne o resumo do OpenAlex, do Crossref e do
   Semantic Scholar, e também abre a página da editora pelo DOI. Os dois lados são normalizados antes (forma Unicode,
   aspas e traços tipográficos, espaços e maiúsculas), para que diferença de formatação nunca conte como erro. Um
   trecho com reticências é dividido nas suas passagens literais, e cada passagem precisa ser encontrada. Uma
   correspondência quase literal, com nota de semelhança muito alta, é aceita, para absorver uma diferença de
   codificação; uma paráfrase não é.
9. **Amostra.** O tamanho da amostra precisa estar no resumo: a frase literal, ou todos os números que ela traz.
   Quando o agente declara que o resumo não informa a amostra, nada é conferido contra ela.

O avaliador consulta fontes que o Nível 3 não usa: o Semantic Scholar e a página da editora. Assim, o Nível 3 nunca é
conferido só contra as mesmas bases em que buscou.

## Os critérios de julgamento

Alguns campos não têm resposta num registro: exigem leitura. Para eles, um juiz recebe o pedido de quem pesquisa, os
metadados do artigo no registro (título, ano, periódico), o seu resumo e os dados que o agente extraiu (tipo de
estudo, método, amostra, achado). Mais nada. E decide quatro critérios:

1. **Do tema.** O artigo trata do assunto pedido, dentro do recorte pedido (plataforma, país, público)?
2. **Empírico.** O estudo coleta ou analisa dados próprios do tipo que o pedido exige (experimento, survey,
   entrevistas, grupos focais, análise de conteúdo ou de documentos)? Ensaio teórico e revisão não contam.
3. **Método como dito.** O tipo de estudo e o método que o agente informou batem com o resumo?
4. **Achado sustentado.** O resumo sustenta o achado que o agente informou? O juiz responde `supported` (sustentado),
   `partial` (só em parte, ou o achado vai além do resumo) ou `unsupported` (não sustentado). Só `supported` passa.

O juiz precisa primeiro copiar o trecho do resumo (ou dos metadados) que decide cada critério, e só então decidir. Os
rótulos precisam concordar com os trechos que ele copiou. Ele responde num esquema JSON estrito, com temperatura 0,
para que todo veredito venha com a sua evidência e tenha o mesmo formato. A chamada do juiz é a mesma para os três
juízes, em `evaluation/judge_llm.py`. As respostas ficam em cache, então rodar a avaliação de novo nunca paga duas
vezes pelo mesmo julgamento.

### O resumo é a evidência

Os juízes leem o resumo, e só o resumo. Três motivos. É o único texto que as bases guardam para quase todo artigo,
então todos os níveis são julgados sobre a mesma evidência. É para ele que o próprio pedido aponta: a amostra "como
aparece no resumo" e o trecho "do resumo". E mantém o julgamento verificável: qualquer pessoa pode abrir o mesmo
resumo e repetir a decisão. A página da editora é usada só pelo código, para achar o trecho; nunca é mostrada a um
juiz. Um artigo para o qual nenhuma fonte guarda resumo não pode ser julgado, então não conta como certo.

Isso também é um limite, discutido em [limits-and-next-steps.pt-BR.md](limits-and-next-steps.pt-BR.md): um resumo pode
omitir um detalhe de método que o artigo completo informa.

## O júri de três empresas (a medida principal)

A medida principal é um júri de três modelos de três empresas: **DeepSeek V4 Pro** (DeepSeek), **Qwen3.7 Plus**
(Alibaba) e **Gemini 3.1 Flash-Lite** (Google). Cada juiz decide os quatro critérios sozinho. O júri fica com a
**maioria por critério**: um critério passa quando pelo menos dois dos três juízes o aprovam. Um artigo está certo
quando passa nas conferências por código e o júri aprova os quatro critérios. Um artigo precisa dos três vereditos
para contar como certo. O júri fica em `evaluation/jury.py`.

Por que três empresas, e por que estas:

- **Um painel supera um juiz só.** Verga et al. (2024) mostram que um painel de modelos menores, de famílias
  diferentes, concorda mais com o julgamento humano do que um único juiz grande, e reduz o viés de cada família de
  modelos.
- **Ninguém julga a própria empresa.** Modelos tendem a reconhecer e preferir textos escritos por eles mesmos
  (Panickssery, Bowman e Feng, 2024). Por isso nenhum juiz é da Anthropic, cujo modelo executa, nem da Z.ai, cujo
  modelo é o verificador dentro dos Níveis 2 e 3. Executor, verificador e juízes somam cinco empresas.
- **Os vieses conhecidos do juiz ficam de fora pelo desenho.** Zheng et al. (2023) documentam os vieses de juízes de
  IA: de posição (preferir a primeira resposta mostrada), de verbosidade (preferir respostas mais longas) e de
  autopromoção (preferir a própria família). Aqui cada juiz avalia um artigo por vez contra critérios fixos, e não
  duas respostas uma contra a outra, então não há posição a favorecer; ele precisa citar a evidência antes de decidir;
  e é de uma empresa diferente da do executor.
- **Cego ao nível.** O juiz não sabe qual nível, nem qual arquitetura, produziu o artigo. As instruções dizem apenas
  que ele não sabe quem extraiu os dados. Assim, um juiz não tem como favorecer uma arquitetura que espera ser melhor.

Os três juízes dão o mesmo veredito em 85% dos 980 artigos que julgaram; a maior parte da discordância está no método.

## O juiz único (a medida de comparação)

Para comparar, o **DeepSeek V4 Pro sozinho** julga os mesmos artigos, nas mesmas rodadas, com os mesmos critérios e as
mesmas conferências por código. Só muda o voto: um juiz no lugar da maioria de três. Se a ordem dos níveis valesse só
num jeito de julgar, ela seria uma propriedade do juiz, e não das arquiteturas. As duas medidas dão a mesma ordem: veja
[results.pt-BR.md](results.pt-BR.md).

## Como o custo é calculado

Para cada rodada, o avaliador informa tempo de relógio, chamadas de IA, tokens e custo em reais.

- **Executor.** Claude Sonnet 5.5 pelo [preço público da API da Anthropic](https://platform.claude.com/docs/en/about-claude/pricing):
  entrada, saída, escrita em cache e leitura de cache, cada uma no seu preço, lidas do uso que a API registra em cada
  chamada em `calls/`; mais as buscas na web que o executor fez, pelo preço público por busca.
- **Verificador.** GLM-5.3 Flash pelo valor que a OpenRouter cobrou em cada chamada, como registrado no log de eventos
  da rodada.
- **Câmbio.** O total em dólar é convertido pela PTAX de venda do Banco Central do Brasil de 14/10/2026,
  US$ 1 = R$ 5,0441.

O executor deste teste rodou numa assinatura do Claude Code. Precificar os seus tokens pelo preço público da API dá um
custo que qualquer pessoa pode comparar e reproduzir. Os juízes não entram no custo de uma rodada: pertencem à
avaliação, e não ao agente. O que o teste inteiro custou de fato foi a assinatura (que já existia) mais cerca de
R$ 170 em tokens na OpenRouter (US$ 33,38, verificador e juízes).

## Onde fica cada arquivo de avaliação

Cada nível guarda as suas avaliações ao lado das suas rodadas, para que um nível possa ser lido e depurado sem mexer
nos outros:

```
agents/level_N/
  runs/class-nN-<topic>-r<rep>/    a rodada: events.jsonl, final.json, meta.json, calls/
  evaluations/judge-deepseek/      um arquivo por rodada: conferências por código + DeepSeek V4 Pro
  evaluations/judge-qwen/          o mesmo, Qwen3.7 Plus
  evaluations/judge-gemini/        o mesmo, Gemini 3.1 Flash-Lite
  evaluations/jury/                o júri: maioria dos três, por critério
```

Cada arquivo de avaliação guarda, para cada artigo entregue naquela rodada, o resultado de cada conferência por
código, o veredito do juiz com a evidência copiada e se o artigo conta como certo; e, para a rodada, o número de
entregues, o número de certos e a precisão.

Para avaliar rodadas suas (tag `mytest`):

```
python -m evaluation.evaluate --judge deepseek --prefix mytest
python -m evaluation.evaluate --judge qwen --prefix mytest
python -m evaluation.evaluate --judge gemini --prefix mytest
python -m evaluation.jury mytest
python -m evaluation.report mytest
python -m evaluation.stats mytest
```

## Referências deste documento

Kalai et al. (2025); Min et al. (2023); Panickssery, Bowman e Feng (2024); Verga et al. (2024); Walters e Wilder
(2023); Zheng et al. (2023); Anthropic, Pricing; Banco Central do Brasil, PTAX. Entradas completas em
[references.pt-BR.md](references.pt-BR.md).
