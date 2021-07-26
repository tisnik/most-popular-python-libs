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
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageMorph

# jméno zdrojového testovacího rastrového obrázku
filename = "Lenna.png"


try:
    # vytvoření prázdného obrázku
    test_image = Image.new("L", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # načtení fontu
    font = ImageFont.truetype('FreeMono.ttf', 100)

    # vykreslení jednoduchého textu
    draw.text((70, height/2 - 50), "Pillow", font=font, fill=255)

    patterns = ["4:(... .1. .0.)->0"]
    lutBuilder = ImageMorph.LutBuilder(patterns=patterns)

    # vytvoření objektu pro morfologické operace
    lut = lutBuilder.build_lut()
    morphOp = ImageMorph.MorphOp(lut=lut)

    # aplikace morfologické operace
    pixels, eroded_image = morphOp.apply(test_image)
    print(pixels)

    # aplikace morfologické operace
    pixels, more_eroded_image = morphOp.apply(eroded_image)
    print(pixels)

    # zobrazení původního i upraveného obrázku
    test_image.show()
    eroded_image.show()
    more_eroded_image.show()

    # uložení původního i upraveného obrázku
    test_image.save("47_bitmap.png")
    eroded_image.save("47_eroded.png")
    more_eroded_image.save("47_eroded_2.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
