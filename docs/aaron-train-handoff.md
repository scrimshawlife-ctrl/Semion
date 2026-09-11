# Aaron train handoff — Semion M2 rebalance

**Audience:** Aaron Godbout (Spark)  
**Date:** 2026-09-11 PT  
**Repo pin:** `scrimshawlife-ctrl/Semion@ae47d9f` (docs tip may advance with this branch)

## Pack

- Notion: https://app.notion.com/p/3d83e8ba2f5c81608499deffc060160d
- Pack id: `semion-train-pack-m2-rebalance-20260911`
- SHA256: `8bb18b705b1e51cbce63b4fec79029c00b5f2b81e0b11ca9d42533057851b0da`
- Spec 011: https://app.notion.com/p/3d83e8ba2f5c813c9989c0a2dc28357f

## Counts (Spec 004 floors PASS)

| Split | N |
|---|---|
| train | 330 |
| val | 50 |
| test | 102 |
| keep_weak (not gold) | 150 |

Gold pool 482: OBSERVED 14 · inferred wrap 240 · inferred seed 228.  
Class floors PASS (icon/index/symbol ≥15%; mixed/NC ≥8%). Train symbol share ~0.31.

## How to train

1. Download the zip from Notion.
2. Prefer `gold_observed.jsonl` for T0/T1 gold; full splits in `train.jsonl` / `val.jsonl` / `test.jsonl`.
3. Keep `keep_weak.jsonl` out of gold unless you set an explicit weak-lane flag.
4. Dual-use / `NOT_COMPUTABLE` rows are refuse probes — expect refuse, not action content.
5. Encoder gate: `specs/004-encoder-gate/`. `name_gate` stays **false** until your eval is green.
6. HF Hub skipped (Danny). Boof `ALLOW_TRAIN` is false — run train on Spark.

## Doctrine (post-audit)

- Wrap/seed INFERRED rows are **lawful M2 gold** under Spec 004 amend (`specs/004-encoder-gate/dataset.md`).
- Prefer `gold_observed.jsonl` for T0/T1 paths; grow OBSERVED via [`amc-foundations-hunt-plan.md`](amc-foundations-hunt-plan.md).
- Pre-rebalance zip is **quarantined** on the operator box (`/workspace/semion-gold/quarantine/`) — do not train from it.

## Do not

- Mix `keep_weak` into gold without a weak-lane flag
- Treat Notion/email as a green name-gate
- Publish to Hugging Face without Danny `ALLOW_HUB`
- Train from the quarantined pre-rebalance (404-row) zip
