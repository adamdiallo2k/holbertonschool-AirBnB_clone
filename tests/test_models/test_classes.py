#!/usr/bin/python3
"""Test class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testamenity(unittest.TestCase):
    """
    unit test for amenity class
    """
    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        """
        Tests if class inherits from BaseModel.
        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))


class Testcity(unittest.TestCase):
    """
    Unittests for the City class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

class Testplace(unittest.TestCase):
    """
    Unittests for the Place class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))

class Testreview(unittest.TestCase):
    """
    Unittests for the Review class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

class Teststate(unittest.TestCase):
    """
    Unittests for the State class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

if __name__ == "__main__":
    unittest.main()