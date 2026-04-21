"""High-level payment orchestration (STK Push -> DB record -> router grant)."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class PaymentService:
    """Coordinates MPesaService, DeviceService, and Payment model."""

    def __init__(self) -> None:
        pass  # TODO: instantiate MPesaService, DeviceService

    def create_pending_payment(
        self, user_id: int, phone: str, amount: float, package_id: int
    ) -> dict:
        """Create a Payment row in pending state, send STK Push.

        Args:
            user_id: FK to users.id
            phone: Full E.164 phone number
            amount: Payment amount
            package_id: Selected WiFi package ID

        Returns:
            dict with checkout_request_id and merchant_request_id.
        """
        raise NotImplementedError("TODO")

    def process_callback(self, callback_data: dict) -> bool:
        """Handle M-Pesa callback: update Payment, create Transaction, grant access.

        Args:
            callback_data: Raw M-Pesa callback JSON.

        Returns:
            bool: True when payment was successful and access was granted.
        """
        raise NotImplementedError("TODO")

    def get_payment_status(self, checkout_request_id: str) -> dict:
        """Return current status for a payment identified by checkout_request_id.

        Args:
            checkout_request_id: M-Pesa CheckoutRequestID.

        Returns:
            dict with keys: status, receipt (optional), error (optional).
        """
        raise NotImplementedError("TODO")

    def expire_timed_out_payments(self) -> int:
        """Mark all pending payments older than PAYMENT_TIMEOUT_MINUTES as 'timeout'.

        Returns:
            int: Number of payments updated.
        """
        raise NotImplementedError("TODO")
