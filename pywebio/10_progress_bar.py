#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out
import time


out.put_processbar("bar")

for i in range(1, 11):
    out.set_processbar("bar", i / 10)
    time.sleep(0.1)
