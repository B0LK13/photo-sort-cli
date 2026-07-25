# Threat Model

## Assets

- User photos and videos.
- Original and destination filesystem paths.
- JSONL operation log, which may contain local paths.
- Package publication credentials and release integrity.

## Trust boundaries

1. CLI input and option values cross into filesystem operations.
2. Media files and EXIF metadata are untrusted input to Pillow and date parsers.
3. GitHub Actions and PyPI are external release systems.

## Threats and controls

| Threat | Current control | Gap |
|---|---|---|
| Accidental mutation | dry-run default, collision skip | dry-run directory side effect and limited tests |
| Destination traversal | none observed | validate `--format` and resolved paths |
| Malformed media metadata | broad EXIF open exception handling | add fixture and resource/error tests |
| Sensitive path exposure | local JSONL only | document retention and permissions |
| Dependency compromise | lockfile and pinned action major versions | no dependency scan or review policy |
| Release credential misuse | GitHub secrets/OIDC reference | workflow configuration unverified |

## Priorities

Address path validation and mutation testing before encouraging real move operations. Track under `SEC-001`, `TEST-001`, and `DEPLOY-002`.
