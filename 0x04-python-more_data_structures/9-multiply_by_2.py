#!/usr/bin/python3
# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary to process.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
