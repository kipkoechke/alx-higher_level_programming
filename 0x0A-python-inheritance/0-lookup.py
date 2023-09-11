#!/usr/bin/python3
"""
0-lookup.py

This module defines the `lookup` function.
"""


def lookup(obj):
    """
    Return a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of attribute and method names.

    Example:
        >>> lookup([])
        ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
         '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
         '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__',
         '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
         '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
         'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
         'reverse', 'sort']
    """
    return dir(obj)

if __name__ == "__main__":
    # Example usage when run as a standalone script
    print(lookup([]))
