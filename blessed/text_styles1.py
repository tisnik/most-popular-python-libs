"""Changing text styles."""

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

# display text using different styles
print(terminal.normal + "normal text")
print(terminal.bold + "bold text" + terminal.normal)
print(terminal.underline + "underlined text" + terminal.normal)
print(terminal.reverse + "reversed text" + terminal.normal)
print()

print(
    terminal.bold
    + "bold "
    + terminal.underline
    + "and underlined "
    + terminal.normal
    + "text"
)
print()

print(
    terminal.underline
    + "underlined "
    + terminal.reverse
    + "and reversed "
    + terminal.normal
    + "text"
)
print()

print(
    terminal.reverse
    + "reversed "
    + terminal.bold
    + "and bold "
    + terminal.normal
    + "text"
)
