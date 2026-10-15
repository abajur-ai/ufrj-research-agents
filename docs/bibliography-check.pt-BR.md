[Read in English](bibliography-check.md)

# Conferência da bibliografia

Neste guia você vai usar o método do Nível 3 para conferir uma bibliografia: para cada afirmação de um texto, a fonte citada diz mesmo aquilo? Você vai ver como a conferência funciona (o código encontra cada obra nos registros oficiais e procura no texto dela; um júri de três modelos de IA de três empresas lê o que o código achou e decide por maioria), como rodar, como trocar os dados de exemplo pelas suas referências e afirmações, como ler as saídas e quanto custa. Os dados de exemplo são o deck da aula: cada referência e cada afirmação do deck passou por esta conferência.

## Sumário

1. [O que ela faz](#1-o-que-ela-faz)
2. [Como funciona, passo a passo](#2-como-funciona-passo-a-passo)
3. [Por que este desenho](#3-por-que-este-desenho)
4. [Rodar](#4-rodar)
5. [Conferir a sua própria bibliografia](#5-conferir-a-sua-própria-bibliografia)
6. [As saídas](#6-as-saídas)
7. [Custo e cache](#7-custo-e-cache)
8. [Como usar o resultado](#8-como-usar-o-resultado)

## 1. O que ela faz

Um texto cita uma fonte e diz algo sobre ela: "55% das referências eram inventadas", "o modelo tende a preferir as próprias respostas", "o CNPq exige declarar o uso de IA". Cada uma dessas frases pode dar errado de dois jeitos. A própria referência pode estar errada (a obra não existe, o autor ou o ano é outro). Ou a referência está certa, mas a fonte não diz o que o texto afirma, ou diz menos, ou diz outra coisa.

A conferência da bibliografia, na pasta `bibcheck/`, responde às duas perguntas para cada referência e cada afirmação:

- **A obra existe, com este autor, ano e veículo?** Quem responde é o código, nos registros oficiais.
- **A fonte sustenta a afirmação?** Quem responde é um júri de três modelos, lendo só trechos da fonte que o código encontrou.

## 2. Como funciona, passo a passo

**1. O código encontra cada obra nos registros oficiais.** Cada referência tem um tipo, e cada tipo tem os seus registros:

| Tipo | Onde o código procura |
| --- | --- |
| `paper` | OpenAlex, DBLP, arXiv e Crossref, consultados em paralelo pelo título |
| `book` | OpenLibrary, mais uma busca na web por páginas sobre o livro |
| `web` | uma busca na web; o código abre os resultados e fica com as páginas que trazem o título da obra |

Depois o código confere se a obra existe (um título muito parecido em pelo menos um registro), se o primeiro autor bate, se o ano bate e se o veículo (periódico, conferência ou editora) bate.

**2. O código baixa o texto da fonte.** O que estiver aberto: o resumo (OpenAlex, Crossref, arXiv), o texto completo (o PDF do arXiv, quando existe), a página da editora pelo DOI, ou a própria página da web. Páginas que recusam download simples são abertas num navegador de verdade.

**3. O código procura os números e as frases literais da afirmação.** Cada afirmação vem com algumas *agulhas*: trechos curtos que precisam aparecer na fonte se a afirmação estiver certa, como `55%`, `636` ou `never replace ultimate human responsibility`. O código procura cada agulha em todos os textos baixados e anota onde achou, ou que não achou.

**4. O código recorta os trechos.** Ele monta um arquivo curto de leitura para o júri: os resumos, mais o texto em volta de cada agulha encontrada. O júri lê esses trechos, não a internet inteira.

**5. Um júri de três modelos de três empresas decide.** DeepSeek V4 Pro, Qwen3.7 Plus (Alibaba) e Gemini 3.1 Flash-Lite (Google), chamados pelo OpenRouter, recebem cada um a obra, a afirmação e os trechos. Cada um precisa copiar o trecho que decide e devolver um de quatro pareceres:

- **sustenta**: os trechos dizem isso, inclusive números e citações literais (tradução fiel vale);
- **sustenta em parte**: parte é dita, ou a afirmação vai além, exagera ou distorce a fonte;
- **não sustenta**: os trechos dizem outra coisa, ou o contrário;
- **trechos insuficientes**: os trechos não tratam do ponto.

Os juízes só podem usar os trechos, não o que eles próprios sabem da obra. O parecer final é o que pelo menos dois juízes deram. Quando os três discordam, a afirmação fica marcada como **dividido**.

## 3. Por que este desenho

É o princípio do Nível 3: **código onde dá, IA com conferência onde precisa.**

- Achar uma obra, comparar título, ano ou autor e procurar um número num texto são tarefas com uma resposta certa. O código faz do mesmo jeito toda vez, e quando falha, falha à vista.
- Decidir se um trecho sustenta uma frase exige leitura. Esse é o único passo que fica com a IA, e ele é conferido: três modelos de três empresas diferentes, cada um sem ver os outros, decidem por maioria.
- Os juízes leem só o que o código achou, então um juiz não consegue inventar uma citação que não está na fonte.

## 4. Rodar

Você precisa da preparação dos [Primeiros passos](getting-started.pt-BR.md), com as três chaves: `OPENROUTER_API_KEY` (o júri), `OPENALEX_API_KEY` (o OpenAlex) e `BRAVE_API_KEY` (as buscas na web por livros, páginas e fontes primárias). No PowerShell, na raiz do repositório, com o ambiente ativo:

```powershell
python -m bibcheck.run
```

O comando confere cada referência e cada afirmação de `bibcheck/data.py`, mostra o começo do relatório e grava os dois arquivos de saída (seção 6).

Também dá para pedir ao Claude Code, na pasta do repositório:

```text
Leia docs/bibliography-check.pt-BR.md, rode python -m bibcheck.run e me mostre cada afirmação cujo parecer não seja "sustenta", com os motivos dos juízes.
```

## 5. Conferir a sua própria bibliografia

Todos os dados ficam num arquivo só, `bibcheck/data.py`, em duas listas: `REFS` (as obras) e `CLAIMS` (as frases que citam as obras). Troque os exemplos pelos seus e rode o comando de novo. Nada neste arquivo é tomado como verdade: identificadores, links e textos são sempre encontrados pelo código.

### As obras: `REFS`

```python
REFS = [
    {"id": "walters", "kind": "paper",
     "title": "Fabrication and errors in the bibliographic citations generated by ChatGPT",
     "authors": ["Walters", "Wilder"], "year": 2023, "venue": "Scientific Reports"},
    {"id": "unesco", "kind": "web",
     "title": "Recommendation on the Ethics of Artificial Intelligence",
     "authors": ["UNESCO"], "year": 2021, "venue": "UNESCO",
     "query": "UNESCO Recommendation on the Ethics of Artificial Intelligence \"never replace ultimate human responsibility\""},
]
```

| Campo | Obrigatório | O que escrever |
| --- | --- | --- |
| `id` | sim | um nome curto que você escolhe, usado pelas afirmações para apontar para esta obra |
| `kind` | sim | `paper` (artigo, trabalho de conferência, preprint), `book` ou `web` (relatório, post, lei, página) |
| `title` | sim | o título como foi publicado, no idioma original |
| `authors` | sim | uma lista de sobrenomes; o primeiro é o que o código confere |
| `year` | sim | o ano de publicação |
| `venue` | sim | periódico, conferência, editora ou site; escreva `arXiv` para um preprint, e o código pula a conferência do veículo |
| `query` | para `book` e `web` | a busca na web que deve encontrar a obra; aspas forçam a frase exata |

### As afirmações: `CLAIMS`

```python
CLAIMS = [
    {"id": "c12", "page": 12, "refs": ["walters"],
     "claim": "55% das referências do ChatGPT-3.5 eram inventadas; 18% no ChatGPT-4, no mesmo teste; 636 referências somando os dois modelos.",
     "needles": ["55%", "18%", "636"]},
    {"id": "n04", "page": 40, "refs": ["unesco"],
     "claim": "Um sistema de IA nunca pode substituir a responsabilidade e a prestação de contas humanas finais.",
     "needles": ["never replace ultimate human responsibility"], "prefer": "unesco.org"},
]
```

| Campo | Obrigatório | O que escrever |
| --- | --- | --- |
| `id` | sim | um nome curto para a afirmação |
| `page` | sim | onde a afirmação está no seu texto (número da página, do slide ou da seção), mostrado no relatório |
| `refs` | sim | o `id` das obras citadas; a primeira é a obra apresentada ao júri, e os textos de todas são consultados |
| `claim` | sim | a frase exatamente como está no seu texto, em qualquer idioma |
| `needles` | sim | trechos literais curtos ou números que precisam aparecer na fonte se a afirmação estiver certa |
| `extra` | não | buscas extras na web, mirando a fonte primária, quando os registros não bastam |
| `prefer` | não | o domínio da fonte primária, como `nature.com` ou `in.gov.br`; os resultados dele são abertos primeiro |

Dicas para boas agulhas:

- Escreva no **idioma da fonte**, não no do seu texto. Uma afirmação em português sobre um artigo em inglês precisa de agulhas em inglês.
- Prefira **números e frases características** a palavras comuns. `636` diz mais que `references`.
- Escreva o número do jeito que a fonte escreve. Na dúvida, liste as duas formas, como `"11.9"` e `"11,9"`.
- A busca ignora maiúsculas e minúsculas, então `hallucinat` encontra tanto *hallucinate* quanto *hallucination*.
- Uma agulha não encontrada é um sinal, não um parecer: o texto pode estar atrás de um paywall. O júri lê do mesmo jeito o que o código achou.

## 6. As saídas

**`bibcheck/REPORT.md`** é o relatório para ler. Ele tem duas partes:

- **Obras**: uma linha por referência, dizendo se a obra existe e se autor, ano e veículo batem, mais o que o código conseguiu ler (resumo, texto completo, página da editora, página da web).
- **Afirmações**: um bloco por afirmação, com o parecer final, a própria afirmação, quais agulhas o código achou, e o parecer e o motivo de cada um dos três juízes.

**`bibcheck/result.json`** guarda os mesmos dados por inteiro, para programas e para auditoria:

- `refs`: para cada obra, o que cada registro devolveu, as quatro conferências e a lista de textos que o código leu;
- `claims`: para cada afirmação, onde cada agulha foi achada, o voto de cada juiz (o trecho que copiou, o parecer e o motivo), o parecer final e todas as fontes lidas.

## 7. Custo e cache

A única parte paga é o júri: três chamadas no OpenRouter por afirmação, que custam **centavos por afirmação**. As consultas a OpenAlex, DBLP, arXiv, Crossref e OpenLibrary são gratuitas; as buscas na web usam o seu plano do Brave Search.

Registros, textos baixados e cada resposta dos juízes ficam salvos em disco. A resposta de um juiz fica em `bibcheck/cache/`, presa exatamente ao que o juiz leu: quando uma nova execução entrega ao juiz os mesmos trechos, a resposta salva é reaproveitada e não custa nada. Se você editar uma afirmação, só ela volta ao júri.

## 8. Como usar o resultado

A conferência aponta onde olhar; ela não assina por você. O agente acelera, quem pesquisa decide.

- **sustenta**: abra o trecho que os juízes copiaram e confirme na fonte antes de citar.
- **sustenta em parte**: o parecer mais útil. Leia os motivos dos juízes: em geral o texto vai um passo além da fonte, e uma palavra resolve.
- **não sustenta**: leia a fonte; ou a afirmação ou a referência está errada.
- **trechos insuficientes** ou **dividido**: o código não chegou ao texto certo, muitas vezes porque ele é fechado. Leia a fonte você mesmo.
- Uma obra que não existe em nenhum registro, ou com autor ou ano errado, é a primeira coisa a acertar.

Quem pesquisa responde pelo texto final. A Portaria CNPq nº 2.664/2026 (art. 9º, I) pede que quem pesquisa declare o uso de IA generativa, com a ferramenta e a finalidade, e estabelece que quem pesquisa responde pelo conteúdo final, inclusive por erros vindos da IA.
