"""
create_app.py
====================================
File that contains all the initializations needed for the program to work.
"""
from werkzeug.utils import find_modules, import_string
from flask import Flask, request, current_app, redirect
from utils.responses import ApiException, ApiResult
from exceptions.handler import AdminServerApiError, AdminServerAuthError, AdminServerError, AdminServerRequestError
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from database import schema_DB 

class ApiFlask(Flask):
    """
    Overrides the make response method to add ApiResult and ApiException support.
    """

    def make_response(self, rv):
        """
        Returns whether or not the password given is in a valid format.
        
        Parameters
        ----------
            rv : object
                Result object to be getting the response from.
        
        Returns
        -------
        object
            Flask http reponse object

        """
        if isinstance(rv, ApiResult):
            return rv.to_response()
        if isinstance(rv, ApiException):
            return rv.to_result()
        return Flask.make_response(self, rv)


def create_app(config=None):
    """
    Returns whether or not the password given is in a valid format.
    
    Parameters
    ----------
        config : string
            String with the path to the config file
    
    Returns
    -------
    ApiFlask
        Application instance with all the initializations performed

    """
    app = ApiFlask(__name__)
    with app.app_context():
        app.config.from_object(config or {})

        # Setup Flask Secret Key
        app.secret_key = "Iamthedatabasekey_Icannotberandom"

        # Setup JWTManager to the app context on the attribute "jwt"
        app.config['JWT_BLACKLIST_ENABLED'] = True
        app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
        app.__setattr__("jwt", JWTManager(app))

        # Setup CORS for all endpoints
        register_cors(app)

        # Setup Flask blueprints to establish app endpoints
        register_blueprints(app)

        # Register the error handlers
        register_error_handlers(app)

        # register '/api endpoint'
        register_base_url(app)

        return app


def register_blueprints(app):
    """
    Register all blueprints under the {.blueprint} module in the passed application instance.
    
    Parameters
    ----------
        app : ApiFlask
            Application instance

    """
    for name in find_modules('blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            # Must add `mod.bp` since `mod` alone intales the hole package and not the Blueprint obj
            app.register_blueprint(mod.blueprint)


def register_base_url(app):
    """
    Register the base url for the application instance.
    
    Parameters
    ----------
        app : ApiFlask
            Application instance
    """

    @app.route('/')
    @app.route('/admin/')
    def api():
        return ApiResult(body=
        {
            'message': 'You have reach the IReNE Administrative API. Please refer to the documentation.'
        }
        )


def register_cors(app: Flask):
    """
    Method to setup CORS, cross-origin-resource-sharing settings
    
    Parameters
    ----------
        app : Flask
            Application instance
    """

    origins_list = '*'

    methods_list = ['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS']

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
        resources={r"/admin/*": {"origins": origins_list}},
        methods=methods_list,
        allowed_headers=allowed_headers_list,
        supports_credentials=True
    )


def register_error_handlers(app):
    """
    Registers the error handler for the flask application instance.
    
    Parameters
    ----------
        app : Flask
            Application instance
    """
    if True:  # app.config['DEBUG']:
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
            return ApiException(
                error_type='AdminServerRequestError',
                message='Invalid Authentication Token.',
                status=400
            )

        @jwt.needs_fresh_token_loader
        def nonfresh_token_callback(callback):
            # Invalid Non-Fresh Access token in auth header
            return ApiException(
                error_type='AdminServerRequestError',
                message='Invalid Authentication Token - Not Fresh.',
                status=400
            )

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
