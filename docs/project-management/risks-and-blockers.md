# Risks and Blockers

## RISK-001 — Unverified filesystem mutation semantics

**Category:** security  
**Probability:** medium  
**Impact:** high  
**Severity:** high  
**Evidence:** `Executor.run` creates destination directories before its dry-run branch; format paths are not constrained by tests.  
**Mitigation:** implement `SEC-001` and `DEBT-001`.  
**Contingency:** use dry-run/copy on backups and stop real execution for unexpected plans.  
**Status:** open  
**Related:** `SEC-001`, `DEBT-001`.

## RISK-002 — Recovery is not implemented

**Category:** operations  
**Probability:** medium  
**Impact:** high  
**Severity:** high  
**Evidence:** JSONL entries are written, but no inverse command exists.  
**Mitigation:** `CORE-003`, `OPS-001`.  
**Contingency:** preserve originals and use external backups.  
**Status:** open  
**Related:** `CORE-003`, `OPS-001`.

## RISK-003 — Release build cannot be locally verified

**Category:** deployment  
**Probability:** high in restricted environments  
**Impact:** medium  
**Severity:** high  
**Evidence:** `uv build` failed fetching Hatchling because DNS resolution was unavailable.  
**Mitigation:** run in a networked CI environment and add clean-install evidence.  
**Contingency:** do not publish a new release until a tag build succeeds.  
**Status:** blocked externally  
**Related:** `DEPLOY-001`.

## RISK-004 — Test coverage is narrow

**Category:** testing  
**Probability:** high  
**Impact:** medium  
**Severity:** high  
**Evidence:** only `tests/test_scanner.py` exists; 16 passing tests cover scanner parsing.  
**Mitigation:** `TEST-001`.  
**Contingency:** require manual dry-run review for changes affecting execution.  
**Status:** open  
**Related:** `TEST-001`.
