#!/usr/bin/python3
"""list 10 commits (from most recent to oldest) of the repository “rails” by
the user “rails”"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits?\
per_page=10".format(sys.argv[2], sys.argv[1]))
    data = r.json()
    for i in data:
        print("{}: {}".format(i["sha"], i["commit"]["author"]["name"]))
