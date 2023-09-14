#!/usr/bin/python3
# 100-my_int.py
"""Defines a custom integer class MyInt, inheriting from int."""


class MyInt(int):
    """Custom integer class that inverts int operators == and !=."""

    def __eq__(self, value):
        """Override the == operator to behave like !=."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator to behave like ==."""
        return self.real == value
