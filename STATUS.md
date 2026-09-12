# STATUS

**Lane**: SHADOW
**Date**: 2026-09-11
**Version**: 0.1.0

| Gate | State |
|---|---|
| Spec 000 spine | specified |
| Spec 001 triad T0 | specified + code |
| Spec 002 corpus adapt | specified + `adapt.py` |
| Spec 003 semiosis chain | specified + export `compat.py` |
| Spec 004 encoder gate | specified, name_gate **false**, dataset note landed |
| E-S0 / E-C0 / E-K0 | in repo |
| Hub | closed (HF skipped 2026-09-11) |
| Spec 009 id swap | done — `semion.triad` |
| Hero / OG rasters | on main — `assets/hero.{png,jpg}` · `assets/og-social.{png,jpg}` |
| Settings Social preview | **manual paste** of `og-social.jpg` (no API/MCP write) |
| M2 rebalance pack | floors **PASS** — gold 482 (train 330 / val 50 / test 102); keep_weak 150 |
| M2 refuse reshuffle | **PASS** — NC by split train **0** / val **9** / test **34**; pack sha `dd0555d3ae4aae85976cb784bca11ebc71e1ac5d4b6b4f80dccb8f36cebcaa10` (superseded by HQ) |
| M2 HQ leakfix | **PASS** — gold **452** (train **300** / val **50** / test **102**); keep_weak **180**; pack sha `2480bca9eaed7c211e2db01e52db9f62ece7e8e0c90b894221c1d0b11fa4d6d7`; `gold_hq.jsonl` = 242; KEEP-93 train-only; Athanor dumps holdout-only; exact prov train∩test empty |
| AMC high7 modality rewrite | **APPLIED** — 7 high-only `sign_form` rewrites (slang phrase / smoke / skull / waveform / market volume spike / sigil / meme template); gold still **452** · 300/50/102 · keep_weak **180** · OBSERVED **14** · NC **0/9/34**; pack path same; zip sha `af83977d1251b7f62b07a184f14fc34c52b603a4c54406609fb247f43f6156c8`; receipt `amc-rewrite-high7-20260911.md` |
| Aaron Notion pack | https://app.notion.com/p/3d83e8ba2f5c81608499deffc060160d (Boof refreshes HQ pack card) |
| Boof ALLOW_TRAIN | **false** — Aaron trains on Spark |
| Handoff doc | [`docs/aaron-train-handoff.md`](docs/aaron-train-handoff.md) |
| Quality bar | [`docs/quality-bar.md`](docs/quality-bar.md) → pack `QUALITY.md` |
| README | operator front door expanded (stack parity with Athanor) |
| Spec 004 doctrine | M2 amend: wrap/seed lawful INFERRED gold; OBSERVED AMC/Foundations preferred |
| Pre-rebalance zip | quarantined under `/workspace/semion-gold/quarantine/` (404-row pack) |
| OBSERVED share | **14 / 452** (~3%) — hunt plan: `docs/amc-foundations-hunt-plan.md` |
| Main tip | `e69e5bf` — M2 HQ pack handoff #6; AMC high7 docs PR advances tip |
