""" Script that starts a Flask web application  with a route:
    /: show the message 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """ handle the root route and show a message """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
