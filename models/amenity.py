#!/usr/bin/python3
"""Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.name = kwargs.get("name", "")

    # def __str__(self):
    #     return f"<Amenity name={self.name}>"

    # def update(self, name):
    #     self.name = name
