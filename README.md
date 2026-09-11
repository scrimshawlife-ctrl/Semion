# Semion

<p align="center">
  <img src="assets/hero.png" alt="Semion hero — bronze triad of icon, index, symbol" width="100%" />
</p>

**Triad specialist** for the Abraxas model stack. Corpus atoms in. `semion.frame.v0` out.

Named for Greek *sēmeion*: a sign. Semiosis is the chain. This repo is the classifier, not the mind.

[![Validate](https://github.com/scrimshawlife-ctrl/Semion/actions/workflows/validate.yml/badge.svg)](https://github.com/scrimshawlife-ctrl/Semion/actions/workflows/validate.yml)

| | |
|---|---|
| **Owns** | triad · sign class · corpus adapt |
| **Honesty** | `OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE` |
| **Shape** | T0 rules now. Encoder name-gated. Not a chatbot. |
| **Anti** | phenomenal heads · forecast mint · numeric Brier · chat trunk · Hyperlex form route · Athanor family gold |
| **Lane** | SHADOW — classify live · train/Hub gated |

The Validate badge may stay red when Actions billing blocks the workflow even if local `pytest` passes.

## Social preview

Raster card for GitHub Settings → Social preview: [`assets/og-social.jpg`](assets/og-social.jpg) (1280×640). Also [`assets/og-social.png`](assets/og-social.png).
SVG stand-in remains at [`assets/og-social.svg`](assets/og-social.svg).

Custom Settings social preview is **not** writable via API or the GitHub MCP connector. After merge, paste `assets/og-social.jpg` in Settings → General → Social preview (private repos may require a prior upload or public visibility for sharing).

## Quick links

| Doc | Path |
|-----|------|
| Status | [`STATUS.md`](STATUS.md) |
| Aaron train handoff | [`docs/aaron-train-handoff.md`](docs/aaron-train-handoff.md) |
| Milestones | [`specs/MILESTONES.md`](specs/MILESTONES.md) |
| Constitution | [`.specify/memory/constitution.md`](.specify/memory/constitution.md) |
| Spec 000 spine | [`specs/000-semion-spine/spec.md`](specs/000-semion-spine/spec.md) |
| Spec 001 triad | [`specs/001-semion-triad/spec.md`](specs/001-semion-triad/spec.md) |
| Spec 002 corpus adapt | [`specs/002-corpus-adapt/spec.md`](specs/002-corpus-adapt/spec.md) |
| Spec 003 chain | [`specs/003-semiosis-chain/spec.md`](specs/003-semiosis-chain/spec.md) |
| Spec 004 encoder gate | [`specs/004-encoder-gate/spec.md`](specs/004-encoder-gate/spec.md) |
| Dual-use gate | [`specs/000-semion-spine/dual-use-gate.md`](specs/000-semion-spine/dual-use-gate.md) |
| Model card | [`MODEL_CARD.md`](MODEL_CARD.md) |
| Quickstart | [`docs/quickstart.md`](docs/quickstart.md) |
| Architecture | [`ARCHITECTURE.md`](ARCHITECTURE.md) |

## Install and classify

```bash
pip install -e ".[dev]"
python -m semion --version
python -m semion classify '{"sign_form":"smoke column","object_candidate":"fire","classification":"index"}'
pytest -q
```

Local labeled corpus, when it exists, lives at `~/.semion/corpus/atoms.jsonl` — **not in git**.

## Peers

Hyperlex (form / lexical) · Athanor (tradition structure) · **Semion (sign relation)** · abx.brier (settled calibration)

## License

Code: MIT. Corpus atoms carry their own licenses — see `LICENSE_POLICY.md`.
