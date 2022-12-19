#!/usr/bin/python3
"""
Script fetches a response from a url
"""

if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\ttype: {}".format(type(res.text)))
    print("\tcontent: {}".format(res.text))
