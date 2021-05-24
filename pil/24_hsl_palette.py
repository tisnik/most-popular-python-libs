#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2020  Pavel Tisnovsky
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
from PIL import ImageColor

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGB", (360, 200))

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # vykreslení různobarevných pixelů
    for saturation in range(0, height):
        for hue in range(0, width):
            color_hsl = "hsl({hue}, {saturation}%, 50%)".format(hue=hue, saturation=saturation/2)
            color = ImageColor.getrgb(color_hsl)
            test_image.putpixel((hue, saturation), color)

    # uložení upraveného obrázku
    test_image.save("hsl_palette.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
