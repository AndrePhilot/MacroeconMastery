import os

from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    # Retrieve the secret key from an environment variable set on the hosting service
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.register_blueprint(main)

    return app