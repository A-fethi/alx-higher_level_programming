#!/usr/bin/python3
"""Python script that takes GitHub credentials,
and uses the GitHub API to display id"""
import requests
import sys


if __name__ == "__main__":
    name = sys.argv[1]
    passwd = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(name, passwd))
    data = r.json()
    print(data.get("id"))
