#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json
from pprint import pprint

with open("openapi.json") as fin:
    content = json.load(fin)

    for parameters in jq.compile('.paths."/client/cluster/search".get.parameters').input(content).all():
        pprint(parameters)
