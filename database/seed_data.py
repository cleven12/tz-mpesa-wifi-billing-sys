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

SAMPLE_PACKAGES = [
    {"id": 1, "name": "Basic (1 Hour)",   "duration_seconds": 3600,   "price": 500},
    {"id": 2, "name": "Standard (1 Day)", "duration_seconds": 86400,  "price": 1000},
    {"id": 3, "name": "Premium (7 Days)", "duration_seconds": 604800, "price": 4000},
]

SAMPLE_ADMIN = {
    "phone": "+255700000001",
    "name": "Admin",
    "password": "changeme123",
    "status": "active",
}
