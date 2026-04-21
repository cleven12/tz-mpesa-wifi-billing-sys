"""M-Pesa Daraja API integration service."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class MPesaService:
    """Wraps the Safaricom Daraja STK Push API."""

    def __init__(self) -> None:
        self.consumer_key: str = os.getenv("MPESA_CONSUMER_KEY", "")
        self.consumer_secret: str = os.getenv("MPESA_CONSUMER_SECRET", "")
        self.shortcode: str = os.getenv("MPESA_SHORTCODE", "")
        self.passkey: str = os.getenv("MPESA_PASSKEY", "")
        self.environment: str = os.getenv("MPESA_ENVIRONMENT", "sandbox")
        self.callback_url: str = os.getenv("MPESA_CALLBACK_URL", "")
        self.auth_url: str = ""
        self.stk_push_url: str = ""
        self.stk_query_url: str = ""

    def _resolve_urls(self) -> None:
        """Set API URLs based on self.environment ("sandbox" or "production")."""
        raise NotImplementedError("TODO")

    def get_access_token(self) -> str:
        """Fetch and return a short-lived OAuth2 access token from Daraja.

        Returns:
            str: Bearer access token.

        Raises:
            RuntimeError: When the API call fails.
        """
        raise NotImplementedError("TODO")

    def _build_password(self, timestamp: str) -> str:
        """Return the base64-encoded STK Push password.

        Args:
            timestamp: Current timestamp string (format YYYYMMDDHHmmss).
        """
        raise NotImplementedError("TODO")

    def initiate_stk_push(
        self,
        phone: str,
        amount: int,
        account_reference: str = "WiFiBilling",
        transaction_desc: str = "WiFi Billing Payment",
    ) -> dict:
        """Send an STK Push prompt to the user's phone.

        Args:
            phone: Full phone number including country code (e.g. 254712345678).
            amount: Amount in TZS/KES (integer).
            account_reference: Displayed on the M-Pesa prompt.
            transaction_desc: Short description of the transaction.

        Returns:
            dict with CheckoutRequestID, MerchantRequestID, ResponseCode.
        """
        raise NotImplementedError("TODO")

    def query_stk_status(self, checkout_request_id: str) -> dict:
        """Query whether a pending STK Push was completed, failed, or still pending.

        Args:
            checkout_request_id: The CheckoutRequestID from initiate_stk_push.

        Returns:
            dict with ResultCode and ResultDesc.
        """
        raise NotImplementedError("TODO")

    def handle_callback(self, callback_data: dict) -> dict:
        """Parse and validate an M-Pesa STK callback payload.

        Args:
            callback_data: Raw JSON payload from M-Pesa POST to callback URL.

        Returns:
            dict with keys: success (bool), amount, phone, receipt, checkout_id.
        """
        raise NotImplementedError("TODO")
