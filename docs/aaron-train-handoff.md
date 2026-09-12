# Aaron train handoff — Semion M2 HQ pack

**Audience:** Aaron Godbout (Spark)  
**Date:** 2026-09-11 PT  
**Repo pin:** `scrimshawlife-ctrl/Semion@e69e5bf` (main tip before this docs PR; docs tip advances on merge)

## Pack

- Notion: https://app.notion.com/p/3d83e8ba2f5c81608499deffc060160d (Boof refreshes card for HQ pack)
- Pack id: `semion-train-pack-m2-hq-20260911`
- SHA256: `af83977d1251b7f62b07a184f14fc34c52b603a4c54406609fb247f43f6156c8`
- Pack path (operator box): `/workspace/semion-gold/train-pack-m2-hq-20260911/`
- Zip: `/workspace/semion-gold/semion-train-pack-m2-hq-20260911.zip`
- **AMC high7 rewrite (2026-09-11):** 7 high-priority `sign_form` modality→atom rewrites applied (text→slang phrase; event/visual signal→smoke; image/object→skull; image/data visualization→waveform; data/event→market volume spike; image/object→sigil; image/text mixed→meme template). Receipt: `/workspace/semion-gold/receipts/amc-rewrite-high7-20260911.md`. Counts unchanged.
- Gate: `QUALITY.md` + `COMPLETE.md` in pack (also [`docs/quality-bar.md`](quality-bar.md))
- Spec 011: https://app.notion.com/p/3d83e8ba2f5c813c9989c0a2dc28357f

**Supersedes** `semion-train-pack-m2-refuse-reshuffle-20260911` (sha `dd0555d3…`) for Aaron train.

## Counts (Spec 004 floors PASS · HQ leakfix)

| Split | N |
|---|---|
| train | 300 |
| val | 50 |
| test | 102 |
| keep_weak (not gold) | 180 |

Gold pool **452**: OBSERVED **14** · inferred wrap **~210** · inferred seed **228**.  
`gold_hq.jsonl` = **242** (OBSERVED + seed + held NC). Class floors PASS; train symbol share ~0.373.

**NOT_COMPUTABLE by split:** train **0** / val **9** / test **34**. NC held out of train.

## Leak / provenance notes (HQ)

- **KEEP-93** train-only (PASS)
- **Athanor dumps** holdout-only (train athanor = 0 PASS)
- Exact provenance train∩test = **empty** (0)
- See pack `QUALITY.md` machine checks

## How to train

1. Download the zip from Notion (HQ pack after Boof refresh).
2. **Prefer `gold_hq.jsonl`** for train mass (OBSERVED + seed + held NC). Use `gold_observed.jsonl` for T0/T1-only paths. Full floor SoT: `train.jsonl` / `val.jsonl` / `test.jsonl` / `dataset.jsonl`.
3. Keep `keep_weak.jsonl` out of gold unless you set an explicit weak-lane flag.
4. Dual-use / `NOT_COMPUTABLE` rows are refuse probes — expect refuse, not action content. **Train has 0 NC**.
5. Encoder gate: `specs/004-encoder-gate/`. `name_gate` stays **false** until your eval is green.
6. HF Hub skipped (Danny). Boof `ALLOW_TRAIN` is false — run train on Spark.
7. Fail the gate if QUALITY checks regress (NC in train, KEEP-93/athanor leak, floors FAIL).

## Doctrine (post-audit)

- Wrap/seed INFERRED rows are **lawful M2 gold** under Spec 004 amend (`specs/004-encoder-gate/dataset.md`), but HQ prefers seed over page-dump wrap.
- Prefer `gold_hq.jsonl` / `gold_observed.jsonl`; grow OBSERVED via [`amc-foundations-hunt-plan.md`](amc-foundations-hunt-plan.md).
- AMC high7: prefer atom-shaped `sign_form` on those 7 OBSERVED rows (slang phrase / smoke / skull / waveform / market volume spike / sigil / meme template); still prefer `gold_hq.jsonl` for train mass.
- Pre-rebalance zip is **quarantined** on the operator box (`/workspace/semion-gold/quarantine/`) — do not train from it.
- Refuse-reshuffle pack `semion-train-pack-m2-refuse-reshuffle-20260911` is **superseded** by the HQ pack above.

## Do not

- Mix `keep_weak` into gold without a weak-lane flag
- Treat Notion/email as a green name-gate
- Publish to Hugging Face without Danny `ALLOW_HUB`
- Train from the quarantined pre-rebalance (404-row) zip
- Train from the refuse-reshuffle pack (superseded; pre-HQ leakfix)
- Grow page-dump wrap mass or pad to 600
