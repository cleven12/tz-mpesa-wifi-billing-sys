"""Authentication routes — /api/auth/..."""

# HTTP status codes used in this blueprint
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_429_TOO_MANY_REQUESTS = 429

from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# POST /register  body: {phone: str, password: str, name: str, email?: str}
# POST /login      body: {phone: str, password: str}
# GET  /profile    header: Authorization: Bearer <token>
# PUT  /profile    body: {name?: str, email?: str}
# POST /logout     header: Authorization: Bearer <token>
# POST /refresh    header: Authorization: Bearer <refresh_token>

@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user.

    Body JSON keys: phone, name, email (optional), password
    Returns 201 with {success, user, token} on success.
    """
    raise NotImplementedError("TODO")


@auth_bp.route("/login", methods=["POST"])
def login():
    """Authenticate an existing user.

    Body JSON keys: phone, password
    Returns 200 with {success, token, user} on success.
    """
    raise NotImplementedError("TODO")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """Invalidate the current JWT token.

    Requires Authorization: Bearer <token>
    """
    raise NotImplementedError("TODO")


@auth_bp.route("/refresh", methods=["POST"])
def refresh():
    """Return a new access token using a valid refresh token."""
    raise NotImplementedError("TODO")


@auth_bp.route("/profile", methods=["GET"])
def get_profile():
    """Return the authenticated user's profile.

    Requires Authorization: Bearer <token>
    """
    raise NotImplementedError("TODO")


@auth_bp.route("/profile", methods=["PUT"])
def update_profile():
    """Update name / email for the authenticated user.

    Requires Authorization: Bearer <token>
    Body JSON keys: name (optional), email (optional)
    """
    raise NotImplementedError("TODO")
