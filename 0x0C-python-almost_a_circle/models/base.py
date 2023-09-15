#!/usr/bin/python3
# base.py
"""Defines a base model class."""


class Base:
    """Represents the base model.

    This class serves as the foundation for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The count of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The unique identifier for the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
