"""E-K0 / E-K1 export compat."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from semion.classify import classify  # noqa: E402
from semion.compat import frame_to_semiosis  # noqa: E402


def test_e_k0_smoke_round_trip() -> None:
    frame = classify(
        {
            "sign_form": "smoke column",
            "object_candidate": "fire",
            "interpretant_candidate": "STATE_UPDATE:alert",
            "classification": "index",
            "corpus_ref": "RUN-AMC-LEARN-0002.SUBCYCLE-0001",
        }
    )
    out = frame_to_semiosis(frame)
    assert out["schema_version"] == "SemiosisFrame.v1"
    assert out["input_signal"]["raw_value"] == "smoke column"
    assert out["sign_status"]["is_sign"] is True
    assert out["interpretant"]["action_type"] == "STATE_UPDATE:alert"
    assert out["frame_id"] == "RUN-AMC-LEARN-0002.SUBCYCLE-0001"
    assert "source_space" not in out
    assert "target_space" not in out
    assert "focus_of_attention" not in out
    assert "abraxas" not in sys.modules


def test_e_k1_forecast_refuse_cannot_enable_forecast() -> None:
    frame = classify({"payload_class": "forecast_request", "sign_form": "odds"})
    out = frame_to_semiosis(frame)
    assert out["forecast_eligible"] is False
    assert out["phenomenal"] is False
    assert out["brier"] is None
    assert out["sign_status"]["is_sign"] is False
    assert out["interpretant"]["action_type"] == "NOT_COMPUTABLE"
