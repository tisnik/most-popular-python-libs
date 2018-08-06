#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/post"

# poslani HTTP dotazu typu POST
response = requests.post(URL)

# vypis odpovedi v plain textu
print(response.text)
