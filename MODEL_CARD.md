# Model card — Semion T0

| Field | Value |
|---|---|
| Name | Semion |
| Artifact | `semion-triad-t0` (rules, not weights) |
| Task | Map corpus atoms to Peircean triad + icon/index/symbol |
| Input | AMC-shaped atom (`sign_form`, `object_candidate`, `interpretant_candidate`, `classification`) |
| Output | `semion.frame.v0` |
| Forecast | never |
| Phenomenal | never |
| Training data | none at T0 |
| Eval | `tests/test_semion_e_s0.py` |
| Intended use | Abraxas BELIEF specialist |
| Out of scope | chat, mind claims, tradition family gold, slang form parse, settled Brier |
