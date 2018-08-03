#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/get"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# precteni hlavicek
headers = response.headers

# vypis typu internetoveho media
print(headers.get("content-type"))
