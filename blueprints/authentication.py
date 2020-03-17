from flask import Blueprint, Response, request

auth_blueprint = Blueprint('authentication', __name__, url_prefix='/admin/api/auth')



@auth_blueprint.route('/login', methods=['GET'])
def login():
    """
    Login the user and establish a new firebase session using a valid firebase token. 
    If a session already exists, then return an `ApiException` response

    Returns
    -------
    Response
        The flask response object containing the result of a successfull login.
    """

    # Verify if the session cookie exists and the session is valid
    """if current_app.session_cookie_name in request.cookies and session_handler.check_valid_session() is not False:
        return ApiException('A valid session already exists!', _type='Authentication', status=401)
    
    try:
        id_token = request.headers['Authorization'].split(' ')[1]
        return session_handler.session_login(id_token)
    except ValueError:
        return ApiException('Invalid token!', _type='Authentication', status=401)"""
    pass


@auth_blueprint.route('/logout', methods=['GET'])
def logout():
    """
    Logout the user and by setting the user session invalid and revoking all tokens from the user.

    Returns
    -------
    Response
        The flask response object containing the result of a successfull logout.
    """
    pass
    #return session_handler.session_logout()


@auth_blueprint.route('/verify', methods=['GET'])
def verify():
    """
    Verify user sessions and return session informatio

    Returns
    -------
    Response
        The flask response object containing a valid `dict` with the session information 

    """
    pass
    """return ApiResult({
        'message': 'TO-DO: Verify email!',
    })"""

@auth_blueprint.route('/register', methods=['POST'])
def register_user():
    """ Registers new user to the database"""
    pass
    #return user_handler.register_new_user(request.json)

@auth_blueprint.before_request
def authentication_before_req():
    """
    `Before request` function for the `admin/api/auth/` routes to validate the sessions and token
    information. If a valid session is found, the session token is refreshed.
    """
    pass
