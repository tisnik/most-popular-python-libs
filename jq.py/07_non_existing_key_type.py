#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)

    # klíč "non_existing_key" ve zdrojovém JSONu neexistuje
    print(type(jq.compile(".non_existing_key").input(content).first()))
