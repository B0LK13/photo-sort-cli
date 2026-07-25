# Release Process

## Current repository workflow

Both `.github/workflows/ci.yml` and `.github/workflows/publish.yml` respond to version tags. CI runs a Python 3.9–3.12 test matrix and has a tag-gated build/upload job. The publish workflow builds an artifact and invokes PyPI trusted publishing.

## Required pre-release evidence

- Update version and changelog intentionally.
- Run the test suite.
- Build source and wheel distributions.
- Inspect distribution contents.
- Validate the tag workflow in GitHub with the required environment and permissions.
- Run a package-install smoke test in a clean environment.

## Rollback

No repository-defined rollback or package-yanking procedure exists. Document the chosen PyPI response and user communication before a production release (`DEPLOY-002`).
