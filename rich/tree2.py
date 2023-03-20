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
tree.add("RGB").add("Red Green Blue")
tree.add("CMYK").add("Cyan Magenta Yellow blacK")
tree.add("YUV").add("Luminance Chrominance")
tree.add("HSL").add("Hue Saturation Lightness")
tree.add("HSV").add("Hue Saturation Value")

print(tree)
