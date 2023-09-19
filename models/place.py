#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import storage

class Place(BaseModel, Base):
    """
    The definition of the Place class for the places table in the database.

    Attributes:
        __tablename__ (str): this attribute represents the table name, "places".
        city_id (str): this attribute represents a column containing a string
        (60 characters). This attribute can't be null and is a foreign key to
        cities.id.
        user_id (str): this attribute represents a column containing a string
        (60 characters).This attribute can't be null and is a foreign key
        to users.id.
        name (str): This attribute represents a column containing a
        string (128 characters). This attribute can't be null.
        description (str): This attribute represents a column containing a
        string (1024 characters).This attribute can be null.
        number_rooms (int): this attribute represents a column containing
        an integer. This attribute can't be null and the default value is 0.
        number_bathrooms (int): this attribute represents a column containing an integer.
        The attribute can't be null and default value: 0.
        max_guest (int): This attributes represents a column containing
        an integer and it can't be null and default value: 0.
        price_by_night (int): this attribute represents a column containing
        an integer. The attribute can't be null and the default value: 0.
        latitude (float): this attribute represents a column containing
        a float; and the attribute can be null.
        longitude (float): the attribute represents a column containing
        a float. The attribute can be null.
        reviews (relationship): this attribute represents a relationship with
        the class Review. If the user object is deleted, all linked Review
        objects will be automatically deleted.
    Args:
        BaseModel (class): the BaseModel class.
        Base (class): the declarative Base class from SQLAlchemy.
    """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', back_populates='place', cascade='all,
            delete-orphan')
    amenity_ids = []

    if storage.TypeStorage == 'db':
        @property
        def reviews(self):
            """This method gets the attribute to return the list of Review
            instances with place_id equals to the current place.id for
            DBStorage.
            """
            reviews_list = []
            reviews_dict = storage.all(Review)
            for review in reviews_dict.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
