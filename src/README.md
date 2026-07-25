# src/

## Purpose

Application package for `photo-sort-cli`.

## Structure

```text
src/photo_sort/
├── cli.py         # Entry (`photo-sort`)
├── scanner.py     # Date resolution
├── planner.py     # Destination planning
└── executor.py    # Move/copy + JSONL log
```

## Status

`partially-verified` — 16 tests passed 2026-07-25 (scanner-focused suite).

## Related

- [../README.md](../README.md)
