"""ZLT X17U router SSH configuration."""

import os
from dataclasses import dataclass


@dataclass
class RouterConfig:
    host: str = ""
    username: str = ""
    password: str = ""
    port: int = 22
    timeout: int = 10


def get_router_config() -> RouterConfig:
    """Build a RouterConfig from environment variables."""
    raise NotImplementedError("TODO")
