"""Display eight basic foreground colors with bold attribute."""

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

# print bold text onto terminal using selected foreground colors
print(f"{terminal.bold_black}black text{terminal.normal}")
print(f"{terminal.bold_red}red text{terminal.normal}")
print(f"{terminal.bold_green}green text{terminal.normal}")
print(f"{terminal.bold_yellow}yellow text{terminal.normal}")
print(f"{terminal.bold_blue}blue text{terminal.normal}")
print(f"{terminal.bold_magenta}magenta text{terminal.normal}")
print(f"{terminal.bold_cyan}cyan text{terminal.normal}")
print(f"{terminal.bold_white}white text{terminal.normal}")
