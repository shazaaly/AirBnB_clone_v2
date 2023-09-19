#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    Definition of the User class for the users table in
    the database.

    Attributes:
        __tablename__ (str): this attributes represents
        the table name, "users".
        email (str): attribute represents a column
        containing a string (128 characters).Attribute
        can't be null.
        password (str): attribute represents a column
        containing a string (128 characters).Attribute can't be null.
        first_name (str): attribute represents a column
        containing a string (128 characters). Attribute can be null.
        last_name (str): attribute represents a column
        containing a string (128 characters).Attribute can be null.
        places (relationship): this represents a relationship with the
        class Place. If the User object is deleted, all linked Place objects
        must be automatically deleted. The reference from a Place object
        to its User should be named "user".

    Args:
        BaseModel (class): the BaseModel class.
        Base (class): the declarative Base class from SQLAlchemy.
    """

     __tablename__ = 'users'

     email = Column(String(128), nullable=False)
     password = Column(String(128), nullable=False)
     first_name = Column(String(128), nullable=True)
     last_name = Column(String(128), nullable=True)
     places = relationship('Place', back_populates='user', cascade='all, delete-orphan')
