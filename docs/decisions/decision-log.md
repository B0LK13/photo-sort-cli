# Decision Log

## ADR-001 — Preserve the existing `src` package layout

**Date:** 2026-07-25  
**Status:** accepted  
**Context:** The package uses Hatchling with `src/photo_sort`, and the console entry point is `photo_sort.cli:main`.  
**Decision:** Keep application code in `src/photo_sort` and tests in `tests`; add documentation around the existing layout rather than moving Python modules.  
**Alternatives considered:** Move to `apps/`, split into packages, or flatten source.  
**Rationale:** The current layout is framework/package compatible and small; moving it would add import and build risk without evidence of a need.  
**Consequences:** The repository remains a compact Python package; responsibilities are documented by module and directory.  
**Reversal conditions:** A second deployable application, service boundary, or packaging constraint emerges.  
**Related files:** `pyproject.toml`, `src/photo_sort/`, `tests/`.  
**Related backlog:** `ARCH-001`.

## ADR-002 — Treat TUI design as proposed, not implemented

**Date:** 2026-07-25  
**Status:** accepted  
**Context:** `TUI_DESIGN.md` specifies Textual screens and modules, but no TUI source files or Textual dependency are present.  
**Decision:** Document the TUI as future work and defer it until core workflow and safety tests are complete.  
**Alternatives considered:** Classify the design as a current subsystem or create empty scaffold files.  
**Rationale:** Empty scaffolding would misrepresent project status.  
**Consequences:** The current architecture remains CLI-only; the TUI has a clear future backlog item.  
**Reversal conditions:** Textual dependency and implementation land with tests.  
**Related files:** `TUI_DESIGN.md`, `src/photo_sort/`.  
**Related backlog:** `UI-001`.

## ADR-003 — Do not restructure application files during documentation pass

**Date:** 2026-07-25  
**Status:** accepted  
**Context:** The repository is small, existing imports and Hatchling configuration are coherent, and the request prioritizes accurate documentation.  
**Decision:** Add documentation and directory READMEs while preserving application paths and framework-required names.  
**Alternatives considered:** Introduce `apps/`, `packages/`, and infrastructure directories.  
**Rationale:** Those folders would be empty or speculative for a local CLI and would increase migration risk.  
**Consequences:** The structure stays minimal and current-state accurate.  
**Reversal conditions:** New applications, services, or independently released packages are added.  
**Related files:** repository root, `src/`, `tests/`.  
**Related backlog:** `ARCH-001`, `DOC-001`.
