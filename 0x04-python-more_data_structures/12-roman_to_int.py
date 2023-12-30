#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            int_val += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            int_val += roman_dict[roman_string[i]]
    return int_val
