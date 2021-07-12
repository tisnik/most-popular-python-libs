"""24-bit palette in terminal - specifying foreground color."""

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

# force terminal to use 24bit colors if possible
terminal.number_of_colors = 1 << 24

# subset from the whole color space
for red in range(0, 256, 16):
    for green in range(0, 256, 16):
        for blue in range(0, 256, 16):
            # display text using selected foreground color
            hex_triplet = "#{:02x}{:02x}{:02x}".format(red, green, blue)
            print(terminal.color_rgb(red, green, blue) + hex_triplet, end=" ")
        print()
    print()

print()
print(f"{terminal.normal}DONE")
