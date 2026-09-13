# Architecture

```
source packet → adapt() → atom → classify() → semion.frame.v0
                                              ↓
                                    frame_to_semiosis()
                                              ↓
                         SemiosisFrame-shaped dict (export only)
```

Router home: `yggdrasil.belief`. Mixed slang+sign hits Hyperlex first. Mixed tradition+sign hits Athanor first.

No circular import of Abraxas. No `source_space` invention in this package.

## Workflow-derived architecture — advisory target

Read [workflows](specs/workflows.md) before implementing these boundaries. Current code is the small pipeline above, not a completed service or encoder. Proposed validation and evidence components are not shipped.

| Component | Workflow responsibility | Contract / boundary |
|---|---|---|
| Shared input/denial validation | WF-001, WF-002; applied at every public entry, including CLI direct classify | CON-001; no adapter-only bypass |
| T0 classifier | WF-003; deterministic relation and evidence classification | CON-002; never executes interpretants |
| Export bridge | WF-004; validate then emit one inert dictionary | CON-003; external consumer owns runtime chain |
| Operator-side label/snapshot tools | WF-005, WF-006, WF-010 | CON-004/CON-005; private data, immutable revisions; not imported by T0 |
| Offline evaluation/review | WF-007, WF-008 | CON-005/CON-006; pinned features and evidence, no activation |
| Authorized handoff preparation | WF-009 | CON-006; recipient scope and bytes validated independently |

Keep T0 dependency-light and network-free. Do not add required torch/transformers, a database service, queues or cloud infrastructure to satisfy documentation structure. CLI and library must share validated behavior. Raw source/label evidence stays outside the unchanged v0 output as sidecar references pending a separately reviewed contract change.

Validate packaging in an isolated installed wheel: current __main__.py reads a repository-relative VERSION that may not ship. Performance SLO, external consumer compatibility, real router deployment and T1 architecture are NOT_COMPUTABLE. No model/backbone choice is made until DEC-001/DEC-006 and a separate encoder cycle.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
