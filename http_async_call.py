# For Asynchronous calls we are creating 3 threads
# which will then make 3 requests without waiting for earlier one to finish
# We wait for threads to finish before exiting.

# Import necessary modules
import threading, time
import requests


# Sends requests to the URL and
# appends Date header to the list
def makeRequest(dates):
    r = requests.get('https://webhook.site/0ce35f12-4cc7-4f73-af9f-149294648631')
    dates.append(r.headers['Date'])
    

# Load output file in append mode.
f = open('output.txt', 'a+')
f.write('Makeing 3 Asynchronous requests . . .\n')

dates = []

for i in range(3):
    t = threading.Thread(target = makeRequest, args = (dates,))
    t.start()

# Wait until all other threads are finished
while threading.active_count() > 1:
    continue

for date in dates:
    f.write(date + '\n')

f.write('\n')
f.close()