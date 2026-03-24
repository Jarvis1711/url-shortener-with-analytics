STATUSES = ["new", "active", "done"]
FIELD_SCHEMA = [
  {
    "key": "owner",
    "label": "Owner",
    "type": "text",
    "required": true
  },
  {
    "key": "impact_score",
    "label": "Impact Score",
    "type": "number",
    "required": true
  },
  {
    "key": "notes",
    "label": "Notes",
    "type": "textarea",
    "required": true
  }
]


def validate_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")

    cleaned = {}
    for field in FIELD_SCHEMA:
        key = field["key"]
        value = payload.get(key)
        if isinstance(value, str):
            value = value.strip()
        if field["required"] and (value is None or value == ""):
            raise ValueError(f"{field['label']} is required")
        if field["type"] == "number" and value not in (None, ""):
            try:
                value = float(value)
            except ValueError as exc:
                raise ValueError(f"{field['label']} must be numeric") from exc
        cleaned[key] = value
    return cleaned
