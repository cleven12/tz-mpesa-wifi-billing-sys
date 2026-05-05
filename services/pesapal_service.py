"""PesaPal v3 API integration service."""

import os
import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

SANDBOX_BASE_URL = "https://cybqa.pesapal.com/pesapalv3"
LIVE_BASE_URL = "https://pay.pesapal.com/v3"



AUTH_ENDPOINT = "/api/Auth/RequestToken"
IPN_REGISTER_ENDPOINT = "/api/URLSetup/RegisterIPN"
IPN_LIST_ENDPOINT = "/api/URLSetup/GetIpnList"
ORDER_ENDPOINT = "/api/Transactions/SubmitOrderRequest"
STATUS_ENDPOINT = "/api/Transactions/GetTransactionStatus"


class PesapalService:
    """Wraps the PesaPal v3 REST API (authentication, orders, IPN, status)."""

    def __init__(self) -> None:
        self.consumer_key: str = os.getenv("PESAPAL_CONSUMER_KEY", "")
        self.consumer_secret: str = os.getenv("PESAPAL_CONSUMER_SECRET", "")
        self.environment: str = os.getenv("PESAPAL_ENVIRONMENT", "sandbox")
        self.callback_url: str = os.getenv("PESAPAL_CALLBACK_URL", "")
        self.ipn_url: str = os.getenv("PESAPAL_IPN_URL", "")
        self.base_url: str = SANDBOX_BASE_URL if self.environment == "sandbox" else LIVE_BASE_URL
        self._token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None

    IPN_TYPE_GET = "GET"
    IPN_TYPE_POST = "POST"

    PAYMENT_STATUS_COMPLETED = "Completed"
    PAYMENT_STATUS_PENDING = "Pending"
    PAYMENT_STATUS_FAILED = "Failed"
    PAYMENT_STATUS_INVALID = "Invalid"

    def authenticate(self) -> bool:
        """Fetch a bearer token from PesaPal and cache it.

        Endpoint: POST /api/Auth/RequestToken
        Returns:
            bool: True when token was obtained successfully.
        """
        raise NotImplementedError("TODO")

    def _get_headers(self) -> dict:
        """Return JSON + Authorization headers, refreshing token if expired.

        Returns:
            dict: Headers with Accept, Content-Type, Authorization.
        """
        raise NotImplementedError("TODO")

    def register_ipn(self, ipn_url: str, notification_type: str = "GET") -> Optional[str]:
        """Register an IPN URL with PesaPal and return the ipn_id.

        Endpoint: POST /api/URLSetup/RegisterIPN
        Args:
            ipn_url: Publicly reachable URL PesaPal will call on payment events.
            notification_type: "GET" or "POST".

        Returns:
            str: ipn_id assigned by PesaPal, or None on failure.
        """
        raise NotImplementedError("TODO")

    def get_registered_ipns(self) -> list:
        """Fetch all IPN registrations for this merchant.

        Endpoint: GET /api/URLSetup/GetIpnList
        Returns:
            list of dicts with url and ipn_id keys.
        """
        raise NotImplementedError("TODO")

    def submit_order(
        self,
        merchant_reference: str,
        amount: float,
        currency: str,
        description: str,
        customer_email: str,
        customer_phone: str,
        customer_first_name: str,
        customer_last_name: str,
        country_code: str = "TZ",
    ) -> dict:
        """Submit an order to PesaPal and get a hosted payment redirect URL.

        Endpoint: POST /api/Transactions/SubmitOrderRequest
        Args:
            merchant_reference: Your unique order ID.
            amount: Payment amount.
            currency: ISO 4217 code, e.g. "TZS" or "KES".
            description: Short description shown to customer.
            customer_email: Customer e-mail address.
            customer_phone: E.164 phone number, e.g. +255712345678.
            customer_first_name: Customer first name.
            customer_last_name: Customer last name.
            country_code: ISO 3166-1 alpha-2 country code.

        Returns:
            dict with keys: success (bool), order_tracking_id (str),
                            redirect_url (str), error (str, on failure).
        """
        raise NotImplementedError("TODO")

    def get_transaction_status(self, order_tracking_id: str) -> dict:
        """Query the current status of a submitted order.

        Endpoint: GET /api/Transactions/GetTransactionStatus
        Args:
            order_tracking_id: The tracking ID returned by submit_order.

        Returns:
            dict with keys: payment_status_description, amount,
                            payment_method, confirmation_code.
        """
        raise NotImplementedError("TODO")

    def _is_token_valid(self) -> bool:
        """Return True when cached token exists and has not expired."""
        raise NotImplementedError("TODO")

    def _build_order_payload(self, merchant_reference: str, amount: float,
                              currency: str, description: str, customer_email: str,
                              customer_phone: str, first_name: str, last_name: str,
                              country_code: str, ipn_id: str) -> dict:
        """Assemble the dict body for SubmitOrderRequest."""
        raise NotImplementedError("TODO")

    def _parse_status_response(self, data: dict) -> dict:
        """Normalise a GetTransactionStatus response dict.

        Returns keys: status, amount, confirmation_code, payment_method.
        """
        raise NotImplementedError("TODO")

    def handle_ipn_callback(self, order_tracking_id: str, order_merchant_reference: str) -> dict:
        """Process an incoming IPN notification from PesaPal.

        Called by the webhook route when PesaPal hits /webhook/pesapal.
        Looks up transaction status and returns a normalised result.

        Args:
            order_tracking_id: Passed by PesaPal as query param OrderTrackingId.
            order_merchant_reference: Passed by PesaPal as OrderMerchantReference.

        Returns:
            dict with keys: success (bool), amount, status, confirmation_code.
        """
        raise NotImplementedError("TODO")
