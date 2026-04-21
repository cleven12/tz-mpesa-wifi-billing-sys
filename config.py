"""Top-level config shim. The real configuration lives in config/settings.py."""

from config.settings import DevelopmentConfig, ProductionConfig, TestingConfig

__all__ = ["DevelopmentConfig", "ProductionConfig", "TestingConfig"]
