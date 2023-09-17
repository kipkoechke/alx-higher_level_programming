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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries to JSON.

        Args:
            list_dictionaries (list): A list of dictionaries.
            
        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write a list of objects as JSON data to a file.

        Args:
            list_objs (list): A list of instances derived from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

