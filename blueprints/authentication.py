"""
authentication.py
====================================
Every route regarding authentication, including but not limited to login, logout and current user id can be found here.
"""
from flask import current_app, jsonify
from flask import Blueprint, Flask, request, g
from flask_jwt_extended import create_access_token, get_jwt_identity, fresh_jwt_required, \
    get_raw_jwt
from utils.responses import ApiResult, ApiException
from cachetools import TTLCache
from datetime import timedelta
from daos.admin_dao import AdminDAO
from utils.validators import username_isvalid, password_isvalid

blueprint = Blueprint('authentication', __name__, url_prefix='/admin/auth')
dao = AdminDAO()
# Set blacklist set for blacklisted tokens
token_blacklist = TTLCache(maxsize=10000, ttl=600)


@current_app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """
    Verifies if a token has been blacklisted.

    Returns
    -------
    JTI
        Blaclisted token or None if the token is not found.
    """
    """"""
    jti = decrypted_token['jti']
    if token_blacklist.currsize == 0:
        return False
    entry = token_blacklist.get(jti)  # search for the jti on the blacklist#
    return entry


@blueprint.route('/login', methods=['POST'])
def login():
    """
    Generate a new access token for the user. User must have valid credentials in the databse to get a valid token.
    
    Parameters
    ----------
    username : string
        Username of the administrator account.
    password : string
        Password of the administrator account.

    Returns
    -------
    string
        JWT token with the username as identity.
    
    returns
    ------
    ApiException
        If the username or password fields are empty or are invalid. 

    """

    username = request.form.get("username")
    password = request.form.get("password")
    if not username_isvalid(username) or not password_isvalid(password):
        return ApiException(
            error_type = "Authentication Error",
            message='Invalid username or password.',
            status=401
        )
    admin = dao.get_admin(username)
    if not admin:
        return ApiException(
            error_type = "Authentication Error",
            message='Invalid username or password.',
            status=401
        )
    authorized = dao.check_password(admin['password'], password)
    if not authorized:
        return ApiException(
            error_type = "Authentication Error",
            message='Invalid username or password.',
            status=401
        )

    return ApiResult(body=
                     {'access_token': create_access_token(identity=username, fresh=True,
                                                          expires_delta=timedelta(minutes=10))}
                     )


@blueprint.route('/me', methods=['GET'])
@fresh_jwt_required
def me():
    """
    Returns the username of the currently active administrator.
    Returns
    -------
    string
        Username of admin.

    """
    return ApiResult(body=
                     {'identity': get_jwt_identity()}
                     )


@blueprint.route("/logout", methods=['GET'])
@fresh_jwt_required
def logout():
    """
    Revoke the authorization and adds token to a blacklist of previously used tokens.

    Returns
    -------
    string
        Successfull message.
    string
        Identity of the logout admin.
    """
    # Blacklist jwt tokens
    jti = get_raw_jwt()['jti']
    token_blacklist[jti] = True  # Add the jti to the cache with value true #

    return ApiResult(body=
                     {'message': "Successfully logged out.",
                      'username': get_jwt_identity()}
                     )
