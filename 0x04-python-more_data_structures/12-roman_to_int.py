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
        current = roman_dict[roman_string[i]]
        previous = roman_dict[roman_string[i - 1]] if i > 0 else 0
        if i > 0 and current > previous:
            int_val += current - 2 * previous
        else:
            int_val += current
    return int_val
