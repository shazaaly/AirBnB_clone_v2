#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Definition of the City class for the cities table in the
    database.

    Attributes:
        __tablename__ (str): this attribute represents the table
        name, "cities".
        name (str): this attribute represents a column containing a
        string (128 characters).This attribute can't be null.
        places (relationship): this attribute represents a relationship
        with the class Place. If the City object is deleted, all linked.
        Place objects must be automatically deleted. The reference from a Place
        object to its City should be named "cities"

    Args:
        BaseModel (class): the BaseModel class.
        Base (class): the declarative Base class from SQLAlchemy.
    """

    __tablename__ = 'cities'

    places = relationship('Place', back_populates='cities', cascade='all, delete-orphan')
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
