#!/usr/bin/python3
# 11-square.py - Defines a Rectangle subclass Square.

# Import the Rectangle class from 9-rectangle module.
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square.

    Args:
        size (int): The size of the new square.
    """
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
