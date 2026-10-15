[Read in English](REPORT.md)

# Resultados das rodadas `class`

Rodadas: 48. Níveis: 4. Temas: 6. 25 artigos pedidos por rodada. Gerado por `python -m evaluation.report`.

## Precisão: dos artigos entregues, quantos estão 100% certos

Média dos temas, com o intervalo de 95% (t de Student sobre os temas).

| Nível | Júri (principal) | Juiz único | Só código |
| --- | --- | --- | --- |
| Nível 0 | 82% (68% a 97%) | 79% (66% a 92%) | 92% |
| Nível 1 | 89% (83% a 96%) | 86% (77% a 94%) | 95% |
| Nível 2 | 90% (78% a 100%) | 86% (77% a 95%) | 98% |
| Nível 3 | 97% (94% a 100%) | 94% (88% a 100%) | 99% |

## Custo e resultado, média por rodada

Certos, errados e não entregues somam 100% dos 25 artigos pedidos, pelo júri.

| Nível | Tempo | Chamadas de IA | Tokens | Custo | Certos | Errados | Não entregues | Rodadas pausadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nível 0 | 10,2 min | 1,0 | 2,2 mi | R$ 7,11 | 80% | 17% | 3% | 0 de 12 |
| Nível 1 | 17,0 min | 1,0 | 4,2 mi | R$ 9,84 | 82% | 10% | 8% | 0 de 12 |
| Nível 2 | 42,1 min | 9,9 | 5,9 mi | R$ 16,33 | 59% | 8% | 33% | 3 de 12 |
| Nível 3 | 5,1 min | 7,0 | 146 mil | R$ 2,90 | 81% | 2% | 17% | 0 de 12 |

Custo: Claude Sonnet 5.5 a preço público da API da Anthropic (tokens e buscas) mais o verificador pelo valor cobrado pela OpenRouter; PTAX de venda de 14/10/2026, US$ 1 = R$ 5,0441. Rodada pausada: o verificador recusou a quinta tentativa de um passo, e a rodada não entregou relatório.

## Diferenças pareadas entre níveis, em pontos (júri)

Por tema, depois intervalo de 95% t de Student sobre os temas.

- Nível 1 sobre o Nível 0: 7,0 (-8,5 a 22,6)
- Nível 2 sobre o Nível 1: 0,6 (-17,6 a 18,8)
- Nível 3 sobre o Nível 2: 7,4 (-2,1 a 17,0)
- Nível 3 sobre o Nível 0: 15,1 (-0,2 a 30,3)
- Nível 3 sobre o Nível 1: 8,0 (0,4 a 15,7)

## Precisão por tema (júri)

| Tema | Nível 0 | Nível 1 | Nível 2 | Nível 3 |
| --- | --- | --- | --- | --- |
| a01 | 94% | 83% | 92% | 100% |
| a02 | 66% | 89% | - | 97% |
| a03 | 64% | 90% | 100% | 100% |
| a04 | 86% | 82% | 92% | 94% |
| a05 | 90% | 98% | 74% | 94% |
| a06 | 94% | 95% | 93% | 100% |

## Por que um artigo entregue não ficou 100% certo (júri; um artigo pode cair em mais de um)

| Motivo | Nível 0 | Nível 1 | Nível 2 | Nível 3 |
| --- | --- | --- | --- | --- |
| DOI inexistente | 5 | 2 | 0 | 0 |
| Erro de dado (título, ano, autor, revista) | 3 | 1 | 1 | 2 |
| Fora do recorte (período, tipo, tema) | 9 | 6 | 0 | 4 |
| Não empírico ou método errado | 9 | 11 | 6 | 3 |
| Citação ou amostra fora do resumo | 16 | 9 | 3 | 0 |
| Achado além do resumo | 1 | 6 | 2 | 2 |
