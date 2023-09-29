#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
