# Verification plan and measured scope

## Reproducible documentation checks

Run from repository root with Python >=3.10:

```text
python -B specs/verification.py
python -B -m pytest -q -p no:cacheprovider
git diff --check
```

The specification checker uses the standard library only. It checks workflow fields, unique definitions, the 14-stage index, traceability references, local Markdown destinations, fixed-lane documentation, protected runtime/constitution/schema identity against the reviewed base, and unchanged duplicate frame schemas. Negative controls remove a workflow field, duplicate a requirement, break a trace reference, and falsely claim PASS; each must be detected. These checks measure documentation integrity, not runtime acceptance.

Existing pytest requires the declared development dependency. Read scripts before executing. No check needs network, home corpus, training, credentials, or external writes. Local Python 3.12 is the measured environment; 3.10/3.11 and hosted CI results must be reported only if observed separately.

## Baseline and target evidence

The reviewed base has nine existing tests. They exercise smoke/flag, one forecast rejection, simple field mapping and two exports. They do not prove typed input, direct slang/tradition denial, epistemic soundness, complete dual-use refusal, dataset quality, installed wheel behavior or external SemiosisFrame schema compatibility.

All AC-001 through AC-010 target conformance remains NOT_COMPUTABLE. A later implementation must run their positive, negative, boundary and recovery cases and store exact code/config/input/output hashes. Historical test evidence cannot close a newly proposed requirement.

## Release of evidence, not authority

Every run distinguishes OBSERVED test outcomes from INFERRED design implications and NOT_COMPUTABLE unavailable artifacts. Review all changed files and verify only README, STATUS, ARCHITECTURE, docs, specs and sanitized out/audit receipt paths changed. Root constitution, its mirror, src, schemas, contracts, tests, fixtures, dependency metadata and CI are unchanged.

A PR check may show the existing smoke suite, not this new specification checker unless explicitly added in a separate CI change. No auto-merge, workflow dispatch, training or Hub action follows from green checks.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
