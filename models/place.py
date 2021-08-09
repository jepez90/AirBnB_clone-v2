#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ColumnDefault
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, ColumnDefault(0), nullable=False)
    number_bathrooms = Column(Integer, ColumnDefault(0), nullable=False)
    max_guest = Column(Integer,  ColumnDefault(0), nullable=False)
    price_by_night = Column(Integer,  ColumnDefault(0), nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
