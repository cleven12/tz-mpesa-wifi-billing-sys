"""Transaction model — one-to-one with Payment; stores raw PesaPal callback."""

from datetime import datetime
from app import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.id"), unique=True, nullable=False)
    pesapal_confirmation_code = db.Column(db.String(100), unique=True, nullable=True)
    raw_callback_payload = db.Column(db.JSON, nullable=True)
    processing_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    payment = db.relationship("Payment", back_populates="transaction")

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dictionary representation."""
        raise NotImplementedError("TODO")

    @classmethod
    def get_by_payment_id(cls, payment_id: int) -> "Transaction | None":
        """Return transaction for a given payment ID."""
        raise NotImplementedError("TODO")

    @classmethod
    def get_by_confirmation_code(cls, code: str) -> "Transaction | None":
        """Return transaction by PesaPal confirmation code."""
        raise NotImplementedError("TODO")

    def __repr__(self) -> str:
        return f"<Transaction payment_id={self.payment_id}>"
