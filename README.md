# Python AI Agent

A command-line coding agent built with Python and the OpenAI SDK. It connects through OpenRouter and can inspect files, run Python programs, and write files in the `calculator` working directory.

## Setup

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Create a `.env` file in the project root and add your OpenRouter API key:

```dotenv
OPENROUTER_API_KEY=your-api-key
```

Keep the real key private. `.env` files are excluded by `.gitignore`.

## Run

```bash
uv run main.py "How does the calculator render results to the console?"
```

Add `--verbose` to show tool calls and token usage:

```bash
uv run main.py "Run the calculator tests" --verbose
```

Run the calculator tests directly with:

```bash
uv run calculator/tests.py
```

The agent's tools use `calculator` as their working directory. They can read and write files there and run Python files there.

> This is a learning project, not a production-ready coding agent. It can modify files and execute Python code in its working directory; use it only with code you trust.
