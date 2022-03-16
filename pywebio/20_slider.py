#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.input as inp
import pywebio.output as out


weight = inp.slider(label="Váha", value=75, min_value=30, max_value=150)

out.put_info("Váha")
out.put_text(weight)
