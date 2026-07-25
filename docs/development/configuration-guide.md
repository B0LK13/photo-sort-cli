# Configuration Guide

The CLI currently uses command-line arguments rather than environment variables or a configuration file.

| Option | Default | Effect |
|---|---|---|
| `directory` | `.` | Directly scanned directory |
| `--execute` | false | Enable filesystem mutation |
| `--copy` | false | Copy instead of move when executing |
| `--format` | `YYYY/MM` | Destination folder template |
| `--source` | `filename,exif,mtime` | Date-source priority |
| `--log` | `photo-sort.log.jsonl` | JSONL log path |
| `--no-log` | false | Disable real-operation logging |

## Environment variables

None are read by application code. CI uses `CODECOV_TOKEN` and `PYPI_API_TOKEN` as GitHub Actions secrets; these are not local application settings. See [environment variables](../reference/environment-variables.md).

## Configuration gaps

The parser accepts arbitrary format strings and log paths; path containment, duplicate source handling, and empty source-list behavior are not specified by tests. Track under `SEC-001`.
