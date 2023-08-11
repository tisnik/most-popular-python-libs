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

def wrapper1(function):
    def inner_function():
        print("-" * 40)
        function()
        print("-" * 40)

    return inner_function


@wrapper1
def hello():
    print("Hello!")


hello()

print("function name:", hello.__name__)
