#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a function to check object class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with the type of obj.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
