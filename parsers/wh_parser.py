def parse_wh(payload: dict) -> dict:
    try:
        payloads = payload["uplink_message"]["decoded_payload"]["payloads"]
        for p in payloads:
            if p.get("type") == "historic":
                for r in p.get("registers", []):
                    if r.get("unit") == "Wh" and "values" in r:
                        values = r["values"]
                        if values:
                            return {"wh": values[0]}
    except Exception as e:
        print(f"[wh_parser] Fehler: {e}")
    return {}
