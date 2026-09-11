# Spec 002 — Corpus adapt

**Feature**: Field map from AMC / Foundations / TEACH atoms onto Semion input
**Date**: 2026-09-11
**Status**: SHADOW specify
**Does not**: scrape new papers, vendor PDFs, gold-settle labels

## Intent

One adapter table so harvest code later does not invent column names.

## Map

| Source field | Semion atom |
|---|---|
| sign_form / raw_value / input_signal.raw_value | representamen path `sign_form` |
| sign_content | `sign_content` |
| object_candidate | `object_candidate` |
| interpretant_candidate / interpretant.action_type | `interpretant_candidate` |
| classification / sign_inventory bucket | `classification` |
| run_id / frame_id / source_artifact_id | `corpus_ref` |
| VisualSemioticParse icons[] | classification=`icon` when singleton |
| VisualSemioticParse indexes[] | classification=`index` |
| VisualSemioticParse symbols[] | classification=`symbol` |
| mixed inventory hits | classification=`mixed` |

## Lanes accepted

Corpus lanes Semiotics and Symbolic Systems from Seed Source Pack P0.
Orchestra `peircean-signs` labels are structure hints, not gold.

## Lanes rejected

HollerSports settled rows. Oracle forecast candidates. Hyperlex slang_atom without a sign wrapper. Athanor tradition_atom without a sign wrapper.

## Eval

E-C0: fixtures/seed/atoms.jsonl maps 1:1 with no extra keys required.
E-C1: missing object does not crash; frame.object is null.

## Implement

Not this cycle. Table is the spec. T0 classifier already accepts these keys.
