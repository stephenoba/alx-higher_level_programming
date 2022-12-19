#!/usr/bin/python3
""" script takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.exceptions import HTTPError

    url = 'https://api.github.com/repos/{}/{}/commits'
    headers = {
            'Authorization': 'Bearer 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',
            }
    repo = sys.argv[1]
    owner = sys.argv[2]

    try:
        url = url.format(repo, owner)
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        content = r.json()
    except (HTTPError, ValueError):
        print(None)
    else:
        for commit in content:
            output = "{}: {}"
            sha = commit["sha"]
            committer = commit["commit"]["committer"]["name"]
            print(output.format(sha, committer))
