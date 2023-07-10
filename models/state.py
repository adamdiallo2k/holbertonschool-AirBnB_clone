#!/usr/bin/python3
"""commented function"""
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """commented class"""
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
