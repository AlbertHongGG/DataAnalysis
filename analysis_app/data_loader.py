from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


FIELD_MAP = {
    "cyclo_fn_diff": "[Cyclo/Fn] Diff",
    "cog_fn_diff": "[Cog/Fn] Diff",
    "cog_fn_s": "[Cog/Fn] S",
    "cyclo_fn_s": "[Cyclo/Fn] S",
    "cog_fn_st": "[Cog/Fn] S+T",
    "cyclo_fn_st": "[Cyclo/Fn] S+T",
    "project_name": "專案名稱",
    "func_diff": "[Func] Diff",
}


def _coerce_number(value: Any) -> float | None:
    if value is None:
        return None

    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip().replace(",", "")
    if not text:
        return None

    try:
        return float(text)
    except ValueError:
        return None


def _extract_property(row: dict[str, Any], field_name: str) -> Any:
    properties = row.get("properties", {})
    field = properties.get(field_name, {})
    return field.get("value")


def load_analysis_dataframe(json_path: str | Path) -> pd.DataFrame:
    json_path = Path(json_path)
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])

    records: list[dict[str, Any]] = []
    for row in rows:
        project_name = _extract_property(row, FIELD_MAP["project_name"])
        if not str(project_name or "").strip():
            continue

        record = {
            "row_id": len(records) + 1,
            "project_name": project_name,
        }

        for key, field_name in FIELD_MAP.items():
            if key == "project_name":
                continue
            record[key] = _coerce_number(_extract_property(row, field_name))

        records.append(record)

    frame = pd.DataFrame.from_records(records)
    return frame