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

from funcy import decorator


@decorator
def wrapper1(function):
    print("-" * 40)
    function()
    print("-" * 40)


@decorator
def wrapper2(function):
    print("=" * 40)
    function()
    print("=" * 40)


@wrapper1
@wrapper2
def hello():
    print("Hello!")


hello()
