#!/usr/bin/python3
"""Module for Student class."""


class Student():
    """The Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic_json = vars(self)
        if isinstance(attrs, list):
            nd = {}
            for key in dic_json:
                for i in attrs:
                    if key is i:
                        nd[key] = dic_json[key]
            return nd
        else:
            return dic_json
