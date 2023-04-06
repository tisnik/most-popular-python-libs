#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#


class Context:
    def __init__(self):
        print("Context: init")

    def __enter__(self):
        print("Context: enter")
        return "foo"

    def __exit__(self, type, value, traceback):
        print("Context: exit", type, value, traceback)


print("Before with block")

with Context() as c:
    print("Inside with block")
    print(c)

print("After with block")
