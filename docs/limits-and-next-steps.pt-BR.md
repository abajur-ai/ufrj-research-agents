[Read in English](limits-and-next-steps.md)

# Limites e próximos passos

## Em poucas palavras

Este é um teste pequeno: seis temas, uma tarefa, 48 rodadas. Ele foi montado para que os seus limites fiquem à vista
e tratados, e não escondidos. Cada limite abaixo vem com o jeito como o teste lida com ele. A segunda metade é
prática: seis maneiras de quem pesquisa levar o Nível 3 adiante no próprio campo, com como fazer cada uma neste
repositório.

## Como ler estes resultados

| O limite | Como o teste trata |
| --- | --- |
| Estudo pequeno: seis temas, uma tarefa | Cada tema roda duas vezes em cada nível; a média é por tema, e a faixa provável de cada média é alargada por serem só seis temas. |
| Um só modelo executando | É o mesmo em todos os níveis: a diferença medida vem da arquitetura, não do modelo. |
| Os juízes são IA e leem só o resumo | Júri de três empresas, cego ao nível, decide por maioria; o dado duro é conferido por código. |
| A web, as bases e os preços mudam | Métricas e critérios fixados antes das rodadas; custo com a cotação e a data. |

### Estudo pequeno: seis temas, uma tarefa

Seis temas e um tipo de tarefa (uma revisão bibliográfica de artigos empíricos de periódico) bastam para ver o padrão,
não para fechar todas as perguntas. O teste trata disso de três jeitos. Cada tema roda duas vezes em cada nível,
porque o modelo é probabilístico. O tema é a unidade de análise: as duas rodadas viram uma média, então o teste nunca
finge ter mais unidades independentes do que tem. E o intervalo de 95% usa t de Student com G - 1 = 5 graus de
liberdade, que o alarga de propósito para poucos grupos (Cameron e Miller, 2015, seção VI). É também por isso que o
Nível 3 supera os Níveis 1 e 2 com sinal mais tímido (p de Holm cerca de 0,06): com seis temas, uma distância de sete
ou oito pontos fica perto do que o teste consegue separar. Veja [statistics.pt-BR.md](statistics.pt-BR.md).

O que os resultados não cobrem: outras tarefas (uma revisão sistemática com protocolo completo, extração de dados do
texto completo), outros campos com as suas próprias bases, ou literatura em outros idiomas.

### Um só modelo executando

Todos os níveis rodam no Claude Sonnet 5.5. Outro modelo poderia ir melhor ou pior em todos os níveis. Mantê-lo igual
é justamente o ponto: é o controle que torna a comparação justa, e assim a diferença medida vem da arquitetura. Se a
mesma ordem vale com outro executor é uma pergunta em aberto.

### Os juízes são IA e leem só o resumo

Os juízes podem errar, e um resumo pode omitir um detalhe de método ou suavizar um achado que o artigo completo
informa. O teste trata disso de quatro jeitos. O júri tem três modelos de três empresas, nenhuma delas a do executor
ou a do verificador (Panickssery, Bowman e Feng, 2024; Verga et al., 2024). Os juízes são cegos ao nível. O veredito
é a maioria por critério. E tudo o que tem resposta num registro (DOI, título, autor, ano, revista, período, tipo,
trecho, amostra) é conferido por código, e não por um juiz.

Quanto os juízes concordam: **os três juízes dão o mesmo veredito em 85% dos 980 artigos que julgaram; a maior parte
da discordância está no método**, o critério que mais depende de como um resumo descreve um estudo. Um juiz único
(DeepSeek V4 Pro sozinho) dá a mesma ordem dos níveis que o júri. Veja [evaluation.pt-BR.md](evaluation.pt-BR.md).

### A web, as bases e os preços mudam

Uma rodada feita amanhã busca numa web um pouco diferente, o OpenAlex e o Crossref ganham registros todo dia, e os
preços dos modelos mudam. O teste trata disso fixando as métricas e os critérios de julgamento antes das rodadas,
guardando cada rodada em disco (a lista entregue, cada chamada de IA, o log de eventos) para que a sua avaliação possa
ser repetida sem rodá-la de novo, e informando o custo com a cotação e a data: PTAX de venda de 14/10/2026,
US$ 1 = R$ 5,0441.

## Do Nível 3 em diante: como refinar o agente

O Nível 3 é um ponto de partida, não um teto. Estes são os seis passos que o tornariam melhor num campo específico, na
ordem em que quem pesquisa costuma segui-los.

### 1. Monte um banco de casos reais

Revisões que você já fez e conferiu viram o gabarito do agente no seu campo. Rode nele a cada mudança de modelo ou de
instrução.

Como:

- Escolha de três a cinco revisões em que você confia, com as listas finais de artigos incluídos.
- Transforme cada uma num tema em `benchmark/topics.json`, com os mesmos campos dos seis temas que já estão lá: o
  pedido nas suas palavras, o período e o número de artigos.
- Rode o Nível 3 nelas com uma tag sua, por exemplo
  `python -m benchmark.bench --topics <seus ids> --levels n3 --reps 2 --tag mybank --workers 4`.
- Avalie (`python -m evaluation.evaluate --judge deepseek --prefix mybank`, e os outros juízes mais
  `python -m evaluation.jury mybank` para o júri completo), e então compare o que o agente entregou com a sua lista: o
  que ele achou e você também incluiu, o que ele achou e você deixou passar, e o que você incluiu e ele não achou.
- Mantenha o banco fixo. Toda vez que o modelo ou uma instrução mudar, rode o banco de novo e compare a precisão e os
  artigos errados com a rodada anterior. Uma mudança que baixa os números do banco não entra.

### 2. Transforme cada erro em regra

Recorte, método ou achado: o erro que se repete vira regra ou verificador novo no agente. Depois, rode o banco de
novo.

Como:

- Abra os arquivos de avaliação das suas rodadas. Para cada artigo errado, `agents/level_3/evaluations/jury/` mostra
  qual conferência reprovou, e os arquivos de cada juiz (`judge-deepseek/`, `judge-qwen/`, `judge-gemini/`) guardam o
  trecho que aquele juiz copiou como evidência.
- Agrupe as reprovações por tipo: fora do tema, não empírico ou método errado, achado além do resumo, trecho ou
  amostra fora do resumo.
- Quando um tipo se repete, decida onde ele mora. Uma regra de julgamento vai para a instrução do passo que toma
  aquela decisão: `agents/level_3/prompts/screener.md` para recorte e desenho empírico,
  `agents/level_3/prompts/extractor.md` para método, amostra e achado. Uma regra com resposta certa (um período, um
  tipo de publicação, uma palavra que precisa aparecer) vai para o código, que nunca a esquece.
- Rode o banco de novo e confira que o erro caiu e nada mais subiu.

### 3. Leia o artigo inteiro

O Nível 3 decide pelo resumo. Com o texto completo, quando aberto, método e achado ficam mais fáceis de confirmar.

Como:

- O OpenAlex registra, para muitos artigos, se existe uma versão em acesso aberto e onde ela está. Os clientes dos
  registros ficam em `benchmark/scholar.py`; é ali o lugar de buscar o texto completo aberto, quando houver.
- Dê ao passo de extração as seções de método e de resultados, além do resumo, e mantenha a conferência do trecho
  contra o texto de onde ele veio.
- Mantenha o caminho só com o resumo para os artigos fechados, e registre em cada artigo qual evidência foi usada,
  para que quem pesquisa saiba o que conferir à mão.

### 4. Busque nas bases da sua área

O Nível 3 busca em duas bases gerais, o OpenAlex e o Crossref. As bases, o vocabulário e os critérios do seu campo
especializam o agente.

Como:

- Acrescente a base da sua área como mais uma fonte em `benchmark/scholar.py`, ao lado do OpenAlex e do Crossref, para
  que o passo 2 do Nível 3 (o código busca nas bases acadêmicas) a consulte também. Saúde, educação, ciências sociais e
  literatura latino-americana têm, cada uma, os seus próprios índices.
- Ponha o vocabulário do seu campo no passo que decide os termos de busca (`agents/level_3/prompts/terms.md`): os
  termos controlados, os sinônimos e os termos a excluir.
- Escreva os critérios de inclusão do seu campo na instrução da triagem: o que conta como empírico, quais desenhos
  entram, quais tipos de publicação ficam de fora.

### 5. Ponha um especialista na régua

Uma pessoa da área julga uma amostra, lendo o artigo inteiro, e mostra o quanto os juízes de IA acertam.

Como:

- Sorteie uma amostra de artigos entregues, de todos os níveis, incluindo alguns que o júri aprovou e alguns que
  reprovou.
- Dê ao especialista o pedido, o artigo (texto completo) e os dados que o agente extraiu, sem o nível e sem o
  veredito do júri, e peça os mesmos quatro critérios: do tema, empírico, método como dito, achado sustentado.
- Compare o veredito do especialista com o do júri, critério por critério. Onde discordam, leia o porquê: isso mostra
  se o júri é tolerante demais, rigoroso demais, ou limitado por ler só o resumo.

### 6. Teste maior, com orçamento

Mais temas e mais repetições mostram com clareza o que cada ajuste melhora.

Como:

- Acrescente temas em `benchmark/topics.json` e aumente `--reps` em `python -m benchmark.bench`. Mais temas estreitam
  mais o intervalo, porque o tema é a unidade de análise; mais repetições firmam a média de cada tema.
- Orçamento: este teste custou uma assinatura do Claude Code e cerca de R$ 170 em tokens na OpenRouter (US$ 33,38)
  para o verificador e os juízes, em 48 rodadas. O custo cresce mais ou menos na proporção do número de rodadas e de
  artigos julgados.
- Fixe as métricas e os critérios antes de rodar, como aqui, e anote as comparações que vai testar, para que o teste
  responda à pergunta que você fez.

## Referências deste documento

Cameron e Miller (2015); Panickssery, Bowman e Feng (2024); Verga et al. (2024). Entradas completas em
[references.pt-BR.md](references.pt-BR.md).
