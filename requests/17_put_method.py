#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import json

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/put"

# hlavicka posilana v dotazu
headers = {"accept": "application/json"}

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
