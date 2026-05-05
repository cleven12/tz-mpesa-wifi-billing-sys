"""Admin routes — /api/admin/... (JWT + admin role required)."""

# All admin routes require @admin_required decorator (utils/decorators.py).
# Import it once implemented: from utils.decorators import admin_required

# Default pagination settings
DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 25
MAX_PER_PAGE = 100

from flask import Blueprint, request, jsonify

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")


@admin_bp.route("/dashboard", methods=["GET"])
def dashboard():
    """Return aggregated stats: total_users, total_revenue, active_sessions, etc."""
    raise NotImplementedError("TODO")


@admin_bp.route("/users", methods=["GET"])
def list_users():
    """Return paginated list of all users.

    Query params: page, limit, status
    """
    raise NotImplementedError("TODO")


@admin_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    """Return a single user's full profile and payment history."""
    raise NotImplementedError("TODO")


@admin_bp.route("/users/<int:user_id>/suspend", methods=["POST"])
def suspend_user(user_id: int):
    """Suspend a user account and revoke all active devices."""
    raise NotImplementedError("TODO")


@admin_bp.route("/payments", methods=["GET"])
def list_payments():
    """Return paginated payment records.

    Query params: page, limit, status
    """
    raise NotImplementedError("TODO")


@admin_bp.route("/devices", methods=["GET"])
def list_all_devices():
    """Return all devices currently tracked in the system."""
    raise NotImplementedError("TODO")


@admin_bp.route("/devices/<int:device_id>/block", methods=["POST"])
def block_device(device_id: int):
    """Block a device MAC address on the router."""
    raise NotImplementedError("TODO")


@admin_bp.route("/logs", methods=["GET"])
def list_logs():
    """Return paginated admin activity logs.

    Query params: page, limit
    """
    raise NotImplementedError("TODO")
