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

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


console = Console()

panel1 = Panel("RGB\n\n[red]Red\n[green]Green\n[blue]Blue")
panel2 = Panel("CMYK\n\n[cyan]Cyan\n[magenta]Magenta\n[yellow]Yellow\n[black]blacK")
panel3 = Panel("YUV")
panel4 = Panel("HSL\n\nHue\nSaturation\nLightness")
panel5 = Panel("HSV\n\nHue\nSaturation\nValue")

columns = Columns([panel1, panel2, panel3, panel4, panel5])
console.print(columns)
