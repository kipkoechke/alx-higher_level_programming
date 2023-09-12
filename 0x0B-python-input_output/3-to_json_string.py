#!/usr/bin/python3
"""This script defines a JSON string conversion function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)
