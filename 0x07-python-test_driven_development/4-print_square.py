#!/usr/bin/python3
# 4-print_square.py
"""Defines a function to print a square pattern."""


def print_square(size):
    """Prints a square pattern using the '#' character.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be greater than or equal to 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
