# Workflows

Status: proposed specification. This does not govern or activate. All 16 fields are mandatory. Existing runtime gaps are listed in assessment.md; these workflows describe target behavior, not claims of conformance.

## Registry

| ID | Purpose |
|---|---|
| WF-001 | Normalize existing source packet |
| WF-002 | Refuse out-of-lane and restricted requests |
| WF-003 | Classify a normalized sign atom |
| WF-004 | Export one compatible semiosis structure |
| WF-005 | Review corpus labels and eligibility |
| WF-006 | Freeze and validate selected dataset |
| WF-007 | Evaluate frozen T0 and candidate |
| WF-008 | Review existing encoder gates without activation |
| WF-009 | Prepare and verify authorized handoff |
| WF-010 | Correct labels, leaks, or stale evidence |

## WF-001

| Field | Specification |
|---|---|
| Purpose | Normalize existing source packet |
| Actors | Caller; adapter; existing source steward |
| Triggers | Explicit adapt call or one batch row |
| Preconditions | Existing source packet in scope; no scrape requested |
| Inputs | JSON object; aliases and typed inventories per CON-001 |
| Happy path | Check type and limits; check route first; detect alias conflicts; normalize selected fields; preserve provenance; return accepted atom |
| Alternate/failure paths | Malformed inventory/type returns input error; alias conflict is held for review; missing optional object stays null; rejected routes go to WF-002; a failed batch row cannot disappear |
| State transitions | SM-001: RECEIVED -> VALIDATING -> NORMALIZED; invalid -> INVALID; lane denial -> REFUSED |
| Terminal states | NORMALIZED, INVALID, REFUSED |
| Side effects | Return data only; proposed caller-owned receipt, no source write |
| Invariants | Normalization does not label GOLD or upgrade evidence; repeated input gives same result |
| Permissions | Existing caller's local read scope only; source harvesting is not implied |
| Observability/audit | CON-006 row index, source hash, schema/map version, status and bounded reason; no raw source in public logs |
| Acceptance criteria | AC-001 |
| Dependencies | REQ-001, REQ-002; CON-001; existing Spec 002 |
| Unresolved items | DEC-005 evidence mapping; proposed resource limits require implementation review |

## WF-002

| Field | Specification |
|---|---|
| Purpose | Refuse out-of-lane and restricted requests |
| Actors | Caller; adapter/classifier/export boundary |
| Triggers | Denied payload class, restricted action content, invalid frame, or failed upstream row |
| Preconditions | No authorization inferred from packet fields |
| Inputs | Original input classification and bounded error category, not executable instructions |
| Happy path | Identify denial before heuristics; return NC/non-sign; clear active interpretant; force forecast/phenomenal false and brier null; carry safe diagnostic |
| Alternate/failure paths | Unknown nonempty payload class refused; malformed JSON uses input error not a fake frame; benign structural discussion must remain allowed; batch refusal retained as an outcome |
| State transitions | SM-001: VALIDATING -> REFUSED; export validation failure -> INVALID |
| Terminal states | REFUSED or INVALID |
| Side effects | No routing execution or external retry; return bounded result |
| Invariants | No positive sign or actionable content in refused export; source evidence unchanged |
| Permissions | No special approval can be manufactured by a payload; existing doctrine bounds all callers |
| Observability/audit | Reason code and workflow id; restricted content excluded; counters distinguish invalid, NC and refusal |
| Acceptance criteria | AC-002 |
| Dependencies | REQ-003, REQ-004; CON-001, CON-002, CON-003; dual-use-gate.md |
| Unresolved items | DEC-004 consumer action contract; content rubric needs existing domain/security reviewer |

## WF-003

| Field | Specification |
|---|---|
| Purpose | Classify a normalized sign atom |
| Actors | Corpus user; T0 classifier; label reviewer for disputed labels |
| Triggers | Accepted atom sent to classify, including direct API/CLI calls |
| Preconditions | Boundary validated; reviewed label precedence required before target behavior ships |
| Inputs | Normalized atom and optional verified label-evidence context; CON-001 |
| Happy path | Validate direct input; preserve object null; select class by approved precedence; calculate is_sign from actual label/object evidence; attach honest epistemic; validate complete frame |
| Alternate/failure paths | No hint or insufficient relation gives NC; explicit NC proposed to abstain; conflicting label evidence held/NC; bad types produce bounded error; heuristic result never becomes OBSERVED solely from corpus_ref |
| State transitions | SM-001: NORMALIZED -> CLASSIFIED or ABSTAINED; VALIDATING -> INVALID/REFUSED |
| Terminal states | CLASSIFIED, ABSTAINED, INVALID, REFUSED |
| Side effects | One frame returned; no corpus/label mutation |
| Invariants | Flags false/null; references are not labels; inferred hints remain inferred; no psyche interpretation |
| Permissions | Read/classify only under existing T0 scope; label settlement requires existing operator authority |
| Observability/audit | Engine version, input hash, evidence refs, selected rule and outcome in caller-owned receipt |
| Acceptance criteria | AC-003 |
| Dependencies | REQ-005, REQ-006; CON-002; WF-001, WF-002 |
| Unresolved items | DEC-003 precedence and DEC-005 OBSERVED evidence semantics |

## WF-004

| Field | Specification |
|---|---|
| Purpose | Export one compatible semiosis structure |
| Actors | Integrator; export bridge; external Abraxas consumer maintainer |
| Triggers | Explicit export of one validated Semion frame |
| Preconditions | Frame schema and cross-field checks pass; consumer schema pin required for conformance claim |
| Inputs | CON-002 frame; CON-003 consumer mapping version |
| Happy path | Validate frame; preserve refusal; map representamen/object/class/reference and approved action representation; force frozen lanes; return dict |
| Alternate/failure paths | Unknown consumer version blocks conformance claim; invalid input rejected; any failed/NC frame suppresses action; missing corpus_ref remains null, never invented; consumer rejection returned to integrator |
| State transitions | SM-001: CLASSIFIED/ABSTAINED/REFUSED -> EXPORT_VALIDATING -> EXPORTED; invalid -> INVALID |
| Terminal states | EXPORTED or INVALID; compatibility may remain NOT_COMPUTABLE |
| Side effects | Return dict only; no import, network, runtime chain, or rune mint |
| Invariants | Do not create spaces/focus/interpreter identity; no actions executed |
| Permissions | Local export only; consumer activation is outside Semion and needs its own authority |
| Observability/audit | Consumer schema hash when available, frame hash, exporter revision, validation result |
| Acceptance criteria | AC-004 |
| Dependencies | REQ-007, REQ-008; CON-003; WF-002, WF-003 |
| Unresolved items | DEC-004 exact action mapping and external schema; DEC-008 consumer status |

## WF-005

| Field | Specification |
|---|---|
| Purpose | Review corpus labels and eligibility |
| Actors | Existing corpus reviewer; operator for gold-settle |
| Triggers | Explicit review of existing candidate rows, not an automatic harvest |
| Preconditions | Source rights and exact review scope known; operator settlement permission required |
| Inputs | Candidate row content, source receipt, license evidence, proposed class and label rationale |
| Happy path | Check source and rights; distinguish label evidence from source observation; review triad coherence; record decision and epistemic; segregate gold, weak, held, refused |
| Alternate/failure paths | Unknown rights/evidence -> HELD; keep_weak not promoted automatically; NC gold_is_sign must be false; disputed label -> HELD; TEACH/raw peer rows not auto-gold |
| State transitions | SM-002: CANDIDATE -> REVIEWING -> ELIGIBLE/WEAK/HELD/REJECTED |
| Terminal states | ELIGIBLE, WEAK, HELD, REJECTED |
| Side effects | Proposed append-only private review record only after authority; no corpus write by this patch |
| Invariants | INFERRED gold stays INFERRED; no floor padding; denied sources remain denied |
| Permissions | Existing operator gold-settle gate; specification approval is not settlement |
| Observability/audit | Row content hash, reviewer/approval references, rationale, label version and rights decision; no secret body |
| Acceptance criteria | AC-005 |
| Dependencies | REQ-009, REQ-010; CON-004; LICENSE_POLICY.md |
| Unresolved items | DEC-005 evidence rubric; DEC-007 rights and retention |

## WF-006

| Field | Specification |
|---|---|
| Purpose | Freeze and validate selected dataset |
| Actors | Dataset reviewer; evaluation reviewer |
| Triggers | Explicit proposal to select a dataset for evaluation |
| Preconditions | WF-005 decisions available; no unknown eligibility included |
| Inputs | Selected row list, source groups, split assignments, schema and exclusion manifest |
| Happy path | Validate row semantics; retain holdouts; group related sources; hash selected rows; compute selected counts/class floors/quality; freeze manifest before candidate run |
| Alternate/failure paths | Too small selected subset -> BLOCKED, not borrowed parent counts; duplicate/group overlap -> BLOCKED; unknown near-dup method -> NOT_COMPUTABLE; NC in train fails current HQ quality bar; changed input makes new snapshot |
| State transitions | SM-003: DRAFT -> VALIDATING -> FROZEN or BLOCKED |
| Terminal states | FROZEN or BLOCKED |
| Side effects | Private immutable manifest after scoped approval; no training, no public corpus |
| Invariants | Snapshot-specific counts; test labels never become training features; floor pass does not prove quality |
| Permissions | Existing local data access and scoped dataset operation only |
| Observability/audit | Snapshot hash, row hashes, group rule version, counts by split/class/epistemic, exclusions, leakage checks |
| Acceptance criteria | AC-006 |
| Dependencies | REQ-011, REQ-012; CON-004, CON-005; WF-005 |
| Unresolved items | DEC-002 effective subset; DEC-007 near-duplicate grouping and rights |

## WF-007

| Field | Specification |
|---|---|
| Purpose | Evaluate frozen T0 and candidate |
| Actors | Evaluation reviewer; existing authorized training operator supplies candidate |
| Triggers | Explicit evaluation request |
| Preconditions | Frozen snapshot; pinned engine/config; candidate use separately authorized; approved feature protocol |
| Inputs | Selected split hashes; target labels separate from input features; T0 and candidate revisions |
| Happy path | Freeze feature allowlist; score same heldout rows; retain predictions; compute exact-match and class/slice/refusal results; record failed cases and hashes |
| Alternate/failure paths | Missing candidate or permission -> NOT_COMPUTABLE; exposed gold/classification labels -> INVALID benchmark; row mismatch/leakage -> INVALID; zero slice support -> NOT_COMPUTABLE, not perfect score; no training performed by eval |
| State transitions | SM-004: REQUESTED -> CHECKING -> SCORED; missing proof -> NOT_COMPUTABLE; invalid benchmark -> INVALID |
| Terminal states | SCORED, NOT_COMPUTABLE, INVALID |
| Side effects | Local evaluation artifacts only; no naming or Hub change |
| Invariants | Separate adapter label fidelity from label-hidden predictive accuracy; same rows/features for both engines |
| Permissions | Read-only evaluation permission does not imply training permission |
| Observability/audit | CON-006 predictions hash, protocol/config/model/data refs, numerator/denominator, confusion/support and errors |
| Acceptance criteria | AC-007 |
| Dependencies | REQ-013, REQ-014; CON-005, CON-006; WF-006 |
| Unresolved items | DEC-001 candidate availability/authority; DEC-006 comparison protocol |

## WF-008

| Field | Specification |
|---|---|
| Purpose | Review existing encoder gates without activation |
| Actors | Operator; existing evaluation and dual-use reviewers |
| Triggers | Evidence packet submitted for E-S3 review |
| Preconditions | Independent evidence for all existing E-S3 conditions; no auto-approval |
| Inputs | Dataset manifest, benchmark, dual-use review, scoped operator sentence, allowed name |
| Happy path | Check each condition separately; verify references and target; report satisfied, failed, unknown; produce advisory recommendation for operator |
| Alternate/failure paths | Any missing evidence -> NOT_COMPUTABLE; known failing condition -> BLOCKED; Notion delivery not approval; ambiguous train/name timing -> DEC-001, no activation |
| State transitions | SM-005: CLOSED -> REVIEWING -> REVIEW_READY/BLOCKED/NOT_COMPUTABLE; REVIEW_READY does not mean OPEN |
| Terminal states | REVIEW_READY, BLOCKED, NOT_COMPUTABLE; gates unchanged |
| Side effects | Advisory review receipt only |
| Invariants | Train, name, Hub, router, canon permissions are distinct; name_gate remains false in this patch |
| Permissions | Existing operator alone governs approval; no new policy or authority layer |
| Observability/audit | Condition-by-condition status with evidence hashes, reviewer, exact target and unverified fields |
| Acceptance criteria | AC-008 |
| Dependencies | REQ-015, REQ-016; existing Spec 004 E-S3; WF-006, WF-007 |
| Unresolved items | DEC-001 training lifecycle; DEC-008 external reviews and operator scope |

## WF-009

| Field | Specification |
|---|---|
| Purpose | Prepare and verify authorized handoff |
| Actors | Existing operator; authorized sender; named recipient |
| Triggers | Exact request to prepare or transfer an identified pack |
| Preconditions | Rights and recipient/purpose scope verified; no transfer authorized by these docs |
| Inputs | Selected immutable snapshot/artifacts, approval reference, restrictions, destination |
| Happy path | Build manifest without secrets; hash permitted files; include reproduction and exclusions; verify bytes; transfer only if separately authorized; record recipient acknowledgement separately |
| Alternate/failure paths | Unknown rights/recipient -> BLOCKED; mismatch -> INVALID and no use; interrupted transfer -> INCOMPLETE retry only same approved scope; no acknowledgement -> delivery unverified |
| State transitions | SM-006: DRAFT -> VERIFIED -> DELIVERED -> ACKNOWLEDGED; failures -> BLOCKED/INVALID/INCOMPLETE |
| Terminal states | VERIFIED if preparation only; ACKNOWLEDGED, BLOCKED, INVALID, INCOMPLETE |
| Side effects | Only authorized bundle/transfer, never Hub or train; no implicit email/Notion write |
| Invariants | Recipient receipt is not release proof; preserve original split labels; exclude keep_weak unless explicitly separate weak artifact |
| Permissions | Existing exact transfer approval, distinct from train and Hub |
| Observability/audit | Artifact sha256 manifest, snapshot ref, allowed recipient reference, transfer outcome; no signed URLs or secrets in public receipt |
| Acceptance criteria | AC-009 |
| Dependencies | REQ-017, REQ-018; CON-005, CON-006; WF-008 |
| Unresolved items | DEC-007 transfer/retention; DEC-008 actual approvals |

## WF-010

| Field | Specification |
|---|---|
| Purpose | Correct labels, leaks, or stale evidence |
| Actors | Corpus/evaluation reviewer; operator; affected recipient |
| Triggers | Verified discrepancy, rights change, or label correction proposal |
| Preconditions | Affected immutable records identified; correction scope approved before mutation |
| Inputs | Old decision/snapshot hashes, correction evidence, impacted results and handoff refs |
| Happy path | Record proposed correction; obtain existing approval; append superseding decision; create new snapshot; mark affected evaluations stale; prepare scoped notification; re-run dependent checks |
| Alternate/failure paths | Unconfirmed issue stays HELD; do not overwrite test or historical receipts; unavailable recipients remain unnotified; rights withdrawal blocks further use; rollback selects a known eligible prior snapshot only |
| State transitions | SM-002 eligible -> SUPERSEDED; SM-003 FROZEN -> SUPERSEDED; SM-004 SCORED -> STALE; revised candidates restart review |
| Terminal states | SUPERSEDED/STALE with linked replacement, or HELD |
| Side effects | Only approved local correction records; external notification separately scoped |
| Invariants | No silent history rewrite; a later count does not retroactively certify old evidence |
| Permissions | Existing operator correction and communication authority, not inferred from detected defect |
| Observability/audit | Old/new hashes, reason, reviewer/approval ref, impacted evaluations, notification status |
| Acceptance criteria | AC-010 |
| Dependencies | REQ-019, REQ-020; CON-004, CON-005, CON-006; WF-005, WF-006 |
| Unresolved items | DEC-007 retention of superseded records; DEC-008 recipient authority |

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
