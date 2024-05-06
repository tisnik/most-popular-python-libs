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

from json import load

from box import Box

with open("openapi.json") as fin:
    j = load(fin)

print(j)
print()

b = Box(j, box_dots=True)

print(b["info"]["license"]["name"])
print(b.info.license.name)
print(b["info.license.name"])
