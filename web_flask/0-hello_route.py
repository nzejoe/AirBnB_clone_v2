#!/usr/bin/python3

""" Module that includes script that starts a Flask web application.
Web application must be listening on 0.0.0.0, port 5000
must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function called through the / route."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
