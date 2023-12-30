#!/usr/bin/env python3
# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary to process.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    return {k: a_dictionary[k] * 2 for k in a_dictionary}


a_dictionary = {"John": 12, "Alex": 8, "Bob": 14, "Mike": 14, "Molly": 16}
print_sorted_dictionary = __import__(
    "6-print_sorted_dictionary"
).print_sorted_dictionary
print_sorted_dictionary(a_dictionary)
