# Quality bar — Semion M2 encoder gold

**Audience:** operators / Aaron  
**Date:** 2026-09-11 PT

Ranked bar for Spec 004 gold (do not pad wrap to chase size).

1. **Label correctness / triad coherence.** NC ⇒ `gold_is_sign` false.
2. **Epistemic.** OBSERVED > INFERRED. Within INFERRED: `seed_fixture` > atomic wrap > page-dump wrap. `keep_weak` is not gold.
3. **Split hygiene.** NC/refuse out of train. No `sign_form` leakage train vs holdout. No identical provenance / `source_run_id` in train AND test. KEEP-93 train-only; Athanor dumps holdout-only.
4. **Class floors.** icon/index/symbol ≥15%; mixed/NC ≥8%. Train symbol share ≤0.85.
5. **Dedup / near-dup.** Do not grow page-dump wrap.
6. **Provenance completeness** (required fields + `source_lane` + license + epistemic).
7. **Size floors** 300/50/100 are secondary to 1–3. Do not pad wrap to chase 600.

Sealed HQ pack machine checks live in:

`/workspace/semion-gold/train-pack-m2-hq-20260911/QUALITY.md`

Prefer `gold_hq.jsonl` for train mass; see [`aaron-train-handoff.md`](aaron-train-handoff.md).
