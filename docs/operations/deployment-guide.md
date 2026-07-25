# Deployment Guide

## User installation

The supported documented installation is:

```bash
pip install photo-sort-cli
```

Source installation is also documented in the root README. No service deployment is required or supported by current repository files.

## Local release build

The declared build backend is Hatchling. CI uses `python -m build`, but no local build command passed during this review: `uv build` could not resolve Hatchling because DNS/network access to PyPI was unavailable.

## Production readiness

Production deployment is not applicable to the current local CLI model. Package publication is configured but unverified here; use `DEPLOY-001` and `DEPLOY-002` to close build and workflow gaps.
