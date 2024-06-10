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

from toolz.itertoolz import get

phonebook = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}

print(get("Bob", phonebook))
print(get(["Alice", "Bob"], phonebook))
print(get("Zdenek", phonebook, "unknown"))
print(get("Zdenek", phonebook))
