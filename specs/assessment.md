# Evidence-backed assessment

## Boundary

OBSERVED repository base: e5ed91bd90afb0429cf816504c7d5e622bbbc153. Advisory documentation only; root constitution, its mirror, runtime, runtime schemas, fixtures, training, Hub, and Notion are unchanged. One conceptual change: specification reconciliation and completion. Encoder implementation must remain a separate cycle.

## Evidence packet

- OBSERVED: five numbered specs exist, but workflows were four spine bullets with no stable IDs, complete exceptions, state contracts, or end-to-end traceability.
- OBSERVED: full code graph built under project Semion: 620 nodes and 801 edges at the base. Graph resolution found adapt, classify, and frame_to_semiosis. Counts describe indexing, not correctness.
- OBSERVED: nine existing local tests pass on Python 3.12. The baseline is smoke coverage, not a full contract proof.
- OBSERVED: README's 482/330/50/102 and keep_weak 150 conflict with later STATUS, dataset note, and Notion handoff's 452/300/50/102 and keep_weak 180.
- OBSERVED: the Notion handoff reports pack SHA256 af83977d1251b7f62b07a184f14fc34c52b603a4c54406609fb247f43f6156c8 and gold_hq 242. Native Notion verification was unverified. Attachment contents and hash were not independently validated.
- INFERRED: 452 is the latest reported snapshot, not a measured local dataset. The 242-row subset alone cannot meet a 300-row train floor, before even reserving holdouts.
- OBSERVED: root constitution is fuller than its abbreviated mirror; this patch references the root without amending either.
- OBSERVED: milestones and old checklists describe different dates; Abraxas router swap and consumer activation cannot be verified from this repo.

## Reproduced runtime gaps

| ID | Evidence at base | Consequence / next task |
|---|---|---|
| GAP-001 | classify accepts bare slang_atom with flag + symbol label as a sign | Spec 001 route rejection differs from adapter; TASK-002 |
| GAP-002 | sign_form=smoke + corpus_ref=unverified yields OBSERVED and is_sign=true without object or label | A reference is not evidence or a corpus label; TASK-003 |
| GAP-003 | explicit classification=NOT_COMPUTABLE + smoke/fire becomes index and OBSERVED | Abstention precedence needs a decision and test; TASK-003, DEC-003 |
| GAP-004 | dataset schema accepts NC with gold_is_sign=true | Cross-field rules missing; TASK-006 |
| GAP-005 | classify calls lower on caller classification without a type guard; output validation is absent | Malformed input can crash or violate frame types; TASK-001 |
| GAP-006 | compat forwards free-text interpretant, and handles only two failure strings | Closed action mapping and consumer validation not proven; TASK-004 |
| GAP-007 | frame schema does not require brier or failure; dataset source_lane is optional | Structural validation alone cannot enforce all prose constraints; TASK-001 and TASK-006 |
| GAP-008 | CLI loads VERSION outside the package; wheel installation not tested | Installed CLI behavior NOT_COMPUTABLE; TASK-009 |

## Implementation-readiness

T0 is an existing prototype with nine passing tests. Target contract conformance is NOT_COMPUTABLE until the acceptance cases in acceptance.md run against a separately approved implementation. Corpus quality, floor satisfaction, effective training subset, legal eligibility, operator train authorization, T1 performance, external SemiosisFrame compatibility, live routing, and release readiness are NOT_COMPUTABLE.

No percentage-complete score is computed: artifact existence is not equivalent to coverage or acceptance.

## Sources

- [Pinned repository](https://github.com/scrimshawlife-ctrl/Semion/tree/e5ed91bd90afb0429cf816504c7d5e622bbbc153)
- [Semion HQ handoff](https://app.notion.com/p/3d83e8ba2f5c81608499deffc060160d), last edited 2026-09-12T00:58:21.253Z; source text only.
- Local paths: src/semion/classify.py, adapt.py, compat.py, __main__.py; schemas/; tests/; specs/004-encoder-gate/dataset.md.

## Recommended next advisory action

Review DEC-001 through DEC-008. Then implement TASK-001 through TASK-005 as bounded T0 work, with packet changes separate from any encoder cycle. Do not infer training permission from specification approval.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
