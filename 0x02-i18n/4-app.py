#!/usr/bin/env python3
"""A simple Flask app
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
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Get the locale based on request parameters or accept_languages.

    Returns:
        str: The best-matching locale from the supported languages.
    """
    # Check if the 'locale' parameter is present in the request args
    requested_locale = request.args.get('locale')
    
    # If 'locale' parameter is present and is a supported locale, return it
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # If 'locale' parameter is not present or is not a supported locale,
    # resort to the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the 4-index.html template.

    Returns:
        str: Rendered content of the 4-index.html template.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
