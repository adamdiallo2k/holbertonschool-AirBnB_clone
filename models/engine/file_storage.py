#!/usr/bin/python3
"""FileStorage class"""
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {
         "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialize_obj = {}
        for key, obj in self.__objects.items():
            serialize_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialize_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for key, obj in objects.items():
                cls_name, obj_id = key.split(".")
                cls = self.__objects[cls_name]
                self.__objects[key] = cls(**obj)
        except FileNotFoundError:
            pass
