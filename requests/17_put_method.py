#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests
import json

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/put"

# hlavicka posilana v dotazu
headers = {'accept': 'application/json'}

# poslani HTTP dotazu typu PUT
response = requests.put(URL, headers=headers)

# precteni hlavicek
headers = response.headers

# vypis vsech hlavicek
print("Headers:")

for header_name, header_value in headers.items():
    print("{:40s} {}".format(header_name, header_value))

print("-" * 60)

print("Content:")

# zpracovani odpovedi, ktera prisla ve formatu JSON
data = response.json()

print(json.dumps(data, indent=4, sort_keys=True))
