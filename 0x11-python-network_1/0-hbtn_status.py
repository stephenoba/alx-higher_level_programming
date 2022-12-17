#!/usr/bin/python3
"""script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as r:
        content = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('UTF-8')))
