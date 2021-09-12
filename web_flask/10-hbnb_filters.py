#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /hbnb_filters:    render a template with all states and its cities
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def statesAndCities():
    """ handle the route /cities_by_states and render a template """
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda state: state.name)
    for state in all_states:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        setattr(state, "sorted_cities", sorted_cities)
    all_amenities = storage.all(Amenity).values()
    all_amenities = sorted(all_amenities, key=lambda am: am.name)
    return render_template('10-hbnb_filters.html', states=all_states,
                           amenities=all_amenities)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
