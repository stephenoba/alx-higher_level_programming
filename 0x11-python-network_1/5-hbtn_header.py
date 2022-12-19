#!/usr/bin/python3
"""Script gget the 'X-Request-Id' for response header
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)
    try:
        print(res.headers["X-Request-Id"])
    except Exception:
        pass
