#!/usr/bin/python3
"""Script takes a url and an email, and makes a post request
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    res = requests.post(url, data=data)
    print(res.text)
