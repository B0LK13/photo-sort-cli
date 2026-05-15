# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-05-15

### Added
- Initial release of `photo-sort-cli`
- EXIF date extraction (`DateTimeOriginal`, `DateTimeDigitized`, `DateTime`)
- Filename pattern recognition for Samsung, WhatsApp, iOS, screenshots, and generic timestamps
- File modification time fallback
- Dry-run mode by default for safety
- `--execute` flag to perform actual moves
- `--copy` flag to copy instead of move
- Configurable folder structure via `--format`
- Configurable date source priority via `--source`
- JSON-lines undo log
- Duplicate detection (skips if destination exists)
