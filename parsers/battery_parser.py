def parse_battery(payload: dict) -> dict:
    try:
        battery = payload["uplink_message"]["decoded_payload"]["header"]["batteryPerc"]
        return {"battery": battery}
    except Exception as e:
        print(f"[battery_parser] Fehler: {e}")
    return {}
