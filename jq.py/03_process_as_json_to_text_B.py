#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    value = jq.compile(".security").input(content).text()
    print(value)
    print(type(value))
