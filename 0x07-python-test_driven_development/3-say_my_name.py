#!/usr/bin/python3
"""This module contain matrix_divided method."""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: It´s a list of lists of integers or floats.
        last_name: Number by which the matrix will be divided.

    Raise:
        - TypeError if matrix are not integers or floats.

    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print ("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
