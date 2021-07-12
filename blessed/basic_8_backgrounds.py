"""Display eight basic background colors."""

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

# print text onto terminal using selected background colors
print(f"{terminal.on_black}black background{terminal.normal}")
print(f"{terminal.on_red}red background{terminal.normal}")
print(f"{terminal.on_green}green background{terminal.normal}")
print(f"{terminal.on_yellow}yellow background{terminal.normal}")
print(f"{terminal.on_blue}blue background{terminal.normal}")
print(f"{terminal.on_magenta}magenta background{terminal.normal}")
print(f"{terminal.on_cyan}cyan background{terminal.normal}")
print(f"{terminal.on_white}white background{terminal.normal}")
