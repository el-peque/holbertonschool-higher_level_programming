#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen
with urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print(f"Body response:\n\
    - type: {type(data)}\n\
    - content: {data}\n\
    - utf8 content: {data.decode('utf8')}")
