#!/usr/bin/python3
# 101-add_attribute.py
"""Defines a function to add custom attributes to objects."""


def add_attribute(obj, attr, value):
    """Add a new custom attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to obj.
        value (any): The value of attr.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute.")
    setattr(obj, attr, value)
