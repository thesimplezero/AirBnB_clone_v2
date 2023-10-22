#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    Route to '/python/' and '/python/<text>'
    with a default value for 'text'.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Route to 'number' for integers only."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n=None):
    """Render an HTML page."""
    return render_template('5-number.html', n=n)


if __name__ == "__main":
    app.run(host='0.0.0.0', port=5000)
