# Data model and lifecycle

## Existing storage

Runtime functions consume dicts and return dicts. Git contains schemas, seed fixtures and documentation, not the private corpus. Earlier spine atoms.jsonl and later dataset.jsonl name different artifacts; do not rename or import either. The latest reported gold SoT is the private dataset.jsonl plus separate keep_weak.jsonl. Its content is NOT_COMPUTABLE here.

## Proposed logical relations

| Relation | Key / references | Lifecycle and validation |
|---|---|---|
| SourceEvidence | source_id, raw content hash, source lane, locator, rights refs | Append observed source evidence; source existence is separate from class truth |
| AtomProjection | row_id + content hash -> SourceEvidence | Typed field projection per CON-001; cannot overwrite source |
| LabelDecision | decision id/revision -> row hash, evidence, reviewer, approval | ELIGIBLE/WEAK/HELD/REJECTED; preserve epistemic; correction links supersedes |
| Snapshot | snapshot id/hash -> selected row hashes and decisions | Immutable FROZEN membership; split/group assignment and exclusions explicit |
| Evaluation | evaluation id -> snapshot, engine, config, feature protocol | Predictions and support retained; stale after dependent correction |
| Handoff | handoff id -> snapshot/artifact hash manifest and scope | VERIFIED/DELIVERED/ACKNOWLEDGED distinct; receipt not authority |

No database engine is mandated. A local append-only JSON/JSONL sidecar implementation is sufficient if atomic replacement of a new manifest is verified and prior snapshots remain unchanged. This is a proposal, not new storage or migration in this patch.

## Identity and atomicity

row_id is a stable locator; content_sha256 changes when text, label-bearing source, or normalization changes. Decisions reference exact content. Reject duplicate row_id with differing bytes within a snapshot; exact duplicate content is reviewed/grouped, not counted repeatedly to meet floors. Freeze writes a new manifest atomically only after all checks; interrupted attempts leave no FROZEN receipt. Corrections create a new revision and invalidate dependent claims.

## Privacy and retention

Private payloads remain in operator-controlled storage; Git receives schema/fixture and sanitized evidence only. No deletion schedule is invented: DEC-007 must establish retention and access before implementation. Rights withdrawal blocks further distribution while the operator decides lawful retention of existing evidence. No home directory is inspected, migrated or modified by these specs.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)

