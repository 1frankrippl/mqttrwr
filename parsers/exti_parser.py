def parse_exti(payload: dict) -> dict:
    try:
        exti_status = payload["uplink_message"]["decoded_payload"].get("Exti_pin_level")
        return {"exti": exti_status}
    except Exception as e:
        print(f"[exti_parser] Fehler: {e}")
        return {}
