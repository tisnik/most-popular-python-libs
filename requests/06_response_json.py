#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/get?x=6&y=7&answer=42"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# zpracovani odpovedi, ktera prisla ve formatu JSON
data = response.json()

print(data)

args = data["args"]
print(args)

print("x =", args["x"])
print("y =", args["y"])
print("answer =", args["answer"])
