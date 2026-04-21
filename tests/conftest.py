"""Shared pytest fixtures for the entire test suite."""

import pytest
from app import create_app, db as _db


@pytest.fixture(scope="session")
def app():
    """Create a test-mode Flask application (in-memory SQLite)."""
    _app = create_app("config.settings.TestingConfig")
    with _app.app_context():
        _db.create_all()
        yield _app
        _db.drop_all()


@pytest.fixture(scope="function")
def db(app):
    """Yield a clean database session that rolls back after each test."""
    with app.app_context():
        yield _db
        _db.session.rollback()


@pytest.fixture(scope="function")
def client(app):
    """Return a Flask test client."""
    return app.test_client()


@pytest.fixture(scope="function")
def auth_headers(client, db):
    """Register and log in a test user; return Authorization headers dict."""
    raise NotImplementedError("TODO — register + login, return {'Authorization': 'Bearer ...'}")


@pytest.fixture(scope="function")
def admin_headers(client, db):
    """Register and log in an admin user; return Authorization headers dict."""
    raise NotImplementedError("TODO")
