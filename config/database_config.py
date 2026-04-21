"""Database connection configuration helpers."""

import os


def get_database_url() -> str:
    """Return the database URL from environment."""
    raise NotImplementedError("TODO")


def is_sqlite() -> bool:
    """Return True when the configured database is SQLite."""
    raise NotImplementedError("TODO")
