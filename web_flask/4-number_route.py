#!/usr/bin/python3

""" Module that includes script that starts a Flask web application.
Web application must be listening on 0.0.0.0, port 5000
Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    - `/python/<text>`: display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
    - /number/<n>: display “`n` is a number” only if `n` is an integer
must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function called through the / route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function called through the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Function called through the /c/<text> route."""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Function called through the /python/<text> route."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Function that displays "n is a number" if n is indeed an integer."""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
