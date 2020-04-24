"""
app.py
=======
Main file that runs the application.
"""
from flask import Flask
from create_app import create_app

app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(host= 'localhost', port=5000, debug=True)