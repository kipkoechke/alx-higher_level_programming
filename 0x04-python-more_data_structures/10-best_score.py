#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """
    Return the key with the highest integer value.

    Args:
        a_dictionary (dict): The dictionary to process.

    Returns:
        str: The key with the highest integer value.
    """
    # if a_dictionary:
    #     return max(a_dictionary, key=a_dictionary.get)
    # return None

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    return_key = list(a_dictionary.keys())[0]
    big_value = a_dictionary[return_key]
    for key, value in a_dictionary.items():
        if value > big_value:
            big_value = value
            return_key = key
    return return_key
