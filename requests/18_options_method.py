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
