#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen


with urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print(f"Body response:\n\
\t- type: {type(data)}\n\
\t- content: {data}\n\
\t- utf8 content: {data.decode('utf8')}")
