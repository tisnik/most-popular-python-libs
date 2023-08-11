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

from functools import wraps


def wrapper1(function):
    @wraps(function)
    def inner_function():
        print("-" * 40)
        function()
        print("-" * 40)

    return inner_function


def wrapper2(function):
    @wraps(function)
    def inner_function():
        print("=" * 40)
        function()
        print("=" * 40)

    return inner_function


@wrapper1
@wrapper2
def hello():
    print("Hello!")


hello()
print("function name:", hello.__name__)
