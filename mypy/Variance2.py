#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

from typing import List


class Ovoce:
    pass


class Hruska(Ovoce):
    def __repr__(self):
        return "Hruska"


class Jablko(Ovoce):
    def __repr__(self):
        return "Jablko"


def smichej(kosik : List[Ovoce]):
    kosik.append(Hruska())
    kosik.append(Jablko())


kosik : List[Hruska] = []

smichej(kosik)

for ovoce in kosik:
    print(ovoce)
