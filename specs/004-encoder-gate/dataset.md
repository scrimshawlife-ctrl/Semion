# Dataset — Semion encoder (gated)

**Status**: SHADOW note. Not a harvest. name_gate still false.
**Date**: 2026-09-11
**Amend**: M2 rebalance doctrine (2026-09-11 PT) — wrap/seed as lawful INFERRED gold; OBSERVED AMC/Foundations still preferred.

## Verdict

Train a **classifier**, not a speaker.

| Axis | Choice |
|---|---|
| Type | Supervised `sign_class` (+ optional `is_sign`). No chat SFT. No DPO. No interpretant-as-prose |
| Source | **Preferred:** AMC LEARN + Foundations inventories as **OBSERVED**. **Lawful M2 mass:** `wrapped_sign_atom` + Peirce/`seed_fixture` as **INFERRED** gold when floors pass. TEACH abstracts = provenance only |
| Shape | jsonl `semion.dataset.row.v0` |
| Size | Floor **300 / 50 / 100** train/val/test. Target **600 / 80 / 150**. Dual-use refuse floor **20** / target **30**, preferred **held out of train** |

T0 already reads AMC labels. An encoder only earns a name if it beats those rules on a frozen holdout that includes mixed class and missing-object rows.

## Epistemic tiers (M2)

| Tier | Meaning | May count toward Spec 004 gold floors? |
|---|---|---|
| `OBSERVED` | Operator / AMC LEARN / Foundations inventory gold | **Yes** (preferred) |
| `INFERRED` | Lawful wrap (`wrapped_sign_atom`) or Peirce pedagogy (`seed_fixture`) after SEMION label | **Yes** for M2 floors / Aaron pack |
| `keep_weak` | Demoted wrap-symbol (or similar) | **No** — weak lane only |

Do **not** treat Notion delivery, email, or pack existence as a green `name_gate`.

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

| Lane | Role | Gold? | Epistemic |
|---|---|---|---|
| AMC LEARN-0002 packets | **preferred primary** | yes, when `classification` is set | OBSERVED |
| Foundations VisualSemioticParse / SemiosisFrame inventories | **preferred visual + frame** | yes when a single inventory bucket is non-empty | OBSERVED |
| `wrapped_sign_atom` (Hyperlex/Athanor wrap) | **lawful M2 mass** | yes after SEMION label + Spec 004 floors | INFERRED |
| Peirce / pedagogy `seed_fixture` harvest | **lawful M2 mass** | yes for icon/index/mixed/NC probes | INFERRED |
| Demoted wrap-symbol | weak lane | **no** (`keep_weak.jsonl`) | — |
| `fixtures/seed/atoms.jsonl` | eval smoke | fixture, not SoT | — |
| TEACH arXiv abstract chunks | provenance / teaching | no | — |
| Orchestra `peircean-signs` | structure hint | no (until minted as seed_fixture) | — |
| Hyperlex slang harvest (raw) | form only | no unless wrapped as `sign_atom` with object or label | — |
| Athanor tradition atoms (raw) | structure only | no unless wrapped as `sign_atom` | — |
| HollerSports / settled forecast rows | Brier | never | — |

Local SoT: `~/.semion/corpus/dataset.jsonl` (+ `keep_weak.jsonl`). Not in git.

### M2 sealed snapshot (OBSERVED 2026-09-11 PT)

| Slice | n | Notes |
|---|---:|---|
| gold pool | 482 | train 330 / val 50 / test 102 — floors **PASS** |
| OBSERVED | 14 | amc_learn 12 · foundations 2 |
| INFERRED wrap | 240 | `wrapped_sign_atom` |
| INFERRED seed | 228 | `seed_fixture` |
| keep_weak | 150 | demoted wrap-symbol — not gold |

**Honesty:** floors pass; preferred OBSERVED share is still thin (~3%). Grow OBSERVED via the hunt plan before raising `name_gate`. Targets 600/150 are **not** hit.

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
| dual-use refuse (preferred **not train**) | 20 | 30 |

Class floor on the gold pool (train+val+test): icon, index, symbol each ≥ 15%. mixed and NOT_COMPUTABLE each ≥ 8%.

This is probe-scale. It is not a 7B SFT corpus. Do not pad with synthetic mind-talk to hit a larger N.

## Split law

- Freeze `test` hashes before any encoder run.
- No source_run_id in both train and test.
- Dual-use refuse rows never appear as positive `is_sign` gold.
- **Preferred:** `NOT_COMPUTABLE` / dual-use refuse live in **val/test** (held out of train). **M2 refuse debt CLEARED** (2026-09-11 PT): NC by split train **0** / val **9** / test **34**. Compensating keep_weak swap kept gold 482 and floors (promoted 40 wrap → train; demoted 40 wrap from val/test → keep_weak; keep_weak still 150). Pack: `semion-train-pack-m2-refuse-reshuffle-20260911`.

## E-S3 bind

N in the gate is the **floor** table above until an operator raises it in this file.

## Hunt plan pointer

See [`docs/amc-foundations-hunt-plan.md`](../../docs/amc-foundations-hunt-plan.md).
