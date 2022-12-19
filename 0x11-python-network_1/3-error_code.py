#!/usr/bin/python3
"""script takes a URL, sends a request to the URL
and displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]
    req = Request(url)
    try:
        res = urlopen(req)
    except HTTPError as e:
        print(e.code)
    else:
        content = res.read()
        print(content.decode('UTF-8'))
