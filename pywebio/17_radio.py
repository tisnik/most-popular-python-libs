#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.input as inp
import pywebio.output as out


answer = inp.radio(label="test", options=["varianta 1", "varianta 2", "varianta 3"])

out.put_info("Odpověď")
out.put_text(answer)
