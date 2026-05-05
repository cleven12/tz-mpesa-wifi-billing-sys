"""Manual migration helpers (supplements Flask-Migrate for raw ALTER statements)."""

import logging
from app import db

logger = logging.getLogger(__name__)


def run_migrations(app) -> None:
    """Apply any pending manual migrations.

    Args:
        app: Active Flask application context owner.
    """
    raise NotImplementedError("TODO")


def add_column_if_missing(table: str, column: str, column_type: str) -> None:
    """Add *column* of *column_type* to *table* when it does not already exist.

    Args:
        table: Table name.
        column: Column name.
        column_type: SQL type string e.g. 'VARCHAR(100)'.
    """
    raise NotImplementedError("TODO")

MIGRATIONS_TABLE = "schema_migrations"
