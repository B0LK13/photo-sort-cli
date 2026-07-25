# Security Overview

## Implemented controls

- Dry-run is the default; mutation requires `--execute`.
- Destination collisions are skipped rather than overwritten.
- Filesystem errors are caught per operation and reported.
- No secrets are embedded in application source found during inspection.
- CI uses GitHub secret references for Codecov and PyPI credentials.

## Missing or unverified controls

- No path containment or traversal validation for format-derived destinations.
- No explicit symlink policy.
- No tested rollback/undo path.
- No dependency/security scan in CI.
- No structured audit-log protection or privacy guidance beyond local file behavior.
- Release workflow permissions and trusted publishing configuration are repository-external and unverified.

## Security posture

`partially-verified`: controls exist for conservative defaults, but filesystem safety and release/dependency controls require validation.
