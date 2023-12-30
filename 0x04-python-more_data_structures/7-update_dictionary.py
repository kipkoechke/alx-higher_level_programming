#!/usr/bin/python3
# 7-update_dictionary.py


def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to add or replace.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
