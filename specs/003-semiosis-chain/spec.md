# Spec 003 — Semiosis chain (specify only)

**Feature**: How frames enter RUNE.SEMIOSIS without Semion owning YGGDRASIL
**Date**: 2026-09-11
**Status**: SHADOW specify. Implement closed.

## Intent

Gudwin: a sign produces an interpretant; an interpretant may become a new sign. That chain is Abraxas runtime (`RUNE.SEMIOSIS.CHAIN`), not this package.

Semion emits one frame. The router may hand that frame to the rune family. Semion does not mint runes.

## Boundary

```
semion.frame.v0  —export→  Abraxas RUNE.SEMIOSIS.CHAIN  →  SemiosisFrame.v1
```

Field bridge (candidate, not implemented):

| Semion | SemiosisFrame.v1 |
|---|---|
| representamen | input_signal.raw_value |
| is_sign | sign_status.is_sign |
| promotion_reason | sign_status.promotion_reason |
| interpretant | interpretant.action_type |
| corpus_ref | frame_id provenance |

`source_space` / `target_space` / `focus_of_attention` stay Abraxas-side. Semion does not invent them at T0.

## Deny

Semion MUST NOT import `abraxas` to call the chain.
A learned residual MUST NOT open private runtime paths (stack constitution III).

## Eval when implement opens

E-K0: fixture frame round-trips to a SemiosisFrame-shaped dict in a *compat* module, no hard import.
E-K1: chain failure cannot set forecast_eligible.
