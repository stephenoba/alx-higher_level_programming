#!/usr/bin/python3
"""script takes a URL and an email, sends a POST
request to the passed URL with the email as a
parameter, and displays the body of the response
(decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print(content.decode('UTF-8'))
