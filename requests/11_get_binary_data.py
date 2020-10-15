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
