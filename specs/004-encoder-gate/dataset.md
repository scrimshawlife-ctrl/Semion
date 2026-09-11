# Dataset — Semion encoder (gated)

**Status**: SHADOW note. Not a harvest. name_gate still false.
**Date**: 2026-09-11

## Verdict

Train a **classifier**, not a speaker.

| Axis | Choice |
|---|---|
| Type | Supervised `sign_class` (+ optional `is_sign`). No chat SFT. No DPO. No interpretant-as-prose |
| Source | AMC LEARN gold first. Foundations inventory second. TEACH abstracts are provenance only |
| Shape | jsonl `semion.dataset.row.v0` |
| Size | Floor **300 / 100** train/holdout. Target **600 / 150**. Dual-use refuse **30** held out of train |

T0 already reads AMC labels. An encoder only earns a name if it beats those rules on a frozen holdout that includes mixed class and missing-object rows.

## Type

Allowed heads:

1. `sign_class` ∈ {icon, index, symbol, mixed, NOT_COMPUTABLE}
2. `is_sign` boolean
3. Optional closed `action_type` ∈ {STATE_UPDATE, ATTENTION_SHIFT, OUTPUT, NO_ACTION, NOT_COMPUTABLE}

Denied heads:

- free-text interpretant / “what this means to a mind”
- phenomenal / access claims
- numeric Brier
- efficacy
- next-token chat

If a later cycle wants a retrieval encoder, that is a different artifact name and a different spec.

## Source

| Lane | Role | Gold? |
|---|---|---|
| AMC LEARN-0002 packets | primary | yes, when `classification` is set |
| Foundations VisualSemioticParse / SemiosisFrame inventories | visual + frame | yes when a single inventory bucket is non-empty |
| `fixtures/seed/atoms.jsonl` | eval smoke | fixture, not SoT |
| TEACH arXiv abstract chunks | provenance / teaching | no |
| Orchestra `peircean-signs` | structure hint | no |
| Hyperlex slang harvest | form only | no unless wrapped as `sign_atom` with object or label |
| Athanor tradition atoms | structure only | no unless wrapped as `sign_atom` |
| HollerSports / settled forecast rows | Brier | never |

Local SoT when harvest opens: `~/.semion/corpus/dataset.jsonl`. Not in git.

## Shape

See `schemas/semion.dataset.row.v0.schema.json`.

Minimum live fields:

- `sign_form` (text ≤ 512)
- `gold_sign_class`
- `gold_is_sign`
- `split` ∈ {train, val, test}
- `provenance` (receipt or run id)
- `epistemic` ∈ {OBSERVED, INFERRED}
- `license`

`object_candidate` may be null. Those rows are the holdout stress, not discard.

## Size

| Slice | Floor | Target |
|---|---|---|
| train | 300 | 600 |
| val | 50 | 80 |
| test / holdout frozen | 100 | 150 |
| dual-use refuse (not train) | 20 | 30 |

Class floor on the gold pool (train+val+test): icon, index, symbol each ≥ 15%. mixed and NOT_COMPUTABLE each ≥ 8%.

This is probe-scale. It is not a 7B SFT corpus. Do not pad with synthetic mind-talk to hit a larger N.

## Split law

- Freeze `test` hashes before any encoder run.
- No source_run_id in both train and test.
- Dual-use refuse rows never appear as positive `is_sign` gold.

## E-S3 bind

N in the gate is the **floor** table above until an operator raises it in this file.
