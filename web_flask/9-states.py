#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /states:        render a template with all states in storage
    /states/<id>:   render a template with all cities of the state id
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def statesList():
    """ handle the route /states and render a template """
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def statesCities(id):
    """ handle the route /states/<id> and render a template """
    all_states = storage.all(State)

    state_id = "State." + id
    if state_id in all_states:
        state = all_states[state_id]
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        setattr(state, "sorted_cities", sorted_cities)
    else:
        state = None
    print(state)

    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
