import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Retrieve the secret key from an environment variable set on Render
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
toolbar = DebugToolbarExtension(app)

