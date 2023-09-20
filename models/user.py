#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """
    Definition of the User class for the users table in
    the database.
    Args:
        BaseModel (class): the BaseModel class.
        Base (class): the declarative Base class from SQLAlchemy.
    """

    __tablename__ = 'users'
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
