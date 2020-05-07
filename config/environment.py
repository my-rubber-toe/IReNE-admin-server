import os

FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
PORT = os.getenv("PORT")
HOST = os.getenv('HOST')

DB_HOST = os.getenv("DB_HOST")

ENABLE_EMAIL = os.getenv('ENABLE_EMAIL')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWD = os.getenv('EMAIL_PASSWD')

# Authorization
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
FLASK_SALT = os.getenv("FLASK_SALT")
