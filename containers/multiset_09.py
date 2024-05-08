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

m1 = Multiset(["a", "b", "c", "d"])
m2 = Multiset(["c", "d", "e", "f"])

print(m1)
print(m2)
print(m1 | m2)
print(m1 & m2)
print(m1 - m2)
print(m1 ^ m2)
