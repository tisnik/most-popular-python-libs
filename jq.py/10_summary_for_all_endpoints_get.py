#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    summaries = jq.compile(".paths[] | .get.summary").input(content).all()
    for summary in summaries:
        print(summary)
