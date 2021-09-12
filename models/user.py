#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
    else:
        @property
        def places(self):
            """getter of cities instances"""
            from models import storage
            from models.place import Place
            allPlaces = storage.all(Place)

            places_of_user = []

            for place_id, place in allPlaces.items():
                if place.user_id== self.id:
                    places_of_user.append(place)
            return places_of_user

        @property
        def reviews(self):
            """getter of cities instances"""
            from models import storage
            from models.review import Review
            allReviews = storage.all(Review)

            reviews_of_user = []

            for review_id, review in allReviews.items():
                if review.user_id == self.id:
                    reviews_of_user.append(review)
            return reviews_of_user
