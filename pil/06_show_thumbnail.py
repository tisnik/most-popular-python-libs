#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

thumbnail_size = 128, 128


def print_image_info(image):
    print("Format:     {fmt}".format(fmt=image.format))
    size = image.size

    print("Resolution: {width}x{height} px".format(width=size[0],
                                                   height=size[1]))

    print("Mode:       {mode}".format(mode=image.mode))


try:
    test_image = Image.open(filename)
    test_image.load()

    print("Original:")
    print_image_info(test_image)
    print()

    test_image.thumbnail(thumbnail_size)

    print("Thumbnail:")
    print_image_info(test_image)

    test_image.show()

except Exception as e:
    print(e)
