# State machines

These are proposed engineering states, not authority grants. Terminal means terminal for an attempt; a new attempt requires new input/revision and receipt. No timer or automatic retry grants missing permission.

| ID | Scope | Allowed transitions and guards |
|---|---|---|
| SM-001 | Packet attempt | RECEIVED -> VALIDATING. Valid supported atom -> NORMALIZED. Invalid types/limits -> INVALID. Denied route/content -> REFUSED. NORMALIZED -> CLASSIFIED only with computable relation; otherwise ABSTAINED. CLASSIFIED/ABSTAINED/REFUSED -> EXPORT_VALIDATING on explicit export request; valid inert mapping -> EXPORTED, invalid mapping -> INVALID |
| SM-002 | Label review | CANDIDATE -> REVIEWING with source evidence. Approved coherent label/rights -> ELIGIBLE. Explicit weak decision -> WEAK. Unknown evidence -> HELD. Known disallowed source/rights -> REJECTED. Approved correction moves prior ELIGIBLE to SUPERSEDED and creates a new CANDIDATE |
| SM-003 | Snapshot | DRAFT -> VALIDATING. All selected-row eligibility, quality, grouping and approved floor checks satisfied -> FROZEN. Failure or unknown required check -> BLOCKED, with failed versus unknown checks distinguished. Approved revision creates new DRAFT and marks old FROZEN SUPERSEDED |
| SM-004 | Evaluation | REQUESTED -> CHECKING. Complete authorized pinned comparison -> SCORED. Missing required evidence -> NOT_COMPUTABLE. Leakage, row mismatch or invalid protocol -> INVALID. Superseding data/protocol -> STALE; never replace old score in place |
| SM-005 | Gate review | CLOSED -> REVIEWING on explicit evidence review. Every existing condition evidenced -> REVIEW_READY. Known failure -> BLOCKED. Missing evidence -> NOT_COMPUTABLE. No transition to OPEN exists here; activation remains outside this advisory specification |
| SM-006 | Handoff | DRAFT -> VERIFIED after scope/rights/hash check. Separate transfer permission and successful transfer -> DELIVERED; recipient confirmation -> ACKNOWLEDGED. Unknown permission -> BLOCKED; hash mismatch -> INVALID; interrupted transfer -> INCOMPLETE. Retry same bytes/destination only under still-valid scope; changed bytes restart DRAFT |

## Cross-machine rules

REFUSED and ABSTAINED are different outcomes but both export no active interpretant. HELD is not rejected forever; evidence can start a new review. ELIGIBLE does not imply OBSERVED, FROZEN does not mean trained, SCORED does not mean approved, REVIEW_READY does not open name_gate, and ACKNOWLEDGED does not imply permission to use.

A correction propagates SUPERSEDED -> STALE across dependent snapshots/results and marks handoff impact, without remotely deleting or mutating anything. Duplicate attempts return the prior receipt only when workflow, input hash, config hash, and scope match; otherwise allocate a distinct attempt.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
