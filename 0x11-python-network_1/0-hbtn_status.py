#!/usr/bin/python3
"""fetches http:??alx-intranet.hbtn.io"""

if __name__ == "__main":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as n:
        cont = n.read()
        print("Body response:")
        print("\t - type: {}".format(type(cont)))
        print("\t - content: {}".format(cont))
        print("\t - utf8 content: {}".format(content.decode('utf-8')))
