import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    def setUp(self):
        """Set up for the tests."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down for the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        instance = BaseModel()
        self.storage.new(instance)
        self.assertIn("BaseModel." + instance.id, self.storage.all())

    def test_save(self):
        """Test the save method."""
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        with open("file.json", 'r') as f:
            self.assertIn("BaseModel." + instance.id, f.read())

    def test_reload(self):
        """Test the reload method."""
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + instance.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()
