#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /:              show the message 'Hello HBNB!'
    /hbnb:          show the message 'HBNB'
    /c/<text>:      show the message 'C <text>'
    /number/<n>:    show “n is a number” only if n is an integer
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """ handle the root route and show a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ handle the route /hbnb and show a message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def CIsFun(text=''):
    """ handle the route /c/<text> and show a message """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n=''):
    """ handle the route /number/<int:n>: and show a message """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
