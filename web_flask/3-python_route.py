#!/usr/bin/python3
"""Start a Flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root URL route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    "/hbnb" route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Route for '/c/<text>'.
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    "/python/" and "/python/<text>" route.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main":
    app.run(host='0.0.0.0', port=5000)
