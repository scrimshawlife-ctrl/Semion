# Dataset — Semion encoder (gated)

Review qualification (2026-09-13 UTC): this dated dataset note is retained as source evidence, not independent validation of the private corpus. The latest 452-row report is consistent with the linked Notion handoff; 242 preferred HQ rows alone cannot meet the 300-row training floor. Effective subset, permission timing and fair T0 comparison are unresolved in [DEC-001/002/006](../decisions.md). No floor is waived and no training is authorized by this patch. See [WF-005 through WF-009](../workflows.md) and [CON-004 through CON-006](../contracts.md).

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

### M2 sealed snapshot (HQ leakfix 2026-09-11 PT)

| Slice | n | Notes |
|---|---:|---|
| gold pool | 452 | train 300 / val 50 / test 102 — floors **PASS** |
| OBSERVED | 14 | amc_learn 12 · foundations 2 — honesty: still thin |
| INFERRED wrap | ~210 | `wrapped_sign_atom` (page-dump wraps demoted in HQ) |
| INFERRED seed | 228 | `seed_fixture` |
| keep_weak | 180 | demoted wrap-symbol / athanor dumps — not gold |
| HQ pack | — | `semion-train-pack-m2-hq-20260911` sha256 `af83977d1251b7f62b07a184f14fc34c52b603a4c54406609fb247f43f6156c8` (post AMC high7); prefer `gold_hq.jsonl` (242) |

**AMC high7 (2026-09-11):** seven high-priority OBSERVED `sign_form` modality labels rewritten to atom forms (slang phrase, smoke, skull, waveform, market volume spike, sigil, meme template). Counts/floors unchanged; medium proposals not applied. Receipt: `/workspace/semion-gold/receipts/amc-rewrite-high7-20260911.md`.

**Honesty:** floors pass; preferred OBSERVED share is still thin (**14** / 452 ≈ 3%). Grow OBSERVED via the hunt plan before raising `name_gate`. Targets 600/150 are **not** hit. Do not pad wrap.

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
- **Preferred:** `NOT_COMPUTABLE` / dual-use refuse live in **val/test** (held out of train). **M2 refuse debt CLEARED** (2026-09-11 PT): NC by split train **0** / val **9** / test **34**. **HQ leakfix** supersedes refuse-reshuffle: gold **452** / keep_weak **180**; KEEP-93 train-only; Athanor dumps holdout-only; exact provenance train∩test empty. Pack: `semion-train-pack-m2-hq-20260911` (sha256 `af83977d1251b7f62b07a184f14fc34c52b603a4c54406609fb247f43f6156c8`, post AMC high7).

## E-S3 bind

N in the gate is the **floor** table above until an operator raises it in this file.

## Hunt plan pointer

See [`docs/amc-foundations-hunt-plan.md`](../../docs/amc-foundations-hunt-plan.md).

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
