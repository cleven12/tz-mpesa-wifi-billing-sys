"""Custom Flask route decorators."""

import functools
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_required(fn):
    """Decorator — allow only users with role='admin' in their JWT claims.

    Usage::

        @admin_bp.route("/dashboard")
        @admin_required
        def dashboard(): ...
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        raise NotImplementedError("TODO")
    return wrapper


def active_user_required(fn):
    """Decorator — reject 'suspended' or 'deleted' users even with valid JWT."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        raise NotImplementedError("TODO")
    return wrapper


def json_required(fn):
    """Decorator — return 400 when Content-Type is not application/json."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        raise NotImplementedError("TODO")
    return wrapper
