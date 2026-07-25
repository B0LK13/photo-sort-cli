# Technical Debt

## DEBT-001 — Dry-run directory creation

**Location:** `src/photo_sort/executor.py`  
**Reason:** directory creation occurs before the dry-run branch.  
**Impact:** dry-run may alter filesystem structure.  
**Future risk:** users may assume preview mode is side-effect free.  
**Remediation:** define and test dry-run side effects; move directory creation into real execution if appropriate.  
**Related:** `DEBT-001`.  
**Status:** open.

## DEBT-002 — No configured quality tooling

**Location:** `pyproject.toml`, `.github/workflows/ci.yml`  
**Reason:** CI only runs pytest and coverage upload.  
**Impact:** style, type, documentation, and security regressions are not automatically checked.  
**Future risk:** maintenance and release defects reach main unnoticed.  
**Remediation:** `TEST-002`.  
**Related:** `DEBT-002`.  
**Status:** open.

## DEBT-003 — Undo terminology mismatch

**Location:** `README.md`, `src/photo_sort/executor.py`  
**Reason:** log records operations but no undo implementation is present.  
**Impact:** users may overestimate recovery capability.  
**Future risk:** data loss or incorrect manual reversal.  
**Remediation:** `CORE-003`.  
**Related:** `CORE-003`.  
**Status:** open.

## DEBT-004 — Partial module test coverage

**Location:** `tests/`  
**Reason:** initial tests focus on scanner parsing.  
**Impact:** planner, executor, and CLI changes lack regression protection.  
**Future risk:** filesystem mutations regress silently.  
**Remediation:** `TEST-001`.  
**Related:** `TEST-001`.  
**Status:** open.
