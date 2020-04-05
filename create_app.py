from werkzeug.utils import find_modules, import_string
from flask import Flask, request, current_app, redirect
from utils.responses import ApiException, ApiResult
from exceptions.handler import AdminServerApiError, AdminServerAuthError, AdminServerError, AdminServerRequestError
#from utils import validator
from flask_cors import CORS
from flask_jwt_extended import JWTManager, unset_jwt_cookies
import os

class ApiFlask(Flask):
    """
    Overrides the make response method to add
    ApiResult and ApiException support  
    """

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_result()
        return Flask.make_response(self, rv)

def create_app(config=None):
    """Creates and returns a Flask app instance.

    Keyword Arguments:
        config {string} --  (default: {None})

    Returns:
        [flask_application] -- instance of a flask app
    """
    app = ApiFlask(__name__)
    with app.app_context():
        app.config.from_object(config or {})

        # Setup Flask Secret Key
        app.secret_key = os.urandom(24)

        # Setup JWTManager to the app context on the attribute "jwt"
        app.config['JWT_BLACKLIST_ENABLED'] = True
        app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
        app.__setattr__("jwt", JWTManager(app))

        # Setup CORS for all endpoints
        register_cors(app)

        # Setup database plugin
        #sql_db.init_app(app)

        # Setup Flask blueprints to establish app endpoints
        register_blueprints(app)

        # Register the error handlers
        register_error_handlers(app)

        # register '/api endpoint'
        register_base_url(app)

        return app

def register_blueprints(app):
    """Register all blueprints under the {.blueprint} module
    in the passed application instance.

    Arguments:
        app {flask application} -- application instance
    """
    for name in find_modules('blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            # Must add `mod.bp` since `mod` alone intales the hole package and not the Blueprint obj
            app.register_blueprint(mod.blueprint)


def register_base_url(app):
    @app.route('/')
    @app.route('/admin/api/')
    def api():
        return ApiResult(body = 
            {
                'message': 'You have reach the IReNE Administrative API. Please refer to the documentation.'
            }
        )


def register_cors(app: Flask):
    """
        Setup CORS , cross-origin-resource-sharing settings
    """

    origins_list = '*'

    methods_list= ['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS']

    allowed_headers_list = [
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Methods', 
        'Access-Control-Allow-Origin',
        'Content-Type',
        'Authorization',
        'Content-Disposition',
        'Referrer-Policy',
        'Strict-Transport-Security',
        'X-Frame-Options',
        'X-Xss-Protection',
        'X-Content-Type-Options',
        'X-Permitted-Cross-Domain-Policies'
    ]
    
    CORS(
        app=app,
        resources={r"/admin/api/*": {"origins": origins_list}},
        methods=methods_list,
        allowed_headers=allowed_headers_list,
        supports_credentials=True
    )

def register_error_handlers(app):
    """Register error daos to flask application instance.

    Arguments:
        app {flask application} -- application instance
    """
    if False:#app.config['DEBUG']:
        # If debug true, then return the whole stack
        @app.errorhandler(AdminServerError)
        def handle_error(error):
            return ApiException(
                error_type=error.__class__.__name__,
                message=error.error_stack,
                status=error.status
            )
    else:
        @app.errorhandler(AdminServerApiError)
        def handle_error(error):
            return ApiException(
                error_type=error.__class__.__name__,
                message=error.msg,
                status=error.status
            )

        @app.errorhandler(AdminServerAuthError)
        def handle_auth_error(error):
            return ApiException(
                error_type=error.__class__.__name__,
                message=error.msg,
                status=error.status
            )

        @app.errorhandler(AdminServerRequestError)
        def handle_request_error(error):
            return ApiException(
                error_type=error.__class__.__name__,
                message=error.msg,
                status=error.status
            )

        @app.errorhandler(Exception)
        def handle_unexpected_error(error):
            AdminServerError(
                err=error,
                msg='An unexpected error has occurred.',
                status=500
            ).log()
            return ApiException(
                error_type='UnexpectedException',
                message='An unexpected error has occurred.',
                status=500
            )
        jwt = app.jwt
        @jwt.invalid_token_loader
        def invalid_token_callback(callback):
            # Invalid Fresh/Non-Fresh Access token in auth header
            resp = app.make_response(redirect('/admin/api/auth/login'))
            unset_jwt_cookies(resp)
            return resp, 302

        @jwt.needs_fresh_token_loader
        def nonfresh_token_callback(callback):
            # Invalid Non-Fresh Access token in auth header
            resp = app.make_response(redirect('/admin/api/auth/login'))
            unset_jwt_cookies(resp)
            return resp, 302 

    app.register_error_handler(
        400,
        lambda err: ApiException(message=str(
            err), status=400, error_type='Bad request')
    )

    app.register_error_handler(
        404,
        lambda err: ApiException(message=str(
            err), status=404, error_type='Not found')
    )

    app.register_error_handler(
        405,
        lambda err: ApiException(message=str(
            err), status=405, error_type='Request method')
    )