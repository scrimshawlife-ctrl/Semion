# Spec 002 — Corpus adapt

Advisory completion: [methodology index](../../docs/START_HERE.md), [requirements](../requirements.md), [workflows](../workflows.md), [contracts](../contracts.md), [acceptance](../acceptance.md), [traceability](../traceability.json), and [tasks](../completion-tasks.md). Original cycle text below is historical; proposed target behavior and unresolved decisions are separate from current runtime proof. This does not govern or activate.

Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)

**Feature**: Field map from AMC / Foundations / TEACH atoms onto Semion input
**Date**: 2026-09-11
**Status**: SHADOW specify + T0 adapter in-repo
**Does not**: scrape new papers, vendor PDFs, gold-settle labels

## Intent

One adapter so harvest code later does not invent column names.

## Map

| Source field | Semion atom |
|---|---|
| sign_form / raw_value / input_signal.raw_value | `sign_form` |
| sign_content / input_signal.information_content | `sign_content` |
| object_candidate | `object_candidate` |
| interpretant_candidate / interpretant.action_type | `interpretant_candidate` |
| classification / sign_inventory bucket | `classification` |
| run_id / frame_id / source_artifact_id | `corpus_ref` |
| VisualSemioticParse icons[] singleton | classification=`icon` |
| indexes[] singleton | classification=`index` |
| symbols[] singleton | classification=`symbol` |
| mixed inventory hits | classification=`mixed` |

## Reject

`forecast_request`, `settled_forecast`, bare `slang_atom`, bare `tradition_atom`.

## Eval

| Gate | Pass |
|---|---|
| E-C0 | fixtures/seed/atoms.jsonl maps 1:1 |
| E-C1 | missing object → null, no crash |
| E-C2 | Foundations inventory smoke → index |

## Implement this cycle

`src/semion/adapt.py`
