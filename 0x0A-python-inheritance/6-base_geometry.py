#!/usr/bin/python3
# base_geometry.py
"""Defines a base geometry class, BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an exception for unimplemented area calculation."""
        raise Exception("area() is not implemented")
