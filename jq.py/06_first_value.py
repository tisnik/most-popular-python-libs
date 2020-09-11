#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

"""Přečtení první hodnoty ze získané sekvence."""

import jq
import json

with open("openapi.json") as fin:
    content = json.load(fin)
    print(jq.compile(".openapi").input(content).first())
    print(jq.compile(".info.description").input(content).first())
    print(jq.compile(".tags").input(content).first())
