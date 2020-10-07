#!/usr/bin/python3
"""Module for add_attribute method."""


def add_attribute(obj, key, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
