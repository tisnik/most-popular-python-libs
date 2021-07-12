"""Image viewer working in terminal."""

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

from PIL import Image
import blessed

# initialize terminal
terminal = blessed.Terminal()

# force terminal to use true colors if possible
terminal.number_of_colors = 1 << 24

# name of test image
filename = "fruits.png"

# load test image
img = Image.open(filename)

# display text image onto terminal
for j in range(0, img.height, 2):
    for i in range(img.width):
        red, green, blue = img.getpixel((i, j))
        print(f"{terminal.color_rgb(red, green, blue)}█", end="")
    print()

# end of image
print()
print(f"{terminal.normal}DONE")
