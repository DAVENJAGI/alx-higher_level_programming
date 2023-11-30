#!/usr/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
#Have to use curl

curl -s "$1" -X DELETE
