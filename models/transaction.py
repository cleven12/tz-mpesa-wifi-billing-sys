"""Transaction model — one-to-one extension of Payment with M-Pesa metadata."""

from datetime import datetime
from app import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.id"), unique=True, nullable=False)
    mpesa_transaction_id = db.Column(db.String(100), unique=True, nullable=True)
    raw_callback_payload = db.Column(db.JSON, nullable=True)
    processing_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    payment = db.relationship("Payment", back_populates="transaction")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<Transaction {self.id}>"
