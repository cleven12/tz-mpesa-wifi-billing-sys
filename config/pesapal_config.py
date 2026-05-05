"""PesaPal API configuration."""

import os
from dataclasses import dataclass


@dataclass
class PesapalConfig:
    consumer_key: str = ""
    consumer_secret: str = ""
    environment: str = "sandbox"   # "sandbox" | "production"
    callback_url: str = ""         # redirect after hosted payment page
    ipn_url: str = ""              # webhook URL PesaPal will POST/GET
    base_url: str = ""             # resolved from environment


def get_pesapal_config() -> PesapalConfig:
    """Build a PesapalConfig from environment variables."""
    raise NotImplementedError("TODO")
