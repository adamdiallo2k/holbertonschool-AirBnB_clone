#!/usr/bin/python3
"""commented module"""
from models.base_model import BaseModel


class City(BaseModel):
    """commented class"""
    state_id = ""
    name = ""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.state_id = kwargs.get("state_id", "")
    #     self.name = kwargs.get("name", "")
