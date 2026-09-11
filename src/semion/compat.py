"""Export-only bridge. Spec 003.

Semion does not import Abraxas. Does not mint runes.
Abraxas may consume this dict at RUNE.SEMIOSIS.CHAIN.
"""

from __future__ import annotations

from typing import Any


def frame_to_semiosis(frame: dict[str, Any]) -> dict[str, Any]:
    failed = frame.get("failure") in {"SPECIALIST_LANE_VIOLATION", "NOT_COMPUTABLE"}
    is_sign = bool(frame.get("is_sign")) and not failed
    return {
        "schema_version": "SemiosisFrame.v1",
        "frame_id": frame.get("corpus_ref"),
        "interpreter_id": None,
        "input_signal": {
            "raw_value": frame.get("representamen"),
            "signal_type": None,
            "information_content": None,
        },
        "sign_status": {
            "is_sign": is_sign,
            "promotion_reason": frame.get("promotion_reason") or "NOT_COMPUTABLE",
        },
        "interpretant": {
            "action_type": frame.get("interpretant") if is_sign else "NOT_COMPUTABLE",
            "state_delta": {},
            "external_effect": "",
            "new_knowledge_units": [],
        },
        "object": frame.get("object"),
        "sign_class": frame.get("sign_class"),
        "forecast_eligible": False,
        "phenomenal": False,
        "brier": None,
        "provenance": {
            "source": "semion.compat.frame_to_semiosis",
            "label": frame.get("epistemic") or "NOT_COMPUTABLE",
            "failure": frame.get("failure"),
        },
    }
