#!/usr/bin/python3
# 3-is_kind_of_class.py
"""
This script defines a function for checking if an object is an
 instance of a class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or a subclass instance
       of a specific class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare the object's type to.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
              False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
