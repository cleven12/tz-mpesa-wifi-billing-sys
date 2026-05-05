"""User CRUD and authentication logic."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class UserService:

    MAX_LOGIN_ATTEMPTS = 5
    LOCKOUT_MINUTES = 15

    """Handles user registration, authentication, and profile management."""

    def register(
        self, phone: str, name: str, password: str, email: Optional[str] = None
    ) -> dict:
        """Create a new User row and return a JWT token pair.

        Args:
            phone: Unique phone number (E.164 format).
            name: Display name.
            password: Plain-text password (will be hashed).
            email: Optional email address.

        Returns:
            dict with keys: user (dict), token (str).

        Raises:
            ValueError: When phone already exists.
        """
        raise NotImplementedError("TODO")

    def login(self, phone: str, password: str) -> dict:
        """Verify credentials and return a JWT token pair.

        Args:
            phone: Registered phone number.
            password: Plain-text password.

        Returns:
            dict with keys: user (dict), token (str).

        Raises:
            ValueError: On invalid credentials.
            PermissionError: When account is suspended.
        """
        raise NotImplementedError("TODO")

    def get_by_id(self, user_id: int):
        """Fetch and return a User by primary key, or None."""
        raise NotImplementedError("TODO")

    def get_by_phone(self, phone: str):
        """Fetch and return a User by phone number, or None."""
        raise NotImplementedError("TODO")

    def update_profile(
        self, user_id: int, name: Optional[str], email: Optional[str]
    ) -> dict:
        """Update mutable profile fields.

        Returns:
            Updated user dict.
        """
        raise NotImplementedError("TODO")

    def get_or_404(self, user_id: int):
        """Return User by id or raise 404 HTTPException."""
        raise NotImplementedError("TODO")

    def update_balance(self, user_id: int, delta: float) -> None:
        """Add *delta* (positive or negative) to user account_balance."""
        raise NotImplementedError("TODO")

    def change_password(self, user_id: int, old_password: str, new_password: str) -> None:
        """Verify old_password then update hash. Raise ValueError on mismatch."""
        raise NotImplementedError("TODO")

    def suspend(self, user_id: int, admin_id: int) -> bool:
        """Set user status to 'suspended' and write an AdminLog entry."""
        raise NotImplementedError("TODO")
