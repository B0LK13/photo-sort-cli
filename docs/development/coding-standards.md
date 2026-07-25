# Coding Standards

Observed conventions:

- PEP 8-oriented Python formatting.
- Type annotations and `from __future__ import annotations` in source modules.
- Small modules organized by scan, plan, and execute responsibilities.
- Docstrings on public functions and the `MoveOp`/`FileInfo` data classes.
- pytest tests with parametrization for filename cases.

No lint or formatting tool is configured. A future tooling change should add the tool, pin its configuration, and add a CI check rather than documenting an unexecuted command (`DEBT-002`).
