#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/get"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# vypis objektu, ktery se vrati
print(response)



# nyni vyzkousime neexistujici endpoint:

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/neexistuje"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# vypis objektu, ktery se vrati
print(response)
