"""Tests for authentication routes."""

import pytest


class TestRegister:
    def test_register_success(self, client, db):
        # Arrange
        # Act
        # Assert
        raise NotImplementedError("TODO")

    def test_register_duplicate_phone(self, client, db):
        raise NotImplementedError("TODO")

    def test_register_invalid_phone(self, client, db):
        raise NotImplementedError("TODO")

    def test_register_missing_fields(self, client, db):
        raise NotImplementedError("TODO")


class TestLogin:
    def test_login_success(self, client, db):
        raise NotImplementedError("TODO")

    def test_login_wrong_password(self, client, db):
        raise NotImplementedError("TODO")

    def test_login_nonexistent_user(self, client, db):
        raise NotImplementedError("TODO")


class TestProfile:
    def test_get_profile_authenticated(self, client, auth_headers):
        raise NotImplementedError("TODO")

    def test_get_profile_unauthenticated(self, client):
        raise NotImplementedError("TODO")

    def test_update_profile(self, client, auth_headers):
        raise NotImplementedError("TODO")


class TestDuplicateRegistration:
    def test_register_duplicate_phone_returns_409(self, client, sample_user):
        """Registering with an already-taken phone number returns 409 Conflict."""
        # Arrange: sample_user already has a phone registered
        # Act: POST /api/auth/register with the same phone
        # Assert: response.status_code == 409
        raise NotImplementedError("TODO")
