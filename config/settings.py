"""Application settings classes."""

import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:

    @classmethod
    def from_env(cls):
        """Instantiate config from environment variables."""
        raise NotImplementedError("TODO")

    @classmethod
    def validate(cls):
        """Raise ValueError if required env vars are missing."""
        raise NotImplementedError("TODO")

    """Shared defaults for all environments."""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret")
    JWT_ACCESS_TOKEN_EXPIRES: int = int(os.getenv("JWT_EXPIRATION_HOURS", 24)) * 3600
    CORS_ORIGINS: list = []
    SOCKETIO_ASYNC_MODE: str = "eventlet"


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///wifi_billing.db")
    CORS_ORIGINS: list = ["*"]


class TestingConfig(BaseConfig):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"
    JWT_ACCESS_TOKEN_EXPIRES: int = 3600


class ProductionConfig(BaseConfig):
    DEBUG: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "")
    CORS_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "").split(",")
