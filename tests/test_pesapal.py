"""Tests for PesapalService (mocked HTTP)."""

from unittest.mock import patch, MagicMock
import pytest


class TestPesapalAuthentication:
    def test_authenticate_success_sets_token(self, pesapal_mock):
        """authenticate() returns True and caches the token on a 200 response."""
        raise NotImplementedError("TODO")

    def test_authenticate_failure_returns_false(self, pesapal_mock):
        """authenticate() returns False when the API returns a non-200 status."""
        raise NotImplementedError("TODO")

    def test_get_headers_refreshes_expired_token(self, pesapal_mock):
        """_get_headers() calls authenticate() automatically when token is expired."""
        raise NotImplementedError("TODO")


class TestPesapalSubmitOrder:
    def test_submit_order_returns_redirect_url(self, pesapal_mock):
        """submit_order() returns a dict with success=True and a redirect_url."""
        raise NotImplementedError("TODO")

    def test_submit_order_on_api_error_returns_success_false(self, pesapal_mock):
        """submit_order() returns {success: False, error: ...} on API failure."""
        raise NotImplementedError("TODO")


class TestPesapalIPN:
    def test_handle_ipn_callback_completed(self, pesapal_mock):
        """handle_ipn_callback() returns success=True for a completed payment."""
        raise NotImplementedError("TODO")

    def test_handle_ipn_callback_failed(self, pesapal_mock):
        """handle_ipn_callback() returns success=False for a failed payment."""
        raise NotImplementedError("TODO")
