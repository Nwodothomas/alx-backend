#!/usr/bin/env python3
"""A simple flask app with Babel
"""

from flask import Flask, render_template
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


@app.route('/')
def index():
    """Route to render the index.html template.

    Returns:
        str: Rendered content of the index.html template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
