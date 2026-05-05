"""High-level payment orchestration (PesaPal order -> DB record -> router grant)."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


WIFI_PACKAGES = {
    1: {"name": "Basic (1 Hour)",   "duration_seconds": 3600,  "price": 500},
    2: {"name": "Standard (1 Day)", "duration_seconds": 86400, "price": 1000},
    3: {"name": "Premium (7 Days)", "duration_seconds": 604800,"price": 4000},
}


class PaymentService:
    """Coordinates PesapalService, DeviceService, and Payment model."""

    def __init__(self) -> None:
        pass  # TODO: instantiate PesapalService, DeviceService

    def create_pending_payment(
        self, user_id: int, phone: str, amount: float, package_id: int
    ) -> dict:
        """Create a Payment row in pending state and submit a PesaPal order.

        Args:
            user_id: FK to users.id
            phone: Full E.164 phone number
            amount: Payment amount
            package_id: Selected WiFi package ID

        Returns:
            dict with order_tracking_id and redirect_url (send redirect_url to client).
        """
        raise NotImplementedError("TODO")

    def process_ipn(self, order_tracking_id: str, merchant_reference: str) -> bool:
        """Handle PesaPal IPN: verify status, update Payment, create Transaction, grant access.

        Args:
            order_tracking_id: PesaPal OrderTrackingId from IPN params.
            merchant_reference: PesaPal OrderMerchantReference from IPN params.

        Returns:
            bool: True when payment was successful and access was granted.
        """
        raise NotImplementedError("TODO")

    def get_payment_status(self, order_tracking_id: str) -> dict:
        """Return current status for a payment identified by order_tracking_id.

        Args:
            order_tracking_id: PesaPal OrderTrackingId.

        Returns:
            dict with keys: status, confirmation_code (optional), error (optional).
        """
        raise NotImplementedError("TODO")

    def get_package_by_id(self, package_id: int) -> dict:
        """Return package dict from WIFI_PACKAGES or raise ValueError for unknown ID."""
        raise NotImplementedError("TODO")

    def get_user_payment_history(self, user_id: int, page: int = 1, per_page: int = 20) -> dict:
        """Return paginated payment history for a user."""
        raise NotImplementedError("TODO")

    def send_confirmation_sms(self, phone: str, package_name: str,
                               confirmation_code: str) -> None:
        """Send payment confirmation SMS via SMSService."""
        raise NotImplementedError("TODO")

    def expire_timed_out_payments(self) -> int:
        """Mark all pending payments older than PAYMENT_TIMEOUT_MINUTES as 'timeout'.

        Returns:
            int: Number of payments updated.
        """
        raise NotImplementedError("TODO")
