#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json
from pprint import pprint

with open("openapi.json") as fin:
    content = json.load(fin)
    search = jq.compile(".paths.\"/client/cluster/search\"").input(content).first()
    pprint(search)

    print("----------------------------------------------------------------------------")

    search = jq.compile('.paths."/client/cluster/search"').input(content).first()
    pprint(search)
