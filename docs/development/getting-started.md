# Getting Started

## Prerequisites

- Python 3.9 or newer.
- `uv` is recommended because `uv.lock` is committed for local reproducibility.
- Network access may be required when dependencies are not already cached.

## Setup

From the repository root:

```bash
uv sync
uv run pytest tests/ -q
```

The documented alternative is `python -m venv .venv` followed by `pip install -e ".[dev]"`; this was not executed in this review because the shell does not expose a `python` command outside the project environment.

## Run the CLI

```bash
uv run photo-sort /path/to/photos
uv run photo-sort /path/to/photos --execute
```

Use a disposable fixture directory for any command with `--execute`.

## Status

The test command was verified locally with 16 passing tests on 2026-07-25. Build validation remained blocked by external dependency resolution.
