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

from box import Box

b = Box({0: "foo", 1: "bar", 2: "baz"})

print(b[0])
print(b[1])
print(b[2])

print(b.x0)
print(b.x1)
print(b.x2)
