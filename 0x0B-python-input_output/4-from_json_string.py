#!/usr/bin/python3
"""This module defines a JSON-to-object function"""

import json


def from_json_string(my_str):
    """Converts a JSON string into a Python object representation"""
    return json.loads(my_str)
