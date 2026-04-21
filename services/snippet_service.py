"""Optional Snippet.sh M-Pesa proxy integration."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class SnippetService:
    """Alternative payment backend via Snippet.sh (testing / MVP)."""

    def __init__(self) -> None:
        self.api_key: str = os.getenv("SNIPPET_API_KEY", "")
        self.api_url: str = "https://api.snippet.sh/v1/mpesa"
        self.callback_url: str = os.getenv("SNIPPET_CALLBACK_URL", "")

    def initiate_payment(self, phone: str, amount: int) -> dict:
        """Send a payment request via Snippet.sh.

        Args:
            phone: Full E.164 phone number.
            amount: Payment amount (integer).

        Returns:
            dict: Snippet.sh API response.
        """
        raise NotImplementedError("TODO")

    def handle_callback(self, callback_data: dict) -> dict:
        """Parse and validate a Snippet.sh callback payload.

        Args:
            callback_data: Raw callback JSON from Snippet.sh.

        Returns:
            dict with keys: success (bool), amount, phone, receipt.
        """
        raise NotImplementedError("TODO")
