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

from multidict import MultiDict

d = MultiDict({str(x): x*2 for x in range(10) if x%3 != 0})

for i in range(10):
    d.add(str(i), "foo")
    d.add(str(i), "bar")

print(d)
print()

keys = sorted(d.keys())
print(keys)
print()

for key in keys:
    print(key, d.getone(key))
