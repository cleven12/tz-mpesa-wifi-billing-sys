"""Device / MAC-address routes — /api/devices/..."""

# MAC address format: AA:BB:CC:DD:EE:FF  (colon-separated, uppercase hex)
# Validated by utils.validators.validate_mac_address before any router call.

from flask import Blueprint, request, jsonify

device_bp = Blueprint("device", __name__, url_prefix="/api/devices")


@device_bp.route("/", methods=["GET"])
def list_devices():
    """Return all devices belonging to the authenticated user.

    Requires Authorization: Bearer <token>
    """
    raise NotImplementedError("TODO")


@device_bp.route("/whitelist", methods=["POST"])
def add_to_whitelist():
    """Add a device MAC address to the router whitelist.

    Requires Authorization: Bearer <token>
    Body JSON keys: mac_address, device_name (optional)
    """
    raise NotImplementedError("TODO")


@device_bp.route("/<int:device_id>", methods=["DELETE"])
def remove_device(device_id: int):
    """Remove a device from the router whitelist.

    Requires Authorization: Bearer <token>
    """
    raise NotImplementedError("TODO")


@device_bp.route("/<int:device_id>", methods=["GET"])
def get_device(device_id: int):
    """Return details for a single device.

    Requires Authorization: Bearer <token>
    """
    raise NotImplementedError("TODO")


@device_bp.route("/bulk-whitelist", methods=["POST"])
def bulk_whitelist():
    """Whitelist multiple MAC addresses in one SSH call.

    Body: {devices: [{mac_address: str, device_name?: str}]}
    Returns: {whitelisted: int, errors: []}
    """
    raise NotImplementedError("TODO")


@device_bp.route("/<int:device_id>/session", methods=["GET"])
def device_session(device_id: int):
    """Return session info for a device (expires_at, remaining_seconds).

    Returns: {mac_address, status, session_expires_at, remaining_seconds}
    """
    raise NotImplementedError("TODO")
