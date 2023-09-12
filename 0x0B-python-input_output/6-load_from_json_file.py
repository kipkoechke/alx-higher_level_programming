#!/usr/bin/python3
"""Reads and loads data from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
