# Environment Variables

## Application

None. The CLI is configured through command-line options.

## CI-only secrets

| Variable | Used by | Purpose | Required locally |
|---|---|---|---|
| `CODECOV_TOKEN` | `.github/workflows/ci.yml` | Coverage upload authentication | no |
| `PYPI_API_TOKEN` | `.github/workflows/ci.yml` | PyPI upload credential in tag job | no |

Values are external secrets and must not be documented or committed.
