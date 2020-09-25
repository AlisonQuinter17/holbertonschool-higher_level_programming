#!/usr/bin/python3
"""This module has a function add 2 integers """


def add_integer(a, b=98):
    """
    Verify that a and b are integers or floats,
    otherwise generate a TypeError exception with
    a specific message
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    """
    Return the addition of the two given numbers.
    a: The first integer
    b: The second integer
    """
    return (int(a) + int(b))
