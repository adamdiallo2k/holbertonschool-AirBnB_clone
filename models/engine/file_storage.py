#!/usr/bin/python3
"""commented module"""
import json


class FileStorage:
    __file_path = ""
    __objects = {}

    def __init__(self, file_path, objects):
        __file__path = file_path
        __objects = objects
    
    def all(self):
        return self.__objects.__dict__()
    
    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{id(obj)}"] = obj
    
    def save(self):
            with open(self.__file_path, "w") as write_file:
                json.dump(self.__objects, write_file)
    
    def reload(self):
        if self.__file_path is not None:
             with open(self.__file_path, 'w') as read_file:
                 data = json.load(read_file)
        self.__objects = data