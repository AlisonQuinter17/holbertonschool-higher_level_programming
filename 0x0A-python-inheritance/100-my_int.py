#!/usr/bin/python3
"""Module for MyInt subclass."""


class MyInt(int):
    def __eq__(self, other):
        return int(self) is not int(other)

    def __ne__(self, other):
        return int(self) is int(other)
