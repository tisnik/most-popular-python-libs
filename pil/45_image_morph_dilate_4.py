#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageMath
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

    lutBuilder = ImageMorph.LutBuilder(patterns=["4:(... .0. .1.)->1"])

    # vytvoření objektu pro morfologické operace
    lut = lutBuilder.build_lut()
    morphOp = ImageMorph.MorphOp(lut=lut)

    # aplikace morfologické operace
    pixels, dilated_image = morphOp.apply(test_image)
    print(pixels)
    
    # aplikace morfologické operace
    pixels, more_dilated_image = morphOp.apply(dilated_image)
    print(pixels)

    # zobrazení původního i upraveného obrázku
    test_image.show()
    dilated_image.show()
    more_dilated_image.show()

    # uložení původního i upraveného obrázku
    test_image.save("45_bitmap.png")
    dilated_image.save("45_dilated.png")
    more_dilated_image.save("45_dilated_2.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
