"""Display eight basic background colors with bold attribute."""

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

print(f"{terminal.bold_on_black}black background{terminal.normal}")
print(f"{terminal.bold_on_red}red background{terminal.normal}")
print(f"{terminal.bold_on_green}green background{terminal.normal}")
print(f"{terminal.bold_on_yellow}yellow background{terminal.normal}")
print(f"{terminal.bold_on_blue}blue background{terminal.normal}")
print(f"{terminal.bold_on_magenta}magenta background{terminal.normal}")
print(f"{terminal.bold_on_cyan}cyan background{terminal.normal}")
print(f"{terminal.bold_on_white}white background{terminal.normal}")
