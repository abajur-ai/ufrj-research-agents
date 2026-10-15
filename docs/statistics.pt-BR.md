[Read in English](statistics.md)

# Estatística: como os níveis são comparados

## Em poucas palavras

Quarenta e oito rodadas é um teste pequeno, então a estatística foi montada para ser cuidadosa, e não para
impressionar. Ela responde a duas perguntas em três passos.

1. **Média por tema.** Cada tema é uma unidade. As duas rodadas de um nível num tema viram um número só: a precisão
   média delas.
2. **Faixa provável.** Para cada nível, a média dos seis temas vem com um intervalo de 95%: onde a média verdadeira
   deve estar. Com só seis temas, o intervalo é alargado de propósito.
3. **Teste por artigo.** Para saber se um nível supera mesmo outro, cada artigo entregue conta. Os artigos da mesma
   rodada são tratados como um grupo, porque compartilham a mesma busca e as mesmas decisões. Uma correção (Holm)
   desconta o fato de fazer várias comparações de uma vez.

O resultado, em precisão, pelo júri: **o Nível 3 supera o Nível 0 com segurança estatística (p de Holm 0,001). Também
supera os Níveis 1 e 2, com sinal mais tímido (p de Holm cerca de 0,06, pouco acima do corte usual de 5%).**

As métricas e os critérios de julgamento foram fixados antes das rodadas. A análise estatística abaixo é o método
usado para comparar os níveis.

## Passo 1: a média por tema

Os seis temas não são igualmente difíceis. Um tema com critério estreito e poucos estudos pode baixar a precisão de
todos os níveis, enquanto um tema com literatura grande pode elevá-la. Se juntássemos todas as rodadas e todos os
artigos, um nível pareceria melhor ou pior conforme os temas que, por acaso, lhe deram mais artigos.

Por isso, o tema é a unidade. Para cada nível e cada tema, a precisão das duas rodadas vira uma média. Cada nível
termina com seis números, um por tema, e todos os níveis são medidos nos mesmos seis temas. A precisão do nível é a
média desses seis números.

As duas rodadas de um tema não são duas unidades independentes: são a mesma pergunta feita duas vezes. Tirar a média
delas primeiro mantém a análise honesta sobre quantas unidades independentes existem (seis), e absorve parte da
variação de uma rodada para outra de um modelo probabilístico.

## Passo 2: a faixa provável (intervalo de 95%)

Uma média de seis temas é uma estimativa. Outros seis temas dariam uma média um pouco diferente. O intervalo de 95%
diz até onde a média verdadeira pode plausivelmente estar: se o teste fosse repetido muitas vezes, intervalos
construídos assim conteriam o valor verdadeiro em cerca de 95% das vezes.

O intervalo é calculado sobre as seis médias por tema: a média, mais ou menos um valor crítico vezes o erro-padrão (o
desvio-padrão das seis médias dividido pela raiz quadrada de seis). O valor crítico vem da **distribuição t de Student
com 5 graus de liberdade**: G - 1, com G = 6 temas.

Por que t de Student, e por que G - 1. Com muitos grupos, o valor crítico seria o conhecido 1,96 da curva normal. Com
poucos grupos, esse valor é pequeno demais e o intervalo sai estreito demais, o que exagera a confiança. Cameron e
Miller (2015, seção VI) expõem o problema de poucos grupos (clusters) e recomendam a distribuição T com G - 1 graus de
liberdade como correção mínima. Com 5 graus de liberdade, o valor crítico fica em cerca de 2,57 em vez de 1,96, e o
intervalo fica cerca de 30% mais largo. É a escolha conservadora.

Depois, o intervalo é recortado à faixa que a precisão pode assumir, de 0 a 100%. Por isso alguns limites superiores
aparecem exatamente como 100%.

### Uma leitura comentada

Pelo júri, o Nível 3 tem precisão média de 97%, com intervalo de 94 a 100%. O Nível 2 tem 90%, com intervalo de 78 a
100%. As duas médias estão a sete pontos de distância, mas as larguras contam uma segunda história: as seis médias por
tema do Nível 3 ficaram próximas umas das outras, então o seu intervalo é estreito; o Nível 2 variou mais de um tema
para outro, então o seu intervalo é largo. Intervalos que se sobrepõem não provam, sozinhos, que dois níveis são
iguais. Para comparar dois níveis diretamente, use o passo 3.

Os intervalos de cada nível, pelo júri e pelo juiz único, estão em [results.pt-BR.md](results.pt-BR.md).

## Passo 3: o teste por artigo

O passo 2 descreve cada nível. O passo 3 testa as diferenças entre os níveis, usando cada artigo.

### O modelo

Uma **regressão logística** do acerto sobre nível e tema, uma linha por artigo entregue:

```
correct ~ level + topic
```

- **O desfecho é um artigo: certo (1) ou errado (0).** A precisão é uma proporção de artigos, e as rodadas entregam
  números diferentes de artigos. Um modelo no nível do artigo pesa cada artigo uma vez e usa toda a informação do
  teste. A regressão logística é o modelo padrão para um desfecho de sim ou não.
- **Tema como efeito fixo.** Cada tema ganha a sua própria linha de base. O efeito do nível é então estimado *dentro*
  dos temas: o Nível 3 no tema dos jogos é comparado com o Nível 0 no tema dos jogos, e não com o Nível 0 num outro
  tema, mais difícil. Isso pareia os níveis por tema, como no passo 1.
- **Erros agrupados por rodada.** Os artigos de uma rodada não são independentes entre si: vêm da mesma busca, da
  mesma triagem e da mesma sessão do modelo. Se o agente lê o tema errado uma vez, muitos dos seus artigos erram
  juntos. Tratá-los como independentes deixaria o teste confiante demais. O erro-padrão agrupado trata os artigos de
  uma rodada como um grupo e deixa que se correlacionem dentro dele.
- **Valores críticos t.** Seguindo Cameron e Miller (2015, seção VI), os testes usam a distribuição T com G - 1 graus
  de liberdade, com G igual ao número de grupos (rodadas), em vez da curva normal.

O resultado de cada comparação é uma **razão de chances** (quantas vezes maiores são as chances de um artigo estar
certo num nível do que no outro, no mesmo tema) e um **valor p** bicaudal.

### As comparações

Cinco comparações são testadas: Nível 1 contra Nível 0, Nível 2 contra Nível 1, Nível 3 contra Nível 2, Nível 3
contra Nível 1 e Nível 3 contra Nível 0.

### A correção de Holm

Cada teste carrega uma pequena chance de alarme falso: achar uma diferença que é só ruído. Faça cinco testes e a
chance de pelo menos um deles dar alarme falso cresce. Holm (1979) controla isso, com um procedimento simples:

1. Ordene os cinco valores p do menor para o maior.
2. Multiplique o menor por 5, o seguinte por 4, depois 3, 2 e 1.
3. Suba a lista sem deixar nenhum p ajustado ficar abaixo do anterior; limite todos os valores a 1.

Os valores ajustados são os **p de Holm**. Um p de Holm abaixo de 0,05 quer dizer que a diferença se sustenta mesmo
depois de descontar o fato de que cinco comparações foram feitas. Holm protege contra alarmes falsos tão bem quanto a
correção de Bonferroni, mais simples (que multiplica todo p por 5), e nunca tem menos capacidade de detectar uma
diferença real.

## Como ler o p e o corte de 5%

Um **valor p** responde a uma pergunta: se os dois níveis fossem de fato iguais, qual seria a chance de ver uma
diferença pelo menos deste tamanho só por acaso? Um p pequeno diz que a diferença observada seria rara se os níveis
fossem iguais.

O corte usual é **5% (p abaixo de 0,05)**: abaixo dele, a diferença é chamada de estatisticamente significativa. O
corte é uma convenção, não uma lei da natureza. Um p de 0,04 e um p de 0,06 trazem quase a mesma evidência; a linha
entre eles é traçada por consistência, e não porque algo muda em 0,05.

Três coisas que um valor p não diz: não é a probabilidade de os níveis serem iguais; não é o tamanho da diferença
(isso é a razão de chances e a própria precisão); e um p acima de 0,05 não mostra que não há diferença, só que este
teste, com esta amostra, não consegue separá-la do acaso com a confiança usual.

## O resultado

Em precisão, pelo júri de três empresas:

| Comparação | p de Holm | Leitura |
| --- | --- | --- |
| Nível 3 contra Nível 0 | 0,001 | o Nível 3 supera o Nível 0 com segurança estatística |
| Nível 3 contra Nível 1 | cerca de 0,06 | o Nível 3 está à frente; o sinal é mais tímido, pouco acima do corte usual de 5% |
| Nível 3 contra Nível 2 | cerca de 0,06 | o Nível 3 está à frente; o sinal é mais tímido, pouco acima do corte usual de 5% |

Em palavras: mesmo descontando as cinco comparações, a chance de ver a distância entre o Nível 3 e o Nível 0, se os
dois fossem iguais, é de cerca de 1 em 1.000. Contra os Níveis 1 e 2, o Nível 3 está à frente em precisão (97% contra
89% e 90%), e a chance de uma distância desse tamanho, se fossem iguais, é de cerca de 6%: um sinal consistente, mas
não conclusivo no corte usual. Um teste maior, com mais temas e mais repetições, é o caminho para decidir (veja
[limits-and-next-steps.pt-BR.md](limits-and-next-steps.pt-BR.md)).

Todas as comparações, com a razão de chances, o p e o p de Holm, estão em `evaluation/STATISTICS.md`.

## Como reproduzir

Na raiz do repositório, com as avaliações que acompanham o repositório em `agents/level_N/evaluations/`:

```
python -m evaluation.report class
python -m evaluation.stats class
```

`evaluation/report.py` calcula as médias por tema e os intervalos t de Student e escreve `evaluation/REPORT.md`.
`evaluation/stats.py` ajusta a regressão logística por artigo com erros agrupados por rodada e aplica Holm; escreve
`evaluation/STATISTICS.md`.

Para rodadas suas, troque `class` pela sua tag (por exemplo, `mytest`), depois de avaliá-las como descrito em
[evaluation.pt-BR.md](evaluation.pt-BR.md).

## Referências deste documento

Cameron e Miller (2015); Holm (1979). Entradas completas em [references.pt-BR.md](references.pt-BR.md).
