"""Input validation functions."""


def validate_phone(phone: str) -> bool:
    """Return True when *phone* is a valid Tanzanian/Kenyan E.164 number.

    Args:
        phone: Phone string to validate (e.g. "254712345678").
    """
    raise NotImplementedError("TODO")


def validate_mac_address(mac: str) -> bool:
    """Return True when *mac* matches the pattern XX:XX:XX:XX:XX:XX.

    Args:
        mac: MAC address string.
    """
    raise NotImplementedError("TODO")


def validate_amount(amount, min_amount: float = 10, max_amount: float = 10000) -> bool:
    """Return True when *amount* is a positive number within allowed bounds.

    Args:
        amount: Value to check (str or numeric).
        min_amount: Inclusive lower bound.
        max_amount: Inclusive upper bound.
    """
    raise NotImplementedError("TODO")


def sanitize_string(value: str, max_length: int = 255) -> str:
    """Strip whitespace and truncate *value* to *max_length* characters."""
    raise NotImplementedError("TODO")
