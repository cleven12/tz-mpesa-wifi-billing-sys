"""Static test fixtures and factory functions."""

VALID_PHONE = "254712345678"
VALID_PASSWORD = "TestPass123!"
VALID_MAC = "00:1A:2B:3C:4D:5E"

SAMPLE_MPESA_CALLBACK_SUCCESS = {
    "Body": {
        "stkCallback": {
            "MerchantRequestID": "test-merchant-id",
            "CheckoutRequestID": "ws_CO_test_001",
            "ResultCode": 0,
            "ResultDesc": "The service request is processed successfully.",
            "CallbackMetadata": {
                "Item": [
                    {"Name": "Amount", "Value": 100},
                    {"Name": "MpesaReceiptNumber", "Value": "LHG31H500111"},
                    {"Name": "PhoneNumber", "Value": 254712345678},
                ]
            },
        }
    }
}

SAMPLE_MPESA_CALLBACK_FAILURE = {
    "Body": {
        "stkCallback": {
            "MerchantRequestID": "test-merchant-id",
            "CheckoutRequestID": "ws_CO_test_002",
            "ResultCode": 1032,
            "ResultDesc": "Request cancelled by user.",
        }
    }
}


def make_user_payload(phone: str = VALID_PHONE, name: str = "Test User") -> dict:
    """Return a minimal user registration payload."""
    raise NotImplementedError("TODO")


def make_payment_payload(package_id: int = 1) -> dict:
    """Return a minimal payment initiation payload."""
    raise NotImplementedError("TODO")

VALID_PESAPAL_IPN_PARAMS = {
    "OrderTrackingId": "test-tracking-id-001",
    "OrderMerchantReference": "WIFI-20260505-TEST01",
    "OrderNotificationType": "IPNCHANGE",
}

SAMPLE_PACKAGES = [
    {"id": 1, "name": "Basic (1 Hour)",   "price": 500,  "duration_seconds": 3600},
    {"id": 2, "name": "Standard (1 Day)", "price": 1000, "duration_seconds": 86400},
    {"id": 3, "name": "Premium (7 Days)", "price": 4000, "duration_seconds": 604800},
]


def make_device_payload(mac="AA:BB:CC:DD:EE:FF", name="Test Device"):
    """Return a valid device whitelist request payload dict."""
    return {"mac_address": mac, "device_name": name}
