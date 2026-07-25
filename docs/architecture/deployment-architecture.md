# Deployment Architecture

## Current model

The project is distributed as a Python package with the `photo-sort` console entry point. `pyproject.toml` uses Hatchling; CI builds distributions on version tags and the separate publish workflow attempts trusted PyPI publication.

## Topology

```text
Developer or end user
        │ pip install / source checkout
        ▼
photo-sort console script
        │ local process
        ▼
User-selected filesystem + optional JSONL log
```

There are no container files, deployment manifests, database migrations, service processes, health endpoints, or production infrastructure files in the repository.

## Verification

Existing `dist/` artifacts are present but ignored by Git and were not treated as fresh release evidence. A fresh `uv build` attempt was blocked because the environment could not resolve PyPI to fetch Hatchling. GitHub workflows were inspected but not executed here.

## Release risks

- Two workflows respond to version tags and both contain publication-related behavior.
- Build and release depend on external PyPI/network and GitHub environment configuration.
- There is no documented rollback or package yanking procedure.
