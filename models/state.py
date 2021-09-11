#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm.base import attribute_str
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        print('dbstorage used')
        cities = relationship("City", back_populates="state")
        name = Column(String(128), nullable=False)
    else:
        @property
        def cities(self):
            """getter of cities instances"""
            from models import storage
            allCities = storage.all(City.__class__.__name__)

            cities_of_state = []

            for city in allCities:
                if city.state_id == self.id:
                    cities_of_state.add(city)
            return cities_of_state
        name = ''
