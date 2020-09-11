#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

"""Chování jq při vzniku chyby, zachycení výjimky."""

import jq

with open("broken.json") as fin:
    content = fin.read()
    try:
        print(jq.compile(".openapi").input(text=content).all())
    except Exception as e:
        print(e)
