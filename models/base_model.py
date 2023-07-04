#!/usr/bin/python3
"""commented module"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id} <{self.__dict__}>)'
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = datetime.isoformat(self.__dict__["updated_at"])
        self.__dict__["updated_at"] = datetime.isoformat(self.__dict__["updated_at"])
        return self.__dict__
