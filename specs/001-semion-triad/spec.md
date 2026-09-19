# Spec 001 — Semion triad T0

Advisory completion: [methodology index](../../docs/START_HERE.md), [requirements](../requirements.md), [workflows](../workflows.md), [contracts](../contracts.md), [acceptance](../acceptance.md), [traceability](../traceability.json), and [tasks](../completion-tasks.md). Original cycle text below is historical; proposed target behavior and unresolved decisions are separate from current runtime proof. This does not govern or activate.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)

**Feature**: Map symbolic-corpus atoms to `semion.frame.v0`
**Date**: 2026-09-11
**Status**: SHADOW specify + T0 code in-repo
**Constitution**: I–X this repo

## Intent

Adapt existing corpus atoms (AMC LEARN-0002, Foundations sign inventory) into one triad packet.
Do not invent a new mythology. Do not claim a mind formed an interpretant.
Do not invent an object or interpretant to force `is_sign=true`. Underdetermined atoms stay `NOT_COMPUTABLE`.

## Packet fields

- `representamen` ← sign_form / raw signal
- `object` ← object_candidate (null allowed → object NOT_COMPUTABLE)
- `interpretant` ← typed action/state string, never psyche
- `sign_class` ∈ {icon, index, symbol, mixed, NOT_COMPUTABLE}
- `is_sign` true only with representamen plus (object or corpus label) and a computable class
- `forecast_eligible`: false
- `phenomenal`: false
- `brier`: null

## Accepted payload_class

`sign_atom`, `corpus_atom`

Rejected: `forecast_request`, `settled_forecast`, bare `slang_atom`, bare `tradition_atom`.
Those hit Hyperlex, Athanor, or Brier first. Mixed packets are the router's job.

## Eval

| Gate | Pass |
|---|---|
| E-S0 | smoke → index; flag → symbol |
| E-S1 | phenomenal and forecast_eligible stay false |
| E-S2 | forecast packets → SPECIALIST_LANE_VIOLATION |
| E-S3 | T1 blocked |

## Implement this cycle

`src/semion/classify.py` is the T0 engine. No weights.
