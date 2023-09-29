#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge."""
import requests
import sys


if __name__ == "__main__":
    name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{name}/commits"
    r = requests.get(url)
    list_obj = r.json()
    i = 0
    try:
        while i < 10:
            sha = list_obj[i].get('sha')
            author = list_obj[i].get('commit').get('author').get('name')
            print(f"{sha}: {author}")
            i = i + 1
    except IndexError:
        pass
