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
