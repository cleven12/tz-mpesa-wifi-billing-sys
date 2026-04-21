"""Payment routes — /api/payment/..."""

from flask import Blueprint, request, jsonify

payment_bp = Blueprint("payment", __name__, url_prefix="/api/payment")


@payment_bp.route("/initiate", methods=["POST"])
def initiate_payment():
    """Trigger an M-Pesa STK Push.

    Requires Authorization: Bearer <token>
    Body JSON keys: phone, amount, package_id
    Returns {success, checkout_request_id, merchant_request_id}
    """
    raise NotImplementedError("TODO")


@payment_bp.route("/status/<string:checkout_request_id>", methods=["GET"])
def payment_status(checkout_request_id: str):
    """Poll the status of a pending payment.

    Requires Authorization: Bearer <token>
    Returns {status, receipt, amount} or {status, error}
    """
    raise NotImplementedError("TODO")


@payment_bp.route("/history", methods=["GET"])
def payment_history():
    """Return paginated payment history for the authenticated user.

    Requires Authorization: Bearer <token>
    Query params: page, limit
    """
    raise NotImplementedError("TODO")


@payment_bp.route("/packages", methods=["GET"])
def list_packages():
    """Return the available WiFi packages and prices."""
    raise NotImplementedError("TODO")
