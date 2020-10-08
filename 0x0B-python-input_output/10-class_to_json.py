#!/usr/bin/python3
"""Module for class_to_json function."""


def class_to_json(obj):
    """
    This function returns the dictionary
    description with simple data structure.
    """
    return vars(obj)
