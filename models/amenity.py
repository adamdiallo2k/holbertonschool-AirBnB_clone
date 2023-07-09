<<<<<<< HEAD:models/Amenity.py
=======
#!/usr/bin/python3
"""Amenity class.
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
>>>>>>> 479ade809e06f69f76efa7ff2df8ea96891feb7f:models/amenity.py
