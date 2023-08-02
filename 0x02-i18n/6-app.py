#!/usr/bin/env python3
"""A simple Flask app with user login system and Babel for internationalization
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

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

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Get the locale based on user preferences, request parameters, or accept_languages.

    Returns:
        str: The best-matching locale from the supported languages.
    """
    # Check if the 'locale' parameter is present in the request args
    requested_locale = request.args.get('locale')

    # Check if a user is logged in and has a preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # If 'locale' parameter is present and is a supported locale, return it
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Resort to the default behavior - get locale from request.accept_languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user(user_id):
    """Get the user dictionary based on the user ID.

    Args:
        user_id (int): ID of the user to find.

    Returns:
        dict or None: The user dictionary if found, None if not found.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """Function executed before all other functions to set the user in flask.g.user."""
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)

@app.route('/')
def index():
    """Render the 6-index.html template.

    Returns:
        str: Rendered content of the 6-index.html template.
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
