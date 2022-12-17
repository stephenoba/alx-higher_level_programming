#!/usr/bin/python3
"""script takes a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        headers = res.info()
        print(headers['X-Request-Id'])
