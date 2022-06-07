#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out

import time


i = 0

for color in (
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
):
    with out.put_loading(shape="border", color=color):
        time.sleep(1)
        out.put_text(i)
        i += 1

out.put_text("Done")
