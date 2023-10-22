#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Root URL route for saying 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route for saying 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Route for displaying 'C' and a variable,
    replacing underscores with spaces.
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    Route for displaying 'Python' and a variable,
    replacing underscores with spaces.
    If 'text' is not provided, it defaults to 'is_cool'.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    Route for displaying whether a number is a number.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n=None):
    """
    Route for rendering an HTML page with a number 'n'.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_template(n=None):
    """Route for rendering an HTML page to check if a number is odd or even."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main":
    app.run(host='0.0.0.0', port=5000)
