"""pytest fixtures shared across all test modules."""

import pytest
from app import create_app
from app import db as _db


@pytest.fixture(scope="session")
def app():
    """Create application with in-memory SQLite for the full test session."""
    _app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SECRET_KEY": "test-secret",
        "JWT_SECRET_KEY": "test-jwt-secret",
        "WTF_CSRF_ENABLED": False,
    })
    with _app.app_context():
        _db.create_all()
        yield _app
        _db.drop_all()


@pytest.fixture
def db(app):
    """Wrap each test in a transaction that is rolled back afterward."""
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()
        yield _db
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture
def sample_user(db):
    """Create and return a persisted User instance for tests."""
    raise NotImplementedError("TODO")


@pytest.fixture
def sample_payment(db, sample_user):
    """Create and return a pending Payment instance for tests."""
    raise NotImplementedError("TODO")


@pytest.fixture
def pesapal_mock(monkeypatch):
    """Monkeypatch PesapalService so no real HTTP calls are made."""
    raise NotImplementedError("TODO")


@pytest.fixture
def auth_headers(client):
    """JWT headers for a regular user. Returns Authorization dict."""
    raise NotImplementedError("TODO: register user, login, return headers")


@pytest.fixture
def admin_headers(client):
    """JWT headers for an admin user."""
    raise NotImplementedError("TODO: create admin, login, return headers")
