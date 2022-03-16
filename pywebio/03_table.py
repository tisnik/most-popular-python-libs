#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out


values = [(x, 1.0/x) for x in range(1, 20)]

out.put_table(values)
