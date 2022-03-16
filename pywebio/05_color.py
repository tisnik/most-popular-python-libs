#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out


for color in ('primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'):
    out.put_text(color, color)
    out.put_loading(shape='border', color=color)
