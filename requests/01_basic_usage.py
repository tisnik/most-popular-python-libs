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
