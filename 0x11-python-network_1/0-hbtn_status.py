#!/usr/bin/python3
"""
fetches http://alx-intranet.hbtn.io
 must use packageurllib
"""


if __name__ == "__main":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as hbtn:
        cont = hbtn.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode('utf-8')))
