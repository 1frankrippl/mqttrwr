def parse_temperature(payload: dict) -> dict:
    try:
        temp = payload["uplink_normalized"]["normalized_payload"]["air"]["temperature"]
        return {"temperature": temp}
    except Exception as e:
        print(f"[temperature_parser] Fehler: {e}")
        return {}
