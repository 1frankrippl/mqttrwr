from .wh_parser import parse_wh
from .battery_parser import parse_battery

def get_parser(name):
    parsers = {
        "wh_parser": parse_wh,
        "battery_parser": parse_battery,
        # weitere Parser hier registrieren
    }
    return parsers.get(name, lambda x: x)  # Fallback: Original zurückgeben
