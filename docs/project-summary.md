# Project Summary

## Identity and purpose

`photo-sort-cli` is a Python command-line tool that sorts photos and videos into date-based folders. It resolves dates from filename patterns, EXIF metadata, or file modification time, then previews or executes move/copy operations.

## Users and use cases

The declared audience is desktop end users. The documented workflow is: point the command at a directory, inspect a dry run, then optionally execute a move or copy with a JSON-lines operation log.

## Current scope

Implemented in source: CLI argument parsing, non-recursive media scanning, filename/EXIF/mtime date resolution, destination planning, dry-run output, move/copy execution, duplicate-destination skipping, and append-only JSONL logging.

Partially implemented or unverified: the complete workflow is not covered by automated tests; the README describes undo-log data but no undo command is shipped; the scanner is explicitly non-recursive; the TUI exists only as a design document.

Planned/proposed: see [roadmap](project-management/roadmap.md) and [backlog](project-management/backlog.md). No web application, API, database, worker, authentication, or hosted service is present in the repository.

## Technology stack

- Python `>=3.9`.
- `Pillow>=10.0.0` for image/EXIF access.
- `pytest` and `pytest-cov` declared as development dependencies.
- Hatchling build backend.
- `uv.lock` for reproducible local dependency resolution.
- GitHub Actions for test and tag-triggered package publication workflows.

## Architecture at a glance

`photo_sort.cli` orchestrates `scanner`, `planner`, and `executor`. Filesystem state is the only runtime persistence; the optional JSONL log is written during real execution. See [architecture overview](architecture/architecture-overview.md).

## Maturity

The package metadata declares Beta and version `0.1.0`. Local scanner tests passed during this review, but broader behavior and build/release validation remain incomplete or blocked; current project status is `partially-verified`.

## Immediate priorities

1. Add tests for planner, executor, CLI validation, and real temporary-directory workflows (`TEST-001`, `CORE-001`).
2. Define safe validation for format and log paths and clarify recursive behavior (`SEC-001`, `CORE-002`).
3. Make build validation reproducible in an environment with build dependencies (`DEPLOY-001`).
