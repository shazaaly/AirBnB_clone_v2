#!/usr/bin/python3
"""This module to change storage type directly by
using an environment variable"""
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity

import os

storage = os.getenv('HBNB_TYPE_STORAGE')
if storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
