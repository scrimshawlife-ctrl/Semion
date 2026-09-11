"""E-S0 / E-S1 / E-S2 for Semion T0."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from semion.classify import classify  # noqa: E402


def test_smoke_is_index() -> None:
    frame = classify(
        {
            "sign_form": "smoke column",
            "object_candidate": "fire",
            "interpretant_candidate": "STATE_UPDATE:alert",
            "classification": "index",
            "corpus_ref": "RUN-AMC-LEARN-0002.SUBCYCLE-0001",
        }
    )
    assert frame["schema"] == "semion.frame.v0"
    assert frame["sign_class"] == "index"
    assert frame["is_sign"] is True
    assert frame["phenomenal"] is False
    assert frame["forecast_eligible"] is False
    assert frame["brier"] is None


def test_flag_is_symbol() -> None:
    frame = classify(
        {
            "sign_form": "national flag",
            "object_candidate": "nation-state",
            "interpretant_candidate": "ATTENTION_SHIFT:allegiance",
            "classification": "symbol",
            "corpus_ref": "RUN-AMC-LEARN-0002.SUBCYCLE-0004",
        }
    )
    assert frame["sign_class"] == "symbol"


def test_forecast_blocked() -> None:
    frame = classify({"payload_class": "forecast_request", "sign_form": "odds"})
    assert frame["failure"] == "SPECIALIST_LANE_VIOLATION"
