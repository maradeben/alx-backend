#!/usr/bin/env python3
""" Simple app with route showing welcome message """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ configuration settings """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ get locale function
        Order:
            - from URL parameters
            - from user settings
            - from request header
            - default locale
    """
    langs = app.config['LANGUAGES']

    # from url parameters
    if request.args.get('locale') and request.args['locale'] in langs:
        return request.args['locale']
    # from user settings
    elif g.user['locale'] and g.user['locale'] in langs:
        return g.user['locale']
    # from request header
    elif request.headers.get('locale') and \
            request.headers.get('locale') in langs:
        return request.headers.get('locale')
    # default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """ returns a user dict if user present in database"""
    try:
        user_id = int(request.args.get('login_as'))
        if user_id and user_id in users:
            return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """ function called before """
    g.user = get_user()


@app.route("/")
def index() -> str:
    """ index route """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
