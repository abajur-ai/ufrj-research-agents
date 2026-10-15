[Read in English](responsible-use.md)

# Uso responsável

## Em poucas palavras

O agente acelera, quem pesquisa decide. Mesmo o melhor nível deste teste erra artigos, e não diz quais. Por isso o
agente é um copiloto: ele busca, faz a triagem, extrai e confere o dado duro em minutos, e quem pesquisa define a
pergunta, confere na fonte original o que vai citar, julga método e achado, e assina o texto. As duas armadilhas a
evitar são confiar no agente porque ele costuma acertar, e entregar a ele o entendimento e a responsabilidade que são
de quem assina. O CNPq já tem regras para isso.

## Human in the loop

Human in the loop é desenhar o sistema para que uma pessoa fique dentro do processo, com um papel definido, em vez de
receber a saída da máquina no fim (Wu et al., 2022). Numa revisão bibliográfica, a divisão é:

| O agente | Quem pesquisa |
| --- | --- |
| Busca nas bases e lê os resumos | Define a pergunta e o recorte |
| Faz a triagem e extrai os dados | Confere na fonte original o que vai citar |
| Confere por código o dado duro | Julga o método e o achado |
| Entrega em minutos, a baixo custo | Assina e responde pelo texto |

A divisão segue os resultados. O código confere o dado duro (DOI, autor, ano, revista) quase sem falha; os erros que
sobram são de recorte, método e achado, que exigem leitura. É ali que a atenção de quem pesquisa rende mais.

### Viés de automação

Com um assistente automático como copiloto, a tendência é aceitar a resposta e deixar de conferir adequadamente. É o
viés de automação: as pessoas dão à recomendação automática mais peso do que ela merece, e conferem menos quando o
sistema costuma acertar (Parasuraman e Manzey, 2010). Não é erro de iniciante. Atinge especialistas também, e cresce
com a confiabilidade do sistema: quanto melhor o agente, mais fácil é parar de olhar.

Na prática: refine o agente para o seu tema, compare abordagens diferentes e mantenha a conferência. Decida de antemão
o que vai conferir em cada artigo que citar, e confira mesmo quando o agente tiver acertado muitas vezes seguidas.

## Confiabilidade: mesmo o melhor nível erra

De cada 100 artigos pedidos ao Nível 3, pelo júri de três empresas nas 48 rodadas deste teste: **81 certos, 2 errados e
17 não entregues.** O agente não diz quais são os 2. Achar o erro é trabalho de quem pesquisa.

Isso não é defeito de um agente que uma instrução melhor vai remover. Kalai e Vempala (2024) mostram que um modelo de
linguagem bem calibrado ainda precisa inventar parte dos fatos raros: fatos que aparecem pouco nos dados de treino não
podem ser todos separados de invenções plausíveis. O erro faz parte do método. A arquitetura pode reduzi-lo (de 17% de
errados no Nível 0 para 2% no Nível 3, veja [results.pt-BR.md](results.pt-BR.md)), não levá-lo a zero.

Humanos também erram. Em revistas médicas, 25% das citações têm erro, e 12% têm erro grave (Jergas e Baethge, 2015). A
pergunta útil não é se o agente erra, mas como os erros dele se comparam com os de um pesquisador cuidadoso, e como
pegá-los.

## Limites do uso de IA

Algumas coisas não se entregam a uma máquina, por melhor que ela fique.

**O entendimento.** Messeri e Crockett (2024) alertam que ferramentas de IA podem criar ilusões de entendimento: a
sensação de saber mais do que se sabe, porque a ferramenta fez a leitura.

> "The proliferation of AI tools in science risks introducing a phase of scientific enquiry in which we produce more
> but understand less."
>
> Messeri e Crockett, *Artificial intelligence and illusions of understanding in scientific research*, Nature, 2024.

Em português: "A proliferação de ferramentas de IA na ciência arrisca inaugurar uma fase da pesquisa científica em que
produzimos mais, mas entendemos menos." (tradução nossa)

Um agente que entrega 25 artigos em cinco minutos produziu uma lista, não um entendimento do campo. Ler o que vai ser
citado continua sendo trabalho de quem pesquisa.

**A responsabilidade.** A Recomendação da UNESCO sobre a Ética da Inteligência Artificial, parágrafo 36:

> "an AI system can never replace ultimate human responsibility and accountability"
>
> UNESCO, *Recommendation on the Ethics of Artificial Intelligence*, 2021, § 36.

Em português: "Um sistema de IA nunca pode substituir a responsabilidade e a prestação de contas humanas finais."
(tradução nossa)

**A autoria.** O editorial da Nature que fixou as suas regras para ferramentas de IA:

> "any attribution of authorship carries with it accountability for the work, and AI tools cannot take such
> responsibility"
>
> Nature, editorial, v. 613, p. 612, 2023.

Em português: "Qualquer atribuição de autoria traz consigo a responsabilidade pelo trabalho, e ferramentas de IA não
podem assumir tal responsabilidade." (tradução nossa)

Um agente pode ser uma ferramenta na seção de método. Não pode ser autor.

## As regras do CNPq

Portaria CNPq nº 2.664/2026, Política de Integridade na Atividade Científica, artigo 9º, inciso I (texto resumido):

| Artigo | Regra |
| --- | --- |
| Art. 9º, I, c | Declarar o uso de IA generativa em qualquer fase da pesquisa, com a ferramenta e a finalidade. |
| Art. 9º, I, d | É vedado submeter conteúdo gerado por IA como se fosse de autoria humana. |
| Art. 9º, I, e | É vedado inserir projetos de terceiros em IA para elaborar pareceres. |
| Art. 9º, I, f | Quem pesquisa responde pelo conteúdo final, inclusive por plágios ou imprecisões da IA. |

Aplicado a este repositório: se você usar um agente como o Nível 3 numa revisão, declare o uso, com a ferramenta e o
que ela fez (busca, triagem, extração); confira o que citar; e trate a saída dele como responsabilidade sua.

## Para refletir

As perguntas com que a aula fecha:

1. Dá para confiar num agente de IA para fazer revisão bibliográfica? (A) Não. (B) Sim, com ele fazendo tudo sozinho.
   (C) Sim, como meu copiloto.
2. O que você conferiria num agente que erra 2%?
3. Quanto do tempo que o agente economiza deveria ir para a conferência?
4. Que taxa de erro é aceitável numa revisão bibliográfica: zero, ou a de um pesquisador experiente?
5. Onde termina a atuação da IA e começa a atuação humana?
6. Na sua dissertação, onde e com que nível de detalhe você declararia o uso de IA?

## Referências deste documento

Brasil, CNPq, Portaria nº 2.664/2026; Jergas e Baethge (2015); Kalai e Vempala (2024); Messeri e Crockett (2024);
Nature (2023); Parasuraman e Manzey (2010); UNESCO (2021); Wu et al. (2022). Entradas completas em
[references.pt-BR.md](references.pt-BR.md).
