"""General-purpose helper functions."""

from datetime import datetime
from typing import Optional


def format_phone_tz(phone: str) -> str:
    """Normalise a Tanzanian phone number to E.164 format (255...).

    Args:
        phone: Input phone, may start with 0 or +255.
    """
    raise NotImplementedError("TODO")


def format_phone_ke(phone: str) -> str:
    """Normalise a Kenyan phone number to E.164 format (254...).

    Args:
        phone: Input phone, may start with 0 or +254.
    """
    raise NotImplementedError("TODO")


def seconds_to_human(seconds: int) -> str:
    """Convert a duration in seconds to a human-readable string (e.g. '2 hours 30 minutes').

    Args:
        seconds: Non-negative integer.
    """
    raise NotImplementedError("TODO")


def generate_reference(prefix: str = "WIFI") -> str:
    """Generate a unique alphanumeric transaction reference.

    Args:
        prefix: Prepended to the random component.
    """
    raise NotImplementedError("TODO")


def paginate(query, page: int, per_page: int) -> dict:
    """Execute a SQLAlchemy query with pagination and return a standard envelope.

    Args:
        query: SQLAlchemy Query object.
        page: 1-based page number.
        per_page: Number of items per page.

    Returns:
        dict with keys: items (list), total, page, pages, per_page.
    """
    raise NotImplementedError("TODO")
