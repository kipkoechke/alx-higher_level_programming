#!/usr/bin/python3
# 0-add_integer.py

"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
