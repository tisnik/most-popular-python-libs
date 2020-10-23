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
from PIL import ImageMath
from PIL import ImageMorph

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

    # parametry filtru realizujícího morfologické operace
    patterns = ['4:(... .0. .1.)->1',
                '4:(... .0. ..1)->1']
    # vytvoření objektu pro morfologické operace
    lutBuilder = ImageMorph.LutBuilder(patterns=patterns)
    lut = lutBuilder.build_lut()
    morphOp = ImageMorph.MorphOp(lut=lut)

    # aplikace morfologické operace dilatace na původní testovací obrázek
    pixels, dilated_image = morphOp.apply(test_image)
    print(pixels)

    # aplikace morfologické operace dilatace na již upravený rastrový obrázek
    pixels, more_dilated_image = morphOp.apply(dilated_image)
    print(pixels)

    # zobrazení původního i upraveného obrázku
    test_image.show()
    dilated_image.show()
    more_dilated_image.show()

    # uložení původního i upraveného obrázku
    test_image.save("46_bitmap.png")
    dilated_image.save("46_dilated.png")
    more_dilated_image.save("46_dilated_2.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
