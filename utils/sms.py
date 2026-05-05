"""SMS notification helpers (Africa's Talking gateway)."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


SMS_SENDER_ID = "WIFI-TZ"

SMS_TEMPLATES = {
    "payment_success": (
        "Malipo ya {amount} TZS yamefanikiwa! Namba ya risiti: {confirmation_code}. "
        "Pakiti: {package_name}. Karibu kwenye mtandao wetu."
    ),
    "payment_failed": (
        "Malipo ya {amount} TZS yameshindwa. Tafadhali jaribu tena. "
        "Wasiliana nasi kama tatizo linaendelea."
    ),
    "session_expiring": (
        "Kipindi chako cha intaneti kitaisha baada ya dakika {minutes}. "
        "Nunua pakiti mpya ili uendelee."
    ),
}


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
