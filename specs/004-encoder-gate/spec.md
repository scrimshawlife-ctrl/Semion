# Spec 004 — Encoder gate (closed)

**Feature**: Conditions under which `semion-encoder-*` may exist as weights
**Date**: 2026-09-11
**Status**: SHADOW specify. Train closed. name_gate false.
**Dataset note**: [`dataset.md`](dataset.md)

## Allow name

`semion-encoder-*` only.

## Deny name

`semion-chat-*` · `semion-mind-*` · `semion-conscious-*` · `semion-dpo-*` · `peirce-*` person checkpoints

## Data (frozen note)

- Type: supervised `sign_class` classifier. Not chat.
- Source: AMC LEARN gold, then Foundations inventory. TEACH is not gold.
- Shape: `semion.dataset.row.v0`
- Size floor: 300 train / 100 frozen test. Target 600 / 150.

## E-S3

1. Labeled set meets the floor in `dataset.md`, held-out slice frozen.
2. T0 rules scored on that slice.
3. Encoder beats T0 on `sign_class` exact-match without lifting phenomenal or forecast fields.
4. Dual-use fixtures still refuse.
5. Operator sentence in STATUS.md.

Until all five, weights do not enter this repo or a Hub.
