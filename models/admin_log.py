"""AdminLog model — audit trail for admin actions."""

from datetime import datetime
from app import db


class AdminLog(db.Model):
    __tablename__ = "admin_logs"

    ACTION_LOGIN = "admin_login"
    ACTION_SUSPEND_USER = "suspend_user"
    ACTION_ACTIVATE_USER = "activate_user"
    ACTION_BLOCK_DEVICE = "block_device"
    ACTION_WHITELIST_DEVICE = "whitelist_device"
    ACTION_REFUND = "refund"
    ACTION_EXPORT = "export_data"

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

    @classmethod
    def log_action(cls, admin_id: int, action: str, details: dict = None,
                   affected_user_id: int = None, status: str = "success") -> "AdminLog":
        """Create and persist an audit log entry."""
        raise NotImplementedError("TODO")

    @classmethod
    def get_recent(cls, limit: int = 50) -> list:
        """Return the most recent *limit* log entries ordered by created_at desc."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<AdminLog {self.action} by admin {self.admin_id}>"
