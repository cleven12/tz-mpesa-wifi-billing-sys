"""Logging configuration."""

import logging
import os
from logging.handlers import RotatingFileHandler


def configure_logging(app) -> None:
    """Attach file and console handlers to *app*'s logger.

    Args:
        app: The Flask application instance.
    """
    raise NotImplementedError("TODO")

LOG_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def configure_file_handler(log_path: str, max_bytes: int = 10_485_760,
                            backup_count: int = 5):
    """Return a RotatingFileHandler configured with LOG_FORMAT."""
    raise NotImplementedError("TODO")
