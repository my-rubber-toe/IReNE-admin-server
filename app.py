"""
app.py
=======
Main file that runs the application.
"""
from flask import Flask
from create_app import create_app
from config import environment

app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(host=environment.HOST, port=environment.PORT, debug=environment.FLASK_DEBUG)