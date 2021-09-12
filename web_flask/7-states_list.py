#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /:              show the message 'Hello HBNB!'
    /hbnb:          show the message 'HBNB'
    /c/<text>:      show the message 'C <text>'
    /number/<n>:    show “n is a number” only if n is an integer
    /number_template/<int:n>: render a template with the argument n
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def statesList():
    """ handle the route /states_list and render a template """
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
