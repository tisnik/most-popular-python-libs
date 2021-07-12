"""Display all combinations of eight basic foreground and background colors."""

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

# text foreground colors
textColors = (
        terminal.black,
        terminal.red,
        terminal.green,
        terminal.yellow,
        terminal.blue,
        terminal.magenta,
        terminal.cyan,
        terminal.white,
)

# text background colors
backgroundColors = (
        terminal.on_black,
        terminal.on_red,
        terminal.on_green,
        terminal.on_yellow,
        terminal.on_blue,
        terminal.on_magenta,
        terminal.on_cyan,
        terminal.on_white,
)

# use all combinations of foreground and background colors
for textColor in textColors:
    for backgroundColor in backgroundColors:
        print(f"{textColor}{backgroundColor}XXXXX{terminal.normal} ", end="")
    # next line
    print()
