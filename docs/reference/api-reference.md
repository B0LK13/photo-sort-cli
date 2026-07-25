# CLI and Module Reference

## Public console entry point

`photo_sort.cli:main(argv=None) -> int` is registered as `photo-sort` in `pyproject.toml`.

## Main module interfaces

- `scanner.scan_directory(root, source_priority=None) -> list[FileInfo]`
- `scanner.parse_filename_date(filepath)`
- `scanner.parse_exif_date(filepath)`
- `scanner.parse_mtime_date(filepath)`
- `planner.build_plan(infos, root, format_template="YYYY/MM") -> (ops, skipped)`
- `executor.Executor(dry_run=True, copy=False, log_path=None)`
- `executor.Executor.run(ops) -> (performed, skipped)`

These are internal Python interfaces; no versioned HTTP API exists.
