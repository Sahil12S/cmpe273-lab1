# For Asynchronous calls we are creating 3 threads
# which will then make 3 requests without waiting for earlier one to finish
# We wait for threads to finish before exiting.

# Import necessary modules
import grequests

# Function to send request.
def makeRequests(url, file):
    reqs = [
        grequests.get(url),
        grequests.get(url),
        grequests.get(url),
    ]

    results = grequests.map(reqs)

    for result in results:
        file.write(result.headers['Date'] + '\n')


def main():
    url = 'https://webhook.site/0ce35f12-4cc7-4f73-af9f-149294648631'
    # Load output file in append mode.
    f = open('output.txt', 'a+')
    f.write('Makeing 3 Asynchronous requests . . .\n')

    makeRequests(url, f)

    f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
