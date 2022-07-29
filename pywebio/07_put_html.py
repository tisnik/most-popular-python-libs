#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pywebio.output as out


html = """
<h1>Header</h1>

<table>
  <tr>
    <td style='background:#ff8080'>Cell</td>
    <td style='background:#ffff80'>Cell</td>
  </tr>
</table>
"""

out.put_html(html)
