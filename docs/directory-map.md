# Directory Map

| Directory | Responsibility | Status | Entry point | Documentation |
|---|---|---|---|---|
| `src/` | Python source layout | partially-verified | `src/photo_sort/` | [src README](../src/README.md) |
| `src/photo_sort/` | CLI, scanning, planning, execution | partially-verified | `src/photo_sort/cli.py:main` | [package README](../src/photo_sort/README.md) |
| `tests/` | pytest tests | partially-verified | `tests/test_scanner.py` | [tests README](../tests/README.md) |
| `.github/workflows/` | CI and PyPI workflows | unverified | `ci.yml`, `publish.yml` | [.github README](../.github/README.md) |
| `docs/` | Maintained project documentation | in-development | `docs/documentation-index.md` | [docs README](README.md) |
| `dist/` | Existing distribution artifacts, ignored by Git | unverified | wheel and sdist | excluded from manual restructuring |
| `.venv/` | Local virtual environment | unverified | environment-managed | excluded |
| `.pytest_cache/` | pytest-generated cache | not applicable | cache files | excluded |
| `.codebase-memory/` | Generated code knowledge index from this review | unverified | `graph.db.zst` | generated; not application source |

Root files such as `pyproject.toml`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, `uv.lock`, `BACKLOG.md`, and `TUI_DESIGN.md` remain at the root because packaging, contributor expectations, or existing project conventions make moving them unnecessary.
