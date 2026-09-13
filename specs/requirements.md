# Requirements

Status: proposed acceptance targets, not a claim of current implementation. Existing constitution controls. DEC-001 through DEC-008 remain open; affected behavior may be specified as a proposal but not treated as ratified. Verification status is in traceability.json.

| ID | Existing spec | Required target behavior | Workflow |
|---|---|---|---|
| REQ-001 | 000/002 | Accept only a JSON object with supported source shape and typed fields; malformed or oversized inputs yield a bounded input error without a traceback or partial success. | WF-001 |
| REQ-002 | 002 | Normalize supported aliases deterministically, preserve source identity and explicit nulls, and report conflicting aliases; adaptation must not upgrade epistemic evidence. | WF-001 |
| REQ-003 | 000/001/002 | Apply the same route rejection at direct classify, adapter, batch, and export entry points; forecast, settled forecast, bare slang/tradition and unknown nonempty payload classes must not become positive signs. | WF-002 |
| REQ-004 | 000/003 | Restricted-intent or malformed outputs remain non-sign with inert interpretant and hard false/null lanes; preserve a bounded reason without reproducing restricted instructions. | WF-002 |
| REQ-005 | 001 | Classify deterministically with explicit, reviewed precedence for valid labels, explicit NC, and heuristic hints; is_sign needs representamen plus object or actual supported label, not a reference alone. | WF-003 |
| REQ-006 | 000/001 | Carry label epistemic independently of source reference; missing or weak evidence cannot become OBSERVED. Every output obeys frozen false/null lanes and consistent failure/is_sign fields. | WF-003 |
| REQ-007 | 003 | Validate a frame before export; preserve refusal, triad fields and source references, and map action values only according to a pinned consumer contract. | WF-004 |
| REQ-008 | 003 | Export one data structure without importing Abraxas or writing runes, source_space, target_space, focus_of_attention, or runtime state; do not claim SemiosisFrame conformance until consumer validation exists. | WF-004 |
| REQ-009 | 004 | Bind each label to exact row content, source lane, rights evidence, epistemic, reviewer and decision revision; lawful inferred gold must remain labeled INFERRED. | WF-005 |
| REQ-010 | 004 | Exclude keep_weak from gold and exclude TEACH raw abstract/slang/tradition/forecast inputs from automatic gold; NC implies gold_is_sign=false. Report held and rejected rows separately. | WF-005 |
| REQ-011 | 004 | Freeze immutable row/split hashes and group related sources before evaluation; recompute floors on the actually selected subset and preserve holdout assignments. | WF-006 |
| REQ-012 | 004 | Measure the existing 300/50/100 split and class-floor rules separately from quality; report NC distribution, exact/near-duplicate leakage, source overlap and exclusions. Unknown checks cannot PASS. | WF-006 |
| REQ-013 | 004 | Score pinned T0 and any separately authorized candidate using identical approved feature views without target-label leakage; retain row predictions and per-class support. | WF-007 |
| REQ-014 | 004 | Report exact-match, class confusion, mixed/missing-object/refusal slices, failures and model/config/data hashes; absent candidate or frozen benchmark yields NOT_COMPUTABLE, not a fabricated score. | WF-007 |
| REQ-015 | 000/004 | Evaluate E-S3 from independent dataset, comparison, dual-use and exact operator evidence; an artifact name, delivery, or recorded count never opens the gate. | WF-008 |
| REQ-016 | 000/004 | Keep train, naming, Hub, router swap and canon decisions separate and action-scoped; no runtime or release mutation follows from this specification review. | WF-008 |
| REQ-017 | 004 | Prepare only recipient- and purpose-approved artifacts; manifest hashes, selected snapshot, restrictions, verification instructions and excluded data must accompany a handoff. | WF-009 |
| REQ-018 | 000/004 | Verify handoff bytes and receipt independently, retain no secrets in public receipts, and never interpret transfer or acknowledgement as train/Hub permission. | WF-009 |
| REQ-019 | 000/004 | Correct labels or leakage with immutable superseding decisions, preserve prior snapshot identity, and mark dependent evaluations stale. | WF-010 |
| REQ-020 | 000/004 | Propagate every approved correction through requirements, workflow, contract, acceptance, traceability and task references; notify the existing operator of impacted handoffs without silently altering external systems. | WF-010 |

## Nonfunctional requirements

Determinism is exact semantic JSON equality on repeated identical input with pinned engine/config. Input resource budgets are proposed in CON-001; do not assert a measured throughput or latency SLO. Local processing must not require network, credentials, corpus-home access, or ML dependencies. Evidence records must be bounded and exclude payload text by default. Installed CLI/package verification is required before distribution. Platform coverage beyond actually run environments is NOT_COMPUTABLE.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
