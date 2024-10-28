import os

from flask import Flask, request, abort
from .routes import main

def create_app():
    app = Flask(__name__)

    # Retrieve the secret key from an environment variable set on the hosting service
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

    @app.before_request
    def enforce_request_limits():
        if request.content_length and request.content_length > app.config['MAX_CONTENT_LENGTH']:
            abort(413)  # Payload Too Large
    
    app.register_blueprint(main)

    return app