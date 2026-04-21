"""Seed the database with default packages and an admin user for development."""

import logging

logger = logging.getLogger(__name__)


def seed_packages() -> None:
    """Insert the three default WiFi packages (Basic, Standard, Premium)."""
    raise NotImplementedError("TODO")


def seed_admin_user() -> None:
    """Create the default admin user from ADMIN_* env vars."""
    raise NotImplementedError("TODO")


def seed_all() -> None:
    """Run all seed functions in dependency order."""
    seed_packages()
    seed_admin_user()


if __name__ == "__main__":
    seed_all()
