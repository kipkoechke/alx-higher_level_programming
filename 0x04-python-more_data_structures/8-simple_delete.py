#!/usr/bin/python3
# 8-simple_delete.py


def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
