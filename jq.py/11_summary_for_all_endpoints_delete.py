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

import json

import jq

with open("openapi.json") as fin:
    content = json.load(fin)
    summaries = jq.compile(".paths[] | .delete.summary").input(content).all()
    for summary in summaries:
        print(summary)
