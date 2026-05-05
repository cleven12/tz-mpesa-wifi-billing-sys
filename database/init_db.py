"""Database initialisation — creates tables and runs seed data."""

import logging
from app import create_app, db

logger = logging.getLogger(__name__)


def init_db(app=None) -> None:
    """Create all tables in the database.

    Args:
        app: Optional Flask app; a new one is created when None.
    """
    raise NotImplementedError("TODO")


def drop_db(app=None) -> None:
    """Drop all tables. Used in tests and reset scripts.

    Args:
        app: Optional Flask app; a new one is created when None.
    """
    raise NotImplementedError("TODO")


if __name__ == "__main__":
    init_db()

SCHEMA_VERSION = 1


def check_schema_version(app=None) -> int:
    """Return the current schema version stored in the database."""
    raise NotImplementedError("TODO")


def backup_before_drop(backup_path: str) -> None:
    """Create a SQLite backup at *backup_path* before dropping tables (dev only)."""
    raise NotImplementedError("TODO")
