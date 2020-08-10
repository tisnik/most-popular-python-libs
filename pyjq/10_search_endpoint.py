#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou pyjq

import pyjq
import json
from pprint import pprint

with open("openapi.json") as fin:
    content = json.load(fin)
    search = pyjq.compile(".paths.\"/client/cluster/search\"").first(content)
    pprint(search)

    print("----------------------------------------------------------------------------")

    search = pyjq.compile('.paths."/client/cluster/search"').first(content)
    pprint(search)
