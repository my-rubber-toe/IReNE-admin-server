from flask import Flask
from create_app import create_app

app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=80, debug=True)