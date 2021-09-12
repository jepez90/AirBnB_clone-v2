#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.review import Review
from os import getenv
from re import S
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ColumnDefault, Table
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False),
                      Column('amenity_id', String(60,),
                             ForeignKey('amenities.id'), nullable=False))


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
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities")
    else:
        user = ''
        cities = []

        @property
        def reviews(self):
            """getter of reviews instances """
            from models import storage
            allReviews = storage.all(Review)

            reviews_of_place = []

            for rwview_id, review in allReviews.items():
                if review.place_id == self.id:
                    reviews_of_place.append(review)
            return reviews_of_place

        @property
        def amenities(self):
            """getter of amenity instances """
            from models import storage
            allAmenities = storage.all(Amenity)

            amenities_of_place = []

            for amenity_id, amenity in allAmenities.items():
                if amenity.id in self.amenity_ids:
                    amenities_of_place.append(amenity)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """setter of amenity instances """
            if isinstance(value, Amenity):
                self.amenity_ids.append(Amenity.id)
