import json
import os
import importlib

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                cls_name = k.split('.')[0]
                if cls_name == "BaseModel":
                    from models.base_model import BaseModel
                    self.__objects[k] = BaseModel(**v)

