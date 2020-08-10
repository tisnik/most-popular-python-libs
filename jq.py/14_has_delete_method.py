#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)

    for endpoint in jq.compile('.paths[]').input(content).all():
        print(",".join(endpoint.keys()))

    print("-------------------------")

    for has_delete in jq.compile('.paths[] | has("delete")').input(content).all():
        print(has_delete)
