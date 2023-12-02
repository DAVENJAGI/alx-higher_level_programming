#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    hbtn = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(hbtn.text)
