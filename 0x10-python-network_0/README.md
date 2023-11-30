Pyhon Networking.
----------------------------------
Task 1
------
script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
$1 is the placeholder for the passed argument
wc, used to count number of bytes in a file
-c tells the wc to only count the number of bytes in a file

Task 2
------
Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
Display only a body of a 200 status code response.

Task 3
------
#Bash script that takes in a URL and displays all HTTP methods the server will accept
#I tells that only the HTTP header should be displayed not actual response
#grep filters the output based on the specified pattern, ie, Allow within header
#last oart futher filters the output using the cut to extract second and subseq fields from each line. delimeter -d set to " " indicating fields are separated by spaces.

Task 4
------
Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
Have to use curl

Task 5
------
Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

Task 6
------
Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
