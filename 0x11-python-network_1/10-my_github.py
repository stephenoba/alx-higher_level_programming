#!/usr/bin/python3
""" script takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.exceptions import HTTPError

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    try:
        r = requests.get(url, auth=(username, password))
        r.raise_for_status()
        content = r.json()
    except (HTTPError, ValueError):
        print(None)
    else:
        print(content['id'])
