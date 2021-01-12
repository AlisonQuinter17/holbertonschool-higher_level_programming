#!/usr/bin/python3
"""Error codes."""
import requests
import sys

if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])
        print(response)
    except requests.HTTPError as error:
        print("Error code:", error.code)
