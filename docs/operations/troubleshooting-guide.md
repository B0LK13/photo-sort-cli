# Troubleshooting Guide

## No media files found

Confirm the directory exists and remember that scanning is non-recursive. Check extensions against `MEDIA_EXTENSIONS` in `src/photo_sort/scanner.py`.

## Files are skipped

Files without a date are returned as skipped if all configured sources fail. Existing destination paths are also skipped by the executor. Review terminal output and the selected `--source` order.

## Unexpected destination

Run without `--execute`, inspect `--format`, and use a disposable copy of the input. Do not retry real execution until the plan is understood. Format-path validation is an open security and safety item (`SEC-001`).

## Build cannot start

Ensure build dependencies are available. During this review, the build was blocked by DNS failure fetching Hatchling from PyPI, not by an observed source compilation error.

## Tests fail to start

Use `uv sync` or an environment containing the declared dev dependencies. The local basic pytest command passed; the CI coverage flags were unavailable in the current environment.
