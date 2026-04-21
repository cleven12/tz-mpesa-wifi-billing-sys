"""M-Pesa / Daraja API configuration constants."""

import os
from dataclasses import dataclass


@dataclass
class MpesaConfig:
    consumer_key: str = ""
    consumer_secret: str = ""
    shortcode: str = ""
    passkey: str = ""
    environment: str = "sandbox"  # "sandbox" | "production"
    callback_url: str = ""
    auth_url: str = ""
    stk_push_url: str = ""
    stk_query_url: str = ""


def get_mpesa_config() -> MpesaConfig:
    """Build an MpesaConfig from environment variables."""
    raise NotImplementedError("TODO")
