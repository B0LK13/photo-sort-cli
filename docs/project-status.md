# Project Status

**Review date:** 2026-07-25  
**Overall status:** `partially-verified`  
**Current phase:** phase 0 foundation, moving toward phase 1 MVP verification

## Executive summary

The repository contains a coherent Beta Python CLI package at version `0.1.0` with scanner, planner, executor, tests, packaging metadata, and GitHub workflows. The scanner-focused suite passes locally with 16 tests. The primary end-to-end filesystem workflow, package build, release workflows, and quality/security checks are not fully verified. The highest-priority next action is to add disposable-directory tests for planner, executor, and CLI behavior before encouraging real execution (`CORE-001`, `TEST-001`).

## Status dashboard

| Area | Status | Evidence | Main gap | Next action |
|---|---|---|---|---|
| Core CLI | partially-verified | `src/photo_sort/cli.py` and `photo_sort` help ran | end-to-end behavior untested | `CORE-001` |
| Scanner | partially-verified | `tests/test_scanner.py`; 16 passed | EXIF/mtime and directory tests missing | `TEST-001` |
| Planner | unverified | `planner.py` exists | no tests for templates/path safety | `CORE-002` |
| Executor | unverified | `executor.py` exists | no mutation, collision, error, or log tests | `CORE-001`, `DEBT-001` |
| Packaging | unverified | `pyproject.toml`, `uv.lock`, existing ignored `dist/` | fresh build blocked by Hatchling fetch | `DEPLOY-001` |
| CI | unverified | `.github/workflows/ci.yml` | GitHub run not observed; no quality jobs | `TEST-002` |
| Publication | unverified | `.github/workflows/publish.yml` | external PyPI setup and overlapping tag workflows | `DEPLOY-002` |
| Documentation | in-development | this documentation set and directory READMEs | link/maintenance automation absent | `DOC-001` |
| Security | partially-verified | dry-run default; no embedded secrets found | path, symlink, dependency controls unverified | `SEC-001`, `SEC-002` |
| TUI | deferred | `TUI_DESIGN.md` only | no source or dependency | `UI-001` |

## Verification status

| Check | Result | Evidence |
|---|---|---|
| Compile/static syntax | passed | `compileall` over `src` exited 0 |
| Unit tests | passed | `UV_CACHE_DIR=/tmp/photo-sort-uv-cache uv run pytest tests/ -q`: 16 passed |
| Coverage report | not-run | installed pytest rejected `--cov` options |
| CLI smoke | passed | `uv run photo-sort --help` displayed usage |
| Build | blocked | `uv build` could not resolve/fetch Hatchling due DNS/network |
| Lint | not-configured | no linter in `pyproject.toml` or workflows |
| Formatting | not-configured | no formatter command configured |
| Type checking | not-configured | no type checker configured |
| Markdown validation | not-configured | no repository validator configured |
| Link validation | passed | local review validator checked 83 links after status file creation |
| Security scan | not-run | no repository security command configured |
| Deployment validation | not-run | no service deployment; GitHub/PyPI workflows not executed |

## Active blockers

### DEPLOY-001 — Build dependency resolution

The local `uv build` attempt failed before source build because DNS could not resolve PyPI to fetch Hatchling. This blocks local release evidence, but source/test work can continue independently.

### TEST-001 — Missing behavioral coverage

Only scanner parsing is covered. This blocks a confident claim that file mutation and logging are safe across success and failure paths.

## Next actions

1. Implement `TEST-001` and `CORE-001` with temporary directories.
2. Resolve dry-run and destination-path behavior through `DEBT-001` and `SEC-001`.
3. Re-run build and clean-install checks in a networked environment for `DEPLOY-001`.
4. Add selected quality/security checks through `TEST-002` and `SEC-002`.
