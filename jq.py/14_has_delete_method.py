#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2020  Pavel Tisnovsky
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

"""Ukázka dotazovacího jazyka použitého v nástroji jq."""

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)

    for endpoint in jq.compile(".paths[]").input(content).all():
        print(",".join(endpoint.keys()))

    print("-------------------------")

    for has_delete in jq.compile('.paths[] | has("delete")').input(content).all():
        print(has_delete)
