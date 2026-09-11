"""E-C0 / E-C1 corpus adapt."""

from __future__ import annotations

import json
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from semion.adapt import adapt, adapt_jsonl, atoms_only  # noqa: E402
from semion.classify import classify  # noqa: E402

SEED = ROOT / "fixtures" / "seed" / "atoms.jsonl"
FOUNDATIONS = ROOT / "fixtures" / "seed" / "foundations_smoke.json"


def test_e_c0_seed_maps_one_to_one() -> None:
    raw = [json.loads(line) for line in SEED.read_text().splitlines() if line.strip()]
    adapted = adapt_jsonl(SEED)
    assert len(adapted) == len(raw)
    for src, atom in zip(raw, adapted):
        assert atom["rejected"] is False
        assert atom["sign_form"] == src["sign_form"]
        assert atom["classification"] == src["classification"]
        frame = classify(atom)
        assert frame["schema"] == "semion.frame.v0"
        assert frame["forecast_eligible"] is False


def test_e_c1_missing_object_does_not_crash() -> None:
    atom = adapt({"sign_form": "slang phrase", "sign_content": "culture code"})
    assert atom["object_candidate"] is None
    frame = classify(atom)
    assert frame["object"] is None
    assert frame["phenomenal"] is False


def test_foundations_inventory_index() -> None:
    source = json.loads(FOUNDATIONS.read_text())
    atom = adapt(source)
    assert atom["classification"] == "index"
    assert atom["sign_form"] == "smoke column"
    assert atom["interpretant_candidate"] == "STATE_UPDATE"
    assert classify(atom)["sign_class"] == "index"


def test_forecast_row_rejected() -> None:
    atom = adapt({"payload_class": "settled_forecast", "sign_form": "odds"})
    assert atom["rejected"] is True
    assert atom["reject_reason"] == "SPECIALIST_LANE_VIOLATION"
    assert atoms_only([atom]) == []
