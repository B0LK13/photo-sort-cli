# Naming Conventions

## Repository files

New manually maintained files and directories use lowercase kebab-case, as required by the repository directive. Required ecosystem names remain unchanged: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`, `Dockerfile`-style names if added, `pyproject.toml`, `uv.lock`, Python `__init__.py`, and GitHub workflow filenames.

Existing uppercase root documents (`BACKLOG.md`, `TUI_DESIGN.md`) are preserved because they predate this documentation pass and are referenced by existing project conventions.

## Python symbols

Python modules use snake_case because that is the language convention and current source structure. Classes use PascalCase (`Executor`, `MoveOp`, `FileInfo`); functions and variables use snake_case.
