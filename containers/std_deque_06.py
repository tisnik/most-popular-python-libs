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

from collections import deque

d = deque(["a", "b", "c"])
print(d)

d.insert(1, "bar")
print(d)

d.insert(3, "baz")
print(d)
