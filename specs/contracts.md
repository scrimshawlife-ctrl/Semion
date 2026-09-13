# Contract catalog

Status: PROPOSED, not runtime migration. Existing schemas remain unchanged. Contracts below specify validation behavior for a separate engineering cycle; unresolved DEC entries block affected claims.

## CON-001 Input and normalized atom

Entry points accept one JSON object, never an array/string/null root. Proposed limits: UTF-8 request <=64 KiB, representamen/sign_form <=512 Unicode code points, other text fields <=2048 code points, source ids <=256 code points, inventory arrays <=100 items each; reject before expensive processing. These are implementation-review targets, not measured current limits.

Accepted payload_class is sign_atom or corpus_atom; absent payload permits legacy atom/source-shape validation. An unknown nonempty class is denied. Reject forecast_request, settled_forecast, bare slang_atom and tradition_atom consistently at every entry point. Mixed-domain routing remains upstream.

Aliases: sign_form, representamen, raw_value, input_signal.raw_value; sign_content or input_signal.information_content; object_candidate or object; interpretant_candidate or interpretant.action_type; classification or sign_class or inventory. Presence, not truthiness, determines selection. Contradictory non-null aliases are an input conflict, not silently selected. Missing optional object/interpretant is null. Empty representamen cannot produce a sign.

Typed sign_inventory has optional icons/indexes/symbols arrays of structural entries; one nonempty bucket gives its class, multiple buckets mixed, none NC absent a valid explicit label. Bucket population is not independent proof of label correctness. Reject invalid bucket types. Preserve original source locator and raw content hash outside the unchanged frame rather than forging schema fields.

Batch adapter must specify UTF-8, blank-line skip, input row position, accepted/refused/invalid counts and per-row outcomes. Proposed batch default is fail whole batch on malformed JSON, retaining diagnostic position and no committed partial output; any later partial mode must be explicitly named.

## CON-002 Frame

Current shape is schemas/semion.frame.v0.schema.json, duplicated in contracts/semion.frame.v0.json. Proposed semantic validator additionally requires all frame fields emitted by classify, including brier=null and failure.

is_sign=true requires nonempty representamen, computable class, failure=null, and actual object or supported label evidence. corpus_ref presence alone is insufficient. sign_class=NOT_COMPUTABLE implies is_sign=false. A refused frame has NC class/epistemic, failure=SPECIALIST_LANE_VIOLATION, no interpretant and false/null lanes. Missing evidence has a bounded NC reason and no invented reference.

OBSERVED for a class requires the approved DEC-005 rubric and verifiable label evidence; an input label or source string alone is not proof. Heuristic labels are INFERRED. Explicit NC precedence and conflicting label semantics remain DEC-003. Raw arbitrary interpretant prose must not be promoted to executable action.

Malformed input produces an input error envelope with code INVALID_INPUT, field/path and bounded reason, not a schema-invalid v0 frame. CLI should print structured error to stderr and nonzero exit; no traceback, raw restricted payload, or partial successful frame. Exit 0 indicates valid processing (including bounded abstention/refusal), not positive sign or authorization. These error-envelope and exit semantics are proposed, not shipped.

## CON-003 Export

Input must satisfy CON-002, not merely be an arbitrary dict. Preserve representamen -> input_signal.raw_value; corpus_ref -> frame_id (null allowed); is_sign/promotion_reason -> sign_status; object and sign_class; epistemic/failure -> provenance. Frozen lanes remain false/false/null.

Refusal or NC yields is_sign=false and action_type=NOT_COMPUTABLE. Known successful action prefixes may only be mapped under DEC-004. STATE_UPDATE:alert is currently copied by tests; splitting it into action_type plus state_delta is a proposal awaiting the consumer schema, not a backwards-compatible fact.

Omit source_space, target_space, focus_of_attention. Do not invent interpreter identity. Empty state_delta/external_effect/new_knowledge_units are inert placeholders in the current bridge, not proof of real updates. Unknown consumer schema: compatibility NOT_COMPUTABLE. A SemiosisFrame.v1 string alone proves no external schema conformance.

## CON-004 Label and row evidence

Existing dataset row fields remain as shipped. Proposed sidecar per row: row_id, content_sha256, source_locator, source_lane, source_run_id or explicit unavailable reason, label_decision_id/revision, reviewer_ref, operator_approval_ref when settlement occurs, label_evidence_refs, rights_evidence_refs, epistemic, eligibility, supersedes and UTC decision time.

No unknown source identity or rights decision may silently become verified. NC implies gold_is_sign=false; positive gold_is_sign requires computable class and nonempty representamen. Weak/held/rejected membership stays outside gold. Source-lane presence is required for eligible selection even though v0 schema makes it optional. Sidecar links use exact content hashes to avoid changing v0 under this documentation patch.

## CON-005 Snapshot and evaluation

Manifest: schema/version, snapshot_id, parent_snapshot_ref, selected row id/hash/split/group entries, exclusion reasons, grouping/normalization version, source and class counts, epistemic counts, split hashes, quality check statuses, effective input fields, created_at and scope refs. Sort entries by row_id; hash canonical UTF-8 JSON with sorted keys and compact separators, no NaN. Hash raw artifact bytes separately; record hash kind to avoid confusing content-normalized and raw hashes.

Existing floors: train>=300, val>=50, test>=100; icon/index/symbol >=15% each and mixed/NC >=8% each on selected gold pool. NC not in train under current HQ quality bar; train symbol share <=0.85. These coexist and can block small HQ subsets; do not waive either. Data targets are not minimum proof of correctness. Report exact row/sign_form/source_run/provenance overlap; near-duplicate pass awaits DEC-007 grouping rule. Freeze before candidate experimentation and disallow train/test group overlap.

Benchmark output: model/code/config hashes, snapshot+feature-protocol hashes, ordered row predictions/targets, count correct and evaluated, confusion matrix, support per class and mixed/missing-object/refusal slices, failures, dual-use outcomes. Exact-match=correct/evaluated; evaluated=0 -> NOT_COMPUTABLE. Candidate must strictly exceed T0 on identical approved feature view to satisfy the existing comparison condition; a numeric tie fails. A statistical margin is not invented. Adaptation label fidelity is a separately named test, never substituted for predictive accuracy. Gold targets/classification/sign_class must not enter predictive features under the proposed DEC-006 protocol.

## CON-006 Receipt and handoff evidence

Proposed receipt: receipt_id, workflow_id, attempt_id, started_at/finished_at in valid UTC, status, input/config/code/output hash references, counts, bounded errors, evidence status and supersedes. No finish earlier than start. Failure requires reason. PASS requires evidence, not an empty list. Unknown measurement -> status NOT_COMPUTABLE, value null, reason required. Hash strings are lowercase SHA256, 64 hex digits.

Handoff manifest additionally lists approved recipient/purpose, exact approval reference, each safe relative path and byte hash, snapshot reference, rights restrictions, exclusions and verification instructions. No absolute operator paths, secrets, raw private corpus text or temporary signed URLs in public receipts. Missing/invalid scope prevents transfer; a review receipt never functions as an executable permission token.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)

