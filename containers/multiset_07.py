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

from multiset import Multiset

m = Multiset({"foo": 0, "bar": 1, "baz": 2, "baf": 3})
print(m)

m.update(["foo"])
print(m)

m.update(["bar"])
print(m)
