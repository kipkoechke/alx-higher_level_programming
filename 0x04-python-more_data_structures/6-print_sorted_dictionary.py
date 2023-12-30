#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """
    Return a string representation of a dictionary sorted by keys.

    Args:
        a_dictionary (dict): The dictionary to sort.

    Returns:
        str: A string representation of the sorted dictionary.
    """
    [print(f"{k}: {a_dictionary[k]}") for k in sorted(a_dictionary)]
