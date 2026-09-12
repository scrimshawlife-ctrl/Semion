# Aaron train handoff — Semion M2 rebalance

**Audience:** Aaron Godbout (Spark)  
**Date:** 2026-09-11 PT  
**Repo pin:** `scrimshawlife-ctrl/Semion@f465dfb` (main tip before this docs PR; docs tip advances on merge)

## Pack

- Notion: https://app.notion.com/p/3d83e8ba2f5c81608499deffc060160d (Boof refreshes card for refuse-reshuffle pack)
- Pack id: `semion-train-pack-m2-refuse-reshuffle-20260911`
- SHA256: `dd0555d3ae4aae85976cb784bca11ebc71e1ac5d4b6b4f80dccb8f36cebcaa10`
- Pack path (operator box): `/workspace/semion-gold/train-pack-m2-refuse-reshuffle-20260911/`
- Zip: `/workspace/semion-gold/semion-train-pack-m2-refuse-reshuffle-20260911.zip`
- Receipt: `/workspace/semion-gold/receipts/refuse-reshuffle-20260911.json`
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

**NOT_COMPUTABLE by split (post refuse reshuffle):** train **0** / val **9** / test **34** (was 40/1/2). NC held out of train. Compensating swap: promoted 40 wrap into train, demoted 40 wrap from val/test to keep_weak (keep_weak still 150).

## How to train

1. Download the zip from Notion (refuse-reshuffle pack after Boof refresh).
2. Prefer `gold_observed.jsonl` for T0/T1 gold; full splits in `train.jsonl` / `val.jsonl` / `test.jsonl`.
3. Keep `keep_weak.jsonl` out of gold unless you set an explicit weak-lane flag.
4. Dual-use / `NOT_COMPUTABLE` rows are refuse probes — expect refuse, not action content. **Train has 0 NC** after M2 refuse reshuffle.
5. Encoder gate: `specs/004-encoder-gate/`. `name_gate` stays **false** until your eval is green.
6. HF Hub skipped (Danny). Boof `ALLOW_TRAIN` is false — run train on Spark.

## Doctrine (post-audit)

- Wrap/seed INFERRED rows are **lawful M2 gold** under Spec 004 amend (`specs/004-encoder-gate/dataset.md`).
- Prefer `gold_observed.jsonl` for T0/T1 paths; grow OBSERVED via [`amc-foundations-hunt-plan.md`](amc-foundations-hunt-plan.md).
- Pre-rebalance zip is **quarantined** on the operator box (`/workspace/semion-gold/quarantine/`) — do not train from it.
- Prior rebalance pack id `semion-train-pack-m2-rebalance-20260911` is superseded by the refuse-reshuffle pack above.

## Do not

- Mix `keep_weak` into gold without a weak-lane flag
- Treat Notion/email as a green name-gate
- Publish to Hugging Face without Danny `ALLOW_HUB`
- Train from the quarantined pre-rebalance (404-row) zip
- Train from the pre-refuse-reshuffle pack (NC still in train)
