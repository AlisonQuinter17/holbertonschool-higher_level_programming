#!/usr/bin/python3
"""Module for class_to_json function."""
import json


def class_to_json(obj):
    return vars(obj)
