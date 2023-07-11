#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines all common
    attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Representation of the class for the user
        """
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """
        Update the updated_at attribute and save the object to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
