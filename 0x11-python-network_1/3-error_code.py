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
        with urlopen(req) as res:
            content = res.read()
    except HTTPError as e:
        print(e.code)
    else:
        print(content.decode('UTF-8'))
