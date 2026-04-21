"""Flask application factory."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
socketio = SocketIO()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)


def create_app(config_object=None):
    """Create and configure the Flask application.

    Args:
        config_object: A configuration class or dotted import path string.
                       Defaults to DevelopmentConfig when None.

    Returns:
        Flask: The configured application instance.
    """
    app = Flask(__name__, template_folder="templates", static_folder="static")

    _load_config(app, config_object)
    _init_extensions(app)
    _register_blueprints(app)
    _register_error_handlers(app)

    return app


def _load_config(app: Flask, config_object) -> None:
    """Apply configuration to *app*."""
    pass  # TODO: load from config_object or fall back to DevelopmentConfig


def _init_extensions(app: Flask) -> None:
    """Bind Flask extensions to *app*."""
    pass  # TODO: db.init_app, jwt.init_app, cors.init_app, socketio.init_app, migrate.init_app, limiter.init_app


def _register_blueprints(app: Flask) -> None:
    """Import and register all route blueprints."""
    pass  # TODO: import from routes/ and call app.register_blueprint(...)


def _register_error_handlers(app: Flask) -> None:
    """Register JSON error handlers for 400, 401, 403, 404, 500."""
    pass  # TODO: use @app.errorhandler decorators
