#!/usr/bin/python3
""" Script that starts a Flask web application  with a route:
    /hbnb:      render a template with all states and its cities
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def statesAndCities():
    """ handle the route /hbnb and render a template """
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda state: state.name)
    for state in all_states:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        setattr(state, "sorted_cities", sorted_cities)

    all_amenities = storage.all(Amenity).values()
    all_amenities = sorted(all_amenities, key=lambda am: am.name)

    all_places = storage.all(Place).values()
    all_places = sorted(all_places, key=lambda place: place.name)

    return render_template('100-hbnb.html', states=all_states,
                           amenities=all_amenities, places=all_places)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
