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
from rich.table import Table

table = Table(title="Barvové modely")

table.add_column("Zkratka")
table.add_column("Význam")
table.add_column("Komponenty")

table.add_row("RGB", "Red Green Blue", "[red]Red [green]Green [blue]Blue")
table.add_row(
    "CMYK",
    "Cyan Magenta Yellow blacK",
    "[cyan]Cyan [magenta]Magenta [yellow]Yellow [black]blacK",
)
table.add_row("HSL", "Hue Saturation Lightness", "")
table.add_row("HSV", "Hue Saturation Value", "")

console = Console()
console.print(table)
