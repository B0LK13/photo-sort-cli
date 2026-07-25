# Development Workflow

1. Read the relevant source, tests, and documentation before changing behavior.
2. Keep changes narrow and preserve the dry-run safety default.
3. Add or update tests for changed scanner, planner, executor, or CLI behavior.
4. Run `UV_CACHE_DIR=/tmp/photo-sort-uv-cache uv run pytest tests/ -q` when the default uv cache is not writable.
5. Run a package build when build dependencies are available.
6. Update status, backlog, risks, and affected directory README files with evidence.

## Existing contributor guidance

`CONTRIBUTING.md` requests PEP 8, practical type hints, tests for new features, feature branches, and pull requests. No formatter, linter, type checker, or commit hook is configured in `pyproject.toml`.

## Branching and commits

The repository history uses short imperative-style commit subjects, but no formal commit validation is configured. Follow the existing project convention unless a future decision records a stricter policy.
