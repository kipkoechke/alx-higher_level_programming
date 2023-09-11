#!/usr/bin/python3
"""
    This script returns a list of an object's attributes and methods.
"""


def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    return list(dir(obj))
