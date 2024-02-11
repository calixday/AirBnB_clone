#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from datetime import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        f = Amenity()
        self.assertEqual(str(type(f)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(f, Amenity)
        self.assertTrue(issubclass(type(f), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
