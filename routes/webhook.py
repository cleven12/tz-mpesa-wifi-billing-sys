"""Webhook routes — receive IPN callbacks from PesaPal."""

from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__, url_prefix="/webhook")


@webhook_bp.route("/pesapal", methods=["GET", "POST"])
def pesapal_ipn():
    """Receive PesaPal IPN notification.

    PesaPal sends GET (or POST) with query params:
        OrderTrackingId, OrderMerchantReference, OrderNotificationType
    Must respond HTTP 200 with {"orderNotificationType": ..., "orderTrackingId": ...,
    "orderMerchantReference": ..., "status": 200} to acknowledge.
    """
    raise NotImplementedError("TODO")


@webhook_bp.route("/pesapal/callback", methods=["GET"])
def pesapal_callback():
    """Landing page after customer completes (or cancels) the PesaPal hosted page.

    PesaPal redirects the browser here with OrderTrackingId as a query param.
    Show the user their payment result.
    """
    raise NotImplementedError("TODO")
