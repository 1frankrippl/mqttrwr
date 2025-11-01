from .wh_parser import parse_wh
from .battery_parser import parse_battery
from .temperature_parser import parse_temperature
from .humidity_parser import parse_humidity
from .exti_parser import parse_exti
from .timestamp_parser import parse_timestamp

def get_parser(name):
    parsers = {
        "wh_parser": parse_wh,
        "battery_parser": parse_battery,
        "temperature_parser": parse_temperature,
        "humidity_parser": parse_humidity,
        "exti_parser": parse_exti,
        "timestamp_parser": parse_timestamp,
        # weitere Parser hier registrieren
    }
    return parsers.get(name, lambda x: x)  # Fallback: Original zurückgeben
