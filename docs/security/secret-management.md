# Secret Management

The application reads no environment variables and has no secret store. The repository scan found no embedded private keys, API keys, or passwords in maintained source.

GitHub workflows reference `CODECOV_TOKEN` and `PYPI_API_TOKEN` as GitHub Actions secrets. The publish workflow also requests `id-token: write` for trusted PyPI publishing. Values must remain in GitHub configuration and must not be added to repository files, logs, or documentation.

If future integrations add secrets, define scope, rotation, redaction, and local-development handling before implementation (`SEC-002`, proposed).
