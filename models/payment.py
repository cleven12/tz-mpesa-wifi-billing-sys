"""Payment model."""

from datetime import datetime
from app import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False, index=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    package_id = db.Column(db.Integer, nullable=True)
    status = db.Column(
        db.Enum("pending", "completed", "failed", "timeout", name="payment_status"),
        default="pending",
        index=True,
    )
    mpesa_receipt = db.Column(db.String(50), nullable=True)
    checkout_request_id = db.Column(db.String(255), unique=True, nullable=True)
    merchant_request_id = db.Column(db.String(255), nullable=True)
    result_code = db.Column(db.Integer, nullable=True)
    result_description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    expires_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="payments")
    transaction = db.relationship("Transaction", back_populates="payment", uselist=False)

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<Payment {self.id} {self.status}>"
