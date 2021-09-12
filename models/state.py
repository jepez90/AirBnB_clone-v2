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
        cities = relationship("City", back_populates="state")
        name = Column(String(128), nullable=False)
    else:
        @property
        def cities(self):
            """getter of cities instances"""
            from models import storage
            allCities = storage.all(City)

            cities_of_state = []

            for city_id, city in allCities.items():
                if city.state_id == self.id:
                    cities_of_state.append(city)
            return cities_of_state
        name = ''
