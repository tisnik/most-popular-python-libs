#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    print("-----------------------------")
    print(jq.compile('.paths."/"').input(content).first())
    print("-----------------------------")
    print(jq.compile('".paths./"').input(content).first())
    print("-----------------------------")
    print(jq.compile('.paths./').input(content).first())
