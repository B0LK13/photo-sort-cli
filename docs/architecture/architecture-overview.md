# Architecture Overview

## Current boundary

The system is a local, single-process Python CLI. It reads a user-selected directory, derives dates, constructs target paths, and optionally mutates the filesystem. There is no server boundary, database, queue, background worker, or user account system.

## Layers

| Layer | Module | Responsibility |
|---|---|---|
| Interface | `src/photo_sort/cli.py` | Parse arguments, validate basic inputs, print results |
| Discovery | `src/photo_sort/scanner.py` | Identify media and resolve dates |
| Planning | `src/photo_sort/planner.py` | Convert dated files into `MoveOp` records |
| Execution | `src/photo_sort/executor.py` | Skip collisions, move/copy files, append JSONL entries |

## Architectural constraints

- The package supports Python 3.9+ according to `pyproject.toml` and CI targets 3.9–3.12.
- Image metadata uses Pillow; other media types rely on filename or mtime because no video metadata dependency is declared.
- `scan_directory` is non-recursive by implementation and docstring.
- The CLI defaults to dry-run mode; `--execute` enables mutation.

## Extension points

The source-priority callable list and the `MoveOp` data class are the clearest internal extension points. A TUI is proposed in `TUI_DESIGN.md`, but no corresponding package modules or optional dependency currently exist.

## Limitations

The current design does not provide transactional execution, rollback, an undo command, structured machine-readable CLI output, or a formal configuration object. These are backlog items, not current capabilities.
