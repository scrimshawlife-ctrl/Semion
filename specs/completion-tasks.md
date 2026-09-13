# Prioritized completion tasks

All tasks are PROPOSED, not implemented by this documentation PR. Existing operator authority controls any corpus writes, training, handoff, consumer or publication. Owners: repository maintainer for T0, existing corpus/evaluation reviewer for data/eval, operator for consequential approval.

| ID | Priority | Workflow | Deliverable | Concrete files/surface | Dependencies |
|---|---|---|---|---|---|
| TASK-001 | P0 | WF-001 | Typed shared input validation, alias conflicts, deterministic JSONL failure and limits | src/semion/adapt.py; shared validator; tests | DEC-007 only for later private storage; input policy can be reviewed independently |
| TASK-002 | P0 | WF-002 | Unify denial across adapter, direct classify, CLI and export; benign and hostile controls | src/semion/classify.py, adapt.py, compat.py; tests | TASK-001 |
| TASK-003 | P0 | WF-003 | Implement approved epistemic and class precedence with frame semantic validation | src/semion/classify.py; validation; tests | TASK-001, TASK-002; DEC-003, DEC-005 |
| TASK-004 | P1 | WF-004 | Pin external consumer schema and validate inert export with closed action mapping | src/semion/compat.py; contract fixtures; tests | TASK-003; DEC-004 |
| TASK-005 | P1 | WF-005 | Implement reviewed label/rights sidecars and separate eligible/weak/held outcomes | separate operator-approved corpus tooling; synthetic fixtures only in git | DEC-005, DEC-007; separate gold-settle scope |
| TASK-006 | P1 | WF-006 | Validate selected-snapshot floors, groups, provenance and immutable split hashes | separate snapshot tooling; synthetic manifests and tests | TASK-005; DEC-002, DEC-007 |
| TASK-007 | P2 | WF-007 | Freeze fair evaluation protocol and build scorer, no training in same packet/schema cycle | separate evaluation tools and fixtures; no required ML dependencies | TASK-003, TASK-006; DEC-001, DEC-006 |
| TASK-008 | P2 | WF-008 | Produce condition-by-condition E-S3 advisory report without opening any gates | evaluation receipt and existing operator review surface | TASK-007; DEC-001, DEC-008 |
| TASK-009 | P2 | WF-009 | Verify safe bundle/recipient scope and installed distribution behavior before authorized handoff | handoff validator; isolated wheel/CLI smoke tests; no corpus in repo | TASK-006, TASK-008; DEC-007, DEC-008 |
| TASK-010 | P1 | WF-010 | Implement append-only correction and stale-result impact analysis; reconcile documentation links | correction tooling; synthetic regression tests; affected spec docs | TASK-005, TASK-006; DEC-007, DEC-008 |

## Definition of ready and done

Ready: referenced decisions closed with evidence, workflow reviewed, contract pinned, scope approved, positive/negative/recovery fixtures specified. Done: associated AC passes at an exact commit, existing regression tests pass, no frozen-lane expansion, sanitized receipt attached, traceability status updated with real evidence. Tests that merely prove the current bug exists cannot close target acceptance.

Sequence: T0 TASK-001 -> TASK-002 -> TASK-003 -> TASK-004. Data TASK-005 -> TASK-006 -> TASK-010 only under separate scope. Evaluation TASK-007 -> TASK-008, then TASK-009. Keep encoder implementation separate from packet/schema changes under constitution X. No new issues, milestone or Loop slice is invented by this plan; Loop 805/Sprint 001 applicability to this repo is N/A until an actual operator reference is provided.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
