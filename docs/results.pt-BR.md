[Read in English](results.md)

# Resultados

## Em poucas palavras

O Nível 3 (multiagente com conferência, mais código) é a melhor abordagem em todos os eixos que medimos: a maior
precisão (97% pelo júri), o menor número de artigos errados (2% dos artigos pedidos), o mais rápido (5 minutos por
rodada) e o mais barato (R$ 2,90 por rodada). Descrever bem o agente (Nível 1) já eleva a precisão de 82% para 89%.
Somar uma IA que confere a IA (Nível 2) dá a mesma precisão de um agente bem descrito, 90%, mas leva mais tempo e
custa mais. Quase todo agente acerta o dado duro (DOI, autor, ano, revista); os erros estão no que exige ler o artigo.

Todos os números vêm de 48 rodadas: 4 níveis x 6 temas x 2 repetições, 12 rodadas por nível. Como cada artigo é
julgado está em [evaluation.pt-BR.md](evaluation.pt-BR.md); como os níveis são comparados está em
[statistics.pt-BR.md](statistics.pt-BR.md).

## Precisão por nível

Precisão: dos artigos entregues, a parte que está 100% certa. Média dos seis temas, com o intervalo de 95% (t de
Student sobre os 6 temas). O júri e o juiz único julgaram as mesmas rodadas.

| Nível | Júri (principal) | Intervalo de 95% | Juiz único | Intervalo de 95% |
| --- | --- | --- | --- | --- |
| 0 | 82% | 68 a 97% | 79% | 66 a 92% |
| 1 | 89% | 83 a 96% | 86% | 77 a 94% |
| 2 | 90% | 78 a 100% | 86% | 77 a 95% |
| 3 | 97% | 94 a 100% | 94% | 88 a 100% |

Júri: DeepSeek V4 Pro, Qwen3.7 Plus e Gemini 3.1 Flash-Lite, maioria por critério. Juiz único: DeepSeek V4 Pro
sozinho, com os mesmos critérios.

## Precisão só com as conferências por código

A mesma precisão, contando só o que o código confere (registro, período, tipo de publicação, trecho e amostra no
resumo), sem juiz nenhum:

| Nível | Precisão só pelo código |
| --- | --- |
| 0 | 92% |
| 1 | 95% |
| 2 | 98% |
| 3 | 99% |

A distância entre esta tabela e a anterior é o que só a leitura pega: recorte, método e achado.

## Custo e desfecho por rodada

Média por rodada, 12 rodadas por nível. Certos, errados e não entregues são partes dos 25 artigos pedidos por rodada,
pelo júri, e somam 100%. A precisão é a parte dos artigos entregues que está 100%
certa.

| Nível | Tempo | Chamadas de IA | Tokens | Custo por rodada | Certos | Errados | Não entregues | Precisão (dos entregues) | Rodadas pausadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10,2 min | 1,0 | 2,2 mi | R$ 7,11 | 80% | 17% | 3% | 82% | 0 de 12 |
| 1 | 17,0 min | 1,0 | 4,2 mi | R$ 9,84 | 82% | 10% | 8% | 89% | 0 de 12 |
| 2 | 42,1 min | 9,9 | 5,9 mi | R$ 16,33 | 59% | 8% | 33% | 90% | 3 de 12 |
| 3 | 5,1 min | 7,0 | 146 mil | R$ 2,90 | 81% | 2% | 17% | 97% | 0 de 12 |

Custo por rodada: Claude Sonnet 5.5 pelo preço público da API da Anthropic (tokens e buscas na web) mais o
verificador pelo valor que a OpenRouter cobrou, convertidos pela PTAX de venda do Banco Central de 14/10/2026,
US$ 1 = R$ 5,0441. Uma rodada pausada é aquela em que o verificador recusou a quinta tentativa de um passo, e a rodada
não entregou relatório; os seus 25 artigos contam como não entregues.

O que o teste inteiro custou de fato: uma assinatura do Claude Code (que já existia) mais cerca de R$ 170 em tokens na
OpenRouter (US$ 33,38, verificador e juízes).

## O que o teste mostrou

**1. O Nível 3 é a melhor abordagem: código onde dá, IA com conferência onde precisa.** É o que menos erra: 2% dos
artigos pedidos estão errados, contra 17%, 10% e 8% dos Níveis 0, 1 e 2. É o mais rápido, 5 minutos por rodada, e o
mais barato, R$ 2,90 por rodada. O código faz a busca, o filtro e as referências; a IA só lê e julga, e é conferida. O
código é rápido e barato onde a IA é lenta e cara, e não inventa: quando falha, falha à vista.

**2. Descrever bem o agente já ajuda muito.** Escrever as quatro camadas (perfil, memória, planejamento, ação), e o que
o agente faz em cada uma, supera a instrução de uma frase: a precisão sobe de 82% para 89%, e os errados caem de 17%
para 10% (Nível 1 sobre o Nível 0). Custa só uma instrução melhor.

**3. IA conferindo IA equivale a um agente bem descrito.** Com os modelos de hoje, a precisão é a mesma: 90% no Nível 2
contra 89% no Nível 1. Só que o Nível 2 leva 42 minutos, não 17, e custa R$ 16,33, não R$ 9,84, e 3 das suas 12
rodadas pausaram sem relatório, o que responde pela maior parte dos 33% de artigos pedidos que ele não entregou. Um
conferente vale o que vale aquilo contra o que ele confere; um verificador de IA continua sendo uma IA (Huang et al.,
2024; Stechly, Valmeekam e Kambhampati, 2025). As conferências que fazem diferença são externas e sólidas, como código
contra um registro oficial (Kambhampati et al., 2024), que é o que o Nível 3 acrescenta.

**4. Dado duro, quase todos acertam.** DOI, autor, ano e revista saem quase sempre certos, e por isso a precisão só pelo
código é alta em todos os níveis. O erro está no que exige ler o artigo:

- **Recorte:** é do tema pedido?
- **Método:** é pesquisa com dados, do tipo dito?
- **Achado:** o resumo confirma o que o agente disse?

### Pelo teste estatístico

O Nível 3 supera o Nível 0 em precisão com segurança estatística (p de Holm 0,001). Também supera os Níveis 1 e 2, com
sinal mais tímido (p de Holm cerca de 0,06, pouco acima do corte usual de 5%). Veja
[statistics.pt-BR.md](statistics.pt-BR.md).

## As duas medidas concordam na ordem

O júri e o juiz único dão a mesma classificação. O Nível 3 é o primeiro pelas duas (97% e 94%), o Nível 0 é o último
pelas duas (82% e 79%), e os Níveis 1 e 2 ficam próximos no meio pelas duas (89% e 90% pelo júri, 86% e 86% pelo juiz
único). A precisão só pelo código sobe na mesma ordem, de 92% a 99%. O juiz único é um pouco mais rigoroso em tudo,
então os seus números ficam alguns pontos abaixo, mas nenhuma troca de juiz muda qual arquitetura vence. A ordem é uma
propriedade das arquiteturas, e não do jeito de julgar.

## Onde ficam os arquivos de cada rodada

Cada nível guarda as suas rodadas e as avaliações delas na sua própria pasta:

```
agents/level_N/
  runs/class-nN-<topic>-r<rep>/    events.jsonl, final.json, meta.json, calls/
  evaluations/judge-deepseek/      um arquivo por rodada, juiz único (DeepSeek V4 Pro) + conferências por código
  evaluations/judge-qwen/          o mesmo, Qwen3.7 Plus
  evaluations/judge-gemini/        o mesmo, Gemini 3.1 Flash-Lite
  evaluations/jury/                o júri: maioria dos três, por critério
  media/level-N.mp4                o vídeo do tema de exemplo
```

Os ids das rodadas seguem `class-<level>-<topic>-r<rep>`; por exemplo, `class-n3-a04-r1` é o Nível 3 no tema de
exemplo (jogos contra a desinformação), repetição 1. `final.json` guarda a lista entregue; `meta.json` guarda tempo,
chamadas e tokens; `events.jsonl` é o log de eventos da rodada; `calls/` guarda cada chamada de IA. Qualquer rodada
pode ser reproduzida no visualizador:

```
python -m http.server 8000
```

e depois abra `http://127.0.0.1:8000/viewer/index.html?run=class-n3-a04-r1&replay=1`.

## Como gerar de novo

Na raiz do repositório:

```
python -m evaluation.report class
python -m evaluation.stats class
```

`python -m evaluation.report class` reproduz os números da aula a partir das avaliações que acompanham o repositório e
escreve `evaluation/REPORT.md` (precisão, intervalos, custo, desfecho). `python -m evaluation.stats class` escreve
`evaluation/STATISTICS.md` (o teste por artigo com correção de Holm). Nenhum dos dois comandos chama uma IA: eles leem
as rodadas e os arquivos de avaliação que já estão em `agents/level_N/`.

## Referências deste documento

Huang et al. (2024); Kambhampati et al. (2024); Stechly, Valmeekam e Kambhampati (2025). Entradas completas em
[references.pt-BR.md](references.pt-BR.md).
