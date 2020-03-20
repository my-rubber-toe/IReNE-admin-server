from flask import current_app, jsonify
from flask import Blueprint, Response, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, \
    jwt_required, get_jwt_identity, get_raw_jwt
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from datetime import timedelta



blueprint = Blueprint('authentication', __name__, url_prefix='/admin/api/auth')

# Set blacklist set for blacklisted tokens
# TODO: Replace blacklist with a Redis Store
token_blacklist = set()


@current_app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """Verifies if a token has been blacklisted."""
    jti = decrypted_token['jti']
    return jti in token_blacklist


@blueprint.route('/login')
def login():
    """Generate a new access token for the user. User must sign in to the databse to get a valid token.
    """
    username_exists = True
    username = request.form.get("username")
    #TODO: Check if admin username exists in DB
    if not username_exists:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    # Use the username as the token identity
    return ApiResult(
        access_token=create_access_token(identity=username, expires_delta=timedelta(hours=1)),
        refresh_token=create_refresh_token(identity=username, expires_delta=timedelta(weeks=2))
    )


@blueprint.route('/me')
@jwt_required
def me():
    """"Return information from the database."""
    # TODO: Use DAOs to look for user in the database.
    return ApiResult(identity=get_jwt_identity())


@blueprint.route('/refresh', methods=["GET"])
@jwt_refresh_token_required
def refresh():
    """Return a new access_token given a valid refresh token."""
    username = get_jwt_identity()
    return ApiResult(access_token=create_access_token(identity=username, expires_delta=timedelta(hours=2)))


@blueprint.route("/logout")
@jwt_required
def logout():
    """Revoke the Google authorization and add tokens to blacklist"""
    # Blacklist jwt tokens
    jti = get_raw_jwt()['jti']
    token_blacklist.add(jti)
    return ApiResult(message="Successfully logged out.")