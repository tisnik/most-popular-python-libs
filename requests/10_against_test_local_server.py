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

# adresa lokalne beziciho serveru
URL = "http://localhost:8000"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# vypis zakladnich informaci ziskanych z odpovedi
print(response)
print(response.status_code)
print(response.ok)
print(response.text)

payload = {"klic": "hodnota", "answer": 42, "question": None, "correct": True}

# poslani dat jako hodnot formulare
response = requests.post(URL, data=payload)

print(response.text)

# poslani dat v tele dotazu
response = requests.post(URL, json=payload)

print(response.text)
