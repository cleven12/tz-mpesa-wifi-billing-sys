"""Routes package.

Blueprint URL prefixes:
    auth_bp    → /api/auth
    payment_bp → /api/payment
    device_bp  → /api/devices
    admin_bp   → /api/admin
    webhook_bp → /webhook
"""

from routes.auth import auth_bp
from routes.payment import payment_bp
from routes.device import device_bp
from routes.admin import admin_bp
from routes.webhook import webhook_bp

__all__ = ["auth_bp", "payment_bp", "device_bp", "admin_bp", "webhook_bp"]
