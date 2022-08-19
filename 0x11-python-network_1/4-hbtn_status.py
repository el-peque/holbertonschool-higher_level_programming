#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(r), r))
