#!/usr/bin/python3
"""Module for appends elements in a json file."""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""dump: crea un objeto usando un json y lo guarda en un archivo .txt"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""load: lee un archivo y los datos json los convierte en objeto."""

try:
    container = load_from_json_file('add_item.json')
except:
    container = []

for i in range(1, len(sys.argv)):
    container.append(sys.argv[i])
save_to_json_file(container, 'add_item.json')
