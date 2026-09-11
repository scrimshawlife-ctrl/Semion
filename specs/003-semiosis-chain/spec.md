# Spec 003 — Semiosis chain

**Feature**: Export `semion.frame.v0` as a SemiosisFrame-shaped dict without owning YGGDRASIL
**Date**: 2026-09-11
**Status**: SHADOW specify + export compat in-repo. Rune mint closed.

## Intent

Gudwin: a sign produces an interpretant; an interpretant may become a new sign. That chain is Abraxas runtime (`RUNE.SEMIOSIS.CHAIN`), not this package.

Semion emits one frame. Compat emits a dict Abraxas may consume. Semion does not mint runes.

## Boundary

```
semion.frame.v0  —export→  dict SemiosisFrame.v1-shaped  —Abraxas→  RUNE.SEMIOSIS.CHAIN
```

| Semion | Export |
|---|---|
| representamen | input_signal.raw_value |
| is_sign | sign_status.is_sign |
| promotion_reason | sign_status.promotion_reason |
| interpretant | interpretant.action_type |
| corpus_ref | frame_id |

`source_space` / `target_space` / `focus_of_attention` are omitted. Semion does not invent them.

## Deny

No `import abraxas`. No rune registry writes. `forecast_eligible` stays false on the export.

## Eval

| Gate | Pass |
|---|---|
| E-K0 | smoke frame → SemiosisFrame shape; no source_space |
| E-K1 | forecast refuse export cannot set forecast_eligible |
