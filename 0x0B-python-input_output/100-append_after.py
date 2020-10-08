#!/usr/bin/python3
"""Module for append_filename function."""


def append_after(filename="", search_string="", new_string=""):
    """This function search and inserts a line of text to a file."""
    with open(filename, "r", encoding="utf-8") as f:
        container = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for x in container:
            f.write(x)
            if x.count(search_string) != 0:
                f.write(new_string)
