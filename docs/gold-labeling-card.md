# Semion gold labeling card — Trichotomy II only

**Audience:** Aaron (Spark pack) · Semion gold authors  
**Date:** 2026-09-18 PT  
**Lane:** docs / labeling hygiene · **not** a schema change  
**Grounding:** PhiloSign Ep4 (`t4miexCUZWg`) + seed fixtures · Design card `/workspace/out/semion-semiotics-design/DESIGN-CARD.md`

Epistemic: examples are **INFERRED teaching rails** from pedagogy + existing Semion seeds. Prefer AMC/Foundations OBSERVED for gold rows. Do **not** dump YouTube ASR into `gold.jsonl`.

---

## Scope lock (T0)

`gold_sign_class` ∈ `{icon, index, symbol, mixed, NOT_COMPUTABLE}` only.

| HOLD (do not label as T0 class) | Why |
|---|---|
| qualisign / sinsign / legisign | Trichotomy I — Spec 005 research only |
| rheme / dicisign / argument | Trichotomy III — Spec 005 research only |
| Eco code / encyclopedia | Not Semion fields |
| Greimas square / actants | REFERENCE only |
| Barthes myth / connotation | provenance tags only |

---

## Decision checklist (order)

1. **Representamen present?** If no clear `sign_form` → `NOT_COMPUTABLE`, `gold_is_sign=false`.
2. **Object underdetermined?** No honest `object_candidate` and no trusted corpus label → `NOT_COMPUTABLE` (coherent-whole / model-reader refuse). **Do not invent object** to force a class.
3. **Relation to object** (pick one primary):
   - **icon** — resemblance / likeness (depicts, looks like)
   - **index** — real connection / causality / trace / pointing
   - **symbol** — convention / law / arbitrary learned link
4. **Conflict / both strong?** → `mixed` (rare; prefer one primary when clear).
5. **Epistemic:** OBSERVED only with trusted provenance (AMC/Foundations/seed). Teaching examples without that → INFERRED and usually stay out of train until promoted.

---

## Canonical examples (label rails)

| sign_form | object_candidate | gold_sign_class | why |
|---|---|---|---|
| smoke column | fire | index | causal / symptom trace |
| national flag | nation-state | symbol | convention |
| stop sign | traffic stop obligation | symbol | conventional law |
| portrait photograph of X | X (as depicted person) | index | existential / evidential link (document) — not “just likeness” |
| painted likeness / diagram of a triangle | geometric triangle (as likeness) | icon | resemblance |
| star map used as navigation chart | positions / course | index | document / pointing-at-world (not emblem) |
| contact emblem / patch motif | group identity (convention) | symbol | emblem ≠ navigational document |
| garbled fragment, no object | null | NOT_COMPUTABLE | refuse overinterpretation |

**Emblem vs document (Marked literacy):** identity emblem → usually **symbol**; navigational/evidential document → usually **index**. Do not flatten.

---

## Fail-closed / model-reader hygiene

- Unlimited semiosis ≠ invent interpretant chains in the gold row.
- Semion emits **one** frame; chain ownership is Abraxas (Spec 003).
- When in doubt between inventing a clever object and NC → **NC**.
- Parallel: vernacular `sacredClass` stays unknown until packet_ready — Semion stays NC until triad is honest.

---

## Row shape reminder (`semion.dataset.row.v0`)

Required: `sign_form`, `gold_sign_class`, `gold_is_sign`, `split`, `provenance`, `epistemic`, `license`.  
Optional: `object_candidate`, `interpretant_candidate`, `source_lane` ∈ amc_learn | foundations | seed_fixture | wrapped_sign_atom.

Interpretant candidates stay in `{STATE_UPDATE, ATTENTION_SHIFT, OUTPUT, NO_ACTION, NOT_COMPUTABLE}` (+ optional suffix), never phenomenal.

---

## Out of scope this card

- Flipping Spec 004 `name_gate` / train  
- Expanding enum to 10 Peirce signs  
- Adding Eco/Greimas fields to `semion.frame.v0`
