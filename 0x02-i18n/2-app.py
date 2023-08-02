#!/usr/bin/env python3
"""A simple Flask app with Babel
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class for Flask-Babel

    Attributes:
        LANGUAGES (list): List of available languages for translation.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best-matching locale for the user based on request.accept_languages.

    Returns:
        str: The best-matching locale from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route to render the 2-index.html template.

    Returns:
        str: Rendered content of the 2-index.html template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
