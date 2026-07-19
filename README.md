# photo-sort-cli

Sort photos and videos into date-based folders using EXIF metadata, filename patterns, or file timestamps.

## Features

- **EXIF-first** — reads `DateTimeOriginal`, `DateTimeDigitized`, and `DateTime`
- **Smart filename parsing** — recognises Samsung, WhatsApp, iOS, screenshot, and generic timestamp patterns
- **Safe by default** — dry-run mode; add `--execute` to actually move files
- **Undo log** — every move is recorded to a JSON-lines file for reversal
- **Customisable** — choose your own folder structure (`YYYY/MM`, `YYYY/MM/DD`, etc.) and date-source priority

## Installation

```bash
pip install photo-sort-cli
```

Or install from source:

```bash
git clone https://github.com/wjbol/photo-sort-cli.git
cd photo-sort-cli
pip install .
```

For reproducible local development, use the committed `uv.lock`:

```bash
uv sync                 # installs exactly what's in uv.lock
uv run pytest tests/ -v
```

(CI intentionally keeps installing via plain `pip install -e ".[dev]"` across its Python 3.9-3.12 matrix,
since a single lockfile can't represent 4 independent resolutions — `uv.lock` is for reproducible local
dev, not the version-compatibility matrix.)

## Usage

```bash
# Preview what would happen (dry-run)
photo-sort /path/to/photos

# Actually sort the files
photo-sort /path/to/photos --execute

# Copy instead of move
photo-sort /path/to/photos --execute --copy

# Custom folder structure
photo-sort /path/to/photos --execute --format "YYYY/MM/DD"

# Prefer EXIF over filenames
photo-sort /path/to/photos --execute --source exif,filename,mtime
```

### Options

| Flag | Description |
|------|-------------|
| `--execute` | Perform the move/copy. Without this, the tool runs in dry-run mode. |
| `--copy` | Copy files instead of moving them. |
| `--format` | Output folder template using `YYYY`, `MM`, `DD`. Default: `YYYY/MM`. |
| `--source` | Comma-separated priority of `exif`, `filename`, `mtime`. Default: `filename,exif,mtime`. |
| `--log` | Path to JSON-lines undo log. Default: `photo-sort.log.jsonl`. |
| `--no-log` | Disable the undo log. |

## Supported filename patterns

- `20190101_035012.jpg`
- `IMG_20200628_1856521.jpg`
- `IMG-20170630-WA0006.jpeg`
- `Screenshot_20190305-071500_Samsung Health.jpg`
- `Scherm_afbeelding 2024-01-15 om 00.45.02.png`
- `VID-20190312-WA0001.mp4`

## Undo log

After running with `--execute`, a JSON-lines log is created in the working directory. Each line records the source and destination path, making it possible to reverse the operation with a simple script.

## License

MIT
