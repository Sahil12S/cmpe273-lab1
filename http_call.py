# Import necessary modules
import requests


# Makes 'count' request to the given URL and
# writes Date header to the file.
def makeRequest(count, file):
    for i in range(count):
        r = requests.get('https://webhook.site/0ce35f12-4cc7-4f73-af9f-149294648631')
        date = r.headers['Date']
        file.write(date + '\n')


# Load file in Append mode
f = open('output.txt', 'a+')
f.write('Makeing 3 Synchronous requests . . .\n')

makeRequest(3, f)

f.write('\n')
f.close()