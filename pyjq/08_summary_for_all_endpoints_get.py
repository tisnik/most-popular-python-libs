#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou pyjq

import pyjq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    summaries = pyjq.compile(".paths[] | .get.summary").all(content)
    for summary in summaries:
        print(summary)
