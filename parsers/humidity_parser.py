def parse_humidity(payload: dict) -> dict:
    try:
        hum = payload["uplink_normalized"]["normalized_payload"]["air"]["relativeHumidity"]
        return {"humidity": hum}
    except Exception as e:
        print(f"[humidity_parser] Fehler: {e}")
        return {}
