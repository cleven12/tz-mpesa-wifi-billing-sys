"""PesaPal API configuration."""

import os
from dataclasses import dataclass


SANDBOX_URL = "https://cybqa.pesapal.com/pesapalv3"
LIVE_URL = "https://pay.pesapal.com/v3"


@dataclass
class PesapalConfig:
    consumer_key: str = ""
    consumer_secret: str = ""
    environment: str = "sandbox"   # "sandbox" | "production"
    callback_url: str = ""         # redirect after hosted payment page
    ipn_url: str = ""              # webhook URL PesaPal will POST/GET
    base_url: str = ""             # resolved from environment


    @property
    def is_sandbox(self) -> bool:
        return self.environment == "sandbox"

    def validate(self) -> None:
        """Raise ValueError if consumer_key or consumer_secret is empty."""
        raise NotImplementedError("TODO")


def get_pesapal_config() -> PesapalConfig:
    """Build a PesapalConfig from environment variables."""
    raise NotImplementedError("TODO")
