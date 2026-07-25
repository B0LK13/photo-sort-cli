# GitHub Workflows

## Purpose

CI and package-publication automation for the repository.

## Structure

```text
.github/workflows/
├── ci.yml       # Python matrix tests; tag-gated build/upload job
└── publish.yml  # Tag-gated artifact build and trusted PyPI publication
```

## Current status

`unverified` — workflow definitions were inspected but not executed in GitHub during this review.

## Known limitations

- CI covers tests and coverage upload but has no configured lint, type, markdown-link, or security job.
- Release behavior depends on GitHub secrets/environment configuration and PyPI trusted publishing setup not present in this repository.
- `ci.yml` and `publish.yml` both publish on tags, so release behavior should be consolidated or explicitly justified (`DEPLOY-002`).

## Related

- [Deployment architecture](../docs/architecture/deployment-architecture.md)
- [Release process](../docs/operations/release-process.md)
