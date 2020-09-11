#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#  Demonstrační příklad k článku:
#      Zpracování dat uložených ve formátu JSON knihovnou jq.py

"""Zpracovnání vstupu ve formě textu s interním parsingem JSONu."""
import jq

with open("openapi.json") as fin:
    content = fin.read()
    print(jq.compile(".openapi").input(text=content).all())
