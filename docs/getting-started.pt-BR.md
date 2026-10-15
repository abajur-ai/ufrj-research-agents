[Read in English](getting-started.md)

# Primeiros passos

Neste guia você vai preparar um computador com Windows 11 para rodar os quatro agentes de pesquisa deste repositório. Você vai entender o que é uma IA agêntica e quais configurações recomendamos, instalar o Claude Code (com login numa assinatura do Claude ou apontado para o OpenRouter), criar as três chaves de que o projeto precisa (OpenRouter, OpenAlex e Brave Search), guardá-las num lugar seguro do seu computador e instalar o Python, o Google Chrome e o próprio projeto. Não é preciso saber programar: cada passo diz onde clicar ou o que colar. No fim, uma lista de conferência confirma que está tudo pronto para [Rodar o benchmark](run-the-benchmark.pt-BR.md).

## Sumário

1. [O que é uma IA agêntica](#1-o-que-é-uma-ia-agêntica)
2. [Qual IA agêntica usar](#2-qual-ia-agêntica-usar)
3. [Instalar o Claude Code do zero](#3-instalar-o-claude-code-do-zero)
4. [OpenRouter: uma chave para várias empresas de IA](#4-openrouter-uma-chave-para-várias-empresas-de-ia)
5. [OpenAlex: a chave gratuita da base acadêmica](#5-openalex-a-chave-gratuita-da-base-acadêmica)
6. [Brave Search: a busca na web do verificador do Nível 2](#6-brave-search-a-busca-na-web-do-verificador-do-nível-2)
7. [Python, Google Chrome e ffmpeg](#7-python-google-chrome-e-ffmpeg)
8. [Instalar o projeto](#8-instalar-o-projeto)
9. [Lista de conferência](#9-lista-de-conferência)

## 1. O que é uma IA agêntica

Uma IA de chat responde uma pergunta por vez. Você decide o próximo passo, você busca, você abre os arquivos e você confere.

Uma IA agêntica recebe um objetivo e executa os passos sozinha. Ela lê arquivos, roda comandos no seu computador, usa ferramentas como a busca na web, olha o resultado e decide o que fazer em seguida, até cumprir o objetivo. Você pede "clone este repositório e rode o Nível 3 no tema de exemplo", e ela baixa o código, instala o que falta, roda o comando, lê a saída e conta o que aconteceu.

É a mesma ideia que a aula estuda: um agente tem perfil, memória, planejamento e ação (as quatro camadas). Aqui você usa um agente para rodar e examinar os quatro agentes do benchmark.

## 2. Qual IA agêntica usar

Primeiro, um fato sobre este repositório: **o executor de todos os agentes é o Claude Code.** O código o chama pelo Claude Agent SDK, que roda o `claude.exe` que vem com a extensão Claude Code do Visual Studio Code (veja `run_agent` em `core/llm.py`). Então, seja qual for a ferramenta que opera o repositório, o Claude Code precisa estar instalado e, além disso, com login numa assinatura do Claude ou apontado para o OpenRouter (seção 3).

### Configurações recomendadas

Para reproduzir a estrutura exata deste repositório, use uma destas duas configurações, nesta ordem de preferência.

**(a) Claude Code (recomendado).** O Claude Code opera o repositório e também é o executor dos agentes: uma instalação faz os dois papéis. Você paga por ele de um de dois jeitos:

- com login numa assinatura do Claude (um plano pago; o plano gratuito não roda o Claude Code); ou
- apontado para o OpenRouter, pagando por token (seção 3).

**(b) OpenCode com OpenRouter.** O OpenCode (https://opencode.ai) é uma IA agêntica de código aberto. Você o configura com o OpenRouter, escolhe um modelo da Anthropic pelo OpenRouter, e o OpenCode opera o repositório: clona, instala, roda os comandos e lê os resultados. O executor dos agentes continua sendo o Claude Code, então nesta configuração o Claude Code também precisa estar instalado, com login ou apontado para o OpenRouter (seção 3).

Passos do guia oficial (https://opencode.ai/docs/providers/#openrouter):

1. Instale o OpenCode como mostra https://opencode.ai/docs/. Este repositório roda no próprio Windows, então use uma das opções para Windows listadas lá, como `scoop install opencode`, `choco install opencode` ou `npm install -g opencode-ai`.
2. Crie uma chave de API do OpenRouter (seção 4).
3. No OpenCode, rode `/connect`, procure o OpenRouter e cole a chave.
4. Rode `/models` e escolha um modelo da Anthropic.

### Outras IAs agênticas

OpenAI Codex CLI, Cursor, Kimi Code, Gemini CLI e GitHub Copilot no modo agente conseguem rodar a mesma estrutura, mas por sua conta: você vai precisar adaptar o executor. O executor é uma função só, `run_agent` em `core/llm.py`, então a adaptação fica num lugar só. Cole esta instrução na sua IA agêntica:

```text
Leia o repositório https://github.com/abajur-ai/ufrj-research-agents, começando pelo README.pt-BR.md e pelo docs/run-the-benchmark.pt-BR.md. Todos os agentes dele chamam uma única função de executor: run_agent em core/llm.py, que comanda o Claude Code pelo Claude Agent SDK. Troque essa chamada do executor pelo meu próprio modelo e pelas minhas ferramentas. Mantenha as mesmas entradas: system_prompt, user_prompt, as ferramentas WebSearch e WebFetch, o esquema JSON da saída, max_turns e timeout_s. Mantenha as mesmas saídas: o AgentResult com o resultado estruturado, o texto, as chamadas de ferramenta e os tokens de uso; os eventos gravados no events.jsonl da rodada, com os mesmos tipos (ai_call_start, ai_text, ai_tool, ai_tool_result, ai_call_error, ai_call_end); e os arquivos da pasta calls/ da rodada (instrução de sistema, pedido e resultado de cada chamada). Não mude agents/level_N/, os prompts, benchmark/qa.py, o verificador, a avaliação nem os temas. Depois rode o Nível 3 no tema a04 com python -m benchmark.run --level n3 --topic a04 --tag adapted --rep 1 e compare os artigos entregues, o tempo e os tokens com as rodadas da aula class-n3-a04-r1 e class-n3-a04-r2.
```

Com outro executor, as suas rodadas são um experimento novo: compare com as rodadas da aula, mas não as leia como os números da aula.

## 3. Instalar o Claude Code do zero

Se você nunca usou o Claude Code, comece pelo repositório de setup da Abajur.ai:

**https://github.com/abajur-ai/setup-for-claude-code**

Ele instala e configura o Claude Code no Windows, passo a passo, em linguagem simples. O README dele leva você por todo o caminho: instalar o Visual Studio Code, adicionar a extensão Claude Code da Anthropic, entrar com a sua conta do Claude e deixar o próprio Claude Code terminar a configuração. Este repositório parte desse setup como base.

O que importa para este projeto:

- **Windows 11.** O projeto foi testado só nele.
- **Claude Code como extensão do Visual Studio Code.** O código procura o programa `claude.exe` que vem com a extensão. Sem a extensão, nenhum nível roda.
- **Um jeito de pagar o executor**: uma assinatura do Claude ou créditos no OpenRouter. Escolha uma das duas opções abaixo.

### Opção 1: login numa assinatura do Claude

Abra o Visual Studio Code, clique no ícone do Claude Code na barra lateral e entre com um plano pago do Claude. O plano gratuito não roda o Claude Code. O executor passa a rodar na sua assinatura.

### Opção 2: apontar o Claude Code para o OpenRouter (pagando por token)

O OpenRouter tem um guia oficial para isso: https://openrouter.ai/docs/guides/guides/claude-code-integration. Ele pede três variáveis de ambiente:

| Variável | Valor |
| --- | --- |
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` |
| `ANTHROPIC_AUTH_TOKEN` | a sua chave do OpenRouter (seção 4) |
| `ANTHROPIC_API_KEY` | explicitamente vazia |

O guia mostra essas variáveis num perfil de shell do macOS ou do Linux, ou num arquivo `.claude/settings.local.json`. Para este repositório, guarde-as como variáveis de ambiente do usuário no Windows: o código inicia o Claude Code sem ler nenhum arquivo de configuração (`core/llm.py`), então só as variáveis de ambiente chegam até ele. No PowerShell, trocando `<key>`:

```powershell
[Environment]::SetEnvironmentVariable('ANTHROPIC_BASE_URL','https://openrouter.ai/api','User')
[Environment]::SetEnvironmentVariable('ANTHROPIC_AUTH_TOKEN','<key>','User')
```

Uma variável de usuário do Windows não guarda valor vazio, então, para a `ANTHROPIC_API_KEY`, garanta que ela não exista: `[Environment]::GetEnvironmentVariable('ANTHROPIC_API_KEY','User')` não pode mostrar nada.

Depois, como diz o guia:

1. Se você entrou no Claude Code com uma conta da Anthropic, rode `/logout` no Claude Code. Um login guardado pode entrar em conflito com as variáveis.
2. Feche e abra de novo o Visual Studio Code, para ele enxergar as variáveis novas.
3. No Claude Code, rode `/status`. O token de autenticação tem que aparecer como `ANTHROPIC_AUTH_TOKEN` e a URL base como `https://openrouter.ai/api`. A página Activity do OpenRouter também mostra cada requisição.

O guia recomenda modelos da Anthropic com o Claude Code. O código pede o Claude Sonnet 5.5 (`MODEL` em `core/config.py`); para saber como os nomes de modelo passam pelo OpenRouter, e para qualquer coisa que não bata com os passos acima, veja o guia oficial.

Nesta opção, o executor é pago com os seus créditos do OpenRouter, por token.

### Confirmar

Abra o Visual Studio Code, clique no ícone do Claude Code na barra lateral e mande uma mensagem curta, como "olá". Se ele responder, o Claude Code está pronto.

## 4. OpenRouter: uma chave para várias empresas de IA

**O que é.** O OpenRouter (https://openrouter.ai) é um serviço que dá uma conta e uma chave para usar modelos de IA de várias empresas. Neste projeto ele roda duas coisas: o **verificador** dos Níveis 2 e 3 (GLM-5.3 Flash, da Z.ai) e os **três juízes** da avaliação (DeepSeek V4 Pro, Qwen3.7 Plus da Alibaba e Gemini 3.1 Flash-Lite do Google). São cinco empresas no total: o Claude executa, o GLM confere, e DeepSeek, Qwen e Gemini julgam. O OpenRouter dá acesso às quatro últimas com uma chave só. Se você apontar o Claude Code para o OpenRouter (seção 3, opção 2), a mesma conta também paga o executor.

**Quanto custa.** Você paga ao OpenRouter só o que usar. O benchmark inteiro (48 rodadas, mais a avaliação pelos três juízes) gastou cerca de **US$ 33 (cerca de R$ 170)** em tokens no OpenRouter, com o executor numa assinatura do Claude. Uma rodada sozinha custa centavos. Os Níveis 0 e 1 nem usam o OpenRouter para rodar; só usam se você os avaliar com os juízes.

**Passo a passo:**

1. Entre em https://openrouter.ai e clique em **Sign up**. Dá para usar uma conta Google ou um e-mail.
2. Abra a página **Credits** (no menu da sua foto de perfil) e adicione créditos com cartão. Um valor pequeno basta para testar uma rodada; para o benchmark inteiro, reserve cerca de US$ 33.
3. Abra a página **Keys** e clique em **Create Key**. Dê um nome, por exemplo `ufrj-research-agents`, e confirme.
4. Copie a chave que aparece. Ela começa com `sk-or-`. O OpenRouter mostra a chave uma vez só, então copie antes de fechar a janela.
5. Guarde a chave como variável de ambiente do usuário. Abra o **PowerShell** (aperte a tecla Windows, digite `PowerShell`, aperte Enter), cole a linha abaixo, troque `<key>` pela sua chave (mantenha as aspas simples) e aperte Enter:

   ```powershell
   [Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY','<key>','User')
   ```

6. **Feche o PowerShell e abra um novo.** Um terminal só enxerga as variáveis que existiam quando ele abriu. Vale o mesmo para o Visual Studio Code: feche e abra de novo.

**Por que variável de ambiente.** A chave fica na sua conta de usuário do Windows, fora da pasta do projeto. O código lê a chave do ambiente na hora de rodar e nunca a grava em disco nem nos registros, então você nunca cola a chave num arquivo que poderia acabar no GitHub.

## 5. OpenAlex: a chave gratuita da base acadêmica

**O que é.** O OpenAlex (https://openalex.org) é um catálogo aberto de produção acadêmica: artigos, autores, periódicos e seus resumos. O Nível 3 busca nele para encontrar artigos, e a avaliação usa o OpenAlex para conferir se cada DOI, título, autor, ano e periódico é real. O OpenAlex pede uma chave de API gratuita.

**Passo a passo:**

1. Entre em https://openalex.org e crie uma conta gratuita.
2. Nas configurações da sua conta, encontre a sua **API key** e copie.
3. No PowerShell, guarde a chave do mesmo jeito, trocando `<key>`:

   ```powershell
   [Environment]::SetEnvironmentVariable('OPENALEX_API_KEY','<key>','User')
   ```

4. Feche o PowerShell e abra um novo.

## 6. Brave Search: a busca na web do verificador do Nível 2

**O que é.** O verificador do Nível 2 confere o trabalho do executor na web aberta: busca e abre páginas para confirmar que um artigo existe e diz o que o executor afirma. Essas buscas passam pela API do Brave Search. A conferência da bibliografia também usa essa API para encontrar páginas da web, livros e fontes primárias.

**Passo a passo:**

1. Entre em https://brave.com/search/api/ e crie uma conta.
2. Escolha um plano e crie uma chave de API no painel. O código manda no máximo cerca de uma busca por segundo.
3. No PowerShell, guarde a chave, trocando `<key>`:

   ```powershell
   [Environment]::SetEnvironmentVariable('BRAVE_API_KEY','<key>','User')
   ```

4. Feche o PowerShell e abra um novo.

Se você já configurou o conector do Brave Search dentro do Claude Code, o código também encontra a chave lá.

O arquivo `.env.example`, na raiz do repositório, lista as três variáveis com uma linha sobre o uso de cada uma. Ele serve só de referência: o código lê as chaves do ambiente, não desse arquivo.

## 7. Python, Google Chrome e ffmpeg

O projeto precisa de:

- **Python 3.13**, a linguagem em que o código está escrito.
- **Google Chrome**, usado para abrir páginas de editoras durante a avaliação e para gravar vídeos das rodadas.
- **Git**, para baixar o repositório (também dá para baixar como ZIP pelo GitHub).
- **ffmpeg**, só se você quiser gravar vídeos de replay. Fora isso, pode pular.

O jeito mais rápido no Windows 11 é o `winget`, que já vem com o sistema. No PowerShell, rode uma linha por vez:

```powershell
winget install Python.Python.3.13
winget install Google.Chrome
winget install Git.Git
winget install Gyan.FFmpeg
```

Feche o PowerShell, abra um novo e confira:

```powershell
python --version
git --version
```

A primeira linha tem que mostrar `Python 3.13`. Se o `python` abrir a Microsoft Store, use `py -3.13` em todo lugar onde este guia diz `python`.

## 8. Instalar o projeto

No PowerShell, vá até a pasta onde você guarda seus projetos e rode:

```powershell
git clone https://github.com/abajur-ai/ufrj-research-agents
cd ufrj-research-agents
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

O que cada linha faz:

| Comando | O que faz |
| --- | --- |
| `git clone ...` | baixa o repositório numa pasta chamada `ufrj-research-agents` |
| `cd ufrj-research-agents` | entra nessa pasta |
| `python -m venv .venv` | cria um ambiente Python isolado para este projeto, na pasta `.venv` |
| `.venv\Scripts\activate` | liga esse ambiente; a linha de comando passa a começar com `(.venv)` |
| `pip install -r requirements.txt` | instala as versões exatas das bibliotecas listadas em `requirements.txt` |
| `python -m playwright install chromium` | baixa o navegador que o código usa para abrir páginas que recusam download simples |

Sempre que abrir um terminal novo para trabalhar no projeto, entre na pasta e rode `.venv\Scripts\activate` de novo.

Se o PowerShell disser que a execução de scripts está desabilitada neste sistema, rode isto uma vez e tente de novo:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Você não precisa digitar nada disso. Dá para abrir o Claude Code (ou o OpenCode, na configuração (b)) numa pasta vazia e pedir que ele faça a instalação; [Rodar o benchmark](run-the-benchmark.pt-BR.md#1-o-jeito-mais-simples-pedir-ao-claude-code) traz instruções prontas para colar.

## 9. Lista de conferência

Abra um PowerShell novo na pasta do projeto, rode `.venv\Scripts\activate` e confirme cada item:

- [ ] Windows 11.
- [ ] Claude Code instalado como extensão do Visual Studio Code, e ele responde a uma mensagem: com login num plano pago do Claude, ou apontado para o OpenRouter (`/status` mostra a URL base `https://openrouter.ai/api`).
- [ ] Só na configuração (b): OpenCode instalado, conectado ao OpenRouter, com um modelo da Anthropic escolhido em `/models`.
- [ ] Conta no OpenRouter com créditos, e a chave guardada:
  `if ($env:OPENROUTER_API_KEY) { 'ok' } else { 'missing' }` mostra `ok`.
- [ ] Chave do OpenAlex guardada:
  `if ($env:OPENALEX_API_KEY) { 'ok' } else { 'missing' }` mostra `ok`.
- [ ] Chave do Brave Search guardada:
  `if ($env:BRAVE_API_KEY) { 'ok' } else { 'missing' }` mostra `ok`.
- [ ] `python --version` mostra Python 3.13.
- [ ] Google Chrome instalado.
- [ ] `pip install -r requirements.txt` e `python -m playwright install chromium` terminaram sem erro.
- [ ] ffmpeg instalado (só para gravar vídeos): `ffmpeg -version` mostra uma versão.

Essas conferências mostram só `ok` ou `missing`, nunca a chave, então dá para rodar com a tela compartilhada.

Tudo conferido? Siga para [Rodar o benchmark](run-the-benchmark.pt-BR.md).
