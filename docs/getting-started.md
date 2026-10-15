[Leia em português](getting-started.pt-BR.md)

# Getting started

In this guide you will prepare a Windows 11 computer to run the four research agents of this repository. You will learn what an agentic AI is and which setups we recommend, install Claude Code (logged in to a Claude subscription or pointed to OpenRouter), create the three keys the project needs (OpenRouter, OpenAlex and Brave Search), save them in a safe place on your computer, and install Python, Google Chrome and the project itself. No programming experience is needed: every step tells you where to click or what to paste. At the end, a checklist confirms that everything is ready for [Run the benchmark](run-the-benchmark.md).

## Contents

1. [What an agentic AI is](#1-what-an-agentic-ai-is)
2. [Which agentic AI to use](#2-which-agentic-ai-to-use)
3. [Install Claude Code from zero](#3-install-claude-code-from-zero)
4. [OpenRouter: one key for many AI companies](#4-openrouter-one-key-for-many-ai-companies)
5. [OpenAlex: the free key for the academic database](#5-openalex-the-free-key-for-the-academic-database)
6. [Brave Search: the web search of the Level 2 verifier](#6-brave-search-the-web-search-of-the-level-2-verifier)
7. [Python, Google Chrome and ffmpeg](#7-python-google-chrome-and-ffmpeg)
8. [Install the project](#8-install-the-project)
9. [Checklist](#9-checklist)

## 1. What an agentic AI is

A chat AI answers one question at a time. You decide the next step, you search, you open the files and you check.

An agentic AI receives a goal and runs the steps itself. It reads files, runs commands on your computer, uses tools such as web search, looks at the result and decides what to do next, until the goal is done. You ask "clone this repository and run Level 3 on the example topic", and it downloads the code, installs what is missing, runs the command, reads the output and tells you what happened.

This is the same idea the class studies: an agent has a profile, a memory, a plan and actions (the four layers). Here you use one agent to run and inspect the four agents of the benchmark.

## 2. Which agentic AI to use

First, one fact about this repository: **the executor of every agent is Claude Code.** The code calls it through the Claude Agent SDK, which runs the `claude.exe` that comes with the Claude Code extension for Visual Studio Code (see `run_agent` in `core/llm.py`). So, whatever tool you use to operate the repository, Claude Code must be installed, and either logged in to a Claude subscription or pointed to OpenRouter (section 3).

### Recommended setups

To reproduce the exact structure of this repository, use one of these two setups, in this order of preference.

**(a) Claude Code (recommended).** Claude Code operates the repository and is also the executor of the agents: one installation does both jobs. You pay for it in one of two ways:

- logged in to a Claude subscription (a paid plan; the free plan does not run Claude Code); or
- pointed to OpenRouter, paying per token (section 3).

**(b) OpenCode with OpenRouter.** OpenCode (https://opencode.ai) is an open-source agentic AI. You configure it with OpenRouter, choose an Anthropic model through OpenRouter, and OpenCode operates the repository: it clones, installs, runs the commands and reads the results. The executor of the agents is still Claude Code, so in this setup Claude Code must also be installed, and logged in or pointed to OpenRouter (section 3).

Steps from the official guide (https://opencode.ai/docs/providers/#openrouter):

1. Install OpenCode as shown in https://opencode.ai/docs/. This repository runs on Windows itself, so use one of the Windows options listed there, such as `scoop install opencode`, `choco install opencode` or `npm install -g opencode-ai`.
2. Create an OpenRouter API key (section 4).
3. In OpenCode, run `/connect`, search for OpenRouter and paste the key.
4. Run `/models` and pick an Anthropic model.

### Other agentic AIs

OpenAI Codex CLI, Cursor, Kimi Code, Gemini CLI and GitHub Copilot agent mode can run the same structure, but on your own: you will need to adapt the executor. The executor is a single function, `run_agent` in `core/llm.py`, so the adaptation stays in one place. Paste this prompt into your agentic AI:

```text
Read the repository https://github.com/abajur-ai/ufrj-research-agents, starting with README.md and docs/run-the-benchmark.md. Every agent in it calls one executor function: run_agent in core/llm.py, which drives Claude Code through the Claude Agent SDK. Replace that executor call with my own model and tools. Keep the same inputs: system_prompt, user_prompt, the tools WebSearch and WebFetch, the JSON schema of the output, max_turns and timeout_s. Keep the same outputs: the AgentResult with the structured result, the text, the tool calls and the usage tokens; the events written to the run's events.jsonl with the same kinds (ai_call_start, ai_text, ai_tool, ai_tool_result, ai_call_error, ai_call_end); and the files in the run's calls/ folder (system prompt, user prompt and result of each call). Do not change agents/level_N/, the prompts, benchmark/qa.py, the verifier, the evaluation or the topics. Then run Level 3 on topic a04 with python -m benchmark.run --level n3 --topic a04 --tag adapted --rep 1, and compare the delivered articles, the time and the tokens with the class runs class-n3-a04-r1 and class-n3-a04-r2.
```

With another executor, your runs are a new experiment: compare them with the class runs, but do not read them as the class numbers.

## 3. Install Claude Code from zero

If you have never used Claude Code, start with the setup repository of Abajur.ai:

**https://github.com/abajur-ai/setup-for-claude-code**

It installs and configures Claude Code on Windows, step by step, in plain language. Its README walks you through installing Visual Studio Code, adding the Claude Code extension by Anthropic, signing in with your Claude account, and letting Claude Code finish the configuration by itself. This repository assumes that setup as its base.

What matters for this project:

- **Windows 11.** The project was tested only there.
- **Claude Code as the Visual Studio Code extension.** The code looks for the `claude.exe` program that comes with the extension. If the extension is missing, no level can run.
- **A way to pay the executor**: a Claude subscription, or OpenRouter credits. Choose one of the two options below.

### Option 1: log in to a Claude subscription

Open Visual Studio Code, click the Claude Code icon on the side bar and sign in with a paid Claude plan. The free plan does not run Claude Code. The executor then runs on your subscription.

### Option 2: point Claude Code to OpenRouter (pay per token)

OpenRouter has an official guide for this: https://openrouter.ai/docs/guides/guides/claude-code-integration. It asks for three environment variables:

| Variable | Value |
| --- | --- |
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` |
| `ANTHROPIC_AUTH_TOKEN` | your OpenRouter key (section 4) |
| `ANTHROPIC_API_KEY` | explicitly empty |

The guide shows them in a macOS or Linux shell profile, or in a `.claude/settings.local.json` file. For this repository, save them as Windows user environment variables: the code starts Claude Code without reading any settings file (`core/llm.py`), so only environment variables reach it. In PowerShell, replacing `<key>`:

```powershell
[Environment]::SetEnvironmentVariable('ANTHROPIC_BASE_URL','https://openrouter.ai/api','User')
[Environment]::SetEnvironmentVariable('ANTHROPIC_AUTH_TOKEN','<key>','User')
```

A Windows user variable cannot hold an empty value, so for `ANTHROPIC_API_KEY` make sure it is not set at all: `[Environment]::GetEnvironmentVariable('ANTHROPIC_API_KEY','User')` must print nothing.

Then, as the guide says:

1. If you logged in to Claude Code with an Anthropic account, run `/logout` in Claude Code. A cached login can conflict with the variables.
2. Close and reopen Visual Studio Code, so it sees the new variables.
3. In Claude Code, run `/status`. The auth token must read `ANTHROPIC_AUTH_TOKEN` and the base URL `https://openrouter.ai/api`. The Activity page of OpenRouter also shows each request.

The guide recommends Anthropic models with Claude Code. The code asks for Claude Sonnet 5.5 (`MODEL` in `core/config.py`); for how model names map through OpenRouter, and for anything that does not match the steps above, see the official guide.

With this option, the executor is paid from your OpenRouter credits, per token.

### Confirm

Open Visual Studio Code, click the Claude Code icon on the side bar, and send a short message such as "hello". If it answers, Claude Code is ready.

## 4. OpenRouter: one key for many AI companies

**What it is.** OpenRouter (https://openrouter.ai) is a service that gives you one account and one key to use AI models from many companies. In this project it runs two things: the **verifier** of Levels 2 and 3 (GLM-5.3 Flash, by Z.ai), and the **three judges** of the evaluation (DeepSeek V4 Pro, Qwen3.7 Plus by Alibaba, and Gemini 3.1 Flash-Lite by Google). Five companies in total: Claude executes, GLM checks, and DeepSeek, Qwen and Gemini judge. OpenRouter lets you reach the last four with a single key. If you point Claude Code to OpenRouter (section 3, option 2), the same account also pays the executor.

**How much it costs.** You pay OpenRouter only for what you use. The whole benchmark (48 runs, plus the evaluation by the three judges) used about **US$ 33 (about R$ 170)** in OpenRouter tokens, with the executor on a Claude subscription. A single run costs cents. Levels 0 and 1 do not use OpenRouter to run at all; they only use it if you evaluate them with the judges.

**Step by step:**

1. Go to https://openrouter.ai and click **Sign up**. You can use a Google account or an email.
2. Open the **Credits** page (in the menu under your profile picture) and add credits with a card. A small amount is enough to try one run; for the whole benchmark, plan for about US$ 33.
3. Open the **Keys** page and click **Create Key**. Give it a name, for example `ufrj-research-agents`, and confirm.
4. Copy the key that appears. It starts with `sk-or-`. OpenRouter shows it only once, so copy it before you close the window.
5. Save the key as a user environment variable. Open **PowerShell** (press the Windows key, type `PowerShell`, press Enter), paste the line below, replace `<key>` with your key (keep the single quotes), and press Enter:

   ```powershell
   [Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY','<key>','User')
   ```

6. **Close PowerShell and open a new one.** A terminal only sees variables that existed when it opened. The same is true for Visual Studio Code: close it and open it again.

**Why an environment variable.** The key stays in your Windows user account, outside the project folder. The code reads it from the environment when it runs and never writes it to disk or to the logs, so you never paste the key into a file that could end up on GitHub.

## 5. OpenAlex: the free key for the academic database

**What it is.** OpenAlex (https://openalex.org) is an open catalog of scholarly works: articles, authors, journals and their abstracts. Level 3 searches it to find articles, and the evaluation uses it to check that each DOI, title, author, year and journal is real. OpenAlex asks for a free API key.

**Step by step:**

1. Go to https://openalex.org and create a free account.
2. In your account settings, find your **API key** and copy it.
3. In PowerShell, save it the same way, replacing `<key>`:

   ```powershell
   [Environment]::SetEnvironmentVariable('OPENALEX_API_KEY','<key>','User')
   ```

4. Close PowerShell and open a new one.

## 6. Brave Search: the web search of the Level 2 verifier

**What it is.** The verifier of Level 2 checks the executor's work on the open web: it searches and opens pages to confirm that an article exists and says what the executor claims. Those searches go through the Brave Search API. The bibliography check also uses it to find web pages, books and primary sources.

**Step by step:**

1. Go to https://brave.com/search/api/ and create an account.
2. Choose a plan and create an API key in the dashboard. The code sends at most about one search per second.
3. In PowerShell, save it, replacing `<key>`:

   ```powershell
   [Environment]::SetEnvironmentVariable('BRAVE_API_KEY','<key>','User')
   ```

4. Close PowerShell and open a new one.

If you already set up the Brave Search connector inside Claude Code, the code also finds the key there.

The file `.env.example` at the root of the repository lists the three variables with one line on what each one is for. It is a reference only: the code reads the keys from the environment, not from that file.

## 7. Python, Google Chrome and ffmpeg

The project needs:

- **Python 3.13**, the language the code is written in.
- **Google Chrome**, used to open publisher pages during the evaluation and to record videos of the runs.
- **Git**, to download the repository (you can also download it as a ZIP from GitHub).
- **ffmpeg**, only if you want to record replay videos. You can skip it otherwise.

The quickest way on Windows 11 is `winget`, which comes with the system. In PowerShell, run one line at a time:

```powershell
winget install Python.Python.3.13
winget install Google.Chrome
winget install Git.Git
winget install Gyan.FFmpeg
```

Close PowerShell and open a new one, then check:

```powershell
python --version
git --version
```

The first line must show `Python 3.13`. If `python` opens the Microsoft Store instead, use `py -3.13` wherever this guide says `python`.

## 8. Install the project

In PowerShell, go to the folder where you keep your projects and run:

```powershell
git clone https://github.com/abajur-ai/ufrj-research-agents
cd ufrj-research-agents
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

What each line does:

| Command | What it does |
| --- | --- |
| `git clone ...` | downloads the repository into a folder called `ufrj-research-agents` |
| `cd ufrj-research-agents` | enters that folder |
| `python -m venv .venv` | creates an isolated Python environment for this project, in the `.venv` folder |
| `.venv\Scripts\activate` | turns that environment on; the prompt starts with `(.venv)` |
| `pip install -r requirements.txt` | installs the exact library versions listed in `requirements.txt` |
| `python -m playwright install chromium` | downloads the browser the code uses to open pages that refuse simple downloads |

Every time you open a new terminal to work on the project, enter the folder and run `.venv\Scripts\activate` again.

If PowerShell says that running scripts is disabled on this system, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

You do not have to type any of this yourself. You can open Claude Code (or OpenCode, in setup (b)) in an empty folder and ask it to do the installation for you; [Run the benchmark](run-the-benchmark.md#1-the-simplest-way-ask-claude-code) has instructions ready to paste.

## 9. Checklist

Open a new PowerShell in the project folder, run `.venv\Scripts\activate`, and confirm each item:

- [ ] Windows 11.
- [ ] Claude Code installed as the Visual Studio Code extension, and it answers a message: logged in with a paid Claude plan, or pointed to OpenRouter (`/status` shows the base URL `https://openrouter.ai/api`).
- [ ] Setup (b) only: OpenCode installed, connected to OpenRouter, with an Anthropic model chosen in `/models`.
- [ ] OpenRouter account with credits, and the key saved:
  `if ($env:OPENROUTER_API_KEY) { 'ok' } else { 'missing' }` prints `ok`.
- [ ] OpenAlex key saved:
  `if ($env:OPENALEX_API_KEY) { 'ok' } else { 'missing' }` prints `ok`.
- [ ] Brave Search key saved:
  `if ($env:BRAVE_API_KEY) { 'ok' } else { 'missing' }` prints `ok`.
- [ ] `python --version` shows Python 3.13.
- [ ] Google Chrome installed.
- [ ] `pip install -r requirements.txt` and `python -m playwright install chromium` finished without errors.
- [ ] ffmpeg installed (only to record videos): `ffmpeg -version` prints a version.

These checks print only `ok` or `missing`, never the key itself, so they are safe to run while sharing your screen.

Everything checked? Go to [Run the benchmark](run-the-benchmark.md).
