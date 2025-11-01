def parse_timestamp(payload: dict) -> dict:
    try:
        timestamp = payload.get("received_at")
        return {"timestamp": timestamp}
    except Exception as e:
        print(f"[timestamp_parser] Fehler: {e}")
        return {}
