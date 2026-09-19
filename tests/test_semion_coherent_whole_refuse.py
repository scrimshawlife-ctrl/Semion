"""Coherent-whole refuse: underdetermined atoms stay NOT_COMPUTABLE."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from semion.classify import classify  # noqa: E402
from semion.compat import frame_to_semiosis  # noqa: E402

FIXTURES = ROOT / "fixtures" / "dual_use"
REFUSE_FILES = (
    "refuse_underdetermined_object.json",
    "refuse_empty_sign_form.json",
    "refuse_overinterpretation_noise.json",
)


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def test_coherent_whole_refuse_fixtures_stay_nc() -> None:
    for name in REFUSE_FILES:
        atom = _load(name)
        frame = classify(atom)
        assert frame["is_sign"] is False, name
        assert frame["forecast_eligible"] is False, name
        assert frame["phenomenal"] is False, name
        assert frame["sign_class"] == "NOT_COMPUTABLE", name
        assert frame["failure"] == "NOT_COMPUTABLE", name
        assert frame["promotion_reason"] == "NOT_COMPUTABLE", name
        assert frame["object"] is None, name


def test_e_k2_underdetermined_export_stays_nc() -> None:
    frame = classify(_load("refuse_underdetermined_object.json"))
    out = frame_to_semiosis(frame)
    assert out["sign_status"]["is_sign"] is False
    assert out["interpretant"]["action_type"] == "NOT_COMPUTABLE"
    assert out["forecast_eligible"] is False
    assert out["phenomenal"] is False
