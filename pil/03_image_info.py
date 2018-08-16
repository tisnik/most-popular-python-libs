#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    print("Image loaded")
    print("Format:     {fmt}".format(fmt=test_image.format))

    size = test_image.size
    print("Resolution: {width}x{height} px".format(width=size[0],
                                                   height=size[1]))

    print("Mode:       {mode}".format(mode=test_image.mode))

except Exception as e:
    print(e)
