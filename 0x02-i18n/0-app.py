#!/usr/bin/env python3
""" Simple app with route showing welcome message """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """ index route """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
