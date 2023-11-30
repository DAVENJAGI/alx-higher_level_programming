#!/usr/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept
#I tells that only the HTTP header should be displayed not actual response
#grep filters the output based on the specified pattern, ie, Allow within header
#last oart futher filters the output using the cut to extract second and subseq fields from each line. delimeter -d set to " " indicating fields are separated by spaces.

curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
