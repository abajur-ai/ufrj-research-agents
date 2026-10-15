[Read in English](run-the-benchmark.md)

# Rodar o benchmark

Neste guia você vai rodar os agentes de pesquisa com as próprias mãos. Começa pelo jeito mais simples, que é pedir ao Claude Code que faça por você, com uma instrução pronta para colar. Depois vêm os comandos manuais, uma seção para cada: uma rodada, um lote de rodadas, a avaliação pelos três juízes, o júri, o relatório e a estatística, a reprodução dos números da aula sem custo, o acompanhamento de uma rodada no visualizador e a gravação de um vídeo de replay. O guia termina com onde fica cada saída, quanto custa e quanto demora cada nível, e o que fazer quando algo dá errado. Antes de começar, conclua os [Primeiros passos](getting-started.pt-BR.md).

## Sumário

1. [O jeito mais simples: pedir ao Claude Code](#1-o-jeito-mais-simples-pedir-ao-claude-code)
2. [Nomes que você vai ver](#2-nomes-que-você-vai-ver)
3. [Uma rodada](#3-uma-rodada)
4. [Um lote de rodadas](#4-um-lote-de-rodadas)
5. [Avaliação com os três juízes](#5-avaliação-com-os-três-juízes)
6. [O júri](#6-o-júri)
7. [Relatório e estatística](#7-relatório-e-estatística)
8. [Reproduzir os números da aula](#8-reproduzir-os-números-da-aula)
9. [Acompanhar uma rodada no visualizador](#9-acompanhar-uma-rodada-no-visualizador)
10. [Gravar um vídeo de replay](#10-gravar-um-vídeo-de-replay)
11. [Onde ficam as saídas](#11-onde-ficam-as-saídas)
12. [Custo e tempo por nível](#12-custo-e-tempo-por-nível)
13. [Solução de problemas](#13-solução-de-problemas)

## 1. O jeito mais simples: pedir ao Claude Code

Você não precisa digitar comandos. Crie uma pasta vazia, abra no Visual Studio Code (**File > Open Folder**), abra o painel do Claude Code (ou o OpenCode, na configuração (b) dos [Primeiros passos](getting-started.pt-BR.md#2-qual-ia-agêntica-usar)) e cole uma das instruções abaixo. A IA agêntica clona o repositório, lê este guia, instala o que falta, roda os comandos e conta o resultado. Ele pede a sua permissão antes de rodar cada comando, então o controle continua com você.

**Rodar o Nível 3 no tema de exemplo** (alguns minutos, alguns centavos de OpenRouter):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, leia docs/run-the-benchmark.pt-BR.md e rode o Nível 3 no tema a04. Quando terminar, diga quantos artigos ele entregou e abra a rodada no visualizador.
```

**Reproduzir o relatório da aula a partir das avaliações que vêm no repositório** (nenhuma chamada de IA, custo zero):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, leia docs/run-the-benchmark.pt-BR.md e reproduza o relatório da aula a partir das avaliações que vêm no repositório, com python -m evaluation.report class. Não rode nenhum agente nem juiz. Depois me mostre a precisão de cada nível pelo júri, com os intervalos de 95%.
```

**Rodar o benchmark inteiro** (muitas horas, cerca de US$ 33 de OpenRouter, mais o executor: o seu plano do Claude, ou tokens no OpenRouter se o Claude Code estiver apontado para o OpenRouter):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, leia docs/run-the-benchmark.pt-BR.md e rode o benchmark inteiro com a tag mytest: os quatro níveis nos seis temas, duas repetições cada. Depois avalie cada rodada com os três juízes, rode o júri e gere o relatório e a estatística. Antes de começar, me diga o custo e o tempo esperados e espere a minha confirmação.
```

## 2. Nomes que você vai ver

| Nome | Significado |
| --- | --- |
| **Nível 0** (`n0`) | uma frase, e mais nada |
| **Nível 1** (`n1`) | um agente, sem conferência; as quatro camadas descritas (perfil, memória, planejamento, ação) |
| **Nível 2** (`n2`) | multiagente, com conferência: um verificador confere cada passo |
| **Nível 3** (`n3`) | multiagente com conferência, mais código: código onde dá, IA com conferência onde precisa |
| **rodada** | um nível num tema, uma vez |
| **tag** | um nome que você escolhe para um grupo de rodadas, por exemplo `mytest`; as rodadas da aula usam `class` |
| **id da rodada** | `<tag>-<nível>-<tema>-r<repetição>`, por exemplo `class-n3-a04-r1` |

Toda rodada pede a mesma coisa: 25 artigos empíricos de periódico, revisados por pares, sobre um tema estreito, publicados de 2018 a 2025, e, para cada um, DOI, título, autores, ano, periódico, tipo de estudo e método, tamanho da amostra como aparece no resumo, achado principal numa frase e um trecho literal do resumo.

Os seis temas, em `benchmark/topics.json`:

| Id | Tema |
| --- | --- |
| `a04` | jogos contra a desinformação, como o Bad News (**o tema de exemplo**) |
| `a01` | influência continuada da informação falsa |
| `a02` | agências de checagem brasileiras |
| `a03` | educação midiática na escola e na universidade |
| `a05` | percepção de imagens, vídeos e áudios feitos por IA |
| `a06` | manchetes caça-cliques |

Todos os comandos abaixo rodam no PowerShell, a partir da raiz do repositório, com o ambiente ativo (`.venv\Scripts\activate`).

## 3. Uma rodada

```powershell
python -m benchmark.run --level n3 --topic a04 --tag mytest --rep 1
```

| Opção | O que define |
| --- | --- |
| `--level` | `n0`, `n1`, `n2` ou `n3` |
| `--topic` | `a01` a `a06` |
| `--tag` | o nome do seu grupo de rodadas |
| `--rep` | o número da repetição; use outro número para rodar o mesmo nível no mesmo tema de novo sem sobrescrever |

O comando mostra o id da rodada quando termina, aqui `mytest-n3-a04-r1`, e a rodada fica em `agents/level_3/runs/mytest-n3-a04-r1/`. Enquanto ela roda, dá para acompanhar ao vivo no visualizador (seção 9).

### Como é uma primeira rodada

Este é o caminho de quem chega agora, percorrido de ponta a ponta a partir de um clone novo deste repositório, no Windows 11 com Python 3.13:

| Passo | Comando | O que você deve ver |
| --- | --- | --- |
| Instalar | `pip install -r requirements.txt` | alguns minutos; nenhum erro |
| Conferir a instalação sem custo | `python -m evaluation.report class` | a tabela da aula: Nível 3 com 97% pelo júri |
| Uma rodada do Nível 3 no tema de exemplo | `python -m benchmark.run --level n3 --topic a04 --tag mytest --rep 1` | de 5 a 8 minutos; mostra `mytest-n3-a04-r1`; o `final.json` tem `"status": "done"` e cerca de 20 artigos |
| Avaliar com os três juízes | `python -m evaluation.evaluate --judge deepseek --prefix mytest` (depois `qwen` e `gemini`; os três podem rodar ao mesmo tempo, em três terminais) | alguns minutos cada; uma linha por rodada, com artigos entregues e corretos |
| Juntar os três | `python -m evaluation.jury mytest` | `jury: 1 runs, ... articles` |
| Ler o resultado | `python -m evaluation.report mytest` | `evaluation/REPORT_mytest.md`, com precisão, tempo, custo e certos, errados e não entregues |

Nessa conferência de ponta a ponta, o Nível 3 no tema a04 entregou 20 artigos em 7,1 minutos, com 6 chamadas de IA e todos os passos de IA aprovados na primeira tentativa; o júri julgou 20 de 20 corretos e o juiz único, 19 de 20; o verificador e os três juízes custaram US$ 0,67 na OpenRouter. Com um nível e um tema, o relatório não mostra intervalo nem comparação entre níveis: isso exige rodadas de pelo menos dois níveis em pelo menos dois temas.

## 4. Um lote de rodadas

```powershell
python -m benchmark.bench --topics a01,a02,a03,a04,a05,a06 --levels n0,n1,n2,n3 --reps 2 --tag mytest --workers 4
```

Este é o benchmark inteiro: 4 níveis x 6 temas x 2 repetições = 48 rodadas.

- Cada rodada roda no seu próprio processo, então uma falha não derruba as outras.
- `--workers 4` roda quatro ao mesmo tempo. Os níveis mais longos começam primeiro.
- Uma rodada que termina em `error` é tentada mais uma vez. Rodadas que já terminaram como `done`, `paused` ou `failed` ficam como estão.
- Por isso dá para parar o lote e rodar o mesmo comando de novo: ele continua do que falta.

Para testar um lote menor, use menos temas, níveis ou repetições, por exemplo `--topics a04 --levels n0,n3 --reps 1`.

## 5. Avaliação com os três juízes

Cada juiz avalia todas as rodadas cujo id começa com a sua tag:

```powershell
python -m evaluation.evaluate --judge deepseek --prefix mytest
python -m evaluation.evaluate --judge qwen --prefix mytest
python -m evaluation.evaluate --judge gemini --prefix mytest
```

Para cada artigo que uma rodada entregou, a avaliação faz dois tipos de conferência.

**Conferência por código (dado duro).** O DOI existe; título, autor, ano e periódico batem com o registro oficial; o artigo está no período pedido e é artigo de periódico; o trecho e a amostra estão no resumo. Para achar o resumo, o avaliador também consulta fontes que o Nível 3 não usa (Semantic Scholar e a página da editora), então o Nível 3 não é conferido só contra as próprias fontes.

**Conferência pelo juiz (o que exige leitura).** O juiz, cego ao nível, lê o resumo e decide quatro critérios: o artigo é do tema, é empírico, o método é o que foi dito, e o resumo sustenta o achado declarado.

Um artigo só conta como certo quando passa em todas as conferências. Um campo errado e o artigo inteiro conta como erro.

Os três juízes são DeepSeek V4 Pro (`deepseek`), Qwen3.7 Plus (`qwen`) e Gemini 3.1 Flash-Lite (`gemini`), chamados pelo OpenRouter. Cada um grava um arquivo por rodada em `agents/level_N/evaluations/judge-<nome>/`. As respostas dos juízes ficam salvas em disco, então avaliar a mesma rodada de novo não paga de novo.

## 6. O júri

```powershell
python -m evaluation.jury mytest
```

O júri é a medida principal. Para cada artigo, ele toma a maioria dos três juízes em cada critério, separadamente. Um artigo está certo quando passa nas conferências por código e o júri aprova. O júri só cobre rodadas que os três juízes avaliaram, e grava um arquivo por rodada em `agents/level_N/evaluations/jury/`.

Por que três empresas: um modelo tende a favorecer respostas parecidas com as suas. O executor (Claude) e o verificador (GLM) vêm de duas empresas, e os três juízes, de outras três. O **DeepSeek V4 Pro sozinho** é o juiz único, mantido para comparação: mesmos critérios, mesmas rodadas.

## 7. Relatório e estatística

```powershell
python -m evaluation.report mytest
python -m evaluation.stats mytest
```

O **`report`** calcula, por nível:

- a **precisão**, a métrica principal: dos artigos entregues, quantos estão 100% certos;
- o **intervalo de 95%** de cada média;
- o **custo**: tempo, chamadas de IA, tokens e custo por rodada;
- o **desfecho**: certos, errados e não entregues, dos 25 artigos pedidos.

O **`stats`** roda o teste por artigo.

O racional estatístico tem três passos:

1. **Média por tema.** Cada tema é uma unidade: as duas rodadas de um nível num tema viram uma média.
2. **Faixa provável (intervalo de 95%).** t de Student com 5 graus de liberdade (6 temas menos 1), a escolha conservadora para poucos grupos (Cameron e Miller 2015, seção VI).
3. **Teste por artigo.** Uma regressão logística do acerto sobre nível e tema, com erros agrupados por rodada (os artigos da mesma rodada formam um grupo), valores críticos t e a correção de Holm para as várias comparações.

Os resultados da aula, em `evaluation/REPORT.md` e `evaluation/STATISTICS.md`, foram gerados por esses dois comandos com a tag `class`.

## 8. Reproduzir os números da aula

```powershell
python -m evaluation.report class
```

As avaliações das 48 rodadas da aula vêm no repositório, então este comando recalcula cada número da aula a partir desses arquivos. Ele não faz nenhuma chamada de IA e não custa nada. Você deve ver:

| Nível | Precisão, júri | Intervalo de 95% | Precisão, juiz único | Intervalo de 95% |
| --- | --- | --- | --- | --- |
| 0 | 82% | 68 a 97% | 79% | 66 a 92% |
| 1 | 89% | 83 a 96% | 86% | 77 a 94% |
| 2 | 90% | 78 a 100% | 86% | 77 a 95% |
| 3 | 97% | 94 a 100% | 94% | 88 a 100% |

Rode `python -m evaluation.stats class` para reproduzir o teste por artigo: o Nível 3 supera o Nível 0 com segurança estatística (p de Holm 0,001) e também supera os Níveis 1 e 2, com sinal mais tímido (p de Holm por volta de 0,06, pouco acima do corte usual de 5%).

## 9. Acompanhar uma rodada no visualizador

O visualizador é uma página web que desenha uma rodada passo a passo: cada chamada de IA, cada busca, cada parecer do verificador e a entrega. Suba um pequeno servidor web local na raiz do repositório:

```powershell
python -m http.server 8000
```

Deixe esse terminal aberto e, no Google Chrome, abra um destes endereços.

**Replay de uma rodada terminada:**

```text
http://127.0.0.1:8000/viewer/index.html?run=class-n3-a04-r1&replay=1
```

O replay toca os eventos reais da rodada numa velocidade maior, e o relógio mostra o tempo real. Acrescente `&speed=20` ao endereço para tocar 20 vezes mais rápido.

**Ao vivo:** comece uma rodada em outro terminal e abra o mesmo endereço sem `&replay=1`, com o id da sua rodada:

```text
http://127.0.0.1:8000/viewer/index.html?run=mytest-n3-a04-r1
```

A página lê o registro da rodada várias vezes por segundo e desenha cada evento conforme ele acontece.

Para parar o servidor, volte ao terminal dele e aperte Ctrl+C.

## 10. Gravar um vídeo de replay

```powershell
python -m benchmark.record_replay class-n3-a04-r1 --speed 20 --cap 0.8 --hold 6
```

O comando serve o projeto numa porta local, abre o visualizador em modo replay no Google Chrome sem janela, em 1920 x 1080, grava até o replay acabar e escreve um vídeo `.mp4` e uma capa `.jpg` (um quadro perto do fim). Ao terminar, mostra o caminho do vídeo. Precisa do Google Chrome e do ffmpeg.

| Opção | O que define |
| --- | --- |
| `--speed 20` | cada evento toca no seu tempo real dividido por 20 |
| `--cap 0.8` | uma pausa maior que 0,8 segundo na tela é encurtada para 0,8 segundo |
| `--hold 6` | cada parecer do verificador fica 6 segundos na tela, para dar tempo de ler |

Os vídeos da aula estão em `agents/level_N/media/`, de `level-0.mp4` a `level-3.mp4`: rodadas reais do tema de exemplo (a04, repetição 1), gravadas com essas opções, cada uma terminando na entrega.

## 11. Onde ficam as saídas

Cada nível mora na sua própria pasta, `agents/level_N/`, com o seu código, as suas instruções, as suas rodadas e as avaliações delas. O Nível 0 é `agents/level_0/`, o Nível 3 é `agents/level_3/`.

**Uma rodada:** `agents/level_N/runs/<run_id>/`

| Arquivo | Conteúdo |
| --- | --- |
| `events.jsonl` | cada evento da rodada, um por linha, gravado conforme acontece (o visualizador lê este arquivo) |
| `final.json` | a lista de artigos entregue e o status da rodada |
| `meta.json` | status, tempo total, chamadas de IA e tokens, por papel e por provedor |
| `calls/` | cada instrução enviada a uma IA e cada resposta que ela deu |

**Uma avaliação:** `agents/level_N/evaluations/<juiz>/<run_id>.json`, onde `<juiz>` é `judge-deepseek`, `judge-qwen`, `judge-gemini` ou `jury`.

**O status de uma rodada:**

| Status | Significado |
| --- | --- |
| `done` | a rodada entregou a sua lista |
| `paused` | Níveis 2 e 3: o verificador recusou a quinta tentativa de um passo, então a rodada não entregou relatório |
| `failed` | a rodada terminou sem lista para entregar, por exemplo quando o Nível 3 encontra candidatos de menos depois dos filtros |
| `error` | o programa parou por um problema inesperado, como a rede ou o limite de uso do seu plano do Claude; um lote tenta mais uma vez |

Uma rodada pausada é um resultado real, não uma pane: é o preço da conferência. Na aula, 3 das 12 rodadas do Nível 2 pausaram, e nenhuma rodada dos outros níveis.

## 12. Custo e tempo por nível

Média por rodada na aula (12 rodadas por nível). Certos, errados e não entregues são dos 25 artigos pedidos, pelo júri.

| Nível | Tempo | Chamadas de IA | Tokens | Custo por rodada | Certos | Errados | Não entregues | Rodadas pausadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10,2 min | 1,0 | 2,2 mi | R$ 7,11 | 80% | 17% | 3% | 0 de 12 |
| 1 | 17,0 min | 1,0 | 4,2 mi | R$ 9,84 | 82% | 10% | 8% | 0 de 12 |
| 2 | 42,1 min | 9,9 | 5,9 mi | R$ 16,33 | 59% | 8% | 33% | 3 de 12 |
| 3 | 5,1 min | 7,0 | 146 mil | R$ 2,90 | 81% | 2% | 17% | 0 de 12 |

Como ler a coluna de custo: é o Claude Sonnet 5.5 a preço público de API da Anthropic (tokens e buscas na web) mais o verificador pelo valor que o OpenRouter cobrou, convertido pela PTAX de venda do Banco Central de 14/10/2026, US$ 1 = R$ 5,0441. Ela mostra o custo de cada arquitetura de um jeito comparável.

O que você paga de fato:

- **O executor** é o Claude Code. Com login numa assinatura do Claude, ele consome o uso do seu plano, não dinheiro por token. Apontado para o OpenRouter, ele é pago por token com os seus créditos do OpenRouter, e a coluna de custo acima serve de referência para isso, a preço público de API da Anthropic.
- **O OpenRouter** paga o verificador (Níveis 2 e 3) e os três juízes. Uma rodada sozinha custa centavos. O benchmark inteiro, com a avaliação, gastou cerca de **US$ 33,38 (cerca de R$ 170)**.

Ou seja, o teste inteiro da aula custou uma assinatura do Claude Code mais cerca de R$ 170 em tokens no OpenRouter.

Sobre o tempo: o Nível 3 é o mais rápido, cerca de 5 minutos por rodada, porque o código faz a busca, os filtros e as referências. O Nível 2 é o mais lento, cerca de 42 minutos, porque cada passo pode ir e voltar com o verificador até 5 vezes. O lote inteiro de 48 rodadas leva várias horas, mesmo com quatro workers.

## 13. Solução de problemas

**"Chave não encontrada", ou um erro que cita `OPENROUTER_API_KEY`, `OPENALEX_API_KEY` ou `BRAVE_API_KEY`.**
O terminal estava aberto antes de você guardar a chave. Feche todos os terminais e o Visual Studio Code, abra de novo e confira com `if ($env:OPENROUTER_API_KEY) { 'ok' } else { 'missing' }` (o mesmo para as outras duas). Se aparecer `missing`, guarde a chave de novo como mostram os [Primeiros passos](getting-started.pt-BR.md#4-openrouter-uma-chave-para-várias-empresas-de-ia). Um HTTP 401 do OpenRouter quer dizer chave errada ou apagada; um HTTP 402 quer dizer que os créditos do OpenRouter acabaram.

**"claude.exe from the VS Code extension not found", ou o Claude Code está sem login.**
O código usa o `claude.exe` que vem com a extensão Claude Code do Visual Studio Code, nas duas configurações recomendadas. Instale a extensão (veja os [Primeiros passos](getting-started.pt-BR.md#3-instalar-o-claude-code-do-zero)) e depois entre com um plano pago do Claude ou aponte o Claude Code para o OpenRouter (nesse caso, `/status` tem que mostrar a URL base `https://openrouter.ai/api`). Mande uma mensagem para confirmar que ele responde. Depois rode de novo.

**O limite de uso do seu plano do Claude acabou (só com assinatura do Claude).**
A rodada para com `error`. Espere o limite do plano renovar e rode o mesmo comando `benchmark.bench` de novo: as rodadas terminadas ficam e só as que faltam rodam. Menos `--workers` espalham o uso por mais tempo.

**Limite de requisições do OpenAlex (HTTP 429).**
O OpenAlex limita quantas requisições uma chave faz por dia. Primeiro confirme que a `OPENALEX_API_KEY` está guardada: sem ela, o limite é bem menor. Se a cota do dia acabou, esperar alguns segundos não resolve: espere a cota renovar e rode de novo. As respostas do OpenAlex e do Crossref ficam salvas em disco, então uma rodada que repete uma consulta não gasta a cota de novo.

**Uma rodada terminou como `paused`.**
É um desfecho normal dos Níveis 2 e 3: o verificador recusou a quinta tentativa de um passo. Para ver o motivo, abra a rodada no visualizador (o último parecer fica na tela) ou leia os últimos eventos de `events.jsonl`. Para tentar de novo, rode o mesmo nível e tema com outro número de `--rep`.

**O PowerShell diz que a execução de scripts está desabilitada.**
Rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` uma vez e ative o ambiente de novo.

**O `python` abre a Microsoft Store.**
Use `py -3.13` no lugar de `python`.

Ainda travado? Cole a mensagem de erro no Claude Code, na pasta do repositório, e peça que ele leia este guia e resolva o problema. Ou escreva para bruno@abajur.ai.
