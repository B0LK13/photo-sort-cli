# Testing Guide

## Current strategy

The repository has one pytest module, `tests/test_scanner.py`, covering media-extension recognition and filename date parsing with 16 passing cases. There are no committed planner, executor, CLI integration, EXIF fixture, collision, or end-to-end tests.

## Confirmed command

```bash
uv run pytest tests/ -q
```

Observed result on 2026-07-25: `16 passed in 0.45s` when run with `UV_CACHE_DIR=/tmp/photo-sort-uv-cache`.

## Unverified or unavailable checks

- Coverage command from CI was not runnable locally because the installed pytest did not recognize `--cov`.
- No lint, type-check, formatting, markdown, link, or security command is configured.
- GitHub Actions matrix behavior was inspected, not executed.

## Required next coverage

Add tests for source-priority fallback, EXIF parsing, non-media handling, folder template expansion, destination collisions, dry-run side effects, copy/move errors, JSONL records, invalid CLI input, and a disposable-directory smoke workflow (`TEST-001`, `CORE-001`).
