# Integration Architecture

## Current integrations

| Integration | Direction | Evidence | Status |
|---|---|---|---|
| Pillow | local library call | `scanner.parse_exif_date` | implemented; test coverage incomplete |
| Local filesystem | read/write | scanner and executor use `os`, `shutil`, `pathlib` | implemented; mutation tests missing |
| GitHub Actions | CI automation | `.github/workflows/ci.yml` and `publish.yml` | configured; unverified here |
| PyPI | package publication | tag workflows | configured; external setup unverified |

## Not present

No HTTP APIs, cloud storage, analytics, telemetry, database, queue, authentication provider, or external media catalog integration is present.

## Integration risks

The local filesystem is both input and output. A malformed or unexpected destination format can affect where files are written. The executor catches OS errors but does not provide transactional rollback. See `SEC-001`, `CORE-001`, and `OPS-001`.
