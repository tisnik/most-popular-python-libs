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

def sign(value):
    if value < 0:
        return "negative"
    elif value > 0:
        return "positive"
    else:
        return "zero"


values = range(-10, 11)

converted = map(sign, values)

for c in converted:
    print(c)
