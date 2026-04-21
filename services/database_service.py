"""Generic database helper operations (not model-specific)."""

import logging
from app import db

logger = logging.getLogger(__name__)


class DatabaseService:
    """Utility wrappers around SQLAlchemy session management."""

    @staticmethod
    def commit() -> bool:
        """Commit the current session; rollback and return False on error."""
        raise NotImplementedError("TODO")

    @staticmethod
    def rollback() -> None:
        """Roll back the current session."""
        raise NotImplementedError("TODO")

    @staticmethod
    def health_check() -> bool:
        """Return True when the DB connection is alive."""
        raise NotImplementedError("TODO")
