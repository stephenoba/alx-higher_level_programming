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
    repo = sys.argv[1]
    owner = sys.argv[2]

    try:
        url = url.format(owner, repo)
        r = requests.get(url)
        r.raise_for_status()
        content = r.json()
    except (HTTPError, ValueError) as e:
        pass
    else:
        for commit in content:
            output = "{}: {}"
            sha = commit["sha"]
            committer = commit["commit"]["author"]["name"]
            print(output.format(sha, committer))
