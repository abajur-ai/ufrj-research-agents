[Read in English](STATISTICS.md)

# Estatística das rodadas `class`

Regressão logística por artigo (acerto ~ nível + tema), erro-padrão agrupado por rodada, valores críticos t com G - 1 graus de liberdade (Cameron e Miller 2015, seção VI); correção de Holm sobre as cinco comparações de cada bloco (Holm 1979). Gerado por `python -m evaluation.stats`.

## Júri de três empresas, maioria por critério (medida principal)

1020 artigos, 45 rodadas com relatório, 6 temas. Precisão média por nível: Nível 0 82%, Nível 1 89%, Nível 2 90%, Nível 3 97%.

| Comparação | Razão de chances | p | p Holm |
| --- | --- | --- | --- |
| Nível 1 contra Nível 0 | 1.81 | 0.1289 | 0.2577 |
| Nível 2 contra Nível 1 | 0.76 | 0.6435 | 0.6435 |
| Nível 3 contra Nível 2 | 5.47 | 0.0175 | 0.0632 |
| Nível 3 contra Nível 1 | 4.14 | 0.0158 | 0.0632 |
| Nível 3 contra Nível 0 | 7.52 | 0.0003 | 0.0013 |

## Juiz único (DeepSeek V4 Pro), para comparar

1020 artigos, 45 rodadas com relatório, 6 temas. Precisão média por nível: Nível 0 79%, Nível 1 86%, Nível 2 86%, Nível 3 94%.

| Comparação | Razão de chances | p | p Holm |
| --- | --- | --- | --- |
| Nível 1 contra Nível 0 | 1.62 | 0.0262 | 0.0673 |
| Nível 2 contra Nível 1 | 0.78 | 0.5706 | 0.5706 |
| Nível 3 contra Nível 2 | 3.14 | 0.0224 | 0.0673 |
| Nível 3 contra Nível 1 | 2.45 | 0.0126 | 0.0506 |
| Nível 3 contra Nível 0 | 3.96 | 0.0000 | 0.0002 |

## Só o que o código confere (sem juiz)

1020 artigos, 45 rodadas com relatório, 6 temas. Precisão média por nível: Nível 0 92%, Nível 1 95%, Nível 2 98%, Nível 3 99%.

| Comparação | Razão de chances | p | p Holm |
| --- | --- | --- | --- |
| Nível 1 contra Nível 0 | 1.91 | 0.0628 | 0.2512 |
| Nível 2 contra Nível 1 | 1.54 | 0.3585 | 0.5098 |
| Nível 3 contra Nível 2 | 3.95 | 0.2549 | 0.5098 |
| Nível 3 contra Nível 1 | 6.09 | 0.1098 | 0.3295 |
| Nível 3 contra Nível 0 | 11.63 | 0.0274 | 0.1370 |

