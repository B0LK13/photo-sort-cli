# Security Backlog

## SEC-001 — Constrain filesystem mutation inputs

**Priority:** p1-high  
**Status:** ready  
**Evidence:** `--format` is string-substituted and joined to the input root; executor creates directories and mutates paths.  
**Acceptance criteria:** traversal, absolute-path, symlink, collision, and dry-run cases are specified, tested, and fail safely.

## SEC-002 — Add dependency and release security checks

**Priority:** p2-medium  
**Status:** proposed  
**Evidence:** no security scan job is present in either workflow.  
**Acceptance criteria:** choose a supported dependency/advisory check, document action pinning and secret permissions, and verify it in CI.
