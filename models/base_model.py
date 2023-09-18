#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage

Base = declarative_base()

class BaseModel:
    """Definition of BaseModel class for common attributes
    or methods of other classes.

    Attributes:
        id (str): this attributes represents a column containing a unique
        string (60 characters). Attribute can't be null and is the primary key.
        created_at (datetime): this attribute represents a column containing
        a datetime. This attribute can't be null and the default value
        is the current datetime.
        updated_at (datetime): this attribute represents a column containing
        a datetime and it can't be null; default value is the current datetime.

    Args:
        None
    """

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This method converts instance into dictionary format"""
        dictionary_copy = dict(self.__dict__)
        dictionary_copy.pop("_sa_instance_state", None)
        dictionary_copy["created_at"] = self.created_at.isoformat()
        dictionary_copy["updated_at"] = self.updated_at.isoformat()
        return dictionary_copy

    def delete(self):
        """This method deletes the current instance from storage."""
        storage.delete(self)
