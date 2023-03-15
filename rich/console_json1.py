#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from rich.console import Console

console = Console()


def perform_computation(x, y):
    dictionary = {}
    dictionary["x"] = x
    dictionary["y"] = y

    try:
        z = x / y
        dictionary["result"] = z
        dictionary["success"] = True
    except Exception as e:
        dictionary["success"] = False
        dictionary["errors"] = e

    console.print_json(data=dictionary)
    return dictionary


perform_computation(1, 2)
perform_computation(1, 0)
