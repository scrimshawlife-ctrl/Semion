# Acceptance criteria

All cases below are proposed runtime/data acceptance, not passed by specification lint. Each requires positive, negative, and failure/recovery controls. Test owners follow completion-tasks.md; closure records exact revision, environment, input and output hashes.

## AC-001

Workflow: WF-001

Given each supported alias, explicit null, Unicode input and single/multiple inventory buckets, normalization is deterministic and preserves source identity. Conflicting aliases, non-object roots, oversized input, malformed inventories and invalid JSONL fail with bounded errors and row position; no partial committed batch or evidence upgrade.

Current evidence: Existing E-C0/E-C1 fixtures cover only a subset; add parametrized boundaries.

Target conformance: NOT_COMPUTABLE.

## AC-002

Workflow: WF-002

Given forecast_request, settled_forecast, bare slang_atom, tradition_atom, unknown payload and restricted interpretant, every entry point returns denial/non-sign or a bounded input error. Direct classify cannot bypass it. Benign smoke/flag controls still pass; refused export has no active action and frozen false/null lanes.

Current evidence: Existing forecast tests pass; bare slang positive counterexample reproduced.

Target conformance: NOT_COMPUTABLE.

## AC-003

Workflow: WF-003

Given approved label/NC precedence, smoke/flag/mixed/no-hint/missing-object inputs produce expected class and is_sign. A corpus_ref alone never becomes label evidence or OBSERVED; explicit source epistemic is not upgraded. Repeat calls yield equal JSON; invalid class types do not crash. All frame fields and cross-field implications validate.

Current evidence: Three evidence/precedence gaps reproduced; DEC-003 and DEC-005 must close.

Target conformance: NOT_COMPUTABLE.

## AC-004

Workflow: WF-004

Given valid, refused, NC, inconsistent and unknown-failure frames, exporter rejects invalid frames and suppresses all failed actions. Valid export preserves triad/reference and false/null lanes with no imports, network or rune writes. Pinned external schema validates all positive controls; missing schema is NOT_COMPUTABLE.

Current evidence: Two current bridge tests pass, external schema not inspected; DEC-004 open.

Target conformance: NOT_COMPUTABLE.

## AC-005

Workflow: WF-005

Given reviewed observed/inferred, weak, unknown-rights, disputed and NC-positive rows, only properly approved eligible rows enter gold; inferred remains inferred, weak stays separate, NC-positive is rejected. Every included label links exact content and source/rights evidence.

Current evidence: Current dataset schema accepts NC-positive counterexample; private rows unverified.

Target conformance: NOT_COMPUTABLE.

## AC-006

Workflow: WF-006

Given selected snapshots, enforce 300/50/100 and selected-pool class floors; independently check NC train count, symbol share, group/source/sign-form overlap, duplicates and exclusion manifest. A 242-row pool cannot PASS a 300-row training floor. Changing one byte invalidates its hash; interrupted freeze cannot appear FROZEN.

Current evidence: No private pack validation performed; DEC-002 and DEC-007 open.

Target conformance: NOT_COMPUTABLE.

## AC-007

Workflow: WF-007

Given approved identical label-hidden features and frozen rows, score T0 and authorized candidate with row-level predictions; recompute correct/evaluated, confusion and slice supports. Injected target labels, changed holdouts and missing predictions invalidate the benchmark; zero support or absent weights returns NOT_COMPUTABLE. Ties fail strict beat-T0 condition.

Current evidence: No candidate or independently verified benchmark available; DEC-006 open.

Target conformance: NOT_COMPUTABLE.

## AC-008

Workflow: WF-008

Given evidence packets with every single required condition independently removed or failed, no review may open train/name/Hub gates. A complete synthetic packet can become REVIEW_READY only, never activation. Approval for transfer must not satisfy training or Hub. Existing E-S3 conditions remain unchanged.

Current evidence: Document-only semantics; DEC-001 and DEC-008 open.

Target conformance: NOT_COMPUTABLE.

## AC-009

Workflow: WF-009

Given safe and tampered bundles, verify every relative member and byte hash; reject traversal, missing file, unknown rights or recipient, expired/mismatched scope and secret-bearing public receipts. Prepare-only stops at VERIFIED; transfer and acknowledgement remain separate and never authorize training.

Current evidence: Notion page text read; original pack bytes and transfer not verified.

Target conformance: NOT_COMPUTABLE.

## AC-010

Workflow: WF-010

Given an approved correction, preserve prior row/snapshot bytes, link a new decision and snapshot, mark affected evaluations stale, and list impacted handoffs. An unapproved correction changes nothing. Notification remains pending until separately authorized and observed.

Current evidence: No real corpus corrections or external notifications performed.

Target conformance: NOT_COMPUTABLE.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)

