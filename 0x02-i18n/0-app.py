#!/usr/bin/env python3
""" Simple app with route showing welcome message """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """ index route """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
