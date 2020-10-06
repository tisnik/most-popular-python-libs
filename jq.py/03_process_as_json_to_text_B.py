#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

"""Zpracovnání vstupu ve formě JSONu (předparsování vstupu)."""

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    value = jq.compile(".security").input(content).text()
    print(value)
    print(type(value))
