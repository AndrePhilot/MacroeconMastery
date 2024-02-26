from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/')
def show_homepage():
    """Show homepage."""

    return render_template('index.html')

@main.route('/frq-quizzer')
def show_frq_quizzer():
    """Renders the page with the FRQ Quizzer chatbot."""

    return render_template('frq_quizzer.html')


@main.route('/def-sched')
def show_def_sched():
    """Renders the page with the Definitions and Scheduler chatbot."""

    return render_template('def_sched.html')

@main.route('/course-review')
def show_course_review():
    """Renders the page containing all concepts divided by units and topic that are need to review before an exam."""

    return render_template('course_review.html')

@main.route('/<topic>')
def show_topic(topic):
    """Show Q&A of the most common concepts in a topic."""

    template_name = f"{topic}.html"

    try:
        return render_template(template_name)
    except TemplateNotFound:
        return "This page does not exist", 404


@main.route('/about')
def show_about():
    """Renders the about page."""

    return render_template('about.html')