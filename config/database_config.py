"""Database connection configuration helpers."""

import os


def get_database_url() -> str:
    """Return the database URL from environment."""
    raise NotImplementedError("TODO")


def is_sqlite() -> bool:
    """Return True when the configured database is SQLite."""
    raise NotImplementedError("TODO")

POOL_SIZE = 5
MAX_OVERFLOW = 10
POOL_TIMEOUT = 30


def is_postgres(database_url: str) -> bool:
    """Return True when *database_url* starts with postgresql:// or postgres://."""
    raise NotImplementedError("TODO")


def get_engine_options(database_url: str) -> dict:
    """Return SQLAlchemy engine kwargs appropriate for the given database URL."""
    raise NotImplementedError("TODO")
