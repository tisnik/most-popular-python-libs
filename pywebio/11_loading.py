#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out

import time


with out.put_loading(shape='border', color='primary'):
    time.sleep(5)
    out.put_text("Done")
