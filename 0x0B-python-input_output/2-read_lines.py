#!/usr/bin/python3
"""Module for read_lines function."""


def read_lines(filename="", nb_lines=0):
    """This function reads n lines of a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.readlines(), end="")

        else:
            x = 0
            for i in f:
                x = x + 1
                if x <= nb_lines:
                    print(i, end="")
