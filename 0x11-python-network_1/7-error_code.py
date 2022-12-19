#!/usr/bin/python3
"""Sript sends a request to the URL and displays the body of
the response. Takes note of http error responses
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code != 200:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
