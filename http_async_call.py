# For making Asynchronous HTTP requests, we are using
# 'grequests' library.

# Import necessary modules
import grequests


# Function to send request.
# @param url: url where request is to be sent.
# @param file: write header in file.
def makeRequests(url, file):
    reqs = [
        grequests.get(url),
        grequests.get(url),
        grequests.get(url),
    ]

    results = grequests.map(reqs)

    for result in results:
        file.write(result.headers['Date'] + '\n')


# main method
def main():
    url = 'https://webhook.site/0ce35f12-4cc7-4f73-af9f-149294648631'
    # Load output file in append mode.
    f = open('output.txt', 'a+')
    f.write('Making 3 Asynchronous requests . . .\n')

    makeRequests(url, f)

    f.write('\n')
    f.close()   # close file


if __name__ == '__main__':
    main()
