"""Webhook routes — receive callbacks from M-Pesa and Snippet.sh."""

from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__, url_prefix="/webhook")


@webhook_bp.route("/mpesa", methods=["POST"])
def mpesa_callback():
    """Receive and process the M-Pesa STK Push callback.

    M-Pesa posts a JSON body with Body.stkCallback structure.
    Must always return HTTP 200 with {ResultCode: 0} to acknowledge.
    """
    raise NotImplementedError("TODO")


@webhook_bp.route("/snippet", methods=["POST"])
def snippet_callback():
    """Receive and process the Snippet.sh payment callback.

    Only active when USE_SNIPPET_PAYMENT=True.
    """
    raise NotImplementedError("TODO")


@webhook_bp.route("/mpesa/timeout", methods=["POST"])
def mpesa_timeout():
    """Handle M-Pesa transaction timeout callbacks."""
    raise NotImplementedError("TODO")
