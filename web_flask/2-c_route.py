#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /:          show the message 'Hello HBNB!'
    /hbnb:      show the message 'HBNB'
    /c/<text>:  show the message 'C <text>'
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
