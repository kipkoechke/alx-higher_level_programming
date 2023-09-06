#!/usr/bin/python3
"""
This module defines a function for printing names.
"""

def print_full_name(first, last=""):
    '''
    Print a full name in the format "First Last".

    Args:
        first (str): The first name.
        last (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If either first or last is not a string.

    Returns:
        None
    '''
    if not isinstance(first, str) or not isinstance(last, str):
        raise TypeError("Both first and last names must be strings.")

    full_name = f"{first} {last}".strip()
    print(f"My name is {full_name}")
