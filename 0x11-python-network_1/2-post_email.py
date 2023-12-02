#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    arguments = {'email': sys.argv[2]}
    data = parse.urlencode(arguments)
    data = data.encode('ascii')
    returned = request.Request(sys.argv[1], data)
    with request.urlopen(returned) as hbtn:
        bdy = hbtn.read()
        print(bdy.decode('utf-8'))
