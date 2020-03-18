from werkzeug.utils import find_modules, import_string
from flask import Flask, request, current_app
from utils.responses import ApiException, ApiResult
#from utils import validator
from flask_cors import CORS
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

    app.config.from_object(config or {})
    
    app.secret_key = app.config['SECRET_KEY']


    # Setup CORS for all endpoints
    register_cors(app)

    # Setup database plugin
    #sql_db.init_app(app)

    # Setup Flask blueprints to establish app endpoints
    register_blueprints(app)

    # Register the error handlers
    #register_error_handlers(app)

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
        return ApiResult(
            {
                'message': 'You have reach the IReNE Administrative API. Please refer to the documentation.'
            },
            status=200
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