[Read in English](README.md)

# Nível 1: um agente, sem conferência

**As quatro camadas descritas.** Um agente, com perfil, memória, planejamento e ação escritos na instrução. Ele busca e
lê sozinho, guiado pelas quatro camadas. Ninguém confere o que ele entrega.

Este README tem duas partes. A parte 1 é para quem pesquisa. A parte 2, [Para agentes de IA](#parte-2-para-agentes-de-ia),
é para um agente de IA de programação que vai rodar, testar, depurar ou alterar este nível.

# Parte 1: para quem pesquisa

## O que é este nível

O Nível 1 é a segunda das quatro arquiteturas comparadas no benchmark da aula. Ele tem o mesmo agente único, o mesmo
modelo e as mesmas ferramentas do Nível 0. A única diferença é a instrução: em vez de uma frase, ela descreve as
quatro camadas de um agente (Wang et al. 2024) e o que o agente faz em cada uma.

A instrução abre com uma prioridade que o Nível 0 nunca declara: "Prefira entregar menos itens certos do que itens
duvidosos".

## Como funciona, passo a passo

1. O agente recebe a instrução das quatro camadas, o pedido e o formato padrão da resposta.
2. Transforma o pedido em critérios de inclusão: tema, período, tipo de publicação, método, recorte geográfico ou de
   plataforma.
3. Busca em bases acadêmicas e na web, em inglês e em português: a API do OpenAlex, o Crossref, o SciELO e a busca na
   web.
4. Para cada candidato, abre o registro oficial (página do DOI, do periódico ou do OpenAlex) e confere título,
   autores, ano, periódico e tipo de publicação.
5. Lê o resumo, confere cada critério e descarta o que não atende a todos.
6. Copia do resumo o trecho literal que sustenta o achado principal e o tamanho da amostra tal como aparece.
7. Entrega a lista final, só com itens conferidos. Ninguém confere a lista.

Tudo isso acontece dentro de uma única chamada de IA: o agente decide quantas buscas e páginas precisa.

Quem faz cada tarefa (página 22 do deck, coluna do Nível 1):

| Tarefa | Nível 1 |
| --- | --- |
| Decidir o que procurar | IA |
| Buscar os artigos | IA |
| Conferir DOI, ano e tipo | IA |
| Ver se o artigo atende ao pedido | IA |
| Extrair método, amostra e achado | IA |
| Conferir o trecho no resumo | Ninguém |
| Montar a referência | IA |

## As quatro camadas neste nível

Página 19 do deck, como está escrito em `prompts/level_1.md`:

| Camada | No Nível 1 |
| --- | --- |
| Perfil | Quem o agente é e o que ele prioriza. Um assistente que apoia uma revisão de literatura. Prefere entregar menos a entregar errado. |
| Memória | O que ele anota enquanto trabalha. Uma ficha para cada artigo que encontra: onde conferiu cada dado e o que decidiu. |
| Planejamento | Os passos, em ordem, até a entrega. Transforma o pedido em critérios e busca nas bases acadêmicas. Lê cada resumo e descarta o que não atende. Ao fim, consolida e entrega o relatório, só com o que conferiu. |
| Ação | O que ele pode usar e as regras de uso. Busca na web e abre as páginas dos artigos. O que não consegue conferir fica de fora. |

## O que recebe, como busca e lê, quem confere

- **Recebe:** instruções das quatro camadas e o pedido.
- **Busca e lê:** sozinho, guiado pelas quatro camadas.
- **Quem confere:** ninguém confere o que ele entrega.

## Resultados

O benchmark da aula: 4 níveis x 6 temas x 2 repetições = 48 rodadas, 12 por nível. Cada rodada pede 25 artigos
empíricos de periódico, revisados por pares, publicados de 2018 a 2025, com 9 campos cada. O executor é o mesmo em
todos os níveis (Claude Sonnet 5.5); só muda a arquitetura.

**Precisão** é a métrica principal: dos artigos entregues, quantos estão 100% certos. Um campo errado e o artigo
inteiro conta como erro. Média dos 6 temas, com o intervalo de 95% (t de Student sobre os temas):

| Nível | Júri (principal) | Intervalo de 95% | Juiz único | Intervalo de 95% | Só checagens por código |
| --- | --- | --- | --- | --- | --- |
| 0 | 82% | 68 a 97% | 79% | 66 a 92% | 92% |
| **1** | **89%** | **83 a 96%** | **86%** | **77 a 94%** | **95%** |
| 2 | 90% | 78 a 100% | 86% | 77 a 95% | 98% |
| 3 | 97% | 94 a 100% | 94% | 88 a 100% | 99% |

O júri são três juízes de IA de três empresas (DeepSeek V4 Pro, Qwen3.7 Plus, Gemini 3.1 Flash-Lite), cegos ao
nível, que decidem por maioria em cada critério. O juiz único é o DeepSeek V4 Pro sozinho, nas mesmas rodadas.

**Custo e resultado**, média por rodada. Certos, errados e não entregues são parcelas dos 25 artigos pedidos, pelo júri; a precisão é a parcela dos artigos entregues que está 100% certa:

| Nível | Tempo | Chamadas de IA | Tokens | Custo por rodada | Certos | Errados | Não entregues | Precisão (dos entregues) | Rodadas pausadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10,2 min | 1,0 | 2,2 mi | R$ 7,11 | 80% | 17% | 3% | 82% | 0 de 12 |
| **1** | **17,0 min** | **1,0** | **4,2 mi** | **R$ 9,84** | **82%** | **10%** | **8%** | **89%** | **0 de 12** |
| 2 | 42,1 min | 9,9 | 5,9 mi | R$ 16,33 | 59% | 8% | 33% | 90% | 3 de 12 |
| 3 | 5,1 min | 7,0 | 146 mil | R$ 2,90 | 81% | 2% | 17% | 97% | 0 de 12 |

Custo por rodada: Claude Sonnet 5.5 a preço de API pública da Anthropic (tokens e buscas na web), convertido pela PTAX
de venda do Banco Central de 14/10/2026, US$ 1 = R$ 5,0441. O Nível 1 não tem verificador.

**Como se compara.** Descrever bem o agente já ajuda muito: em relação ao Nível 0, a precisão sobe de 82% para 89% e
os errados caem de 17% para 10%. O Nível 1 chega à mesma precisão do Nível 2 (89% contra 90%) em 17 min, não 42, por
R$ 9,84, não R$ 16,33; o Nível 3 é mais preciso (97%), mais rápido e mais barato.

## Veja rodando

Uma rodada real do tema de exemplo (a04, jogos contra a desinformação, como o Bad News), repetição 1, reproduzida em
20x e terminando na entrega.

[![Rodada do Nível 1 no tema de exemplo](media/level-1.jpg)](media/level-1.mp4)

Música: "Deliberate Thought", Kevin MacLeod (incompetech.com), CC BY 4.0.

## Quando usar este nível

Use o Nível 1 quando tudo o que você tem é um chat ou um agente com busca na web, sem verificador nem código: escrever
as quatro camadas é a melhoria mais barata em relação à instrução de uma frase. Ele serve para uma primeira passada,
exploratória. Ninguém confere a lista, e 10% dos artigos pedidos voltaram errados.

O human in the loop continua valendo: o agente acelera, quem pesquisa decide. Confira na fonte original cada artigo
que você vai citar.

## Rodar só este nível

A preparação (Python, Claude Code) está no [README do repositório](../../README.pt-BR.md). Rodar o Nível 1 exige só o
Claude Code com login feito; avaliar exige `OPENROUTER_API_KEY` e `OPENALEX_API_KEY`. Na raiz do repositório, no
PowerShell:

```
python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1
```

A rodada fica em `agents/level_1/runs/mytest-n1-a04-r1/`. Para assistir, rode `python -m http.server 8000` e abra
`http://127.0.0.1:8000/viewer/index.html?run=mytest-n1-a04-r1&replay=1`.

## O que você pode editar

`prompts/level_1.md`, em português, em texto simples, com uma seção por camada (Perfil, Memória, Planejamento, Ação).
Mude uma regra, acrescente uma base, aperte um critério e rode de novo.

# Parte 2: para agentes de IA

## Arquivos deste nível

| Caminho | O que faz |
| --- | --- |
| `agent.py` | O agente do Nível 1. Ponto de entrada: `run(topic, run_dir, log)`, uma corrotina aguardada por `benchmark/run.py`. `topic` é uma entrada de `benchmark/topics.json`, `run_dir` a pasta da rodada, `log` o registro de eventos de `core/`. Uma chamada do executor: prompt de sistema `prompts/level_1.md`, prompt do usuário o pedido do tema mais o bloco de formato compartilhado, ferramentas `WebSearch` e `WebFetch`, saída estruturada no esquema final. |
| `prompts/level_1.md` | O prompt de sistema: as quatro camadas. Em português. |
| `runs/class-n1-<topic>-r<rep>/` | As 12 rodadas da aula: `events.jsonl`, `final.json`, `meta.json`, `calls/`. |
| `evaluations/judge-deepseek/` | Um arquivo por rodada: checagens por código mais os pareceres do DeepSeek V4 Pro. |
| `evaluations/judge-qwen/` | O mesmo, Qwen3.7 Plus. |
| `evaluations/judge-gemini/` | O mesmo, Gemini 3.1 Flash-Lite. |
| `evaluations/jury/` | Maioria dos três juízes em cada critério; a medida principal. |
| `media/level-1.mp4`, `media/level-1.jpg` | Vídeo de `class-n1-a04-r1` reproduzido em 20x, e a capa. |

## Módulos compartilhados de que depende

| Módulo | Usado para |
| --- | --- |
| `benchmark/common.py` | O esquema final (o item de 9 campos mais `search_notes`), o bloco de formato acrescentado ao pedido, gravação do `final.json`. O mesmo esquema e o mesmo bloco servem ao Nível 0, então os dois níveis só diferem no prompt de sistema. |
| `core/` | Chamada do executor pelo Claude Agent SDK (Claude Sonnet 5.5, esforço alto, o `claude.exe` da extensão do Claude Code no VS Code), o registro de eventos, a configuração. |

O Nível 1 não usa `benchmark/qa.py`, `benchmark/verifier.py` nem `benchmark/scholar.py` durante a rodada. O avaliador
usa `benchmark/scholar.py` para conferir as referências dele.

## Esquema de saída

O executor responde `{"items": [...], "search_notes": "..."}`. O `final.json` contém `status`, `report.items` (ou
`null`), `notes` (as notas de busca) e `errors` (até 3). Cada item tem os 9 campos do pedido (tipo de estudo e método
são duas chaves), todos escritos pelo agente:

| Chave | Conteúdo |
| --- | --- |
| `doi` | Só o DOI, por exemplo `10.1000/xyz123` |
| `title` | Título |
| `authors` | Lista de nomes |
| `year` | Número inteiro |
| `venue` | Periódico |
| `study_type` | Tipo de estudo |
| `method` | Método |
| `sample_size` | Amostra como aparece no resumo, ou `não informado no resumo` |
| `main_finding` | Achado principal em uma frase |
| `abstract_quote` | Trecho literal do resumo |

## Ferramentas

`WebSearch` e `WebFetch` (Claude Agent SDK). O agente pode chamar qualquer API pública pelo `WebFetch`; o prompt aponta
as APIs do OpenAlex e do Crossref, o SciELO e a busca na web.

## Limites e constantes

- 25 artigos pedidos por rodada.
- Uma chamada de IA, no máximo 215 turnos (90 + 5 x 25) e 4.950 s (2.700 + 90 x 25).
- Sem verificador, sem checagem por código, sem novas tentativas.

## Status da rodada

| Status | Significado |
| --- | --- |
| `done` | O agente devolveu uma resposta estruturada válida; o `final.json` tem os itens. |
| `paused` | Não ocorre neste nível (não há verificador). |
| `failed` | Nenhuma resposta estruturada válida (limite de turnos, tempo esgotado ou saída malformada); o `final.json` tem `errors`. |
| `error` | Uma exceção; o `events.jsonl` termina com `run_error` e o `meta.json` registra `error`. |

## Como rodar

```
python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1
```

Ids dos temas: `a01` a `a06` (`a04` é o tema de exemplo). Id da rodada: `<tag>-n1-<topic>-r<rep>`.

## Como avaliar só as rodadas deste nível

```
python -m evaluation.evaluate --judge deepseek --prefix mytest-n1
python -m evaluation.evaluate --judge qwen --prefix mytest-n1
python -m evaluation.evaluate --judge gemini --prefix mytest-n1
python -m evaluation.jury mytest
python -m evaluation.report mytest
```

O prefixo seleciona as rodadas. `jury` e `report` recebem a tag e cobrem toda rodada dessa tag que tem avaliações; se
você rodou só o Nível 1, só o Nível 1 aparece. `python -m evaluation.report class` reproduz os números da aula a partir
das avaliações que vêm no repositório.

## Como depurar

1. Abra `runs/<run_id>/meta.json`: status, tempo total, chamadas de IA e tokens.
2. Leia `runs/<run_id>/events.jsonl` em ordem: `run_start`, `step_start`, `ai_call_start`, `ai_tool` (cada busca e
   página que o agente abriu), `ai_call_end` (tokens, erros), `step_end` (número de itens), `run_error`, `run_end`.
3. Abra `runs/<run_id>/calls/`: `.system.md` (o prompt), `.user.md` (pedido mais bloco de formato) e `.result.json`
   (resposta estruturada, uso, erros) da chamada única.
4. Reproduza a rodada: `python -m http.server 8000` e depois
   `http://127.0.0.1:8000/viewer/index.html?run=<run_id>&replay=1`.

## Checklist antes de alterar um prompt

- [ ] Mantenha o esquema de saída: o bloco de formato em `benchmark/common.py` pede o item de 9 campos; não o contradiga
      no prompt.
- [ ] Mantenha as quatro seções (Perfil, Memória, Planejamento, Ação), para o nível continuar sendo o que a aula descreve.
- [ ] Rode de novo no tema de exemplo: `python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1` (e `--rep 2`).
- [ ] Avalie com os três juízes, depois `jury` e `report`.
- [ ] Compare com as rodadas da aula que vêm no repositório, `class-n1-a04-r1` e `class-n1-a04-r2`: precisão, certos,
      errados, não entregues, tempo e tokens.
