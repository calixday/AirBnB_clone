#!/usr/bin/python3
"""AirBnB clone console Base  class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Base class model."""

    def __init__(self, *args, **kwargs):
        """this is just but the start of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Do Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        _my_dict = self.__dict__.copy()
        _my_dict["__class__"] = type(self).__name__
        _my_dict["created_at"] = _my_dict["created_at"].isoformat()
        _my_dict["updated_at"] = _my_dict["updated_at"].isoformat()
        return _my_dict
