#!/usr/bin/python3
"""FileStorage class"""
import json
<<<<<<< HEAD
import os
<<<<<<< Updated upstream

=======
import importlib
import pickle
>>>>>>> Stashed changes
=======
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
<<<<<<< HEAD
        """
        The `save` function saves the objects in a dictionary to a JSON file.
        """
        with open(self.__file_path, 'w') as f:
            pickle.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
=======
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)
>>>>>>> 479ade809e06f69f76efa7ff2df8ea96891feb7f

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        try:
<<<<<<< HEAD
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'rb') as f:
                    data = pickle.load(f)
                for k, v in data.items():
                    cls_name = k.split('.')[0]
                    if cls_name == "BaseModel":
                        from models.base_model import BaseModel
                        self.__objects[k] = BaseModel(**v)
=======
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for obj in objects.values():
                cls = obj['__class__']
                if cls in globals():
                    FileStorage.__objects[obj['id']] = globals()[cls](**obj)
>>>>>>> 479ade809e06f69f76efa7ff2df8ea96891feb7f
        except FileNotFoundError:
            pass
