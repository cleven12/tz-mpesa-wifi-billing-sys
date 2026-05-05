"""ZLT X17U router SSH configuration."""

import os
from dataclasses import dataclass


DEFAULT_SSH_PORT = 22
DEFAULT_SSH_TIMEOUT = 10
SSH_RETRY_DELAY = 2
MAX_RETRIES = 3
DEFAULT_BANDWIDTH_LIMIT_MBPS = 5


@dataclass
class RouterConfig:
    host: str = ""
    username: str = ""
    password: str = ""
    port: int = 22
    timeout: int = 10


    def validate(self) -> None:
        """Raise ValueError if host, ssh_user, or ssh_password is empty."""
        raise NotImplementedError("TODO")


def get_router_config() -> RouterConfig:
    """Build a RouterConfig from environment variables."""
    raise NotImplementedError("TODO")
