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

from rich.tree import Tree
from rich import print


tree = Tree("Barvové modely")
rgb = tree.add("RGB")
cmyk = tree.add("CMYK")
yuv = tree.add("YUV")
hsl = tree.add("HSL")
hsv = tree.add("HSV")

rgb.add("Red")
rgb.add("Green")
rgb.add("Blue")

cmyk.add("Cyan")
cmyk.add("Magenta")
cmyk.add("Yellow")
cmyk.add("blacK")

hsl.add("Hue")
hsl.add("Saturation")
hsl.add("Lightness")

hsv.add("Hue")
hsv.add("Saturation")
hsv.add("Value")

print(tree)
