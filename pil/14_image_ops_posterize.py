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

from PIL import Image, ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    test_image.show()

    for bits in range(8, 0, -1):
        modified_image = ImageOps.posterize(test_image, bits)
        modified_image.show()

except Exception as e:
    print(e)
