#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/bytes/100"

# poslani HTTP dotazu typu GET
response = requests.get(URL, stream=True)

# precteni hlavicek
headers = response.headers

# vypis typu internetoveho media
print("Typ dat:", headers.get("content-type"))

# vypis delky dat predanych v tele
print("Delka dat:", headers.get("content-length"))

length = int(headers.get("content-length"))

# precteni tela bajt po bajtu
for i in range(length):
    byte = response.raw.read(1)
    print(hex(byte[0]))
