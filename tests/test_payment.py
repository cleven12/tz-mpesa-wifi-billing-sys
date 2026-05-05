"""Tests for payment routes and callback handling."""

import pytest
from tests.test_data import SAMPLE_MPESA_CALLBACK_SUCCESS, SAMPLE_MPESA_CALLBACK_FAILURE


class TestInitiatePayment:
    def test_initiate_success(self, client, auth_headers):
        # Arrange: authenticated user, pesapal_mock
        # Act: POST /api/payment/initiate with package_id
        # Assert: 200, redirect_url in response JSON
        raise NotImplementedError("TODO")

    def test_initiate_unauthenticated(self, client):
        raise NotImplementedError("TODO")

    def test_initiate_invalid_package(self, client, auth_headers):
        raise NotImplementedError("TODO")


class TestPaymentStatus:
    def test_status_pending(self, client, auth_headers):
        raise NotImplementedError("TODO")

    def test_status_completed(self, client, auth_headers):
        raise NotImplementedError("TODO")

    def test_status_unknown_checkout_id(self, client, auth_headers):
        raise NotImplementedError("TODO")


class TestMpesaCallback:
    def test_callback_success(self, client):
        raise NotImplementedError("TODO")

    def test_callback_failure(self, client):
        raise NotImplementedError("TODO")

    def test_callback_invalid_payload(self, client):
        raise NotImplementedError("TODO")


class TestPackages:
    def test_list_packages_returns_200(self, client):
        """GET /api/payment/packages returns a list of package objects."""
        raise NotImplementedError("TODO")

    def test_packages_have_required_fields(self, client):
        """Each package has id, name, price, duration_seconds, currency."""
        raise NotImplementedError("TODO")
