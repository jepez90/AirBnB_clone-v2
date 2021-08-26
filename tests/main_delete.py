#!/usr/bin/python3
""" Test delete feature
"""
import os, sys
sys.path.append(os.path.abspath('..'))
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new City
new_city = City()
new_city.name = "LA"
new_city.state_id = another_state.id
fs.new(new_city)
fs.save()
print("New City: {}".format(new_city))


# All States
all_states = fs.all()
print("All: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])


# Delete the new City
fs.delete(new_city)


# All States
all_states = fs.all()
print("All: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
