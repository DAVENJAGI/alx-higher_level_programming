#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    hbtn = requests.get(sys.argv[1])
    if hbtn.status_code >= 400:
        print('Error code: {}'.format(hbtn.status_code))
    else:
        print(hbtn.text)
