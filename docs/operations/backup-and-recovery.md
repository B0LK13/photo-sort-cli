# Backup and Recovery

## Current state

The tool does not create backups. Move operations are filesystem mutations; copy mode preserves the source but still creates destination files. The JSONL log records successful real operations, but no restore or undo command is implemented.

## Safe operating procedure

1. Preserve the original media before a first real run.
2. Run the default dry-run and review destinations.
3. Use `--copy` for an initial non-destructive migration where disk space permits.
4. Retain the JSONL log and terminal output.
5. Verify destination counts and representative files before removing originals.

## Recovery gap

An explicit, tested inverse operation is required before the log can be described as a usable undo mechanism (`CORE-003`).
