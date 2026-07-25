# `photo_sort` Package

## Purpose

Runtime package behind the `photo-sort` console script.

## Structure

```text
src/photo_sort/
├── __init__.py  # Package version
├── cli.py       # Argument parsing and workflow orchestration
├── scanner.py   # Media detection and date resolution
├── planner.py   # Destination operation planning
└── executor.py  # Move/copy execution and JSONL logging
```

## Data flow

`cli.main` resolves arguments, calls `scan_directory`, passes results to `build_plan`, and sends operations to `Executor.run`. The package uses local filesystem paths and has no network or database dependency.

## Status

`partially-verified` — scanner behavior has 16 passing tests; planner, executor, and CLI paths lack equivalent automated coverage.

## Known limitations

- `scan_directory` is non-recursive.
- The package has no built-in undo operation despite recording an undo-oriented log.
- Dry-run execution creates destination directories before it decides not to copy or move, which should be covered and reviewed as a safety issue.

## Related

- [Component architecture](../../docs/architecture/component-architecture.md)
- [Testing guide](../../docs/development/testing-guide.md)
- [Package backlog](../../docs/project-management/backlog.md)
