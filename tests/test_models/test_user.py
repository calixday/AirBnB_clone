#!/usr/bin/python3
"""Unittest module for the User Class."""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestUser(unittest.TestCase):

    """__Test Cases for the User class."""

    def setUp(self):
        """__Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_8_instantiation(self):
        """Tests instantiation of User class."""

        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_attributes(self):
        """__Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
