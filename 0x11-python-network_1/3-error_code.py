#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import urllib.error, urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as hbtn:
            data = hbtn.read()
            print(data)

    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
