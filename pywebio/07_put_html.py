#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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
