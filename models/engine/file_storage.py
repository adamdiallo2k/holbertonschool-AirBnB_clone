#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import path


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialize_obj = {}
        for key, obj in self.__objects.items():
            serialize_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(serialize_obj))

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists
        """
        try:
            if path.exists(self.__file_path):
                with open(self.__file_path, mode='r', encoding='utf-8') as f:
                    json_dict = json.loads(f.read())
                    for k, v in json_dict.items():
                        self.__objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass
