#!/usr/bin/python
# vim: set fileencoding=utf-8

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

def perform_command():
    response = input("> ")

    match response:
        case "quit":
            return "Quit"
        case "list employees":
            return "List employees"
        case "list departments":
            return "List departments"
        case "list rooms":
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
