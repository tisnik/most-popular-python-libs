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

panel1 = Panel("První")
panel2 = Panel("Druhý")
panel3 = Panel("Třetí")

columns = Columns([panel1, panel2, panel3])
console.print(columns)
