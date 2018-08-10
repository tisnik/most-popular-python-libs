#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "http://localhost:8000"

# hlavicka posilana v dotazu
headers = {'accept': 'application/json',
           'Set-Cookie': "x=y"}

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
data = response.text

print(data)

print("-" * 60)

print("Cookies:")
print(response.cookies.get_dict())
