#!/usr/bin/python3
"""
fetches http://alx-intranet.hbtn.io
 must use packageurllib
"""


if __name__ == "__main__":
    import requests

    hbtn = requests.get('https://alx-intranet.hbtn.io/status')
    cont = hbtn.text
    print("Body response:")
    print("\t- type: {}".format(type(cont)))
    print("\t- content: {}".format(cont))
