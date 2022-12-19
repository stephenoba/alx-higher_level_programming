#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import sys
    import requests

    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    res = requests.post(url, data=data)
    try:
        content = res.json()
        if not content:
            print("No result")
        else:
            output = "[{}] {}"
            print(output.format(content["id"], content["name"]))
    except ValueError as e:
        print("Not a valid JSON")
