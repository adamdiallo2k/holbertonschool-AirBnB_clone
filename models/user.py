#!/usr/bin/python3
"""inherite the basemodel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """commented class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.email = kwargs.get("email", "")
    #     self.password = kwargs.get("password", "")
    #     self.first_name = kwargs.get("first_name", "")
    #     self.last_name = kwargs.get("last_name", "")
