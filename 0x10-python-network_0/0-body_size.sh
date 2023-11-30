#!/usr/bin/bash
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# $1 is the placeholder for the passed argument
# wc, used to count number of bytes in a file
# -c tells the wc to only count the number of bytes in a file
curl -s "$1" | wc -c
