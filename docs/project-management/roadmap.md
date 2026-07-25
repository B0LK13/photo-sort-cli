# Roadmap

No dates are assigned; phases are dependency-driven.

## Phase 0 — Foundation (`in-progress`)

Objective: make the small package understandable and repeatably verifiable. Deliverables are the current documentation set, repository map, baseline tests, and documented CI gaps. Exit when docs links and directory coverage validate and the local test command is repeatable. Related: `DOC-001`, `ARCH-001`, `TEST-002`.

## Phase 1 — MVP workflow (`partially-verified`)

Objective: verify the end-to-end scan → plan → dry-run/execute workflow on disposable directories. Deliver planner/executor/CLI tests, explicit behavior for collisions and logging, and a tested package-install smoke path. Exit when success and failure paths are automated. Related: `CORE-001`, `CORE-002`, `CORE-003`, `TEST-001`.

## Phase 2 — Reliability and safety (`proposed`)

Objective: make filesystem mutation safer and operationally diagnosable. Deliver format/log path validation, structured summaries, clearer partial-failure semantics, and a tested recovery workflow. Exit when destructive-path cases and recovery are tested. Related: `SEC-001`, `OPS-001`, `OPS-002`.

## Phase 3 — Release readiness (`proposed`)

Objective: establish repeatable package builds and unambiguous tag publication. Deliver offline/CI build evidence, clean-install smoke tests, workflow consolidation, and release rollback guidance. Exit when a tag build and publish dry run are verified in GitHub. Related: `DEPLOY-001`, `DEPLOY-002`.

## Phase 4 — Expansion (`future`)

Objective: add user-valued capabilities only after the core workflow is verified. Candidates include recursive scanning and the TUI proposed in `TUI_DESIGN.md`. Related: `CORE-004`, `UI-001`.
