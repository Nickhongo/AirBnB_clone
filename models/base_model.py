#!/usr/bin/python3
"""
Module contains the BaseModel class:
    BaseModel - defining all comm attr and methods for other classes

This module links BaseModel to FileStoragr

"""

import datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    Def a BaseModel class

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all BaseModel instance attr
        """
        if args:
            raise TypeError("args should not be used")
        if kwargs:
            for key, value in kwargs.items():
                for key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self.__class__, key, value)
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __setatrr__(self, name, value):
        """
        update dynamic att in self.__dict__
        """
        self.__dict__[name] = value
        self.__dict__["updated_at"] = datetime.now()
        storage.new(self)

    def __str__(self):
        """
        Return unoff str represantation
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id
                self.__dict__
                )

    def save(self):
        """
        Update updated_at with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary
        """
        inst_dict = {}
        for key, value in self.__dict__items():
            inst_dict[key] = value.isoformat()
        else:
            inst_dict[key] = value
        inst_dict["__class__"] = self.__class__.name__
        return inst_dict
