#!/usr/bin/python3
# square.py
"""Defines a square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identity of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square. Both width and height are affected."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square. Both width and height
        are updated with the same value.
        """
        self.width = value
        self.height = value

