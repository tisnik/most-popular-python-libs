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

from toolz.itertoolz import pluck

phonebook = [
    {"id": 0, "name": "Alice", "phone": "555-1234"},
    {"id": 1, "name": "Bob", "phone": "555-5678"},
    {"id": 2, "name": "Charlie", "phone": "555-9999"},
]

print(list(pluck(["name", "phone"], phonebook)))
