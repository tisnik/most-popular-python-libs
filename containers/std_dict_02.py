#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

d = {"id": 1, "name": "Eda", "surname": "Wasserfall"}

print(d)

print(d["name"])

d["hra"] = "Svestka"

print(d)

del d["id"]

print(d)
