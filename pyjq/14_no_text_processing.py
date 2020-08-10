#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou pyjq

import pyjq

with open("openapi.json") as fin:
    content = fin.read()
    print(pyjq.compile(".openapi").all(content))
