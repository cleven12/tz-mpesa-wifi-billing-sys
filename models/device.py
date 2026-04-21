"""Device model (WiFi-connected device linked to a user)."""

from datetime import datetime
from app import db


class Device(db.Model):
    __tablename__ = "devices"

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

    user = db.relationship("User", back_populates="devices")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<Device {self.mac_address}>"
