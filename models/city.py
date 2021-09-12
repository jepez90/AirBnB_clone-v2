#!/usr/bin/python3
""" City Module for HBNB project """
from re import S
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    if getenv("HBNB_TYPE_STORAGE") == 'db':

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities")

    else:
        state_id = ""
        name = ""

        @property
        def places(self):
            return []
        state = None
