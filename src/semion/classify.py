"""T0 rule classifier. Adapts AMC / Foundations corpus atoms to triad frames."""

from __future__ import annotations

from typing import Any

SCHEMA = "semion.frame.v0"
ICON_HINTS = ("image", "likeness", "depict", "icon")
INDEX_HINTS = ("smoke", "trace", "symptom", "index", "causal", "point")
SYMBOL_HINTS = ("flag", "word", "slang", "convention", "symbol", "rune", "name")


def _text(*parts: Any) -> str:
    return " ".join(str(p).lower() for p in parts if p)


def _class_from_atom(atom: dict[str, Any]) -> str:
    labeled = (atom.get("classification") or atom.get("sign_class") or "").lower()
    if labeled in {"icon", "index", "symbol", "mixed"}:
        return labeled
    blob = _text(
        atom.get("sign_form"),
        atom.get("sign_content"),
        atom.get("object_candidate"),
        atom.get("interpretant_candidate"),
    )
    hits = []
    if any(h in blob for h in ICON_HINTS):
        hits.append("icon")
    if any(h in blob for h in INDEX_HINTS):
        hits.append("index")
    if any(h in blob for h in SYMBOL_HINTS):
        hits.append("symbol")
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        return "mixed"
    return "NOT_COMPUTABLE"


def classify(atom: dict[str, Any]) -> dict[str, Any]:
    payload = atom.get("payload_class")
    if payload in {"settled_forecast", "forecast_request"}:
        return {
            "schema": SCHEMA,
            "representamen": None,
            "object": None,
            "interpretant": None,
            "sign_class": "NOT_COMPUTABLE",
            "is_sign": False,
            "promotion_reason": "NOT_COMPUTABLE",
            "forecast_eligible": False,
            "phenomenal": False,
            "brier": None,
            "epistemic": "NOT_COMPUTABLE",
            "failure": "SPECIALIST_LANE_VIOLATION",
            "corpus_ref": atom.get("corpus_ref"),
        }

    representamen = atom.get("sign_form") or atom.get("representamen") or atom.get("raw_value")
    obj = atom.get("object_candidate") or atom.get("object")
    interpretant = atom.get("interpretant_candidate") or atom.get("interpretant")
    sign_class = _class_from_atom(atom)
    has_rep = bool(representamen)
    labeled = bool(atom.get("classification") or atom.get("corpus_ref"))
    is_sign = bool(has_rep and (obj or labeled) and sign_class != "NOT_COMPUTABLE")

    return {
        "schema": SCHEMA,
        "representamen": representamen,
        "object": obj,
        "interpretant": interpretant,
        "sign_class": sign_class,
        "is_sign": is_sign,
        "promotion_reason": "CORPUS_LABEL" if labeled and is_sign else (
            "CAUSES_STATE_CHANGE" if is_sign else "NOT_COMPUTABLE"
        ),
        "forecast_eligible": False,
        "phenomenal": False,
        "brier": None,
        "epistemic": "OBSERVED" if labeled else ("INFERRED" if is_sign else "NOT_COMPUTABLE"),
        "failure": None if is_sign else "NOT_COMPUTABLE",
        "corpus_ref": atom.get("corpus_ref") or atom.get("run_id"),
    }
