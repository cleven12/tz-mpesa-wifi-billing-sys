"""Encryption and hashing utilities."""

import os
from typing import Optional


def hash_password(plain: str) -> str:
    """Return a bcrypt hash of *plain*.

    Args:
        plain: Plain-text password.
    """
    raise NotImplementedError("TODO")


def verify_password(plain: str, hashed: str) -> bool:
    """Return True when *plain* matches *hashed*.

    Args:
        plain: Plain-text password.
        hashed: Stored bcrypt hash.
    """
    raise NotImplementedError("TODO")


def encrypt_field(value: str, key: Optional[str] = None) -> str:
    """Encrypt a sensitive field value using Fernet symmetric encryption.

    Args:
        value: Plain-text value.
        key: Optional base64-encoded Fernet key; defaults to SECRET_KEY env var.
    """
    raise NotImplementedError("TODO")


def decrypt_field(token: str, key: Optional[str] = None) -> str:
    """Decrypt a Fernet-encrypted field value.

    Args:
        token: Encrypted token string.
        key: Same key used during encrypt_field.
    """
    raise NotImplementedError("TODO")

BCRYPT_ROUNDS = 12
FERNET_KEY_ITERATIONS = 100_000
FERNET_HASH_ALGORITHM = "SHA256"
