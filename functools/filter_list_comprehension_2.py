#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

def odd(value):
    return value % 2 == 1


def even(value):
    return not odd(value)


data = range(0, 11)

filtered = [value for value in data if odd(value)]
print(filtered)

filtered = [value for value in data if even(value)]
print(filtered)
