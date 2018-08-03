#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "https://httpbin.org/post"

payload = {
    "klic": "hodnota",
    "answer": 42,
    "question": None,
    "correct": True}

# poslani HTTP dotazu typu POST se specifikaci hodnot formulare
response = requests.post(URL, data=payload)

# vypis tela odpovedi v plain textu
print(response.text)
