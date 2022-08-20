#!/usr/bin/python3
"""takes in a letter and send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        data = {'q': sys.argv[2]}
    else:
        data = {'q': ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
