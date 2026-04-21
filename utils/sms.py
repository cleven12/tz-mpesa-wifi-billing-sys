"""SMS notification helpers (Africa's Talking gateway)."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class SMSService:
    """Send SMS messages via Africa's Talking."""

    def __init__(self) -> None:
        self.api_key: str = os.getenv("AFRICASTALKING_API_KEY", "")
        self.username: str = os.getenv("AFRICASTALKING_USERNAME", "")
        self._client = None  # africastalking SDK client, initialised lazily

    def _get_client(self):
        """Initialise and return the Africa's Talking SMS client."""
        raise NotImplementedError("TODO")

    def send(self, phone: str, message: str) -> bool:
        """Send a single SMS.

        Args:
            phone: Recipient phone in E.164 format.
            message: Message body (max 160 chars for single SMS).

        Returns:
            bool: True on success.
        """
        raise NotImplementedError("TODO")

    def send_payment_confirmation(
        self, phone: str, amount: float, receipt: str, duration_human: str
    ) -> bool:
        """Send a pre-composed payment-success SMS.

        Args:
            phone: Recipient.
            amount: Amount paid.
            receipt: M-Pesa receipt number.
            duration_human: Human-readable session duration (e.g. "1 Hour").
        """
        raise NotImplementedError("TODO")

    def send_payment_failure(self, phone: str, reason: str) -> bool:
        """Send a pre-composed payment-failure SMS."""
        raise NotImplementedError("TODO")
