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

seznam = [1, 2, 3, 4]

print(seznam[0])
print(seznam[1])
print(seznam[-1])
print(seznam[-2])

seznam.append(5)
seznam.append(6)

seznam.insert(0, -10)
seznam.insert(0, -100)

print(seznam)

del seznam[0]
print(seznam)
del seznam[-1]
print(seznam)
