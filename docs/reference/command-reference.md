# Command Reference

## Installation and development

```bash
uv sync
uv run pytest tests/ -q
uv run photo-sort --help
```

## CLI

```text
photo-sort [directory] [--execute] [--copy] [--format FORMAT]
           [--source SOURCE] [--log LOG] [--no-log]
```

Default mode is dry-run. `--execute` enables move/copy operations. The command returns `2` for an invalid directory or unknown source name; other execution outcomes are reported in terminal counts and currently return `0` from `main`.

## Release

```bash
uv build
```

This command is declared as the local build target but was not successful in the review environment because Hatchling could not be fetched.
