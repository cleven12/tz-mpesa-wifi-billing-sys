"""Configuration package."""

from config.settings import DevelopmentConfig, ProductionConfig, TestingConfig

CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

__all__ = ["DevelopmentConfig", "ProductionConfig", "TestingConfig", "CONFIG_MAP"]
