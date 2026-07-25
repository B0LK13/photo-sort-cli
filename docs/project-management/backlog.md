# Backlog

Items below are derived from repository evidence. `ready` means the scope is sufficiently defined to implement; `proposed` means discovery or a decision is still needed.

## CORE-001 — Verify the primary workflow end to end

**Priority:** p0-critical  
**Status:** ready  
**Category:** core  
**Roadmap phase:** phase-1-mvp  
**Complexity:** large

### Objective

Test and harden scan → plan → execute behavior using disposable directories.

### Current state

`cli.main`, `scan_directory`, `build_plan`, and `Executor.run` are connected, but only scanner parsing is tested.

### Scope

- Add temporary-directory tests for dry-run, move, copy, collision, skipped files, and errors.
- Assert counts, destinations, and JSONL records.
- Document any intentionally non-transactional behavior.

### Acceptance criteria

- Success and failure paths run without manual inspection.
- Dry-run does not mutate input files.
- Move/copy and log output are asserted.
- Tests pass with the documented command.

### Validation

`uv run pytest tests/ -q` plus the targeted integration tests.

### Relevant files

`src/photo_sort/cli.py`, `planner.py`, `executor.py`, `tests/`.

## CORE-002 — Define scanner scope and destination safety

**Priority:** p1-high  
**Status:** ready  
**Category:** core  
**Roadmap phase:** phase-1-mvp  
**Complexity:** medium

### Objective

Make non-recursive scanning and `--format` behavior explicit and tested.

### Acceptance criteria

- Recursive vs non-recursive behavior is an intentional documented choice.
- Valid token formats are specified and tested.
- Invalid or unsafe formats produce a controlled error.
- No destination escapes the selected root unless explicitly supported.

### Relevant files

`src/photo_sort/scanner.py`, `src/photo_sort/planner.py`, `src/photo_sort/cli.py`.

## CORE-003 — Implement or rename undo-log behavior

**Priority:** p1-high  
**Status:** proposed  
**Category:** core  
**Roadmap phase:** phase-2-reliability  
**Complexity:** medium

### Objective

Resolve the mismatch between “undo log” language and the absence of an undo command.

### Acceptance criteria

- Either a tested inverse command exists, or user-facing docs call the file an operation log and remove undo claims.
- Copy and move semantics are unambiguous.
- Partial failures are represented accurately.

## TEST-001 — Expand behavioral test coverage

**Priority:** p0-critical  
**Status:** ready  
**Category:** testing  
**Roadmap phase:** phase-1-mvp  
**Complexity:** large

Add tests for EXIF, mtime fallback, planner templates, executor side effects, CLI errors, and a clean-install smoke workflow. Acceptance is coverage of all public CLI options and each major module with passing local and CI runs.

## TEST-002 — Add repository quality checks

**Priority:** p1-high  
**Status:** proposed  
**Category:** testing  
**Roadmap phase:** phase-0-foundation  
**Complexity:** medium

Choose and configure formatter/linter/type-check/markdown-link checks, then run them in CI. Do not claim coverage until the chosen tools execute successfully.

## SEC-001 — Validate mutation and output paths

**Priority:** p1-high  
**Status:** ready  
**Category:** security  
**Roadmap phase:** phase-2-reliability  
**Complexity:** medium

Validate format-derived destinations and log paths, define symlink behavior, and add traversal/collision tests. Acceptance requires unsafe inputs to fail closed without unintended writes.

## SEC-002 — Add dependency and release security checks

**Priority:** p2-medium  
**Status:** proposed  
**Category:** security  
**Roadmap phase:** phase-3-release-readiness  
**Complexity:** medium

### Objective

Add a repeatable dependency/advisory check and review release-action permissions.

### Current state

The repository has `uv.lock` and pinned major GitHub Actions, but neither workflow defines a security scan job. The publish workflow requests `id-token: write`, and external PyPI configuration is unverified.

### Business value

Reduce the chance of publishing a vulnerable dependency or granting broader release permissions than intended.

### Technical rationale

The package executes on user files and is published through automation; dependency and workflow integrity are part of the delivery boundary.

### Acceptance criteria

- A selected dependency/advisory tool runs in CI.
- Action permissions and secret scope are documented.
- The release workflow is reviewed in a pull request and its result is recorded.

### Validation

Run the selected security command in CI and inspect the workflow permission summary.

### Relevant files

`.github/workflows/ci.yml`, `.github/workflows/publish.yml`, `pyproject.toml`, `uv.lock`.

## OPS-001 — Define recovery procedure

**Priority:** p1-high  
**Status:** proposed  
**Category:** operations  
**Roadmap phase:** phase-2-reliability  
**Complexity:** medium

Provide and test a restore/undo workflow or explicitly document that recovery requires an external backup. Acceptance includes a disposable fixture drill.

## OPS-002 — Add structured execution summary

**Priority:** p2-medium  
**Status:** proposed  
**Category:** operations  
**Roadmap phase:** phase-2-reliability  
**Complexity:** medium

Define stable exit codes and machine-readable summary output for performed, skipped, and failed operations.

## DEPLOY-001 — Verify package build and clean install

**Priority:** p1-high  
**Status:** blocked  
**Category:** deployment  
**Roadmap phase:** phase-3-release-readiness  
**Complexity:** medium

Run `uv build`, inspect artifacts, and install them in a clean environment. Current blocker: network/DNS prevented fetching Hatchling during this review.

## DEPLOY-002 — Consolidate release workflow behavior

**Priority:** p1-high  
**Status:** proposed  
**Category:** deployment  
**Roadmap phase:** phase-3-release-readiness  
**Complexity:** medium

Resolve overlapping tag workflows, document permissions/secrets, and add release rollback guidance.

## ARCH-001 — Preserve a verified architecture record

**Priority:** p2-medium  
**Status:** ready  
**Category:** architecture  
**Roadmap phase:** phase-0-foundation  
**Complexity:** small

Keep architecture docs aligned with the four-module pipeline and record future structural decisions in the decision log.

## DOC-001 — Maintain evidence-backed documentation

**Priority:** p1-high  
**Status:** in-progress  
**Category:** documentation  
**Roadmap phase:** phase-0-foundation  
**Complexity:** medium

Validate links, directory coverage, and status claims whenever implementation changes.

## DEBT-001 — Resolve dry-run directory side effect

**Priority:** p1-high  
**Status:** ready  
**Category:** technical-debt  
**Roadmap phase:** phase-1-mvp  
**Complexity:** small

`Executor.run` calls `os.makedirs` before checking `dry_run`; decide and test whether dry-run may create destination directories, then align code and docs.

## DEBT-002 — Add explicit quality-tool configuration

**Priority:** p2-medium  
**Status:** proposed  
**Category:** technical-debt  
**Roadmap phase:** phase-0-foundation  
**Complexity:** small

Add pinned tool configuration and CI checks for the selected formatter/linter/type checker.

## CORE-004 — Add recursive scanning

**Priority:** p3-low  
**Status:** proposed  
**Category:** core  
**Roadmap phase:** phase-4-expansion  
**Complexity:** medium

Only implement after the non-recursive contract is tested; define symlink, destination, and duplicate behavior first.

## UI-001 — Implement the proposed TUI

**Priority:** p4-future  
**Status:** deferred  
**Category:** user-interface  
**Roadmap phase:** phase-4-expansion  
**Complexity:** large

`TUI_DESIGN.md` describes a Textual design, but no TUI source or dependency exists. Revisit after MVP and safety validation.
