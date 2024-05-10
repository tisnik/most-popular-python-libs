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

d1 = {"id": 1, "name": "Eda", "surname": "Wasserfall"}
d2 = {"foo": "F", "bar": "B", "baz": "Z"}

d = {**d1, **d2}

print(d)
