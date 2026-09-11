# Data model — Semion v0

## Atom (input)
`sign_form` · `sign_content` · `object_candidate` · `interpretant_candidate` · `classification` · `corpus_ref` · optional `payload_class` · optional `run_id`

## Frame (output)
See `schemas/semion.frame.v0.schema.json`.
Hard-false `forecast_eligible`, `phenomenal`. Hard-null `brier`.

## Receipt (later)
`run_id` · `job_type` (`classify`\|`adapt`\|`eval`) · `atom_count` · `not_computable_count` · `content_hash`
Not implemented this cycle.

## Local SoT
- `~/.semion/corpus/atoms.jsonl`
- `~/.semion/receipts/*.json`
- Git holds schemas, fixtures, specs — not full corpus dumps.
