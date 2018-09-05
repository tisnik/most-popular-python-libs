#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

    # vzorek pro LUT
    patterns = ["1:(1)->0",
                "1:(0)->1"]

    # vytvoření objektu pro morfologické operace
    lutBuilder = ImageMorph.LutBuilder(patterns=patterns)
    lut = lutBuilder.build_lut()
    
    # aplikace morfologické operace
    morphOp = ImageMorph.MorphOp(lut=lut)
    pixels, updated_image = morphOp.apply(test_image)

    # zobrazení původního i upraveného obrázku
    test_image.show()
    updated_image.show()

    # uložení původního i upraveného obrázku
    test_image.save("42_bitmap.png")
    updated_image.save("42_updated.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
