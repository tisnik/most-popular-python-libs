"""Display eight basic foreground colors."""

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

import blessed

# initialize terminal
terminal = blessed.Terminal()

# print text onto terminal using selected foreground colors
print(f"{terminal.black}black text{terminal.normal}")
print(f"{terminal.red}red text{terminal.normal}")
print(f"{terminal.green}green text{terminal.normal}")
print(f"{terminal.yellow}yellow text{terminal.normal}")
print(f"{terminal.blue}blue text{terminal.normal}")
print(f"{terminal.magenta}magenta text{terminal.normal}")
print(f"{terminal.cyan}cyan text{terminal.normal}")
print(f"{terminal.white}white text{terminal.normal}")
