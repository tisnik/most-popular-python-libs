#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou pyjq

import pyjq
import json

with open("openapi.json") as fin:
    content = json.load(fin)

    for endpoint in pyjq.compile('.paths[]').all(content):
        print(",".join(endpoint.keys()))

    print("-------------------------")

    for has_delete in pyjq.compile('.paths[] | has("delete")').all(content):
        print(has_delete)
