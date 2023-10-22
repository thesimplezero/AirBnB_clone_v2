#!/usr/bin/python3
"""Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Root URL route."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route for '/hbnb'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Route for '/c/<text>' with a variable 'text'."""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main":
    app.run(host='0.0.0.0', port=5000)
