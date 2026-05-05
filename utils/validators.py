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

import re

PHONE_TZ_REGEX = re.compile(r"^\+255[67]\d{8}$")
PHONE_KE_REGEX = re.compile(r"^\+2547\d{8}$")
MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")

AMOUNT_MIN = 100
AMOUNT_MAX = 500_000


class ValidationError(ValueError):
    """Raised by validator functions when input fails a rule."""

    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")
