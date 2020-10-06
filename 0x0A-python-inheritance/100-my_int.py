#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    def __eq__(self, other):
        """If equals, inverting it."""
        return int(self) != int(other)

    def __ne__(self, other):
        """If not-equals, inverting it."""
        return int(self) == int(other)
