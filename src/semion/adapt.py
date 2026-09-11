"""Map source packets onto Semion atoms. Spec 002.

Does not scrape. Does not gold-settle. Does not import Abraxas.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

REJECT_PAYLOAD = frozenset(
    {
        "forecast_request",
        "settled_forecast",
        "slang_atom",
        "tradition_atom",
    }
)

ATOM_KEYS = (
    "sign_form",
    "sign_content",
    "object_candidate",
    "interpretant_candidate",
    "classification",
    "corpus_ref",
    "payload_class",
    "run_id",
)


def _inventory_class(parse: dict[str, Any]) -> str | None:
    inv = parse.get("sign_inventory") or {}
    hits = []
    if inv.get("icons"):
        hits.append("icon")
    if inv.get("indexes"):
        hits.append("index")
    if inv.get("symbols"):
        hits.append("symbol")
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        return "mixed"
    return None


def adapt(source: dict[str, Any]) -> dict[str, Any]:
    payload = source.get("payload_class")
    if payload in REJECT_PAYLOAD:
        return {
            "payload_class": payload,
            "sign_form": None,
            "sign_content": None,
            "object_candidate": None,
            "interpretant_candidate": None,
            "classification": None,
            "corpus_ref": source.get("corpus_ref"),
            "rejected": True,
            "reject_reason": "SPECIALIST_LANE_VIOLATION",
        }

    signal = source.get("input_signal") if isinstance(source.get("input_signal"), dict) else {}
    interpretant = source.get("interpretant") if isinstance(source.get("interpretant"), dict) else {}
    sign_status = source.get("sign_status") if isinstance(source.get("sign_status"), dict) else {}

    classification = (
        source.get("classification")
        or source.get("sign_class")
        or _inventory_class(source)
    )
    interpretant_candidate = source.get("interpretant_candidate")
    if interpretant_candidate is None:
        interpretant_candidate = interpretant.get("action_type")

    atom = {
        "sign_form": source.get("sign_form")
        or source.get("representamen")
        or source.get("raw_value")
        or signal.get("raw_value"),
        "sign_content": source.get("sign_content") or signal.get("information_content"),
        "object_candidate": source.get("object_candidate") or source.get("object"),
        "interpretant_candidate": interpretant_candidate,
        "classification": classification,
        "corpus_ref": source.get("corpus_ref")
        or source.get("run_id")
        or source.get("frame_id")
        or source.get("source_artifact_id"),
        "payload_class": source.get("payload_class") or "sign_atom",
        "run_id": source.get("run_id"),
        "rejected": False,
        "reject_reason": None,
        "promotion_hint": sign_status.get("promotion_reason"),
    }
    return atom


def adapt_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(adapt(json.loads(line)))
    return rows


def atoms_only(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        if row.get("rejected"):
            continue
        out.append({k: row.get(k) for k in ATOM_KEYS})
    return out
