"""User model."""

from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    account_balance = db.Column(db.Numeric(10, 2), default=0.00)
    status = db.Column(
        db.Enum("active", "suspended", "deleted", name="user_status"),
        default="active",
        index=True,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)

    payments = db.relationship("Payment", back_populates="user", lazy="dynamic")
    devices = db.relationship("Device", back_populates="user", lazy="dynamic")
    admin_logs = db.relationship(
        "AdminLog",
        back_populates="admin",
        lazy="dynamic",
        foreign_keys="AdminLog.admin_id",
    )

    def set_password(self, password: str) -> None:
        """Hash *password* and store in password_hash."""
        raise NotImplementedError("TODO")

    def check_password(self, password: str) -> bool:
        """Return True when *password* matches the stored hash."""
        raise NotImplementedError("TODO")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<User {self.phone}>"
