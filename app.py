import os

from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

def create_app():
    app = Flask(__name__)

    # Retrieve the secret key from an environment variable set on Render
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    return app


@app.route('/')
def show_homepage():
    """Show homepage."""

    return render_template('index.html')

@app.route('/frq-quizzer')
def show_frq_quizzer():
    """Renders the page with the FRQ Quizzer chatbot."""

    return render_template('frq_quizzer.html')


@app.route('/def-sched')
def show_def_sched():
    """Renders the page with the Definitions and Scheduler chatbot."""

    return render_template('def_sched.html')

@app.route('/course-review')
def show_course_review():
    """Renders the page containing all concepts divided by units and topic that are need to review before an exam."""

    return render_template('course_review.html')

@app.route('/<topic>')
def show_topic(topic):
    """Show Q&A of the most common concepts in a topic."""

    template_name = f"{topic}.html"

    try:
        return render_template(template_name)
    except TemplateNotFound:
        return "This page does not exist", 404


@app.route('/about')
def show_about():
    """Renders the about page."""

    return render_template('about.html')