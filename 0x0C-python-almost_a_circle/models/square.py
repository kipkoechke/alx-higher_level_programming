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
        """Get the size of the Square. Both width and height are affected."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square. Both width and height
        are updated with the same value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Convert the Square attributes to a dictionary."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the string representation of a Square.

        Returns:
            str: A string containing Square information.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width,
        )
