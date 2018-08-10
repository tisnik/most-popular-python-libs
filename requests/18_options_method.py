#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests
import json

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/get"

# hlavicka posilana v dotazu
headers = {'accept': 'application/json'}

# poslani HTTP dotazu typu OPTIONS
response = requests.options(URL, headers=headers)

# precteni hlavicek
headers = response.headers

# vypis vsech hlavicek
print("Headers:")

for header_name, header_value in headers.items():
    print("{:40s} {}".format(header_name, header_value))

print("-" * 60)

print("Content:")

# vypis tela odpovedi
print("Plain text:")
print("-" * 60)
print(response.text)
print("-" * 60)
