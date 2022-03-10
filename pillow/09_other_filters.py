#!/usr/bin/env python3
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

from PIL import Image, ImageFilter

filename = "Lenna.png"

IMAGE_FILTERS = (
    ImageFilter.BLUR,
    ImageFilter.CONTOUR,
    ImageFilter.DETAIL,
    ImageFilter.EDGE_ENHANCE,
    ImageFilter.EDGE_ENHANCE_MORE,
    ImageFilter.EMBOSS,
    ImageFilter.FIND_EDGES,
    ImageFilter.SHARPEN,
    ImageFilter.SMOOTH,
    ImageFilter.SMOOTH_MORE,
)


def print_image_info(image):
    print("Format:     {fmt}".format(fmt=image.format))
    size = image.size

    print("Resolution: {width}x{height} px".format(width=size[0], height=size[1]))

    print("Mode:       {mode}".format(mode=image.mode))


def apply_filter_and_save_image(image, prefix, image_filter):
    filter_name = image_filter.__name__.lower()
    print("Applying filter {filter_name}".format(filter_name=filter_name))

    filename = "{prefix}{filter_name}.png".format(
        prefix=prefix, filter_name=filter_name
    )

    filtered_image = image.filter(image_filter)
    filtered_image.save(filename)


try:
    test_image = Image.open(filename)
    test_image.load()

    print("Original:")
    print_image_info(test_image)

    for image_filter in IMAGE_FILTERS:
        apply_filter_and_save_image(test_image, "Lenna_", image_filter)

except Exception as e:
    print("An exception:")
    print(e)
