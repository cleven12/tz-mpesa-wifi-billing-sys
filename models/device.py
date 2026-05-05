"""Device model (WiFi-connected device linked to a user)."""

from datetime import datetime
from app import db


class Device(db.Model):
    __tablename__ = "devices"

    STATUS_ACTIVE = "active"
    STATUS_WHITELISTED = "whitelisted"
    STATUS_BLOCKED = "blocked"

    DEVICE_TYPE_MOBILE = "mobile"
    DEVICE_TYPE_LAPTOP = "laptop"
    DEVICE_TYPE_TABLET = "tablet"
    DEVICE_TYPE_OTHER = "other"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    mac_address = db.Column(db.String(17), unique=True, nullable=False, index=True)
    device_name = db.Column(db.String(100), nullable=True)
    device_type = db.Column(
        db.Enum("mobile", "laptop", "tablet", "other", name="device_type"),
        default="other",
    )
    os_type = db.Column(db.String(50), nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    first_connected = db.Column(db.DateTime, default=datetime.utcnow)
    last_connected = db.Column(db.DateTime, nullable=True)
    status = db.Column(
        db.Enum("active", "whitelisted", "blocked", name="device_status"),
        default="active",
        index=True,
    )

    session_expires_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="devices")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    @classmethod
    def get_by_mac(cls, mac_address: str) -> "Device | None":
        """Find device by MAC address (case-insensitive)."""
        raise NotImplementedError("TODO")

    @classmethod
    def get_active_for_user(cls, user_id: int) -> list:
        """Return all whitelisted / active devices for a user."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<Device {self.mac_address}>"
