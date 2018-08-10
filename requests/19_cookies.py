#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests
import json

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/cookies"

# hlavicka posilana v dotazu
headers = {'accept': 'application/json'}

# priprava cookies
cookies = {'key1': 'value1',
           'key2': 'value2',
           'key3': 'value3'}

# poslani HTTP dotazu typu GET
response = requests.get(URL, headers=headers, cookies=cookies)

# precteni hlavicek
headers = response.headers

print("-" * 60)

# vypis vsech hlavicek
print("Headers:")

for header_name, header_value in headers.items():
    print("{:40s} {}".format(header_name, header_value))

print("-" * 60)

print("Content:")

# zpracovani odpovedi, ktera prisla ve formatu JSON
data = response.json()

print(json.dumps(data, indent=4, sort_keys=True))

print("-" * 60)

print("Cookies:")
print(response.cookies.get_dict())
