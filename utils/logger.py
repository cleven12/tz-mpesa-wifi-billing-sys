"""Application-wide logger factory."""

import logging
import os


def get_logger(name: str) -> logging.Logger:
    """Return a named logger configured with the project log level.

    Args:
        name: Usually __name__ of the calling module.

    Returns:
        logging.Logger instance.
    """
    raise NotImplementedError("TODO")


def setup_request_logging(app) -> None:
    """Attach before/after request hooks to log HTTP requests to *app*.

    Args:
        app: Flask application instance.
    """
    raise NotImplementedError("TODO")

REQUEST_LOG_FORMAT = (
    "%(asctime)s | %(method)s %(path)s | %(status)s | %(duration).1fms"
)


def get_request_id() -> str:
    """Return or generate a unique ID for the current request (for log correlation)."""
    raise NotImplementedError("TODO")
