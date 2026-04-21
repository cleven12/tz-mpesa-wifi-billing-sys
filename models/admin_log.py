"""AdminLog model — audit trail for admin actions."""

from datetime import datetime
from app import db


class AdminLog(db.Model):
    __tablename__ = "admin_logs"

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    action = db.Column(db.String(255), nullable=False, index=True)
    details = db.Column(db.JSON, nullable=True)
    affected_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    status = db.Column(
        db.Enum("success", "failed", name="log_status"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    admin = db.relationship("User", back_populates="admin_logs", foreign_keys=[admin_id])

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<AdminLog {self.action} by admin {self.admin_id}>"
