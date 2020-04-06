from flask import current_app, jsonify
from flask import Blueprint, Flask, request
from flask_jwt_extended import create_access_token, get_jwt_identity, fresh_jwt_required, \
     get_raw_jwt, unset_jwt_cookies
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerAuthError
from cachetools import TTLCache
from datetime import timedelta
from daos.admin import AdminDAO



blueprint = Blueprint('authentication', __name__, url_prefix='/admin/auth')
dao = AdminDAO()
# Set blacklist set for blacklisted tokens
# TODO change ttl to the decided token ttl
token_blacklist = TTLCache(maxsize=10000, ttl=600)


@current_app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """Verifies if a token has been blacklisted."""
    jti = decrypted_token['jti'] 
    if token_blacklist.currsize == 0:
        return False
    entry = token_blacklist.get(jti)  #search for the jti on the blacklist#
    return entry


@blueprint.route('/login')
def login():
    """Generate a new access token for the user. User must sign in to the databse to get a valid token.
    """
    username = request.form.get("username")
    password = request.form.get("password")
    if username is None or username=='':
        raise AdminServerAuthError(
            msg= 'Username field is empty.', 
            status = 400
            )
    if password is None or password=='':
        raise AdminServerAuthError(
            msg= 'Password field is empty.', 
            status = 400
            )
    admin = dao.get_admin(username)
    if not admin:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    authorized = dao.check_password(admin['password_hash'], password)
    if not authorized:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    # Use the username as the token identity
    return ApiResult(body =
        {'access_token':create_access_token(identity=username, fresh = timedelta(hours=1))}
    )


@blueprint.route('/me')
@fresh_jwt_required
def me():
    """"Return information from the database."""
    # TODO: Use DAOs to look for user in the database.
    return ApiResult(body = 
    {'identity':get_jwt_identity()}
    )


@blueprint.route('/refresh', methods=["GET"])
@fresh_jwt_required
def get_fresh():
    """Return a new access_token given a valid refresh token."""
    username = get_jwt_identity()
    return ApiResult(body = 
    {'access_token':create_access_token(identity=username, fresh=timedelta(hours=1))}
    )


@blueprint.route("/logout")
@fresh_jwt_required
def logout():
    """Revoke the authorization and add tokens to blacklist"""
    # Blacklist jwt tokens
    jti = get_raw_jwt()['jti']
    token_blacklist[jti] = True   # Add the jti to the cache with value true #
    print(token_blacklist)
    return ApiResult(body = 
    {'message':"Successfully logged out."}
    )